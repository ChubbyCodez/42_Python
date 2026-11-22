#!/usr/bin/env python3

import sys as s


def create_scoreboard(args: list[str]) -> list[int]:
    out: list[int] = []
    temp: int = 0
    for i in args:
        try:
            temp = int(i)
            out.append(temp)
        except Exception:
            pass
    return out


def average_score(args: list[int]) -> float:
    return sum(args) / len(args)


if __name__ == "__main__":
    i: int = 1
    error: bool = False
    print("=== Player Score Analytics ===")
    if len(s.argv) < 2:
        error = True
    if not error:
        args: list[int] = create_scoreboard(s.argv[1:])
        if not args:
            error = True
        else:
            print(f"Score processed: {args}")
            print(f"Total players: {len(args)}")
            print(f"Total score: {sum(args)}")
            print(f"Average score: {average_score(args)}")
            print(f"High score: {max(args)}")
            print(f"Low score: {min(args)}")
            print(f"Score range: {max(args) - min(args)}")
    if error:
        print(f"No scores provided. Usage: {s.argv[0]} <score1> <score2> ...")
    print("")
