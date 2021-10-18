#include <iostream>
#include <algorithm>
using namespace std;

int n;

void print_arr(int *a) {
	for (int i = 0; i < n; i++)
		printf("%d ", a[i]);
	printf("\n");
}


int main() {
	scanf_s("%d",&n);

	int *a = new int[n];
	for (int i = 0; i < n; i++)
		a[i] = i + 1;

	do
		print_arr(a);
	while (next_permutation(a, a+n));
}