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
	output = func_and(10, 20);
    output = func_or(10, 20);

}
