# Declarando uma classe para exceção de valores negativos
class NumNegativo(Exception):
    pass

# Inicializando o programa
programa = "Meus Filmes Favoritos da Netflix"
print(f"\033[1m{programa:^60}\033[0m")
print("-" * 60)

colecao_principal = []
continuar = 's'

while continuar == 's':
    filme = {}
    filme['titulo'] = input("Digite o título do filme: ")
    filme['genero'] = input("Digite o gênero do filme: ")

    try:
        filme['qtde exibicoes'] = int(input("Digite a quantidade de exibições: "))
        if filme['qtde exibicoes'] < 0:
            raise NumNegativo

    except ValueError as v:
        print('Você deve entrar com um valor numérico')
    except NumNegativo as n:
        print('Você deve entrar com um valor positivo')
    except Exception as e:
        print(e)

    else:
        colecao_principal.append(filme)

    continuar = input("Deseja adicionar outro filme? (s/n) ").lower()

print("-" * 60)
print(colecao_principal)
print("-" * 60)

titulo = "Filmes do gênero AVENTURA"
contador_aventura = 0
print(f"\033[1m{titulo:^60}\033[0m")

for filme in colecao_principal:
    if filme['genero'].upper() == 'AVENTURA':
        print(f"{filme['titulo']} – {filme['qtde exibicoes']} exibições")
        contador_aventura += 1

print(f"Quantidade de filmes do gênero Aventura: {contador_aventura}")
print("-" * 60)
