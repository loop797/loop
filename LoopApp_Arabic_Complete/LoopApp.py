import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import pygame
import os
import sys

# ---------------- إعداد المسارات ----------------
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ---------------- الإعدادات العامة ----------------
APP_TITLE = "أداة Loop"
DISCORD_URL = "https://discord.gg/DVTbMPnF"
AUDIO_FILE = resource_path("loop_music.wav")
LOGO_FILE = resource_path("LOGO.png")
BACKGROUND_FILE = resource_path("snow_background.gif")

# ---------------- إعداد الصوت ----------------
pygame.mixer.init()
if os.path.exists(AUDIO_FILE):
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

# ---------------- الوظائف ----------------
def open_discord():
    webbrowser.open(DISCORD_URL)

def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        music_button.config(text="▶️ تشغيل الموسيقى")
    else:
        pygame.mixer.music.unpause()
        music_button.config(text="⏸️ إيقاف الموسيقى")

def update_volume(val):
    pygame.mixer.music.set_volume(int(val) / 100)

def show_updates():
    updates = (
        "📌 التحديثات الأخيرة:
"
        "- تصميم عربي كامل
"
        "- تأثير ثلج أنيق في الخلفية
"
        "- تحكم بالصوت والموسيقى
"
        "- دعم ديسكورد + تحديثات"
    )
    messagebox.showinfo("📦 التحديثات", updates)

# ---------------- نافذة التطبيق ----------------
root = tk.Tk()
root.title(APP_TITLE)
root.geometry("700x500")
root.configure(bg="#121212")

# ---------------- الخلفية المتحركة ----------------
if os.path.exists(BACKGROUND_FILE):
    bg_frames = [tk.PhotoImage(file=BACKGROUND_FILE, format=f"gif -index {i}") for i in range(10)]
    bg_label = tk.Label(root)
    bg_label.place(relwidth=1, relheight=1)

    def animate(index=0):
        bg_label.configure(image=bg_frames[index])
        root.after(120, animate, (index + 1) % len(bg_frames))

    animate()

# ---------------- الإطار العام (يمين لليسار) ----------------
main_frame = tk.Frame(root, bg="#121212")
main_frame.pack(fill="both", expand=True)

# قائمة جانبية
sidebar = tk.Frame(main_frame, width=160, bg="#1c1c1c")
sidebar.pack(side="right", fill="y")

content = tk.Frame(main_frame, bg="#121212")
content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# ---------------- عناصر القائمة الجانبية ----------------
def create_sidebar_button(text, command):
    btn = tk.Button(sidebar, text=text, font=("Arial", 11, "bold"), fg="white", bg="#2c2c2c",
                    activebackground="#aa1c1c", activeforeground="white",
                    relief="flat", padx=10, pady=8, anchor="e", command=command)
    btn.pack(fill="x", pady=2)
    return btn

create_sidebar_button("🏠 الرئيسية", lambda: messagebox.showinfo(APP_TITLE, "مرحبًا بك في أداة Loop"))
music_button = create_sidebar_button("🎵 الموسيقى", toggle_music)
create_sidebar_button("🔊 مستوى الصوت", lambda: None)
create_sidebar_button("❄️ الخلفية", lambda: messagebox.showinfo("الخلفية", "الخلفية الثلجية تعمل الآن."))
create_sidebar_button("🔗 ديسكورد", open_discord)
create_sidebar_button("📝 التحديثات", show_updates)

# ---------------- عناصر المحتوى ----------------
title_label = tk.Label(content, text="مرحبًا بك في أداة Loop", fg="white", bg="#121212", font=("Arial", 18, "bold"))
title_label.pack(pady=10, anchor="e")

volume_label = tk.Label(content, text="🎚️ تحكم في مستوى الصوت", fg="lightgray", bg="#121212", font=("Arial", 12))
volume_label.pack(pady=(20, 5), anchor="e")

volume_slider = ttk.Scale(content, from_=0, to=100, orient="horizontal", command=update_volume)
volume_slider.set(50)
volume_slider.pack(fill="x", anchor="e")

welcome_label = tk.Label(content, text="🔊 أهلاً بك في أداة Loop", fg="gray", bg="#121212", font=("Arial", 11))
welcome_label.pack(pady=10, anchor="e")

# ---------------- تشغيل التطبيق ----------------
root.mainloop()
