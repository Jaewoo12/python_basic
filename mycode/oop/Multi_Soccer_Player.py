# 선수명, 선수 포지션, 선수 등번호
names = ['홍길동', '박지성', '손흥민', '둘리', '파이썬']
position = ['MF', 'DF', 'GK', 'FW', 'FW']
back_numbers = [5, 10, 20, 30, 1]

# Class 없이 여러명의 선수 정보를 2차원 배열에 저장
for na,po,ba in zip(names,position,back_numbers):
    print(na, po, ba)

players = [[name, position, back_numbers] for name, position, back_numbers in zip(names,position,back_numbers)]
print(players)
player1 = players[0]

# back_number 를 변경
player1[2] = 20
print(player1)

# SoccerPlayer 클래스를 import

from mycode.oop.python_class import SoccerPlayer

player = SoccerPlayer('dooly','MF',10)
print(player)
print(player.back_number)

players_obj = [SoccerPlayer(name,position, back_numbers)for name,position,back_numbers in zip (names,position,back_numbers)]
print(players_obj)
player1 = players_obj[0]

# back_number 변경
player1.change_back_number(30)
print(player1)