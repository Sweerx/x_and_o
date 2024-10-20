from app import player_select, get_base, base, move_selection_and_game_logic


def main():

    print("Игра крестики и нолики, попробуй победить!")

    player_one = player_select("X")
    player_two = player_select("O")

    print(f"*********** {player_one}, {player_two} ***********")

    main_base = get_base(base)

    move_selection_and_game_logic(main_base, player_one, player_two)


if __name__ == "__main__":

    main = main()
