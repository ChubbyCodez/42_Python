#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str = "Plant",
        height: float = 0.0,
        age: int = 0,
        rate: float = 0.1
    ) -> None:
        self._name = ""
        self.set_name(name)
        self._height = -1.0
        self.set_height(height)
        self._age = -1
        self.set_age(age)
        self._rate: float = -1.0
        self.set_rate(rate)

    def age(self, days: int = 1) -> int:
        self._age += days
        return self._age

    def grow(self, days: int = 1) -> float:
        self._height += self._rate * float(days)
        return self._height

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_rate(self) -> float:
        return self._rate

    def set_name(self, name: str) -> None:
        initial: bool = False
        if self.get_name() == "":
            initial = True
        if name.strip() != "":
            self._name = name.capitalize()
            if not initial:
                print(f"Name updated: {self._name}")
        else:
            self._name = self._name if self._name != "" else "Plant"
            print(f"{self._name}: Error, name can't be empty")
            print("Name update rejected")

    def set_height(self, height: float) -> None:
        initial: bool = False
        if self.get_height() == -1.0:
            initial = True
        if height >= 0:
            self._height = height
            if not initial:
                print(f"Height updated: {round(self._height, 1)}cm")
        else:
            self._height = self._height if self._height >= 0.0 else 0.0
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        initial: bool = False
        if self.get_age() == -1:
            initial = True
        if age >= 0:
            self._age = age
            if not initial:
                print(f"Age updated: {self._age} days")
        else:
            self._age = self._age if self._age >= 0 else 0
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_rate(self, rate: float) -> None:
        initial: bool = False
        if self.get_rate() == -1.0:
            initial = True
        if rate >= 0:
            self._rate = rate
            if not initial:
                print(f"Rate updated: {round(self._rate, 1)}cm per day")
        else:
            self._rate = self._rate if self._rate >= 0.0 else 0.0
            print(f"{self._name}: Error, rate can't be negative")
            print("Rate update rejected")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-25)
    rose.set_age(-30)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
