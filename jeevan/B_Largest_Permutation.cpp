#include <bits/stdc++.h>
using namespace std;

// ---------- debug utilities ----------

// ---------- shortcut macros ----------
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define len(x) (int)(x).size()
#define pb push_back
#define out(x) cout << (x) << endl;
#define out1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
#define out2(zzz) for (auto &zzzzz : zzz) {out1(zzzzz)}
#define space cout << endl;
#define execute ios_base::sync_with_stdio(false);cin.tie(NULL);

#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, a, b) for (int i = (a); i <= (b); ++i)
#define per(i, n) for (int i = (n) - 1; i >= 0; --i)
#define per1(i, a, b) for (int i = (b); i >= (a); --i)

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
#define in_vi(v, n) vi v(n); rep(i, n) cin >> v[i]
#define in_vs(v, n) vs> v(n); rep(i, n) cin >> v[i]
#define rd_vi(v) for (auto &x : v) cin >> x
#define rd_vs(v) for (auto &s : v) cin >> s
#define msb(x) (x == 0 ? -1 : 1<<(63 - __builtin_clzll(x)))      
#define lsb(x) (x == 0 ? -1 : 1<<(__builtin_ctzll(x)))   
#define pc(x) (__builtin_popcountll(x))
string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}

void solve() {
    int n,k;
    cin >> n >> k;
    in_vi(v,n);

    vi ref(n);

    rep(i,n){
        ref[v[i]-1] = i;
    }

    // rep(i,n){
    //     cout << ref[i] << " ";
    // }


    int c = 0;


    for(int i=0; c<min(n,k) && i<n; i++){


        
        int temp = n-i-1;

        if(temp+1 != v[i]){

        int ind1 = ref[temp];
        int num = v[i];

        ref[temp] = i;
        ref[v[i]-1] = ind1;

        v[i] = temp+1;
        v[ind1] = num;
        c++;
        }






    }

    rep(i,n){
        cout << v[i] << " ";
    }

    
    
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