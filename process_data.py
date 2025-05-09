# This code helps read and import functions, calculating the scores and assigning the grades
import csv
from utils import calculate_average, assign_grade

def process_grades():
    students = []
    with open('students.csv','r') as file:
         reader = csv.reader(file)
         header = next(reader)
         for row in reader:
             Name, French, Science, History = row
             average = calculate_average([int(French), int(Science), int(History)])
             grade = assign_grade(average)
             students.append([Name, average, grade])

    with open('student_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'average', 'grade'])
        writer.writerows(students)

    print('Results saved to student_results.csv')


