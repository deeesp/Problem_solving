#include <iostream>

using namespace std;

int lab[8][8], copied_lab[8][8];
int N, M, max = 0;

void input();
void Wall_dfs(int depth);
void copyLab();
void check(int a, int b);
void sum();

int main() {
	input();
	Wall_dfs(0);
	printf("%d", max);
}

void input() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> lab[i][j];
		}
	}
}

void Wall_dfs(int depth) {
	if (depth == 3) {
		copyLab();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (copied_lab[i][j] == 2) {
					check(i, j);
				}
			}
		}
		sum();
		return;
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (lab[i][j] == 0) {
				lab[i][j] = 1;
				Wall_dfs(depth + 1);
				lab[i][j] = 0;
			}
		}
	}
}

void copyLab() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			copied_lab[i][j] = lab[i][j];
		}
	}
}

void check(int a, int b) {
	if (copied_lab[a][b + 1] == 0 && b<M - 1){ //right
		copied_lab[a][b + 1] = 2;
		check(a, b + 1);
	}
	if (copied_lab[a][b - 1] == 0 && b>0){ //left
		copied_lab[a][b - 1] = 2;
		check(a, b - 1);
	}
	if (copied_lab[a + 1][b] == 0 && a<N - 1){ //down
		copied_lab[a + 1][b] = 2;
		check(a + 1, b);
	}
	if (copied_lab[a - 1][b] == 0 && a>0){ //up
		copied_lab[a - 1][b] = 2;
		check(a - 1, b);
	}
}

void sum() {
	int sum = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (copied_lab[i][j] == 0) {
				sum++;
			}
		}
	}

	if (max < sum) {
		max = sum;
	}
}
