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
    int n,k,x;cin >> n >> k >> x;

    set<int> ans;
    set<int> frien;
    set<array<int,2>> run;

    vector<int> position(n);

    for(int i = 0;i < n;i++){
        cin >> position[i];
        frien.insert(position[i]);
    }


    sort(all(position));

    run.insert({-position[0],0});
    run.insert({-(x - position[n-1]),x});


    for(int i = 1;i < n;i++){
        int temp = (position[i] - position[i-1]) / 2;
        run.insert({-temp,position[i-1] + temp});
    }



    while (ans.size() < k){
        auto it = *run.begin();
        ans.insert(it[1]);
        run.erase(it);
 
        if (it[1] + 1 <= x and ans.count(it[1] + 1) == 0){
            auto next = frien.upper_bound(it[1] + 1);
            int mina = INT_MAX;
            if (next != frien.end()){
                mina = min(mina,abs((*next) - (it[1] + 1)));
            }
            if (next != frien.begin()){
                next--;
                mina = min(mina,abs((*next) - (it[1] + 1)));
            }
            
            run.insert({-mina,it[1] + 1});
        }

        if (it[1] - 1  >= 0 and ans.count(it[1] - 1) == 0){
            auto next = frien.upper_bound(it[1] - 1);
            int mina = INT_MAX;
            if (next != frien.end()){
                mina = min(mina,abs((*next) - (it[1] - 1)));
            }
            next--;
            mina = min(mina,abs((*next) - (it[1] - 1)));
            run.insert({-mina,it[1] - 1});
        }

    }

    for(auto xxx:ans){
        cout << xxx << " ";
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