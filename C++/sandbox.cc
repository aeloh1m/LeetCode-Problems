#include <iostream>

#include <vector>
#include <algorithm>

// Class declaration
class MyClass
{
public:
    // Member variables
    int myVariable;

    // Member function declaration
    void printMessage();

    // Constructor declaration
    MyClass(); // Default constructor

    // Destructor declaration
    ~MyClass(); // Destructor
};

// Member function definition outside the class declaration
void MyClass::printMessage()
{
    std::cout << "Hello from MyClass!" << std::endl;
}

// Constructor definition outside the class declaration
MyClass::MyClass()
{
    std::cout << "Constructor called!" << std::endl;
    myVariable = 0; // Initialize member variable if needed
}

// Destructor definition outside the class declaration
MyClass::~MyClass()
{
    std::cout << "Destructor called!" << std::endl;
}

int main()
{
    // Create an object of MyClass
    MyClass myObject;
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    // Access member variables and call member functions
    myObject.myVariable = 42;
    myObject.printMessage();

    // Declare and initialize a vector of integers
    std::vector<int> myVector = {1, 2, 3, 4, 5};

    // Iterate over each element of the vector using a range-based for loop
    for (int num : myVector)
    {
        // 'num' takes on the value of each element in 'myVector' in each iteration
        std::cout << num << " ";
    }

    return 0;
}
int cheatsheet()
{
    int x;
    // Print:
    std::cout << "my message" << x << std::endl;

    // Vectors
    // 1) Initialization:
    std::vector<int> myVector;                        // Empty vector of integers
    std::vector<int> anotherVector = {1, 2, 3, 4, 5}; // Vector with initial values

    // 2) Adding Elements:
    myVector.push_back(42);                    // Add an element to the end
    myVector.insert(myVector.begin() + 2, 10); // Insert element at a specific position

    // 3) Accessing Elements:
    int firstElement = myVector[0];    // Access element using index
    int lastElement = myVector.back(); // Access the last element

    // 4) Iterating Over Elements:
    for (int num : myVector)
    {
        // Iterate over elements using a range-based for loop
    }

    // 5 Size and Capacity:
    int size = myVector.size();         // Number of elements in the vector
    int capacity = myVector.capacity(); // Current storage capacity

    // 6) Resizing:

    myVector.resize(10);    // Resize the vector to contain 10 elements
    myVector.resize(20, 0); // Resize and fill with a default value (0 in this case)

    // 7) Removing elements:
    myVector.pop_back();                  // Remove the last element
    myVector.erase(myVector.begin() + 2); // Remove element at a specific position

    // 8) Sorting

    std::sort(myVector.begin(), myVector.end()); // Sort the vector in ascending order

    // Else:

    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Using a traditional for loop
    for (size_t i = 0; i < numbers.size(); ++i) {
        int currentValue = numbers[i];
        // Your code using currentValue goes here
        std::cout << currentValue << " ";
    }

    numbers.size(); // gives you the number of elements in the vector.

}
