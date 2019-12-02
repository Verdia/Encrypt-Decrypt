#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

int main(){
	string s;
	int key=0, size = 0, choose;
	char y;
	int *array;

	cout << "Choice :\n1. Encryption. \n 2. Decryption\n\n" << endl;
	cout << "your choice : ";
	cin >> choose;
	switch(choose){
		case 1:
			cout << "Enter Massage to Encrypt : \n";
			cin >> s;
			cout << "Enter Pin : ";
			cin >> key;
			size = s.length();
			array = new int[s.length()];
			cout << "Encrypted Success";
			for(int i=0;i<size;i++)
			*(array+i) = s[i]+key;
			for (int i = 0; i < size; ++i)
			 {
			 	y = *(array+i);
			 	cout << array[i] << "\t" << y << endl;
			 } 
			 delete[]array;
			 break;

		case 2:
			cout << "Enter Massage to Decrypt : \n";
			cin >> s;
			cout << "Enter Pin : ";
			cin >> key;
			size = s.length();
			array = new int[s.length()];
			cout << "Decrypt Success";
			for (int i = 0; i < size; ++i)
			{
				y=*(array+i);
				cout << array[i] << "\t" << y << endl;
			}
			delete[]array;
			break;
				default:
					cout << "Wrong Password \n";
					cout << "\n\n\n\n\n";
					system("pause");
	}
}