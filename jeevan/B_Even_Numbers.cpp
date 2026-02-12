#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    for (int i = 2; i < n+1; i+=2){
        cout << i << endl;
    }
    if (n == 1){
        cout << -1 << endl;
    }
}