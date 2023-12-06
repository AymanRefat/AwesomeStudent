#include <iostream>
#include <string>
using namespace std;
int main()
{
	string str;
	long long int n;
	cin >> n;
	while (n--)
	{
		cin >> str;
		if (str.length() > 10)
		{
			cout << str[0] << str.length() - 2 << str.back() << endl;
		}
		else
		{
			cout << str << endl;
		}
	}

	return 0;
}