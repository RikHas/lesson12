def text(*args):
     print(*args)
text(47, 'HI', True)
def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n - 1) * n
print(fac(6))
