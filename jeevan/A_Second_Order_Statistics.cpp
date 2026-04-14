#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    set<int> a;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x; 
        a.insert(x);
    }
    auto it = a.begin();
    it++;
    if (it == a.end()){cout << "NO" << endl;}
    else{cout << *it << endl;};
      
}