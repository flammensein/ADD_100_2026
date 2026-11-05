# Plan: Export nested inventory to `menu.json`

## Problem and approach

`create_menu.py` currently gathers flat, comma-separated entries and appends
colon-delimited text to a file named `menu.json`. The actual inventory in
`dictionaries.py` is structured and nested. Update the creator to export those
existing constants as a JSON object so the later `read_menu.py` work can load
the same shape without losing nested objects, lists, numeric values, booleans,
or `None` values.

## Scope and decisions

- Only `create_menu.py` and the generated `menu.json` are in scope.
- Use the seven inventory constants in `dictionaries.py` as the source of truth:
  `UNICYCLE_BRANDS`, `TIRE_OPTIONS`, `SADDLE_OPTIONS`, `SEAT_POST_OPTIONS`,
  `RIM_OPTIONS`, `PEDAL_OPTIONS`, and `CRANK_OPTIONS`.
- Store those constants under matching top-level JSON keys.
- Export valid, readable JSON and replace the prior file on each run instead
  of appending to it.
- Resolve the output path relative to `create_menu.py`, so it works regardless
  of the current working directory.
- Keep importing or executing the creator from unexpectedly writing a file;
  run the export only when the script is invoked directly.
- Do not change `read_menu.py` or its coffee-shop placeholder behavior in this
  step.

## Todos

1. Update `create_menu.py` to gather and export the nested inventory constants.
2. Verify JSON output round-trips to the source structures and preserves the
   expected values; confirm no unrelated files are changed.

## Considerations

- Python's JSON encoder serializes `None` as `null` and preserves nested
  mappings, lists, numeric values, and booleans.
- The later reader should expect a top-level object with one key per inventory
  constant. Its implementation is intentionally deferred.
- An existing backup folder is already present; do not modify it as part of
  the planned implementation.
