def stock_cal(stock):
    buy = False
    sell_day = []
    buy_day = []
    for i in range(len(stock) - 1):

        if stock[i] > stock[i + 1]:
            if buy:
                buy = False
                sell_day.append(i)

        elif stock[i] < stock[i + 1]:
            if not buy:
                buy = True
                buy_day.append(i)

    return buy_day, sell_day


s = [10, 8, 5, 4, 6, 8, 11, 9, 10, 8, 7, 6, 5, 6, 7, 6, 5]
buy, sell = stock_cal(s)
print(buy)
print(sell)
