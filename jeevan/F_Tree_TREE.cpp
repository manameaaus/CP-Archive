// #include <bits/stdc++.h>
// using namespace std;

// // ---------- debug utilities ----------
// #ifndef Local
//     #define debug(...)
//     #define debugArr(...)
// #else
//     #include <debug.cpp>
//     auto start = chrono::high_resolution_clock::now();
// #endif


// // ---------- shortcut macros ----------
// #define all(a) (a).begin(), (a).end()
// #define rall(a) (a).rbegin(), (a).rend()
// #define len(x) (int)(x).size()
// #define pb push_back
// #define print(zzz) cout << zzz << ' '<<endl;
// #define print1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
// #define print2(zzz) for (auto &zzzzz : zzz) {print1(zzzzz)}
// #define space cout << endl;
// #define sum(v) (accumulate((v).begin(), (v).end(), 0LL))
// #define lb(v, x) (lower_bound((v).begin(), (v).end(), (x)) - (v).begin())  
// #define ub(v, x) (upper_bound((v).begin(), (v).end(), (x)) - (v).begin())  
// #define execute ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

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
// #define msb(x) (x == 0 ? -1 : 1ll<<(63 - __builtin_clzll(x)))      
// #define lsb(x) (x == 0 ? -1 : 1ll<<(__builtin_ctzll(x)))   
// #define pc(x) (__builtin_popcountll(x))
// ll gcd(ll a, ll b) {return b ? gcd(b, a % b) : a;}
// ll lcm(ll a, ll b) {return a * b / gcd(a, b);}

// struct array2_hash {
//     size_t operator()(const array<int,2> &a) const {
//         return hash<int>()(a[0]) ^ (hash<int>()(a[1]) << 1);
//     }
// };

// void solve() {
//     int k,n;cin >> n >> k;
//     int ans = 0;
//     int c_for = 0,co = 0;


//     vvi adj(n+1);
//     // unordered_map<hash<array<int,2>>,array<int,2>> edge;
//     unordered_map<array<int,2>, array<int,2>, array2_hash> edge;

//     for(int i = 1;i <= n-1;i++){
//         int u,v; cin >> u >> v;
//         adj[u].pb(v);
//         adj[v].pb(u);
//     }

//     function<void(int,int)> dfs = [&](int par,int node) {
//         co++;
//         int down = 1,temp = 0;

//         for(int nbr:adj[node]){
//             c_for++;
//             if (nbr == par) continue;
//             if (edge.count({node,nbr}) == 0) dfs(node,nbr) ;
            
//             temp += edge[{node,nbr}][0];
//             down += edge[{node,nbr}][1];
//         }

//         temp += down >= k;
//         edge[{par,node}] = {temp,down};
//     };


//     for(int i = 1;i <= n;i++){
//         dfs(0,i);
//         ans += edge[{0,i}][0];
//     }

//     cout << ans << endl;
//     debug(c_for,n,co);
// }

// int32_t main(){
//     // cout << fixed << setprecision(10);
//     #ifdef Local
//         freopen("input.txt", "r+", stdin);
//         freopen("output.txt", "w+", stdout);
//     #endif

//     execute
//     int t = 1;
//     cin >> t;
//     // cout << t;
//     while (t--) {
//         solve();
//     }
    
//     #ifdef Local
//         chrono::duration<double> elapsed = chrono::high_resolution_clock::now() - start;
//         cerr << fixed << setprecision(6) << "\nTime: " << elapsed.count() << "s\n"; 
//     #endif
//     return 0;
// }




// ...existing code...
#include <bits/stdc++.h>
using namespace std;

// ---------- debug utilities ----------
#ifndef Local
    #define debug(...)
    #define debugArr(...)
#else
    #include <debug.cpp>
    auto start = chrono::high_resolution_clock::now();
#endif


// ---------- shortcut macros ----------
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define len(x) (int)(x).size()
#define pb push_back
#define print(zzz) cout << zzz << ' '<<endl;
#define print1(zzz) for(auto zzzz: zzz) cout << zzzz << ' ';cout<<endl;
#define print2(zzz) for (auto &zzzzz : zzz) {print1(zzzzz)}
#define space cout << endl;
#define sum(v) (accumulate((v).begin(), (v).end(), 0LL))
#define lb(v, x) (lower_bound((v).begin(), (v).end(), (x)) - (v).begin())  
#define ub(v, x) (upper_bound((v).begin(), (v).end(), (x)) - (v).begin())  
#define execute ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

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
#define msb(x) (x == 0 ? -1 : 1ll<<(63 - __builtin_clzll(x)))      
#define lsb(x) (x == 0 ? -1 : 1ll<<(__builtin_ctzll(x)))   
#define pc(x) (__builtin_popcountll(x))
ll gcd(ll a, ll b) {return b ? gcd(b, a % b) : a;}
ll lcm(ll a, ll b) {return a * b / gcd(a, b);}
// ...existing code...

void solve() {
    int k,n;cin >> n >> k;
    int ans = 0;
    int c_for = 0,co = 0;

    // Build adjacency with directed-edge indices:
    // for each undirected edge eid (0..m-1) we create two directed indices: eid*2 and eid*2+1
    // additionally we reserve indices base0 + node for virtual parent 0 -> node
    vvi dummy; // placeholder to keep file structure similar
    vector<vector<pair<int,int>>> adj(n+1);
    int m = max<int>(0, n-1);
    int eid = 0;
    for(int i = 1;i <= n-1;i++){
        int u,v; cin >> u >> v;
        adj[u].push_back({v, eid*2});
        adj[v].push_back({u, eid*2+1});
        eid++;
    }
    int base0 = 2*m; // start index for virtual edges 0->node : base0 + node
    int total_dir = base0 + (n+5);

    // dir_temp[idx] and dir_down[idx] store values for directed edge represented by idx
    vector<int> dir_temp(total_dir, -1);
    vector<int> dir_down(total_dir, -1);

    function<void(int,int,int)> dfs = [&](int par,int node,int pidx) {
        co++;
        int down = 1, temp = 0;

        for(auto &pr : adj[node]){
            int nbr = pr.first;
            int idx_node_nbr = pr.second;
            c_for++;
            if (nbr == par) continue;
            if (dir_down[idx_node_nbr] == -1) dfs(node, nbr, idx_node_nbr);
            
            temp += dir_temp[idx_node_nbr];
            down += dir_down[idx_node_nbr];
        }

        temp += (down >= k);
        dir_temp[pidx] = temp;
        dir_down[pidx] = down;
    };


    for(int i = 1;i <= n;i++){
        int pidx = base0 + i;
        if (dir_down[pidx] == -1) dfs(0, i, pidx);
        ans += dir_temp[pidx];
    }

    cout << ans << endl;
    debug(c_for,n,co);
}
// ...existing code...

int32_t main(){
    // cout << fixed << setprecision(10);
    #ifdef Local
        // freopen("input.txt", "r+", stdin);
        // freopen("output.txt", "w+", stdout);
    #endif

    execute
    int t = 1;
    cin >> t;
    // cout << t;
    while (t--) {
        solve();
    }
    
    #ifdef Local
        chrono::duration<double> elapsed = chrono::high_resolution_clock::now() - start;
        cerr << fixed << setprecision(6) << "\nTime: " << elapsed.count() << "s\n"; 
    #endif
    return 0;
}