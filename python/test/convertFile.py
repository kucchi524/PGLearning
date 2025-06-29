import ffmpeg
import tkinter.filedialog
import os

iDir = 'C:\\Users\\USER\\Desktop\\新しいフォルダー'#'C:\\Users\\USER\\Videos\\VideoProc Converter AI'
fTyp = [("", "*")]
fileNames = tkinter.filedialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)

saveIDir = 'C:\\Users\\USER\\Desktop\\音声変換ファイル'
saveDir = tkinter.filedialog.askdirectory(title='保存先を選択してください', initialdir=saveIDir)

for fileName in fileNames:
    baseName = os.path.splitext(os.path.basename(fileName))[0]
    saveFileName=os.path.join(saveDir, baseName + '.mp3')
    
    try:
        (
            ffmpeg
            .input(fileName)
            .output(saveFileName, format='mp3', acodec='libmp3lame')
            .run(overwrite_output=True)
        )
        print(f'変換完了: {saveFileName}')
    except ffmpeg.Error as e:
        print(f'変換失敗: {fileName}\nエラー内容: {e}')

print('すべての変換処理が完了しました')