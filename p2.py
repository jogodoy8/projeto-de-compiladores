# p2.py
# Executor de Código Objeto (Máquina Hipotética)
# Parte 2 do Projeto de Compiladores

class Instrucao:
    def __init__(self, instrucao, argumento=None):
        self.instrucao = instrucao
        self.argumento = argumento

    def __repr__(self):
        return f"{self.instrucao} {self.argumento if self.argumento is not None else ''}".strip()


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

    # Topo da pilha
    s = -1

    while i < len(codigo):
        instr = codigo[i].instrucao
        arg = codigo[i].argumento

        if instr == "INPP":
            s = -1

        elif instr == "ALME":
            for _ in range(arg):
                D.append(0)
                s += 1

        elif instr == "CRCT":
            D.append(arg)
            s += 1

        elif instr == "CRVL":
            D.append(D[arg])
            s += 1

        elif instr == "SOMA":
            D[s-1] = D[s-1] + D[s]
            D.pop()
            s -= 1

        elif instr == "SUBT":
            D[s-1] = D[s-1] - D[s]
            D.pop()
            s -= 1

        elif instr == "MULT":
            D[s-1] = D[s-1] * D[s]
            D.pop()
            s -= 1

        elif instr == "DIVI":
            D[s-1] = D[s-1] / D[s]
            D.pop()
            s -= 1

        elif instr == "ARMZ":
            D[arg] = D[s]
            D.pop()
            s -= 1

        elif instr == "LEIT":
            valor = float(input("Digite um valor: "))
            D.append(valor)
            s += 1

        elif instr == "IMPR":
            print(D[s])
            D.pop()
            s -= 1

        elif instr == "PARA":
            print("Execução finalizada.")
            break

        else:
            print(f"Erro: instrução desconhecida {instr}")
            break

        i += 1
