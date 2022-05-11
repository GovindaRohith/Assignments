/*
Code by Govinda Rohith Y
CS21BTECH11062
for NCERT class 12 Example 15
*/
#include<stdio.h>
int main()
{
    double px1=0.65;
    double px0=1.00-0.65;
    //px1 represents P(X=1) 
    //px0 represents P(X=0)
    double pa=0.80;
    double pb=0.32;
    //pa represents P(Y=1|X=0)
    //pb represents P(Y=1|X=1)
    printf("P(Y=1)=%lf",px1*pb+px0*pa);
    return 0;
}