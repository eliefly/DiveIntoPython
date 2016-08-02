import re
import itertools

def solve(puzzle):
    # re.findall() 函数找到谜题中的所有单词
    words = re.findall('[A-Z]+', puzzle.upper())
    # set 函数找到谜题中出现的所有不同的字母
    unique_characters = set(''.join(words)) # 集合不允许重复，且无序
    # assert 语句检查是否超过10个不同的字母，否则无解
    assert len(unique_characters) <= 10, 'Too mamy letters'
    # 把单词的字母放在前面，后续判断是否映射的是0
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)

    # 通过一个生成器对象将字符转换成对应的ASCII码值
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')

    zero = digits[0] # zero 字符0的ascii码值
    # permutations 排列组合，计算所有可能的解法
    for guess in itertools.permutations(digits, len(characters)):
        # 0不是映射的 first_letters
        if zero not in guess[:n]: 
            # zip() 创建一个字母-数字对的迭代器，dict() 得到得到字母为键，对应数字为值的字典
            # translate() 依据字典转换表把所有可能的解转换成Python表达式
            equation = puzzle.translate(dict(zip(characters, guess)))
            # eval 通过求值Python 表达式来检验解法
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)  

# E:\DiveIntoPython\chapter 09-Super Iterator>python alphametics.py "HAWAII + IDAHO + IOWA + OHIO == STATES"
# HAWAII + IDAHO + IOWA + OHIO == STATES
# 510199 + 98153 + 9301 + 3593 == 621246