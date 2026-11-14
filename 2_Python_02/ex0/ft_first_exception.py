#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int = 0
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    input_temperature("abc")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
