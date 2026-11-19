# Test evidence: validator.py

Run from the folder containing the files (Git Bash):
```bash
python3 validator.py <file>; echo "Exit code: $?"
```

| # | File | What it tests | Output | Exit code | Result |
|---|---|---|---|---|---|
| 1 | `valid.env.example` | All four rules satisfied | `Configuration accepted` | 0 | ✅ Accepted |
| 2 | `messy.env` | Original broken file | `APP_PORT is not an integer`<br>`DEBUG must be false`<br>`DB_PASSWORD is missing or empty` | 1 | ❌ Rejected |
| 3 | `bad-port.env.example` | `APP_PORT=80` (below 1024) | `APP_PORT is not in the valid range 1024..65535` | 1 | ❌ Rejected |
| 4 | `no-host.env.example` | `DB_HOST` line removed | `DB_HOST is missing or empty` | 1 | ❌ Rejected |

**Secret check:** the password value (`example-only-placeholder`) does not appear in any output. Errors name the key `DB_PASSWORD` only.

**Note:** in `messy.env`, `dbhost=localhost` is ignored because the contract requires `DB_HOST`, which is present (`DB_HOST=db`).