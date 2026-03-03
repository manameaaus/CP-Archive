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

// int dp[1001][2];
// // 0 -> length;
// // 1 -> nooflis;
// int arr[1001];


// void solve() {
//     int n;
//     cin >> n;
//     memset(dp,0,sizeof dp);
//     memset(arr,0,sizeof dp);

//     int upper = 0;

//     for(int i = 1;i <= n;i++){
//         cin >> arr[i];
//         upper = max(upper,arr[i]);
//     }

//     dp[0][1] = 1;
//     arr[n+1] = upper + 1;
//     int maxa = 0;
//     int ulti = 0;
//     for(int i = 1;i <= n+1;i ++){
//         maxa = 0;
//         for (int j = i-1;j >= 0;j--){
//             // print(arr[i],arr[j],i,j);
//             if (arr[j] < arr[i]){
//                 maxa = max(maxa,dp[j][0]);
//                 // if (i == 2 && j == 1){
//                 //     print(maxa,i,j);
//                 // }
//             }
//             // print(ulti,maxa,i);

//         }
//         ulti = max(ulti,maxa);
//         dp[i][0] = maxa+1;
//         for (int j = i-1;j >= 0;j--){
//             if (arr[j] < arr[i] && dp[j][0] == maxa){
//                 dp[i][1] += dp[j][1];
//             }
//         }
//     }
//     print(dp[n+1][1]);
//     // print2(dp);
// }

// int32_t main(){
//     // cout << fixed << setprecision(10);
//     JBR_CP_1000101
//     int t = 1;
//     cin >> t;
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

ll mod_mul(ll a,ll b) {return ((a % MOD) * (b % MOD)) % MOD;}
ll mod_add(ll a,ll b) {return ((a % MOD) + (b % MOD)) % MOD;}
ll mod_sub(ll a,ll b) {return ((a % MOD) - (b % MOD) + MOD) % MOD;}
ll mod_pow(ll a,ll b, ll m = MOD) {ll res = 1;a %= m;while (b) {if (b & 1ll) res = res * a % m;a = mod_mul(a, a);b >>= 1ll;}return res;}
ll mod_inv(ll a, ll m = MOD) {return mod_pow(a, m - 2, m);}  // fermat's little theorem
ll mod_div(ll a, ll b) {return mod_mul(a, mod_inv(b));}
ll gcd(ll a, ll b) {return b ? gcd(b, a % b) : a;}
ll lcm(ll a, ll b) {return a * b / gcd(a, b);}

int dp[1001][2];
// 0 -> length;
// 1 -> nooflis;
int arr[1001];


// void solve() {
//     int n; 
//     cin >> n;
//     invi(arr, n);

//     for (int i = 0; i < n; i++) {
//         dp[i][0] = 1;   // length of LIS ending at i is at least 1
//         dp[i][1] = 1;   // one such subsequence
//     }

//     int max_len = 1;

//     for (int i = 1; i < n; i++) {
//         for (int j = 0; j < i; j++) {
//             if (arr[j] < arr[i]) {
//                 if (dp[j][0] + 1 > dp[i][0]) {
//                     dp[i][0] = dp[j][0] + 1;
//                     dp[i][1] = dp[j][1];
//                 } else if (dp[j][0] + 1 == dp[i][0]) {
//                     dp[i][1] = mod_add(dp[i][1], dp[j][1]);
//                 }
//             }
//         }
//         max_len = max(max_len, dp[i][0]);
//     }

//     int ans = 0;
//     for (int i = 0; i < n; i++) {
//         if (dp[i][0] == max_len) {
//             ans = mod_add(ans, dp[i][1]);
//         }
//     }

//     cout << ans << "\n";
// }



void solve() {
    int n;
    cin >> n;
    memset(dp,0,sizeof dp);
    memset(arr,0,sizeof arr);

    for(int i = 1;i <= n;i++){
        cin >> arr[i];
    }

    dp[0][1] = 1;
    int ulti = 0;
    for(int i = 1;i <= n;i ++){
        for (int j = i-1;j >= 0;j--){
            if (arr[j] < arr[i]){
                if (dp[i][0] < dp[j][0]+1){
                    dp[i][0] = dp[j][0]+1;
                    dp[i][1] = dp[j][1];
                }else if(dp[i][0] == dp[j][0]+1){
                    dp[i][1] = mod_add(dp[i][1],dp[j][1]);
                }
            }
        }
        ulti = max(ulti,dp[i][0]);
    }

    int ans = 0;
    for(int i = 1;i <= n;i++){
        if (dp[i][0] == ulti){
            ans = mod_add(ans,dp[i][1]);
        }
    }
    print(ans);
}

int32_t main(){
    // cout << fixed << setprecision(10);
    JBR_CP_1000101
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}