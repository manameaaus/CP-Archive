// // #include <bits/stdc++.h>
// // using namespace std;

// // // ---------- debug utilities ----------
// // template<typename... Args>

// // // ---------- shortcut macros ----------
// // #define all(a) (a).begin(), (a).end()
// // #define rall(a) (a).rbegin(), (a).rend()
// // #define len(x) (int)(x).size()
// // #define pb push_back
// // #define print1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
// // #define print2(zzz) for (auto &zzzzz : zzz) {print1(zzzzz)}
// // #define space cout << endl;
// // #define sum(v) (accumulate((v).begin(), (v).end(), 0LL))
// // #define execute ios_base::sync_with_stdio(false);cin.tie(NULL);

// // #define rep(i, n) for (int i = 0; i < (n); ++i)
// // #define rep1(i, a, b) for (int i = (a); i <= (b); ++i)
// // #define per(i, n) for (int i = (n) - 1; i >= 0; --i)
// // #define per1(i, a, b) for (int i = (b); i >= (a); --i)
// // void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

// // // ----------- constants -----------
// // #define PI 3.14159265358979323846
// // #define INF 1e18
// // #define MOD 1000000007
// // #define MOD2 998244353

// // // ---------- type aliases ----------
// // #define ll long long
// // #define int long long
// // #define vi vector<int> 
// // #define vc vector<char> 
// // #define vs vector<string> 
// // #define vvc vector<vector<char>> 
// // #define vvi vector<vector<int>> 
// // #define pii pair<int, int> 

// // // ---------- input macros ----------
// // #define invi(v, n) vi v(n); rep(i, n) cin >> v[i]
// // #define invs(v, n) vs> v(n); rep(i, n) cin >> v[i]
// // #define rdvi(v) for (auto &x : v) cin >> x
// // #define rdvs(v) for (auto &s : v) cin >> s
// // #define msb(x) (x == 0 ? -1 : 1<<(63 - __builtin_clzll(x)))      
// // #define lsb(x) (x == 0 ? -1 : 1<<(__builtin_ctzll(x)))   
// // #define pc(x) (__builtin_popcountll(x))
// // string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}





// // class SegmentTree {
// // private:
// //     int n;
// //     vector<vector<int>> tree; 
// //     vector<int> xr;           
// //     vector<int> &arr;         

// //     void mergeNode(int node) {
// //         int l = 2 * node;
// //         int r = 2 * node + 1;

// //         if (xr[l] >= xr[r]) {
// //             tree[node] = tree[l];
// //             tree[node].insert(
// //                 tree[node].end(),
// //                 tree[r].begin(),
// //                 tree[r].end()
// //             );
// //         } else {
// //             tree[node] = tree[r];
// //             tree[node].insert(
// //                 tree[node].end(),
// //                 tree[l].begin(),
// //                 tree[l].end()
// //             );
// //         }

// //         xr[node] = xr[l] ^ xr[r];
// //     }

// //     void build(int node, int start, int end) {
// //         if (start == end) {
// //             tree[node] = {start};   // store index
// //             xr[node] = arr[start];  // XOR uses value
// //         } else {
// //             int mid = (start + end) / 2;
// //             build(2 * node, start, mid);
// //             build(2 * node + 1, mid + 1, end);
// //             mergeNode(node);
// //         }
// //     }

// //     void update(int node, int start, int end, int idx, int val) {
// //         if (start == end) {
// //             arr[idx] = val;
// //             tree[node] = {idx};
// //             xr[node] = val;
// //         } else {
// //             int mid = (start + end) / 2;
// //             if (idx <= mid)
// //                 update(2 * node, start, mid, idx, val);
// //             else
// //                 update(2 * node + 1, mid + 1, end, idx, val);

// //             mergeNode(node);
// //         }
// //     }

// // public:
// //     SegmentTree(vector<int>& a) : arr(a) {
// //         n = arr.size();
// //         tree.resize(4 * n);
// //         xr.resize(4 * n);
// //         build(1, 0, n - 1);
// //     }

// //     void update(int idx, int val) {
// //         update(1, 0, n - 1, idx, val);
// //     }

// //     int getIndexInRoot(int target) const {
// //         const vector<int>& v = tree[1];
// //         for (int i = 0; i < (int)v.size(); i++) {
// //             if (v[i] == target)
// //                 return i;
// //         }
// //         return -1; 
// //     }

// //     int getRootXor() const {
// //         return xr[1];
// //     }
// // };



// // void solve() {
// //     int n,q;
// //     cin >> n >> q;
// //     vector<int> cows(1 << n);
// //     for(int i = 0;i < (1 << n);i++){
// //         cin >> cows[i];
// //     }
// //     // print1(cows);
// //     SegmentTree st(cows);

// //     for(int i = 0;i < q;i++){
// //         int b,c,old;cin >> b >> c;
// //         b--;
// //         old = cows[b];
// //         st.update(b,c);
// //         cout << st.getIndexInRoot(b) << endl;
// //         st.update(b,old);
// //         // print1(cows);
// //     }
// // }

// // int32_t main(){
// //     // cout << fixed << setprecision(10);
// //     execute
// //     int t = 1;
// //     cin >> t;
// //     while (t--) {
// //         solve();
// //     }

// //     return 0;
// // }




// #include <bits/stdc++.h>
// using namespace std;

// #define int long long
// #define execute ios::sync_with_stdio(false); cin.tie(nullptr);

// struct SegmentTree {
//     int N;
//     vector<int> xr;

//     SegmentTree(const vector<int>& a) {
//         N = a.size();
//         xr.assign(4 * N, 0);
//         build(1, 0, N - 1, a);
//     }

//     void build(int node, int l, int r, const vector<int>& a) {
//         if (l == r) {
//             xr[node] = a[l];
//             return;
//         }
//         int mid = (l + r) >> 1;
//         build(node << 1, l, mid, a);
//         build(node << 1 | 1, mid + 1, r, a);
//         xr[node] = xr[node << 1] ^ xr[node << 1 | 1];
//     }

//     void update(int node, int l, int r, int idx, int val) {
//         if (l == r) {
//             xr[node] = val;
//             return;
//         }
//         int mid = (l + r) >> 1;
//         if (idx <= mid)
//             update(node << 1, l, mid, idx, val);
//         else
//             update(node << 1 | 1, mid + 1, r, idx, val);
//         xr[node] = xr[node << 1] ^ xr[node << 1 | 1];
//     }

//     void update(int idx, int val) {
//         update(1, 0, N - 1, idx, val);
//     }


//     int getPosition(int idx) {
//         int pos = 0;
//         int node = 1;
//         int l = 0, r = N - 1;

//         while (l < r) {
//             int mid = (l + r) >> 1;
//             int left = node << 1;
//             int right = left | 1;

//             bool inLeft = (idx <= mid);

//             if (xr[left] >= xr[right]) {
//                 if (!inLeft)
//                     pos += (mid - l + 1);
//             } else {
//                 if (inLeft)
//                     pos += (r - mid);
//             }

//             if (inLeft) {
//                 node = left;
//                 r = mid;
//             } else {
//                 node = right;
//                 l = mid + 1;
//             }
//         }
//         return pos;
//     }
// };

// void solve() {
//     int n, q;
//     cin >> n >> q;
//     int N = 1 << n;

//     vector<int> cows(N);
//     for (int i = 0; i < N; i++)
//         cin >> cows[i];

//     SegmentTree st(cows);

//     while (q--) {
//         int b, c;
//         cin >> b >> c;
//         --b;

//         int old = cows[b];
//         cows[b] = c;
//         st.update(b, c);

//         cout << st.getPosition(b) << '\n';

//         cows[b] = old;
//         st.update(b, old);
//     }
// }

// int32_t main() {
//     execute
//     int t;
//     cin >> t;
//     while (t--) solve();
//     return 0;
// }



#include <bits/stdc++.h>
using namespace std;

// ---------- debug utilities ----------
template<typename... Args>

// ---------- shortcut macros ----------
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define len(x) (int)(x).size()
#define pb push_back
#define print1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
#define print2(zzz) for (auto &zzzzz : zzz) {print1(zzzzz)}
#define space cout << endl;
#define sum(v) (accumulate((v).begin(), (v).end(), 0LL))
#define execute ios_base::sync_with_stdio(false);cin.tie(NULL);

#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, a, b) for (int i = (a); i <= (b); ++i)
#define per(i, n) for (int i = (n) - 1; i >= 0; --i)
#define per1(i, a, b) for (int i = (b); i >= (a); --i)
void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

// ----------- constants -----------
#define PI 3.14159265358979323846
#define INF 1e18
#define MOD 1000000007
#define MOD2 998244353

// ---------- type aliases ----------
#define ll long long
#define int long long
#define vi vector<int> 
#define vc vector<char> 
#define vs vector<string> 
#define vvc vector<vector<char>> 
#define vvi vector<vector<int>> 
#define pii pair<int, int> 

// ---------- input macros ----------
#define invi(v, n) vi v(n); rep(i, n) cin >> v[i]
#define invs(v, n) vs> v(n); rep(i, n) cin >> v[i]
#define rdvi(v) for (auto &x : v) cin >> x
#define rdvs(v) for (auto &s : v) cin >> s
#define msb(x) (x == 0 ? -1 : 1<<(63 - __builtin_clzll(x)))      
#define lsb(x) (x == 0 ? -1 : 1<<(__builtin_ctzll(x)))   
#define pc(x) (__builtin_popcountll(x))
string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}

struct SegmentTree {
    int N;
    vector<int> xr;

    SegmentTree(const vector<int>& a) {
        N = a.size();
        xr.assign(4 * N, 0);
        build(1, 0, N - 1, a);
    }

    void build(int node, int l, int r, const vector<int>& a) {
        if (l == r) {
            xr[node] = a[l];
            return;
        }
        int mid = (l + r) >> 1;
        build(node << 1, l, mid, a);
        build(node << 1 | 1, mid + 1, r, a);
        xr[node] = xr[node << 1] ^ xr[node << 1 | 1];
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            xr[node] = val;
            return;
        }
        int mid = (l + r) >> 1;
        if (idx <= mid)
            update(node << 1, l, mid, idx, val);
        else
            update(node << 1 | 1, mid + 1, r, idx, val);
        xr[node] = xr[node << 1] ^ xr[node << 1 | 1];
    }

    void update(int idx, int val) {
        update(1, 0, N - 1, idx, val);
    }


    int getPosition(int idx) {
        int pos = 0;
        int node = 1;
        int l = 0, r = N - 1;

        while (l < r) {
            int mid = (l + r) >> 1;
            int left = node << 1;
            int right = left | 1;

            bool inLeft = (idx <= mid);

            if (xr[left] >= xr[right]) {
                if (!inLeft)
                    pos += (mid - l + 1);
            } else {
                if (inLeft)
                    pos += (r - mid);
            }

            if (inLeft) {
                node = left;
                r = mid;
            } else {
                node = right;
                l = mid + 1;
            }
        }
        return pos;
    }
};

void solve() {
    int n, q;
    cin >> n >> q;
    int N = 1 << n;

    vector<int> cows(N);
    for (int i = 0; i < N; i++)
        cin >> cows[i];

    SegmentTree st(cows);

    while (q--) {
        int b, c;
        cin >> b >> c;
        --b;

        int old = cows[b];
        cows[b] = c;
        st.update(b, c);

        cout << st.getPosition(b) << '\n';

        cows[b] = old;
        st.update(b, old);
    }
}

int32_t main() {
    execute
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
