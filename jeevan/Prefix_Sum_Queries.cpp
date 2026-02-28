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
    int n,q; cin >> n >> q;
    invi(arr,n);

    // int b = sqrt(n)+1;
    int b = 400;
    vector<int> block((n+b-1)/b, 0);
    vector<int> pre(n);

    for (int i = 0;i < n;i++){
       pre[i] = arr[i];
    }

    for (int i = 0;i < n;i++){
        if (i%b != 0) pre[i] += pre[i-1];
        block[i/b] = max(block[i/b],pre[i]);
    }

    // print1(pre);
    // print1(block);

    // print1(pre);
    // print1(block);


    for(int h = 0; h < q; h++){
        int what;cin >> what;
        if (what == 1){
            
            int idx,val;
            cin >> idx >> val;
            idx--;

            // print(arr[idx]);

            arr[idx] = val;
            // print(arr[idx]);

            int run = (idx/b);
            int rune = min((run+1) * b,n);
            int runs = run*b;

            block[run] = 0;

            // print(runs,rune);

            // for (int i = runs;i < rune;i++){
            //     pre[i] = arr[i];
            // }

            pre[runs] = arr[runs];
            for (int i = runs;i < rune;i++){
                if (i%b != 0) pre[i] = pre[i-1] + arr[i];
                block[i/b] = max(block[i/b],pre[i]);
            }

            // print1(pre);
            // print1(block);

            // print(block[run]);

            // for (int i = runs;i < rune;i++){
            //     print(pre[i],i,"  l ");
            //     // if (i%b != 0) pre[i] += pre[i-1];
            //     // block[i/b] = max(block[i/b],pre[i]);
            // }

            
            
        }else{
            
            int l,r;cin >> l >> r;
            l--;r--;

            int curr = 0;
            int maxa = 0;

            int run = l;

            while ((run == l || run%b) && run <= r){
                curr+=arr[run];
                maxa = max(maxa,curr);
                run++;
            }

            // print(curr," hh",run);

            for (int j = run/b;j < r/b;j++){
                maxa = max(maxa,curr+block[j]);
                curr += pre[min(n-1,(j*b)+b-1)];
                run+=b;
            }
            // print(curr," hh");

            for(int j = max((r/b) * b,run);j <= min(n-1,r);j++){
                maxa = max(maxa,curr);
                curr += arr[j];
            }
            maxa = max(maxa,curr);

            cout << maxa << '\n';

            // break;
            
        }
    }
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