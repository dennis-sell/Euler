/**
 * Created with IntelliJ IDEA.
 * User: dennis
 * Date: 10/7/12
 * Time: 2:21 AM
 * To change this template use File | Settings | File Templates.
 */
public class Euler10 {
    public static void main(String[] args) {
      Euler2();
    }

    /**
     * Find the sum of all numbers less than 1000 which are a multiple of 3 or 5.
     */
    public static void Euler1() {
        int limit = 1000;
        int sum = 0;
        for (int i = 3; i < limit; i++) {
            if (i%3 == 0 || i % 5 == 0) sum += i;
        }
        System.out.println("Euler 1 : " + sum);
    }


    /**
     *  Determine the sum of all even Fibonacci numbers below 4 million.
     *  Based off the fact that every third fibonacci number is even and
     *  F(n) = 4*F(n-3) + F(n-6)
     */
    public static void Euler2() {
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
