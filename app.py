import re
import random


base = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_base(base: list) -> list:
    print(" ")
    print(*base[:3])
    print(*base[3:6])
    print(*base[6:9])

    return base


def player_select(symbol: str) -> str:

    while True:
        print(f"Введите имя игрока({symbol}): ")
        player_list = input().split(" ")
        player = "".join(player_list)
        search_int = re.findall(r"\d+", player)

        if search_int:
            print("Имя не может состоять из цифр!")
        else:
            if player == "":
                print("Ой! Нельзя вводить пустую строку. Пожалуйста повторите ввод!")
            elif 2 >= len(player):
                print("Ой! Имя должно быть не меньше 3х букв!")
            else:
                print(f"Игрок с именем {player} играет за {symbol}\n")
                return player


def win(y: str, main_base: list) -> bool:

    # Горизонтальные линии
    if main_base[0:3] == [y, y, y] or main_base[3:6] == [y, y, y] or main_base[6:9] == [y, y, y]:
        return True

    # Вертикальные линии
    if (
        [main_base[0], main_base[3], main_base[6]] == [y, y, y]
        or [main_base[1], main_base[4], main_base[7]] == [y, y, y]
        or [main_base[2], main_base[5], main_base[8]] == [y, y, y]
    ):
        return True

    # Диагонали
    if [main_base[0], main_base[4], main_base[8]] == [y, y, y] or [main_base[2], main_base[4], main_base[6]] == [
        y,
        y,
        y,
    ]:
        return True

    return False


def check_draw(main_base: list) -> bool:

    if all(isinstance(cell, str) for cell in main_base):  # Если все клетки уже заняты (строковое значения)
        return True
    return False


def move_selection_and_game_logic(base: list, x: str, o: str) -> None:

    print("\nТасуем, колдуем, решаем кто будет ходить..")

    players = [x, o]

    random.shuffle(players)

    if players[0] == x:
        print(f"\nХодит: {players[0]} за Х\n")

    else:
        print(f"\nХодит: {players[0]} за O\n")

    game = True

    while game:

        if players[0] == x:
            player = "X"
            try:
                user_input = int(input(f"\nВведите цифру, ходит {players[0]}\n"))
                for i, k in enumerate(base, start=1):
                    if k == user_input:
                        base[user_input - 1] = player
                        players[0] = o
                        players[1] = x
                        get_base(base)
                        if win("X", base) == True:
                            print(f"\nПобедил игрок {players[1]}")
                            game = False
                        if check_draw(base) == True:
                            print(f"\nНичья! Победила дружба!)")
                            game = False

            except ValueError:
                print("Неправильно, нужно ввести число!")

        elif players[0] == o:
            player = "O"
            try:
                user_input = int(input(f"\nВведите цифру, ходит {players[0]}\n"))
                for i, k in enumerate(base, start=1):
                    if k == user_input:
                        base[user_input - 1] = player
                        players[0] = x
                        players[1] = o
                        get_base(base)
                        if win("O", base) == True:
                            print(f"\nПобедил игрок {players[1]}")
                            game = False
                        if check_draw(base) == True:
                            print(f"\nНичья! Победила дружба!)")
                            game = False
            except ValueError:
                print("Неправильно, нужно ввести число!")
