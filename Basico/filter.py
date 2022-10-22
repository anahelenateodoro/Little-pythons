nomes = ['Alessandra', 'Giesle', 'Jo', 'Olinda', 'Jaqueline', 'Marcos', 'Evilazio', 'Nadjane','Leandro', 'Gloria']

def nomes_vogais(x):
  return x[1].lower() in Valor_input #lower() é um método embutido usado para manipulação de strings.

Valor_input = input('Digite para filtar: ')

nomes_filtrados = filter(nomes_vogais, nomes)

print(list(nomes_filtrados))