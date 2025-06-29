package learning2;

import java.util.List;

public class EvenNumberExtractor {

	// 数値格納用
	private static int num;
	
	// 偶数のみ抽出して返すメソッド
	static List<Integer> returnEvennumberList(List<Integer> intList, List<String> strList) {
		
		// 文字列に格納されている要素数だけ繰り返す
		for (String str : strList) {
			
			// 取得した文字列を数値に変換して変数に格納する
			num = Integer.parseInt(str);
			
			// 格納した数値を偶数か判定して、偶数の場合はリストに格納する
			if (num % 2 == 0) {
				intList.add(num);
			}
		}
		
		return intList;
	}
	
}
