package learning7;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		try {
			// 入力情報を受け付ける
			System.out.println("従業員の任数を入力してください");
			Scanner sc = new Scanner(System.in);
			int empCount = Integer.parseInt(sc.nextLine());
			
			// 従業員用リスト
			List<Employee> empList = new ArrayList<Employee>();
			
			// 従業員数分回して配列に格納
			for (int i = 1; i <= empCount; i++) {
				
				// 各情報を入力してもらう
				System.out.println("従業員の氏名を入力してください");
				String name = sc.nextLine();
				System.out.println("従業員の年齢を入力してください");
				int age = Integer.parseInt(sc.nextLine());
				System.out.println("従業員の部署を入力してください");
				String department = sc.nextLine();
				
				empList.add(new Employee(name, age, department));
			}
			
			// Mapにする
			Map<String, List<Employee>> deptMap = new HashMap<>();
			
			for (Employee e : empList) {
				String dept = e.getDepartment();
				deptMap.putIfAbsent(dept, new ArrayList<>());
				deptMap.get(dept).add(e);
			}
			
			// 表示する
			for (Map.Entry<String, List<Employee>> entry : deptMap.entrySet()) {
				System.out.println("【" + entry.getKey() + "】");
				for (Employee e : entry.getValue()) {
					System.out.println(" " + e);
				}
			}
			
		} catch (NumberFormatException e) {
			// 数値が入力されていない場合の例外処理
			System.err.println("年齢に数値を入力してください");
		} finally {
			System.out.println("処理を終了します");
		}

	}

}
