package matrix_multiplication;

import java.util.Arrays;


public class Main {
    

    public static void main(String[] args) {
        int[][] A = {
            {1,2,3},
            {2,3,4}
        };
        int [][] B = {
            {3,2,1},
            {2,4,3},
            {5,5,5}
        };
        MatrixMultiplication multiply = new MatrixMultiplication(A, B);

        System.out.println(Arrays.deepToString(multiply.calculate()));

    }
}
