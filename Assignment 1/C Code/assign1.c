#include<stdio.h>
#include<math.h>

int main()
{
    //input section
    double angle=0;

    double num=sin(angle)-2*sin(angle)*sin(angle)*sin(angle);
    
    double den=2*cos(angle)*cos(angle)*cos(angle)-cos(angle);

    //output
    if((double)num/den==(double)tan(angle))
    {
        printf("Verified");
    }
    else
    {
        printf("Not verified");
    }
    
    return 0;
}