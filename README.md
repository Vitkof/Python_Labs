# Python_Labs
my BSUIR labs. Language: Python

### Lab_1
**1. Статистики по тексту.** 
На вход поступают текстовые данные. Необходимо
посчитать и вывести:
- сколько раз повторяется каждое слово в указанном тексте
- среднее количество слов в предложении
- медианное количество слов в предложении
- top-K самых часто повторяющихся буквенных N-грам (K и N имеют значения
по-умолчанию 10 и 4, но должна быть возможность задавать их с
клавиатуры)
            <p>При решении использовать контейнер <i>dict()</i> или его аналоги и встроенные
операции над строками. Предусмотреть обработку знаков препинания.</p>

**2. Сортировки.** 
    На вход поступает строка содержащая числа разделённые
    пробелами. На выходе будут отсортированные по возрастанию числа. Необходимо
    реализовать алгоритмы:
- быстрой сортировки
- сортировки слияниями (при решении воспользоваться механизмом срезов
(слайсы, slices))
- поразрядной сортировки
<p>Необходимо знать алгоритмическую сложность реализованных алгоритмов.</p>

**3. Хранилище уникальных элементов.** 
При запуске программа работает в
интерактивном режиме и поддерживает команды:
            - add <key> [<key> … ] - добавить один или более элементов в хранилище
(если уже содержится, то не добавлять).
            - remove <key> - удалить элемент из хранилища.
            - find <key> [<key> …] - проверить наличие одного или более элементов в
хранилище, вывести найденные.
            - list - вывести все элементы в хранилище.
    <p>При решении использовать контейнер set().</p>
    
**4. Генератор чисел Фибоначчи.** 
Написать генератор возвращающий последовательно
числа Фибоначчи начиная с первого.

[h3][i]Дополнительные задания:[/i][/h3]

**5.**      Читать входные данные для каждого из заданий описанных выше из файла с
фиксированным именем. При работе с файлами воспользоваться контекстным
оператором with. (1 балл)

**6.**      Использовать аргументы командной строки для получения имени файла из
которого читать входные данные. (1 балл)

**7.**      Объединить все описанные выше задания в одну программу и определять то,
какую подпрограмму запускать, с помощью аргументов командной строки. (1 балл)

**8.**      Использовать модуль argparse для работы с аргументами командной строки. (1
балл)

**9.**      Оформить лабораторную как Python-модуль с возможность использования
отдельных заданий и функций в других модулях. (1 балл)

**10.**     Изучить модуль re и написать регулярные выражения для:
<p>○ валидации email-адреса (1 балл)</p>
<p>○ валидации записи числа с плавающей строчкой (1 балл)</p>
<p>○ получения отдельных частей URL (схема, хост, порт, путь, параметры) с
помощью механизма именованных групп (3 балла)</p>

**11.**     Для третьего задания реализовать команды:
<p>○ grep <regexp> - поиск значения по регулярному выражению. (1 балл)</p>
<p>○ save и load - сохранить хранилище в файл и загрузить хранилище из файла
(1 балл)</p>

### Lab_2

**1. Сортировка большого объема данных.**
- Написать программу для сортировки данных не помещающихся в
оперативную память.
- В качестве входных данных выступает файл с текстовыми данными (или
сами данные), в качестве выходных – один сортированный файл (или сами
данные).
- Файлы могут быть очень большие и превышать объем доступной
оперативной памяти на порядок.
- Входные данные представляют собой последовательность ascii строк,
каждая из которых оканчивается символом разделителя строк
(по-умолчанию \n, но должна быть возможность изменить с помощью
аргумента командной строки --line-separator=’символ_разделитель’).
- Каждая строка состоит из последовательностей символов разделённых
символом разделителя частей строки (по-умолчанию \t, но должна быть
возможность изменить с помощью аргумента командной строки -t
‘символ_разделитель’ или --field-separator=’символ_разделитель’).</li>
- С помощью аргумента командной строки (-k 1,2,5; --key 1,2,5) можно
перечислить индексы частей строки используемых для сортировки
(по-умолчанию используются все позиции).
- С помощью аргумента командной строки можно указать интерпретировать
части строки как числа (-n, --numeric).
- С помощью аргумента командной строки --reverse можно указать сортировку
в обратном порядке.
- С помощью аргумента командной строки можно указать режим проверки
сортированности --check: в этом режиме сортировка не производится, а
входные данные просто проверяются на отсортированность согласно
правилам указанным в аргументах командной строки.
- Данные в файле сортируются построчно (меняется порядок строк).
- Порядок сортировки определяется с помощью частей строки в соответствии
с указанными аргументами (или их значениями по-умолчанию).
- Строки сортируются в лексикографическом порядке на основе частей
строки описанных разделителями.
- Пример сортировки двух строк (спец. символы и кавычки написаны явно для
примера):
“cc\tbb\taa\ncc\taa\tbb\naa\tbb\tcc\n” -> “aa\tbb\tcc\ncc\taa\t\bb\ncc\tbb\taa\n”
- Промежуточные результаты рекомендуется хранить во временных файлах
(обратите внимание на модуль tempfile), а саму сортировку – делать с
помощью сортировки слиянием с использованием фиксированного буфера
в памяти (размер буфера можно указать в качестве аргумента командной
строки --buffer-size=число_байт).</li>
- Интерфейс использования:
cat in.txt | python sort.py > out.txt # читаем данные из стандартного ввода и выводим
на стандартный вывод
python sort.py --input in.txt --output out.txt # читаем из файла и пишем результат в
файл

**2. Написать программу генерирующую входной файл (произвольного размера)**         для
задачи сортировки больших файлов описанной выше. Файл должен
соответствовать спецификации указанной в этой задаче. Должна быть
возможность с помощью аргументов командной строки изменить вид
генерируемых файлов:
<p>○ Фиксированное или переменное количество полей в одной строке.</p>
<p>○ Числа или произвольные ascii текстовые данные в качестве полей строки.</p>
<p>○ Разделитель полей в строке.</p>
<p>○ Разделитель строк.</p>
<p>○ Количество строк.</p>

**3. Свой преобразователь в JSON.** 

Реализовать функцию to_json(obj), которая на вход
получает python-объект, а на выходе у неё строка в формате JSON. Создать
собственное исключение (унаследовав от подходящего встроенного), которое
должно выбрасываться при попытке преобразования неизвестного типа, но только
если при вызове to_json был передан опциональный параметр raise_unknown=True
(по-умолчанию False). В исключении должна сохраняться информация о типе,
которые попытались преобразовать: этот тип должен выводиться при
преобразовании исключения в строковое представление.

**4. Класс “n-мерный вектор”.** 

У этого класса должны быть определены все
естественные для вектора операции – сложение, вычитание, умножение на
константу и скалярное произведение, сравнение на равенство. Кроме этого
должны быть операции вычисления длины, получение элемента по индексу, а
также строковое представление.

**5. Класс логгер с возможностью наследования.** 

Класс должен логировать то, какие
методы и с какими аргументами у него вызывались и какой был результат этого
вызова. Функция str() от этого класса должна отдавать лог вызовов. Должна быть
возможность унаследоваться от такого класса, чтобы добавить логгирование
вызовов у любого класса. При форматировании строк использовать метод format.

**6. Рекурсивный defaultdict.** 

Реализовать свой класс-аналог defaultdict, который
позволяет рекурсивно читать и записывать значения в виде d[“a”][“b”] = 1, а при
вызове str(d) выводит данные как словарь в текстовом представлении.

**7. Метакласс берущий поля класса из файла.** 

Реализовать метакласс, который
позволяет при создании класса добавлять к нему произвольные аттрибуты (классу,
не экземпляру класса), которые загружаются из файла. В файле должны быть
имена аттрибутов и их значения. Нужно уметь передавать путь к файлу как
изменяемый параметр.

**8. Декторатор @cached.** 

Kоторый сохраняет значение функции при каждом вызове.
Если функция вызвана повторно с теми же аргументами, то возвращается
сохраненное значение, а функция не вычисляется.

**9. Свой xrange.** 

Реализовать полностью свой xrange с аналогичным встроенному
интерфейсом.

**10. Последовательность с фильтрацией.** 

Реализовать класс, соответствующий
некоторой последовательности объектов и имеющий следующие методы:
<p>○ Создать объект на основе произвольного iterable объекта.</p>
<p>○ Итерирование (__iter__) по элементам (неистощаемое – можно несколько
раз использовать объект в качестве iterable для for).</p>
<p>○ Отфильтровать последовательность с помощью некоторой функции и
вернуть новую сокращенную последовательность, в которой присутствуют
только элементы, для которых эта функция вернула True.</p>
Будем считать, что в данной задаче основным приоритетом является экономия
памяти. Поэтому количество копирований данных нужно свести к минимуму
(возможно, пожертвовав скоростью работы): например, если применим несколько
раз по цепочке операции фильтрации, то данные об элементах
последовательности не должны дублироваться.

[h3][i]Дополнительные задания[/i][/h3]

**1. Свой преобразователь из JSON.**             Реализовать функцию from_json(text), которая
возвращает python-объект соответствующий json-строке. Не использовать
стандартные инструменты работы с JSON. (4 балла)

**2. Синглтон.**         Реализовать шаблон проектирования Singleton, который можно
применять на произвольный класс. Разработать самостоятельно, как этот
инструмент будет применяться к целевому классу (например, модифицировать
исходный класс или изменять способ вызова конструктора). (2 балла)

**3. Поддержка параметризованных форматов вывода для класса-логгера.**
Параметры можно зафиксировать зарание (имя функции, имена аргументов, возвращаемое
значение и др.) или придумать как это можно давать задавать пользователю. (1
балла)

**4. Метакласс model creator.**      Реализуйте метакласс ModelCreator, позволяющий
объявлять поля класса в следующем виде:
class Student ( object ):
__metaclass__ = ModelCreator
name = StringField ()
Здесь StringField — некоторый объект, который обозначает, что это поле является
текстовым. После такого вызова должен быть создан класс, конструктор которого
принимает именованный аргумент name и сохраняет его в соответствующий
атрибут (с возможной проверкой и приведением типа). Таким образом должна
быть возможность писать так:
s = Student (name =’abc’)
print s.name
Постарайтесь добиться того, чтобы создание класса было как можно более гибким:
чтобы допускалось наследование и т.п. Обязательно должна быть проверка типов
(например, в текстовое поле нельзя записать число). (4 балла)

**5. Юниттесты.**       Использовать любой фреймворк для тестирования (unittest, nose,
pytest). Использовать модуль coverage для оценки покрытия кода тестами. На
каждое основное задание написать 2+ тестов (корректная работа, некорректная
работа). (3 балла)

**6. Реализовать свой устанавливаемый (setup.py)**          пакет со всеми заданиями этой
лабораторной, разбитой на модули. Описать зависимости, указать скрипты для
запуска заданий из каждого пункта. После установки они должны вызываться как
системные команды ( user@host: lab2_task1.py ). (3 балла)
