// nPr 순열
// n = r 

#include <iostream>

using namespace std;

int arr[] = { 1,2,3,4,5 };


void swap(int *a, int *b);
void print_arr();
void permutation(int n, int r);

int main() {
	permutation(sizeof(arr) / sizeof(int), sizeof(arr) / sizeof(int));
	return 0;
}


void swap(int *a, int *b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}

void print_arr() {
	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
		cout << arr[i];
	cout << "\n";
}

void permutation(int n, int r) {
	if (r == 0) {
		print_arr();
		return;
	}

	for (int i = n - 1; i >= 0; i--) {
		swap(&arr[i], &arr[n - 1]);
		permutation(n - 1, r - 1);
		// 다시 swap을해줘야 마지막에 모두 끝났을 때 arr가 변화 없음
		swap(&arr[i], &arr[n - 1]); 
	}
}