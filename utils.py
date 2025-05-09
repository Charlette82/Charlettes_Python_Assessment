def calculate_average(scores):
    # This code Calculates the average of scores and rounds to 2 decimal places.
    return round(sum(scores) / len(scores), 2)

def assign_grade(avg):
    # This code Assigns a grade based on the average score using normal if-else statements.
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'