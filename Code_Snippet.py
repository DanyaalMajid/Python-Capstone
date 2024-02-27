import json
import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

SNIPPETS_FILE = "snippets.json"

def load_snippets():
    if os.path.exists(SNIPPETS_FILE):
        with open(SNIPPETS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_snippets(snippets):
    with open(SNIPPETS_FILE, "w") as f:
        json.dump(snippets, f, indent=4)

def add_snippet(snippets):
    language = input("Enter the language of the snippet: ")
    snippet_type = input("Enter the type of the snippet (function, class, etc.): ")
    code = input("Enter the code snippet: ")

    if language not in snippets:
        snippets[language] = {}

    if snippet_type not in snippets[language]:
        snippets[language][snippet_type] = []

    snippets[language][snippet_type].append(code)
    save_snippets(snippets)
    print("Snippet added successfully!")

def display_snippets(snippets):
    language = input("Enter the language to display snippets for: ")
    if language not in snippets:
        print("No snippets found for this language.")
        return

    print("Snippets for", language + ":")
    for snippet_type, codes in snippets[language].items():
        print("\n", snippet_type + ":")
        for code in codes:
            lexer = get_lexer_by_name(language)
            formatted_code = highlight(code, lexer, TerminalFormatter())
            print(formatted_code)

def main():
    snippets = load_snippets()

    while True:
        print("\nCode Snippet Manager")
        print("1. Add a snippet")
        print("2. Display snippets")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_snippet(snippets)
        elif choice == "2":
            display_snippets(snippets)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
