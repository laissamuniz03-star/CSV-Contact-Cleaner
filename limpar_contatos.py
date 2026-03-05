import csv
import re

entrada = "contatos.csv"
saida = "contatos_corrigidos.csv"

def corrigir_numero(numero):

    if not numero:
        return numero

    # pega apenas o primeiro número se houver ::: 
    numero = numero.split(":::")[0]

    # remove qualquer caractere que não seja número
    numero = re.sub(r"\D", "", numero)

    # se tiver 8 dígitos → sem DDD
    if len(numero) == 8:
        numero = "859" + numero

    # se tiver 9 dígitos → sem DDD mas já tem 9
    elif len(numero) == 9:
        numero = "85" + numero

    # se tiver 10 dígitos → tem DDD mas falta o 9
    elif len(numero) == 10:
        numero = numero[:2] + "9" + numero[2:]

    # se tiver 11 dígitos → já está correto
    elif len(numero) == 11:
        pass

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

print("CSV corrigido mantendo padrão do Google Contatos!")
