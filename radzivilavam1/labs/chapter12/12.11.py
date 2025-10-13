
import csv

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

midterm_1_marks = []
midterm_2_marks = []
final_marks = []
rows_to_write = []

file_to_open = input()

with open(file_to_open, "r") as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t')

    for row in tsv_reader:
        scores = [int(score) for score in row[2:]]
        midterm1, midterm2, final = scores
        midterm_1_marks.append(midterm1)
        midterm_2_marks.append(midterm2)
        final_marks.append(final)
        scores_avg = int(sum(scores) / len(scores))
        grade = assign_grade(scores_avg)
        row.append(grade)
        rows_to_write.append(row)

avg_midterm_1 = sum(midterm_1_marks) / len(midterm_1_marks)
avg_midterm_2 = sum(midterm_2_marks) / len(midterm_2_marks)
avg_final = sum(final_marks) / len(final_marks)

rows_to_write.append([])
rows_to_write.append([f"Averages: midterm1 {avg_midterm_1:.2f}, midterm2 {avg_midterm_2:.2f}, final {avg_final:.2f}"])

with open("report.txt", "w") as report_file:
    grades_writer = csv.writer(report_file, delimiter='\t')

    for row in rows_to_write:
        grades_writer.writerow(row)