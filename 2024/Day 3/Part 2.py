import re
import pathlib

def FindSections(memory:str) -> list[str]:
    pattern = r'(?:mul\(\d{1,3},\d{1,3}\))|(?:don\'t\(\))|(?:do\(\))*'
    sections = re.findall(pattern, memory)
    return sections

def Multiply(section:str):
    v1, v2 = map(int, section.strip('mul()').split(','))
    return v1 * v2

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    memories = file.readlines()

    result = 0
    should_do = True
    for memory in memories:
        sections = FindSections(memory)

        # for mul, dont, do in sections:
        for section in sections:
            if section == '':
                continue
            elif section[0:3] == 'mul' and should_do:
                result += Multiply(section)
            elif section == 'don\'t()':
                should_do = False
            elif section == 'do()':
                should_do = True

    print(result)

Part1()