#include <iostream>

using namespace std;

int divisors (int n)
{
  int divisors = 2;

  for (int i = 2; i < n; i++)
  {
    
    if (n % i == 0)
    {
      divisors++;
    }
  }

  
  return divisors;
}

int main() {

  int addnum = 10;
  int num = 55;

  /*
  while (num < 100000000000)
  {
    addnum++;
    num = num + addnum; 
    cout << num << endl;
  }*/

  cout << endl;
  cout << "begin while loop" << endl;

  while (divisors(num) <= 500)
  { 
    addnum++;
    num = num + addnum;
    cout << num << endl;
  }

  cout << endl;

  cout << num << endl;      

}