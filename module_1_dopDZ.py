grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_srednee = (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]))
students_spisok = sorted(tuple(students))
sr_grades_student = {students_spisok[0]:grades_srednee[0], students_spisok[1]:grades_srednee[1], students_spisok[2]:grades_srednee[2], students_spisok[3]:grades_srednee[3], students_spisok[4]:grades_srednee[4]}
print(sr_grades_student)