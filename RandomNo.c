#include<stdio.h>
#include<time.h>
int main()
{
int num;
time_t sec;
sec=time(NULL);
printf("Enter The Number:\n");
scanf("%d",&num);
if(num>0)
{
for(;;)
{
sec=sec%23412;
if(num>=sec)
{
printf("%ld\n",sec);
break;
}
sec=sec%num;
}
}
else
{
printf("Please Enter Positive Value:\n\n\n");
}
return 0;
}
