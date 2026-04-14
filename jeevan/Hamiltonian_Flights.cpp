#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const double PI = 3.14159265358979323846;
const double E = 2.718281828459045;
const ll INF = 1000000000000000000;
const ll MOD1 = 1000000007;
const ll MOD2 = 998244353;

int n, m;
vector<vector<ll>> a;
int dp[1<<20][20];

ll dfs(int mask, int u) {
    if (dp[mask][u] != -1) {
        return dp[mask][u];
    }

    if (u == n - 1) {
        if (mask == (1 << n) - 1) return 1;
        return 0;
    }

    ll res = 0;
    for (int v = 0; v < n; v++) {
        if (!(mask & (1 << v)) && a[u][v]) {
            res = (res + (a[u][v] * dfs(mask | (1 << v), v)) % MOD1) % MOD1;
        }
    }

    dp[mask][u] = res;
    return res;
}

void solve() {
    cin >> n >> m;
    memset(dp,-1,sizeof(dp));

    a.assign(n + 1, vector<ll>(n + 1, 0));

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        a[u - 1][v - 1] += 1;
    }

    cout << dfs(1,0) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    // cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}