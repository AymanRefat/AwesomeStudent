#include <iostream>
#include <string>
using namespace std;
int main()
{

	int n;
	cin >> n;
	int total;
	total = 0;
	int x, y, z;
	// loop till end
	while (n--)
	{
		int answers;
		cin >> x >> y >> z;
		if (x + y + z >= 2)
		{
			total += 1;
		}
	}
	cout << total;

	return 0;
}