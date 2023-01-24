#include <bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include "algo/debug.h"
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

#define int long long

void swap(int *xp, int *yp) {
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

int ans = 0;
void selectionSort(vector<int> &arr, int n) {
	int min_idx;

	for (int i = 0; i < n - 1; i++) {
		min_idx = i;
		for (int j = i + 1; j < n; j++)
			if (arr[j] < arr[min_idx]) {
				min_idx = j;
			}

		if (min_idx != i) {
			swap(&arr[min_idx], &arr[i]);
			ans++;
		}
	}
}

void merge(vector<int> &array, int const left, int const mid, int const right) {
	auto const a1 = mid - left + 1;
	auto const a2 = right - mid;

	auto *lArr = new int[a1],
	*rArr = new int[a2];

	for (auto i = 0; i < a1; i++) {
		lArr[i] = array[left + i];
	}
	for (auto j = 0; j < a2; j++) {
		rArr[j] = array[mid + 1 + j];
	}

	auto indexOfa1 = 0, indexOfa2 = 0;
	int iMerged = left;

	while (indexOfa1 < a1 && indexOfa2 < a2) {
		if (lArr[indexOfa1] <= rArr[indexOfa2]) {
			array[iMerged] = lArr[indexOfa1];
			indexOfa1++;
		}
		else {
			array[iMerged] = rArr[indexOfa2];
			indexOfa2++;
			ans++;
		}
		iMerged++;
	}
	while (indexOfa1 < a1) {
		array[iMerged] = lArr[indexOfa1];
		indexOfa1++;
		iMerged++;
	}
	while (indexOfa2 < a2) {
		array[iMerged] = rArr[indexOfa2];
		indexOfa2++;
		iMerged++;
	}
	// delete[] lArr;
	// delete[] rArr;
}
void mergeSort(vector<int> &array, int const begin, int const end)
{
	if (begin >= end){
		return;
	}

	auto mid = begin + (end - begin) / 2;
	mergeSort(array, begin, mid);
	mergeSort(array, mid + 1, end);
	merge(array, begin, mid, end);
}
void solve() {
	vector<int> a = {28999, 1600, 1100, 1400, 800, 1200, 2300, 669, 3600, 1, 186, 299, 25, 3300, 2599, 1008, 900, 169, 607, 1280};
	auto dup = a;

	selectionSort(a, a.size());

	for (auto &x : a) {
		cout << x << " ";
	}
	cout << "\n";
	cout << ans << "\n";
	ans = 0;
	a = dup;

	mergeSort(a, 0, a.size() - 1);

	for (auto &x : a) {
		cout << x << " ";
	}
	cout << "\n";
	cout << ans << "\n";

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

