#include <bits/stdc++.h>
using namespace std;

int main(){
    int x,maxa,sum,xxy;
    vector< vector<int> > mat;

    maxa = -1e9;
    for (int i = 0; i < 5; i++){
        vector<int> ne;
        for (int j = 0; j < 5; j++){
            cin >> x;
            ne.push_back(x);
        }
        mat.push_back(ne);
    }

    vector<int> raw;
    for (int i = 0; i < 5; i++){
        raw.push_back(i);
    }

    do {
        sum = 0;
        xxy = mat[raw[0]][raw[1]] + mat[raw[1]][raw[0]] + mat[raw[2]][raw[1]] + mat[raw[1]][raw[2]] + 2 * (mat[raw[2]][raw[3]] + mat[raw[3]][raw[2]] + mat[raw[3]][raw[4]] + mat[raw[4]][raw[3]]);
        maxa = max(maxa,xxy);
    }
    while (next_permutation(raw.begin(), raw.end()));
    cout << maxa;

}

// (g23 + g32 + g15 + g51) + (g13 + g31 + g54 + g45) + (g15 + g51) + (g54 + g45) = 32
// 23154