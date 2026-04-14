#include <bits/stdc++.h>
using namespace std;

// ---------- debug utilities ----------
#define cerr cout
namespace __DEBUG_UTIL__ { void print(const char *x) { cerr << x; } void print(bool x) { cerr << (x ? "T" : "F"); } void print(char x) { cerr << '\'' << x << '\''; } void print(signed short int x) { cerr << x; } void print(unsigned short int x) { cerr << x; } void print(signed int x) { cerr << x; } void print(unsigned int x) { cerr << x; } void print(signed long int x) { cerr << x; } void print(unsigned long int x) { cerr << x; } void print(signed long long int x) { cerr << x; } void print(unsigned long long int x) { cerr << x; } void print(float x) { cerr << x; } void print(double x) { cerr << x; } void print(long double x) { cerr << x; } void print(string x) { cerr << '\"' << x << '\"'; } template <size_t N> void print(bitset<N> x) { cerr << x; } void print(vector<bool> v) { int f = 0; cerr << '{'; for (auto &&i : v) cerr << (f++ ? "," : "") << (i ? "T" : "F"); cerr << "}"; } template <typename T> void print(T &&x); template <typename T> void print(vector<vector<T>> mat); template <typename T, size_t N, size_t M> void print(T (&mat)[N][M]); template <typename F, typename S> void print(pair<F, S> x); template <typename T, size_t N> struct Tuple; template <typename T> struct Tuple<T, 1>; template <typename... Args> void print(tuple<Args...> t); template <typename... T> void print(priority_queue<T...> pq); template <typename T> void print(stack<T> st); template <typename T> void print(queue<T> q); template <typename T> void print(T &&x) { int f = 0; cerr << '{'; for (auto &&i : x) cerr << (f++ ? "," : ""), print(i); cerr << "}"; } template <typename T> void print(vector<vector<T>> mat) { int f = 0; cerr << "\n~~~~~\n"; for (auto &&i : mat) { cerr << setw(2) << left << f++, print(i), cerr << "\n"; } cerr << "~~~~~\n"; } template <typename T, size_t N, size_t M> void print(T (&mat)[N][M]) { int f = 0; cerr << "\n~~~~~\n"; for (auto &&i : mat) { cerr << setw(2) << left << f++, print(i), cerr << "\n"; } cerr << "~~~~~\n"; } template <typename F, typename S> void print(pair<F, S> x) { cerr << '('; print(x.first); cerr << ','; print(x.second); cerr << ')'; } template <typename T, size_t N> struct Tuple { static void printTuple(T t) { Tuple<T, N - 1>::printTuple(t); cerr << ",", print(get<N - 1>(t)); } }; template <typename T> struct Tuple<T, 1> { static void printTuple(T t) { print(get<0>(t)); } }; template <typename... Args> void print(tuple<Args...> t) { cerr << "("; Tuple<decltype(t), sizeof...(Args)>::printTuple(t); cerr << ")"; } template <typename... T> void print(priority_queue<T...> pq) { int f = 0; cerr << '{'; while (!pq.empty()) cerr << (f++ ? "," : ""), print(pq.top()), pq.pop(); cerr << "}"; } template <typename T> void print(stack<T> st) { int f = 0; cerr << '{'; while (!st.empty()) cerr << (f++ ? "," : ""), print(st.top()), st.pop(); cerr << "}"; } template <typename T> void print(queue<T> q) { int f = 0; cerr << '{'; while (!q.empty()) cerr << (f++ ? "," : ""), print(q.front()), q.pop(); cerr << "}"; } void printer(const char *) {} template <typename T, typename... V> void printer(const char *names, T &&head, V &&...tail) { int i = 0; for (int bracket = 0; names[i] != '\0' and (names[i] != ',' or bracket > 0); i++) if (names[i] == '(' or names[i] == '<' or names[i] == '{') bracket++; else if (names[i] == ')' or names[i] == '>' or names[i] == '}') bracket--; cerr.write(names, i) << " = "; print(head); if (sizeof...(tail)) cerr << " ||", printer(names + i + 1, tail...); else cerr << "]\n"; } }
#ifndef ONLINE_JUDGE
#define debug(...) cerr << __LINE__ << ": [", __DEBUG_UTIL__::printer(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...)
#endif

// ---------- shortcut macros ----------
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(x) (int)(x).size()

#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, a, b) for (int i = (a); i <= (b); ++i)
#define per(i, n) for (int i = (n) - 1; i >= 0; --i)
#define per1(i, a, b) for (int i = (b); i >= (a); --i)

// ---------- type aliases ----------
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

// ---------- input macros ----------
#define input_vec(v, n) vi v(n); rep(i, n) cin >> v[i]
#define input_vec_str(v, n) vector<string> v(n); rep(i, n) cin >> v[i]
#define read_vec(v) for (auto &x : v) cin >> x
#define read_vec_str(v) for (auto &s : v) cin >> s



map<int, pair<vector<pii>, vector<pii>>> buildSortedSideMap(const vi &arr) {
    int n = arr.size();
    map<int, pair<vector<pii>, vector<pii>>> res;

    multiset<pii> left, right;

    for (int i = 1; i < n; ++i)
        right.insert({arr[i], i});

    rep(i, n) {
        vector<pii> l(left.begin(), left.end());
        vector<pii> r(right.begin(), right.end());

        res[i] = {l, r};

        if (i + 1 < n)
            right.erase(right.find({arr[i + 1], i + 1}));
        left.insert({arr[i], i});
    }

    return res;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vi a(n);
        read_vec(a);

        int ans = 1e8;
        bool done = false;


        // auto result = buildSortedSideMap(a);





        rep(i, n) {
            if(done) break;
            int x = a[i];
            vi vals = {x - 1, x, x + 1};
            int cur = 1e8;

            rep(k, 1) {
                if((i < n - 1 && abs(a[i]-a[i + 1]) <= 1) || (i > 0 && abs(a[i] - a[i - 1]) <= 1)) {
                    ans = 0;
                    done = true;
                    break;
                }
            }

            // if (a)
            // cout << "fcf " << i << endl;
            bool fwd = false;
            rep1(j, i + 1, n - 2) {
                // int l = min(a[j], a[j + 1]);
                // int r = max(a[j], a[j + 1]);

                int l=a[j],r=a[j+1];
                if(l > r) swap(l, r);


                // cout << cur << " " << i << " " << j << endl;

                if ((vals[0] >= l && vals[0] <= r) || (vals[1] >= l && vals[1] <= r) || (vals[2] >= l && vals[2] <= r)){
                    cur = min(cur, j - i);
                    // cout << "fcf " << i << endl;
                    // cout << cur << " " << i << " " << j << endl;

                    fwd = true;
                    // break;
                }
                // rep(k, 3) {
                //     if(vals[k] >= l && vals[k] <= r) {
                //         cur = min(cur, j - i);
                //         fwd = true;
                //         break;
                //     }
                // }

                // cout << cur << endl;
                if(fwd) break;


            }

            // bool bwd = false;
            // per1(j, 1, i - 1) {
            //     int l = min(a[j], a[j - 1]);
            //     int r = max(a[j], a[j - 1]);


            //     if ((vals[0] >= l && vals[0] <= r) || (vals[1] >= l && vals[1] <= r) || (vals[2] >= l && vals[2] <= r)){
            //         cur = min(cur, i - j);
            //         bwd = true;
            //         // cout << cur << " " << i << " " << j << endl;
            //         // break;
            //     }

            //     // rep(k, 3) {
            //     //     if(vals[k] >= l && vals[k] <= r) {
            //     //         cur = min(cur, i - j);
            //     //         bwd = true;
            //     //         break;
            //     //     }
            //     // }
            //     if(bwd) break;
            // }


            ans = min(ans, cur);
            // cout << cur << " " << i << " " << ans <<endl;

        }

        // cout << ans << endl;

        if(ans == 1e8) cout << -1 << '\n';
        else cout << ans << '\n';
    }
}
