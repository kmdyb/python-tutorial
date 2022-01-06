from bank import MinimalBalanceAccount


minkonto = MinimalBalanceAccount(1500, 1000)
result = minkonto.try_withdraw(600)

if result.is_ok():
    print(result.message)
else:
    print(result.message)
