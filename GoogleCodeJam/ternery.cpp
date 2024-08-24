// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>

int main() {
    // Write C++ code here
    std::cout << "Hello world!";
    std::vector<int> vec{0,0,0,0,0,0,1,0,0};
    std::vector<int> ve0{0,1,2,3,4,5,6,7,8};
    //c=1;
    //e=1;
    if(vec[0]>vec[1]?:
        vec[2]>vec[3]?vec[4]>vec[5]:vec[6]>vec[7]){
            std::cout<<"Inside";
        }

    return 0;
}
