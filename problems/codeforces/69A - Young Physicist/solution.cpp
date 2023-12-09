#include <iostream>
using namespace std;

int main()
{
	int vectors, x, y, z;
	x = y = z = 0;

	int cx, cy, cz;
	cin >> vectors;
	while (vectors--)
	{
		cin >> cx >> cy >> cz;
		x += cx;
		y += cy;
		z += cz;
	}

	if (x == 0 && y == 0 && z == 0)
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}
	return 0;
}