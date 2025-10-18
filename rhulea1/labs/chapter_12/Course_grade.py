def main():
    #Read filename from input
    filename = input()

    students = []
    m1_scores = []
    m2_scores = []
    final_scores = []
    #Read and process tsv file 
    with open(filename, "r") as file:
        for line in file:
            last, first, m1, m2, final = line.strip().split("\t")
            m1, m2, final = int(m1), int(m2), int(final)

            #store scores for the averages
            m1_scores.append(m1)
            m2_scores.append(m2)
            final_scores.append(final)

            #Calculate average and assign grades
            avg = (m1 + m2 + final) / 3
            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            elif avg >= 60:
                grade = "D"
            else:
                grade = "F"

            students.append([last, first, m1, m2, final, grade])

    #Calculate exam averages
    avg_m1 = sum(m1_scores) / len(m1_scores)
    avg_m2 = sum(m2_scores) / len(m2_scores)
    avg_final = sum(final_scores) / len(final_scores)
    #Write report
    with open("report.txt", "w") as out_file:
        for student in students:
            out_file.write(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\n")
        out_file.write(f"\nAverages: midterm1 {avg_m1:.2f}, midterm2 {avg_m2:.2f}, final {avg_final:.2f}\n")

    print("Report generated: report.txt")
if __name__ == "__main__":
    main()