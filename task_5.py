# Задача 5 Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

revenue = int(input('Enter the company revenue'))
costs = int(input('Enter the company costs'))

if revenue > costs:
    print('Profit')
else:
    print('Loss')

