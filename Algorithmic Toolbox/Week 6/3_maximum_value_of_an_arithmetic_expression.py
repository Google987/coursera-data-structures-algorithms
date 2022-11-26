# Problem details: 
# (Please checdp page no. 125) https://alexandersdpulidpov.github.io/files/toolbox_statements.pdf

# Answer is copied from: https://stackoverflow.com/questions/37101475/dynamic-programming-solution-to-maximizing-an-expression-by-placing-parentheses

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinMax(i, j, op, m, M):
    mmin = 10000
    mmax = -10000
    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], op[k])
        b = evaluate(M[i][k], m[k+1][j], op[k])
        c = evaluate(m[i][k], M[k+1][j], op[k])
        d = evaluate(m[i][k], m[k+1][j], op[k])
        mmin = min(mmin, a, b, c, d)
        mmax = max(mmax, a, b, c, d)
    return(mmin, mmax)


def maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset)+1:2]
    n = len(d)
    #iniitializing matrices/tables
    m = [[0 for i in range(n)] for j in range(n)]  #minimized values
    M = [[0 for i in range(n)] for j in range(n)]  #maximized values
    for i in range(n):
        m[i][i] = int(d[i])   #so that the tables will look like
        M[i][i] = int(d[i])   #[[i, 0, 0...], [0, i, 0...], [0, 0, i,...]]
    for s in range(1, n):   #here's where I get confused
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i,j,op,m,M)
    return M[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
    