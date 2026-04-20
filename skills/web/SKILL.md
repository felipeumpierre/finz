---
name: web
description: >
  Build the local Astro-based web dashboard that visualizes workspace/*.json
  data and open it in the user's default browser. Use this skill on any
  invocation of /finz:web. The site is read-only; the data comes from
  workspace files already produced by other finz skills.
---

# finz web dashboard — build & open

You are responsible for running the local web dashboard. The dashboard is a
static Astro site under `web/` in the plugin repo. It reads `workspace/*.json`
at build time and outputs `web/dist/`.

## Important rules

- English only, same as the rest of finz.
- The site is read-only. If the user asks to edit data, direct them to the
  appropriate `/finz:*` skill.
- Never commit `web/dist/` or `web/node_modules/` — both are gitignored.

## Workflow

### Step 1: Locate the web directory

The plugin root contains a `web/` directory alongside `commands/`, `skills/`,
and `workspace/`. Work from the plugin root for all commands.

### Step 2: Install dependencies if needed

Check for `web/node_modules/`. If it does not exist, run:

```bash
cd web && bun install
```

Expected: dependencies install, no errors. First run takes ~5–45 seconds
depending on network.

### Step 3: Build the site

Run:

```bash
cd web && bun run build
```

Expected: `web/dist/index.html` is created. Build time is typically under 2
seconds with cached dependencies.

If the build fails, report the error to the user. Common causes:

- A state file in `workspace/` has malformed JSON → fix the file.
- A required TypeScript type has drifted from the real JSON shape → update
  `web/src/lib/types.ts`.

### Step 4: Open the dashboard

On macOS:

```bash
open web/dist/index.html
```

On Linux:

```bash
xdg-open web/dist/index.html
```

On Windows:

```bash
start web/dist/index.html
```

Detect the platform from `uname -s`. If unsure, print the absolute path of
`web/dist/index.html` and ask the user to open it manually.

### Step 5: Tell the user what they have

After opening the browser, print a one-line summary:

> "Dashboard is open. Six pages: Overview, Cash, Portfolio, Insurance, Tax,
> Crypto. Run /finz:web again after any /finz:* command that writes state."

## Failure modes

- `bun` not found → tell the user to install Bun (`curl -fsSL https://bun.sh/install | bash`) and retry.
- `workspace/` missing or empty → the dashboard still builds and shows empty-state cards on each page with the exact `/finz:*` command to run. Tell the user to run `/finz:profile setup` first if they have no data at all.
- Port conflict / existing dev server → not applicable, we build static output.

## Do not

- Start `bun dev`. Always use `bun run build`.
- Modify files in `workspace/`. This skill is read-only.
- Commit `web/dist/`.
