# пока не вышло по красивому
pushkin = {
    'year': 1799,
    'day': 6
}

def bornday(pushkin):
    year = input('Введите год рождения А.С.Пушкина:')
    while year != '1799':
        print("Не верно")
        year = input('Введите год рождения А.С.Пушкина:')

    day = input('Введите день рождения Пушкинa?')
    while day != '6':
        print("Не верно")
        day = input('В какой день июня родился Пушкин?')
    print('Верно')

bornday(pushkin)

# пытался связать  функцию с работой списка
def function(pushkin):
    year = input('Ввведите год рождения А.С.Пушкина:')
    for year in pushkin.values():
        if year == pushkin['year']:
            print('Верно')
        else: year = input('Ввведите год рождения А.С.Пушкина:')
    day = input('Ввведите день рождения Пушкин?')
    for day in pushkin.values():
        if day == pushkin['day']:
            print('Верно')
            #elif day = input('Ввведите день рождения Пушкин?')
        else: print("Не верно")

pushkin = {
    'year': 1799,
    'day': 6
}
print(function(pushkin))
