#include <iostream>
#include <string>
using namespace std;

int main()
{
	string valows;
	valows = "ayoeui";

	string str;
	cin >> str;
	for (int i = 0; i < str.length(); i++)
	{
		if (valows.find(tolower(str[i])) == std::string::npos)
		{
			cout << "." << char(tolower(str[i]));
		}
	}
	return 0;
}