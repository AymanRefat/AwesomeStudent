#include <iostream>
using namespace std;
int main()
{

	long long int n;
	cin >> n;
	if (n <= 2)
	{
		cout << "NO";
	}
	else if (n % 2 == 0)
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}

	return 0;
}