import csv
import re

entrada = "contatos.csv"
saida = "contatos_limpos.csv"

telefones_vistos = set()
contatos = []

def limpar_numero(numero):
    numero = re.sub(r"\D", "", numero)

    if numero.startswith("55"):
        numero = numero[2:]

    if len(numero) == 8:
        numero = "9" + numero

    if len(numero) == 9:
        numero = "85" + numero

    if len(numero) == 10:
        numero = "9" + numero

    if len(numero) == 11 and not numero.startswith("85"):
        numero = "85" + numero[-9:]

    return "55" + numero


with open(entrada, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        texto = " ".join(linha)

        numeros = re.findall(r"\+?\d[\d\s\-]{7,}", texto)

        for num in numeros:
            telefone = limpar_numero(num)

            if telefone not in telefones_vistos:
                telefones_vistos.add(telefone)
                nome = linha[0] if linha else "Sem Nome"

                contatos.append([nome, telefone])


with open(saida, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Name", "Phone 1 - Type", "Phone 1 - Value"])

    for nome, telefone in contatos:
        escritor.writerow([nome, "Mobile", "+" + telefone])

print("Contatos únicos:", len(contatos))
print("Arquivo gerado:", saida)
