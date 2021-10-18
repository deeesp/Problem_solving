#include <iostream>
#include <vector>
#include <string>

using namespace std;

int N, max = -999999, min = 999999;
vector <int> num, operation(4);

void DFS(int a, int b);

int main() {
	cin >> N;
	num.resize(N);
	for (int i = 0; i < N; i++)
		cin >> num[i];

	for (int i = 0; i < 4; i++)
		cin >> operation[i];
	
	DFS(1, num[0]);

	cout << max << "\n" << min << "\n";

}
void DFS(int a, int b) {

	if (a == N){
		min = min < b ? min : b;
		max = max > b ? max : b;
		return;
	}

	if (operation[0]) {
		--operation[0];
		DFS(a + 1, b + num[a]);
		++operation[0];
	}
	if (operation[1]) {
		--operation[1];
		DFS(a + 1, b - num[a]);
		++operation[1];
	}
	if (operation[2]) {
		--operation[2];
		DFS(a + 1, b * num[a]);
		++operation[2];
	}
	if (operation[3]) {
		--operation[3];
		DFS(a + 1, b / num[a]);
		++operation[3];
	}

}