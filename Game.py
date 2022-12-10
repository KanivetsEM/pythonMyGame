import random
from typing import List, Union, Tuple

"""
Определение глобальных переменных
"""
#создаем игровое поле (инициализация)
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


#текущий игрок
current_player = "X"


#победитель
winner = None


#игра
game_running = True


#печатаем игровое поле (отрисовка)
def print_board(board: str):
    """
    Функция отрисовывает поле
    :param board: индекс ячейки
    :return: возвращает нарисованное поле
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#ввод игрока
def player_input(board:int):
    """
    Функция выбора игроком ячейки
    :param board: заменяет пустое значение на значение указанное игроком
    :return: изменяем параметр ячейки на текущего игрока
    """
    inp = int(input("Необходимо выбрать ячейку от 1 до 9:"))
    #проверяем что ячейка доступна для ввода
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Выбранная ячейка занята")


#проверяем победа или проигрыш

#проверка горизонтали
def check_horizontle(board:bool):
    """
    Функция проверки выйгрыша по трем горизонтальным вариантам
    :param board: равенство всех значений в одной из горизонтальных линий и отсутствие пустого значения в линии
    :return: True
    """
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner == board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner == board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner == board[6]
        return True

#проверка вертикали
def check_row(board:bool):
    """
    Функция проверки выйгрыша по трем вертикальным вариантам
    :param board: равенство всех значений в одной из вертикальных линий и отсутствие пустого значения в линии
    :return: True
    """
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner == board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner == board[4]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner == board[2]
        return True

#проверка диагонали
def check_diagonal(board) -> bool:
    """
    Функция проверки выйгрыша по двум диагональным вариантам
    :param board: равенство всех значений в одной из диагоналей и отсутствие пустого значения в данной диагонале
    :return: True
    """
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner == board[0]
        return True
    elif board[2] == board[4] == board[6] and board[6] != "-":
        winner == board[4]
        return True

#проверяем ничью
def check_tie(board)-> bool:
    """
    Функция вычисляет ничью
    :param board: отсутствие пустых ячеек
    :return: False
    """
    if "-" not in board:
        print_board(board)
        print("Ничья!")
        game_running = False


#проверка на победу
def check_win():
    """
    Функция проверяет выполнено ли условие по заполнения вертикали/горизонтали или диагонали
    :return:
    """
    if check_diagonal(board) or check_horizontle(board) or check_row(board):
        print(f"Победил {current_player}")

#смена игрока
def switch_player():
    """
    Функция меняет игрока 
    :return: 
    """
    global current_player
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"


#игра с компьютером
def computer(board):
    """
    Функция вводит случайное значение от "имени" противника после ввода значения игроком
    :param board:
    :return: значение соперника в пустую ячейку
    """
    while current_player == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switch_player()



#игровой цикл
def app():
    """
    Запуск приложения
    :return:
    """
    while game_running:
        print_board(board)
        player_input(board)
        check_win()
        check_tie(board)
        switch_player()
        computer(board)
        check_win()
        check_tie(board)


if __name__ == "__main__":
    app()


n