/*
Code by Govinda Rohith Y
CS21BTECH11062
for NCERT class 12 Exercise 13.1 prob 1
*/
#include<stdio.h>
int main()
{
    //pe denotes Pr(E) 
    //pf denotes Pr(F)
    //pexf denotes Pr(E intersection F)
    double pe=0.6;
    double pf=0.3;
    double pexf=0.2;
    printf("Pr(E|F)=%lf\nPr(F|E)=%lf",(double)pexf/pf,(double)pexf/pe);
    return 0;
}