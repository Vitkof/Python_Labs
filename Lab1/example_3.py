import re

# 1-е доп.задание
with open('number.txt', 'r') as f:
    first = f.read()
    f.close()
repos = set([el.strip() for el in first.split()])
b = set(['qwerty', 'slonim', 'minsk'])
repos.update(b)

for el in repos:
    try:
        el = int(el)
    except ValueError:
        continue


def info():
    print(' add <key> [<key> … ] - добавить 1 или более элементов '
          'в хранилище (если уже содержится, то не добавлять)'
          '\n remove <key> - удалить элемент из хранилища'
          '\n find <key> [<key> …] - проверить наличие одного или более '
          'элементов в хранилище, вывести найденные'
          '\n grep <regexp> - поиск значения по регулярному выражению(без кавычек)'
          '\n save - сохранить хранилище в файл'
          '\n load - загрузить хранилище из файла'
          '\n list - вывести все элементы в хранилище'
          '\n exit - выход')


def list():
    print("В хранилище:  " + format(repos))


def add(line):
    args = line.split()[1:]  # слово add не аргумент
    for el in args:  # без доп.списка
        try:
            el_num = int(el)
            args.remove(el)
            args.insert(0, el_num)
        except ValueError:
            continue
    added = set(args)
    repos.update(added)
    print('Добавлено!')


def remove(line):
    arg = line.split()[1]
    try:
        key = int(arg)
    except ValueError:
        key = arg
    try:
        repos.remove(key)
        print('Удален!')
    except KeyError:
        print('Несуществующий ключ (в хранилище нет объекта)')
    except Exception as e:
        print(type(e))
        print(e)


def find(line):
    args = line.split()[1:]
    key = []  # с доп. списком
    for el in args:
        try:
            el = int(el)  # пытаемся преобразовать введеный аргумент в число
            key.append(el)
        except ValueError:
            key.append(el)  # если не выходит, записываем в доп.list как строку

    res = set(key)
    res &= repos
    if len(res) == 0:
        print("Найдено: 0 элементов")
    else:
        print("Найдено:  " + format(res))


# 7-e Доп.задание.
def save():
    print("Сохранить в: ")
    path = input()
    file = open(path, 'w')
    file.write(str(repos))
    file.close()


def load():
    print("Прочитать из: ")
    path = input()
    file = open(path, 'r')
    data = file.read()
    file.close()
    data = set([el.strip() for el in data.split(',')])
    repos.clear()
    repos.update(data)


def grep(line):
    patt = line.split()[1]
    print(patt)
    res = []
    for el in repos:
        match = re.fullmatch(patt, el)
        if match is not None:
            res.append(match.group())

    if len(res) == 0:
        print("Найдено: 0 элементов")
    else:
        print("Найдено:  " + format(res))


print('Chumakov_Repository 1.0.0 (v1.0.0, Feb 6 2020, 15:15:15)')
print('Type "help" for more information.')

while True:
    cmd = input().strip()
    if cmd == 'help':
        info()
    elif cmd == 'list':
        list()
    elif cmd == 'save':
        save()
    elif cmd == 'load':
        load()

    elif cmd == 'add' or cmd == 'remove' or cmd == 'find':
        print('Вы не задали элементы после "{}"'.format(cmd))
    elif cmd == 'grep':
        print('Вы не задали регулярное выражение после grep')

    elif cmd.find('add', 0, 3) == 0 and cmd[3] == ' ':  # второе условие против ввода add345
        add(cmd)

    elif cmd.find('remove', 0, 6) == 0 and cmd[6] == ' ':
        remove(cmd)

    elif cmd.find('find', 0, 4) == 0 and cmd[4] == ' ':
        find(cmd)

    elif cmd.find('grep', 0, 4) == 0 and cmd[4] == ' ':
        grep(cmd)

    elif cmd == 'exit':
        break
    else:
        print('Команда "{}" не поддерживаетя.'.format(cmd))
