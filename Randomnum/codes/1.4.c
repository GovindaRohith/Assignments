#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "source.h"
double variance(char *str)
{
return (meansquare(str)-mean(str)*mean(str));
}

int  main(void) //main function begins
{
printf("mean =%lf\n",mean("uni.dat"));
printf("variance=%lf\n",variance("uni.dat"));
return 0;
}


