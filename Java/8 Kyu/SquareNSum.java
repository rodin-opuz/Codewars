public class Kata {
  public static int squareSum(int[] n) { 
    int sum = 0;
    for (int number: n) {
      sum += number * number;
    }
    return sum;
  }
}
