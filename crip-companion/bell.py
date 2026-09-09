#!/usr/bin/env python3
"""bell.py: the ringer for the Crip Companion.

One script, three jobs:

  bell.py due          print the bell that is currently due, as a stable block
                       of text. Output only changes when a new bell comes due,
                       so a cron monitor can hash it and wake the companion
                       exactly once per bell.
  bell.py hold ITEM    Sparrow said "not yet" to ITEM. Remember it.
  bell.py done ITEM    ITEM happened. Forget it.
  bell.py held         list what is being held.

State lives in held.json next to this file (gitignored). Templates live in
bells/*.yaml. No LLM in here; this is the clock and the memory. The voice is
the companion's.
"""
import json, sys, datetime, pathlib
try:
    import yaml
except ImportError:
    sys.exit("bell.py needs pyyaml: pip3 install pyyaml")

HERE = pathlib.Path(__file__).resolve().parent
BELLS = HERE / "bells"
HELD = HERE / "held.json"
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MEDS = {"morning_meds", "second_dose", "night_meds", "night_meds_packed"}


def load_templates():
    out = {}
    for p in sorted(BELLS.glob("*.yaml")):
        d = yaml.safe_load(p.read_text())
        for day in d.get("applies", []):
            out[day] = d
    return out


def read_held():
    if HELD.exists():
        try:
            return json.loads(HELD.read_text())
        except json.JSONDecodeError:
            pass
    return {"items": []}


def write_held(state):
    HELD.write_text(json.dumps(state, indent=2) + "\n")


def hhmm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def current_bell(now=None):
    now = now or datetime.datetime.now()
    day = DAYS[now.weekday()]
    tpl = load_templates().get(day)
    if not tpl:
        return day, None, None
    minutes = now.hour * 60 + now.minute
    quiet = hhmm(tpl.get("quiet_after", "22:00"))
    due = None
    for b in tpl["bells"]:
        if hhmm(b["at"]) <= minutes:
            due = b
    if minutes >= quiet:
        return day, tpl, None
    return day, tpl, due


def cmd_due():
    now = datetime.datetime.now()
    day, tpl, bell = current_bell(now)
    today = now.date().isoformat()
    if tpl is None:
        print(f"no template for {day}")
        return
    if bell is None:
        print(f"{today} {tpl['day_type']}: no bell due (before lauds or after quiet hours)")
        return
    state = read_held()
    held_today = [h for h in state["items"] if h["day"] == today]
    lines = [
        f"BELL {bell['name'].upper()} · {today} · {tpl['day_type']} · rings at {bell['at']}",
        "",
        "say (in your own words, this is the gist, not a script):",
        f"  {bell['says'].strip()}",
        "",
        "asks: " + ", ".join(bell.get("asks", [])),
    ]
    if held_today:
        lines.append("still held from earlier today (ask once, in passing): "
                     + ", ".join(f"{h['item']} (since {h['bell']})" for h in held_today))
    if bell.get("note"):
        lines += ["", "note: " + bell["note"].strip()]
    lines += ["", f"stop word: {tpl.get('stop_word', '🦇')}   quiet after: {tpl.get('quiet_after', '22:00')}"]
    print("\n".join(lines))
    # Compline clears everything except meds. Do it here so the next day starts clean.
    if bell["name"] == "compline":
        keep = [h for h in state["items"] if h["item"] in MEDS and h["day"] == today]
        if len(keep) != len(state["items"]):
            write_held({"items": keep})


def cmd_hold(item):
    now = datetime.datetime.now()
    day, tpl, bell = current_bell(now)
    state = read_held()
    today = now.date().isoformat()
    state["items"] = [h for h in state["items"] if not (h["item"] == item and h["day"] == today)]
    state["items"].append({"item": item, "day": today, "bell": bell["name"] if bell else "none",
                           "at": now.strftime("%H:%M")})
    write_held(state)
    print(f"holding {item}")


def cmd_done(item):
    state = read_held()
    before = len(state["items"])
    state["items"] = [h for h in state["items"] if h["item"] != item]
    write_held(state)
    print(f"done {item}" if len(state["items"]) < before else f"{item} was not held")


def cmd_held():
    state = read_held()
    if not state["items"]:
        print("nothing held")
    for h in state["items"]:
        print(f"{h['item']}  (not yet at {h['bell']}, {h['day']} {h['at']})")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "due":
        cmd_due()
    elif args[0] == "hold" and len(args) > 1:
        cmd_hold(args[1])
    elif args[0] == "done" and len(args) > 1:
        cmd_done(args[1])
    elif args[0] == "held":
        cmd_held()
    else:
        print(__doc__)
        sys.exit(1)
