import tkinter as tk
from tkinter import messagebox
from datetime import date

# 설정
PW = 'ta'
today = date.today()

# 콜백 함수: 비밀번호 확인
def check_password():
    if pw_entry.get() == PW:
        login_frame.pack_forget()
        diary_frame.pack()
    else:
        messagebox.showerror("Access Denied", "Wrong password!")

# 콜백 함수: 다이어리 저장
def save_diary():
    feeling = feeling_entry.get()
    reason = reason_entry.get()
    extra = extra_entry.get()

    with open('logue.txt', 'a', encoding='utf-8') as f:
        f.write(feeling + '\n' + reason + '\n' + extra + '\n' + 'This is written on ' + str(today) + '\n\n')

    messagebox.showinfo("Saved", "Your diary has been saved!")
    root.quit()

# 윈도우 만들기
root = tk.Tk()
root.title("Magic Diary")
root.geometry("400x300")

# ------------------ 로그인 화면 ------------------
login_frame = tk.Frame(root)
login_frame.pack(pady=30)

tk.Label(login_frame, text="Enter the Magic Word:").pack()
pw_entry = tk.Entry(login_frame, show="*")  # * 처리됨
pw_entry.pack(pady=10)

tk.Button(login_frame, text="Unlock Diary", command=check_password).pack()

# ------------------ 다이어리 화면 ------------------
diary_frame = tk.Frame(root)

tk.Label(diary_frame, text="Today I feel:").pack()
feeling_entry = tk.Entry(diary_frame)
feeling_entry.pack()

tk.Label(diary_frame, text="Because:").pack()
reason_entry = tk.Entry(diary_frame)
reason_entry.pack()

tk.Label(diary_frame, text="Anything else?").pack()
extra_entry = tk.Entry(diary_frame)
extra_entry.pack()

tk.Button(diary_frame, text="Save Diary", command=save_diary).pack(pady=10)

# 실행 시작
root.mainloop()