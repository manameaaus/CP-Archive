#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

// ---------- Ordered Set Template ----------
template <typename T>
using ordered_set = tree<
    T,
    null_type,
    less<T>,                    // can change to greater<T> for descending order
    rb_tree_tag,
    tree_order_statistics_node_update
>;

/*
    🔹 Functions available:

    - s.insert(x)               → insert element x
    - s.erase(x)                → erase element x
    - *s.find_by_order(k)       → returns iterator to k-th smallest element (0-indexed)
    - s.order_of_key(x)         → returns count of elements < x
    - s.lower_bound(x)          → returns iterator to first element >= x
    - s.upper_bound(x)          → returns iterator to first element > x
*/

int main() {
    ordered_set<int> s;

    s.insert(10);
    s.insert(20);
    s.insert(30);
    s.insert(40);

    cout << *s.find_by_order(0) << "\n";  // 10 (0th smallest)
    cout << *s.find_by_order(2) << "\n";  // 30

    cout << s.order_of_key(25) << "\n";   // 2 (since 10, 20 < 25)
    cout << s.order_of_key(30) << "\n";   // 2

    // Erase element
    s.erase(20);

    cout << "After erase:\n";
    for (auto x : s) cout << x << " ";    // 10 30 40
    cout << "\n";

    return 0;
}