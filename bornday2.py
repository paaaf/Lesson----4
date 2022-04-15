def question_date(question, date):
    answer = input(question)
    while answer != date:
        print('Не верно')
        answer = input(question)

question_date('Введите год рождения А.С.Пушкина:', '1799')
question_date('Введите день рождения Пушкинa?', '6')
print('Верно')