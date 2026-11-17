#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    if not temp_str.isnumeric():
        raise ValueError(int(temp_str))
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for i in ("25", "abc"):
        print(f"\nInput data is '{i}'")
        try:
            input_temperature(i)
            print(f"Temperature is now {i}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
