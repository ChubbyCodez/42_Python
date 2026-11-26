#!/usr/bin/env python3

import random as r
from typing import Generator as g


def gen_event(names: list[str],
              moves: list[str]
              ) -> g[tuple[str, str], None, None]:
    while True:
        yield (r.choice(names), r.choice(moves))


def consume_event(events: list[tuple[str, str]]
                  ) -> g[tuple[tuple[str, str], list[tuple[str, str]]],
                         None, None]:
    while bool(events):
        yield (events.pop(r.randint(0, len(events) - 1)), events)


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
    moves: list[str] = ["carry", "homework", "mop", "sweep", "touch",
                        "push", "pull", "type", "hit", "punch", "kick",
                        "zip", "sit", "stand", "see", "watch", "trip",
                        "fall", "smoke", "demolish", "destroy", "delete",
                        "smack", "whack", "bait", "run", "jump", "flip",
                        "jog", "sing", "dance", "play", "laugh", "sniff",
                        "cry", "use", "release", "move", "swim", "wave",
                        "climb", "grab", "leave", "enter", "stab", "peek",
                        "dip", "clean", "clear", "yell", "shout", "bow",
                        "lick", "spit", "step", "stomp", "shoot", "eject",
                        "reload", "fire", "attack", "write", "erase", "fry",
                        "pour", "cook", "talk", "throw", "catch", "chop",
                        "crack", "pinch", "cuddle", "hug", "hold", "fold",
                        "break", "wink", "put", "share", "take", "record",
                        "listen", "swallow", "fill", "refill", "submit",
                        "open", "close", "walk", "crawl", "stroll", "roll",
                        "sprint", "slide", "scroll", "kneel", "crouch",
                        "lean", "stretch", "twist", "turn", "spin", "point",
                        "tap", "press", "knock", "pray", "clap", "snap",
                        "rub", "scratch", "pat", "brush", "comb", "shave",
                        "wash", "rinse", "wipe", "organize", "sort", "cut",
                        "stack", "pack", "wrap", "tie", "freeze", "wear",
                        "remove", "dress", "change", "hum", "hang", "shelve",
                        "store", "fetch", "deliver", "lift", "drag", "trade",
                        "borrow", "lend", "place", "balance", "eat", "drink",
                        "weigh", "count", "inspect", "compare", "search",
                        "find", "hide", "seek", "show", "read", "draw",
                        "paint", "print", "scan", "edit", "save", "send",
                        "reply", "call", "text", "browse", "teach", "practice"]
    print("=== Game Data Stream Processor ===")
    events: g[tuple[str, str], None, None] = gen_event(names, moves)
    for i in range(0, 1000):
        n, m = next(events)
        print(f"Event {i}: Player {n} did action {m}")
    ten_events: list[tuple[str, str]] = [next(events) for _ in range(0, 10)]
    for event in consume_event(ten_events):
        print(f"Got event from list: {event[0]}")
        print(f"Remains in the list: {event[1]}")
