# bells/

One file per day type. Each file is the whole day: seven bells, the time each
rings, what the companion is for at that bell, and what she should hold if
the answer is "not yet."

These are written for one specific person and one specific semester (fall
2026). That is deliberate. The wizard, when it exists, will write files in
this same shape for other people. Until then, edit these by hand.

The templates say "your person" where a real name goes, and "second dose"
where a medication goes. Keep it that way in this repo. Names and meds are
yours; put them in your local copy, not in the public one.

## Shape

```yaml
day_type: camh-day
applies: [monday, friday]
voice: moth
stop_word: "🦇"          # everything stops until the next day
quiet_after: "22:00"     # no bells after this
bells:
  - name: lauds
    at: "07:00"
    says: >
      what she opens with, in her voice
    asks:                # each one can get "yes", "no", "not yet", or silence
      - breakfast
    holds:               # "not yet" answers come back at the next bell
      - breakfast
```

## Rules the ringer follows

- A bell rings once. If there is no reply, she may re-ring once, gently,
  after 20 minutes. Then she is quiet until the next bell.
- "not yet" moves the item into `held`. Held items are asked again at the
  next bell, once, in passing. They are dropped at Compline unless they are
  meds.
- The stop word ends the day. No more bells. She may say one thing:
  that she is here. Then nothing.
- Silence all day is data, not failure. She notices it in the journal,
  not in the chat.
