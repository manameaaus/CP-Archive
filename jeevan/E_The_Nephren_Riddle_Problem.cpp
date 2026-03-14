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


int const MAXN = 100001;
string s0 , s1 , s2, s3;
int l0,l1,l2,l3;
int dp[MAXN];
void calc(){
    s0 = "What are you doing at the end of the world? Are you busy? Will you save us?";
    s1 = "What are you doing while sending \"";
    s2 = "\"? Are you busy? Will you send \"";
    s3 = "\"?";

    l0 = len(s0);
    l1 = len(s1);
    l2 = len(s2);
    l3 = len(s3);

    dp[0] = l0;

    int maxax = 0;

    for (int i = 1;i < MAXN;i++){
        if (i < 56){
            dp[i] = l1 + dp[i-1] + l2 + dp[i-1] + l3;
        }else{
            dp[i] = dp[i-1];
        }
    }
}
void solve() {
    int n,k;cin >> n >> k;
    
    function<char(int,int)> find = [&](int n,int k) -> char{
        if (n == 0) return k >= l0 ? '.' : s0[k];

        if (k < l1) return s1[k];
        k -= l1;

        if (k < dp[n-1]) return find(n-1,k);
        k -= dp[n-1];

        if (k < l2) return s2[k];
        k -= l2;

        if (k < dp[n-1]) return find(n-1,k);
        k -= dp[n-1];

        if(k < l3) return s3[k];
        
        return '.';
    };

    cout << find(n,k-1);

}

int32_t main(){
    // cout << fixed << setprecision(10);
    execute
    int t = 1;
    calc();
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}