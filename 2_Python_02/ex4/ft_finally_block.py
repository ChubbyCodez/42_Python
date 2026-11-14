#!usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self._message = message

    def __str__(self) -> str:
        return f"Caught {self.__class__.__name__}: {self._message}"


class PlantError(GardenError):
    def __init__(self, plant: str = "tomato") -> None:
        super().__init__()
        self._plant = ""
        self._set_plant(plant)
        self._message = f"Invalid plant name to water: '{self._plant}'"

    def _set_plant(self, plant: str) -> None:
        self._plant = plant

    def __str__(self) -> str:
        return super().__str__()


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(plant_name)


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for i in ("Tomato", "Lettuce", "Carrots"):
            water_plant(i)
            print(f"Watering {i}: [OK]")
    except PlantError as e:
        print(f"{e}\n.. ending test and returning to main")
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        for i in ("Tomato", "lettuce", "Carrots"):
            water_plant(i)
            print(f"Watering {i}: [OK]")
    except PlantError as e:
        print(f"{e}\n.. ending test and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
