import PySimpleGUI as sg

# ウィンドウを表示する
win = sg.Window(
    title = "格言を表示するアプリ",
    layout = [[sg.Text("以下のボタンを押してください")],
              [sg.Button("格言を表示")]]
)

# イベントループを開始
while True:
    # イベントを読む
    event, _ = win.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "格言を表示":
        sg.popup("良い言葉によって心が晴れる")