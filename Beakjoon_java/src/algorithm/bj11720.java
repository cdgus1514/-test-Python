package algorithm;
// 숫자의 합

import java.util.*;

public class bj11720 {
	public static void main(String[] args) {
		Scanner sc2 = new Scanner(System.in);
		
		int num = sc2.nextInt();
		int sum = 0;
		
		String line = sc2.next();
		System.out.println("line >> " + line +"\n");
		
		for(int i=0; i<num; i++) {
			// char형을 아스키코드를 사용해서 int형으로 변환
			//sum += line.charAt(i) -'0';
			
			// Integer 클래스의 parseInt와 String 클래스의 substring 사용 
			sum += Integer.parseInt(line.substring(i, i+1));
		}
		
		System.out.println(sum);
	}
}