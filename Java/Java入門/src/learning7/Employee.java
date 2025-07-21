package learning7;

public class Employee {

	
	// 氏名
	private String name;
	
	// 年齢
	private int age;
	
	// 部署
	private String department;
	
	// コンストラクタ
	public Employee (String name, int age, String department) {
		
		this.name = name;
		this.age = age;
		this.department = department;
	}
	
	// 部署を取得するためのメソッド
	public String getDepartment() {
		return department;
	}
	
	// 氏名、年齢を取得するメソッド
	@Override
	public String toString() {
		return name + "（" + age + "歳）";
	}
}
