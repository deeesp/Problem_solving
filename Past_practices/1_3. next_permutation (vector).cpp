#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n;
vector <int> v;

void print_arr() {
	for (int i = 0; i < n; i++)
		cout << v[i] << " ";
	cout << "\n";
}

int main() {
	cin >> n;
	v.resize(n);
	for (int i = 0; i < n; i++)
		v[i] = i + 1;

	do
		print_arr();
	while (next_permutation(v.begin(), v.end()));
}