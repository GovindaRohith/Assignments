/*
2017 ICSE Grade 12 Question 1-ii
Govinda Rohith Y
CS21BTECH11062

*/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double n_finder(double a,double b,double l,double m)
{
    //function which returns n 
    //n^2=a^2 l^2-b^2 m^2
    return sqrt(a*a*l*l-b*b*m*m);
}
int main()
{
    //equation of hyper bola  x^2/a^2-y^2/b^2=1
    //equation of line is lx+my+n
    double a=sqrt(5);
    double b=sqrt(3);
    double l=-2;
    double m=1;
    printf("%lf,-%lf",n_finder(a,b,l,m),n_finder(a,b,l,m));
    return 0;
}