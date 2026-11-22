#!/usr/bin/env python3

import math as m


def get_player_pos() -> str:
    prompt: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        try:
            coor_str: str = input(prompt)
            if coor_str.count(",") != 2:
                raise Exception("Invalid syntax")
            for i in coor_str.split(","):
                _ = float(i)
            (_, _, _) = [float(x) for x in coor_str.split(",")]
            break
        except ValueError as e:
            print(f"Error on parameter '{i}': {e}")
        except Exception as e:
            print(e)
    return coor_str


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    (x1, y1, z1) = [float(x) for x in get_player_pos().split(",")]
    print(f"Got a first tuple: {(x1, y1, z1)}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance1: float = round(m.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Distance to center: {distance1}")
    print("\nGet a second set of coordinates")
    (x2, y2, z2) = [float(x) for x in get_player_pos().split(",")]
    distance2: float = round(m.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), 4)
    print(f"Distance to center: {distance2}")
