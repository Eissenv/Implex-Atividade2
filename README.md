# Experimento de Corte de Tora

Este repositório contém um projeto para realizar um experimento de corte de tora, incluindo a compilação de um programa em C++ e a geração de gráficos usando Python.

## Compilação do Programa em C++

Para compilar o código em C++, siga os passos abaixo:

### Estrutura do Código

- **Arquivos**: `main.cpp`, `functions.cpp`, e `cut_log.h`
- **Executável**: `corte_tora`

### Comando para Compilar

1. No terminal, navegue até o diretório do projeto.
2. Execute o seguinte comando para compilar os arquivos `main.cpp` e `functions.cpp` e gerar o executável:

   ```bash
   g++ main.cpp functions.cpp -o corte_tora -O2

# Projeto de Geração de Gráficos com Python

Este projeto utiliza um script Python (`graphics.py`) para geração de gráficos, usando as bibliotecas `os` e `matplotlib.pyplot`. Para garantir que as dependências do projeto não conflitem com outras bibliotecas Python instaladas no sistema, recomenda-se o uso de um ambiente virtual.

## Requisitos

- **Python**: Versão 3.6 ou superior.
- **Bibliotecas Python**:
  - `os` (inclusa na biblioteca padrão do Python).
  - `matplotlib` (necessária para a geração de gráficos).
- **C++**: Necessário para compilar o código principal (`main.cpp` e `functions.cpp`).

## Configuração do Ambiente Virtual

Siga as instruções abaixo para configurar o ambiente virtual `generateGraphics` em sistemas Linux e Windows:

### 1. Criar o Ambiente Virtual

No terminal, dentro do diretório do projeto, execute o comando correspondente ao seu sistema operacional para criar o ambiente virtual:

- **Linux**:
  ```bash
  python3 -m venv generateGraphics
### Ativar o Ambiente virtual
 source generateGraphics/bin/activate

- **Windows**:
  ```bash
  python -m venv generateGraphics
### Ativar o Ambiente virtual 
    ./generateGraphics\Scripts\activate

## Dependências

Para instalar as dependências, você deve estar dentro do ambiente virtual, logo após, insira o seguinte comando:

pip install matplotlib

### Desativar o Ambiente Virtual

Quando terminar de usar o ambiente virtual, desative-o para retornar ao ambiente global do sistema:

deactivate

