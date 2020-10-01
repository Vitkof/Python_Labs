import sys
import argparse
import re
from statistics import median


def clean_words(text):
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '«', '»', '"', '[', ']', '-', '—', '„', '“', '']

    w_list = [word.lower() for word in text.split()]  # список с повторами слов
    i = 0
    for word in w_list:
        if word[0] in punctuation:  # если слово начинается с  «  (  [
            if len(word) > 1:  # если не дефис, тире
                word = word[1:]
            else:
                w_list.remove(word)  # удаляем дефис, тире
                i += 1
                continue

        try:
            if word[-3] in punctuation:  # если слово заканчивается   ...
                word = word[:-3]
            elif word[-2] in punctuation:  # если слово заканчивается  ?!  !?  ).
                word = word[:-2]
            elif word[-1] in punctuation:  # если слово заканчивается  )  ]  »  .  !  ?  ,
                word = word[:-1]
            w_list[i] = word
        except Exception:
            i += 1
            continue
        i += 1
    return w_list


def every_word(text):
    words_dict = {}
    w_list = clean_words(text)
    for key in set(w_list):  # множество удаляет повторы слов
        words_dict[key] = str(w_list.count(key))
    for key, value in words_dict.items():
        print("Slovo '{}' vstrechaetsya in text {} raz".format(key, value))


def stata_word(text):
    beta = re.split('; |\?\!|\!\?|\!|\?|\.\.\.|\.|\‽', text)  # сперва проверка на троеточие(спаренные знаки), а затем на одиночные(не наоборот). (‽) - интерробанг
    beta.remove('')  # удаляем пустое после последней точки
    print('\nПредложения: {}'.format(len(beta)))

    total_word = len(clean_words(text))
    count = 0
    for predloz in beta:
        predloz = predloz.strip()
        print(predloz)
        count += 1
    print("________________\nСлов: {}, Предложений: {}, "
          "Cреднее кол-во слов в предложении: {}".format(total_word, count, total_word/count))
    wcount_list = []
    for predloz in beta:
        wcount_list.append(len(clean_words(predloz)))
    print("Cреднее медианное кол-во слов в предложении: {}".format(median(wcount_list)))


def get_ngram(word, n):
    word_ngrams = [word[i:i+n] for i in range(len(word)-n+1)]
    return word_ngrams


def top_ngram(text):
    print("\n* Top-K самых часто повторяющихся буквенных N-грам\n  "
          "Введите K нажмите Enter: [default 10]")
    try:
        k = int(input())
    except:
        k = 10
    print("Введите N нажмите Enter: [default 4]")
    try:
        n = int(input())
    except:
        n = 4
    ngram_dict = {}
    word_list = [word.lower() for word in text.split()]
    ngram_list = []
    for word in word_list:
        ngram_list += get_ngram(word, n)

    for key in set(ngram_list):
        ngram_dict[key] = ngram_list.count(key)

    # переведем в список, чтобы отсортировать
    dict_tolist = [(key, value) for key, value in sorted(ngram_dict.items(), key=lambda el: el[1], reverse=True)]
    print("Top-{0} повторяющихся буквенных {1}-gramm: ".format(k, n))
    for i in range(k):
        print("{0}) '{1}' - {2} raz".format(i + 1, dict_tolist[i][0], dict_tolist[i][1]))




# 6-e Доп.задание  Регулярки
str_email = '\tРазослать предварительный продукт по адресам электронных почт: vitkow@tut.by, alenakastuk9@gmail.com, romaha@nxtmail.ru. ' \
      '\n\tО результатах анализа сообщить на shder@yandex.ru. Информировать о возникающих проблемах. С уважением, Чумаков. В.А.'
email = '[\w.-]+@[\w.-]+\.?[\w]+?'
emails = re.findall(email, str_email)
print("Message: \n"+str_email+ "\n\tE-mails: "+format(emails))


str_float = '0 1 2 3,14159'
float = '[-+]?[0-9]*[,.][0-9]+'
f = re.search(float, str_float)
print("\nFloat number: "+f.group())


str_url = r'https://www.example.com:8080/hello/index.html?arg=val&arg2=val2#fragment'
url = "^([a-z]+)\:\/\/([\w.-]+)\:(\d+)\/([\w./-]+)\?([\w=&+_]+)\#([\w_-]+)$"
match = re.findall(url, str_url)
print("\nСхема: "+match[0][0]+"\nХост: "+match[0][1]+"\nPort: "+match[0][2]+
      "\nURL-путь: "+match[0][3]+"\nПараметры: "+match[0][4]+"\nЯкорь: "+match[0][5])


# 4-е и 2-е Доп.задания. Использовать аргументы командной строки для получения имени файла с данными
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default='data.txt', type=argparse.FileType(mode='r', bufsize=-1))
    return parser

if __name__ == '__main__':
    pars = createParser()
    namespace = pars.parse_args(sys.argv[1:])  # содержит в качестве члена имя нашего параметра
    text = namespace.name.read()
    namespace.name.close()
    print(text)
    every_word(text)
    stata_word(text)
    top_ngram(text)
