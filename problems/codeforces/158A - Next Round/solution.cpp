#include <iostream>

int main()
{
	int n, k;
	std::cin >> n >> k;

	int scores[n];
	for (int i = 0; i < n; ++i)
	{
		std::cin >> scores[i];
	}

	int advanceCount = 0;

	for (int i = 0; i < n; ++i)
	{
		if (scores[i] > 0 && scores[i] >= scores[k - 1])
		{
			advanceCount++;
		}
	}

	std::cout << advanceCount;

	return 0;
}
