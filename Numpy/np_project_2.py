import numpy as np
import ast

def display_menu():
    print("\nNumPy Operations Toolkit")
    print("1. Bit Wise AND")
    print("2. Bit Wise OR")
    print("3. Bit Wise XOR")
    print("4. Invert")
    print("5. Binary Representation")
    print("6. Exit")

def parse_input(prompt):
    user_input = input(prompt).strip()
    try:
        if user_input.startswith('[') and user_input.endswith(']'):
            return np.array(ast.literal_eval(user_input))
        else:
            return int(user_input)
    except Exception as e:
        print("Invalid input:", e)
        return None

def bitwise_and():
    a = parse_input("Enter first number or array (e.g., 5 or [1,2,3]): ")
    b = parse_input("Enter second number or array (e.g., 5 or [1,2,3]): ")
    if a is None or b is None:
        return True

    try:
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray) and a.shape != b.shape:
            raise ValueError("Arrays must have the same shape for bitwise AND.")
        result = np.bitwise_and(a, b)
        print("Result of Bitwise AND:", result)
    except Exception as e:
        print("Error:", e)
    print()
    return True

def bitwise_or():
    a = parse_input("Enter first number or array (e.g., 5 or [1,2,3]): ")
    b = parse_input("Enter second number or array (e.g., 5 or [1,2,3]): ")
    if a is None or b is None:
        return True

    try:
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray) and a.shape != b.shape:
            raise ValueError("Arrays must have the same shape for bitwise OR.")
        result = np.bitwise_or(a, b)
        print("Result of Bitwise OR:", result)
    except Exception as e:
        print("Error:", e)
    print()
    return True

def bitwise_xor():
    a = parse_input("Enter first number or array (e.g., 5 or [1,2,3]): ")
    b = parse_input("Enter second number or array (e.g., 5 or [1,2,3]): ")
    if a is None or b is None:
        return True

    try:
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray) and a.shape != b.shape:
            raise ValueError("Arrays must have the same shape for bitwise XOR.")
        result = np.bitwise_xor(a, b)
        print("Result of Bitwise XOR:", result)
    except Exception as e:
        print("Error:", e)
    print()
    return True

def invert():
    a = parse_input("Enter number or array (e.g., 5 or [1,2,3]): ")
    if a is None:
        return True

    try:
        result = np.invert(a)
        print(f"Result of Invert of {a}: {result}")
    except Exception as e:
        print("Error:", e)
    print()
    return True

def binary_represent():
    a = parse_input("Enter number or array (e.g., 5 or [1,2,3]): ")
    if a is None:
        return True

    try:
        if isinstance(a, np.ndarray):
            result = [np.binary_repr(x) for x in a]
        else:
            result = np.binary_repr(a)
        print(f"Binary representation of {a}: {result}")
    except Exception as e:
        print("Error:", e)
    print()
    return True

def switch(choice):
    switcher = {
        '1': bitwise_and,
        '2': bitwise_or,
        '3': bitwise_xor,
        '4': invert,
        '5': binary_represent,
        '6': lambda: False
    }
    func = switcher.get(choice, lambda: print("Invalid choice\n"))
    return func()

if __name__ == "__main__":
    running = True
    while running:
        display_menu()
        user_choice = input("Enter your choice: ").strip()
        running = switch(user_choice)
