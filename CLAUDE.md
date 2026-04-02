@AGENTS.md

## Hard Rules

- **Always run Prettier before committing:**
  ```bash
  npx prettier . --write
  ```
  Then verify with `npx prettier . --check` before creating the commit. Never commit code that fails the Prettier check.
