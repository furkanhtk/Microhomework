int sum(int num1, int num2) 
{
   return num1 + num2; 
}
int subtract(int num4, int num5) 
{
   return num4 - num5 ; 
}
int multiple(int num4, int num5) 
{
   return num4 * num5 ; 
}

int func_and(int num4, int num5) 
{
   return num4 && num5 ; 
}

int func_or(int num4, int num5) 
{
   return num4 || num5 ; 
}

int main () {
    int output;
    int output2;
    int output3;
    int output4;
    int output5;
	output = sum(1, 2);
	output2 = subtract(3,4);
	output3 = multiple(5,6);
	output4 = func_and(10, 20);
    output5 = func_or(10, 20);
}
