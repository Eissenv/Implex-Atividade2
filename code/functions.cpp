#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "cut_log.h"



void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Função para particionar o array
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// Função do QuickSort
void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

// Função de corte da tora usando programação dinâmica
int cut_rod_dynamic(int prices[], int n) {
    int *dp = (int *)malloc((n + 1) * sizeof(int));
    if (dp == NULL) {
        printf("Erro na alocação de memória!\n");
        return -1;
    }

    dp[0] = 0;

    for (int i = 1; i <= n; i++) {
        int max_val = -1; // Inicialização de max_val com -1
        for (int j = 0; j < i; j++) {
            if (prices[j] + dp[i - j - 1] > max_val) {
                max_val = prices[j] + dp[i - j - 1];
            }
        }
        dp[i] = max_val;
    }

    int result = dp[n];
    free(dp);
    return result;
}

// Função de corte da tora usando estratégia gulosa
int cut_rod_greedy(int prices[], int n) {
    int total_value = 0;
    while (n > 0) {
        int max_density = 0;
        int best_piece = 0;
        for (int i = 1; i <= n; i++) {
            int density = prices[i - 1] / i;
            if (density > max_density) {
                max_density = density;
                best_piece = i;
            }
        }
        total_value += prices[best_piece - 1];
        n -= best_piece;
    }
    return total_value;
}

// Função para gerar preços aleatórios
void generate_prices(int prices[], int n) {
    for (int i = 0; i < n; i++) {
        prices[i] = rand() % n + 1;
    }
}

// Função para executar os experimentos e salvar os resultados em um arquivo
void run_experiments(int inc, int fim, int stp) {
    FILE *outfile = fopen("results\\resultados.txt", "w");

    if (outfile == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return;
    }

    fprintf(outfile, "n vDP tDP vGreedy tGreedy %%\n");
    printf("%-8s %-12s %-10s %-12s %-12s %-10s\n", "n", "vDP", "tDP", "vGreedy", "tGreedy", "Accuracy");
    
    for (int n = inc; n <= fim; n += stp) {
        int *prices = (int *)malloc(n * sizeof(int));
        if (prices == NULL) {
            printf("Erro na alocação de memória para preços!\n");
            fclose(outfile);
            return;
        }
        
        generate_prices(prices, n);
        quicksort(prices, 0, n - 1);

        // Programação Dinâmica
        clock_t start = clock();
        int vDP = cut_rod_dynamic(prices, n);
        double tDP = (double)(clock() - start) / CLOCKS_PER_SEC;

        // Estratégia Gulosa
        start = clock();
        int vGreedy = cut_rod_greedy(prices, n);
        double tGreedy = (double)(clock() - start) / CLOCKS_PER_SEC;

        double accuracy = (vGreedy / (double)vDP) * 100;

        fprintf(outfile, "%d %d %.6f %d %.6f %.2f\n", n, vDP, tDP, vGreedy, tGreedy, accuracy);
        printf("%-8d %-12d %-10.6f %-12d %-12.6f  %-8.2f%%\n", n, vDP, tDP, vGreedy, tGreedy, accuracy);

        free(prices);
    }

    fclose(outfile);
}