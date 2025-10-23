import numpy as np

#Read two sets of exam scores of five students from user input
exam1 = np.array(list(map(float, input().split())))
exam2 = np.array(list(map(float, input().split())))

#Compute the average scores for each of the five students
average_scores = (exam1 + exam2) / 2

#Output "Average scores: " followed by the NumPy array of the average scores
print(f"Average scores: {average_scores}")

#Count the number of average scores that are >= 80
count = np.sum(average_scores >= 80)

#Output "Number of students who received 80 and above: " followed by the count
print(f"Number of students who received 80 and above: {count}")
