#include<stdio.h>
double mean_calculator(int data[])
{
    int sum=data[0]+data[1]+data[2]+data[3]+data[4];
    return (double)sum/5;
}
int main()
{
    int data[5]={70, 71, 75, 77, 72};
    printf("mean of first data%lf\n",mean_calculator(data));
    int seconddata[5]={10,15,20,25,95};
    printf("mean of second data%lf\n",mean_calculator(seconddata));
    return 0;
}