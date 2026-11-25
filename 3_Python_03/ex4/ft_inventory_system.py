#!/usr/bin/env python3

import sys as s


class InventoryError(Exception):
    def __init__(self, message: str = "Unknown inventory error") -> None:
        super().__init__(message)
        self._message = message

    def __str__(self) -> str:
        return self._message


class InvalidParameter(InventoryError):
    def __init__(self, para: str = "Unknown parameter error") -> None:
        super().__init__(f"Error - invalid parameter: '{para}'")

    def __str__(self):
        return super().__str__()


class InvalidQuantity(InventoryError):
    def __init__(self, num: int = 0):
        super().__init__(f"Error - quantity should be at least 1, given {num}")

    def __str__(self):
        return super().__str__()


class RedundantItem(InventoryError):
    def __init__(self, loot: str = "Unknown redundancy error"):
        super().__init__(f"Redundant item '{loot}' - discarding")

    def __str__(self):
        return super().__str__()


# invalid syntax, redundant parameters, etc.
class InventorySystem:
    def __init__(self, input: list[str]) -> None:
        self._player_inventory: dict[str, int] = {}
        if len(input) < 2:
            return
        for i in input[1:]:
            self.slot_validation(i)

    def slot_validation(self, weapon: str) -> None:
        try:
            slot: dict[str, int] = {}
            if weapon.count(":") != 1:
                raise InvalidParameter(weapon)
            loot: str = weapon.split(":")[0]
            if loot in self._player_inventory.keys():
                raise RedundantItem(loot)
            slot[loot] = int(weapon.split(":")[1])
            if slot[loot] < 1:
                raise InvalidQuantity(slot[loot])
            self._player_inventory.update(slot)
        except (InvalidParameter,
                InvalidQuantity,
                RedundantItem,) as e:
            print(e)
        except ValueError as e:
            print(f"Quantity error for '{loot}': {e}")

    def add_slot(self, slot: str) -> None:
        self.slot_validation(slot)

    def get_inventory(self) -> dict:
        return self._player_inventory


def most_abundant(storage: dict[str, int]) -> str:
    item_max: str = ""
    max: int = 0
    for k, v in storage.items():
        if max == 0:
            item_max = k
            max = v
            pass
        if v > max:
            item_max = k
            max = v
    return item_max


def least_abundant(storage: dict[str, int]) -> str:
    item_min: str = ""
    min: int = 0
    for k, v in storage.items():
        if min == 0:
            item_min = k
            min = v
            pass
        if v < min:
            item_min = k
            min = v
    return item_min


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: InventorySystem = InventorySystem(s.argv)
    player_a: dict[str, int] = inventory.get_inventory()
    if not bool(player_a):
        print("Please provide valid inputs with the following format: "
              "<item_name>:<quantity>")
        s.exit()
    print(f"Got inventory: {player_a}")
    print(f"Item list: {player_a.keys}")
    total: int = sum(player_a.values())
    print(f"Total quantity of the {len(player_a.keys())} items: {total}")
    for k, v in player_a.items():
        print(f"Item {k} represents {round(v / total * 100, 1)}%")
    # Since max() and min() wasn't mentioned to be allowed...
    most: str = most_abundant(player_a)
    least: str = least_abundant(player_a)
    print(f"Item most abundant: {most} with quantity {player_a[most]}")
    print(f"Item least abundant: {least} with quantity {player_a[least]}")
    inventory.add_slot("magic_item:1")
    player_a = inventory.get_inventory()
    print(f"Updated inventory: {player_a}")
