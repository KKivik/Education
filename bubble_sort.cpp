#include <iostream>

using namespace std;

void fillTheArray(int* arr, int n) 
{
    for (int i = 0; i < n; ++i) {
        arr[i] = rand() % 100;
        cout << arr[i] << " ";
    }
    cout << endl;
}


//long long summ(int* arr, int n) {
//    long long summ = 0;
//    for (int i = 0; i < n; ++i) {
//        summ += arr[i];
//    }
//    return summ;
//}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (arr[j] < arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
        
    }
}

int main()
{
    int const n = 5;
    int arr[n];
    fillTheArray(arr, n);
    bubbleSort(arr, n);

    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }

}
