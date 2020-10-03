// area of rectangle by user input
# include <stdio.h>

void main(){
	
	float a;
	float b;
	float area;
	
	printf("enter length : ");
	scanf("%f",&a);
	
	printf("enter breadth : ");
	scanf("%f",&b);
	
	area  =  a * b;
	
	printf("The are of rectangle is %f cm2",area);
}
