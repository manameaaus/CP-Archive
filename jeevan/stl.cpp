// #include <bits/stdc++.h>
// #include <iostream>
// #include <vector>
// using namespace std;

// int main() {
//     vector <int> v={1,2,3,4};
//     do {
//         for (int i = 0 ; i< v.size(); i++){
//             cout << v[i] << " ";
//         }
//         cout << endl;
//     }
//     while (next_permutation(v.begin(), v.end()));
    
// }

#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n,t,sum,curr,mina,tot;
    cin >> n;

    vector<int> v(n);
    mina = pow(10,9);
    tot = 0;

    for (int i = 0; i < n; i++){
        cin >> v[i];
        tot += v[i];
    }
    for (int i = 0; i<pow(2,n)-1 ; i++){
        t = i;
        curr = n-1;
        sum = 0;
        while (curr >= 0){            
            if (t%2 == 1){
                sum += v[curr];
            }
            t = t >> 1;
            curr --;
        }
        mina = min(mina, abs(tot - (2 * sum)));   
    }
    cout << mina << endl;
}
