#include<stdio.h>

//void test(int a) {
//	for (int i=0; i < a; i++) {
//		if (i % 2 == 0) {
//			printf("%d \n", i);
//		}
//	}
//}

void Fibo(int input) {
	int arr[2] = { 0, 1 };
	int temp = arr[0] + arr[1];
	
	printf("%d ", arr[0]);
	while (temp <= input) {
		printf("%d ", temp);

		temp = arr[0] + arr[1];
		arr[0] = arr[1];
		arr[1] = temp;
	}
}


int fibo_recursion(int n) {
	if (n == 0 || n == 1) {
		return 1;
	}
	else {
		return fibo_recursion(n - 1) + fibo_recursion(n - 2);
	}
}

void main() {

	/*test(10);*/
	int arra[3] = { 1,2,3 };
	Fibo(10);
}