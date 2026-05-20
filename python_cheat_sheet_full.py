"""Comprehensive Python cheat sheet demo based on requested topics."""

from array import array
from collections import namedtuple
import math


def announce_topic(topic: str, recursive: bool) -> None:
    mode = "self-call" if recursive else "initial-call"
    print(f"\n=== {topic} ({mode}) ===")


def present_topic(topic: str, demo_func, recursive: bool = False) -> None:
    announce_topic(topic, recursive)
    demo_func()
    if not recursive:
        present_topic(topic, demo_func, recursive=True)


def demo_literals() -> None:
    print(f"int={10}, float={2.5}, complex={3+2j}, str={'hello'}, bool={True}, none={None}")


def demo_operators() -> None:
    a, b = 7, 3
    print(f"a+b={a+b}, a>b={a>b}, a and b={bool(a and b)}")


def demo_arithmetic_operators() -> None:
    x, y = 9, 4
    print(f"+:{x+y}, -:{x-y}, *:{x*y}, /:{x/y}, //:{x//y}, %:{x%y}, **:{x**y}")


def demo_comparison_operators() -> None:
    x, y = 5, 8
    print(f"==:{x==y}, !=:{x!=y}, <:{x<y}, <=:{x<=y}, >:{x>y}, >=:{x>=y}")


def demo_assignment_operators() -> None:
    value = 10
    value += 5
    value *= 2
    value //= 3
    print(f"After +=, *=, //= result is {value}")


def demo_logical_operators() -> None:
    is_admin = True
    is_active = False
    print(f"and={is_admin and is_active}, or={is_admin or is_active}, not={not is_active}")


def demo_bitwise_operators() -> None:
    a, b = 6, 3
    print(f"&:{a & b}, |:{a | b}, ^:{a ^ b}, <<:{a << 1}, >>:{a >> 1}, ~:{~a}")


def demo_membership_operators() -> None:
    langs = ["python", "go", "rust"]
    print(f"'python' in langs -> {'python' in langs}, 'java' not in langs -> {'java' not in langs}")


def demo_identity_operators() -> None:
    one = [1, 2]
    two = one
    three = [1, 2]
    print(f"two is one -> {two is one}, three is one -> {three is one}, three == one -> {three == one}")


def demo_walrus_operator() -> None:
    if (length := len("cheat-sheet")) > 5:
        print(f"Walrus captured length={length}")


def demo_operator_precedence() -> None:
    print("Tutorialspoint precedence examples:")
    print(f"2 + 3 * 5 = {2 + 3 * 5}")
    print(f"(2 + 3) * 5 = {(2 + 3) * 5}")
    print(f"10 / 5 * 4 = {10 / 5 * 4}")


def demo_comments() -> None:
    print("Single-line comment: # comment")
    print('Docstring style: """text"""')


def demo_user_input() -> None:
    simulated_input = "25"
    age = int(simulated_input)
    print(f"Simulated input='{simulated_input}' converted to int={age}")


def demo_numbers() -> None:
    number = 42
    print(f"type={type(number).__name__}, abs(-42)={abs(-42)}, pow(2,5)={pow(2, 5)}")


def demo_booleans() -> None:
    print(f"bool(0)={bool(0)}, bool(1)={bool(1)}, bool('')={bool('')}, bool('x')={bool('x')}")


def demo_floating_points() -> None:
    value = 10.0 / 3
    print(f"float division={value}, rounded(2)={round(value, 2)}, isclose={math.isclose(0.1+0.2, 0.3)}")


def demo_control_flow() -> None:
    points = 73
    grade = "A" if points >= 90 else "B" if points >= 70 else "C"
    print(f"Control flow with ternary gave grade={grade}")


def demo_decision_making() -> None:
    temperature = 30
    decision = "Turn on AC" if temperature > 25 else "Open window"
    print(f"Decision: {decision}")


def demo_if_statement() -> None:
    if 7 > 3:
        print("If statement executed because 7 > 3")


def demo_if_else() -> None:
    number = 4
    if number % 2 == 0:
        print("If-else: number is even")
    else:
        print("If-else: number is odd")


def demo_nested_if() -> None:
    x = 15
    if x > 10:
        if x < 20:
            print("Nested if: x is between 10 and 20")


def demo_conditional_user_inputs() -> None:
    simulated_answer = "yes"
    if simulated_answer.lower() in ("yes", "y"):
        print("Conditional user input accepted positive response")
    else:
        print("Conditional user input rejected response")


def demo_match_case() -> None:
    command = "start"
    match command:
        case "start":
            print("match-case: starting")
        case "stop":
            print("match-case: stopping")
        case _:
            print("match-case: unknown command")


def demo_loops() -> None:
    print(f"Loop summary with sum over range(1,6) -> {sum(range(1, 6))}")


def demo_for_loops() -> None:
    values = []
    for item in ["a", "b", "c"]:
        values.append(item.upper())
    print(f"for loop transformed values -> {values}")


def demo_for_else() -> None:
    for value in [1, 2, 3]:
        if value == 4:
            break
    else:
        print("for-else: loop completed without break")


def demo_while_loops() -> None:
    count = 0
    while count < 3:
        count += 1
    print(f"while loop count ended at {count}")


def demo_break_statement() -> None:
    numbers = []
    for i in range(10):
        if i == 4:
            break
        numbers.append(i)
    print(f"break stopped loop at i=4 -> {numbers}")


def demo_continue_statement() -> None:
    numbers = []
    for i in range(6):
        if i % 2 == 0:
            continue
        numbers.append(i)
    print(f"continue skipped even numbers -> {numbers}")


def demo_pass_statement() -> None:
    for i in range(3):
        if i == 1:
            pass
    print("pass statement used as placeholder")


def demo_nested_loops() -> None:
    pairs = []
    for i in range(2):
        for j in range(2):
            pairs.append((i, j))
    print(f"nested loops produced pairs -> {pairs}")


def demo_functions() -> None:
    def square(n: int) -> int:
        return n * n

    print(f"function square(5) -> {square(5)}")


def demo_default_arguments() -> None:
    def greet(name: str = "Guest") -> str:
        return f"Hello, {name}"

    print(greet(), "|", greet("Sam"))


def demo_keyword_arguments() -> None:
    def build_name(first: str, last: str) -> str:
        return f"{first} {last}"

    print(build_name(last="Lovelace", first="Ada"))


def demo_keyword_only_arguments() -> None:
    def configure(*, retries: int, timeout: int) -> str:
        return f"retries={retries}, timeout={timeout}"

    print(configure(retries=3, timeout=30))


def demo_positional_arguments() -> None:
    def subtract(a, b):
        return a - b

    print(f"positional subtract(10,4) -> {subtract(10, 4)}")


def demo_positional_only_arguments() -> None:
    def divide(a, b, /):
        return a / b

    print(f"positional-only divide(8,2) -> {divide(8, 2)}")


def demo_arbitrary_arguments() -> None:
    def total(*args, **kwargs):
        return sum(args) + kwargs.get("bonus", 0)

    print(f"*args/**kwargs total(1,2,3, bonus=4) -> {total(1, 2, 3, bonus=4)}")


def demo_variable_scope() -> None:
    global_value = "global"

    def inner():
        local_value = "local"
        return f"{global_value}-{local_value}"

    print(f"scope demo -> {inner()}")


def demo_function_annotations() -> None:
    def multiply(a: int, b: int) -> int:
        return a * b

    print(f"annotations={multiply.__annotations__}, value={multiply(3, 4)}")


def demo_modules() -> None:
    print(f"module usage math.sqrt(49) -> {math.sqrt(49)}")


def demo_packing_unpacking() -> None:
    point = (4, 5, 6)
    x, y, z = point
    merged = [*point, 7]
    print(f"unpacked=({x},{y},{z}), packed merge={merged}")


def demo_builtin_functions() -> None:
    values = [5, 2, 9]
    print(f"len={len(values)}, min={min(values)}, max={max(values)}, sorted={sorted(values)}")


def demo_strings() -> None:
    text = "Python"
    print(f"string='{text}', length={len(text)}")


def demo_slicing_strings() -> None:
    text = "ABCDEFGHI"
    print(f"text[2:7]={text[2:7]}, text[::-1]={text[::-1]}")


def demo_modify_strings() -> None:
    text = " python "
    print(f"strip+upper -> '{text.strip().upper()}'")


def demo_string_concatenation() -> None:
    first = "Hello"
    second = "World"
    print(f"concatenation -> {first + ' ' + second}")


def demo_string_formatting() -> None:
    name = "Alex"
    score = 93.456
    print(f"f-string -> {name} scored {score:.2f}")


def demo_escape_characters() -> None:
    print("Line1\\nLine2 and quote -> \"Python\"")


def demo_string_methods() -> None:
    text = "python cheat sheet"
    print(f"title={text.title()}, replace={text.replace('cheat', 'study')}")


def demo_string_exercises() -> None:
    sample = "radar"
    print(f"exercise palindrome check for '{sample}' -> {sample == sample[::-1]}")


def demo_lists() -> None:
    values = [10, 20, 30]
    print(f"list={values}, length={len(values)}")


def demo_access_list_items() -> None:
    items = ["red", "green", "blue"]
    print(f"first={items[0]}, last={items[-1]}")


def demo_change_list_items() -> None:
    items = ["red", "green", "blue"]
    items[1] = "yellow"
    print(f"changed list -> {items}")


def demo_add_list_items() -> None:
    items = [1, 2]
    items.append(3)
    items.extend([4, 5])
    print(f"added list items -> {items}")


def demo_remove_list_items() -> None:
    items = [1, 2, 3, 4]
    items.remove(2)
    popped = items.pop()
    print(f"after remove/pop -> {items}, popped={popped}")


def demo_loop_lists() -> None:
    items = ["a", "b", "c"]
    print(f"loop result -> {[char.upper() for char in items]}")


def demo_list_comprehension() -> None:
    squares = [n * n for n in range(1, 6)]
    print(f"list comprehension squares -> {squares}")


def demo_sort_lists() -> None:
    nums = [4, 1, 9, 2]
    nums.sort()
    print(f"sorted list -> {nums}")


def demo_copy_lists() -> None:
    original = [1, 2, 3]
    copied = original.copy()
    print(f"copy list -> original={original}, copied={copied}")


def demo_join_lists() -> None:
    one = [1, 2]
    two = [3, 4]
    print(f"joined list -> {one + two}")


def demo_list_methods() -> None:
    items = ["x", "y", "x"]
    items.append("z")
    print(f"count('x')={items.count('x')}, index('y')={items.index('y')}, items={items}")


def demo_list_exercises() -> None:
    nums = [3, 1, 2]
    nums.sort(reverse=True)
    print(f"exercise sort descending -> {nums}")


def demo_tuples() -> None:
    item = ("apple", "banana", "orange")
    print(f"tuple={item}, length={len(item)}")


def demo_access_tuple_items() -> None:
    item = ("a", "b", "c")
    print(f"access tuple -> first={item[0]}, slice={item[1:]}")


def demo_update_tuples() -> None:
    item = ("a", "b", "c")
    temp = list(item)
    temp[1] = "beta"
    updated = tuple(temp)
    print(f"updated tuple via list conversion -> {updated}")


def demo_unpack_tuples() -> None:
    item = ("x", "y", "z")
    first, second, third = item
    print(f"unpacked tuple -> {first}, {second}, {third}")


def demo_loop_tuples() -> None:
    item = (1, 2, 3)
    total = 0
    for value in item:
        total += value
    print(f"loop tuple sum -> {total}")


def demo_join_tuples() -> None:
    a = (1, 2)
    b = (3, 4)
    print(f"joined tuples -> {a + b}")


def demo_tuple_methods() -> None:
    item = ("a", "b", "a", "c")
    print(f"count('a')={item.count('a')}, index('b')={item.index('b')}")


def demo_namedtuple() -> None:
    Point = namedtuple("Point", ["x", "y"])
    p = Point(10, 20)
    print(f"namedtuple Point -> x={p.x}, y={p.y}")


def demo_tuple_exercises() -> None:
    a, b = (1, 2)
    a, b = b, a
    print(f"exercise tuple swap -> a={a}, b={b}")


def demo_sets() -> None:
    values = {1, 2, 2, 3}
    print(f"set removes duplicates -> {values}")


def demo_access_set_items() -> None:
    values = {"apple", "banana", "cherry"}
    print(f"iterate set example -> {sorted(values)}")


def demo_add_set_items() -> None:
    values = {1, 2}
    values.add(3)
    values.update([4, 5])
    print(f"add set items -> {values}")


def demo_remove_set_items() -> None:
    values = {1, 2, 3, 4}
    values.remove(2)
    values.discard(9)
    print(f"remove set items -> {values}")


def demo_loop_sets() -> None:
    values = {3, 1, 2}
    ordered = [v for v in sorted(values)]
    print(f"loop set values (sorted for display) -> {ordered}")


def demo_join_sets() -> None:
    a = {1, 2}
    b = {2, 3}
    print(f"join sets with union -> {a.union(b)}")


def demo_copy_sets() -> None:
    original = {1, 2, 3}
    copied = original.copy()
    print(f"copy set -> original={original}, copied={copied}")


def demo_set_operators() -> None:
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(f"intersection={a & b}, difference={a - b}, symmetric_diff={a ^ b}")


def demo_set_methods() -> None:
    values = {1, 2, 3}
    values.pop()
    print(f"set methods demo after pop -> {values}")


def demo_set_exercises() -> None:
    values = [1, 2, 2, 3, 3, 4]
    print(f"exercise remove duplicates -> {list(set(values))}")


def demo_dictionaries() -> None:
    user = {"name": "Ada", "role": "Engineer"}
    print(f"dictionary={user}")


def demo_access_dictionary_items() -> None:
    user = {"name": "Ada", "role": "Engineer"}
    print(f"access dict -> name={user['name']}, role={user.get('role')}")


def demo_change_dictionary_items() -> None:
    user = {"name": "Ada", "role": "Engineer"}
    user["role"] = "Architect"
    print(f"changed dict -> {user}")


def demo_add_dictionary_items() -> None:
    user = {"name": "Ada"}
    user["role"] = "Engineer"
    print(f"added dict item -> {user}")


def demo_remove_dictionary_items() -> None:
    user = {"name": "Ada", "role": "Engineer", "active": True}
    removed = user.pop("active")
    print(f"removed active={removed}, dict={user}")


def demo_dictionary_view_objects() -> None:
    user = {"name": "Ada", "role": "Engineer"}
    print(f"keys={list(user.keys())}, items={list(user.items())}")


def demo_loop_dictionaries() -> None:
    user = {"name": "Ada", "role": "Engineer"}
    pairs = [f"{k}:{v}" for k, v in user.items()]
    print(f"loop dict pairs -> {pairs}")


def demo_copy_dictionaries() -> None:
    original = {"a": 1}
    copied = original.copy()
    print(f"copy dict -> original={original}, copied={copied}")


def demo_nested_dictionaries() -> None:
    org = {"team": {"lead": "Ada", "size": 4}}
    print(f"nested dict lead -> {org['team']['lead']}")


def demo_dictionary_methods() -> None:
    user = {"name": "Ada"}
    user.update({"role": "Engineer"})
    print(f"dict methods update/get -> role={user.get('role')}, dict={user}")


def demo_dictionary_exercises() -> None:
    data = {"a": 1, "b": 2}
    inverted = {value: key for key, value in data.items()}
    print(f"exercise invert dictionary -> {inverted}")


def demo_arrays() -> None:
    values = array("i", [1, 2, 3])
    print(f"array={values.tolist()}")


def demo_access_array_items() -> None:
    values = array("i", [10, 20, 30])
    print(f"access array -> first={values[0]}, last={values[-1]}")


def demo_add_array_items() -> None:
    values = array("i", [1, 2])
    values.append(3)
    values.extend(array("i", [4, 5]))
    print(f"add array items -> {values.tolist()}")


def demo_remove_array_items() -> None:
    values = array("i", [1, 2, 3, 4])
    values.pop()
    values.remove(2)
    print(f"remove array items -> {values.tolist()}")


def demo_loop_arrays() -> None:
    values = array("i", [2, 4, 6])
    doubled = [item * 2 for item in values]
    print(f"loop array doubled -> {doubled}")


def demo_copy_arrays() -> None:
    values = array("i", [5, 6, 7])
    copied = array("i", values)
    print(f"copy arrays -> original={values.tolist()}, copied={copied.tolist()}")


def demo_reverse_arrays() -> None:
    values = array("i", [1, 2, 3, 4])
    reversed_values = values.tolist()[::-1]
    print(f"reverse array -> {reversed_values}")


def demo_sort_arrays() -> None:
    values = array("i", [4, 1, 3, 2])
    print(f"sort array -> {sorted(values)}")


def demo_join_arrays() -> None:
    one = array("i", [1, 2])
    two = array("i", [3, 4])
    joined = array("i", one)
    joined.extend(two)
    print(f"join arrays -> {joined.tolist()}")


def demo_array_methods() -> None:
    values = array("i", [1, 2, 2, 3])
    print(f"array count(2)={values.count(2)}, index(3)={values.index(3)}")


def demo_array_exercises() -> None:
    values = array("i", [10, 20, 30, 40])
    average = sum(values) / len(values)
    print(f"exercise array average -> {average}")


TOPIC_DEMOS = [
    ("Python - Literals", demo_literals),
    ("Python - Operators", demo_operators),
    ("Python - Arithmetic Operators", demo_arithmetic_operators),
    ("Python - Comparison Operators", demo_comparison_operators),
    ("Python - Assignment Operators", demo_assignment_operators),
    ("Python - Logical Operators", demo_logical_operators),
    ("Python - Bitwise Operators", demo_bitwise_operators),
    ("Python - Membership Operators", demo_membership_operators),
    ("Python - Identity Operators", demo_identity_operators),
    ("Python - Walrus Operator", demo_walrus_operator),
    ("Python - Operator Precedence", demo_operator_precedence),
    ("Python - Comments", demo_comments),
    ("Python - User Input", demo_user_input),
    ("Python - Numbers", demo_numbers),
    ("Python - Booleans", demo_booleans),
    ("Python - Floating Points", demo_floating_points),
    ("Python - Control Flow", demo_control_flow),
    ("Python - Decision Making", demo_decision_making),
    ("Python - If Statement", demo_if_statement),
    ("Python - If else", demo_if_else),
    ("Python - Nested If", demo_nested_if),
    ("Python - Conditional User Inputs", demo_conditional_user_inputs),
    ("Python - Match-Case Statement", demo_match_case),
    ("Python - Loops", demo_loops),
    ("Python - for Loops", demo_for_loops),
    ("Python - for-else Loops", demo_for_else),
    ("Python - While Loops", demo_while_loops),
    ("Python - break Statement", demo_break_statement),
    ("Python - continue Statement", demo_continue_statement),
    ("Python - pass Statement", demo_pass_statement),
    ("Python - Nested Loops", demo_nested_loops),
    ("Python Functions & Modules", demo_functions),
    ("Python - Functions", demo_functions),
    ("Python - Default Arguments", demo_default_arguments),
    ("Python - Keyword Arguments", demo_keyword_arguments),
    ("Python - Keyword-Only Arguments", demo_keyword_only_arguments),
    ("Python - Positional Arguments", demo_positional_arguments),
    ("Python - Positional-Only Arguments", demo_positional_only_arguments),
    ("Python - Arbitrary Arguments", demo_arbitrary_arguments),
    ("Python - Variables Scope", demo_variable_scope),
    ("Python - Function Annotations", demo_function_annotations),
    ("Python - Modules", demo_modules),
    ("Python - Packing and Unpacking", demo_packing_unpacking),
    ("Python - Built in Functions", demo_builtin_functions),
    ("Python Strings", demo_strings),
    ("Python - Strings", demo_strings),
    ("Python - Slicing Strings", demo_slicing_strings),
    ("Python - Modify Strings", demo_modify_strings),
    ("Python - String Concatenation", demo_string_concatenation),
    ("Python - String Formatting", demo_string_formatting),
    ("Python - Escape Characters", demo_escape_characters),
    ("Python - String Methods", demo_string_methods),
    ("Python - String Exercises", demo_string_exercises),
    ("Python Lists", demo_lists),
    ("Python - Lists", demo_lists),
    ("Python - Access List Items", demo_access_list_items),
    ("Python - Change List Items", demo_change_list_items),
    ("Python - Add List Items", demo_add_list_items),
    ("Python - Remove List Items", demo_remove_list_items),
    ("Python - Loop Lists", demo_loop_lists),
    ("Python - List Comprehension", demo_list_comprehension),
    ("Python - Sort Lists", demo_sort_lists),
    ("Python - Copy Lists", demo_copy_lists),
    ("Python - Join Lists", demo_join_lists),
    ("Python - List Methods", demo_list_methods),
    ("Python - List Exercises", demo_list_exercises),
    ("Python Tuples", demo_tuples),
    ("Python - Tuples", demo_tuples),
    ("Python - Access Tuple Items", demo_access_tuple_items),
    ("Python - Update Tuples", demo_update_tuples),
    ("Python - Unpack Tuples", demo_unpack_tuples),
    ("Python - Loop Tuples", demo_loop_tuples),
    ("Python - Join Tuples", demo_join_tuples),
    ("Python - Tuple Methods", demo_tuple_methods),
    ("Python - Namedtuple", demo_namedtuple),
    ("Python - Tuple Exercises", demo_tuple_exercises),
    ("Python Sets", demo_sets),
    ("Python - Sets", demo_sets),
    ("Python - Access Set Items", demo_access_set_items),
    ("Python - Add Set Items", demo_add_set_items),
    ("Python - Remove Set Items", demo_remove_set_items),
    ("Python - Loop Sets", demo_loop_sets),
    ("Python - Join Sets", demo_join_sets),
    ("Python - Copy Sets", demo_copy_sets),
    ("Python - Set Operators", demo_set_operators),
    ("Python - Set Methods", demo_set_methods),
    ("Python - Set Exercises", demo_set_exercises),
    ("Python Dictionaries", demo_dictionaries),
    ("Python - Dictionaries", demo_dictionaries),
    ("Python - Access Dictionary Items", demo_access_dictionary_items),
    ("Python - Change Dictionary Items", demo_change_dictionary_items),
    ("Python - Add Dictionary Items", demo_add_dictionary_items),
    ("Python - Remove Dictionary Items", demo_remove_dictionary_items),
    ("Python - Dictionary View Objects", demo_dictionary_view_objects),
    ("Python - Loop Dictionaries", demo_loop_dictionaries),
    ("Python - Copy Dictionaries", demo_copy_dictionaries),
    ("Python - Nested Dictionaries", demo_nested_dictionaries),
    ("Python - Dictionary Methods", demo_dictionary_methods),
    ("Python - Dictionary Exercises", demo_dictionary_exercises),
    ("Python Arrays", demo_arrays),
    ("Python - Arrays", demo_arrays),
    ("Python - Access Array Items", demo_access_array_items),
    ("Python - Add Array Items", demo_add_array_items),
    ("Python - Remove Array Items", demo_remove_array_items),
    ("Python - Loop Arrays", demo_loop_arrays),
    ("Python - Copy Arrays", demo_copy_arrays),
    ("Python - Reverse Arrays", demo_reverse_arrays),
    ("Python - Sort Arrays", demo_sort_arrays),
    ("Python - Join Arrays", demo_join_arrays),
    ("Python - Array Methods", demo_array_methods),
    ("Python - Array Exercises", demo_array_exercises),
]


def main() -> None:
    print("Comprehensive Python Cheat Sheet")
    print("Each topic is announced and then repeated once via self-call.\n")

    for topic, handler in TOPIC_DEMOS:
        present_topic(topic, handler)

    print(f"\nCheat sheet complete. Topics covered: {len(TOPIC_DEMOS)}")


if __name__ == "__main__":
    main()
