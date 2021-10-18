// nPr 순열
// n > r 


#include <iostream>

using namespace std;

int arr[] = { 1,2,3,4 };

void swap(int *a, int *b);
void print_arr();
void permutation(int n, int r, int depth);

int main() {
	int r;
	cout << "r을 입력해주세요: ";
	cin >> r;
	permutation(sizeof(arr) / sizeof(int), r, 0);
	return 0;
}


void swap(int *a, int *b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}
void print_arr(int size) {
	for (int i = 0; i < size; i++)
		cout << arr[i];
	cout << "\n";
}

void permutation(int n, int r, int depth) {
	// r과 depth의 크기가 같아지면 출력하고 반환
	// 배열 index가 0부터 depth-1까지(r-1까지)
	// 즉 r개만큼 앞에서 순열이 생성되었기에 반환
	if (r == depth) {
		print_arr(depth);
		return;
	}

	for (int i = depth; i < n ; i++) {
		swap(&arr[i], &arr[depth]);
		permutation(n, r, depth+1);
		// 다시 swap을해줘야 마지막에 모두 끝났을 때 arr가 변화 없음
		swap(&arr[i], &arr[depth]); 
	}
}