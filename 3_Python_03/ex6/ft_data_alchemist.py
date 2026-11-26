#!/usr/bin/env python3

import random as r


if __name__ == '__main__':
    names: list[str] = ["elysia", "jun hong", "joon hoe", "lanisha", "dexmund",
                        "chan hao", "keith", "li ting", "kin yew", "yo hen",
                        "selene", "shou xiang", "shun qi", "melvin", "sonia",
                        "luke", "zhuo heng", "shaun", "nate", "dylan", "bryan",
                        "john", "leon", "maxwell", "maxson", "jodene", "sim",
                        "chiang", "pointer king", "kenneth", "prag", "bunyod",
                        "zhen min", "lynnett", "amanda", "jun han", "thomas",
                        "phat mo", "yong cheng", "miqa", "yu xuan", "kee wan",
                        "meeve", "nicole", "xin min", "faizal", "madinata",
                        "caleb", "jifoo", "jia jiet", "ze hao", "chien seng",
                        "vinson", "wilson", "adam", "zep", "teo", "nicholas"
                        "nichoo", "nilim", "yue deng", "angelyn", "hanson",
                        "jayden", "zhang jing", "jia xuan", "desmond", "tofu",
                        "jeff", "yu ning", "joseph", "harith", "shien shien",
                        "anis", "marcus", "salheen", "asma", "wendy", "rex",
                        "xin jie", "hannah", "raja", "vagner", "bok chuan",
                        "kyle", "chia", "yi jie", "alex", "ben", "cedric"]
    print("=== Game Data Alchemist ===\n")
    initial_list: list[str] = r.sample(names, 10)
    chosen_cap: list[str] = r.sample(initial_list, r.randint(0, 9))
    for i in chosen_cap:
        initial_list[initial_list.index(i)] = i.title()
    print(f"Initial list of players: {initial_list}")
    all_cap: list[str] = [s.title() for s in initial_list]
    only_cap: list[str] = [s for s in initial_list if s == s.title()]
    print(f"New list with all name capitalized: {all_cap}")
    print(f"New list of capitalized names only: {only_cap}")
    score_board: dict[str, int] = {n: r.randint(0, 999) for n in all_cap}
    print(f"Score dict: {score_board}")
    avg: float = round(sum(score_board.values()) / len(score_board), 1)
    print(f"Score average is {avg}")
    print("High scores: ", {n: s for n, s in score_board.items() if s > avg})
