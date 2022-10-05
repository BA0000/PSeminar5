
# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# original_text = "вабв этомабв текстеабв слишкомабв много лишнегоабв абв"
# print("Изначальный текст: " + original_text)

# rem_text = original_text.replace('абв', '') 
# print("Текст после удаления всех абв: " + rem_text) 


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. 
#    Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#    Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random
# from random import randint, choice
 
# print('На столе лежит 2021 конфета.\n Играют два игрока делая ход друг после друга.\n Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем 28 конфет.\n Игрок 1 - человек, игрок 2 - бот')
 
# messages = ['Ваш ход', 'Возьмите конфеты',
#             'сколько конфет берете?', 'берите еще', 'Ваш ход']
# max_number_move = 0
 
# def two_players():
#     player1 = input('Первый игрок, представьтесь: ')
#     player2 = 'SmartBOT'
#     print(f'Здравствуйте{player1}, Вы играете с ИИ {player2}')
#     return [player1, player2]
 
# def game(players):
#     global max_number_move
#     total_sweets = int(input('Введите cколько всего у нас конфет: '))
#     max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход: '))
#     first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу'))
#     if first != 1:
#         first = 0
#     return [total_sweets, max_number_move, int(first)]
 
# max_move = max_number_move
 
# def game_player_vs_smart_bot(sweets, players, messages):
#     global max_number_move
#     count = sweets[2]
 
 
#     while sweets[0] > 0:
#         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#             move = sweets[0] -1
#             print(f'Я забираю {move}')
 
#         elif not count % 2:
#             move = random.randint(1, sweets[1])
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > sweets[0] or move > sweets[1]:
#                 print(
#                     f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                 chance = 2
#                 while chance > 0:
#                     if sweets[0] >= move <= sweets[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                     move = int(input())
#                     chance -= 1
#                 else:
#                     return print(f'Попыток не осталось. Game over!')
#         sweets[0] = sweets[0] - move
#         if sweets[0] > 0:
#             print(f'Осталось {sweets[0]} конфет')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
 
 
# players = two_players()
# sweets = game(players)
 
# winer = game_player_vs_smart_bot(sweets, players, messages)
# if not winer:
#     print('Нет победителя.')
# else:
#     print(f'Победил {winer}!')


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1,10))

# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Введите число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Клетка занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "Победа!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)



# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.



                                                             # НЕ СДЕЛАЛ


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------














































