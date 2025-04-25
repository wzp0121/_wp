def summ(data):
    for student in data:
        name = student['name']
        scores = student['scores']
        total = sum(scores)
        avg = round(total / len(scores), 1)
        print(f"{name}: 總分 = {total}, 平均 = {avg}")

students = [
    {'name': 'Alice', 'scores': [90, 80, 70]},
    {'name': 'Bob', 'scores': [100, 85, 95]}
]
summ(students)