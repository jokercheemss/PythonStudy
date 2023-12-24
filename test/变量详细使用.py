name = "传播智客"
stock_price = 19.99
stock_code = "003032"
number = 1.2
growth_days = 7
money = stock_price*number**growth_days
print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
message = "每日增长系数是:%.1f,经过%d天增长后,股价达到了:%.2f" % (number, growth_days, money)
print(message)