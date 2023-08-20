from class_parser import undergraduate, graduate, Parser

# name = '199-637-080 37'
# url = "https://pnzgu.ru/apply/list/faculty/31429808/speciality/2648/edu_level/3/edu_form/1/edu_base/1/sort_field/name/sort_type/asc/"
# education_level = '2'


def take_points(elem):
    return int(elem[1])


def main():

    print('Вставьте ссылку со списками: ')
    url = input()
    url += "p/"

    print('Введите уровень образования (цифрой): \n1. Бакалавриат \n2. Магистратура')

    while True:
        education_level = input()
        if education_level == '1':
            education_level = undergraduate
            break
        if education_level == '2':
            education_level = graduate
            break
        else:
            print('Неверно введённый формат данных, пожалуйста, введите снова.')

    print('Введите ваш СНИЛС: ')

    name = input()

    parser = Parser(url, education_level)

    data = parser.parsing_page()

    data.sort(key=take_points, reverse=True)

    position = -1
    for d in data:
        if name in d:
            position = data.index(d)
        print(f'{data.index(d)+1}. СНИЛС: {d[0]}, Количество баллов: {d[1]}')

    if position != -1:
        print(f'Вы находитесь на {position+1}-м месте.')
    else:
        print(f'Ваш СНИЛС не был найден в списке.')


if __name__ == '__main__':
    main()
