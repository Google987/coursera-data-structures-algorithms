def majority_element_naive(elements):
    counts = {}
    n = len(elements)
    for e in elements:
        counts[e] = counts.get(e, 0) + 1
        if counts[e] > n/2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
