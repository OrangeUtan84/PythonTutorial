# x = range(10)
# for i in x:
#     print(i)
#     if i % 2 == 0:
#         print("Ya")
#         continue
# else:
#     print("no")

#while True:
#    pass


def ask_ok(prompt, retries=4, complaint='Bitte Ja oder Nein'):
    while True:
        ok = input(prompt)
        if ok in ('j', 'J', 'ja', 'Ja'): return True
        if ok in ('n', 'N', 'nein', 'Nein'): return False
        retries -= 1
        if retries < 0:
            raise IOError('Benutzer abgelehnt!')
        print(complaint)

# def fib(n):
#     """Print the Fibonacci series up to n"""
#     a,b = 0,1
#     while a < n:
#         print(a, end=' ')
#         a,b = b, a + b
#     print()

# fib(2000)


while True:
    if ask_ok('Beenden? ', retries=3):
        quit(1)


