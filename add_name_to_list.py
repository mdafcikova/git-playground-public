from pathlib import Path

participants = Path("PARTICIPANTS.md")
name = "AI generated cybernetic humanoid"

existing_text = participants.read_text(encoding="utf-8")
with participants.open("a", encoding="utf-8") as fh:
    prefix = "" if not existing_text or existing_text.endswith("\n") else "\n"
    fh.write(f"{prefix}{name}\n")
