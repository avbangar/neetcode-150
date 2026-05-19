import os
import re
from pathlib import Path

TOTAL_PROBLEMS = 150
SOLUTIONS_DIR = "./solutions"
README_PATH = "./README.md"


def count_solutions(directory):
    """Counts all Python files in the solutions directory."""
    path = Path(directory)
    if not path.exists():
        return 0

    solutions = [file for file in path.rglob("*.py")]
    return len(solutions)


def generate_progress_bar(completed, total, bar_length=20):
    """Generates a markdown progress bar."""
    percentage = (completed / total) * 100
    filled_length = int(bar_length * completed // total)

    # █ for completed, ░ for remaining
    bar = "█" * filled_length + "░" * (bar_length - filled_length)

    return f"**{completed}/{total}** completed ({percentage:.2f}%)\n\n`[{bar}]`"


def update_readme(progress_text):
    """Injects the progress text between the HTML markers in the README."""
    with open(README_PATH, "r") as file:
        readme_content = file.read()

    # Regex to find the tags and replace everything in between them
    pattern = r"(\n).*?(\n)"
    replacement = rf"\g<1>{progress_text}\g<2>"

    updated_content = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)

    with open(README_PATH, "w") as file:
        file.write(updated_content)


if __name__ == "__main__":
    completed_count = count_solutions(SOLUTIONS_DIR)
    progress_bar = generate_progress_bar(completed_count, TOTAL_PROBLEMS)

    update_readme(progress_bar)
    print(f"Success! Updated README to {completed_count}/{TOTAL_PROBLEMS}.")
