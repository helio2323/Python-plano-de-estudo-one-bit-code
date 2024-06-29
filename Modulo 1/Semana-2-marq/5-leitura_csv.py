languagens = []
with open("languagens.csv", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        languagens.append(f"{language} - {category}") 

for language in sorted(languagens):
    print(language)