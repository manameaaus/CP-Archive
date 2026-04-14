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
int arr[5001];
int dp[5001][5001][2];

int rec(int l, int r, int pos) {
    if (l == r) {
        return arr[l] * pos;
    }
    if (dp[l][r][pos] != -1) {
        return dp[l][r][pos];
    }

    int x = rec(l+1,r,1-pos) + arr[l] * pos;
    int y = rec(l,r-1,1-pos) + arr[r] * pos;

    if (pos) {
        dp[l][r][pos] = max(x,y);
    } else {
        dp[l][r][pos] = min(x,y);
    }

    return dp[l][r][pos];

}

void solve() {
    cin >> n;
    memset(dp,-1,sizeof(dp));
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int x,y;

    for (int right = 0;right < n;right++){
        for(int left = right;left >= 0;left--){
            for(int pos = 0;pos < 2;pos++){
                if (left == right){
                    dp[left][right][pos] = pos * arr[left];
                }else{
                    x = dp[left][right-1][1-pos] + arr[right] * pos;
                    y = dp[left+1][right][1-pos] + arr[left] * pos;
                    if (pos){
                        dp[left][right][pos] = max(x,y);
                    }else{
                        dp[left][right][pos] = min(x,y);
                    }
                }
            }
        }
    }

    cout << dp[0][n-1][1];

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