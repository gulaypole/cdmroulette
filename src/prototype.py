from generator import genroulette
from modifier import getmodifier
score = 0
money = 0
baraban = genroulette()
while True:
    bet = int(input("Введите ставку CDM (от 0.5 до 2)\n>>> "))
    if bet > 2.0 or bet < 0.5:
        print("Выберите ставку от 0.5 до 2 CDM")
    else: break
while True:
    cond = int(input("1 - Стрелять из пистолета\n2 - Покинуть игру с деньгами\n\n>>> "))
    if cond == 2:
        if money == 0:
            print("Ушел так и не начав? Деньги сохранены, трус.")
        else:
            print(f"Ты получил {money}. Закрываю сессию.")
        break
    elif baraban[0] == 0:
        print(f"Ты выжил!")
        score += 1
        money = float(str(bet*getmodifier(score))[:4])
        print(f"Полученные деньги: {bet}*{str(getmodifier(score))[:4]}={money}")
        baraban = baraban[1:]
    elif baraban[0] == 1 and score == 0:
        print(f"Видимо ты не обладаешь особым везением... Деньги потеряны.")
        break
    elif baraban[0] == 1:
        print(f"Ты проиграл! Потерянные деньги: {bet}\nМог получить: {money}")
        break
    elif score == 5:
        print(f"5 первых пуль оказались безопасными! Вы получили: {money}CDM")
        break