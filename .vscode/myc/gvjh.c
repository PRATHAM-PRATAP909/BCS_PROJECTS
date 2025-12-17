#include <stdio.h>

// Correct iterative binary search
int bsearch_iterative(int a[], int key, int st, int end) {
    int left = st;
    // The right boundary is the last valid index, not the size.
    int right = end - 1; 

    while (left <= right) {
        // Using this formula avoids potential integer overflow
        int mid = left + (right - left) / 2; 

        if (a[mid] == key) {
            return mid; // Found the key, return its index
        } 
        
        if (a[mid] > key) {
            right = mid - 1; // Search in the left half
        } else { // a[mid] < key
            left = mid + 1;  // Search in the right half
        }
    }

    return -1; // Key was not found
}

int main() {
    // NOTE: The array MUST be sorted for binary search to work.
    int a[10] = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100};
    int key;

    printf("Enter a number to search for: ");
    scanf("%d", &key);

    int result = bsearch_iterative(a, key, 0, 10);

    if (result != -1) {
        printf("Element found at index: %d\n", result);
    } else {
        printf("Element not found.\n");
    }

    return 0;
}