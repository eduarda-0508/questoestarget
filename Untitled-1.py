def pertence_fibonacci(numero):
    # Verifica se o número é negativo
    if numero < 0:
        return False
    
    # Inicializa os primeiros dois números da sequência de Fibonacci
    a, b = 0, 1
    
    # Gera a sequência de Fibonacci até encontrar o número ou ultrapassar o número
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    
    return False

def main():
    # Número definido para verificação
    numero = 50  # Substitua esse valor pelo número que você deseja verificar
    
    # Verifica se o número pertence à sequência de Fibonacci
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()

#questao 3 
import json

dados_faturamento = '''[
    {"dia": 1, "valor": 1000},
    {"dia": 2, "valor": 1500},
    {"dia": 3, "valor": 0},
    {"dia": 4, "valor": 1200},
    {"dia": 5, "valor": 0},
    {"dia": 6, "valor": 1800}
]'''

faturamento = json.loads(dados_faturamento)

# Filtra dias com faturamento
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Menor e maior valor
menor_faturamento = min(valores)
maior_faturamento = max(valores)

# Média mensal
media_mensal = sum(valores) / len(valores)

# Dias acima da média
dias_acima_media = len([v for v in valores if v > media_mensal])

print(f"Menor faturamento: R$ {menor_faturamento}")
print(f"Maior faturamento: R$ {maior_faturamento}")
print(f"Dias acima da média: {dias_acima_media}")

#questao 4
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")

#questao 5 
def inverter_string(s):
    invertida = ''
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

# String definida
texto = "Inverter esta string"
print(inverter_string(texto))
