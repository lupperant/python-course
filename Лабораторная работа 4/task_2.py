import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    json_array = []
    with open(INPUT_FILENAME, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            json_array.append(row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(json_array, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
