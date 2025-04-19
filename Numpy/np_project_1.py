def display_menu():
    print("NumPy Matrix Toolkit")
    print("1. Create array")
    print("2. Create arange array")
    print("3. Create zeros array")
    print("4. Create ones array")
    print("5. Create full array")
    print("6. Create identity matrix")
    print("7. Create linspace array")
    print("8. Create empty array")
    print("9. Exit")

def create_array():
    raw_input = input("Enter array elements separated by commas (e.g., 1,2.5,3) [default: 1,2,3]: ").strip()
    
    if not raw_input:
        raw_input = "1,2,3"

    elements = []
    for x in raw_input.split(","):
        x = x.strip()
        try:
            val = float(x) if '.' in x else int(x)
            elements.append(val)
        except ValueError:
            print(f"Warning: Skipped invalid entry '{x}'")

    if not elements:
        print("No valid elements provided. Array not created.")
        return

    arr = np.array(elements)
    print("1D Array created:", arr)

    reshape = input("Do you want to reshape the array? (y/n): ").strip().lower()
    if reshape == 'y':
        shape_input = input("Enter new shape (e.g., 2,2): ").strip()
        try:
            shape = tuple(int(dim) for dim in shape_input.split(","))
            arr = arr.reshape(shape)
            print("Reshaped array:\n", arr)
        except Exception as e:
            print("Error reshaping array:", e)

    return True

def create_arange_array():
    start = input("Enter start value [default: 0]: ").strip()
    stop = input("Enter stop value [default: 10]: ").strip()
    step = input("Enter step value [default: 1]: ").strip()
    dtype = input("Enter data type (int, float32, float64) [default: int]: ").strip()
    like = input("Enter like array (e.g., [1,2,3]) [default: None]: ").strip()

    start = int(start) if start else 0
    stop = int(stop) if stop else 10
    step = int(step) if step else 1

    dtype_map = {
        "int": int,
        "float32": np.float32,
        "float64": np.float64
    }

    dtype = dtype_map.get(dtype, int)
    like = np.array(eval(like)) if like else None

    try:
        arr = np.arange(start, stop, step, dtype=dtype, like=like)
        print("Arange array created:", arr)
    except Exception as e:
        print("Error creating arange array:", e)
        return 
    
    reshape = input("Do you want to reshape the array? (y/n): ").strip().lower()
    if reshape == 'y':
        shape_input = input("Enter new shape (e.g., 2,2): ").strip()
        try:
            shape = tuple(int(dim) for dim in shape_input.split(","))
            arr = arr.reshape(shape)
            print("Reshaped array:\n", arr)
        except Exception as e:
            print("Error reshaping array:", e)      

    return True

def create_zeros_array():
    shape_input = input("Enter shape (e.g., 2,3) [default: 2,3]: ").strip()
    dtype = input("Enter data type (int, folat32, float64)  [default: int]: ").strip()
    order = input("Enter order (C, F) [default: C]: ").strip()

    shape_input = shape_input if shape_input else "2,3"
    dtype = dtype if dtype else "int"
    order = order if order else "C"

    shape_input = tuple(int(dim) for dim in shape_input.split(","))

    dtype_map = {
        "int": int,
        "float32":np.float32,
        "float64": np.float64
    }
    dtype = dtype_map.get(dtype, int)

    try:
        arr = np.zeros(shape_input, dtype=dtype, order=order)
        print("Zeros array created: \n", arr)
    except Exception as e:
        print("Error creating zeros array:", e)
        return

    return True

def create_ones_array():
    shape_input = input("Enter shape (e.g., 2,3) [default: 2,3]: ").strip()
    dtype = input("Enter data type (int, float32, float64) [default: int]: ").strip()

    shape_input = shape_input if shape_input else "2,3"
    dtype = dtype if dtype else "int"

    shape_input = tuple(int(dim) for dim in shape_input.split(","))
    dtype_map = {
        "int": int,
        "float32":np.float32,
        "float64": np.float64
    }
    dtype = dtype_map.get(dtype, int)

    try:
        arr = np.ones(shape_input, dtype=dtype)
        print("Ones array created: \n", arr)
    except Exception as e:
        print("Error creating Ones array:", e)
        return
    
    reshape = input("Do you want to reshape the array? (y/n): ").strip().lower()
    if reshape == 'y':
        shape_input = input("Enter new shape (e.g., 2,2): ").strip()
        try:
            shape = tuple(int(dim) for dim in shape_input.split(","))
            arr = arr.reshape(shape)
            print("Reshaped array:\n", arr)
        except Exception as e:
            print("Error reshaping array:", e)

    return True


def create_full_array():
    shape_input = input("Enter shape (e.g., 2,3) [default: 2,3]: ").strip()
    fill_value = input("Enter fill value [default: 0]: ").strip()
    dtype = input("Enter data type (int, float32, float64) [default: int]: ").strip()

    shape_input = shape_input if shape_input else "2,3"
    fill_value = float(fill_value) if fill_value else 0
    dtype = dtype if dtype else "int"

    shape = tuple(int(dim) for dim in shape_input.split(","))
    dtype_map = {
        "int": int,
        "float32": np.float32,
        "float64": np.float64
    }
    dtype = dtype_map.get(dtype, int)

    try:
        arr = np.full(shape, fill_value, dtype=dtype)
        print("Full array created: \n", arr)
    except Exception as e:
        print("Error creating full array:", e)

    return True

def create_identity_matrix():
    size = input("Enter size of identity matrix [default: 3]: ").strip()
    dtype = input("Enter data type (int, float32, float64) [default: int]: ").strip()

    size = int(size) if size else 3
    dtype = dtype if dtype else "int"

    dtype_map = {
        "int": int,
        "float32": np.float32,
        "float64": np.float64
    }
    dtype = dtype_map.get(dtype, int)

    try:
        arr = np.eye(size, dtype=dtype)
        print("Identity matrix:\n", arr)
    except Exception as e:
        print("Error creating identity matrix:", e)

    return True

def create_linspace_array():
    start = input("Enter start value [default: 0]: ").strip()
    stop = input("Enter stop value [default: 1]: ").strip()
    num = input("Enter number of samples [default: 50]: ").strip()
    dtype = input("Enter data type (float32, float64) [default: float64]: ").strip()

    start = float(start) if start else 0
    stop = float(stop) if stop else 1
    num = int(num) if num else 50
    dtype = dtype if dtype else "float64"

    dtype_map = {
        "float32": np.float32,
        "float64": np.float64
    }
    dtype = dtype_map.get(dtype, np.float64)

    try:
        arr = np.linspace(start, stop, num, dtype=dtype)
        print("Linspace array:\n", arr)
    except Exception as e:
        print("Error creating linspace array:", e)

    return True

def create_empty_array():
    shape_input = input("Enter shape (e.g., 2,3) [default: 2,3]: ").strip()
    dtype = input("Enter data type (int, float32, float64) [default: float64]: ").strip()

    shape_input = shape_input if shape_input else "2,3"
    dtype = dtype if dtype else "float64"

    shape = tuple(int(dim) for dim in shape_input.split(","))
    dtype_map = {
        "int": int,
        "float32": np.float32,
        "float64": np.float64
    }
    dtype = dtype_map.get(dtype, np.float64)

    try:
        arr = np.empty(shape, dtype=dtype)
        print("Empty (uninitialized) array:\n", arr)
    except Exception as e:
        print("Error creating empty array:", e)

    return True

def switch(choice):
    switcher = {
        '1': create_array,
        '2': create_arange_array,
        '3': create_zeros_array,
        '4': create_ones_array,
        '5': create_full_array,
        '6': create_identity_matrix,
        '7': create_linspace_array,
        '8': create_empty_array,
        '9': exit
    }
    func = switcher.get(choice, lambda: print("Invalid choice"))
    return func()
    
    

if __name__ == "__main__":
    import numpy as np

    iteration = True
    while iteration:
        display_menu()
        choice = input("Enter your choice: ")
        iteration = switch(choice)