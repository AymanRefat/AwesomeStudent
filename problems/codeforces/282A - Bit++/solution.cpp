#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n, x = 0;
	string ch;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> ch;
		if (ch[1] == '+')
			x++;
		else
			x--;
	}
	cout << x << "\n";

	return 0;
}