# Problem details: 
# (Please check page no. 112) https://alexanderskulikov.github.io/files/toolbox_statements.pdf


def change(money):
    coins = [1, 3, 4]
    dp = [0] * (money + 1)
    for m in range(1, money + 1):
        temp_counts = []
        for coin in coins:
            if m - coin >= 0: temp_counts.append(1 + dp[m - coin])
        dp[m] = min(temp_counts)
    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
