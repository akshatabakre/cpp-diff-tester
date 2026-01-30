#include <bits/stdc++.h>
using namespace std;

int main() {
    srand(time(0));
    ifstream fin("constraints.txt");

    string var;
    int T_min, T_max;
    fin >> var >> T_min >> T_max;

    int T = rand() % (T_max - T_min + 1) + T_min;
    cout << T << endl;

    string n_var;
    int n_min, n_max;
    fin >> n_var >> n_min >> n_max;

    string arr, size_var;
    int a_min, a_max;
    fin >> arr >> size_var >> a_min >> a_max;

    for(int tc = 0; tc < T; tc++) {
        int n;
        int mode = rand() % 5;

        if(mode == 0) n = n_min;
        else if(mode == 1) n = n_max;
        else n = rand() % (n_max - n_min + 1) + n_min;

        cout << n << endl;

        for(int i = 0; i < n; i++) {
            int x;
            if(mode == 2) x = 0;
            else if(mode == 3) x = a_min;
            else if(mode == 4) x = a_max;
            else x = rand() % (a_max - a_min + 1) + a_min;

            cout << x << " ";
        }
        cout << endl;
    }
}
