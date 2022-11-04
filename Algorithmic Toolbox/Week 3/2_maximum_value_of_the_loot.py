# Problem details: 
# (Please check page no. 52) https://alexanderskulikov.github.io/files/toolbox_statements.pdf


# If you face any issue with inputs when executing this program, please check the below link
# https://stackoverflow.com/questions/36798798/using-sys-stdin-readline-to-read-multiple-lines-from-cmd-in-python


from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    v_w = [[values[i], weights[i]] for i in range(len(weights))]
    v_w.sort(key=lambda x: x[0]/x[1], reverse=True)
    index = 0
    while capacity > 0 and index < len(v_w):
        item_value, item_weight  = v_w[index]
        min_weight = min(capacity, item_weight)
        capacity -= min_weight
        value += ((item_value/item_weight) * min_weight)
        index += 1
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
