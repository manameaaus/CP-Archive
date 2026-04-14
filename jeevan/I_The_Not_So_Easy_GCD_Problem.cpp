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



constexpr int MAXN = 200001;
int n,q;
int gcdc = 1;
int spf[MAXN];
vector<map<int,int>> prime_factorisation(MAXN);
map<int,multiset<int>> primes; 

void sp(){
    for (int i = 0;i < MAXN;i++){
        spf[i] = i;
    }
    for(int i = 2;i < MAXN;i++){
        if(spf[i] == i){
            for(int j = i*i;j < MAXN;j += i){
                spf[j] = min(spf[j],i);
            }
        }
    }
}


map<int,int> factorise(int num){
    map<int,int> factors;
    while (num > 1){
        factors[spf[num]]++;
        num /= spf[num];
    }
    return factors;
}


void run_query(int i,int x){
    map<int,int> new_factors = factorise(x);

    for (auto &[key, value] : new_factors) {
        
        int old,curr;
        old = primes[key].size() == n ? *(primes[key].begin()) : 0;
        

        if (prime_factorisation[i][key] == 0){
            primes[key].insert(value);
        }else{
            primes[key].erase(primes[key].find(prime_factorisation[i][key]));
            primes[key].insert(value + prime_factorisation[i][key]);
        }

        if (primes[key].size() == n){
            curr = *(primes[key].begin());
            gcdc = mod_mul(gcdc,mod_pow(key,curr-old));
        }

        prime_factorisation[i][key] += value;
    }

}


     


void solve() {
    cin >> n >> q;
    
    for(int i = 0;i < n;i++){
        int x;cin >> x;
        run_query(i,x);
    }

    for(int j = 0;j < q;j++){
        int i,x;cin >> i >> x;i--;

        run_query(i,x);
        cout << gcdc << endl;
    }


}

int32_t main(){
    // cout << fixed << setprecision(10);
    execute
    int t = 1;
    // cin >> t;
    sp();
    while (t--) {
        solve();
    }

    return 0;
}



// 1 
// 1 2 3
// 1 2
// 1 2 3