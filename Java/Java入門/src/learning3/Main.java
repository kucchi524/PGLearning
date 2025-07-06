package learning3;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		
		System.out.println("月を入力してください");
		Scanner sc = new Scanner(System.in);
		int month = sc.nextInt();
		
		System.out.println(SeasonUtil.getSeason(month));
	}

}
