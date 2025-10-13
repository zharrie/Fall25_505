def assign_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Read file name from user
    filename = input("Enter the name of the TSV file: ")

    try:
        with open(filename, 'r') as infile:
            lines = infile.readlines()

        students = []
        total_m1 = 0
        total_m2 = 0
        total_final = 0
        count = 0

        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) != 5:
                continue  # Skip invalid lines

            last, first, m1, m2, final = parts
            m1 = int(m1)
            m2 = int(m2)
            final = int(final)
            avg = (m1 + m2 + final) / 3
            grade = assign_letter_grade(avg)

            students.append((last, first, m1, m2, final, grade))

            total_m1 += m1
            total_m2 += m2
            total_final += final
            count += 1

        # Compute averages
        avg_m1 = total_m1 / count
        avg_m2 = total_m2 / count
        avg_final = total_final / count

        # Write to report.txt
        with open("report.txt", "w") as outfile:
            for student in students:
                # Tab-separated values
                outfile.write(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\n")
            # Final averages line
            outfile.write(f"\nAverages: midterm1 {avg_m1:.2f}, midterm2 {avg_m2:.2f}, final {avg_final:.2f}\n")

        print("Report written to 'report.txt'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    main()
