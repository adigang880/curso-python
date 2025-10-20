# curva_carga_residencial.py
import matplotlib.pyplot as plt

# TODO fazer isos epois 

class Equipamento:
    def __init__(self, nome, pot_w, inicio_h, dur_h):
        self.nome = nome
        self.pot_w = float(pot_w)
        self.inicio = int(inicio_h)
        self.dur = int(dur_h)


def curva_total(equipamentos):
    h = list(range(24))
    p = [0.0]*24
    for e in equipamentos:
        for k in range(e.dur):
            p[(e.inicio + k)] += e.pot_w
    return h, p


def plotar(h, p, titulo="Curva de carga (W)"):
    plt.figure()
    plt.step(h + [24], p + [p[-1]], where="post")
    plt.xlim(0, 24)
    plt.xlabel("Hora")
    plt.ylabel("Potência [W]")
    plt.title(titulo)
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    eqs = []
    while True:
        nome = input("Nome do equipamento: ").strip()
        pot = float(input("Potência (W): ").strip())
        inicio = int(input("Hora inicial (0–23): ").strip())
        dur = int(input("Duração (h): ").strip())
        eqs.append(Equipamento(nome, pot, inicio, dur))

        mais = input("Adicionar outro equipamento? (s/n): ").strip().lower()
        if mais != "s":
            break

    if not eqs:
        print("Nenhum equipamento informado.")
    

    h, p = curva_total(eqs)
    plotar(h, p, "Curva de carga (W)")
