# TODO: Import NumPy
import numpy as np

# TODO: Read two sets of exam scores of five students from user input
#       and store the scores into two NumPy arrays
exam1_input = input()
exam2_input = input()

exam1 = np.array(list(map(int, exam1_input.split())))
exam2 = np.array(list(map(int, exam1_input.split())))

# TODO: Compute the average scores for each of the five students
average_scores = (exam1 + exam2) / 2

count_80_or_above = np.sum(average_scores >= 80)

# Output results
print("Average scores:", average_scores)
print("Number of students who received 80 and above:", count_80_or_above)