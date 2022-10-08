import random

Камень ="""
    _______
---|   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Бумага = """
     _______
---/    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Ножницы = """
    _______
---|   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while True:
    game_img=[Камень, Бумага, Ножницы]
    print(game_img[0],game_img[1],game_img[2])
    user_choise = int(input('Что вы выбираете? Выберите 0 для камня, 1 для бумаги и 2 для ножниц:'))
    print(game_img[user_choise])
    print(40*"-")
    computer_choise = random.randint(0,2)
    print(game_img[computer_choise])
    print(40*"-")
    if computer_choise > user_choise:
            print('Computer win!')
    elif user_choise < computer_choise:
            print('User win!')
    elif computer_choise == 2 and user_choise == 0:
            print('User win!')
    elif computer_choise == 0 and user_choise == 2:
            print('Computer win!')
    if user_choise == computer_choise:
            print('Try again!')
        
