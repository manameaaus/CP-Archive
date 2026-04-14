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

    vector<int> values(n);
    for(int i = 0; i < n; i++) cin >> values[i];

    vector<vector<int>> adj(n+1);

    for (int i = 0; i < n-1;i++){
        int u,v;cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // print1(adj[1]);

    int dp[n+1],ans[n+1],durra[n+1],pd[n+1];
    for(int i = 0;i <= n;i++){
        dp[i] = 0;
        ans[i] = 0;
        durra[i] = 0;
    }

    // print1(adj[4]);return;

    function<int(int,int)> dfs_calc = [&](int node,int par) -> int{
        dp[node] = values[node - 1];
        for(int cld:adj[node]){
            if (cld != par) dp[node] += dfs_calc(cld,node);
        }
        return dp[node];
    };

    dfs_calc(1,0);


    function<int(int,int)> dfs = [&](int node,int par) -> int{
        int best_len = -1;
        int len = 0;
        int second = 0;

        int don = -1;
        int maxa = 0;
        int kkk = -1;

        int plain_ans = 0;


        // vector<int> all_heights;


        for(int cld:adj[node]){
            if(cld != par){
                int temp = dfs(cld,node);
                // cout << cld << " " << node 
                plain_ans += temp;

                if (durra[cld] >= len) {
                    second = len;
                    len = durra[cld];
                    best_len = cld;
                }else if (durra[cld] > second){
                    second = durra[cld];
                }

                // if (node == 4){
                //     cout << durra[cld] << " " << cld << " "  << c1 << endl;
                // }
                if (temp > maxa){
                    maxa = temp;
                    don = cld;
                    kkk = temp;
                }
            }
        }


        int res = plain_ans;

        if (don != -1) {

            int to_add = ans[don] - pd[don] + dp[don];
    
            // if (best_len != don || c1 > 1){
                //     to_add = max((dp[don] * len),to_add);
                // }else if (best_len == don){
                    // }
                    
                    for (int cld:adj[node]) {
                        if ((cld != par)){
                            int jjjj = len;
                            if (durra[cld] == jjjj){
                                jjjj = second;
                            }
                            to_add = max(to_add,dp[cld] * jjjj);
                            // if (node == 3){
                            //     print(to_add,dp[don],don,cld,res);
                            // }
                        }
                    }
                    // cout << c1 << endl;
                    // cout << best_len << " " << don << " " << node << " -- ";
                    // cout << to_add << " ";
                    // cout << endl << endl;
                    
            // print(res,to_add,node);
            // print(plain_ans,node);
            res += to_add;
        }
        
        
        ans[node] = res * min(1ll,best_len+1);
        durra[node] = len + 1;


        // print(plain_ans ,node);
        return pd[node] = plain_ans + dp[node];
        // return plain_ans + values[node-1];
    };

    dfs(1,0);
    for(int i = 1;i <= n;i++){
        cout << ans[i] << " ";
    }
    cout << endl;

    // print1(dp);
    // print1(pd);
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







// #include <bits/stdc++.h>
// using namespace std;

// // ---------- debug utilities ----------
// template<typename... Args>

// // ---------- shortcut macros ----------
// #define all(a) (a).begin(), (a).end()
// #define rall(a) (a).rbegin(), (a).rend()
// #define len(x) (int)(x).size()
// #define pb push_back
// #define print1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
// #define print2(zzz) for (auto &zzzzz : zzz) {print1(zzzzz)}
// #define space cout << endl;
// #define sum(v) (accumulate((v).begin(), (v).end(), 0LL))
// #define execute ios_base::sync_with_stdio(false);cin.tie(NULL);

// #define rep(i, n) for (int i = 0; i < (n); ++i)
// #define rep1(i, a, b) for (int i = (a); i <= (b); ++i)
// #define per(i, n) for (int i = (n) - 1; i >= 0; --i)
// #define per1(i, a, b) for (int i = (b); i >= (a); --i)
// void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

// // ----------- constants -----------
// #define PI 3.14159265358979323846
// #define INF 1e18
// #define MOD 1000000007
// #define MOD2 998244353

// // ---------- type aliases ----------
// #define ll long long
// #define int long long
// #define vi vector<int> 
// #define vc vector<char> 
// #define vs vector<string> 
// #define vvc vector<vector<char>> 
// #define vvi vector<vector<int>> 
// #define pii pair<int, int> 

// // ---------- input macros ----------
// #define invi(v, n) vi v(n); rep(i, n) cin >> v[i]
// #define invs(v, n) vs> v(n); rep(i, n) cin >> v[i]
// #define rdvi(v) for (auto &x : v) cin >> x
// #define rdvs(v) for (auto &s : v) cin >> s
// #define msb(x) (x == 0 ? -1 : 1<<(63 - __builtin_clzll(x)))      
// #define lsb(x) (x == 0 ? -1 : 1<<(__builtin_ctzll(x)))   
// #define pc(x) (__builtin_popcountll(x))
// string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}

// void solve() {
//     int n;
//     cin >> n;

//     vector<int> cost(n+1);
//     for (int i = 1;i <= n;i++) cin >> cost[i];

//     vector<vector<int>> adj(n+1);

//     for (int i = 0; i < n-1;i++){
//         int u,v;cin >> u >> v;

//         adj[u].push_back(v);
//         adj[v].push_back(u);
//     }

//     vector<int> plain(n+1),ans(n+1),subTreeSum(n+1),haala(n+1);

//     function<void(int,int)> dfs = [&](int node,int par) {
//         int maxDepth = 0, secondDepth = 0, total_plain = 0, tree_sum = cost[node], sonInLaw = 0 , cur_ans = 0;
//         for (int cld : adj[node]){
//             if (cld != par){
//                 dfs(cld , node);
//                 if (haala[cld] >= maxDepth){
//                     secondDepth = maxDepth;
//                     maxDepth = haala[cld];                    
//                 }else if (haala[cld] > secondDepth){
//                     secondDepth = haala[cld];
//                 }

//                 sonInLaw = max(sonInLaw, ans[cld] - plain[cld]);

//                 total_plain += plain[cld] + subTreeSum[cld];
//                 cur_ans += plain[cld] + subTreeSum[cld];
//                 tree_sum += subTreeSum[cld];
//             }
//         }


//         subTreeSum[node] = tree_sum;
//         haala[node] = maxDepth + 1;
//         plain[node] = total_plain;
        
//         cur_ans += sonInLaw;
//         for (int cld : adj[node]){
//             if (cld != par){
//                 int useful = maxDepth;
//                 if (haala[cld] == useful){
//                     useful = secondDepth;
//                 }
//                 cur_ans = max(cur_ans,total_plain + useful * subTreeSum[cld]);
//             }
//         }
//         ans[node] = cur_ans;
//         // if (node == 3){
//         //     print(subTreeSum[4],secondDepth,total_plain);
//         // }
//         // print(total_plain,node);
//     };

//     dfs(1,0);
//     for(int i = 1;i <= n;i++) cout << ans[i] << " ";
//     cout << endl;
// }

// int32_t main(){
//     // cout << fixed << setprecision(10);
//     execute
//     int t = 1;
//     cin >> t;
//     while (t--) {
//         solve();
//     }

//     return 0;
// }