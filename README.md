# [mCoding] All Dunders Video

## Contributing

If you'd like to add a code example, make sure it has not already been done or
is in progress (see the [spreadsheet] or the [Issues tab] for reference). Once
you have confirmed that, open an issue for the dunder(s) you'd like to add
examples for. When you're done, simply make a PR!

Each PR is required to have 3 approving reviews in order to be merged, and
anyone is free to review, so your approval counts!

### Submission guidelines
* The code has to be [PEP8]-compliant and lines must be at most 80 chars long
* Typehints are not necessary (unless needed for the example to work)
* Be consistent about typehints: either do them properly or don't include them
  at all
* Examples can include multiple dunders if they go together
* The code should be a minimal working example that uses the dunder(s)

When submitting code for the `__cool_dunder__` dunder, name the file
`cool_dunder.py` (basically strip the underlines). When submitting multiple
dunders in one example, you can:
* use the dunder name that's the most important/widely used, e.g. `name.py` when
  adding `__name__` and `__qualname__`
* use a name that easily describes all of them, e.g. `comparisons.py` when
  adding `__gt__`, `__le__`, etc.

The file should be put in the corresponding folder inside `src`, e.g. a
`__post_init__` example should be located in `src/library-lagoon/post_init.py`
(see categories in the [spreadsheet]).

Your code must pass CI. To check if your code will pass CI locally run these
commands:
```
pip install -r requirements.txt
black --check .
ruff check .
```
You can also apply fixes if these checks don't pass:
```
black .
ruff check . --fix
```

### Giveaway
Everyone who contributes a dunder before **July 23** is entered into the
giveaway for Discord Nitro or a JetBrains license. All entrants have the same
chances regardless of how many dunders they have added. However, the
winners with the highest number of contributions have priority and can choose
their prize.

| Prize Pool                   |
| ---                          |
| **2x** 1-Month Discord Nitro |
| **1x** 1-Year Discord Nitro  |
| **2x** JetBrains License     |

*The giveaway was funded by @mcoding and @pi3014 on Discord :heart:*

## Credits

People who have contributed at least 1 dunder or have reviewed at least 2 PRs
are eligible for the **Volunteer** role on [the mCoding server].

Big thanks to everybody who contributed with code examples or code reviews:
- [@CircuitSacul](https://github.com/CircuitSacul)
- [@edsaac](https://github.com/edsaac)
- [@Endercheif](https://github.com/Endercheif)
- [@FuexFollets](https://github.com/FuexFollets)
- [@Lunarmagpie](https://github.com/Lunarmagpie)
- [@MicaelJarniac](https://github.com/MicaelJarniac)
- [@MithicSpirit](https://github.com/MithicSpirit)
- [@qexat](https://github.com/qexat)
- [@trag1c](https://github.com/trag1c)

[Issues tab]: https://github.com/trag1c/mcoding-all-dunders/issues
[mCoding]: https://www.youtube.com/@mCoding
[the mCoding server]: http://mcoding.io/discord
[PEP8]: https://peps.python.org/pep-0008/
[spreadsheet]: https://docs.google.com/spreadsheets/d/1-45UeKKMCePmTDLptT2zpI4L-jikmsCnve_lwOMyeuY/edit?usp=sharing
