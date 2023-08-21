#include <iostream>
#include <cmath>
using namespace std;
double total;
double myFunction(int n);
double myFunction();
int main() {
    int n;
    cout<<"Enter one number :"<<endl;
    cin>>n;
    cout<<"Result = "<<myFunction(n)<<endl;
    cout<<myFunction();
    return 0;
}

double myFunction(int n){
    if (n==0){
        return total;
    }
    else {
        int sqrt= pow(-1,n+1);
        total += ((double)sqrt/n);
        myFunction(n - 1);
    }
}

double myFunction(){
    int n;
    cout << "Enter one number :" << endl;
    cin >> n;
    while (n!=0){
        int sqrt= pow(-1,n+1);
        total += ((double)sqrt/n);
        n--;
    }
    cout<<"Result.."<<endl;
    return total;
}
