#include <iostream>
using namespace std;
int main()
{

	for (int r = 1; r <= 5; r++)
	{

		for (int h = 1; h <= 5; h++)
		{
			int num;
			cin >> num;
			if (num == 1)
			{
				cout << abs(3 - r) + abs(3 - h);
			}
		}
	}

	return 0;
}