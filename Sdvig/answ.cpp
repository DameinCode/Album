#include <bits/stdc++.h>
using namespace std;
int main() {
    string n;
    cin >> n;
    int reg;
    cout << "Register: ";
    cin >> reg;   
    vector<int> vec;
    vector<int> ne;
    for(int i = 0; i < n.size(); i++) {
        if(n[i] == '1'){
            vec.push_back(1);
        } else {
            vec.push_back(0);
        }
    }

    int a[reg+1][reg+1];
    for(int i = 0; i < reg+1; i++) {
        for(int j = i, c = 0; j < i+reg+1, c < reg+1; j++, c++) {
            if(c != reg)
                a[i][c] = vec[j];
            else 
                ne.push_back(vec[j]);
        }
    }
    cout << "   To solve: \n";
    for(int i = 0; i < reg+1; i++) {
        for(int j = 0; j < reg; j++) {
            cout << a[i][j] << " ";
        } cout << "  " << ne[i] << "\n";
    }

    cout << "    ANSWER:             \n";
    bool ok = false;
    for(int i = 0; i < reg+1; i++) {
        bool ok = false;
        if(a[i][i] != 1) {
            for(int c = i; c < reg; c++) {
                if(a[c][i] == 1) {
                    ok = true; 
                    for(int k = 0; k < reg; k++) {
                        a[i][k] ^= a[c][k];
                    } 
                    ne[i] = ne[c]^ne[i];
                    break;
                } 
            } 
            if(!ok) {
                for(int c = 0; c < i; c++) {
                    if(a[c][i] == 1) {
                        for(int k = 0; k < reg; k++) {
                            a[i][k] ^= a[c][k];
                        } 
                        ne[i] = ne[c]^ne[i];
                        break;
                    }
                }
            }
        } 
        if (a[i][i] == 1) {
            for(int u = 0; u < reg+1; u++) {
                if(u == i) {
                    continue;
                } 
                else if(a[u][i] == 1) {
                    for(int k = 0; k < reg; k++) {
                        a[u][k] = (a[u][k]^a[i][k]);
                    } 
                    ne[u] = (ne[u]^ne[i]);
                }
            }
        }
    }
    int ans = reg;
    for(int i = 0; i < reg; i++) {
        for(int j = 0; j < reg; j++) {
            cout << a[i][j] << " ";
        } cout << "  " << "X" << ans << " = " << ne[i] << "\n";
        ans --;
    }

    return 0;
}