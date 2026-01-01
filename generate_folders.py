# This is a simple program to generate all the folders required for the AOC
from pathlib import Path

def create_structure(advent_of_code_year: int):
    MAIN_FOLDER = Path(f"AOC-{advent_of_code_year}")
    TOTAL_DAYS = 25
    MAIN_FOLDER.mkdir(exist_ok=True)

    for day in range(1, TOTAL_DAYS + 1):
        day_folder = MAIN_FOLDER / f"Day-{day}"
        day_folder.mkdir(parents=True, exist_ok=True)

        (day_folder / "input.txt").touch()
        (day_folder / "part1.py").write_text(
            "def main():\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )
        (day_folder / "part2.py").write_text(
            "def main():\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )

if __name__ == "__main__":
    advent_of_code_year = int(input("Enter the year of Advent Of Code: "))
    print(f"Creating the local repo for AOC-{advent_of_code_year}")
    create_structure(advent_of_code_year)
