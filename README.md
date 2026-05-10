# Brute Force — Password Attack PoC

> **Educational project.** All testing was performed against a dedicated lab server (chocolate.cyber.org.il) set up for this exercise.

A Python proof-of-concept demonstrating how constrained password policies make brute-force attacks viable. Given a known username and password length, the script systematically tests all valid combinations until it finds the correct credential.

---

## How it works

The target enforces a specific constraint: each digit in the 4-character password must be **greater than or equal to the next** (non-increasing order). This dramatically reduces the search space from 10,000 to 715 combinations.

For each candidate password the script:
1. Generates the password string via `helper.get_password()`
2. Tests it against the target using `helper.check_password_correct()`
3. On match — reports the password and its **strength rating**

### Strength classification

| Pattern | Strength |
|---|---|
| All digits identical (e.g. `3333`) | 50 |
| Sequential digits (e.g. `4321`) | 60 |
| Two distinct digits (e.g. `3311`) | 70 |
| Other valid combinations | 100 |

---

## Key takeaway

When password length is known and character constraints are narrow, brute-force becomes trivial even without GPU acceleration. This demonstrates why **password policies must enforce complexity, not just length**.

---

## Tech stack

Python · HTTP requests · Combinatorics · Authentication testing
