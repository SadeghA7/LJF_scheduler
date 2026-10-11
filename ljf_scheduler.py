"""
Longest Job First (LJF) Scheduling Algorithm
Embedded and Real-Time Systems Course Project

This program schedules 5 tasks using the LJF (Longest Job First) algorithm.
In LJF, the task with the longest burst time is executed first.
"""

import time


class Task:
    """Represents a single task in the scheduling system."""

    def __init__(self, task_id, name, burst_time):
        self.task_id = task_id        # Unique identifier
        self.name = name              # Task name
        self.burst_time = burst_time  # CPU burst time (in time units)
        self.waiting_time = 0         # Time spent waiting before execution
        self.turnaround_time = 0      # Total time from arrival to completion


def longest_job_first(tasks):
    """
    Implements the Longest Job First scheduling algorithm.

    Steps:
    1. Sort all tasks in descending order of burst time.
    2. Execute tasks one by one in that order.
    3. Compute waiting time and turnaround time for each task.
    """
    print("=" * 60)
    print("     LONGEST JOB FIRST (LJF) SCHEDULING ALGORITHM")
    print("=" * 60)

    # Step 1: Sort tasks by burst time in descending order
    sorted_tasks = sorted(tasks, key=lambda t: t.burst_time, reverse=True)

    print("\n[TASKS SORTED BY BURST TIME - DESCENDING ORDER]")
    print("-" * 60)
    print(f"{'Task ID':<10}{'Name':<15}{'Burst Time':<15}")
    print("-" * 60)
    for task in sorted_tasks:
        print(f"{task.task_id:<10}{task.name:<15}{task.burst_time:<15}")

    # Step 2: Calculate waiting time and turnaround time
    current_time = 0
    total_waiting = 0
    total_turnaround = 0

    print("\n[EXECUTION ORDER AND TIMING]")
    print("-" * 60)
    print(f"{'Task ID':<10}{'Name':<15}{'Burst':<10}{'Wait':<10}{'Turnaround':<12}")
    print("-" * 60)

    for task in sorted_tasks:
        task.waiting_time = current_time
        current_time += task.burst_time
        task.turnaround_time = task.waiting_time + task.burst_time

        total_waiting += task.waiting_time
        total_turnaround += task.turnaround_time

        print(f"{task.task_id:<10}{task.name:<15}{task.burst_time:<10}"
              f"{task.waiting_time:<10}{task.turnaround_time:<12}")

    # Step 3: Compute averages
    n = len(sorted_tasks)
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n

    print("-" * 60)
    print(f"\n[STATISTICS]")
    print("-" * 60)
    print(f"Total Waiting Time      : {total_waiting}")
    print(f"Total Turnaround Time   : {total_turnaround}")
    print(f"Average Waiting Time    : {avg_waiting:.2f}")
    print(f"Average Turnaround Time : {avg_turnaround:.2f}")

    # Step 4: Show Gantt chart (text-based)
    print("\n[GANTT CHART]")
    print("-" * 60)
    gantt_line = "|"
    time_line = "0"
    current = 0
    for task in sorted_tasks:
        gantt_line += f"  {task.name}  |"
        current += task.burst_time
        time_line += f"{current:>7}"

    print(gantt_line)
    print(time_line)
    print("-" * 60)

    return sorted_tasks, avg_waiting, avg_turnaround


def main():
    """Entry point: defines 5 tasks and runs the LJF scheduler."""

    # Define 5 tasks with different burst times
    tasks = [
        Task(1, "T1", 6),
        Task(2, "T2", 3),
        Task(3, "T3", 8),
        Task(4, "T4", 2),
        Task(5, "T5", 4),
    ]

    print("\n[INPUT TASKS]")
    print("-" * 60)
    print(f"{'Task ID':<10}{'Name':<15}{'Burst Time':<15}")
    print("-" * 60)
    for task in tasks:
        print(f"{task.task_id:<10}{task.name:<15}{task.burst_time:<15}")

    # Run the scheduler
    longest_job_first(tasks)


if __name__ == "__main__":
    main()