#include <iostream>
using namespace std;

int add(int a, int b) {
      return a + b;
}

int main() {
   int a = 0;
   int b = 0;
   int c = a + b;
   
   cout << add(1, 2) << endl;
   cout << "T" << endl; 
   return 0;
}
