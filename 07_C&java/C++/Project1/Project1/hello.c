


#include <stdio.h>

void test(int num) {
	for (int i = 0; i < num ; i++)
	{
		if (i % 2 == 0)
			printf(%d, i);
	}
	
}

int main() {

	printf("Hello World! \n");
	test(10);
	return 0;
}

