// #include <bits/stdc++.h>
// using namespace std;

// // ---------- debug utilities ----------
// template<typename... Args>

// // ---------- shortcut macros ----------
// #define all(a) (a).begin(), (a).end()
// #define rall(a) (a).rbegin(), (a).rend()
// #define len(x) (int)(x).size()
// #define pb push_back
// #define print1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
// #define print2(zzz) for (auto &zzzzz : zzz) {print1(zzzzz)}
// #define space cout << endl;
// #define sum(v) (accumulate((v).begin(), (v).end(), 0LL))
// #define JBR_CP_1000101 ios_base::sync_with_stdio(false);cin.tie(NULL);

// #define rep(i, n) for (int i = 0; i < (n); ++i)
// #define rep1(i, a, b) for (int i = (a); i <= (b); ++i)
// #define per(i, n) for (int i = (n) - 1; i >= 0; --i)
// #define per1(i, a, b) for (int i = (b); i >= (a); --i)
// void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

// // ----------- constants -----------
// #define PI 3.14159265358979323846
// #define INF 1e18
// #define MOD 1000000007
// #define MOD2 998244353

// // ---------- type aliases ----------
// #define ll long long
// #define int long long
// #define vi vector<int> 
// #define vc vector<char> 
// #define vs vector<string> 
// #define vvc vector<vector<char>> 
// #define vvi vector<vector<int>> 
// #define pii pair<int, int> 

// // ---------- input macros ----------
// #define invi(v, n) vi v(n); rep(i, n) cin >> v[i]
// #define invs(v, n) vs v(n); rep(i, n) cin >> v[i]
// #define rdvi(v) for (auto &x : v) cin >> x
// #define rdvs(v) for (auto &s : v) cin >> s
// #define msb(x) (x == 0 ? -1 : 1ll<<(63 - __builtin_clzll(x)))      
// #define lsb(x) (x == 0 ? -1 : 1ll<<(__builtin_ctzll(x)))   
// #define pc(x) (__builtin_popcountll(x))
// string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}



// void solve() {
//     int n,q;
//     cin >> n >> q;

//     invi(v,n);

//     int b = sqrt(n);
//     // vector<vector<int>> block((n + b - 1) / b);
//     vector<multiset<int>> block((n + b - 1) / b);

//     for (int i = 0; i < n; i++) {
//         block[i / b].insert(v[i]);
//     }

//     // print2(block);

//     for(int i = 0;i < q;i++){
//         char c;cin >>c;

//         // if(c == '!'){
//         //     int ind,val;
//         //     cin >> ind >> val;

//         //     ind--;

//         //     int old = v[ind];

//         //     int idx = lower_bound(all(block[ind/b]),old) - block[ind/b].begin();
//         //     block[ind/b][idx] = val;
//         //     // sort(all(block[ind/b]));

            
//         //     v[ind] = val;
//         // }
//         if(c == '!'){
//             int ind, val;
//             cin >> ind >> val;
//             ind--;

//             int old = v[ind];
//             int block_idx = ind / b;
//             block[block_idx].erase(block[block_idx].find(old));
//             block[block_idx].insert(val);
//             v[ind] = val;
//         }else{
//             int a,bi;cin >> a >> bi;
//             int kkk = 0;
//             for (auto& blk : block) {
//                 kkk += distance(blk.lower_bound(a), blk.upper_bound(bi));
//             }
//             cout << kkk << '\n';
//         }   
//     }


//     // vi pok = {1,2,2,2,4,4,5,5,7,7};
//     // print(upper_bound(all(pok),2) - lower_bound(all(pok),2));



// }

// int32_t main(){
//     // cout << fixed << setprecision(10);
//     JBR_CP_1000101
//     int t = 1;
//     // cin >> t;
//     while (t--) {
//         solve();
//     }

//     return 0;
// }



#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

template<typename T>
using ordered_multiset = tree<
    T, null_type, less<T>,
    rb_tree_tag, tree_order_statistics_node_update>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q; 
    cin >> n >> q;
    vector<int> v(n);
    for (int &x : v) cin >> x;

    ordered_multiset<pair<int,int>> os; 
    // store pairs (value, index) to handle duplicates uniquely

    for (int i = 0; i < n; i++) {
        os.insert({v[i], i});
    }

    while (q--) {
        char c; cin >> c;
        if (c == '!') {
            int ind, val; cin >> ind >> val;
            ind--;

            os.erase({v[ind], ind});
            v[ind] = val;
            os.insert({val, ind});
        } else {
            int a, b; cin >> a >> b;
            // number of elements in [a, b] = order_of_key({b+1, -inf}) - order_of_key({a, -inf})
            int cnt = os.order_of_key({b+1, -1e9}) - os.order_of_key({a, -1e9});
            cout << cnt << '\n';
        }
    }

    return 0;
}
