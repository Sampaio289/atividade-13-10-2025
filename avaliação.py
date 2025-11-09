import csv

with open('filmes.txt', 'r', encoding='utf-8') as f:
    filmes = [linha.strip().split(', ') for linha in f if linha.strip()]

avaliacoes = []

for ano, titulo in filmes:
    while True:
        try:
            nota = float(input(f"Digite uma nota de 0 a 10 para '{titulo}': "))
            
            if 0 <= nota <= 10:
                avaliacoes.append([ano, titulo, nota])
                break  
            else:
                print("  Nota inválida! Digite um número entre 0 e 10.")
        except ValueError:
            print(" Entrada inválida! Digite apenas números.")


with open('filmes_avaliacao.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Ano', 'Filme', 'Nota'])
    writer.writerows(avaliacoes)

print("\n Avaliações salvas com sucesso no arquivo 'filmes_avaliacao.csv'!")
