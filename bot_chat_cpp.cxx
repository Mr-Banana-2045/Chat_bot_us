#include <iostream>
#include <string>
using namespace std;

int main() {
    while (true)
    {
    string text;
    
    cout << "\x1B[93myou > \x1B[97m";
    getline(cin, text);

    if(text.find("hello") != string::npos){
        cout << "\x1B[94mBot:\x1B[92m hello my friend";
    }
    else if(text.find("bye") != string::npos){
    	cout << "\x1B[94mBot:\x1B[92m bye my friend";
    }
    else{
        cout << "\x1B[91merror";
    }

    cout << endl;
    }
}