#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    dir: str = "/non/existent/file"
    print(f"Testing operation {operation_number}...")
    try:
        if operation_number == 0:
            print(int(dir))
        elif operation_number == 1:
            print(1 / 0)
        elif operation_number == 2:
            print(open(dir, 'r'))
        elif operation_number == 3:
            dir += 1
        print("Operation completed successfully")
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    except Exception:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
