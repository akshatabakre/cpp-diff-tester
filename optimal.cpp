#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--) {
        int n;
        cin >> n;
        vector<int>a(n);
        for(int i=0;i<n;i++) cin >> a[i];
        
        //testing crash
        // int *p = nullptr;
        // cout << *p << endl;


        int cur = 0, best = INT_MIN;
        for(int x : a){
            cur += x;
            best = max(best, cur);
            // if(cur < 0) cur = 0;
        }
        cout << best << endl;
    }
}
