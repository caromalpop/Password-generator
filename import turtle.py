import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# K-pop groups
kpop_groups = ["BTS", "BLACKPINK", "TWICE", "EXO", "SEVENTEEN"]
votes = {group: 0 for group in kpop_groups}

def vote(group):
    votes[group] += 1
    vote_labels[group].config(text=f"Votes: {votes[group]}")
    update_progress()

def update_progress():
    max_votes = max(votes.values()) if max(votes.values()) > 0 else 1
    for group in kpop_groups:
        progress_bars[group]['value'] = (votes[group] / max_votes) * 100

def show_winner():
    max_votes_count = max(votes.values())
    winners = [g for g, v in votes.items() if v == max_votes_count]
    if len(winners) == 1:
        messagebox.showinfo("🏆 Winner 🏆", f"The winner is {winners[0]} with {max_votes_count} votes!")
    else:
        messagebox.showinfo("🏆 It's a tie! 🏆", f"Tie between: {', '.join(winners)} with {max_votes_count} votes each!")

# GUI
root = tk.Tk()
root.title("🎤 Kpop Voting! 🎤")
root.geometry("900x600")
root.config(bg="#ffe6f0")

title = tk.Label(root, text="Kpop Voting!", font=("Impact", 36, "bold"), fg="#ff1493", bg="#ffe6f0")
title.pack(pady=20)

frame = tk.Frame(root, bg="#ffe6f0")
frame.pack()

vote_labels = {}
progress_bars = {}

for i, group in enumerate(kpop_groups):
    sub_frame = tk.Frame(frame, bg="#ffe6f0")
    sub_frame.grid(row=0, column=i, padx=10)
    
    placeholder = tk.Label(sub_frame, text=group, bg="#ffb6c1", width=15, height=7, font=("Helvetica", 12, "bold"))
    placeholder.pack()
    
    btn = tk.Button(sub_frame, text="Vote ❤️", command=lambda g=group: vote(g), bg="#ff69b4", font=("Helvetica", 12, "bold"))
    btn.pack(pady=5)
    
    vote_label = tk.Label(sub_frame, text="Votes: 0", font=("Helvetica", 12), bg="#ffe6f0")
    vote_label.pack()
    vote_labels[group] = vote_label
    
    pb = ttk.Progressbar(sub_frame, length=120, mode='determinate')
    pb.pack(pady=5)
    progress_bars[group] = pb

winner_btn = tk.Button(root, text="Show Winner 🏆", command=show_winner, font=("Helvetica", 16, "bold"), bg="#90ee90")
winner_btn.pack(pady=20)

root.mainloop()

