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

void solve() {
    int n,m,k;
    cin >> n >> m >> k;

    vector<int> robot(n);
    set<int> spikes;
    set<array<int,3>> pos,neg;

    for(int i = 0;i < n;i++){
        cin >> robot[i];
    }
    for(int j = 0;j < m;j++){
        int sp;cin >> sp;
        spikes.insert(sp);
    }

    for(int i = 0;i < n;i++){
        int robo = robot[i];
        auto it = spikes.upper_bound(robo);

        int right = it == spikes.end()   ? INT_MAX : (*it);
        int left  = it == spikes.begin() ? INT_MIN : *(prev(it));

        pos.insert({right-robo,robo-left,i});
        neg.insert({robo-left,right-robo,i});
    }

    int curr = 0;
    int alive = n;
    for(int i = 0;i < k;i++){
        char op;cin >> op;

        if (op == 'L'){
            curr -= 1;
            for (auto it = neg.begin(); it != neg.end() && (*it)[0] <= -curr; ) {
                auto [l,r,i] = (*it);
                pos.erase({r,l,i});
                it = neg.erase(it);
                alive -= 1;
            }
        }else{
            curr += 1;
            for (auto it = pos.begin(); it != pos.end() && (*it)[0] <= curr; ) {
                auto [r,l,i] = (*it);
                neg.erase({l,r,i});
                it = pos.erase(it);
                alive -= 1;
            }
        }
        cout << alive << " ";
    }
    cout << endl;


}

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