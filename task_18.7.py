import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести список должников по предметам
        5. Удалить и редактировать данные по оценкам, предметам и ученикам
        6. Вывести информацию по всем оценкам для определенного ученика
        7. Вывести средний балл по каждому предмету по определенному ученику
        8. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Вывести список должников по предметам')
        for student in students:
            print(student)
            for class_ in classes:
                all_marks = students_marks[student][class_]
                needed_marks = []
                for mark in all_marks:
                    if mark < 3:
                        needed_marks.append(mark)
                print(f'\t{class_} - {needed_marks}')

    elif command == 5:
        print('''
                Выберите команду:
                1. Удалить и редактировать данные по оценкам
                2. Удалить и редактировать данные по ученикам
                3. Удалить и редактировать данные по предметам
                4. Выход из программы
                   ''')
        while True:
            command = int(input('Введите команду: '))
            if command == 1:
                print('1. Удалить и редактировать данные по оценкам')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    print(f'Оценки {student} по предмету {class_}: {students_marks [student][class_]}')
                    edited_mark = int(input('Какую оценку нужно удалить: '))
                    students_marks[student][class_].remove(edited_mark)
                    new_mark = int(input('Введите новую оценку: '))
                    students_marks[student][class_].append(new_mark)
                    print(f'Актуальные оценки {student} по предмету {class_}: {students_marks[student][class_]}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')

            if command == 2:
                print('2. Удалить и редактировать данные по ученикам')
                delete_student = input('Введите имя ученика, которого нужно удалить: ')
                new_student = input('Введите имя нового ученика: ')
                if delete_student in students:
                    del students_marks[delete_student]
                else:
                    print('ОШИБКА: неверное имя ученика')
                students_marks[new_student] = classes
                print(f'Ученик {delete_student} удален из списка. Добавлен новый ученик {new_student}')
                print(f'Список всех учеников: {list(students_marks.keys())}')

            if command == 3:
                print('3. Удалить и редактировать данные по предметам')
                student = input('Введите имя ученика для удаления предмета: ')
                delete_class = input('Введите предмет, который нужно удалить: ')
                new_class = input('Введите название нового предмета: ')
                if student in students_marks.keys() and delete_class in students_marks[student].keys():
                    students_marks[student][new_class] = students_marks[student][delete_class]
                    students_marks[student].pop(delete_class)
                    print(f'Список всех предметов после изменений: {students_marks}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')

            elif command == 4:
                print('4. Выход в предыдущее меню')
                break

    elif command == 6:
        print('6. Вывести информацию по всем оценкам для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Оценки {student} по всем предметам:')
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 7:
        print('7. Вывести средний балл по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'\t{class_} - {marks_sum // marks_count}')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 8:
        print('8. Выход из программы')
        break

