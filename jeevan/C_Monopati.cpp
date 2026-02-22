#include <bits/stdc++.h>
using namespace std;

/* INPUT */
#define vin(v, n)  for (int i = 0; i < n; ++i) cin >> v[i];

/* TYPES  */
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>


/* FUNCTIONS */
#define f(i,s,e) for(long long int i=s;i<e;i++)
#define cf(i,s,e) for(long long int i=s;i<=e;i++)
#define rf(i,e,s) for(long long int i=e;i>=s;i--)
#define all(v) v.begin(), v.end()
#define allr(v) v.rbegin(), v.rend()
#define bpc(x) __builtin_popcount(x)
#define pb push_back
#define eb emplace_back

/* PRINTS */
template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}";}

const ll MOD = 1e9+7 ;
ll tt=0;

void solve(){
    tt++;
    ll n;
    cin>>n;
    vll vo(n);
    vin(vo,n);
    vll vt(n);
    vin(vt,n);

    vector<array<ll,2>> mimao(n,{0,0});
    vector<array<ll,2>> mimat(n,{0,0});

    mimao[0]={vo[0], vo[0]};
    mimat[n-1]={vt[n-1], vt[n-1]};
    f(i,1,n){
        mimao[i][0]=min(vo[i], mimao[i-1][0]);
        mimao[i][1]=max(vo[i], mimao[i-1][1]);
    }
    
    rf(i,n-2,0){
        mimat[i][0]=min(vt[i], mimat[i+1][0]);
        mimat[i][1]=max(vt[i], mimat[i+1][1]);
    }
    // for(auto i:mimao){
    //     cout<<i[0]<<" "<<i[1]<<"\n";
    // }
    ll p=0,q=LLONG_MAX;
    ll ans=0;
    vector<array<ll,2>> st;
    f(i,0,n){
        if(tt==9222){
            cout<<vo[i]<<"."<<vt[i]<<",";
        }
        ll x = min(mimao[i][0], mimat[i][0]);
        ll y = max(mimao[i][1], mimat[i][1]);
        st.pb({x,y});
        // cout<<x<<" "<<y<<"\n";
    }

    sort(all(st));
    vector<array<ll,2>> fin;
    fin.pb({0,0});
    for(auto i:st){
        if(fin.size()){
            if(fin.back()[0]==i[0]) {;;continue;};
            if(fin.back()[0]<=i[0] && fin.back()[1]>=i[1]) {
                fin.pop_back();
                fin.pb({i[0], i[1]});
                continue;
            }
            fin.pb({i[0],i[1]});
            continue;
        }
        fin.pb({i[0],i[1]});
    }

    for(auto dabba:fin){
        cout << dabba[0] << " " << dabba[1] << endl;
    }
    cout << endl;
    f(i,1,fin.size()){
        ans+= (fin[i][0]-fin[i-1][0])*(2*n-fin[i][1]+1);
    }
    cout<<ans<<"\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    ll t;
    cin>>t;
    while(t--){
        solve();
    }
}