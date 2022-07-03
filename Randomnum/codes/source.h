//begin declaration
void uniform(char *str,int len);
double mean(char *str);
double meansquare(char *str);
void gaussian(char *str, int len);
void summerofuni(char *str,char *str1);
void sumofuni(char *tri,int len);
void equiprobable(char *str,int len);
int signum(double a);
void combo(char *str,int len);
void gausquare(char *str,int len);
//end declaration

//uniform func generator
void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}

//mean calculator function
double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}

//function to calculate mean of squared numbers

double meansquare(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Squaring and adding numbers in file
temp = temp+x*x;
}
fclose(fp);
temp = temp/(i-1);
return temp;
}

//guassian ditribution generator

void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//Function to generate the sum of two uniform distributions
void sumofuni(char *tri,int len)
{
int i;
double x,y;
FILE *fp,*fp2,*destinyfile;
//get two uniform distributions 
uniform("uni1.dat",len);
uniform("uni2.dat",len);
//open the two files
fp = fopen("uni1.dat","r");
fp2=fopen("uni2.dat","r");
destinyfile=fopen(tri,"w");
//Generate numbers
while(fscanf(fp,"%lf",&x)!=EOF)
{
fscanf(fp2,"%lf",&y);
fprintf(destinyfile,"%lf\n",(double)(x+y));
}
fclose(fp);
fclose(fp2);
fclose(destinyfile);
remove("uni1.dat");
remove("uni2.dat");
}

int signum(double a)
{
    if(a>=0)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}
//Function to generate equiprobable distribution belongs to {-1,1}
void equiprobable(char *str,int len)
{
    int i;
    FILE *fp;
    fp=fopen(str,"w");
    for (i = 0; i < len; i++)
    {
    fprintf(fp,"%d\n",signum(2*(double)rand()/(double)RAND_MAX - 1));
    }
    fclose(fp);
}
void combo(char *str,int len)
{
int i,j,equi;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
equi=signum(2*(double)rand()/(double)RAND_MAX - 1);
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",5*equi+temp);
}
fclose(fp);
}
void gausquare(char *str,int len)
{
FILE *fp,*gau1,*gau2;
int i;
double f1,f2;
gaussian("gau1.dat",len);
gaussian("gau2.dat",len);
gau1=fopen("gau1.dat","r");
gau2=fopen("gau2.dat","r");
fp=fopen(str,"w");
for(i=0;i<len;i++)
{
  fscanf(gau1,"%lf",&f1);
  fscanf(gau2,"%lf",&f2);
  fprintf(fp,"%lf\n",f1*f1+f2*f2);
}
fclose(fp);
fclose(gau1);
fclose(gau2);
remove("gau1.dat");
remove("gau2.dat");
}

