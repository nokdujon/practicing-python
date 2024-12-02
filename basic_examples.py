"""essential examples"""


def using_print() -> None:
    """_examples of using the print function_"""

    favorite_player: str = "Dennis Bergkamp"
    favorite_number: int = 10
    favorite_football_club: str = "Arsenal FC"

    # print(*values: object, sep: str | None = " ", end: str | None = '\n')
    print("a", "b")  # a b
    print("c", "d", sep=", ")  # c, d
    print("e", "f", sep="; ", end=" ^^ ")  # e; f ^^
    print("g", "h")  # g h
    # a b
    # c, d
    # e; f ^^ g h

    print(
        "My favorite number is {1} because I like {0}.".format(
            favorite_player, favorite_number
        )
    )

    print(f"My favorite football club is {favorite_football_club}.")  # Support for 3.6+
