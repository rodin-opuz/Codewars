public class Kata {
    public static double findAverage(int[] array) {
        int sum = 0;
      if (array.length == 0) {
        return 0.0;
      }
      for (int i = 0; i < array.length; i++) {
          sum += array[i];
      }
      return (double) sum / array.length;
    }
}
