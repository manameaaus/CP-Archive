#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    map<string,int> m;
    while(t--){
        string s;
        cin >> s;
        if (m.find(s) == m.end()){
            m[s] = 1;
            cout << "OK" << endl;
        } else{
            cout << s << m[s] << endl;
            m[s]++;
        }
    }
}