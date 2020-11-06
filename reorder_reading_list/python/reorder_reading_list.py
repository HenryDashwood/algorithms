import re
from pathlib import Path
from typer import Typer

app = Typer()


def reverse(reading_list):
    if not reading_list:
        return reading_list
    return reverse(reading_list[1:]) + [reading_list[0]]


def divide_into_years(reading_list):
    split_list = re.split("(2\d{3})", reading_list)[1:]

    for i, list in enumerate(split_list[1::2]):
        one_years_books = [l for l in list.split("\n") if l]
        reversed_list = reverse(one_years_books)
        reversed = "\n\n".join(reversed_list)
        split_list[i * 2 + 1] = reversed
    return [
        f"{i.strip()}\n\n{j.strip()}\n"
        for i, j in zip(split_list[::2], split_list[1::2])
    ]


def reorder(reading_list):
    paired_list = divide_into_years(reading_list)
    reordered_list = reverse(paired_list)
    return "\n".join(reordered_list)


@app.command()
def main(input: Path, output: Path):
    with open(input) as f:
        reading_list = f.read()
    output_list = reorder(reading_list)
    with open(output, "w") as f:
        f.write(output_list)


if __name__ == "__main__":
    app()
