#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        ages: int
    ) -> None:
        self.name = name.capitalize()
        self.height: float = height
        self.ages: int = ages

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.ages} days old")


def ft_garden_data() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("\n=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
