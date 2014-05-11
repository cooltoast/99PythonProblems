#include <iostream>

using namespace std;

bool divisors_500 (int n)
{
  int divisors = 2;

  for (int i = 2; i < n; i++)
  {
    if (n % i == 0)
    {
      divisors++;
    }
  }
  return (divisors > 500);
}

int main() {

  int num = 55;
  int addnum = 10;

  while (num < 100000)
  {
    addnum++;
    num = num + addnum; 
  }

  while (!divisors_500(num))
  { 
    addnum++;
    num = num + addnum;
  }

  cout << num << endl;      

}