/*
Code by Govinda Rohith Y
CS21BTECH11062
for Assignment-9 from Papoullis Text Book 2-24
*/
#include<stdio.h>
int main()
{
    double x0=0.5;
    double x1=0.5;
    double x20=(double)(100*99)/(1000*999);
    double x21=(double)(100*99)/(2000*1999);
    //x0 denotes Pr(X=0)
    //x1 denotes Pr(X=1)
    //x20 denotes Pr(X=2|X=0)
    //x21 denotes Pr(X=2|X=1)
    printf("Pr(X=2)=%lf\n",x0*x20+x1*x21);
    printf("Pr(X=0|X=2)=%lf\n",(double)(x0*11)/((x0*x20+x1*x21)*1110));
}