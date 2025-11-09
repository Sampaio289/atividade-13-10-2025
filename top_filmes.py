import csv

with open('filmes_indicacao.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    filmes = list(reader)

filmes_ordenados = sorted(filmes, key=lambda x: float(x['Nota']), reverse=True)

print("\n🎥 TOP FILMES INDICADOS 🎥\n")
for f in filmes_ordenados:
    print(f"{f['Filme']} ({f['Ano']}) - Nota: {f['Nota']}")