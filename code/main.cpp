#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "cut_log.h"


int main() {
    int inc = 1000, fim = 20000, stp = 1000;
    run_experiments(inc, fim, stp);
    return 0;
}
