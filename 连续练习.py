def day(n1, n2):
    day = []
    for i in range(n1, n2):
        day.append(i)
    print(day)
def month(x, n1, n2):
    print(x, '月份')
    print(day(n1, n2))
a = [1, 3, 5, 7, 8, 10, 12]
b = [2]
c = [4, 6, 9, 11]
def main():
    for i in range(1, 13):
        if i in a:
            month(i, 1, 32)
        if i in b:
            month(i, 1, 30)
        if i in c:
            month(i, 1, 31)
main()