def ft_countdown(days: int) -> None:
    if days > 1:
        ft_countdown(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    ft_countdown(day)
    print("Harvest time!")
