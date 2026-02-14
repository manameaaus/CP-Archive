#include <bits/stdc++.h>
using namespace std;

// ---------- debug utilities ----------
// template<typename... Args>

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
// void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

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
#define msb(x) (x == 0 ? -1 : 1<<(63 - __builtin_clzll(x)))      
#define lsb(x) (x == 0 ? -1 : 1<<(__builtin_ctzll(x)))   
#define pc(x) (__builtin_popcountll(x))
string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}
ll gcd(ll a, ll b) {return b ? gcd(b, a % b) : a;}
ll lcm(ll a, ll b) {return a * b / gcd(a, b);}



void solve() {
    int n,w;
    cin >> n >> w;
    vi value(n);
    vi weight(n);

    rep(i,n){
        int a,b;
        cin >> a >> b;
        weight[i] = a;
        value[i] = b;
    }

    vvi mat(n+1,vi(w+1,0));

    rep1(i,1,n){
        rep1(j,1,w){
            if (weight[i-1] > j){
                mat[i][j] = mat[i-1][j];
            }else{
                mat[i][j] = max(mat[i-1][j-weight[i-1]]+value[i-1],mat[i-1][j]);
            }
        }
    }


    cout << mat[n][w] << endl;
}

int32_t main(){
    // cout << fixed << setprecision(10);
    execute
    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}


//   0  1  2  3  4  5  6  7  8
//      &  &  &  &  &  &  &  &
// 3 0  &  &  30 &  &  30 &  &
// 4 0  &  &  30 50 &  &  80  0
// 5 0  0  0  0  0  0  0  0  0