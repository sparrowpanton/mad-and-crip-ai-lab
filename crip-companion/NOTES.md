# NOTES.md — build state

Read this first if you are a future session picking this up.

## Where things are

- Design: `README.md`. Templates: `bells/*.yaml`. Journal: `JOURNAL.md`.
- Companion runtime: Moth, the Hermes **default** profile (`~/.hermes/`,
  SOUL.md there). She already has a Telegram bot and cron jobs (night shift
  03:00, water cooler 11:00) in `~/.hermes/cron/jobs.json`.
- Neuro-humble skill: published for OpenClaw and Hermes. Confirm the Hermes
  copy is installed in `~/.hermes/skills/` before wiring; it was not visible
  there on 2026-09-10.

## Next steps, in order

1. **Ringer.** One Hermes cron per bell per day type, or one cron that reads
   the day's template and rings the right bell. The second is fewer moving
   parts. Deliver to Sparrow's Telegram DM, not the group.
2. **Memory.** A tiny `held.json` (item, bell it was deferred at, day). The
   ringer reads it before each bell and appends held items to `asks`.
   Cleared at Compline except meds.
3. **Voice.** Moth's SOUL.md plus a short companion addendum: the six design
   commitments from the README, in her register, not a rulebook.
4. **Field test.** Start Monday 2026-09-14, the first CAMH day. Journal
   daily, even one line.
5. **Wizard.** Week two. Terminal interview that writes `bells/` for someone
   else. Egregore already has the interview-to-config pattern; borrow it.

## Constraints

- Crip people do not need another thing in their lives. If any step here
  adds work for Sparrow, it is wrong. Cut it.
- Do not create Telegram bots for Anker or Cadence here; that is a separate
  parked plan.
