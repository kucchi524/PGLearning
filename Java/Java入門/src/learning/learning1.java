package learning;

import java.util.ArrayList;
import java.util.List;

public class learning1 {
	
	// ランダム偶数のみ配列にする用
	public static List<Integer> numList;
	
	// ランダムで生成した数値用
	public static int randNum;

	public static void main(String[] args) {
		
		// リストを初期化する
		// ランダム生成用
		List<String> array = new ArrayList<String>();
		
		// 偶数用
		List<Integer> numList = new ArrayList<Integer>();
		
		// 繰り返す回数をランダムに決める
		int loopRandNum = (int)Math.ceil(Math.random() * 10);
		
		System.out.println(loopRandNum);
		
		// 10回繰り返して、ランダム生成用の配列に格納する
		for (int i = 0; i < loopRandNum; i++) {
			
			// 1～10の数値をランダムに生成する
			randNum = (int)Math.ceil(Math.random() * 10);
			
			// リストに数値を追加する
			array.add(String.valueOf(randNum));
			
		}
		
		// ランダム生成した配列の中身を表示する
		System.out.println(array);
			
		// 偶数のみの配列を表示する
		System.out.println(convertNum(array, numList));
	}
	
	// 偶数のみ配列にするメソッド
	public static List<Integer> convertNum(List<String> array, List<Integer>numList) {
		
		// 配列の長さの分だけ繰り返す
		for (String arrayNum : array) {
			
			// 偶数の場合は配列に格納する
			if (Integer.parseInt(arrayNum) % 2 == 0) {
				numList.add(Integer.parseInt(arrayNum));
			}
		}
		
		// 配列格納後のオブジェクトを返却する
		return numList;
	}

}
