s = {"Aa", "Ab", "Ar", "Adi","Bivya", "Ba", "Bet", "Baanf"}
A = set()
B = set()

for i in s:
    if i.startswith("A"):
        A.add(i)
    elif i.startswith("B"):
        B.add(i)

print(f"s = {s}")
print(f"A = {A}")
print(f"B = {B}")

