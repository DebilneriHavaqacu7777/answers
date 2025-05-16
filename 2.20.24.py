#20
fuel_per_100km = float(input())
distance = float(input())

total_fuel = (fuel_per_100km / 100) * distance
print("Անհրաժեշտ վառելիք:", round(total_fuel, 2), "լիտր")


#21
str1 = input("Մուտքագրեք առաջին տողը: ").replace(" ", "").lower()
str2 = input("Մուտքագրեք երկրորդ տողը: ").replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Անագրամներ են")
else:
    print("Անագրամներ չեն")


#22
roman_leagues = float(input("Մուտքագրեք հռոմեական լիգաների քանակը: "))
km = roman_leagues * 2.2
french_leagues = km / 4.6

print("Ֆրանսիական լիգա:", int(french_leagues))


#23
coins = int(input("Մուտքագրեք 200 դրամանոց մետաղադրամների քանակը: "))
total_weight = coins * 4.5

copper = (14 / 20) * total_weight
aluminum = (1 / 20) * total_weight
nickel = (5 / 20) * total_weight

print("Պղինձ:", round(copper, 2), "գրամ")
print("Ալյումին:", round(aluminum, 2), "գրամ")
print("Նիկել:", round(nickel, 2), "գրամ")

#24
def dna_encode(sequence):
    result = ""
    for char in sequence.upper():
        if char == 'A':
            result += 'T'
        elif char == 'T':
            result += 'A'
        elif char == 'C':
            result += 'G'
        elif char == 'G':
            result += 'C'
        else:
            result += char  # եթե այլ տառ է, թողնում ենք նույնը
    return result

text = input("Մուտքագրեք տողը՝ ԴՆԹ գաղտնագրման համար: ")
encoded = dna_encode(text)
print("Գաղտնագրված տեքստ:", encoded)
