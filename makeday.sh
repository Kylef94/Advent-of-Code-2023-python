#!/bin/bash

template='
def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            data.append(l.strip())
    return data

if __name__ == "__main__":
    data = get_input()
    print(data)
    '

mkdir day$1
echo >> day$1/input.txt
printf "$template" >> day$1/part1.py
printf "$template" >> day$1/part2.py
echo "done!"

