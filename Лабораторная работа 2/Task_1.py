money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_months = 0
while money_capital > spend - salary:
    money_capital += salary - spend
    spend = spend * (1 + increase)
    count_months += 1
print("Количество месяцев, которое можно протянуть без долгов:", count_months)
