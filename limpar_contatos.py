import csv
import re

entrada = "contatos.csv"
saida = "contatos_corrigidos.csv"

def corrigir_numero(numero):

    if not numero:
        return numero

    # pega apenas o primeiro número se houver :::
    numero = numero.split(":::")[0]

    # remove tudo que não for número
    numero = re.sub(r"\D", "", numero)

    # remove código do Brasil
    if numero.startswith("55"):
        numero = numero[2:]

    # sem DDD (8 dígitos)
    if len(numero) == 8:
        numero = "859" + numero

    # sem DDD mas já com 9
    elif len(numero) == 9:
        numero = "85" + numero

    # tem DDD mas falta 9
    elif len(numero) == 10:
        numero = numero[:2] + "9" + numero[2:]

    # se tiver 11 já está correto
    return numero


with open(entrada, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    campos = leitor.fieldnames
    linhas = list(leitor)

for linha in linhas:
    linha["Phone 1 - Value"] = corrigir_numero(linha["Phone 1 - Value"])

with open(saida, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(linhas)

print("Contatos corrigidos e prontos para importar no Google!")

