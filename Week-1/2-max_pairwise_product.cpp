#include <bits/stdc++.h>
using namespace std;

long long MaxPairwiseProductSuperFast(const std::vector<int>& numbers){
    int poslarge1 = -1, poslarge2 = -1;
    int neglarge1 = 0,  neglarge2 = 0;
    int n = numbers.size();

    if(n < 2){
        return 0;
    }
    if(n == 2){  
        return ((long long)numbers[0]*numbers[1]); 
    }

    for (int i = 0; i < n; ++i){
        if(numbers[i] > poslarge1){
            poslarge2 = poslarge1;
            poslarge1 = numbers[i];
        }
        else if(numbers[i] > poslarge2) 
            poslarge2 = numbers[i];
        if(numbers[i] < 0 && abs(numbers[i]) > abs(neglarge1)){ 
            neglarge2 = neglarge1;
            neglarge1 = numbers[i]; 
        }
        else if(numbers[i] < 0 && abs(numbers[i]) > abs(neglarge2)) 
            neglarge2 = numbers[i]; 
    }

    return (std::max((long long)poslarge1*poslarge2, (long long)neglarge1*neglarge2));
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductSuperFast(numbers) << "\n";
    return 0;
}
