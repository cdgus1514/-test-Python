// 아스키 코드

package algorithm;
import java.util.Scanner;


public class bj11654 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String ascii = sc.next();
		int result = ascii.charAt(0);
		
		System.out.println(result);
	}
}
