package merge_sort;

public class MergeSort {
    private int[] A; // The initial Array


    // No size inputted
    public MergeSort(int[] array){
        this.A = array;
        mergeSort(A, 0, A.length - 1);
    }

    private void mergeSort(int[] array, int p, int r){
        if (p >= r){
            return; // Callback 
        }

        int q = (p + r) / 2;

        mergeSort(array, p, q);
        mergeSort(array, q + 1, r);
        merge(array, q, p, r);
    }

    public void merge(int[] array, int q, int p, int r){
        int n1 = q - p + 1; // define the size of the left array
        int n2 = r - q; // define the size of the right array


        int[] left = new int[n1];
        int[] right = new int[n2]; 


        for(int i = 0; i < n1; i++){
            left[i] = array[p + i];
        }

        for(int i = 0; i < n2; i++){
            right[i] = array[q + 1 + i];
        }


        int i = 0, j = 0, k = p;

        while( i < n1 && j < n2){
            if(left[i] <= right[j]){
                array[k] = left[i];
                i++;
            }
            else{
                array[k] = right[j];
                j++;
            }

            k++;
        }
        // Making sure that no elements are left inside the array that is not sorted
        while(i < n1){
            array[k] = left[i];
            i++;
            k++;
        }

        while (j < n2){
            array[k] = right[j];
            j++;
            k++;
        }
    }


    // Print the array
    public void printArray(){
        for(int num : A){
            System.out.println(num + " ");
        }
    }
}
