"""
Lista de exercícios de revisão de Python
Disciplina: Programação para Análise de Dados
Nome do aluno: Vinícius Gama Dourado

Soluções corrigidas e testadas.
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
nome = input("Digite o seu nome: ")
cidade = input("Digite sua cidade: ")
print(f"Olá, {nome}! Você mora em {cidade}.")


# Exercício 3 — Soma de dois números
x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
total = x + y
print(f"A soma é: {total}")


# Exercício 4 — Operações básicas
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print(f"Soma: {x + y}")
print(f"Subtração: {x - y}")
print(f"Multiplicação: {x * y}")

if y != 0:
    print(f"Divisão: {x / y}")
else:
    print("Divisão: não é possível dividir por zero.")


# Exercício 5 — Média de três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")


# Exercício 6 — Idade no futuro
idade_atual = int(input("Digite sua idade atual: "))
idade_futura = idade_atual + 10
print(f"Daqui a 10 anos você terá {idade_futura} anos.")


# Exercício 7 — Conversão de temperatura
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")


# Exercício 8 — Área de um retângulo
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = largura * altura
print(f"A área do retângulo é: {area:.2f}")


# Exercício 9 — Manipulação de texto
frase = input("Digite uma frase: ")
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")
print(f"Quantidade de caracteres: {len(frase)}")


# Exercício 10 — Preço com desconto
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * percentual_desconto / 100
preco_final = preco - valor_desconto

print(f"Produto: {produto}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")


# ============================================================================
# 2. ESTRUTURA CONDICIONAL — EXERCÍCIOS 11 A 20
# ============================================================================

# Exercício 11 — Positivo, negativo ou zero
numero = float(input("Digite um número: "))

if numero == 0:
    print("O número é igual a zero.")
elif numero > 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")


# Exercício 12 — Par ou ímpar
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# Exercício 13 — Aprovação
media_aluno = float(input("Digite a média do aluno: "))

if media_aluno >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# Exercício 14 — Aprovação com recuperação
media_aluno = float(input("Digite a média do aluno: "))

if media_aluno >= 7:
    print("Aprovado")
elif media_aluno >= 5 and media_aluno < 7:
    print("Recuperação")
else:
    print("Reprovado")


# Exercício 15 — Maior entre dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero2 > numero1:
    print(f"O maior número é {numero2}.")
else:
    print("Os números são iguais.")


# Exercício 16 — Faixa etária
idade = int(input("Digite a idade: "))

if idade <= 11:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")


# Exercício 17 — Desconto na compra
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
    total = valor_compra * 0.90
else:
    total = valor_compra

print(f"Total: R$ {total:.2f}")


# Exercício 18 — Acesso ao sistema
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")


# Exercício 19 — Número dentro do intervalo
numero = float(input("Digite um número: "))

if numero >= 10 and numero <= 50:
    print("O número está dentro do intervalo.")
else:
    print("O número está fora do intervalo.")


# Exercício 20 — Calculadora simples
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, * ou /): ")

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
print(frutas)


# Exercício 22 — Acessando elementos
cores = ["azul", "verde", "amarelo", "vermelho"]
print(cores[0])
print(cores[-1])


# Exercício 23 — Adicionando elementos
nomes = ["Ana", "Bruno", "Carla"]
novo_nome = input("Digite outro nome: ")
nomes.append(novo_nome)
print(nomes)


# Exercício 24 — Removendo elementos
frutas = ["maçã", "banana", "laranja", "uva"]
frutas.remove("banana")
print(frutas)


# Exercício 25 — Alterando um elemento
frutas = ["maçã", "banana", "laranja", "uva"]
frutas[2] = "abacaxi"
print(frutas)


# Exercício 26 — Tamanho e presença
numeros = [10, 20, 30, 40, 50]
print(f"Quantidade de elementos: {len(numeros)}")

if 30 in numeros:
    print("O número 30 pertence à lista.")
else:
    print("O número 30 não pertence à lista.")


# Exercício 27 — Soma, maior e menor
valores = [12, 5, 28, 9, 17]
print(f"Soma: {sum(valores)}")
print(f"Maior: {max(valores)}")
print(f"Menor: {min(valores)}")


# Exercício 28 — Ordenação
cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]
cidades.sort()
print(cidades)


# Exercício 29 — Concatenação
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)


# Exercício 30 — Fatiamento
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Três primeiros:", numeros[:3])
print("Três últimos:", numeros[-3:])
print("Índices 2 ao 5:", numeros[2:6])


# ============================================================================
# 4. ESTRUTURAS DE REPETIÇÃO — EXERCÍCIOS 31 A 40
# ============================================================================

# Exercício 31 — Números de 1 a 10
for n in range(1, 11):
    print(n)


# Exercício 32 — Números pares
for n in range(2, 21, 2):
    print(n)


# Exercício 33 — Percorrendo nomes
nomes = ["Ana", "Bruno", "Carla", "Diego"]

for nome in nomes:
    print(nome)


# Exercício 34 — Quadrados
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

print(quadrados)


# Exercício 35 — Soma com for
valores = [10, 20, 30, 40, 50]
soma = 0

for valor in valores:
    soma = soma + valor

print(soma)


# Exercício 36 — Contando aprovados
notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]
aprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados = aprovados + 1

print(f"Quantidade de aprovados: {aprovados}")


# Exercício 37 — Contagem com while
numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1


# Exercício 38 — Contagem regressiva
numero = 10

while numero >= 1:
    print(numero)
    numero = numero - 1

print("Fim!")


# Exercício 39 — Senha correta
senha = input("Digite a senha: ")

while senha != "python123":
    print("Senha incorreta.")
    senha = input("Digite a senha novamente: ")

print("Senha correta.")


# Exercício 40 — Somando até zero
soma = 0
numero = int(input("Digite um número inteiro (0 para terminar): "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite outro número inteiro (0 para terminar): "))

print(f"Soma: {soma}")


# ============================================================================
# 5. DICIONÁRIOS — EXERCÍCIOS 41 A 50
# ============================================================================

# Exercício 41 — Criando um dicionário
aluno = {
    "nome": "Vinícius",
    "idade": 21,
    "curso": "Análise de Dados"
}
print(aluno)


# Exercício 42 — Acessando valores
produto = {"nome": "Teclado", "preco": 150.0, "estoque": 8}
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")


# Exercício 43 — Adicionando uma chave
produto = {"nome": "Mouse", "preco": 80.0}
produto["marca"] = "Logitech"
print(produto)


# Exercício 44 — Atualizando um valor
produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}
produto["estoque"] = 15
print(produto)


# Exercício 45 — Removendo uma chave
carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}
carro.pop("cor")
print(carro)


# Exercício 46 — Verificando uma chave
contato = {"nome": "Marina", "email": "marina@email.com"}

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

print(capitais.keys())
print(capitais.values())


# Exercício 48 — Percorrendo um dicionário
produtos = {
    "caderno": 25.0,
    "caneta": 4.5,
    "mochila": 120.0
}

for nome, preco in produtos.items():
    print(f"Produto: {nome} | Preço: R$ {preco:.2f}")


# Exercício 49 — Soma dos valores
estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 12,
    "monitor": 4
}

total_estoque = sum(estoque.values())
print(f"Total em estoque: {total_estoque}")


# Exercício 50 — Frequência de palavras
palavras = ["python", "dados", "python", "lista", "dados", "python"]
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] = frequencia[palavra] + 1
    else:
        frequencia[palavra] = 1

print(frequencia)