package learning4;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		// 数字を入力してもらう
		Scanner sc = new Scanner(System.in);
		System.out.println("登録する所品数を入力してください");
		int count = Integer.parseInt(sc.nextLine());
		int total = 0;
		
		List<Item> itemList = new ArrayList();
		
		try {
			
			for (int i = 1; i <= count; i++) {
				
				// 商品名を入力してもらう 
				System.out.println("商品名: ");
				String name = sc.nextLine();
				
				// 数量を入力してもらう
				System.out.println("数量: ");
				int quantity = Integer.parseInt(sc.nextLine());
				
				// 値段を入力してもらう
				System.out.println("値段: ");
				int price = Integer.parseInt(sc.nextLine());
				
				itemList.add(new Item(name, quantity, price));
			}
			
		} catch(NumberFormatException e) {
			System.out.println("数値を入力してください");
		}
		
		for (Item item : itemList) {
			System.out.println(item.getInfo());
			total += item.getSubtotal();
		}
		
		System.out.println("合計金額: " + total + "円です");

	}

	

}
