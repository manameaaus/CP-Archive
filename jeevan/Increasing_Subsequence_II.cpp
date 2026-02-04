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
ll mod_mul(ll a,ll b) {return ((a % MOD) * (b % MOD)) % MOD;}
ll mod_add(ll a,ll b) {return ((a % MOD) + (b % MOD)) % MOD;}
ll mod_sub(ll a,ll b) {return ((a % MOD) - (b % MOD) + MOD) % MOD;}
ll mod_pow(ll a,ll b, ll m = MOD) {ll res = 1;a %= m;while (b) {if (b & 1ll) res = res * a % m;a = mod_mul(a, a);b >>= 1ll;}return res;}
ll mod_inv(ll a, ll m = MOD) {return mod_pow(a, m - 2, m);}  // fermat's little theorem
ll mod_div(ll a, ll b) {return mod_mul(a, mod_inv(b));}
ll gcd(ll a, ll b) {return b ? gcd(b, a % b) : a;}
ll lcm(ll a, ll b) {return a * b / gcd(a, b);}

const int N = 200005;
int srr[N], seg[4*N];
const int NEUTRAL = 0;

int combine(int a, int b) {
    return mod_add(a,b);
}

void build(int node, int st, int nd) {
    if (st == nd) {
        seg[node] = srr[st];
        return;
    }

    int mid = (st+nd)/2;
    build(2*node, st, mid);
    build(2*node+1, mid+1, nd);
    seg[node] = combine(seg[2*node], seg[2*node+1]);
}

void update(int node, int st, int nd, int idx, int val) {
    if (st == nd) {
        srr[idx] = val;
        seg[node] = srr[idx];
        return;
    }

    int mid = (st+nd)/2;
    if (idx <= mid) update(2*node, st, mid, idx, val);
    else update(2*node+1, mid+1, nd, idx, val);
    seg[node] = combine(seg[2*node], seg[2*node+1]);
}   

int query(int node, int st, int nd, int L, int R) {
    if (L <= st and nd <= R) return seg[node];
    if (R < st or L > nd) return NEUTRAL;

    int mid = (st+nd)/2;
    int qL = query(2*node, st, mid, L, R);
    int qR = query(2*node+1, mid+1, nd, L, R);
    return combine(qL, qR);
}

void solve() {
    int n;
    cin >> n;

    invi(arr,n);

    set<int> ids;
    for(auto ele:arr){
        ids.insert(ele);
    }

    unordered_map<int,int> mp;
    int st = 0;
    for(auto ele:ids){
        st++;
        mp[ele] = st;
    }

    for(int i = 0;i < n;i++){
        arr[i] = mp[arr[i]];
    }

    build(1,1,st);

    for(int i = 0;i < n;i++){
        int num = arr[i];
        int small = query(1,1,st,0,num-1) + 1;
        update(1,1,st,num,srr[num] + small);
    }

    print(seg[1]);

    
}

int32_t main(){
    // cout << fixed << setprecision(10);
    JBR_CP_1000101
    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}