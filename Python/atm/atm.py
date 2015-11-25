widthdrawl, balance = input().split()
widthdrawl = int(widthdrawl)
balance = int(balance)

if balance > 0:
    if widthdrawl + 0.5 > balance:
        print('%.2f' %balance)
    elif widthdrawl % 5 == 0:
        balance = balance - widthdrawl - 0.50
        print('%.2f' %balance)
    else:
        print('%.2f' %balance)