package learning6;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		try {
			// 入力情報を受け付ける
			Scanner sc = new Scanner(System.in);
			
			// 入力する従業員数を受け付けるする
			System.out.println("従業員数を入力してください");
			int employeeInput = Integer.parseInt(sc.nextLine());
			
			// 従業員情報をリストにする
			List<Employee> employeeInfo = new ArrayList<Employee>();
			
			// 入力した回数分繰り返す
			for (int i = 0; i < employeeInput; i++) {
				// 氏名
				System.out.println("従業員" + (i + 1) + "の氏名を入力してください");
				String name = sc.nextLine();
				
				// 年齢
				System.out.println("従業員" + (i + 1) + "の年齢を入力してください");
				int age = Integer.parseInt(sc.nextLine());
				
				// 部署
				System.out.println("従業員" + (i + 1) + "の部署を入力してください");
				String department = sc.nextLine();
				
				employeeInfo.add(new Employee(name, age, department));
			}
			
			// 社員情報一覧を表示する
			System.out.println("社員情報一覧:");
			
			for (Employee empStr :employeeInfo) {
				System.out.println(empStr);
			}
			
		} catch(NumberFormatException e) {
			
			// 数値が入力されていない場合の例外処理
			System.err.println("年齢に数値を入力してください");
			
		} finally {
			System.out.println("処理を終了します");
		}
		
	}

}
