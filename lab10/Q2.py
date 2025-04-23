import csv

with open(r"C:\Users\acer\Desktop\python lab\lab10\Q2.csv", "r") as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        row['CP'] = int(row['CP'])
        row['Maths'] = int(row['Maths'])
        row['Chemistry'] = int(row['Chemistry'])
        row['total'] = row['CP'] + row['Maths'] + row['Chemistry']
        data.append(row)
    for record in data:
        print(record)
