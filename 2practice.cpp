#include <iostream>

using namespace std;

int main()
{
    float math,science,tle,esp,computer,filipino;
    float average;

    cout <<"Enter Grade Math: ";
    cin >> math;

    cout <<"Enter Grade Science: ";
    cin >> science;

    cout <<"Enter Grade Tle: ";
    cin >> tle;

    cout <<"Enter Grade Esp: ";
    cin >> esp;

    cout <<"Enter Grade Computer: ";
    cin >> computer;

    cout <<"Enter Grade Filipino: ";
    cin >> filipino;

    average = (math + science + tle + esp + computer + filipino) /6;
    cout <<"Final Grade: " << average;
    cout << endl;
    if(average > 100) cout << "Invalid Grade";
    else if(average >= 98) cout << "With High Honor";
    else if(average >= 90) cout << "With Honor";
    else if(average >= 75) cout << "Passed";
    else cout << "Failed";

    return 0;
}

