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
#define JBR_CP_1000101 ios_base::sync_with_stdio(false);cin.tie(NULL);

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
#define invs(v, n) vs v(n); rep(i, n) cin >> v[i]
#define rdvi(v) for (auto &x : v) cin >> x
#define rdvs(v) for (auto &s : v) cin >> s
#define msb(x) (x == 0 ? -1 : 1ll<<(63 - __builtin_clzll(x)))      
#define lsb(x) (x == 0 ? -1 : 1ll<<(__builtin_ctzll(x)))   
#define pc(x) (__builtin_popcountll(x))
string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}

// const int N = 100000;
// int arr[N]; 
// vector<int> seg[4*N];
// const int neutral = 0;

const int N = 10;
// const int N = 100000;
int arr[N]; 
vector<int> seg[4 * N];   // Segment tree storing vectors at each node
bool valid[4 * N];        // Boolean array to track validity at each node

int combine(int a, int b) {
    return a+b;
}

void build(int node, int st, int nd) {
    if (st == nd) {
        seg[node] = {arr[st]};
        valid[node] = true;
        return;
    }

    int mid = (st + nd) / 2;
    build(2 * node, st, mid);
    build(2 * node + 1, mid + 1, nd);

    vector<int>& left = seg[2 * node];
    vector<int>& right = seg[2 * node + 1];

    seg[node] = left;
    seg[node].insert(seg[node].end(), right.begin(), right.end());

    // Step 1: If any child is invalid → parent invalid
    if (!valid[2 * node] || !valid[2 * node + 1]) {
        valid[node] = false;
        return;
    }

    // Step 2: Check if left.back() < right.front()
    if (left.back() < right.front()) {
        valid[node] = true;
        return;
    }

    // Step 3: Check relaxed condition
    bool cond1 = (left.size() >= 2 && right.size() >= 1) ? (left[left.size() - 2] < right[0]) : false;
    bool cond2 = (right.size() >= 2 && left.size() >= 1) ? (right[1] > left.back()) : false;

    if (cond1 && cond2) {
        valid[node] = true;
    } else {
        valid[node] = false;
    }
}


// void update(int node, int st, int nd, int idx, int val) {
//     if (st == nd) {
//         arr[idx] = val;
//         seg[node] = arr[idx];
//         return;
//     }

//     int mid = (st+nd)/2;
//     if (idx <= mid) update(2*node, st, mid, idx, val);
//     else update(2*node+1, mid+1, nd, idx, val);
//     seg[node] = combine(seg[2*node], seg[2*node+1]);
// }   

// int query(int node, int st, int nd, int L, int R) {
//     if (L <= st and nd <= R) return seg[node];
//     if (R < st or L > nd) return neutral;

//     int mid = (st+nd)/2;
//     int qL = query(2*node, st, mid, L, R);
//     int qR = query(2*node+1, mid+1, nd, L, R);
//     return combine(qL, qR);
// }

void solve() {
    int n,q;
    cin >> n >> q;

    // invi(v,n);

    // print(n);

    for (int i = 1;i < n+1;i++){
        cin >> arr[i];
    }
    build(1,1,n);
    // print(arr);
    print2(seg);
    print1(valid);
    // print1(seg[1]);




}

int32_t main(){
    // cout << fixed << setprecision(10);
    JBR_CP_1000101
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}