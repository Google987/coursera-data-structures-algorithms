# Problem details: 
# (Please check page no. 113) https://alexanderskulikov.github.io/files/toolbox_statements.pdf


def compute_operations(n):
    dp = [0] * (n + 1)
    for num in range(2, n + 1):
        temp_counts = []
        if num - 1 >= 0: temp_counts.append(1 + dp[num - 1])
        if num % 2 == 0 and num // 2 >= 0: temp_counts.append(1 + dp[num // 2])
        if num % 3 == 0 and num // 3 >= 0: temp_counts.append(1 + dp[num // 3])
        dp[num] = min(temp_counts)
    solution = []
    while n > 1:
        solution.append(n)
        if dp[n-1] == dp[n] - 1: n = n-1
        elif n % 2 == 0 and dp[n // 2] == dp[n] -1: n = n // 2
        elif n % 3 == 0 and dp[n // 3] == dp[n] -1: n = n // 3
    solution.append(1)
    solution.reverse()
    return solution


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
