with open('emd.csv', 'r') as file:
    lines = file.readlines()

header = lines.pop(0)

total_people = 0
fit_people = 0
not_fit_people = 0
athlete_categories = {}
modalities = []

for line in lines:
    data = line.strip().split(',')

    age = int(data[5])
    total_people += 1
    resultado = data[12]


    if resultado == 'true':
        fit_people += 1
    elif resultado == 'false':
        not_fit_people += 1

    age_category = f"[{((age-1)//5)*5}-{((age-1)//5)*5 + 4}]"
    if age_category not in athlete_categories:
        athlete_categories[age_category] = []
    athlete_categories[age_category].append((data[3], data[4]))

    if data[8] not in modalities:
        modalities.append(data[8])


percentage_fit = (fit_people / total_people) * 100
percentage_not_fit = (not_fit_people / total_people) * 100

modalities.sort()

print("modalidades")
print(modalities)
print("Percentagem de atletas aptos:", percentage_fit)
print("Percentagem de atletas inaptos:", percentage_not_fit)
print("\nAtletas por escalão etário:")
for first, last in athlete_categories.items():
    print(f"{first} {last}")

