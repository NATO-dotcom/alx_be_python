# Prompt for a single task
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to construct the base reminder text that includes priority
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority level"

# Append time-sensitivity information and print a single clear reminder line
if time_bound == "yes":
    print(f"Reminder: {base} that requires immediate attention today!")
else:
    print(f"Reminder: {base}. Consider completing it when you have free time.")


