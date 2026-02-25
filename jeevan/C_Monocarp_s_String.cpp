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



void solve() {
    int n;cin >> n;

    string s;
    cin >> s;

    s = "z" + s;

    set<pii> intro;
    vector<int> suff(n+1);
    vector<int> pre(n+1);

    int ca = 0,cb = 0,diff = 0;
    for(int i = n;i > 0;i--){
        if (s[i] == 'a'){
            ca++;
        }else{
            cb++;
        }
        suff[i] = ca - cb;
        intro.insert({suff[i],i});
    }
    intro.insert({0,n+1});

    // cout << " " << endl;
    // for(auto x:intro){
    //     cout << x.first << " " << x.second << endl;
    // }
    // cout << " " << endl;

    // auto it = intro.lower_bound({0,-1});
    // if (it != intro.end()){
    //     print("hello");
    // }

    ca = 0,cb = 0;
    int ans = n;
    for(int i = 0;i < n;i++){
        diff = ca-cb;
        auto it = intro.lower_bound({-diff,-1});
        if (it != intro.end() and ((*it).first == -diff)){
            ans = min(ans,(*it).second - i - 1);
        }
        intro.erase({suff[i+1],i+1});
        if (s[i+1] == 'a'){
            ca++;
        }else{
            cb++;
        }
    }
    if (ans == n){
        print(-1);
    }else{
        print(ans);
    }
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