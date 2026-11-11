def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    units = unit.lower()
    if units == "packets":
        print(f"{seed} seeds: {quantity} {units} available")
    elif units == "grams":
        print(f"{seed} seeds: {quantity} {units} total")
    elif units == "area":
        print(f"{seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
