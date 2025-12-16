
data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

rows = len(data)

averages = []

for i in range(len(data[0])):
    column_sum = 0
    for row in data:
        column_sum += row[i]
    averages.append(column_sum / rows)

data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

rows = len(data)
averages = []

for i in range(len(data[0])):
    column_sum = 0
    for row in data:
        column_sum += row[i]
    averages.append(column_sum / rows)

for i, avg in enumerate(averages, start=1):
    print(f"The average of column {i} is {avg}")

