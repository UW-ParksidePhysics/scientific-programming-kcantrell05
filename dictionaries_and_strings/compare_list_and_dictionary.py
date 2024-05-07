def print_code_snippets():
    code_snippets = {
        "numbers": {
            "code": "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5",
            "explanation": "This code initializes a dictionary 'numbers' and assigns values to specific keys (0 and 1) using the square bracket notation, which works fine for dictionaries.",
            "fixed_code": None
        },
        "other_numbers": {
            "code": "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5",
            "explanation": "This code initializes an empty list 'other_numbers' and then tries to assign values to specific indices (0 and 1) using the square bracket notation, which raises an IndexError because lists cannot have gaps in their indices.",
            "fixed_code": "other_numbers = [0, 0]\nother_numbers[0] = -5\nother_numbers[1] = 10.5"
        }
    }

    for snippet_name, snippet_info in code_snippets.items():
        print(f"Snippet Name: {snippet_name}")
        print(f"Code Snippet:\n{snippet_info['code']}")
        print(f"Explanation:\n{snippet_info['explanation']}")
        if snippet_info["fixed_code"]:
            print(f"Fixed Code Snippet:\n{snippet_info['fixed_code']}")
        print()

if __name__ == '__main__':
    print_code_snippets()
