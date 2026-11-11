#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str = "Plant",
        height: float = 0,
        ages: int = 0,
        rate: float = 0.1
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.ages: int = ages
        self.rate: float = rate

    def age(self, days: int) -> int:
        self.ages += days
        return self.ages

    def grow(self, days: int) -> float:
        self.height = round(self.height + days * self.rate, 1)
        return self.height

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.ages} days old")


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30, 0.8)
    rose.show()
    old_cm: float = rose.height
    for i in range(1, 8):
        rose.age(1)
        rose.grow(1)
        print(f"=== Day {i} ===")
        rose.show()
    print(f"Growth this week: {rose.height - old_cm:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
