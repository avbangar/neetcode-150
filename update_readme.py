import os
from pathlib import Path

TOTAL_PROBLEMS = 150
SOLUTIONS_DIR = "./solutions"
README_PATH = "./README.md"

def count_solutions(directory):
    """Counts all Python and Swift files in the solutions directory."""
    path = Path(directory)
    if not path.exists():
        return 0

    # Look for both extensions and combine the results
    py_files = list(path.rglob("*.py"))
    swift_files = list(path.rglob("*.swift"))
    
    all_solutions = py_files + swift_files
    return len(all_solutions)


def generate_progress_bar(completed, total, bar_length=30):
    """Generates a markdown progress bar using colored emojis."""
    percentage = (completed / total) * 100
    filled_length = int(bar_length * completed // total)

    # 🟩 for completed, ⬜ for remaining
    bar = "🟩" * filled_length + "⬜" * (bar_length - filled_length)

    # Removed the backticks `[ ]` because emojis look better without them
    return f"**{completed}/{total}** completed ({percentage:.2f}%)\n\n{bar}"


def rewrite_readme(progress_text):
    """Rewrites the entire README from scratch using a template."""

    # This is the exact text that will become your README
    # We inject the progress_text directly into it using the f-string
    readme_content = f"""# My NeetCode 150 Journey
Having a bit of fun and testing my basics.
This repository contains my solutions to the NeetCode 150.

### Current Progress
{progress_text}
"""

    # Opening in "w" mode completely overwrites the file
    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)


if __name__ == "__main__":
    completed_count = count_solutions(SOLUTIONS_DIR)
    progress_bar = generate_progress_bar(completed_count, TOTAL_PROBLEMS)

    rewrite_readme(progress_bar)
    print(f"Success! Rebuilt README with {completed_count}/{TOTAL_PROBLEMS}.")
