# 📊 Marks-to-GPA Automation Script

A simple Python automation tool that reads student marks from an Excel file, calculates total marks, average, and assigns a letter grade — then saves the results into a polished Excel report.

Perfect for school teachers, admin staff, or freelance clients who need to process marksheets efficiently.

---

## ✅ What It Does

- Reads marks from an Excel file (e.g., CSE101, MATH201)
- Calculates:
  - **Total marks**
  - **Average marks**
  - **Letter Grade**
- Saves a clean Excel report with all computed values

---

## 🚀 How to Run It

### 1. Set Up Your Project Folder

```
marks_to_gpa/
├─ marks_input.xlsx       # Raw input marks
├─ marks_processor.py     # The Python script
└─ output/                # Will contain generated Excel report
```

Create an empty `output/` folder before running the script.

---

### 2. Install Required Library

If you haven't already:

```bash
pip install pandas openpyxl
```

---

### 3. Run the Script

```bash
python marks_processor.py
```

It will generate a file like:

```
output/marks_report.xlsx
```

---

## 📥 Sample Input (marks_input.xlsx)

| Name   | ID  | CSE101 | CSE102 | MATH201 |
| ------ | --- | ------ | ------ | ------- |
| Ali    | 101 | 85     | 90     | 88      |
| Nishi  | 102 | 92     | 87     | 95      |
| Arafat | 103 | 78     | 80     | 75      |
| Nadia  | 104 | 67     | 70     | 65      |

---

## 📤 Sample Output (marks_report.xlsx)

| Name   | ID  | CSE101 | CSE102 | MATH201 | Total | Average | Grade |
| ------ | --- | ------ | ------ | ------- | ----- | ------- | ----- |
| Ali    | 101 | 85     | 90     | 88      | 263   | 87.67   | A+    |
| Nishi  | 102 | 92     | 87     | 95      | 274   | 91.33   | A+    |
| Arafat | 103 | 78     | 80     | 75      | 233   | 77.67   | A     |
| Nadia  | 104 | 67     | 70     | 65      | 202   | 67.33   | B     |

---

## 🎓 Grading Criteria (Customizable)

You can tweak this part inside `marks_processor.py`:

```python
def get_grade(avg):
    if avg >= 80: return "A+"
    elif avg >= 70: return "A"
    elif avg >= 60: return "B"
    else: return "F"
```

---

## 💡 Why Use This?

✅ Saves time for teachers  
✅ Works for **any number of subjects**  
✅ Reusable for schools, universities, or freelance clients  
✅ Fully customizable

---

## 👨‍💻 Author

**Oli Ahmed Khan**  
Email: oli.khan.contact@gmail.com@gmail.com  
GitHub: [oliahmedkhan](https://github.com/oliahmedkhan)

---
