package learning8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		List<Employee> empList = new ArrayList<>();
		
		String readFilePath = "C:\\Users\\USER\\Desktop\\PG学習\\employees.csv";
		
		try (BufferedReader br = new BufferedReader(new FileReader(readFilePath))) {
			
			String line;
			
			while ((line = br.readLine()) != null) {
				
				String[] parts = line.split(",");
				String name = parts[0];
				int age = Integer.parseInt(parts[1]);
				String department = parts[2];
				
				empList.add(new Employee(name, age, department));
			}
			
		} catch (IOException e) {
			System.err.println("ファイルの読み込みに失敗しました" + e.getMessage());
		} finally {
			System.out.println("ファイル読み込みを終了します");
		}
		
		for (Employee e : empList) {
			System.out.println(e);
		}
		
		String writeFilePath = "C:\\Users\\USER\\Desktop\\PG学習\\filtered.csv";
		
		try (BufferedWriter bw = new BufferedWriter(new FileWriter(writeFilePath))) {
			
			for (Employee e : empList) {
				if (e.toString().contains("営業部")) {
					bw.write(e.toCsv());
					bw.newLine();
				}
			}
			
		} catch (IOException e) {
			System.err.println("ファイルの書き込みに失敗しました。" + e.getMessage());
		} finally {
			System.out.println("処理を終了します");
		}
	}

}
