import json

file_name = "input.json"


def task() -> float:
    with open(file_name, 'r') as file:
        json_data = json.load(file)

        multiplied_values = [item["score"] * item["weight"] for item in json_data]
        summarised_values = sum(multiplied_values)
    return round(summarised_values, 3)


if __name__ == '__main__':
    print(task())
