#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "source.h"
int  main(void) //main function begins
{
//Uniform random numbers
printf("P_(e|0)=%lf\n",estimator("combo.dat", "equi.dat",1000000,1));
printf("P_(e|1)=%lf\n",estimator("combo.dat", "equi.dat",1000000,-1));
return 0;
}


