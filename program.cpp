# include <iostream>
# include <cstring>
using namespace std;
int main(){
    string s ="deekshithareddykandula";
    cout<< s.size();
    cout<<s.length();
    cout<< strlen(s); //for only the char array
    cout<<strlen(s.c_str());
}