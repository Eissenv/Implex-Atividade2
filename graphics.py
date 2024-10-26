import matplotlib.pyplot as plt

# Carregar dados do arquivo de resultados
data = []
with open('resultados.txt', 'r') as f:
    next(f)  # Pular cabeçalho
    for line in f:
        if line.strip():  # Ignorar linhas vazias
            n, vDP, tDP, vGreedy, tGreedy, acc = map(float, line.split())
            data.append((n, vDP, tDP, vGreedy, tGreedy, acc))

# Separar os dados em listas
n_values = [int(row[0]) for row in data]  # 'n' como inteiro
vDP_values = [row[1] for row in data]
vGreedy_values = [row[3] for row in data]
tDP_values = [row[2] for row in data]
tGreedy_values = [row[4] for row in data]

# Gráfico de Valor Total de Venda
plt.figure(figsize=(10, 5))
plt.plot(n_values, vDP_values, label='Programação Dinâmica', linestyle='-', marker='o', color='blue')
plt.plot(n_values, vGreedy_values, label='Guloso', linestyle='--', marker='x', color='red')
plt.xlabel('Comprimento da Tora (n)', fontsize=12)
plt.ylabel('Valor Total de Venda', fontsize=12)
plt.title('Programação Dinâmica vs. Guloso (Valor de Venda)', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('valor_total_venda.png')  # Salvar o gráfico em um arquivo

# Gráfico de Tempo de Execução
plt.figure(figsize=(10, 5))
plt.plot(n_values, tDP_values, label='Programação Dinâmica', linestyle='-', marker='o', color='blue')
plt.plot(n_values, tGreedy_values, label='Guloso', linestyle='--', marker='x', color='red')
plt.xlabel('Comprimento da Tora (n)', fontsize=12)
plt.ylabel('Tempo de Execução (s)', fontsize=12)
plt.title('Programação Dinâmica vs. Guloso (Tempo de Execução)', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('tempo_execucao.png')  # Salvar o gráfico em um arquivo

plt.show()  # Mostrar os gráficos
