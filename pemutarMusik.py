import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    pygame.mixer.music.load(selected_file)
    pygame.mixer.music.play()

def choose_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if selected_file:
        label_selected_file.config(text=f"File terpilih: {selected_file}")

pygame.mixer.init()

root = tk.Tk()
root.title("Aplikasi Pemutar Musik")
root.geometry("500x400")  
root.resizable(False, False)


label_selected_file = tk.Label(root, text="Choosen File: -", font=("Arial", 12), bg="#333333", fg="#ffffff")
label_selected_file.pack(pady=10)

button_choose_file = tk.Button(root, text="Choose File", command=choose_file, font=("Arial", 14))
button_choose_file.pack(pady=5)

button_play = tk.Button(root, text="Play", command=play_music, font=("Arial", 14))
button_play.pack(pady=5)

def set_dark_theme():
    root.config(bg="#333333")  
    label_selected_file.config(bg="#333333", fg="#ffffff") 
    button_choose_file.config(bg="#444444", fg="#ffffff", activebackground="#555555")  
    button_play.config(bg="#444444", fg="#ffffff", activebackground="#555555")  
    button_dark_theme.config(text="Light theme", command=set_light_theme)  

def set_light_theme():
    root.config(bg="white")  
    label_selected_file.config(bg="white", fg="black") 
    button_choose_file.config(bg="lightgray", fg="black", activebackground="gray")  
    button_play.config(bg="lightgray", fg="black", activebackground="gray")  
    button_dark_theme.config(text="Tema Gelap", command=set_dark_theme)  

button_dark_theme = tk.Button(root, text="Dark Theme", command=set_dark_theme, font=("Arial", 14))
button_dark_theme.pack(pady=5)

root.mainloop()
