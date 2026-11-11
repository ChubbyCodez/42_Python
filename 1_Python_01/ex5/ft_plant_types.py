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


class Flower(Plant):
    def __init__(
        self,
        name: str = "Flower",
        height: float = 0,
        age: int = 0,
        color: str = "white",
        rate: float = 0.1
    ) -> None:
        super().__init__(name, height, age, rate)
        self.color = color.lower()
        self._bloom: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloom:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str = "Tree",
        height: float = 0.0,
        age: int = 0,
        trunk: float = 0.0,
        rate: float = 0.1
    ) -> None:
        super().__init__(name, height, age, rate)
        self._trunk_diameter = trunk
        self._shade: bool = False

    def produce_shade(self) -> None:
        if not self._shade:
            print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}"
              f"cm long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str = "Vegetable",
        height: float = 0.0,
        age: int = 0,
        season: str = "January",
        value: int = 0,
        rate: float = 0.1
    ) -> None:
        super().__init__(name, height, age, rate)
        self._harvest_season = season.capitalize()
        self._nutritional_value = value

    def _age_grow(self, days: int = 1) -> None:
        print(f"[make {self._name.lower()} grow and age for {days} days]")
        self._nutritional_value += days
        super().age(days)
        super().grow(days)

    def grow(self, days: int = 1) -> float:
        self._age_grow(days)
        return super().get_height()

    def age(self, days: int = 1) -> int:
        self._age_grow(days)
        return super().get_age()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "april", 0, 2.1)
    tomato.show()
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
