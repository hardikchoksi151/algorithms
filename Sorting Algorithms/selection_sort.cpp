#include <iostream>
using namespace std;

int selection_sort(int arr[], int n)
{
    int i_min;
    for (int i = 0; i < n - 1; i++)
    {
        i_min = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[i_min])
                i_min = j;
        int temp = arr[i];
        arr[i] = arr[i_min];
        arr[i_min] = temp;
    }
}

int main()
{
    int arr[] = {5, 1, 12, -5, 16, 2, 12, 14};
    int n = sizeof(arr) / sizeof(arr[0]);
    int pass = selection_sort(arr, n);
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    return 0;
}