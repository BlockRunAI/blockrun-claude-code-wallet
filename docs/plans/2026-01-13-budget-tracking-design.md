# Budget Tracking Design

**Date:** 2026-01-13
**Status:** Approved
**Problem:** Spending resets on each session, no budget limits, poor visibility

## Overview

Add persistent spending tracking with budget enforcement at the plugin level. Users can set daily budget limits and see cumulative spending across sessions.

## Data Model

**File:** `~/.blockrun/spending.json`

```json
{
  "session_id": "2026-01-13T17:30:00",
  "budget_limit": 1.0,
  "spending": {
    "total_usd": 0.0234,
    "calls": 12
  },
  "history": [
    {"timestamp": "2026-01-13T17:31:22", "model": "deepseek/deepseek-chat", "cost": 0.0001},
    {"timestamp": "2026-01-13T17:32:45", "model": "openai/gpt-4o", "cost": 0.0012}
  ]
}
```

**Key decisions:**
- Session resets daily (new day = fresh budget)
- Budget limit is optional (`null` means no limit)
- History capped at 100 entries
- Atomic writes (temp file + rename)

## New CLI Flags

```bash
python run.py --set-budget 1.00    # Set $1 daily limit
python run.py --clear-budget       # Remove limit
python run.py --spending           # Show spending summary
```

## SpendingTracker Module

**New file:** `scripts/utils/spending.py`

```python
class SpendingTracker:
    """Persistent spending tracker with budget enforcement."""

    def __init__(self):
        self.file = Path.home() / ".blockrun" / "spending.json"
        self.data = self._load()

    def _load(self) -> dict:
        """Load or create fresh session (resets daily)."""

    def record(self, model: str, cost: float):
        """Record a call and save."""

    def check_budget(self) -> tuple[bool, float]:
        """Returns (within_budget, remaining)."""

    def set_budget(self, amount: float):
        """Set daily budget limit."""

    def clear_budget(self):
        """Remove budget limit."""

    def get_total(self) -> float:
        """Get total spent this session."""

    def get_limit(self) -> float | None:
        """Get current budget limit."""
```

## Integration with run.py

```python
def cmd_chat(prompt, model, ...):
    tracker = SpendingTracker()

    # CHECK BUDGET BEFORE CALL
    within_budget, remaining = tracker.check_budget()
    if not within_budget:
        branding.print_error("Budget limit reached")
        return 1

    # MAKE THE CALL
    response = client.chat(...)

    # RECORD SPENDING
    sdk_spending = client.get_spending()
    tracker.record(model, sdk_spending['total_usd'])

    # SHOW UPDATED FOOTER
    branding.print_footer(
        call_cost=sdk_spending['total_usd'],
        session_total=tracker.get_total(),
        budget_remaining=remaining
    )
```

## Updated Output Format

**Normal footer:**
```
------------------------------------------------------------
  This call: $0.0010
  Session total: $0.0234 (12 calls)
  Budget remaining: $0.9766 of $1.00
  Powered by BlockRun
```

**Budget exhausted:**
```
============================================================
  BUDGET LIMIT REACHED
============================================================
  Spent: $1.0012 across 47 calls
  Limit: $1.00/day

  Options:
    python run.py --set-budget 2.00   # Increase limit
    python run.py --clear-budget      # Remove limit
    (Budget resets tomorrow)
```

**Spending summary (`--spending`):**
```
============================================================
  SPENDING SUMMARY
============================================================
  Today: $0.0234 across 12 calls
  Budget: $1.00 ($0.9766 remaining)

  Recent calls:
    17:31 deepseek/deepseek-chat  $0.0001
    17:32 openai/gpt-4o           $0.0012
    17:35 xai/grok-3              $0.0200
```

## Files to Change

| File | Action | Changes |
|------|--------|---------|
| `scripts/utils/spending.py` | Create | SpendingTracker class (~80 lines) |
| `scripts/run.py` | Modify | Budget check, record spending, new CLI flags |
| `scripts/utils/branding.py` | Modify | Update footer, add spending summary |

## Edge Cases

- **First run:** Creates `~/.blockrun/spending.json` automatically
- **No budget set:** Works as before (no limit enforced)
- **Corrupted file:** Resets to fresh session
- **Concurrent access:** Atomic writes prevent corruption
- **Midnight rollover:** New day starts fresh session

## Testing Plan

1. Test fresh install (no spending.json)
2. Test budget enforcement (set $0.01, make calls until blocked)
3. Test session reset (change system date or wait for midnight)
4. Test --spending output
5. Test --clear-budget removes limit
