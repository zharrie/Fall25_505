
file_name = input() 

students = []
score_midterm1 = 0
score_midterm2 = 0
final_grade = 0
total_students = 0

def letter_grade(avg):
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
      
# Read a file name from the user and read the tsv file
with open(file_name, 'r') as f:
    for line in f:
        x = line.strip().split('\t')
        last_name = x[0]
        first_name = x[1]
        midterm1 = int(x[2])
        midterm2 = int(x[3])
        final = int(x[4])

        avg = (midterm1 + midterm2 + final) / 3
        grade = letter_grade(avg)

        students.append((last_name, first_name, midterm1, midterm2, final, grade))

        score_midterm1 += midterm1
        score_midterm2 += midterm2
        final_grade += final
        total_students += 1


# Compute student grades and exam averages
with open("report.txt", "w") as report:
    for student in students:
        report.write(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\n")

    avg1 = score_midterm1 / total_students
    avg2 = score_midterm2 / total_students
    avg3 = final_grade / total_students

    report.write(f"\nAverages: midterm1 {avg1:.2f}, midterm2 {avg2:.2f}, final {avg3:.2f}\n")
