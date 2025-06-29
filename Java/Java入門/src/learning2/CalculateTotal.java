package learning2;

import java.util.List;

public class CalculateTotal {
	
	private static int total;

	// リストに格納されている値の合計値を計算する
	public static int calculateTotal(List<Integer> list) {
		
		total = 0;
		
		for (int num : list) {
			total += num;
		}
		
		return total;
	}
	
}
