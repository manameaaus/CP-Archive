#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> sock(2*n);
    for (int i = 0;i < 2*n;i++){
        cin >> sock[i];
    }
    int count = 0;
    int maxa = 0;
    set<int> temp;
    for (int i = 0;i < 2*n;i++){
        if (temp.find(sock[i]) == temp.end()){
            temp.insert(sock[i]);
            count++;
        } else{ count--;}
        if (count > maxa) {maxa = count;}
        
    }
    if (count > maxa) {maxa = count;}
    cout << maxa << endl;
}