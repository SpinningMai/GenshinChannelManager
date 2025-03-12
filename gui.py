import tkinter as tk
from tkinter import ttk

server_config = {
    "天空岛 + 米哈游通行证": 1,
    "世界树 + BiliBili账号": 2,
}

def center_window(root, width=300, height=150):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

def get_server_selection():
    def on_submit():
        selected_server = server_var.get()
        if selected_server in server_config:
            user_selection["server"] = selected_server
            user_selection["value"] = server_config[selected_server]
            user_selection["autoStartGame"] = auto_start_game_var.get()
        root.quit()

    root = tk.Tk()
    root.title("原神切服小助手")
    root.config(padx=10, pady=10)

    center_window(root, 260, 135)

    tk.Label(root, text="请选择服务器和渠道:", font=("TkDefaultFont", 10, "bold")).pack(anchor=tk.W)

    server_var = tk.StringVar()
    server_dropdown = ttk.Combobox(root, textvariable=server_var, values=list(server_config.keys()), state="readonly")
    server_dropdown.pack(anchor=tk.W, pady=5)
    server_dropdown.current(0)

    auto_start_game_var = tk.BooleanVar(value=True)
    check_button = tk.Checkbutton(root, text="确定后启动游戏", variable=auto_start_game_var)
    check_button.pack(anchor=tk.W)

    # "Start" button
    submit_button = tk.Button(root, text="确定", command=on_submit)
    submit_button.pack(pady=(10, 0))

    user_selection = {}
    root.mainloop()  # run GUI

    return user_selection


if __name__ == '__main__':
    result = get_server_selection()
    if result:
        print(f"Selected Server: {result['server']}")
        print(f"Assigned Value: {result['value']}")
