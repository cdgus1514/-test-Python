package algorithm;
// ������ ��

import java.util.*;

public class bj11720 {
	public static void main(String[] args) {
		Scanner sc2 = new Scanner(System.in);
		
		int num = sc2.nextInt();
		int sum = 0;
		
		String line = sc2.next();
		System.out.println("line >> " + line +"\n");
		
		for(int i=0; i<num; i++) {
			// char���� �ƽ�Ű�ڵ带 ����ؼ� int������ ��ȯ
			//sum += line.charAt(i) -'0';
			
			// Integer Ŭ������ parseInt�� String Ŭ������ substring ��� 
			sum += Integer.parseInt(line.substring(i, i+1));
		}
		
		System.out.println(sum);
	}
}