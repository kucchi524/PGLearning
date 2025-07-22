import tkinter as tk
import tkinter.messagebox as msg

# ウィンドウを表示する関数
def show_window():
    
    # メインウィンドウを作成
    root = tk.Tk()
    root.title("格言を表示するアプリ")
    
    # サイズを指定
    root.geometry("300x200")
    
    # ラベルを作成
    tk.Label(root, text="以下のボタンを押してください。").pack()
    
    # ボタンを作成
    tk.Button(root, text="格言を表示", command=click_handler).pack()
    
    # メインループ開始
    root.mainloop()
    
# ボタンクリック時のイベント
def click_handler():
    msg.showinfo(title="格言", message="良い言葉によって心が晴れる")
    
if __name__ == "__main__":
    show_window()