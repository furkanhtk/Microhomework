#include<stdio.h>
#include<stdlib.h>

int main()
{
	int x;//x today//
	
	printf("Monday=1\nTuesday=2\nWednesday=3\nThursday=4\nFriday=5\nSaturday=6\nSunday=7\n");
	printf("Please enter the day : ");
	scanf("%d",&x);
	switch(x){
		case 1 : 
			printf("Today there is no C course\n");
				break;
		case 2 :
			printf("Today there is no C course\n");
				break;
		case 3 :
			printf("Today there is no C course\n");
				break;
		case 4 :
			printf("Today there is  C course\n");
				break;		
		case 5 :
			printf("Today there is  C course\n");
				break;
		case 6 :
			printf("Today there is no C course\n");
				break;
		case 7 :
			printf("Today there is no C course\n");
				break;				
		default : 	
			printf("Please enter a defined number\n");	
	}
}
	
	
	
	



