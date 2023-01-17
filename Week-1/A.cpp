#include <bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include "algo/debug.h"
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

#define int long long

int  ceilD(int a, int b) {
	return (a + b - 1) / b;
}
void solve() {
	vector<int> a;

	for (int i = 0, x; i < 3; i++) {
		cin >> x;
		a.push_back(x);
	}

	cout << "Q1\n";
	int i = 0;
	do {
		i++;
		cout << i << "Permutation: ";
		for (auto &x : a) {
			cout << x << " ";
		}
		cout << "\n";
	} while (next_permutation(a.begin(), a.end()));

	int mean = 0;

	for (auto x : a) {
		int sm = 0;
		while (x > 0) {
			sm += x % 10;
			x /= 10;
		}
		mean += sm;
	}
	cout << "Q2\n";

	cout << "The mean of the array is :";
	cout << mean / 27. << "\n";


	cout << "The Rounded-mean of the array is :";
	cout << mean / 27 << " or " << ceilD(mean, 27) << "\n";

	int rMean = mean / 27;
	cout << "Q3\n";

	do {
		i = 0;
		for (auto x : a) {
			int id = 0;
			while (x > 0) {
				int zz = x % 10;
				x /= 10;

				if (zz == rMean) {
					cout << i * 9 + 9 - id - 1 << " ";
				}
				id++;
			}
			i++;
		}

		cout << "\n";

	} while (next_permutation(a.begin(), a.end()));



	vector<int> aa = {2, 0, 0, 1, 0, 8, 0, 0, 5, 2, 0, 0, 1, 0, 8, 0, 1, 1, 2, 0, 0, 1, 0, 8, 0, 6, 1};

	sort(aa.begin(), aa.end());
	cout << "Q4\n";
	for (auto x : aa) {
		cout << x << " ";
	}
	cout << "\n";

	int l = 0, r = 27;


	while (r - l > 1) {
		int md = (r + l) >> 1;
		if (aa[md] == rMean) {
			r = md;
		} else if (aa[md] > rMean) {
			r = md - 1;
		}
		else {
			l = md + 1;
		}
	}
	cout << "Q5\n\n";
	for (i = r; i < 27; i++) {
		if (aa[i] != rMean) {
			break;
		}
		cout << i << "\n";
	}
}

signed main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
#endif
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int t = 1;
	//cin >> t;

	while (t--) {
		solve();
	}

	// cerr << "Time elapsed: " << ((long double)clock() / CLOCKS_PER_SEC) << " s.\n";
}

