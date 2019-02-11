using namespace std;

int main()
{
    string name, age, username;
    cout << "Enter your name: ";
    cin >> name;
    cout << "Enter your age: ";
    cin >> age;
    cout << "Enter your username: ";
    cin >> username;
    cout << "your name is " << name << ", you are " << age
        << " years old, and your username is " << username;
    ofstream output_file("info_log.txt");
    if(output_file.is_open())
    {
        output_file << "your name is " << name << ", you are " << age
            << " years old, and your username is " << username;
    }
    return 0;
}
