

def fib(n):
    if n == 0: return 0
    elif n > 30: return print("Число больше 30")
    fib_n_0 = 0
    fib_n_1 = 1
    i = 0
    while i <= n:
        temp_num = fib_n_1
        fib_n_1 += fib_n_0
        fib_n_0 = temp_num
        i +=1

    return fib_n_1

#print(fib(2))
