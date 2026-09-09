# NOTES.md — build state

Read this first if you are a future session picking this up.

## Where things are

- Design: `README.md`. Templates: `bells/*.yaml`. Journal: `JOURNAL.md`.
- Companion runtime: Moth, the Hermes **default** profile (`~/.hermes/`,
  SOUL.md there). She already has a Telegram bot and cron jobs (night shift
  03:00, water cooler 11:00) in `~/.hermes/cron/jobs.json`.
- Neuro-humble skill: published for OpenClaw and Hermes. Confirm the Hermes
  copy is installed in `~/.hermes/skills/` before wiring; it was not visible
  there on 2026-09-09.

## Wired on 2026-09-09
- Hermes cron `Crip Companion bells` (id 0b39547b74fd) on Moth's default
  profile: every 10 min, monitor-script `~/.hermes/scripts/crip-bell.sh`,
  delivers to Sparrow's Telegram DM. `hermes cron list` to see it,
  `hermes cron pause 0b39547b74fd` to silence it.
- MOTH.md appended to `~/.hermes/SOUL.md` (backup in `~/.hermes/soul_backups/`).
- neuro-humble installed at `~/.hermes/skills/domain/neuro-humble`.
- All three Hermes profiles locked to Sparrow's Telegram id
  (`GATEWAY_ALLOW_ALL_USERS=false`, `TELEGRAM_ALLOWED_USERS` set). Before
  this, the bots were open to anyone on Telegram. Never turn that back on.

## Next steps, in order

1. **Ringer.** `bell.py` (done). `bell.py due` prints the bell that is
   currently due as a stable block; a Hermes cron with `--monitor-script`
   every 10 minutes hashes that output and wakes Moth exactly once per bell.
   Wrapper at `~/.hermes/scripts/crip-bell.sh`. Deliver to Sparrow's
   Telegram DM (`telegram:<her id>`), never the group.
2. **Memory.** `held.json` (done, gitignored). `bell.py hold ITEM` when she
   says "not yet", `bell.py done ITEM` when it happened. `due` appends held
   items to the bell. Compline clears everything except meds.
3. **Voice.** Moth's SOUL.md plus a short companion addendum: the six design
   commitments from the README, in her register, not a rulebook.
4. **Field test.** Started 2026-09-10 (Luther Thursday). The semester
   proper starts Monday 2026-09-14. Journal daily, even one line.
   Known rough edge: templates assume the Waterloo hotel on Wed/Thu; the
   first week she is elsewhere. Moth has the gist, not a script.
5. **Wizard.** Week two. Terminal interview that writes `bells/` for someone
   else. Egregore already has the interview-to-config pattern; borrow it.

## Constraints

- Crip people do not need another thing in their lives. If any step here
  adds work for Sparrow, it is wrong. Cut it.
- Do not create Telegram bots for Anker or Cadence here; that is a separate
  parked plan.
