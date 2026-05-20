"""Python feature cheat sheet with self-calling demo functions."""

from array import array


def announce_feature(feature_name: str, recursive: bool) -> None:
    """Print a consistent banner before each feature demo."""
    mode = "self-call" if recursive else "initial-call"
    print(f"\n=== Presenting Feature: {feature_name} ({mode}) ===")


def demonstrate_lists(recursive: bool = False) -> None:
    announce_feature("Lists", recursive)
    languages = ["Python", "Java", "Go"]
    languages.append("Rust")
    languages[1] = "TypeScript"
    print(f"List values: {languages}")
    print(f"Sliced list (first 2): {languages[:2]}")

    if not recursive:
        demonstrate_lists(recursive=True)


def demonstrate_tuples(recursive: bool = False) -> None:
    announce_feature("Tuples", recursive)
    version_info = ("Python", 3, 12)
    name, major, minor = version_info
    print(f"Tuple unpacked -> name={name}, major={major}, minor={minor}")
    print(f"Tuple length: {len(version_info)}")

    if not recursive:
        demonstrate_tuples(recursive=True)


def demonstrate_dictionaries(recursive: bool = False) -> None:
    announce_feature("Dictionaries", recursive)
    user = {"name": "Alex", "role": "Admin", "active": True}
    user["role"] = "Engineer"
    user["last_login"] = "2026-05-20"
    print(f"Dictionary values: {user}")
    print(f"Dictionary keys: {list(user.keys())}")

    if not recursive:
        demonstrate_dictionaries(recursive=True)


def demonstrate_arrays(recursive: bool = False) -> None:
    announce_feature("Arrays (array module)", recursive)
    scores = array("i", [82, 91, 76, 88])
    scores.append(95)
    scores[0] = 85
    print(f"Array values: {scores.tolist()}")
    print(f"Array max score: {max(scores)}")

    if not recursive:
        demonstrate_arrays(recursive=True)


def demonstrate_flow_control(recursive: bool = False) -> None:
    announce_feature("Flow Control", recursive)
    numbers = [1, 2, 3, 4, 5, 6]

    even_numbers = []
    for value in numbers:
        if value % 2 == 0:
            even_numbers.append(value)
        else:
            continue

    print(f"Input numbers: {numbers}")
    print(f"Even numbers found with for/if/continue: {even_numbers}")

    if not recursive:
        demonstrate_flow_control(recursive=True)


def demonstrate_operator_precedence(recursive: bool = False) -> None:
    """
    Demonstrate precedence inspired by Tutorialspoint examples:
    https://www.tutorialspoint.com/python/operators_precedence_example.htm
    """
    announce_feature("Operator Precedence", recursive)

    a = 2 + 3 * 5
    b = (2 + 3) * 5
    c = 10 / 5 * 4
    d = 20 + (10 * 15) / 5

    print("2 + 3 * 5 =", a, " (multiplication before addition)")
    print("(2 + 3) * 5 =", b, " (parentheses override default precedence)")
    print("10 / 5 * 4 =", c, " (same precedence, left-to-right associativity)")
    print("20 + (10 * 15) / 5 =", d, " (BODMAS-style evaluation)")

    if not recursive:
        demonstrate_operator_precedence(recursive=True)


def main() -> None:
    print("Python Cheat Sheet Demo")
    print("Each function announces its feature and self-calls once.\n")

    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_arrays()
    demonstrate_flow_control()
    demonstrate_operator_precedence()

    print("\nCheat sheet demo complete.")


if __name__ == "__main__":
    main()
