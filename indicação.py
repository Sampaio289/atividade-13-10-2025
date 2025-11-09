import csv

with open('filmes_avaliacao.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    filmes = list(reader)

for filme in filmes:
    filme['Nota'] = float(filme['Nota'])

filmes_ordenados = sorted(filmes, key=lambda x: (-x['Nota'], x['Filme']))

top5 = filmes_ordenados[:5]

with open('filmes_indicacao.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Ano', 'Filme', 'Nota'])
    writer.writeheader()
    writer.writerows(top5)

print(" Arquivo 'filmes_indicacao.csv' criado com sucesso!")