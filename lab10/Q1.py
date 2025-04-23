import csv

with open("Q1.csv", "wb") as f:
    f.write(b"Name,Age,City\n")
    f.write(b"Divy,19,Gandhinagar\n")
    f.write(b"Priyanshu,13,Surat\n")
with open("Q1.csv", "rb") as f:
    for line in f:
        print(line.decode().strip())
