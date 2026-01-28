// #include <bits/stdc++.h>
// using namespace std;

// // ---------- debug utilities ----------
// // template<typename... Args>

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
// // void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

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



// void solve() {
//     string text1,text2,text3;
//     cin >> text1 >> text2 >> text3;

//     int n,m;
//     n = text1.size();
//     m = text2.size();

//     vector<vector<int>> mat(n+1,vector<int>(m+1,0));


//     for(int i = 1;i <= n;i++){
//         for(int j = 1;j <= m;j++){
//             mat[i][j] = max(mat[i-1][j],mat[i][j-1]);
//             if (text1[i-1] == text2[j-1]){
//                 mat[i][j] = max(mat[i-1][j-1]+1,mat[i][j]);
//             }
//         }
//     }

//     int i = n,j = m;
//     string s1,s2;s1 = text1;s2 = text2;
//     string ans = "";
//     while (i > 0 && j > 0){
        
//         if (s1[i-1] == s2[j-1]){
//             ans+=s1[i-1];
//             i--;
//             j--;
//         }else{
//             if (mat[i-1][j] > mat[i][j-1]){
//                 i--;
//             }else{
//                 j--;
//             }
//         }
//     }
//     // cout << ans << endl;

//     reverse(ans.begin(),ans.end());
//     text1 = ans;


//     n = text1.size();
//     m = text3.size();

//     vector<vector<int>> mat1(n+1,vector<int>(m+1,0));

//     int ans1 = 0;

//     for(int i = 1;i <= n;i++){
//         for(int j = 1;j <= m;j++){
//             mat1[i][j] = max(mat1[i-1][j],mat1[i][j-1]);
//             if (text1[i-1] == text3[j-1]){
//                 mat1[i][j] = max(mat1[i-1][j-1]+1,mat1[i][j]);
//             }
//             ans1 = max(ans1,mat1[i][j]);
//         }
//     }

//     cout << ans1 << endl;



//     // print2(mat);

    
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
// template<typename... Args>

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
// void print(Args&&... args) {((cout << args << " "), ...);cout << '\n';}

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
    string x_axis,y_axis,z_axis;

    cin >> x_axis >> y_axis >> z_axis;

    int n,m,p; n = len(x_axis);m = len(y_axis);p = len(z_axis);

    int dp[101][101][101];
    memset(dp,0,sizeof dp);
    int ans = 0;

    for(int i = 1;i < n+1;i++){
        for(int j = 1;j < m+1;j++){
            for (int k = 1; k < p+1; k++){
                dp[i][j][k] = max(dp[i][j][k-1],max(dp[i][j-1][k],dp[i-1][j][k]));
                if (x_axis[i-1] == y_axis[j-1] && y_axis[j-1] == z_axis[k-1]){
                    dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k-1]+1);
                }
                ans = max(ans,dp[i][j][k]);
            }
        }
    }

    cout << ans << endl;
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