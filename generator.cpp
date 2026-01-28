#include <bits/stdc++.h>
using namespace std;

int main() {
    srand(time(0));

    int n = rand() % 10 + 1;
    cout << n << endl;
    for(int i=0;i<n;i++){
        int x = rand() % 20 - 10;
        cout << x << " ";
    }
    cout << endl;
}
