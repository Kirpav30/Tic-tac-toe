game_board = [[" "] * 3 for i in range(3)]
def show_game_board():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {game_board[i][0]} {game_board[i][1]} {game_board[i][2]}")
def greet():
    print("Формат ввода: x y")
    print("x - номер строки")
    print("y - номер столбца")
def ask_coord():
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print("Введите две координаты!")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне диапозона!")
            continue
        if game_board[x][y] != " ":
            print("Клетка занята!")
            continue
        return x, y
def win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if game_board[a[0]][a[1]] == game_board[b[0]][b[1]] == game_board[c[0]][c[1]] != " ":
            print(f"Выиграл {game_board[a[0]][a[1]]}!")
            return True
    return False
greet()
count = 0
while True:
    count += 1
    show_game_board()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = ask_coord()
    if count % 2 == 1:
        game_board[x][y] ="X"
    else:
        game_board[x][y] = "0"
    if win():
        break
    if count == 9:
        print("Ничья!")
        break

