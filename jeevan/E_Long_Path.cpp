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


ll mod_mul(ll a,ll b) {return ((a % MOD) * (b % MOD)) % MOD;}
ll mod_add(ll a,ll b) {return ((a % MOD) + (b % MOD)) % MOD;}
ll mod_sub(ll a,ll b) {return ((a % MOD) - (b % MOD) + MOD) % MOD;}
ll mod_pow(ll a,ll b, ll m = MOD) {ll res = 1;a %= m;while (b) {if (b & 1ll) res = res * a % m;a = mod_mul(a, a);b >>= 1ll;}return res;}
ll mod_inv(ll a, ll m = MOD) {return mod_pow(a, m - 2, m);}  // fermat's little theorem
ll mod_div(ll a, ll b) {return mod_mul(a, mod_inv(b));}


// int dp[1003][1003][2];
int dp2[1003][2];

void solve() {
    int n;
    cin >> n;

    vector<int> p(n+1);
    for(int i = 1;i < n+1;i++) cin >> p[i];

    int ans = 0;

    vector<int> steps(n+1);

    memset(dp2,-1,sizeof dp2);

    // int c = 0;
    // int used = 0;
    // int got = 0;
    // function<int(int,int,int)> ddc = [&](int node,int curr,int par) -> int{
    //     if (got) return 0;
    //     if (node == n+1){
    //         cout << curr << endl;
    //         got = 1;
    //         return 0;
    //     }
    //     c++;
    //     // if (c > 1000000){
    //     //     return 0;
    //     // }
    //     curr++;
    //     // if (node > n){
    //     //     print(node,"kk");
    //     //     return;
    //     // }
    //     // cout << node << endl;
    //     steps[node]++;
    //     // print(node,par,curr,steps[node]%2,"l");
    //     if (dp2[node][steps[node]%2] != -1){
    //         // print(node,"jjj",(curr-2) , dp2[node][steps[node]%2]);
    //         used = 1;
    //         int yyy = mod_sub((curr-2) , dp2[node][steps[node]%2]);
    //         steps[node]--;
    //         return yyy;
    //     }else{
    //         // steps[node]++;
    //         // steps[node] = mod_add(1,steps[node]);
    //         dp2[node][steps[node]%2] = mod_sub(curr,1);
    //         if(steps[node] % 2){
    //             // ddc(p[node],curr,node);
                
    //             curr = mod_add(ddc(p[node],curr,node),curr);
    //             if (true or (used) and (got == 0)){
    //                 used = 0;
    //                 curr = mod_add(1,curr);
    //                 steps[node] = mod_add(1,steps[node]);
    //                 dp2[node][steps[node]%2] = mod_sub(curr,1);
    //                 // print(node,par,curr,steps[node]%2);
    //                 return ddc(node+1,curr,node);
    //             }
    //             // steps[node]++;
    //             // dp2[node][steps[node]%2] = curr-2;
    //             // return 1;
    //         }else{
    //             // dp2[node][steps[node]%2] = mod_sub(curr,1);
    //             // dp2[node][steps[node]%2] = mod_sub(curr,2);
    //             return ddc(node+1,curr,node);
    //         }
    //     }

    // };

    int reached = 0;
    function<int(int,int,int)> ddc = [&](int node,int par,int curr) -> int{
        if (reached) return 0;
        steps[node] = 1-steps[node];
        curr = mod_add(1,curr);

        if (dp2[node][steps[node]] != -1){
            int temp = mod_sub(curr - 2 , dp2[node][steps[node]]);
            steps[node] = 1-steps[node];
            return temp;
        }else{
            dp2[node][steps[node]] = curr - 1;
            if (steps[node]){

                curr = mod_add(curr,ddc(p[node],node,curr));
                curr = mod_add(curr,1);
                steps[node] = 1-steps[node];
                dp2[node][steps[node]] = curr - 1;
                return ddc(node+1,curr,node);
            }else{
                return ddc(node+1,curr,node);

            }
        }


    };
    ddc(1,0,0);
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







// 1 0 1 1 
// 1 1 2 0 
// 2 1 3 1 
// // 1 2 4 1 
// // 1 1 5 0 
// 2 1 6 0 
// 3 2 7 1 
// // 1 3 8 1 
// // 1 1 9 0 
// // 2 1 10 1 
// // 1 2 11 1 
// // 1 1 12 0 
// // 2 1 13 0 
// 3 2 14 0 
// 4 3 15 1 
// // 1 4 16 1 
// // 1 1 17 0 
// // 2 1 18 1 
// // 1 2 19 1 
// // 1 1 20 0 
// // 2 1 21 0 
// // 3 2 22 1 
// // 1 3 23 1 
// // 1 1 24 0 
// // 2 1 25 1 
// // 1 2 26 1 
// // 1 1 27 0 
// // 2 1 28 0 
// // 3 2 29 0 
// 4 3 30 0 
// 5 4 31 1 
// // 1 5 32 1 
// // 1 1 33 0 
// // 2 1 34 1 
// // 1 2 35 1 
// // 1 1 36 0 
// // 2 1 37 0 
// // 3 2 38 1 
// // 1 3 39 1 
// // 1 1 40 0 
// // 2 1 41 1 
// // 1 2 42 1 
// // 1 1 43 0 
// // 2 1 44 0 
// // 3 2 45 0 
// // 4 3 46 1 
// // 1 4 47 1 
// // 1 1 48 0 
// // 2 1 49 1 
// // 1 2 50 1 
// // 1 1 51 0 
// // 2 1 52 0 
// // 3 2 53 1 
// // 1 3 54 1 
// // 1 1 55 0 
// // 2 1 56 1 
// // 1 2 57 1 
// // 1 1 58 0 
// // 2 1 59 0 
// // 3 2 60 0 
// // 4 3 61 0 
// 5 4 62 0 



// 1 0 1 1 
// 1 1 2 0 
// 2 1 3 1 
// // 1 2 4 1 
// // 1 1 5 0 
// 2 1 6 0 
// 3 2 7 1 
// // 2 3 8 1 
// // 1 2 9 1 
// // 1 1 10 0 
// // 2 1 11 0 
// 3 2 12 0 
// 4 3 13 1 
// // 3 4 14 1 
// // 2 3 15 1 
// // 1 2 16 1 
// // 1 1 17 0 
// // 2 1 18 0 
// // 3 2 19 0 
// 4 3 20 0 




// 1 0 1 0 
// 1 1 2 1 
// 1 0 2 0 
// 2 1 3 0 
// 1 2 4 0 
// 1 1 5 1 
// 1 2 5 0 
// 2 1 6 1 
// 2 1 6 0 
// 3 2 7 0 
// 2 3 8 0 
// 1 2 9 0 
// 1 1 10 1 
// 1 2 10 0 
// 2 1 11 1 
// 2 3 11 0 
// 3 2 12 1 
// 3 2 12 0 
// 4 3 13 0 
// 3 4 14 0 
// 2 3 15 0 
// 1 2 16 0 
// 1 1 17 1 
// 1 2 17 0 
// 2 1 18 1 
// 2 3 18 0 
// 3 2 19 1 
// 3 4 19 0 
// 4 3 20 1 
// 4 3 20 0