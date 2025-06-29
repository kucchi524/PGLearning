package learning2;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
	
	// 文字列格納用リスト
	public static List<String> strList;
	
	// 数値格納用リスト
	public static List<Integer> intList;

	public static void main(String[] args) {
		
		// 各リストを初期化
		List<String> strList = new ArrayList<String>();
		List<Integer> intList = new ArrayList<Integer>();
		
		// 乱数生成用クラスを呼び出す
		System.out.println(RandomGenerator.createStringNumber(strList));
		
		// 偶数抽出用クラスを呼び出す
		System.out.println(EvenNumberExtractor.returnEvennumberList(intList, strList));

		// 文字列配列を数値型の配列へ変換する
		List<Integer> strToIntList = strList.stream().map(Integer::parseInt).collect(Collectors.toList());
		
		// 偶数抽出前後のリストの合計値を求める
		int allListTotal = CalculateTotal.calculateTotal(strToIntList);
		System.out.println(allListTotal);
		int evenListTotal = CalculateTotal.calculateTotal(intList);
		System.out.println(evenListTotal);
		
		// 差を求める
		System.out.println(allListTotal - evenListTotal);
	}

}
