#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "source.h"
int  main(void) //main function begins
{
//Uniform random numbers
double temp1,temp2;
temp1=estimator("combo.dat", "equi.dat",1000000,1);
temp2=estimator("combo.dat", "equi.dat",1000000,-1);
printf("P_(e|0)=%lf\n",temp1);
printf("P_(e|1)=%lf\n",temp2);
printf("Answer for the 5.5 part=%lf\n",(double)(temp1+temp2)/2);
return 0;
}


