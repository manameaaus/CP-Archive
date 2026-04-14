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
    int n,q;cin >> n >> q;
    // int left[n+1],right[n+1],dp[n+1],parent[n+1][21],cost[n+1][21];


    vector<int> left(n + 1, -1);
    vector<int> right(n + 1, -1);
    vector<int> dp(n + 1,0);

    vector<vector<int>> parent(n + 1, vector<int>(21, 0));
    vector<vector<int>> cost(n + 1, vector<int>(21));


    vector<int> order;
    vector<int> first_idx(n+1,MOD);

    
    for(int par = 1;par <= n;par++){
        int u,v;cin >> u >> v;
        left[par] = u;
        right[par] = v;
        if (u)
        parent[u][0] = par;
        parent[v][0] = par;
    }


    function<int(int,int)> dfs = [&](int node, int par) -> int{
        if (node == 0) return 0;
        int l,r,decendants;
        
        first_idx[node] = min(len(order),first_idx[node]);

        order.push_back(node);
        l = dfs(left[node],node);
        if(l) order.push_back(node);
        r = dfs(right[node],node);
        if(r) order.push_back(node);


        decendants = l + r + 1;
        dp[node] = 2 * decendants - 1;
        return decendants;
    };
    dfs(1,0);

    for(int node = 2;node <= n;node++){
        cost[node][0] = dp[node] + dp[parent[node][0]];
    }


    // print1(parent[2]);
    // print1(cost[2]);


    for(int par = 1;par <= 20;par++){
        for (int node = 2;node <= n;node++){
            int prev_par = parent[node][par-1];
            
            parent[node][par] = parent[prev_par][par-1];
            cost[node][par] = cost[node][par-1] + cost[prev_par][par-1] - dp[prev_par];
            cost[node][par] = (cost[node][par] > cost[node][par-1]) ? cost[node][par] : MOD;
            // if (node == 2 and par == 1){
            //     print("hello");
            //     print(cost[node][par],cost[node][par-1],par);
            // }
        }
    }

    for(int j = 0;j < q;j++){
        int v,pp; cin >> v >> pp;
        
        int node = v;
        int k = pp;
        for(int par = 19;par >= -1;par--){
            if (par != -1){
                if ((k < dp[node]) or (node == 1)){
                    // print(order[first_idx[node]+k]);
                    cout << order[first_idx[node]+k] << " ";
                    // cout << order[first_idx[node]+k] << "---- ";
                    break;
                }
                if (k >= cost[node][par] and k < cost[node][par+1]){
                    k -= cost[node][par];
                    // node = parent[node][par+1];
                    node = parent[parent[node][par]][0];
                }
            }
            else{
                // print(order[first_idx[node] + k]);
                // cout << "he,llll" << " " << v << " " 
                // print(v,k,"--------");
                // cout << v << " " << k  


                if (k <= dp[node]){
                    // print(node,k);
                    // cout << order[first_idx[node] + k] << " =====";
                    cout << order[first_idx[node] + k] << " ";
                    break;
                }
                k -= dp[node];
                // cout << order[first_idx[parent[node][0]] + k] << " .....";
                cout << order[first_idx[parent[node][0]] + k] << " ";
            }
        }
    }
    cout << endl;


    // print1(parent[1]);
    // print1(cost[1]);
    // print1(parent[2]);
    // print1(cost[2]);
    // print1(parent[3]);
    // print1(cost[3]);
    // print1(parent[4]);
    // print1(cost[4]);
    // print1(parent[5]);


    // for (int node = 2;node <= n;node ++){
    //     print1(parent[node]);
    //     print1(cost[node]);
    //     cout << "------" << endl;
    // }
    

    // print1(parent[7]);
    // print1(cost[7]);
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