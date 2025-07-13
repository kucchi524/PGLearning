package learning6;

public class Employee {
	
	private String name;
	
	private int age;
	
	private String department;
	
	public Employee (String name, int age, String department) {
		
		this.name = name;
		this.age = age;
		this.department = department;
	}
	
	// 従業員情報を1行に成形して返却する
	@Override
	public String toString() {
		return  "氏名: " + name + " / 年齢: " + age + " / 部署: " + department;
	}

}
