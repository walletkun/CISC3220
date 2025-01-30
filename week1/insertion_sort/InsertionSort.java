package insertion_sort;

import java.util.Arrays;

public class InsertionSort {
    private int[] array;

    // Defining the insertion sort with an array
    public InsertionSort(int[] arr){
        this.array = arr;
        sort();
    }

    // Define it with a given size
    public InsertionSort(int[] arr, int size){
        this.array = Arrays.copyOf(arr, size);
        sort();
    }

    private void sort(){
        for(int i = 1; i < this.array.length; i++){
            int key = this.array[i];
            int j = i - 1;


            while (j >= 0 && this.array[j] > key){
                this.array[j  + 1] = this.array[j];
                j = j - 1;
            }

            this.array[j + 1] = key;
        }
    }

    public int[] getSortedArray(){
        return array;
    }

    // Method to print array
    public void printArray() {
        System.out.println(Arrays.toString(array));
    }

}
