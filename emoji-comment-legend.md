# Emoji Comment Legend (Class Standard)

We use emojis in comments as *scannable signposts*.

- Students are **not required** to use emojis.
- If you do use them, **use them consistently** so your code is easier to skim.
- Emoji comments should explain **intent** (what/why), not repeat the code (how).

## Legend

| Emoji | Use for | Example (Python comment) |
|------:|---------|---------------------------|
| 📌 | Constants / important fixed values | `# 📌 CONSTANTS` |
| 🧠 | Planning / algorithm steps (stubs) | `# 🧠 Plan: ask → validate → store → return` |
| ✅ | Goal / expected result / return value | `# ✅ Return: employee_id (int)` |
| ⚠️ | Warnings / common beginner mistakes | `# ⚠️ Don't confuse = with ==` |
| 💡 | Tips / helpful hints / shortcuts | `# 💡 tip: use .strip() to remove extra spaces` |
| ℹ️ | Quick info / vocabulary / definitions | `# ℹ️ info: tuples are fixed-size collections` |
| 💾 | Saving / files / persistence | `# 💾 Save the updated order to the file` |
| ▶️ | Entry point / where the program starts | `# ▶️ Start the program by calling main()` |
| 🧪 | Testing / example inputs & expected outputs | `# 🧪 Test: input 3 → output "Large"` |
| 🖨️ | Output / printing / display formatting | `# 🖨️ Display the receipt neatly` |
| 🛡️ | Safety / error handling / try-except | `# 🛡️ Catch bad input so the program doesn't crash` |
| 📁 | Files / data structure location / storage ideas | `# 📁 Data file format: id,name,room,ext` |

## Pattern for stub functions (recommended)

When planning a function that is not implemented yet, use this structure:

```python
def some_function(inputs):
    # 🧠 STEP X: short name of the job
    # Plan:
    # 1) ...
    # 2) ...
    # ✅ Return: what this function gives back
    pass
```

## Rules of thumb

- Keep comments short; prefer 1–5 lines per idea.
- Put the emoji at the start of the comment line for easier scanning.
- Use **✅ Return** to define what type/shape comes back (int, str, list, dict, etc.).
- Use **⚠️** only for real pitfalls students repeatedly hit.

