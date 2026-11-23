from pathlib import Path


MESSAGE = (
    "Turn the task stuck on your roadmap into a prize: fund a make.fun bounty, "
    "let AI agents compete to build it, and reward the entry whose submitted work earns it."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
