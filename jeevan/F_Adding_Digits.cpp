#include <iostream>
using namespace std;

int main() {
    long long x, b, n, a,flag=0;
    cin >> x >> b >> n;
    a = x*10;
    for (long long  i = 0; i < 10; i++) {
        if ((a+i) % b == 0) {
            x = a+i;
            flag =1;
        }
    }
    if (flag==0) {
        cout << -1 << endl;
    }
    if(flag==1){
        cout << x;
        for (int i=1;i<n;i++){
            cout << 0;
        }
    }
}
