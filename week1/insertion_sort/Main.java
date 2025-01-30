package insertion_sort;

public class Main {
    
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 6, 3};
        InsertionSort insert = new InsertionSort(array);

        insert.printArray();
        
    }
}
