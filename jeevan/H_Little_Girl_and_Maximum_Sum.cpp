#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
 
int main() {
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a.rbegin(), a.rend());
 
    vector<int> freq(n + 1, 0);
    for (int i = 0; i < q; ++i) {
        int x, y;
        cin >> x >> y;
        freq[x - 1]++;
        freq[y]--;
    }
 
    for (int i = 1; i < n; ++i) {
        freq[i] += freq[i - 1];
    }
 
    freq.pop_back();
    sort(freq.rbegin(), freq.rend());
 
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += (long long)freq[i] * a[i];
    }
 
    cout << ans << endl;
    return 0;
}