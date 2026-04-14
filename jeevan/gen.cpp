#include <bits/stdc++.h>
using namespace std;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

vector<int> sieve_primes(int N) {
    vector<bool> isPrime(N+1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= N; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= N; j += i)
                isPrime[j] = false;
        }
    }
    vector<int> primes;
    for (int i = 2; i <= N; i++)
        if (isPrime[i]) primes.push_back(i);
    return primes;
}

// Try to combine two expressions safely
bool try_combine(string &out, const string &a, const string &b,
                 char op, int maxLen) {
    string cand = "(" + a + op + b + ")";
    if ((int)cand.size() > maxLen) return false;
    out = cand;
    return true;
}

// Create a random constant 0..9
string random_constant() {
    char d = char('0' + (rng() % 10));
    return string(1, d);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string mode;   // easy, medium, hard
    cin >> mode;

    const int MAXLEN = 300;

    // Precompute primes
    vector<int> primes = sieve_primes(14999);
    int P = primes.size();

    int lo, hi;
    int maxVars;
    int maxOps;
    int maxExp;
    int constProb; // % chance to inject a constant

    if (mode == "easy") {
        lo = 0; hi = min(50, P-1);
        maxVars = 4;
        maxOps = 4;
        maxExp = 2;
        constProb = 10;
    } else if (mode == "medium") {
        lo = min(300, P-1);
        hi = min(700, P-1);
        maxVars = 10;
        maxOps = 10;
        maxExp = 3;
        constProb = 25;
    } else { // hard
        lo = min(1500, P-1);
        hi = P-1;
        maxVars = 26;
        maxOps = 25;
        maxExp = 4;
        constProb = 40;
    }

    uniform_int_distribution<int> distP(lo, hi);
    int p = primes[distP(rng)];
    cout << p << "\n";

    // ---- VARIABLE POOL (unique) ----
    vector<char> allVars;
    for (char c = 'a'; c <= 'z'; c++) allVars.push_back(c);
    shuffle(allVars.begin(), allVars.end(), rng);

    vector<string> varPool;
    for (int i = 0; i < maxVars; i++) {
        varPool.push_back(string(1, allVars[i]));
    }

    // Initial expressions = variables only (unique)
    vector<string> exprs = varPool;

    int ops = 0;

    while (exprs.size() >= 2 && ops < maxOps) {
        int i = rng() % exprs.size();
        int j = rng() % exprs.size();
        if (i == j) continue;
        if (i > j) swap(i, j);

        string a = exprs[i];
        string b = exprs[j];

        char op = (rng() % 100 < 50 ? '*' : '+');

        string combined;
        if (!try_combine(combined, a, b, op, MAXLEN))
            break;

        // ---- Optional exponentiation ----
        if (mode != "easy" && (rng() % 100) < 30) {
            int e = 2 + (rng() % maxExp);
            string expCand = "(" + combined + "^" + to_string(e) + ")";
            if ((int)expCand.size() <= MAXLEN) {
                combined = expCand;
            }
        }

        // ---- Optional constant injection ----
        if ((rng() % 100) < constProb) {
            string cst = random_constant();
            char cop = (rng() % 2 ? '+' : '*');
            string withConst;
            if (try_combine(withConst, combined, cst, cop, MAXLEN)) {
                combined = withConst;
            }
        }

        // Replace
        exprs.erase(exprs.begin() + j);
        exprs.erase(exprs.begin() + i);
        exprs.push_back(combined);

        ops++;
    }

    // Final linear combining if needed
    while (exprs.size() > 1) {
        string a = exprs.back(); exprs.pop_back();
        string b = exprs.back(); exprs.pop_back();

        string combined;
        if (!try_combine(combined, a, b, '*', MAXLEN)) {
            exprs.push_back(a);
            break;
        }
        exprs.push_back(combined);
    }

    string final_expr = exprs[0];

    // Safety trim (should almost never trigger)
    if ((int)final_expr.size() > MAXLEN) {
        final_expr = final_expr.substr(0, MAXLEN-1);
        final_expr.push_back(')');
    }

    cout << final_expr << "\n";
    return 0;
}
