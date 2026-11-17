#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self._message = message

    def __str__(self) -> str:
        return f"Caught {self.__class__.__name__}: {self._message}"


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()


def ft_custom_errors() -> None:
    plant: str = "The tomato plant is wilting!"
    tank: str = "Not enough water in the tank!"
    print("=== Custom Garden Errors Demo ===")
    for i in range(0, 3):
        try:
            if i == 0:
                raise PlantError(plant)
            elif i == 1:
                raise WaterError(tank)
            elif i == 2:
                raise GardenError
        except (PlantError, WaterError) as e:
            print(f"\nTesting {e.__class__.__name__}...")
            print(e)
        except GardenError:
            print("\nTesting catching all garden errors...")
            print(GardenError(plant))
            print(GardenError(tank))
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
