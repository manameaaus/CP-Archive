#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n,maxa,x;
    cin >> n;
    maxa = -1e9;
    

    for (int i = 0; i < n; i++){ 
        cin >> x;  
        maxa = max(maxa , x);
    }
    cout << maxa << endl;
}