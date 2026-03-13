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

const int INV2 = 500000004;

void solve() {
    int n;cin >> n;

    // print((sqrt(5)));

    int ans = 0;
    // int k,num;

    for (int i = 1;i * i <= n;i++){

        int num = i;
        int p = n/i;
        int k = mod_mul(n, mod_inv(num));  // k = n / num under modulo
        print((mod_inv(num)*10) % MOD,num,p,k);

        int64_t kkk = ((int64_t)k * (k + 1)) % MOD;
        int64_t nnn = ((int64_t)num * (num + 1)) % MOD;

        int64_t diff = (kkk - nnn + MOD) % MOD;
        int64_t term1 = (diff * INV2) % MOD;

        int64_t term2 = ((int64_t)(k - num + 1) * num) % MOD;

        ans = mod_add(mod_add(ans , term1) , term2);

        // num = i;
        // k = n/num;
        // k = mod_mul(n , mod_inv(num));
        // // int kkk = mod_mul(k,(k + 1));
        // // int nnn = mod_mul(num,(num - 1));
        // // int diff = mod_sub(kkk,nnn);

        // // int temp = mod_mul(num,diff);
        // // ans = mod_add(ans,(k-num+1)*num);
        // // ans = mod_add(ans,(k-num+1)*num);
        

        // // int kkk = (k*(k + 1));
        // // int nnn = (num*(num + 1));
        // // int diff = (kkk-nnn);
        // // ans = ans + diff/2 + (k-num+1)*num;

        // int64_t kkk = ((int64_t)k * (k + 1)) % MOD;
        // int64_t nnn = ((int64_t)num * (num + 1)) % MOD;

        // int64_t diff = (kkk - nnn + MOD) % MOD;
        // int64_t term1 = (diff * INV2) % MOD;

        // int64_t term2 = ((int64_t)(k - num + 1) * num) % MOD;

        // ans = (ans + term1 + term2) % MOD;


        // print(diff);

        // int temp = (num*diff);
        // print(i,ans);
        // print("____");
        // print(kkk,nnn,k);
        // print();
        // ans = mod_add(ans,temp/2);


    }

    print(ans);

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