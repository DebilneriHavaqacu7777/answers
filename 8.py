#1
m = {1, 2, 3, 4, 5, 6, 7}
print(m)

#2
s = {2, 9, 6, 3}
print(len(s))

#3
s = {10, 11, 6, 9, 25, 36}
for _ in range(3):
    s.pop()
print(s)

#4
n1 = int(input())
n2 = int(input())
n3 = int(input())
s = set()
s.add(n1)
s.add(n2)
s.add(n3)
print(s)

#5
n1 = int(input())
n2 = int(input())
n3 = int(input())
s = {2, 6, 3}
s.add(n1)
s.add(n2)
s.add(n3)
s1 = list(s)
arx = 0
for i in s1:
    arx+=i 
print(arx)

#6
n = int(input())
s = {1, 2, 3, 14}
s1 = list(s)
for i in s1:
    if n == i:
        print("The integer is in set")
    else:
        print("There is no integer")

#7
s = {1, 2, 3, 4, 5}
n = int(input())
if n in s:
    s.remove(n)
print(s)

#8
s = {1, 0, 2, 8, 25}
for i in s:
    if i == 0:
        s.clear()
        break
print(s)

#9
s = {6, 15, 3, 8}  
while s:
    i = s.pop()  
    if i % 5 == 0:
        print("Բաժանվում է 5-ի:")
        break
    else:
        print("Չի բաժանվում 5-ի:")

#10
s1 = {6, "a", 3, 8}  
s2 = {"l", "h", 1}
print(s1 | s2)

#11
s1 = {6, "a", 3, 8}  
s2 = {"l", "h", 1, 3}
print(s1 & s2)

#12
s = {4, 3, 8}  
n = int(input())
new_s = {i * n for i in s}
print(new_s)

#13
s1 = {4, 3, 8, "d"}  
s2 = {3, 5,"d", 9}
s3 = {2, "d", 3, 25}
print(s1 & s2 & s3)

#14
s1 = {5, 3, 8, "a"}  
s2 = {12, 5,"a"}
print(s1 - s2)

#15
s = {21, 12, 33, 42}  
m = sorted(list(s))
i = m[-1]
if i % 2 == 0:
    print("Զույգ է")
else:
    print("Կենտ է")

#16
s = {21, 5, 9, 42}  
m = sorted(list(s))
i = m[0]
if i % 2 != 0:
    print("Կենտ է")
else:
    print("Զույգ է")

#17
s = {5, 21, 9, 14}  
m = list(s)
mijin = sum(m) / len(m)
print(mijin)

#18
l = [2, 6, 2, 9, 11, 10, 9]
print(set(l))

#19
student1_sports = {"football", "tennis", "basketball"}
student2_sports = {"tennis", "cricket", "basketball"}
student3_sports = {"basketball", "football", "swimming"}
print(student1_sports & student2_sports & student3_sports)

#20
William = {"Monopoly", "Chess", "Uno", "Scrabble", "Catan"}
Isabella = {"Chess", "Catan", "Uno", "Pandemic"}
James = {"Uno", "Ticket to Ride", "Chess", "Monopoly"}
if "Catan" not in William:
    print("William")
if "Catan" not in Isabella:
    print("Isabella")
if "Catan" not in James:
    print("James")

#21
first_year = {2577, 3908, 3597, 3521, 3593, 2821, 3100}
second_year = {3100, 4090, 3888, 3201, 5137, 3925, 5033, 3521, 3597}

repeated = first_year & second_year
total = sum(first_year | second_year)

print(f"2 անգամ բարձրացած լեռների բարձրությունները: {repeated}")
print(f"Բոլոր լեռների ընդհանուր բարձրությունը: {total}")

#22
orders = [
    {"coffee", "sandwich"},
    {"tea", "cake", "coffee"},
    {"coffee", "cookie"},
    {"tea", "sandwich", "cookie", "coffee"}
]

total = set.intersection(*orders)
print(f"Բոլոր հաճախորդների կողմից պատվիրած մթերքը: {total}")

#23
developers_languages = [
    {"Python", "Java", "C++"},
    {"JavaScript", "Python", "C++", "PHP"}
]

u = developers_languages[0] ^ developers_languages[1]
print(f"Ծրագրավորման լեզուներ, որոնք միայն մեկ ծրագրավորող գիտի: {u}")

#24
visited_2023 = {"Armenia", "Georgia", "France", "Italy"}
visited_2024 = {"France", "Germany", "Italy", "Spain"}

only_2023 = visited_2023 - visited_2024
print(f"Երկրները, որոնք ճանապարհորդը այցելել է միայն 2023թ-ին: {only_2023}")
