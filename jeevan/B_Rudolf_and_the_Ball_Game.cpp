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

int dp[1001][1001],ans[1001];
void solve() {
    int n,m,x; cin >> n >> m >> x;
    vector<int> dist(m);
    vector<char> ops(m);
    for(int i = 0;i < m;i++){
        cin >> dist[i] >> ops[i]; 
    }
    for(int i = 0;i <= m;i++){
        for (int j = 0;j <= n;j++){
            dp[i][j] = 0;
            ans[j] = 0;
        }   
    }
    

    function<void(int,int)> run = [&](int val, int player) {
        // print(val,player,ops[val]);
        if (val == m){
            ans[player] = 1;
            return;
        }
        if (dp[val][player] != 0){
            return;
        }
        if (ops[val] == '?'){
            run(val+1,(player + dist[val]) % n);
            run(val+1,(player - dist[val] + n) % n);
        }else{
            if (ops[val] == '0'){
                run(val+1,(player + dist[val]) % n);
            }else{
                run(val+1,(player - dist[val] + n) % n);
            }
        }

        dp[val][player] = 1;
    };
    run(0,x);
    int c = 0;
    vector<int> res;
    for (int i = 1;i <= n;i++){
        if (ans[i%n]){
            c++;
            res.pb(i);
        }
    }

    print(c);
    print1(res);


    // for(int i = 0;i <= m;i++){
    //     for (int j = 0;j <= n;j++){
    //         dp[i][j] = 0;
    //         ans[j] = 0;
    //     }   
    // }



    // auto run = [&](int throwVal, int player) -> void {
    //     if (throwVal == m){
    //         ans[player] = 1;
    //         return;
    //     }
        
    //     if (dp[throwVal][player] != 0){
    //         return;
    //     }
    // };

};


int32_t main(){
    // cout << fixed << setprecision(10);
    execute
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}