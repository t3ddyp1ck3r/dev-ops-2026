# Findings: messy.env

## Defects found
1. **Invalid data type:** `APP_PORT=hello` is text, but the port must be a whole number.
2. **Debug policy violation:** `DEBUG=true`, but deployment requires `DEBUG=false`.
3. **Empty required setting:** `DB_PASSWORD=` has no value.
4. **Duplicate concept, wrong name:** `dbhost=localhost` and `DB_HOST=db` both describe the database host. The contract requires `DB_HOST`; `dbhost` is a legacy key and is ignored.

## Validation rules
| Key | Rule |
|---|---|
| APP_PORT | Whole number from 1024 to 65535 (inclusive) |
| DEBUG | Exactly `false` |
| DB_HOST | Present and nonempty |
| DB_PASSWORD | Present and nonempty; its value is never displayed |