#!/usr/bin/env python3

import random as r


def gen_player_achievements(achv: set[str]) -> set[str]:
    return set(r.sample(list(achv), r.randint(0, len(achv))))


if __name__ == "__main__":
    achv_full: set[str] = {'Crafting Genius', 'Strategist', 'World Savior',
                           'Speed Runner', 'Survivor', 'Master Explorer',
                           'Treasure Hunter', 'Unstoppable', 'First Steps',
                           'Collector Supreme', 'Untouchable', 'Sharp Mind',
                           'Boss Slayer'}
    alice: set[str] = gen_player_achievements(achv_full)
    bob: set[str] = gen_player_achievements(achv_full)
    charlie: set[str] = gen_player_achievements(achv_full)
    dylan: set[str] = gen_player_achievements(achv_full)
    players: dict[str, set[str]] = {
        'Alice': alice,
        'Bob': bob,
        'Charlie': charlie,
        'Dylan': dylan
    }
    print("=== Achievement Tracker System ===")
    print("")
    for k, v in players.items():
        print(f"{k}: {v}")
    print("")
    print(f"All distinct achievements: {alice | bob | charlie | dylan}")
    print("")
    print(f"Common achievements: {alice & bob & charlie & dylan}\n")
    for k, v in players.items():
        print(f"Only {k} has: "
              f"{v - set().union(*(j for i, j in players.items() if i != k))}")
    print("")
    for k, v in players.items():
        print(f"{k} is missing: {achv_full.difference(v)}")
