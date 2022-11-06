# Problem details: 
# (Please check page no. 54) https://alexanderskulikov.github.io/files/toolbox_statements.pdf

# If you face any issue with inputs when executing this program, please check the below link
# https://stackoverflow.com/questions/36798798/using-sys-stdin-readline-to-read-multiple-lines-from-cmd-in-python

from sys import stdin


def min_refills(distance, tank, stops):
    last_stop_index = 0
    distance_covered = 0
    no_of_refills = 0
    while distance_covered + tank < distance:
        prev_stop = last_stop_index
        while last_stop_index < len(stops) and stops[last_stop_index] <= distance_covered + tank:
            last_stop_index += 1
        if prev_stop == last_stop_index: return -1
        distance_covered = stops[last_stop_index - 1]
        no_of_refills += 1

    return no_of_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
