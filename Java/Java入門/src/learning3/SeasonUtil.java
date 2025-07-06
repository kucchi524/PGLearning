package learning3;

public class SeasonUtil {
	
	public static String season;
	
	// 季節を抽出するメソッド
	public static String getSeason(int month) {
		
		// 引数から季節を決める
		switch(month) {
		
			case 3, 4, 5:
				season = String.valueOf(Season.spring);
				break;
			case 6, 7, 8:
				season = String.valueOf(Season.summer);
				break;
			case 9, 10, 11:
				season = String.valueOf(Season.autum);
				break;
			case 1, 2, 12:
				season = String.valueOf(Season.winter);
				break;
			default:
				season = month + "月は存在しません。";
		}
		
		return season;
	}

}
