#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, plant: str = "tomato", spot: str = "tank") -> None:
        super().__init__(plant)
        self._plant = ""
        self._set_plant(plant)
        self._spot = ""
        self._set_spot(spot)

    def _set_plant(self, plant: str) -> None:
        self._plant = plant

    def _set_spot(self, spot: str) -> None:
        self._spot = spot

    def __caught__(self) -> str:
        return f"Caught {self.__class__.__name__}: "

    def _wilting(self) -> str:
        return self.__caught__() + f"The {self._plant} plant is wilting!"

    def _watering(self) -> str:
        return self.__caught__() + f"Not enough water in the {self._spot}!"

    def __str__(self) -> str:
        return self._wilting() + "\n" + self._watering()


class PlantError(GardenError):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return super()._wilting()


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return super()._watering()


def ft_custom_errors(error: int) -> None:
    try:
        if error == 0:
            raise PlantError
        elif error == 1:
            raise WaterError
        elif error == 2:
            raise GardenError
        else:
            raise Exception
    except (PlantError, WaterError) as e:
        print(f"Testing {e.__class__.__name__}...")
        print(e)
    except GardenError as e:
        print("Testing catching all garden errors...")
        print(e)
    except Exception:
        print("Unknown plant error")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    for i in range(0, 3):
        ft_custom_errors(i)
        print("")
    print("All custom error types work correctly!")
