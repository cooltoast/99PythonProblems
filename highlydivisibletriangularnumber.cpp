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
  int num = 55 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22;

  cout << endl;

  while (divisors(num) <= 500)
  { 
    addnum++;
    num = num + addnum;
  }

  

  cout << num << endl;      

}