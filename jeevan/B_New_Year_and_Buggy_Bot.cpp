#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(){
    int n,m,ans,x,y,endx,endy,uio = 1;
    string route;

    ans = 0;
    cin >> n >> m;
    vector< vector<char> > mat;

    for (int i = 0; i < n; i++){
        vector<char> row;
        for (int j = 0; j < m; j++){
            // cout << j << endl;
            char s;
            cin >> s;
            row.push_back(s);
            // cout << s << " ";
            if (s == 'S'){
                x = i;
                y = j;
                // cout << x << " " << y << endl;
            }
        }
        mat.push_back(row);
    }
    // cout << mat[4][3] << x << " " << y << endl;
    cin >> route;
    // cout << route << endl;

    // d,l,u,r
    vector<char> raw(4);
    raw[0] = 'D';
    raw[1] = 'L';
    raw[2] = 'U';
    raw[3] = 'R';

    // while (true){
    //     int tempi = x,tempj = y;
    //     for (int b = 0; b < route.size(); b++){
    //         if (raw[b] == "U"){
    //             tempj++;
    //         }else if(raw[b] == "D"){
    //             tempj--;
    //         }else if(raw[b] == "R"){
    //             tempi++;
    //         }else if(raw[b] == "L"){
    //             tempi--;
    //         }
    //         if (tempi >= 0 && tempi < m && tempj >= 0 && tempj < n && mat[tempi][tempj] != "E"){
    //             ans++;
    //         }
    //     }
    //     next_permutation(raw.begin(), raw.end())
    // }

    int tempi = x,tempj = y;
    for (int b = 0; b < route.size(); b++){
        // int uio = stoi(route[b]);


        if (route[b] == '1'){uio = 1;}
        if (route[b] == '2'){uio = 2;}
        if (route[b] == '3'){uio = 3;}
        if (route[b] == '4'){uio = 4;}



        if (raw[uio] == 'U'){
            tempj++;
        }else if(raw[uio] == 'D'){
            tempj--;
        }else if(raw[uio] == 'R'){
            tempi++;
        }else if(raw[uio] == 'L'){
            tempi--;
        }
        cout << tempi << " " << tempj << " " << uio << endl;
        if (tempi >= 0 && tempi < m && tempj >= 0 && tempj < n && mat[tempi][tempj] == 'E'){
            ans++;
            continue;
        }
    }

    // do{
    //     int tempi = x,tempj = y;
    //     for (int b = 0; b < route.size(); b++){
    //         if (raw[b] == "U"){
    //             tempj++;
    //         }else if(raw[b] == "D"){
    //             tempj--;
    //         }else if(raw[b] == "R"){
    //             tempi++;
    //         }else if(raw[b] == "L"){
    //             tempi--;
    //         }
    //         if (tempi >= 0 && tempi < m && tempj >= 0 && tempj < n && mat[tempi][tempj] == "E"){
    //             ans++;
    //             continue;
    //         }
    //     }
    // }
    // while (next_permutation(raw.begin(), raw.end()));
    cout << ans << endl;


}