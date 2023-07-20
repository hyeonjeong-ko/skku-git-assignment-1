#include <iostream>

using namespace std;

int sumFromZero(int num){
    int sum=0;
    for(int i=0;i<=num;i++) sum+=i;
    return sum;
}

int main(){
    cout<<"Hello World"<<"\n";

    int num = 10;
    cout<<sumFromZero(num);
    
    //I don't know why I feel so nervous when doing this stuff....god plz
}
