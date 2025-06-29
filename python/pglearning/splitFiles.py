import os
import tkinter.filedialog
import shutil

# 対象フォルダを選択する
dir = tkinter.filedialog.askdirectory()
print(dir)

# キャンセルボタンをクリックされたときの処理
if not dir:
    print('処理がキャンセルされました')
    exit()

# ファイル移動処理のメソッド
def moveFiles(dir):
    
    #移動対象ファイルのディクショナリ
    fileCategorises = {
        "movies": ".mp4",
        "audios": [".mp3", ".wav", ".aac"]
    }

    # ディレクトリにファイルがない場合
    if not os.path.exists(dir):
        print('ないよ')

    # ディレクトリ内にあるファイルを1件ずつ抽出する
    for file in os.listdir(dir):
        
        # ファイルの絶対パスを生成
        filePath =os.path.join(dir, file)
    
        # 隠しファイルやディレクトリはスキップする
        if not os.path.isfile(filePath):
            continue
    
        #拡張子を取得する
        _, ext = os.path.splitext(file)
    
        # 拡張子とカテゴリのディクショナリをループして、マッチするか確認する
        for category, extentions in fileCategorises.items():
            
            # 拡張子がカテゴリに存在しているか
            if ext.lower() in extentions:
                
                #　カテゴリ名をもとにした保存先ディレクトリパスを生成
                folder = os.path.join(dir, category)
            
                #　存在しなければディレクトリ作成
                if not os.path.exists(folder):
                    os.makedirs(folder)
                    
                # ファイルをカテゴリのディレクトリへ移動
                shutil.move(filePath, os.path.join(folder, file))
                
                # ログ出力
                print(f'MOVE: {file} → {folder}')
                
                # マッチすれば次へ
                break

# メソッドを呼び出す            
moveFiles(dir)

# 終了ログ
print('処理が完了しました')