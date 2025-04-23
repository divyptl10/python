def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
marks = [90, 70, 90, 67, 53]
total, average = sum_avg(marks) 
print(f"Total: {total}, Average: {average}")