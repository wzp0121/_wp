def grade(score):
    if 100 < score:
        return 's'
    elif 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <= 59:
        return 'F'
    elif score <0:
        return 'Failer'
        
print(grade(95)) 
print(grade(72))
print(grade(40)) 
print(grade(105))
print(grade(-5))
