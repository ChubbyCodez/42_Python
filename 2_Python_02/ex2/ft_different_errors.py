#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    dir: str = "/non/existent/file"
    if operation_number == 0:
        raise ValueError(int("abc"))
    elif operation_number == 1:
        raise ZeroDivisionError(1 / 0)
    elif operation_number == 2:
        raise FileNotFoundError(open(dir, 'r'))
    elif operation_number == 3:
        raise TypeError(dir + 1)
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
