def ft_water_reminder() -> None:
    last_water = int(input("Days since last watering: "))
    if last_water < 3:
        print("Plants are fine")
    else:
        print("Water the plants")
