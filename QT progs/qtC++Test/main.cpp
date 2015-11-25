#include <iostream>
#include <string>
using namespace std;

int main()
{

    string name = "marc";
    cout << "Enter last name" << endl;
    string lName;
    getline(cin, lName);
    string newName =  name + " " +lName;
    cout << "New name: " + newName;


    return 0;
}

