#include<stdio.h>
#include<math.h>

int main()
{
    //input section
    double angle=M_PI/3;

    double num=sin(angle)-2*sin(angle)*sin(angle)*sin(angle);
    
    double den=2*cos(angle)*cos(angle)*cos(angle)-cos(angle);

    //output

    printf("%lf , %lf",(double)num/den,tan(angle));

    return 0;
}