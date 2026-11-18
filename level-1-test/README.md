# Marks report

A small Python script that turns a marks file into a grade report.

## Input
`marks.txt`, one student per line as `name,score` (made-up names in the sample):

```
Asha,72
Ravi,45
Meena,90
```

## Run
```
py marks_report.py
```

## Output
Each student is graded `A` (80 or more), `pass` (50 or more) or `fail`, followed by the class average and the number who passed. The same lines are saved to `report.txt`.

If `marks.txt` is missing, the script prints `File Not Found` and leaves any existing `report.txt` untouched.

Written by hand from a blank file as the Level 1 test of the Python Wizardry path.
