import re


def calc(v):
    # print(bool(re.match('[0-9+-/()*]+', '2+a')))
    if re.match('[0-9+-/()*]+$', v):
        res = eval(v)
        return res
    else:
        return 'Не верный формат'

if __name__ == '__main__':
    inp = input('Введите арифметическое выражение: ')
    print(calc(inp))