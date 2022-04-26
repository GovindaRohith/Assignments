/*
Code by Govinda Rohith Y
CS21BTECH11062
for NECRT class 10 Exercise 15.1 prob 7
*/
#include<stdio.h>
int main()
{
    //let A denotes Pr(X=0)(2 students dont have same birthday) and B denotes Pr(X=1)(2 students have same birthday)
    double pr_A=0.992;
    double pr_B=1-pr_A;
    printf("%lf",pr_B);
    return 0;
}