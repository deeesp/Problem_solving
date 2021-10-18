#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> minimi(9);
void sum100();

int main() {
	for (int i = 0; i < 9; i++)
		cin >> minimi[i];
	
	sum100();	// 일곱난장이 키의 합이 100이 되는 조합
	sort(minimi.begin(), minimi.end());  // 오름차순

	for (int i = 2; i < 9; i++)  // index 0,1번 난장이 -> 나가리
		cout << minimi[i] << "\n";
}


void sum100() {
	int sum9= 0; // sum아홉난쟁이 키 합
	for (int i = 0; i < 9; i++)
		sum9 += minimi[i];

	for(int i=0; i<8; i++)
		for (int j = i + 1; j < 9; j++) {
			if (sum9 - (minimi[i] + minimi[j]) == 100) {
				minimi[i] = 0;
				minimi[j] = 0;
				return;
			}
		}
}