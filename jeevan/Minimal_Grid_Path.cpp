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
// #define JBR_CP_1000101 ios_base::sync_with_stdio(false);cin.tie(NULL);

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
// #define invs(v, n) vs v(n); rep(i, n) cin >> v[i]
// #define rdvi(v) for (auto &x : v) cin >> x
// #define rdvs(v) for (auto &s : v) cin >> s
// #define msb(x) (x == 0 ? -1 : 1ll<<(63 - __builtin_clzll(x)))      
// #define lsb(x) (x == 0 ? -1 : 1ll<<(__builtin_ctzll(x)))   
// #define pc(x) (__builtin_popcountll(x))
// string d2b(long long num, ll pad = 0) { if (num == 0) return string(max(1LL, pad), '0');string res;while (num) {res += '0' + (num & 1);num >>= 1;}reverse(res.begin(), res.end());if (len(res) < pad) res = string(pad - res.size(), '0') + res;return res;}

// string dp[2][3003];

// void solve() {
//     int n;cin >> n;
//     char curr;
    
//     for(int i = 1;i <= n;i++){
//         for(int j = 1;j <= n;j++){
//             cin >> curr;
//             if (i == 1 and j == 1) dp[i%2][j] = curr;
//             else if (i == 1) dp[i%2][j] = dp[i%2][j-1] + curr;
//             else if (j == 1) dp[i%2][j] = dp[1-(i%2)][j] + curr;
//             else dp[i%2][j] = min(dp[1-(i%2)][j],dp[i%2][j-1]) + curr;
//         }   
//     }
//     cout << dp[n%2][n];
// }

// int32_t main(){
//     // cout << fixed << setprecision(10);
//     JBR_CP_1000101
//     int t = 1;
//     // cin >> t;
//     while (t--) {
//         solve();
//     }

//     return 0;
// }



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
// #define int long long
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
    int n;cin >> n;
    vvc mat(n,vc(n));
    for(int i = 0;i < n;i++) for(int j = 0;j < n;j++) cin >> mat[i][j];

    vvi vis(n,vi(n,0));
    vvi p(n,vi(n,-1));


    queue<array<int,2>> q;
    q.push({0,0});
    int mina;
    for(int i = 0; i < 2*n-1;i++){
        mina = 26;
        vector<array<int,3>> temp;
        while(!q.empty()){
            auto [x,y] = q.front();q.pop();
            for(int dir = 0;dir < 2;dir++){
                int nx = x + dir;
                int ny = y + 1-dir;

                if (nx >= n || ny >= n || vis[nx][ny]) continue;

                vis[nx][ny] = 1;
                mina = min(mina,mat[nx][ny] - 'A');
                temp.pb({nx,ny,dir});
            }
        }

        for(auto [x,y,d] : temp){
            if(mina == mat[x][y] - 'A'){
                q.push({x,y});
                p[x][y] = d;
            }
        }
    }

    int x = n-1,y = n-1;
    string ans;

    while(x!=0 || y!=0){
        ans += mat[x][y];
        int d = p[x][y];
        x -= d;
        y -= 1-d;
    }

    ans += mat[0][0];
    reverse(all(ans));
    cout << ans;
    
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