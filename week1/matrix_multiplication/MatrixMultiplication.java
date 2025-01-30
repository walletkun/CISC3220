package matrix_multiplication;
public class MatrixMultiplication {
    

    private int[][] MatrixA;
    private int [][] MatrixB;


    public MatrixMultiplication(int[][] MatrixA, int[][] MatrixB){
        if(MatrixA[0].length != MatrixB.length){
            throw new Error("You suck");
        }
        this.MatrixA = MatrixA;
        this.MatrixB = MatrixB;
        calculate();
    }


    public int[][] calculate(){
        int[][] solution = new int[MatrixA.length][MatrixB[0].length];
        for(int i = 0; i < MatrixA.length; i++){
            for(int j = 0; j < MatrixB.length; j++){
                int cur_cell = 0;
                for (int k = 0; k < MatrixA[0].length; k++){
                    cur_cell += MatrixA[i][j] * MatrixB[j][k];
                }
                solution[i][j] = cur_cell;
            }
        }
        return solution;
    }

}
