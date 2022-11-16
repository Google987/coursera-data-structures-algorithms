# Problem details: 
# (Please check page no. 117) https://alexanderskulikov.github.io/files/toolbox_statements.pdf

# You may follow this article for better understanding 
# https://www.programiz.com/dsa/longest-common-subsequence


def lcs2(first_sequence, second_sequence):
    dp = [[0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if first_sequence[i - 1] == second_sequence[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
            else: dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
