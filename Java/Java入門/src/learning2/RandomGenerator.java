package learning2;

import java.util.List;

public class RandomGenerator {

	// 繰り返し用
	private static int loopNum;
	
	// リスト格納用
	private static int randNum;
	
	// ランダム生成した数値を文字列で格納するメソッド
	public static List<String> createStringNumber(List<String> strList) {
		
		// 繰り返す回数を1～10のランダムで決める
		loopNum = (int)Math.ceil(Math.random() * 10);
		
		// 繰り返し処理を実行する
		for (int i = 0; i < loopNum; i++) {
			
			// 1～10の数値をランダムで生成する
			randNum = (int)Math.ceil(Math.random() * 10);
			
			// リスト格納時に文字列に変換する
			strList.add(String.valueOf(randNum));
		}
		
		return strList;
	}
}
	