package learning5;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		try {
			Scanner sc = new Scanner(System.in);
			System.out.println("割られる数を入力してください");
			int num = Integer.parseInt(sc.nextLine());
			
			System.out.println("割る数を入力してください");
			int nu = Integer.parseInt(sc.nextLine());
			
			System.out.println(num /nu);
			
		} catch (NumberFormatException e) {
			System.err.println("数字を入力してください");
		} catch (ArithmeticException e) {
			System.err.println("0では割り切れません");
		} finally {
			System.out.println("処理を終了します");
		}
	}

}
