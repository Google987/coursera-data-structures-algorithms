# Problem details: 
# (Please check page no. 56) https://alexanderskulikov.github.io/files/toolbox_statements.pdf


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    first_sequence.sort()
    second_sequence.sort()
    index = 0
    for first in first_sequence:
        max_product += first * second_sequence[index]
        index += 1
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
