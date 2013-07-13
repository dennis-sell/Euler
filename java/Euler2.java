public class Euler2 {
  public static void main(String[] args) {
    int x = 0;
    int y = 2;

    int sum = 0;
    while (y < 4000000) {
        sum += y;
        int swap = x;
        x = y;
        y = 4 * x + swap;
    }
    System.out.println(sum);
  }
}
