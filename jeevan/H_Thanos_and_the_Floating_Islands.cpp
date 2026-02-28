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


ll mod_mul(ll a,ll b) {return ((a % MOD) * (b % MOD)) % MOD;}
ll mod_add(ll a,ll b) {return ((a % MOD) + (b % MOD)) % MOD;}
ll mod_sub(ll a,ll b) {return ((a % MOD) - (b % MOD) + MOD) % MOD;}
ll mod_pow(ll a,ll b, ll m = MOD) {ll res = 1;a %= m;while (b) {if (b & 1ll) res = res * a % m;a = mod_mul(a, a);b >>= 1ll;}return res;}
ll mod_inv(ll a, ll m = MOD) {return mod_pow(a, m - 2, m);}  // fermat's little theorem
ll mod_div(ll a, ll b) {return mod_mul(a, mod_inv(b));}


const int MAXN = 200005;
int factorials[MAXN];
void fac(){
    factorials[0] = 1,factorials[1] = 1;
    for (int i = 2;i < MAXN;i++){
        factorials[i] = mod_mul(factorials[i-1],i);
    }
}

int nck(int n,int k){
    if (n < k) return 0;
    return mod_div(factorials[n],mod_mul(factorials[k],factorials[n-k]));
}

void solve() {
    int n,k; cin >> n >> k;
    vvi adj(n+1);
    for (int i = 0;i < n - 1;i++){
        int u,v;cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    if (k == 1){
        cout << 1 << endl;
        return;
    }
    

    // print1(adj[1]);

    int xyz = 0;
    int tot = nck(n,k);

    function<int(int,int)> dfs = [&](int node,int par) -> int{
        int desendants = 0;
        for(int cld : adj[node]){
            if (cld != par) {
                int ppp = dfs(cld,node);
                xyz = mod_add(xyz,mod_mul(desendants,ppp));
                desendants += ppp;
            }
        }
        xyz = mod_add(xyz,mod_mul(desendants,n-desendants-1));
        desendants += 1;
        xyz = mod_add(xyz,n-1);
        return desendants;
    };


    function<int(int,int)> dfs1 = [&](int node,int par) -> int{

        // cout << node << " hhh" << endl;
        int desendants = 0;
        int two_pair = 0;

        vi tp;
        vi thrr;
        for(int cld : adj[node]){
            if (cld != par) {
                // cout << node << " " << cld << 
                int ppp = dfs1(cld,node);
                // xyz = mod_add(xyz,nck(ppp,k));
                xyz = mod_add(xyz,mod_mul(ppp,two_pair));
                xyz = mod_add(xyz,mod_mul(desendants,ppp));
                two_pair = mod_add(two_pair,mod_mul(desendants,ppp));
                tp.pb(two_pair);
                thrr.pb(desendants);
                
                desendants += ppp;
            }
        }
        xyz = mod_add(xyz,mod_mul(n - desendants - 1,desendants));
        xyz = mod_add(xyz,mod_mul(n - desendants - 1,two_pair));
        
        desendants += 1; 
        // print(node);
        // print1(tp);
        // print1(thrr);
        // cout << endl;

        return desendants;
    };

    if (k == 2){
        dfs(1,0);
    }else{
        dfs1(1,0);
    }
    cout << mod_mul(xyz,mod_inv(tot)) << endl;
    // cout << xyz << endl;

    // cout << mod_div(157,30) << endl;
    // cout << mod_div(116,120) << endl;
}

int32_t main(){
    // cout << fixed << setprecision(10);
    execute
    int t = 1;
    // cin >> t;
    fac();
    while (t--) {
        solve();
    }

    return 0;
}