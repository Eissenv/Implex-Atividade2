import os
import matplotlib.pyplot as plt

# Construir o caminho para o arquivo resultados.txt com base na localização do script
script_dir = os.path.dirname(os.path.abspath(__file__))  
resultados_path = os.path.join(script_dir, '../code/results/resultados.txt')  

# Carregar dados do arquivo resultados.txt
data = []
try:
    with open(resultados_path, 'r') as f:
        next(f)  # Pular o cabeçalho
        for line in f:
            if line.strip():  # Ignorar linhas vazias
                n, vDP, tDP, vGreedy, tGreedy, acc = map(float, line.split())
                data.append((n, vDP, tDP, vGreedy, tGreedy, acc))
except FileNotFoundError:
    print(f"Arquivo não encontrado: {resultados_path}")
    exit(1)

# Separar os dados em listas
n_values = [int(row[0]) for row in data]
vDP_values = [row[1] for row in data]
vGreedy_values = [row[3] for row in data]
tDP_values = [row[2] for row in data]
tGreedy_values = [row[4] for row in data]

# Criar e salvar o gráfico de "Valor Total de Venda"
plt.figure(figsize=(10, 5))
plt.plot(n_values, vDP_values, label='Programação Dinâmica', linestyle='-', marker='o', color='blue')
plt.plot(n_values, vGreedy_values, label='Guloso', linestyle='--', marker='x', color='red')
plt.xlabel('Comprimento da Tora (n)', fontsize=12)
plt.ylabel('Valor Total de Venda', fontsize=12)
plt.title('Programação Dinâmica vs. Guloso (Valor de Venda)', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
output_dir = os.path.join(script_dir, '../generateGraphics/image')  # Ajustar o caminho conforme necessário
os.makedirs(output_dir, exist_ok=True)  # Criar o diretório, se não existir
plt.savefig(os.path.join(output_dir, 'valor_total_venda.png'))

# Criar e salvar o gráfico de "Tempo de Execução"
plt.figure(figsize=(10, 5))
plt.plot(n_values, tDP_values, label='Programação Dinâmica', linestyle='-', marker='o', color='blue')
plt.plot(n_values, tGreedy_values, label='Guloso', linestyle='--', marker='x', color='red')
plt.xlabel('Comprimento da Tora (n)', fontsize=12)
plt.ylabel('Tempo de Execução (s)', fontsize=12)
plt.title('Programação Dinâmica vs. Guloso (Tempo de Execução)', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'tempo_execucao.png'))

plt.show()  # Exibir os gráficos
