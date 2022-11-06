# Problem details: 
# (Please check page no. 60) https://alexanderskulikov.github.io/files/toolbox_statements.pdf


def optimal_summands(n):
    summands = []
    num = 1
    total = 0
    while total < n:
        total += num
        if total > n:
            summands[-1] += (n - (total - num))
        else: summands.append(num)
        num += 1
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
