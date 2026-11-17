#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        new_int: int = int(temp_str)
    except Exception:
        raise ValueError(int(temp_str))
    if new_int > 40:
        raise OverflowError(f"{new_int}°C is too hot for plants (max 40°C)")
    elif new_int < 0:
        raise OverflowError(f"{new_int}°C is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    for i in ("25", "abc", "100", '-50'):
        try:
            print(f"\nInput data is '{i}'")
            temp: int = input_temperature(i)
            print(f"Temperature is now {temp}°C")
        except (ValueError, OverflowError) as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
