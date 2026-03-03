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

// void solve(int which,int correct,int n) {
//     vector<vector<int>> adj(n+1);
//     for (int i = 0;i < n-1;i++){
//         int u,v;
//         cin >> u >> v;
//         adj[u].push_back(v);
//         adj[v].push_back(u);
//     }



//     map<int,int> freq;
//     vector<int> leaf(n+1);


//     function<int(int,int)> dfs = [&](int node,int par){
//         int leafs = 0;
//         for (auto cld : adj[node]){
//             if (cld != par){
//                 int ccc = dfs(cld,node);
//                 leafs += ccc;
//             }
//         }
//         if (leafs == 0) {leafs += 1;}; 
//         leaf[node] = leafs;
//         // cout << node << " " << leafs;

//         if ((node == 1 && adj[node].size() > 1) || (adj[node].size() > 2)){
//             freq[leafs%3]++;
//         }

//         return leafs;
//     };


//     int total_leaves = dfs(1,0);
//     // int leafs = leaf[1];
//     // if (!leafs or freq[((leafs)%3 + 1)%3] > 0){
//     //     cout << "YES" << endl;
//     //     // cout << leafs << " " << leaf[(leafs + 1)%3] << " " << (leafs + 1)%3;
//     //     return;
//     // }


//     if (total_leaves % 3 == 0){
//         cout << "YES" << endl;
//         return;
//     }

//     for (int i = 1;i < n+1;i++){
//         int leafs = leaf[i];
//         if ((total_leaves - leafs + 1) % 3 == 0){
//             cout << "YES" << endl;
//             return;
//         }
//     }





//     int to_look = (total_leaves) % 3;

//     // cout << total_leaves << endl;
//     // for(auto x:freq){
//     //     cout << x.first << " " << x.second << endl;
//     // }

//     if ((to_look == 2 && freq[2] > 1) || (to_look == 1 && freq[0] > 1)){
//         cout << "YES" << endl;
//         return;
//     }
//     cout << "NO" << endl;



//     // cout << leafs << " " ;

//     // 1 2 3 4 5 6 7 8 9 10
//     // 1 2 0 1 2 0 1 2 0 1


// }

// int32_t main(){
//     // cout << fixed << setprecision(10);
//     execute
//     int t = 1;
//     cin >> t;
//     int c = 0;
//     int correct = true;
//     while (c < t) {
//         int n;cin >> n;
//         if (c == 0 and n == 3) correct = false;
//         solve(c,correct,n);
//         c++;
//     }

//     return 0;
// }



// // (8|4)(9|5)(1|4)(9|4)(7|1)(3|7)(7|6)(2|1)











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

    vector<vector<int>> adj(n+1);
    for (int i = 0;i < n-1;i++){
        int u,v;cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }


    function<array<int,4>(int,int)> dfs = [&](int node,int par){

        array<int,4> check = {0,0,0,0},temp;
        int leafs = 0;

        for(int cld : adj[node]){
            if (cld != par){
                temp = dfs(cld,node);
                for (int i = 0;i < 3;i++) check[i]+=temp[i]; 
                leafs += temp[3];
            }
        }

        if (adj[node].size() == 1 and par != 0) leafs++;
        if (check[leafs%3] == 0) check[leafs%3]++;
        
        check[3] = leafs;
        return check;
    };

    array<int,4> total = dfs(1,0);
    int leaves = total[3];

    if((leaves % 3 == 0)) {
        cout << "YES" << endl;
        return;
    }
    if ((leaves % 3 == 1) && (total[2] > 0 || total[0] > 1)){
        cout << "YES" << endl;
        return;
    }
    if ((leaves % 3 == 2) && (total[2] > 1 || total[0] > 0)){
        cout << "YES" << endl;
        return;
    }

    cout << "NO" << endl;
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