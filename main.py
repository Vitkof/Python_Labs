import sys
import argparse
#from Lab1 import example_2
#from Lab1 import example_3

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default='1')
    return parser

if __name__ == "__main__":
    pars = createParser()
    namespace = pars.parse_args(sys.argv[1:])
    print(namespace)
    print(namespace.n)
    if namespace.n == '1':
        from Lab1 import example_1
        text = 'Afganistan, afganistan - strana gor, duhov i modjahedov. ' \
               'Anglichane ne zahvatili v 19 veke. Stolica - gorod Kabul.'
        example_1.every_word(text)
    elif namespace.n == '2':
        from Lab1 import example_2
    elif namespace.n == '3':
        from Lab1 import example_3
    elif namespace.n == '4':
        from Lab1 import example_4
    else:
        print('Подпрограмм всего 4!')
