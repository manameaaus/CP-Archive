#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    vector<long long> v(21);
    v[0] = 1;;

    for (int i = 1 ; i < 21 ; i++){
        v[i] = v[i-1] * i;
    }

    while(t--){
        int n;
        cin >> n;
        cout << v[n] << endl;
        
    }
}