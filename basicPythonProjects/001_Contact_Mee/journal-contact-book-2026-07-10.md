# Contact Book (Python OOP) — July 7–10, 2026

## Goal
Build a Contact Book CLI application in Python to solidify OOP fundamentals (classes, composition, data persistence) before moving on to AI/API work. The principle behind this project: don't mix shaky fundamentals with new AI concepts.

## Progress
All core features are done and working: `add`, `search`, `edit`, `delete`, and JSON persistence (`save()` / load on `__init__`). The project has been committed and pushed to GitHub.

## What I Learned
- **`json.load()` vs `json.loads()`**: `load()` takes a file-like object (something with a `.read()` method) and reads directly from it. `loads()` takes a string that's already been read and parses that instead. The "s" at the end signals "string" — the same pattern applies to `dump()` vs `dumps()`.
- **Composition vs inheritance**: `ContactBook` doesn't inherit from `Contact` — it *has* many `Contact` objects (composition, has-a), not *is* a type of `Contact` (inheritance, is-a). The two ideas got tangled together at first ("Contact will inherit ContactBook"), and it took working through the difference between "is a type of" (inheritance) and "is made up of / contains" (composition) with the phone contacts app analogy before it clicked.
- **Reference vs copy semantics**: when `search()` returns a `Contact` object from `self.contacts`, the returned variable points to the *same* object in memory — not a copy. This is why `edit()` can mutate the object directly through the reference returned by `search()`, and why that change is automatically reflected in `self.contacts` without needing to write it back manually.
- **Two objects with the same value/type are still different objects**: creating two separate variables with identical values (e.g. two `Contact` objects with the same name and number) results in two distinct objects in memory — they're equal in value but not the same object. This is different from assigning one existing variable to another (`b = a`), which doesn't create a new object at all — it just makes `b` a second reference pointing to the exact same object `a` already points to.
- **Python variables are always references, unlike C**: in C, a variable is a memory slot that holds a value directly (`int y = x;` copies the value into a new independent slot). In Python, a variable is always a name pointing to an object — there's no "value vs reference" choice per variable like there is in C (where you'd need an explicit pointer). Assigning `y = x` in Python makes `y` a second name pointing to the *same* object `x` already points to, not a copy. This is easy to miss with immutable types like `int`/`str`, since Python creates a new object on "modification" rather than mutating in place, making it look like a copy happened — but it's clearly visible with mutable objects like `Contact`, where changing an attribute through one name is visible through the other name too.
- **`@classmethod` vs calling the class directly**: `Contact.from_dict(data)` (a classmethod using `cls`) and `Contact(data["name"], data["number"])` (calling the constructor directly) both produce the same result for this project. `from_dict()` only pays off when there are multiple call sites that need to convert a dict into a `Contact` — with only one call site (in `__init__`), calling the constructor directly is just as good and simpler. Recognizing that this specific "best practice" wasn't actually saving effort in this case was part of the learning here.
- **Forgetting to capture a return value**: `Contact.from_dict(contact)` was called without assigning the result to a variable, so the newly created object was discarded — the item later appended to `self.contacts` was still the raw dict from the loop, not the converted object. This produced a `'dict' object has no attribute 'to_dict'` error later in `save()`.

## Biggest Challenge
Not any single bug, but designing the class structure and data relationships — specifically figuring out how `Contact` and `ContactBook` should relate to each other, and initially assuming that relationship had to be inheritance.

## Debugging Story
One bug stood out: contacts kept getting overwritten so that only the most recently added contact was ever saved to `contact.json`. The cause was that `__init__` didn't yet load existing data from the file — so every time the program restarted, `self.contacts` started as an empty list in memory, even though `contact.json` already had contacts saved from a previous run. Adding a new contact and calling `save()` then wrote out only what was in memory (the one new contact), overwriting everything that had been saved before. The fix was to have `__init__` read `contact.json` on startup, convert each stored dict back into a `Contact` object, and append those into `self.contacts` before any new contacts were added.

## Technical Decisions
- Chose composition (`ContactBook` holds a list of `Contact` objects) over inheritance for the `ContactBook`–`Contact` relationship.
- Decided against implementing `from_dict()`/`to_dict()` as a strict rule to always follow — concluded that calling `Contact()` directly is equally valid when there's only one place in the code doing the conversion, and reserved `from_dict()`/`to_dict()`-style patterns for cases with multiple call sites.

## Reflection
Looking back, the plan going forward is to spend more time thinking through class and data structure design before writing code, and to keep working step by step rather than jumping ahead (this came up directly — at one point the load-from-file step was being thought through before `save()` had even been tested and confirmed working).

## Next Steps
Move into the first AI-engineering project: an AI Caption/Hook Generator using the Gemini API (free tier), starting with the underlying concepts — HTTP requests, API keys via environment variables, and calling an LLM API — before touching Gemini directly.

## English Feedback

**Useful technical vocabulary from this session:**
- **"has-a" / "is-a"** — shorthand for composition vs inheritance. Worth keeping these exact phrases in mind; they're commonly used this way in English-language OOP discussions.
- **"reference" vs "copy"** — when explaining this to another English-speaking developer, you'd say "it's a reference to the same object" rather than "it's pointing to" (both work, but "reference" is the more standard term in this context).
- **"call site"** — the place in code where a function/method is called. Useful term for exactly what came up today (deciding between `from_dict()` and calling `Contact()` directly based on how many call sites there are).

**A few natural phrasings for things you described:**
- Instead of "ngedesain data nya, struktur class nya" → in English: "designing the data structure and class relationships" (rather than "the class's structure and its data").
- Instead of "return value dari from_dict yang kelupaan ditampung" → a natural way an English-speaking dev might say this out loud: "I forgot to capture the return value" or "the result just got thrown away since I never assigned it to anything."
- For describing the overwrite bug in standup-style English: "Turns out I wasn't loading existing data on startup, so every save was clobbering the file." ("Clobbering" is a common informal term among engineers for "overwriting destructively.")
