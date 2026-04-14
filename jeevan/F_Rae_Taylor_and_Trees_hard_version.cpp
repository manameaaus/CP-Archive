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
    int n;cin >> n;
    vector<int> v(n);
    for (int i = 0;i < n;i++){
        cin >> v[i];
    }

    int mina = INT_MAX;
    int maxa = -1;

    set<int> curr(all(v));
    vector<int> vis(n+1,0);
    vector<int> idx(n+1); 

    for (int i = n-1;i >= 1;i--){
        mina = min(v[i],mina);
        maxa = max(v[i],maxa);

        if ((maxa == n-i) && (mina == 1)){
            cout << "No" << endl;
            return;
        }

        idx[v[i]] = i;
    }

    cout << "Yes" << endl;


    vector<array<int,2>> edges;

    int live = idx[1];
    int to_use = 0;

    while (edges.size() < n-1){
        int j = live;
        int next_max = -1;
        int curr_min = v[live];

        while ((j < n) and (!vis[j])){
            next_max = max(next_max,v[j]);
            if (v[j] != 1){
                if (v[j] < to_use){
                    edges.push_back({to_use,v[j]});
                }else{
                    edges.push_back({curr_min,v[j]});
                }
            }
            vis[j] = 1;
            curr.erase(v[j]);
            j++;
        }

        int next_idx = n;

        while ((curr.begin() != curr.end()) and (*curr.begin() < next_max)){
            next_idx = min(next_idx,idx[*curr.begin()]);
            curr.erase(curr.begin());
        }

        live = next_idx;
        to_use = next_max;
    }


    for (auto [u,v] : edges){
        cout << u << " " << v << endl;
    }


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