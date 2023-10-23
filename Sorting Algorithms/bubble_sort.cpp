#include <bits/stdc++.h>
using namespace std;

void bubble_sort(int arr[], int n)
{
    bool flag;
    for (int i = 0; i < n - 1; i++)
    {
        flag = false;
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1]) // by changin '>' to '<', you will get array sorted in descending order.
            {
                swap(arr[j], arr[j + 1]);
                flag = true;
            }
        }
        if (!flag)
            break;
    }
}

int main()
{
    int arr[] = {2, 7, 4, 1, 5, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, n);
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    return 0;
}