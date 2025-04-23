
dict1 = {
    'dept1': {'roll_no': 75, 'salary': 70000},
    'dept2': {'roll_no': 27, 'salary': 65000},
    'dept3': {'roll_no': 51, 'salary': 50000},
}


def find(dept_dict):
    min = float('inf')
    max = float('-inf')
    for dept, info in dept_dict.items():
        salary = info['salary']
        if salary < min:
            min = salary
        if salary > max:
            max = salary
    return min, max

min, max = find(dict1)
print(f"Minimum Salary: {min}")
print(f"Maximum Salary: {max}")
