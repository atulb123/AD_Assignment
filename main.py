from random import randint
import argparse


def convertDecimalToBin(num):
    """converts decimal to binary"""
    bin_num = ""
    while num > 0:
        rem = num % 2
        bin_num += str(rem)
        num = num // 2
    return bin_num[::-1]


def generateOutput(n):
    """generates binary Output with the numbers specified"""
    with open("intermediate_output.txt", "w") as f:
        random_numbers = [f'{str(randint(0, 999999))}\n' for i in range(n)]
        f.writelines(random_numbers)
    with open("intermediate_output.txt", "r") as fr:
        with open("final_output.txt", "w") as fw:
            random_numbers = fr.readlines()
            fw.writelines([f'{convertDecimalToBin(int(num))}\n' for num in random_numbers])


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--num", default=1)
    parse_obj = arg_parser.parse_args()
    num = int(parse_obj.num)
    generateOutput(num)
