package learning8;

public class Employee {
	
	// 氏名
	private String name;
	
	// 年齢
	private int age;
	
	// 部署
	private String department;
	
	public Employee (String name, int age, String department) {
		
		this.name = name;
		this.age = age;
		this.department = department;
	}
	
	@Override
	public String toString() {
		return name + "（" + age + "歳）" + department;
	}
	
	public String toCsv() {
		return name + "," + age + "," + department;
	}

}
