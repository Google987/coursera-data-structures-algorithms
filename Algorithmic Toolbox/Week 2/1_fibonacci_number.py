def fibonacci_number(n):
    if n <= 1:
        return n

    first, second = 0, 1
    nums = [first, second]
    for _ in range(n - 1):
        nums.append(nums[-1] + nums[-2])

    return nums[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
