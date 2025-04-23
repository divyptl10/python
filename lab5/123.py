
employees = [
    {'dept_no': 1, 'emp_roll_no': 101, 'salary': 50000},
    {'dept_no': 1, 'emp_roll_no': 102, 'salary': 60000},
    {'dept_no': 2, 'emp_roll_no': 201, 'salary': 55000},
    {'dept_no': 2, 'emp_roll_no': 202, 'salary': 45000},
    {'dept_no': 3, 'emp_roll_no': 301, 'salary': 70000},
    {'dept_no': 3, 'emp_roll_no': 302, 'salary': 80000},
]
dept_salaries = defaultdict(list)
for i in employees:
    dept_salaries[i['dept_no']].append(i['salary'])

dept_min_max_salaries = {
    dept: {'min_salary': min(salaries), 'max_salary': max(salaries)}
    for dept, salaries in dept_salaries.items()
}
print(dept_min_max_salaries)