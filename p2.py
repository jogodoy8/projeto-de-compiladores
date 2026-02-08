# p2.py
# Executor de Código Objeto – Máquina Hipotética
# Parte 2 do Projeto de Compiladores

class Instrucao:
    def __init__(self, instrucao, argumento=None):
        self.instrucao = instrucao
        self.argumento = argumento

def carregar_codigo(arquivo):
    """
    Lê o código objeto gerado pelo compilador (p1.py)
    e transforma em uma lista de instruções.
    """
    codigo = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split()
            instrucao = partes[0]
            argumento = None

            if len(partes) > 1:
                try:
                    argumento = int(partes[1])
                except ValueError:
                    argumento = float(partes[1])

            codigo.append(Instrucao(instrucao, argumento))
    return codigo


if __name__ == "__main__":
    codigo = carregar_codigo("codigoCompilado.txt")

    # Pilha de dados
    D = []

    # Ponteiro de instrução
    i = 0

    while i < len(codigo):
        instr = codigo[i].instrucao
        arg = codigo[i].argumento

        if instr == "INPP":
            D.clear()

        elif instr == "ALME":
            D.append(0)

        elif instr == "CRCT":
            D.append(arg)

        elif instr == "CRVL":
            D.append(D[arg])

        elif instr == "SOMA":
            b = D.pop()
            a = D.pop()
            D.append(a + b)

        elif instr == "SUBT":
            b = D.pop()
            a = D.pop()
            D.append(a - b)

        elif instr == "MULT":
            b = D.pop()
            a = D.pop()
            D.append(a * b)

        elif instr == "DIVI":
            b = D.pop()
            a = D.pop()
            D.append(a / b)

        elif instr == "ARMZ":
            D[arg] = D.pop()

        elif instr == "LEIT":
            valor = float(input("Digite um valor: "))
            D.append(valor)

        elif instr == "IMPR":
            print(D.pop())

        elif instr == "PARA":
            print("Execução finalizada.")
            break

        else:
            print(f"Erro: instrução desconhecida {instr}")
            break

        i += 1
