"""
Lista de exercícios de revisão de Python

Nome: Vinícius Gama Dourado
"""

# ============================================================================
# 1. VARIÁVEIS — EXERCÍCIOS 1 A 10
# ============================================================================

# Exercício 1 — Dados pessoais
nome = "Vinícius Gama Dourado"
idade = 21
altura = 1.76
eh_estudante = True

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(eh_estudante, type(eh_estudante))


# Exercício 2 — Saudação
nome = "Vinícius"
cidade = "Brasília"
print(f"Olá, {nome}! Você mora em {cidade}.")


# Exercício 3 — Soma de dois números
x = 15
y = 25
total = x + y
print(f"A soma de {x} + {y} é: {total}")


# Exercício 4 — Operações básicas
x = 50.0
y = 5.0

print(f"Soma: {x + y}")
print(f"Subtração: {x - y}")
print(f"Multiplicação: {x * y}")
if y != 0:
    print(f"Divisão: {x / y}")
else:
    print("Divisão: não é possível dividir por zero.")


# Exercício 5 — Média de três notas
nota1 = 8.5
nota2 = 7.0
nota3 = 9.5
media = (nota1 + nota2 + nota3) / 3
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"A média das notas é: {media:.2f}")


# Exercício 6 — Idade no futuro
idade_atual = 21
idade_futura = idade_atual + 10
print(f"Idade atual: {idade_atual}")
print(f"Daqui a 10 anos você terá {idade_futura} anos.")


# Exercício 7 — Conversão de temperatura
celsius = 30.0
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura de {celsius}°C em Fahrenheit é: {fahrenheit:.2f}°F")


# Exercício 8 — Área de um retângulo
largura = 5.5
altura = 10.0
area = largura * altura
print(f"A área do retângulo de {largura}x{altura} é: {area:.2f}")


# Exercício 9 — Manipulação de texto
frase = "Python para Análise de Dados"
print(f"Frase original: {frase}")
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")
print(f"Quantidade de caracteres: {len(frase)}")


# Exercício 10 — Preço com desconto
produto = "Notebook"
preco = 4500.00
percentual_desconto = 15.0

valor_desconto = preco * percentual_desconto / 100
preco_final = preco - valor_desconto

print(f"Produto: {produto}")
print(f"Valor original: R$ {preco:.2f} | Desconto: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")


# ============================================================================
# 2. ESTRUTURA CONDICIONAL — EXERCÍCIOS 11 A 20
# ============================================================================

# Exercício 11 — Positivo, negativo ou zero
numero = -15.5
print(f"Analisando o número: {numero}")
if numero == 0:
    print("O número é igual a zero.")
elif numero > 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")


# Exercício 12 — Par ou ímpar
numero = 42
print(f"Analisando o número: {numero}")
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# Exercício 13 — Aprovação
media_aluno = 7.5
print(f"Média: {media_aluno}")
if media_aluno >= 7:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")


# Exercício 14 — Aprovação com recuperação
media_aluno = 6.0
print(f"Média: {media_aluno}")
if media_aluno >= 7:
    print("Status: Aprovado")
elif media_aluno >= 5 and media_aluno < 7:
    print("Status: Recuperação")
else:
    print("Status: Reprovado")


# Exercício 15 — Maior entre dois números
numero1 = 85.0
numero2 = 120.0
print(f"Números: {numero1} e {numero2}")
if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero2 > numero1:
    print(f"O maior número é {numero2}.")
else:
    print("Os números são iguais.")


# Exercício 16 — Faixa etária
idade = 21
print(f"Idade: {idade}")
if idade <= 11:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")


# Exercício 17 — Desconto na compra
valor_compra = 150.0
if valor_compra > 100:
    total = valor_compra * 0.90
    print("Desconto de 10% aplicado!")
else:
    total = valor_compra

print(f"Valor original: R$ {valor_compra:.2f} | Total a pagar: R$ {total:.2f}")


# Exercício 18 — Acesso ao sistema
usuario = "admin"
senha = "1234"
print(f"Tentativa de login com usuário '{usuario}' e senha '{senha}'")
if usuario == "admin" and senha == "1234":
    print("Status: Acesso permitido")
else:
    print("Status: Acesso negado")


# Exercício 19 — Número dentro do intervalo
numero = 35.0
print(f"Número escolhido: {numero}")
if numero >= 10 and numero <= 50:
    print("O número está dentro do intervalo de 10 a 50.")
else:
    print("O número está fora do intervalo de 10 a 50.")


# Exercício 20 — Calculadora simples
numero1 = 20.0
numero2 = 4.0
operacao = "/"
print(f"Calculando: {numero1} {operacao} {numero2}")
if operacao == "+":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
    else:
        print("Não é possível dividir por zero.")
else:
    print("Operação inválida.")


# ============================================================================
# 3. LISTAS — EXERCÍCIOS 21 A 30
# ============================================================================

# Exercício 21 — Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista de frutas:", frutas)


# Exercício 22 — Acessando elementos
cores = ["azul", "verde", "amarelo", "vermelho"]
print(f"Primeiro elemento: {cores[0]}")
print(f"Último elemento: {cores[-1]}")


# Exercício 23 — Adicionando elementos
nomes = ["Ana", "Bruno", "Carla"]
novo_nome = "Daniel"
nomes.append(novo_nome)
print(f"Lista após adicionar '{novo_nome}':", nomes)


# Exercício 24 — Removendo elementos
frutas = ["maçã", "banana", "laranja", "uva"]
frutas.remove("banana")
print("Lista após remover 'banana':", frutas)


# Exercício 25 — Alterando um elemento
frutas = ["maçã", "banana", "laranja", "uva"]
frutas[2] = "abacaxi"
print("Lista após substituir o índice 2 por 'abacaxi':", frutas)


# Exercício 26 — Tamanho e presença
numeros = [10, 20, 30, 40, 50]
print(f"Quantidade de elementos: {len(numeros)}")
if 30 in numeros:
    print("O número 30 pertence à lista.")
else:
    print("O número 30 não pertence à lista.")


# Exercício 27 — Soma, maior e menor
valores = [12, 5, 28, 9, 17]
print(f"Lista de valores: {valores}")
print(f"Soma: {sum(valores)}")
print(f"Maior: {max(valores)}")
print(f"Menor: {min(valores)}")


# Exercício 28 — Ordenação
cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]
cidades.sort()
print("Cidades ordenadas em ordem alfabética:", cidades)


# Exercício 29 — Concatenação
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(f"Lista A: {lista_a} | Lista B: {lista_b}")
print("Concatenação (Lista C):", lista_c)


# Exercício 30 — Fatiamento
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista completa:", numeros)
print("Três primeiros:", numeros[:3])
print("Três últimos:", numeros[-3:])
print("Índices 2 ao 5:", numeros[2:6])


# ============================================================================
# 4. ESTRUTURAS DE REPETIÇÃO — EXERCÍCIOS 31 A 40
# ============================================================================

# Exercício 31 — Números de 1 a 10
print("Números de 1 a 10:")
for n in range(1, 11):
    print(n, end=" ")
print() # Pula linha


# Exercício 32 — Números pares
print("Números pares de 2 a 20:")
for n in range(2, 21, 2):
    print(n, end=" ")
print()


# Exercício 33 — Percorrendo nomes
nomes = ["Ana", "Bruno", "Carla", "Diego"]
for nome in nomes:
    print(f"Nome: {nome}")


# Exercício 34 — Quadrados
numeros = [1, 2, 3, 4, 5]
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2)
print(f"Originais: {numeros} -> Quadrados: {quadrados}")


# Exercício 35 — Soma com for
valores = [10, 20, 30, 40, 50]
soma = 0
for valor in valores:
    soma = soma + valor
print(f"A soma dos valores {valores} é: {soma}")


# Exercício 36 — Contando aprovados
notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]
aprovados = 0
for nota in notas:
    if nota >= 7:
        aprovados = aprovados + 1
print(f"Notas da turma: {notas}")
print(f"Quantidade de aprovados (nota >= 7): {aprovados}")


# Exercício 37 — Contagem com while
numero = 1
print("Contagem com while:")
while numero <= 10:
    print(numero, end=" ")
    numero = numero + 1
print()


# Exercício 38 — Contagem regressiva
numero = 10
print("Contagem regressiva:")
while numero >= 1:
    print(numero, end=" ")
    numero = numero - 1
print("\nFim!")


# Exercício 39 — Senha correta
# Adaptado para rodar sem input usando uma lista de tentativas simuladas
tentativas_senha = ["admin", "12345", "python123"]
indice = 0
senha = tentativas_senha[indice]

while senha != "python123":
    print(f"Digitou: '{senha}' -> Senha incorreta.")
    indice += 1
    senha = tentativas_senha[indice]

print(f"Digitou: '{senha}' -> Senha correta.")


# Exercício 40 — Somando até zero
# Adaptado para rodar sem input usando uma lista de números simulados
soma = 0
entradas = [15, 25, 10, 0] # 0 é a condição de parada
indice = 0
numero = entradas[indice]
print(f"Números digitados: {entradas}")

while numero != 0:
    soma = soma + numero
    indice += 1
    numero = entradas[indice]

print(f"Soma total: {soma}")


# ============================================================================
# 5. DICIONÁRIOS — EXERCÍCIOS 41 A 50
# ============================================================================

# Exercício 41 — Criando um dicionário
aluno = {
    "nome": "Vinícius Gama Dourado",
    "idade": 21,
    "curso": "Análise de Dados"
}
print(aluno)


# Exercício 42 — Acessando valores
produto = {"nome": "Teclado", "preco": 150.0, "estoque": 8}
print(f"Nome do produto: {produto['nome']}")
print(f"Preço do produto: R$ {produto['preco']:.2f}")


# Exercício 43 — Adicionando uma chave
produto = {"nome": "Mouse", "preco": 80.0}
produto["marca"] = "Logitech"
print("Dicionário após adicionar 'marca':", produto)


# Exercício 44 — Atualizando um valor
produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}
produto["estoque"] = 15
print("Dicionário após atualizar o 'estoque':", produto)


# Exercício 45 — Removendo uma chave
carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}
carro.pop("cor")
print("Dicionário após remover a 'cor':", carro)


# Exercício 46 — Verificando uma chave
contato = {"nome": "Marina", "email": "marina@email.com"}
print(f"Contato: {contato}")
if "telefone" in contato:
    print("A chave telefone existe.")
else:
    print("A chave telefone não existe.")


# Exercício 47 — Chaves e valores
capitais = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}
print("Chaves (Países):", list(capitais.keys()))
print("Valores (Capitais):", list(capitais.values()))


# Exercício 48 — Percorrendo um dicionário
produtos = {
    "caderno": 25.0,
    "caneta": 4.5,
    "mochila": 120.0
}
for nome, preco in produtos.items():
    print(f"Produto: {nome.capitalize()} | Preço: R$ {preco:.2f}")


# Exercício 49 — Soma dos valores
estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 12,
    "monitor": 4
}
total_estoque = sum(estoque.values())
print(f"Estoque por item: {estoque}")
print(f"Total de itens em estoque: {total_estoque}")


# Exercício 50 — Frequência de palavras
palavras = ["python", "dados", "python", "lista", "dados", "python"]
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] = frequencia[palavra] + 1
    else:
        frequencia[palavra] = 1

print("Contagem de frequência das palavras:")
print(frequencia)