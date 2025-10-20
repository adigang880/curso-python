
import matplotlib.pyplot as plt

def curva_total(pot, inicio, dur):
    p = [0.0]*24
    for k in range(dur):
        p[inicio+k] += pot

    return p

eqs = [] #Lista principal que vai guardar todas as sublistas de equipamentos

while True:
    print("\n--- Cadastro de novo equipamento ---")
    nome = input("Nome do equipamento: ").strip()
    pot = float(input("Potência (W): ").strip())
    inicio = int(input("Hora inicial (0–23): ").strip())
    dur = int(input("Duração (h): ").strip())

    # Cada equipamento será uma lista com 4 informações
    equipamento = [nome, pot, inicio, dur]

    # Adiciona essa lista dentro da lista principal
    eqs.append(equipamento)
    # Pergunta se quer continuar
    mais = input("Adicionar outro equipamento? (s/n): ")
    if mais != "s":
        break


p_total = [0.0] * 24  # vetor acumulador

for eq in eqs:
    nome, pot, inicio, dur = eq
    p_eq = curva_total(pot, inicio, dur)  # curva individual
    # soma cada hora
    for h in range(24):
        p_total[h] += p_eq[h]

h = list(range(24))
plt.figure()
plt.step(h + [24], p_total + [p_total[-1]])
plt.xlabel("Hora")
plt.ylabel("Potência [W]")
plt.title("Curva de carga (W)")
plt.grid(True)
plt.savefig('Figura_1.png')
plt.show()

