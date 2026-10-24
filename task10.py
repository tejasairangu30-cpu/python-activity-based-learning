
# Examination Result and Grace-Mark Validation

PASS_MARK = 40
MAX_MARKS = 100
MAX_GRACE = 5

subjects = ["Mathematics", "Physics", "Programming", "English", "Chemistry"]
marks = []

# Input and validate marks
for subject in subjects:
    while True:
        try:
            mark = int(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= mark <= MAX_MARKS:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

# Apply grace-mark policy
final_marks = marks.copy()
grace_used = 0

for i in range(len(subjects)):
    if final_marks[i] < PASS_MARK:
        required = PASS_MARK - final_marks[i]

        # Give grace marks only if the remaining
        # grace allowance can make the subject pass.
        if required <= MAX_GRACE - grace_used:
            final_marks[i] = min(
                final_marks[i] + required, MAX_MARKS
            )
            grace_used += required

# Calculate results
total = sum(final_marks)
maximum_total = len(subjects) * MAX_MARKS
percentage = (total / maximum_total) * 100

passed_all = all(mark >= PASS_MARK for mark in final_marks)

if not passed_all:
    classification = "Fail"
elif percentage >= 75:
    classification = "Distinction"
elif percentage >= 60:
    classification = "First Class"
elif percentage >= 50:
    classification = "Second Class"
else:
    classification = "Pass Class"

# Display result
print("\n========== EXAMINATION RESULT ==========")
print(f"{'Subject':<15}{'Original':>10}{'Final':>10}")
print("-" * 35)

for i in range(len(subjects)):
    print(f"{subjects[i]:<15}{marks[i]:>10}{final_marks[i]:>10}")

print("-" * 35)
print(f"Total Marks     : {total}/{maximum_total}")
print(f"Percentage      : {percentage:.2f}%")
print(f"Grace Marks Used: {grace_used}/{MAX_GRACE}")
print(f"Final Result    : {classification}")
print("========================================")
