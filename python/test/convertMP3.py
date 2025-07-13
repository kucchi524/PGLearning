import ffmpeg
import tkinter.filedialog
import os

# 対象とする動画拡張子
video_exts = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']

# 入力：上位フォルダ選択
input_root_dir = tkinter.filedialog.askdirectory(title='動画ファイルが入った上位フォルダを選択してください')

# 出力：保存先のルートフォルダ選択
output_root_dir = tkinter.filedialog.askdirectory(title='音声ファイルの保存先フォルダを選択してください')

# 再帰的に動画ファイルを収集
video_files = []
for root, dirs, files in os.walk(input_root_dir):
    for file in files:
        if os.path.splitext(file)[1].lower() in video_exts:
            full_path = os.path.join(root, file)
            video_files.append(full_path)

# 変換処理（フォルダ構造を維持して出力）
for video_path in video_files:
    # 相対パス（例：B/movie.mp4）
    relative_path = os.path.relpath(video_path, input_root_dir)
    relative_folder = os.path.dirname(relative_path)
    base_name = os.path.splitext(os.path.basename(video_path))[0]

    # 出力先フォルダとファイル名の決定
    output_folder = os.path.join(output_root_dir, relative_folder)
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, base_name + '.mp3')

    # 変換実行
    try:
        (
            ffmpeg
            .input(video_path)
            .output(output_path, format='mp3', acodec='libmp3lame')
            .run(overwrite_output=True)
        )
        print(f'変換完了: {output_path}')
    except ffmpeg.Error as e:
        print(f'変換失敗: {video_path}\nエラー: {e.stderr.decode()}')

print('すべての変換が完了しました')
