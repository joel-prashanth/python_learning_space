def grade(score):
    if score >= 80:
        return "A"
    elif score >= 50:
        return "pass"
    else:
        return "fail"


total = 0
count = 0
lines = []
try:
    with open("marks.txt", "r", encoding="utf-8") as f:
        passed = 0
        for line in f:
            parts = line.strip().split(",")
            name = parts[0]
            marks = int(parts[1])
            count += 1
            total += marks
            grade_returned = grade(marks)
            if grade_returned != "fail":
                passed += 1
            text = f"{name}: {grade_returned}"
            print(text)
            lines.append(text)
    average = total / count
    average_text = f"Class average: {average}"
    passed_text = f"Passed: {passed}"
    lines.append(average_text)
    lines.append(passed_text)
    print(average_text)
    print(passed_text)
    try:
        with open("report.txt", "w", encoding="utf-8") as out:
            for item in lines:
                out.writelines(item + "\n")
    except FileNotFoundError:
        print("File not found")

except FileNotFoundError:
    print("File Not Found")
