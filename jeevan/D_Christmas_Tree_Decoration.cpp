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
#define MOD 998244353
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


int perm[51];
void calc(){
    perm[1] = 1;
    for (int i = 2;i <= 50;i++){
        perm[i] = mod_mul(perm[i-1] , i);
    }
}

void solve() {
    int n;cin >> n;
    vector<int> v(n+1);
    int suma = 0;
    int maxa = 0;
    for(int i = 0;i <= n;i++){
        cin >> v[i];
        suma += v[i];
        if (i > 0){
            maxa = max(maxa,v[i]);
        }
    }

    if (suma >= n * maxa){
        cout << perm[n] << endl;
        return;
    }

    int in_hand = v[0];
    int ccc = 0;
    for (int i = 1;i <= n;i++){
        if (v[i] < maxa - 1){
            in_hand -= ((maxa - 1) - v[i]);
            v[i] = maxa - 1;
        }
        if (v[i] == maxa){
            ccc++;
        }
    }


    if (in_hand < 0){
        cout << 0 << endl;
    }else if(in_hand == 0){
        cout << mod_mul(perm[ccc],perm[n-ccc]) << endl;
    }else {
        int x = n - ccc;
        int don = mod_mul(mod_inv(perm[x - in_hand]),mod_inv(perm[in_hand]));
        int don1 = mod_mul(perm[x],don);
        cout << mod_mul(don1,mod_mul(perm[in_hand + ccc],perm[n-(in_hand + ccc)])) << endl;
    }

    // cout << in_hand << endl;
    // for (int i = 1;i <= n;i++){
    //     cout << v[i] << " ";
    // }
    // cout << endl;







}

int32_t main(){
    // cout << fixed << setprecision(10);
    execute
    int t = 1;
    cin >> t;
    calc();
    while (t--) {
        solve();
    }

    return 0;
}