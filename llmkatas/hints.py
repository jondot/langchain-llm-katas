import yaml
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter


def load_yaml_file(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def display_hint(entries, test_name):
    for entry in entries:
        if entry["test"] == test_name:
            print(f"\nHint for test '{test_name}':\n")
            print(entry["hint"])
            break


def hints():
    file_path = "tests/hints.yaml"
    entries = load_yaml_file(file_path)

    test_names = [entry["test"] for entry in entries]
    completer = FuzzyWordCompleter(test_names)

    while True:
        search_query = prompt(
            'Search for a hint (type "exit" to quit): ',
            completer=completer,
            complete_while_typing=True,
        )
        search_query = search_query.strip().lower()

        if search_query == "exit":
            break

        if search_query in test_names:
            display_hint(entries, search_query)
        else:
            print("Test not found. Try again.")
