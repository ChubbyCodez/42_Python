#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str = "Plant",
        height: float = 0,
        ages: int = 0,
        rate: float = 0.1
    ) -> None:
        self.name = name.capitalize()
        self.height = height
        self.ages = ages
        self.rate = rate

    def age(self, days: int) -> int:
        self.ages += days
        return self.ages

    def grow(self, days: int) -> float:
        self.height = round(self.height + days * self.rate, 1)
        return self.height

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.ages} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plants: list[Plant] = []
    plants.append(Plant('Rose', 25, 30))
    plants.append(Plant('Oak', 200, 365))
    plants.append(Plant('Cactus', 5, 90))
    plants.append(Plant('Sunflower', 80, 45))
    plants.append(Plant('Fern', 15, 120))
    for i in plants:
        print(f"Created: {plants}", end="")
        i.show()


if __name__ == "__main__":
    ft_plant_factory()
