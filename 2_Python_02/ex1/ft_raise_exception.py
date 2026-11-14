#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int = 0
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        if temp_int > 40 or temp_int < 0:
            raise OverflowError
        print(f"Temperature is now {temp_int}°C")
    except OverflowError:
        print("Caught input_temperature error: ", end="")
        if temp_int > 40:
            print(f"{temp_int}°C is too hot for plants (max 40°C)")
        else:
            print(f"{temp_int}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
