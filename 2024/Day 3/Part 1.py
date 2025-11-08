import re
import pathlib

def FindSections(memory:str) -> list[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    sections = re.findall(pattern, memory)
    return sections

def Multiply(sections:list[str]):
    total = 0
    for section in sections:
        v1, v2 = map(int, section.strip('mul()').split(','))
        total += v1 * v2

    return total

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    memories = file.readlines()

    result = 0
    for memory in memories:
        sections = FindSections(memory)
        result += Multiply(sections)
    print(result)

Part1()