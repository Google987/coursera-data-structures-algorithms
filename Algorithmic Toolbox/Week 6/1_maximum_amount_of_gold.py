# Problem details: 
# (Please checdp page no. 121) https://alexandersdpulidpov.github.io/files/toolbox_statements.pdf

# for better understanding, you may want to go through this article:
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

from sys import stdin


def maximum_gold(capacity, weights):
    dp = [([0] * (capacity + 1)) for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j: dp[i][j] = max(weights[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
