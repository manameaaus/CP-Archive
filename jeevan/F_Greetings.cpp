#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

#define int long long

// ordered_set: supports order_of_key() and find_by_order()
template <typename T>
using ordered_set = tree<
    T, 
    null_type, 
    less<T>, 
    rb_tree_tag, 
    tree_order_statistics_node_update
>;


void solve() {
    int n;cin >> n;

    vector<array<int , 2>> dabba;

    for (int i = 0;i < n;i++){
        int a,b;cin >> a >> b;
        dabba.push_back({-a,b});
    }


    sort(dabba.begin(),dabba.end());

    ordered_set<int> s;
    int ans = 0;

    for(auto [a,b] : dabba) {
        ans += s.order_of_key(b);
        s.insert(b);
    }


    cout << ans << endl;
}

int32_t main() {
    // ordered_set<int> s;

    // s.insert(10);
    // s.insert(1);
    // s.insert(5);

    // // Elements are automatically sorted: {1, 5, 10}

    // // --- find_by_order(k) ---
    // // returns iterator to k-th smallest element (0-indexed)
    // cout << *s.find_by_order(0) << "\n"; // 1
    // cout << *s.find_by_order(1) << "\n"; // 5
    // cout << *s.find_by_order(2) << "\n"; // 10

    // // --- order_of_key(x) ---
    // // returns number of elements strictly less than x
    // cout << s.order_of_key(5) << "\n"; // 1
    // cout << s.order_of_key(7) << "\n"; // 2
    // cout << s.order_of_key(10) << "\n"; // 2

    // // Deleting element
    // s.erase(5);

    // cout << "After erase: ";
    // for (auto x : s) cout << x << " "; // 1 10
    // cout << "\n";


    ios_base::sync_with_stdio(false);cin.tie(NULL);
    int t;cin >> t;
    while(t--){
        solve();
    }
    return 0;
}