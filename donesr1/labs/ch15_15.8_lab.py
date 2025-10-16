import numpy as np

# Read exam scores from user input
exam1_input = input()
exam2_input = input()

# Convert the inputs to NumPy arrays
exam1 = np.array(list(map(float, exam1_input.strip().split())))
exam2 = np.array(list(map(float, exam2_input.strip().split())))

# Calculate the average scores
average_scores = (exam1 + exam2) / 2

# Count how many average scores are 80 or above
count_80_or_above = np.sum(average_scores >= 80)

# Print results
print(f"Average scores: {average_scores}")
print(f"Number of students who received 80 and above: {count_80_or_above}")
