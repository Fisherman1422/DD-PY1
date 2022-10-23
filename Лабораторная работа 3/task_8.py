money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0 # количество месяцев, которое можно прожить

summ = spend
while money_capital >= 0:
   spend = spend * 1.05
   summ = summ + spend

month = (money_capital) + summ / salary * (-1)

print(month)