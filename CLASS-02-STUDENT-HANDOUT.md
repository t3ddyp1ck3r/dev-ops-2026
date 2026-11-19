# Class 2 — Configuration validation and Git review

## What you are building

You are a developer asked to stop unsafe application configuration *before deployment*. You will repair a configuration example, **complete the unfinished Python validator**, prove that it accepts good settings and rejects bad settings, then ask a classmate to review your work. You are **not** expected to start the Flask app or connect to a real database.

By the end, you should be able to say: “My script reads an `.env` file, checks our four required settings, prints useful error messages without exposing passwords, and returns a failure status when the settings are invalid.”

## First, understand the four rules

| Key | Required behavior | Example |
|---|---|---|
| `APP_PORT` | Whole number between 1024 and 65535, inclusive | `APP_PORT=8080` |
| `DEBUG` | Must be exactly `false` (for this exercise) | `DEBUG=false` |
| `DB_HOST` | Must be present and nonempty | `DB_HOST=db` |
| `DB_PASSWORD` | Must be present and nonempty; **never display its value** | `DB_PASSWORD=example-only-placeholder` |

`dbhost` is a differently named legacy key: it does **not** satisfy the `DB_HOST` requirement. Avoid copying any actual credentials into this exercise.

## Step 1 — Inspect the supplied broken configuration (10 minutes)

Open `messy.env` in a text editor. On paper or in `findings.md`, answer:

1. Which entry has an invalid data type?
2. Which entry violates the deployment debug policy?
3. Which required setting is empty?
4. Which two names appear to represent the same concept, and which spelling does the contract require?

**Checkpoint:** Your findings should identify `APP_PORT`, `DEBUG`, `DB_PASSWORD`, and `dbhost` versus `DB_HOST`.

## Step 2 — Inspect the unfinished code (10 minutes)

Open `validator.py`. The `load(path)` function already reads `KEY=value` lines into a dictionary. The `validate(values)` function is **deliberately incomplete** and currently raises `NotImplementedError`. **Your job is to implement `validate`; do not delete the provided loader or main block.**

Run from the directory containing the files:

```bash
python3 validator.py messy.env
```

On Windows use `py validator.py messy.env` if `python3` is not available. **Expected *before implementation*:** an error mentioning `NotImplementedError`. That is intentional, not a passed test.

## Step 3 — Write the configuration validator (25 minutes)

Replace the TODOs in `validate(values)` with checks for the four rules in the table. The function must **return a list of error strings** (empty if valid). Every error should identify the field name and the problem, but **must not include the password value**. You can use `values.get("APP_PORT", "")` and `int(...)` inside `try/except ValueError` to check the port.

**Checkpoint:** Re-run:

```bash
python3 validator.py messy.env
```

You should now see messages about the invalid port, debug setting, and missing password (wording may differ). It should **not** print `Configuration accepted`.

## Step 4 — Create a valid example (10 minutes)

Create `valid.env.example` containing only **dummy** values:

```ini
APP_PORT=8080
DEBUG=false
DB_HOST=db
DB_PASSWORD=example-only-placeholder
```

Do not commit a real `.env` file with production or personal passwords. The `.example` extension indicates a template, not a secret-bearing deployment configuration.

Run:

```bash
python3 validator.py valid.env.example
```

**Expected:** `Configuration accepted` and process exit code `0`.

## Step 5 — Run negative tests and capture exit codes (20 minutes)

Test the supplied `messy.env` and at least two additional *different* defects. Start by copying `valid.env.example` to `bad-port.env.example`; change the port to `80`. For another file, remove `DB_HOST` or set `DEBUG=true`. Test each file.

```bash
python3 validator.py messy.env
 echo "Exit code: $?"
python3 validator.py valid.env.example
 echo "Exit code: $?"
```

In **PowerShell**, use `$LASTEXITCODE` instead of `$?` (which is not the numeric process exit code):

```powershell
py validator.py messy.env
$LASTEXITCODE
py validator.py valid.env.example
$LASTEXITCODE
```

**Expected:** invalid files return exit code `1` (or another nonzero status); the valid file returns `0`. Capture the output and status for each case in `test-evidence.md` or screenshots. Check that no password values appear in error output.

## Step 6 — Share and review with Git (25 minutes)

Use your **own repository**, not a shared working tree. From the repository root:

```bash
git switch -c class02-config-validator
git status
git add validator.py valid.env.example findings.md test-evidence.md
git commit -m "Validate application configuration"
```

Adjust paths if your files are inside `lab/classwork/`. If `git switch` reports that the directory is not a Git repository, ask the instructor for the course repository setup; do not initialize a repository in the wrong folder.

Ask a peer to reproduce one *negative* test. The reviewer should leave one meaningful written comment (for example, an untested boundary condition), then you should respond with a code or test improvement and a second commit. A GitHub pull request is welcome but **not required** if the class has no remote repository; a local diff and dated review comment are acceptable.

## Step 7 — Submit your evidence (15 minutes)

Submit:

1. `validator.py` with the completed `validate()` function.
2. `findings.md` listing the defects in `messy.env` and four validation rules.
3. `valid.env.example` with dummy values only.
4. `test-evidence.md` showing **one successful and at least three failed cases** with their exit codes (the original broken file can be one failed case).
5. Your Git branch/commits and a peer review comment with your response.

## What a pass looks like

| Criterion | Points |
|---|---:|
| Correctly explains the configuration contract and original defects | 2 |
| Validator passes the good file, rejects three bad cases, and produces correct exit codes | 3 |
| No real secrets committed or exposed in outputs; password errors name the key, not its value | 2 |
| Another student can reproduce your tests using your instructions | 1 |
| Meaningful peer feedback plus a follow-up improvement | 2 |
| **Total** | **10** |

**Pass:** 8/10 or higher, **and** any real secret exposure must be fixed. A script that still raises `NotImplementedError` cannot pass.


## Folder setup (read before running commands)

Your instructor will supply a student folder containing `validator.py`, `messy.env`, and `valid.env.example`. Open a terminal **inside that folder**. You do not need to run `app.py` or Docker in this class.

If you do not already have a personal Git repository, you may initialize a **local practice repository** inside your own Class 2 folder:

```bash
git init
git add validator.py valid.env.example
git commit -m "Add Class 2 starter files"
```

Only do this after confirming the directory contains **no real credentials** and that your Git name/email have been configured. The Git branch commands in Step 6 run from this directory. If the instructor gives you a course repository, use that instead: do not initialize a nested repository.

