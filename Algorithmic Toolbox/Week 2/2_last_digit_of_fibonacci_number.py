def fibonacci_last_digit(n):
    if n <= 1:
        return n

    first, second = 0, 1
    nums = [first, second]
    for _ in range(n - 1):
        nums.append((nums[-1] + nums[-2]) % 10)

    return nums[-1] 


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
