# Longest Job First (LJF) Scheduling Algorithm
# الگوریتم زمان‌بندی طولانی‌ترین کار اول

---

## 🇬🇧 English Section

### Overview
This project implements the **Longest Job First (LJF)** CPU scheduling algorithm in Python. The program schedules **5 tasks** based on their burst time, executing the longest task first.

### Algorithm Description
The LJF algorithm selects the task with the **largest burst time** and executes it first. The process continues until all tasks are completed.

**Algorithm Steps:**
1. Read all tasks and their burst times.
2. Sort tasks in **descending order** of burst time.
3. Execute tasks sequentially from the sorted list.
4. For each task, compute:
   - **Waiting Time** = time spent waiting before execution
   - **Turnaround Time** = Waiting Time + Burst Time
5. Calculate the average waiting time and average turnaround time.
6. Display a **Gantt chart** showing the execution order.

### What the Code Does
- Defines a `Task` class to represent each task with an ID, name, burst time, waiting time, and turnaround time.
- Implements the `longest_job_first()` function that performs the scheduling logic.
- Uses the `main()` function as the entry point, where 5 predefined tasks are created and passed to the scheduler.
- Prints structured output including:
  - The input task list
  - Tasks sorted by burst time (descending)
  - Execution order with waiting and turnaround times
  - Total and average waiting/turnaround times
  - A text-based Gantt chart

### Inputs
The program uses 5 predefined tasks:

| Task ID | Name | Burst Time |
|---------|------|------------|
| 1       | T1   | 6          |
| 2       | T2   | 3          |
| 3       | T3   | 8          |
| 4       | T4   | 2          |
| 5       | T5   | 4          |

Tasks can be modified inside the `main()` function.

### Outputs
- Input task list
- Tasks sorted by burst time (descending)
- Execution order with waiting and turnaround times
- Total and average waiting/turnaround times
- Text-based Gantt chart (see `output.png` for a sample)

### Project Structure
.
├── ljf_scheduler.py # Main Python source file
├── output.png # Sample program output
└── README.md # Project documentation

text

### Requirements
- Python 3.6 or higher
- No external libraries required

### Concepts Covered
- CPU Scheduling Algorithms
- Longest Job First (LJF)
- Waiting Time & Turnaround Time
- Gantt Chart Visualization
- Real-Time Systems Fundamentals

---

## 🇮🇷 بخش فارسی

### معرفی
این پروژه الگوریتم زمان‌بندی **طولانی‌ترین کار اول (LJF)** را در زبان پایتون پیاده‌سازی می‌کند. برنامه **۵ تسک** را بر اساس زمان اجرایشان زمان‌بندی می‌کند و ابتدا تسکی که بیشترین زمان اجرا دارد، اجرا می‌شود.

### توضیح الگوریتم
الگوریتم LJF تسکی را انتخاب می‌کند که **بیشترین زمان اجرا (Burst Time)** را دارد و آن را ابتدا اجرا می‌کند. این فرآیند تا اتمام همه تسک‌ها ادامه می‌یابد.

**مراحل الگوریتم:**
۱. خواندن تمام تسک‌ها همراه با زمان اجرایشان.
۲. مرتب‌سازی تسک‌ها به صورت **نزولی** بر اساس زمان اجرا.
۳. اجرای تسک‌ها به ترتیب لیست مرتب‌شده.
۴. محاسبه برای هر تسک:
   - **زمان انتظار (Waiting Time)** = زمان انتظار قبل از اجرا
   - **زمان بازگشت (Turnaround Time)** = زمان انتظار + زمان اجرا
۵. محاسبه میانگین زمان انتظار و میانگین زمان بازگشت.
۶. نمایش **نمودار گانت** برای نشان دادن ترتیب اجرا.

### کد چه کاری انجام می‌دهد
- کلاس `Task` را برای نمایش هر تسک با شناسه، نام، زمان اجرا، زمان انتظار و زمان بازگشت تعریف می‌کند.
- تابع `longest_job_first()` منطق زمان‌بندی را پیاده‌سازی می‌کند.
- تابع `main()` به عنوان نقطه ورود برنامه، ۵ تسک از پیش تعریف‌شده را ایجاد و به زمان‌بند ارسال می‌کند.
- خروجی ساختاریافته شامل موارد زیر چاپ می‌شود:
  - لیست تسک‌های ورودی
  - تسک‌های مرتب‌شده بر اساس زمان اجرا (نزولی)
  - ترتیب اجرا همراه با زمان انتظار و زمان بازگشت
  - مجموع و میانگین زمان‌های انتظار و بازگشت
  - نمودار گانت متنی

### ورودی‌ها
برنامه از ۵ تسک از پیش تعریف‌شده استفاده می‌کند:

| شناسه تسک | نام  | زمان اجرا |
|-----------|------|-----------|
| ۱         | T1   | ۶         |
| ۲         | T2   | ۳         |
| ۳         | T3   | ۸         |
| ۴         | T4   | ۲         |
| ۵         | T5   | ۴         |

برای تغییر تسک‌ها، می‌توانید لیست داخل تابع `main()` را ویرایش کنید.

### خروجی‌ها
- لیست تسک‌های ورودی
- تسک‌های مرتب‌شده بر اساس زمان اجرا (نزولی)
- ترتیب اجرا همراه با زمان انتظار و زمان بازگشت
- مجموع و میانگین زمان‌های انتظار و بازگشت
- نمودار گانت متنی (برای نمونه به فایل `output.png` مراجعه کنید)

### ساختار پروژه
.
├── ljf_scheduler.py # فایل اصلی پایتون
├── output.png # نمونه خروجی برنامه
└── README.md # مستندات پروژه

text

### پیش‌نیازها
- پایتون نسخه ۳.۶ یا بالاتر
- نیازی به کتابخانه جانبی نیست

### مفاهیم پوشش‌داده‌شده
- الگوریتم‌های زمان‌بندی CPU
- طولانی‌ترین کار اول (LJF)
- زمان انتظار و زمان بازگشت
- نمایش نمودار گانت
- مبانی سیستم‌های بلادرنگ

---

## 📄 License
This project is released for educational purposes.