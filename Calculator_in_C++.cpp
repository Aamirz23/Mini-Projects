#include<iostream>
using namespace std;
int main() {
   char operation;
   float a,b;
   
   cout<<"Enter the Operation you want to perform (+ , - , * , /): ";
   cin>> operation;
   switch (operation)
   {
      
      case '+' :
         float sum;
         cout<<"Enter two numbers: "<<endl;
         cin>>a>>b;
         sum = a + b;
         cout<<"Sum of two numbers is: "<<sum<<endl;
         break;
   
      case '-':
         float diff;
         cout<<"Enter two numbers: "<<endl;
         cin>>a>>b;
         diff = a - b;
         cout<<"Difference is: "<<diff<<endl;
         break; 
   
      case '*':
         float prod;
         cout<<"Enter two numbers: "<<endl;
         cin>>a>>b;
         prod = a * b;
         cout<<"Product is: "<<prod<<endl;
         break;
   
   case '/':
         float division;
         cout<<"Enter two numbers: "<<endl;
         cin>>a>>b;
         if(b == 0) {
            cout<<"You can't divide by zero bro!"<<endl;
         }
         else{
            division = a/b;
         cout<<"Division is: "<< division <<endl;
         }
         break;
      
      default:
      
      break;
   }
   return 0;
   }

