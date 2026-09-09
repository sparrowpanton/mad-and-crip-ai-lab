# The Crip Companion

*A Daily Office for executive dysfunction.*

## What this is

Not a reminder app. Every productivity assistant that exists is built on the
neurotypical assumption that the problem is *forgetting*. That is not the
AuDHD problem. The problem is:

- You know you should eat, but the transition from working to kitchen is a wall.
- You have meds, but the sequence of stop, get water, take them, resume does not initiate.
- You can see the calendar, but you cannot feel time moving toward the thing on it.
- You are dehydrated, and you know it, and knowing does not make you get up.

What executive dysfunction needs is not motivation and not reminders. It
needs a bell.

## The frame: the Daily Office

Lauds, Prime, Terce, Sext, None, Vespers, Compline. Seven bells. The monks
do not do Lauds because they are motivated. They do Lauds because it is
Lauds. The bell rings, you show up, and the structure carries you on the
days you cannot carry yourself.

So: a companion (Moth, a Hermes agent, on Telegram) rings seven bells a day.
Each bell is a short check-in in her own voice, shaped to what kind of day
it is. You answer with a word, a 👍, or nothing. She adapts.

## The load-bearing feature: she remembers

You say "not yet" to breakfast at Lauds. She does not let it go. It comes
back at Terce, gently: "hey, did that breakfast ever happen?" Not nagging.
Holding it for you so you do not have to hold it yourself. That is the thing
a calendar cannot do. That is what makes it care.

## Design commitments

1. **Pacing, not productivity.** The bells are transitions, not tasks.
   She walks beside you at the speed you need.
2. **She initiates.** The version where you have to *report* to her is
   another task. She checks in at the right times; you reply or you don't.
3. **Brutally simple.** Crip people do not need another thing in their lives.
   Seven bells, one voice, one memory. Nothing else until that works.
4. **Tone is the product.** Not a drill sergeant, not a worried parent.
   "Did you eat" lands differently than "you should eat." She knows the
   difference.
5. **A bad day is data, not failure.** No reply, or the stop-word, and she
   backs off. One gentle re-ring at most. Then quiet until the next bell.
   The neurotypical version keeps pinging. The crip version knows when to stop.
6. **Neuro-humble underneath.** She runs on the neuro-humble skill: don't
   diagnose, don't fix, don't flatten. Sit with the person.

## The bells, in one sentence each

| Bell | Roughly | What she is for |
|---|---|---|
| Lauds | waking | Breakfast, or stop on the way? Ready to look at the day? |
| Prime | leaving | The door checklist. Meds, food, sunglasses, ear defenders, phone, keys. |
| Terce | mid-morning | Whatever got a "not yet" at Lauds. Water. |
| Sext | noon | Lunch? How are you feeling? How did the morning go? |
| None | 3pm | **The one that saves you.** Coffee. Pee. Second dose. Errands on the way home? Is your person ok? |
| Vespers | commute home | Chit-chat. What needs finishing. What's for dinner. |
| Compline | evening | Tomorrow's shape. Night meds. Go to sleep on time. |

The 3pm bell is the load-bearing one for this particular brain: executive
function is lowest, the morning dose is wearing off, and it is the hour
things quietly do not happen.

## Day types

Monday-Sparrow is not Wednesday-Sparrow. The companion needs to know which
day it is and which version of the day she is in. Templates live in
[`bells/`](bells/), one per day type:

- `camh-day` — Monday and Friday, clinic 8:30 to 4:30, clients and a commute
- `teaching-day` — Tuesday, seventy students, 5 to 8pm
- `luther-wednesday` — drive to Waterloo, class 4 to 6:50, hotel overnight
- `luther-thursday` — class 1 to 3:50, drive home
- `rest-day` — fewer bells, later, gentler

## Making it portable: the wizard

The companion is opinionated about the *approach* (crip-led, neuro-humble,
pacing not productivity) but the content is entirely shaped by the person
using it. So the plan for week two is an interactive setup in the terminal.
Not a form. A conversation.

> When does your day start?
> What does a bad day feel like for you?
> When do you usually forget to eat?
> Do you want me to check on you or leave you alone after 9pm?
> What word do you use when you need everything to stop?

It writes your `bells/` from your answers. Someone else runs the same wizard
and gets a completely different companion, because they have a completely
different brain and a completely different life.

## Status

- **2026-09-08, late** — idea. Named. Framed as the Daily Office.
- **2026-09-09** — scoped. Repo, templates, journal, ringer. Not yet wired to Telegram.

First we build the thing that helps one person survive one semester. Then we
make it portable. Research journal: [`JOURNAL.md`](JOURNAL.md).
