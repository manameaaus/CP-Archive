#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> names(n);
    map<string, pair<int, string>> dict;
    set<pair <int,string>> s;
    
    for (int i = 0; i < n; ++i) {
        cin >> names[i];
    }

    for (int i = 0; i < n; ++i) {
        auto it = dict.find(names[i]);
        if (it != dict.end()) {
            s.erase(it->second);
        }
        s.insert({-1 * (i+1),names[i]});
        dict[names[i]] = {-1 * (i+1), names[i]}; 
    }
    for(auto it: s)
        cout << it.second << endl;

    return 0;
}
