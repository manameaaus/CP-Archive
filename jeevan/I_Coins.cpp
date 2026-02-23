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

int n;
double arr[3000];
double dp[3000][3000];

// double cal(int idx,int curr){
//     if (idx == n){
//         if (curr <= n/2) return 0.0;
//         else return 1.0;
//     }

//     if (dp[idx][curr] != -1.0) return dp[idx][curr];

//     double take = cal(idx+1,curr+1) * arr[idx];
//     double Nottake = cal(idx+1,curr) * (1 - arr[idx]);

//     return dp[idx][curr] = take + Nottake;
// }
// print(cal(0,0));


void solve() {
    cin >> n;

    for(int i = 1;i < n+1;i++){
        cin >> arr[i];
        dp[i-1][0] = 1.0;
    }

    for(int i = 1;i < n+1;i++){
        for(int j = 1;j < n+1;j++){
            dp[i][j] = dp[i-1][j-1] * arr[i] + dp[i-1][j] * (1 - arr[i]);
        }
    }
    print(dp[n][n/2+1]);
}

int32_t main(){
    cout << fixed << setprecision(10);
    JBR_CP_1000101
    int t = 1;
    // cin >> t;    
    while (t--) {
        solve();
    }

    return 0;
}