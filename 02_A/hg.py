from breezypythongui import EasyFrame
import tkinter as tk
from tkinter import font
from game_logic import HangmanGame
from PIL import Image, ImageTk
import os
import pygame

class HangmanGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Hangman's Game (Wild West Edition)", width=1200, height=700, background="black")
        self.master.resizable(True, True) 
        
        self.mode = "MAIN_MENU" # MAIN_MENU, GAME, FINISHED
        self.p1_done = False # Has player 1 set the word?
        self.game = None 
        self.waiting_for_finish = False
        
        # --- Music Setup ---
        pygame.mixer.init()
        self.music_on = True
        self.music_loaded = False
        self.music_path = "assets/bgm.mp3"
        self.init_music()
        
        # Fonts
        self.chalk_font = font.Font(family="Courier New", size=18, weight="bold")
        self.title_font = font.Font(family="Times New Roman", size=36, weight="bold")
        self.word_font = font.Font(family="Consolas", size=28, weight="bold")
        self.input_font = font.Font(family="Courier New", size=14, weight="bold")
        self.clue_font = font.Font(family="Courier New", size=20, weight="bold", slant="italic")
        
        # --- Resources ---
        self.raw_bg_image = self.load_raw_image()
        self.assets = {"bg": None}

        # --- UI Layout ---
        self.canvas = self.addCanvas(row=0, column=0, width=1200, height=700, background="black")
        self.canvas.grid(sticky="NSEW")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.buttons = {}
        self.p1_widgets = [] 
        self.menu_widgets = []
        
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.bind("<Button-1>", self.on_click)
        self.master.bind("<Key>", self.on_key)
        
    def init_music(self):
        if os.path.exists(self.music_path):
            try:
                pygame.mixer.music.load(self.music_path)
                pygame.mixer.music.play(-1) # Loop indefinitely
                self.music_loaded = True
                if not self.music_on:
                    pygame.mixer.music.pause()
            except Exception as e:
                print(f"Music load error: {e}")
        else:
            # Check for .wav fallback
            wav_path = "assets/music.wav"
            if os.path.exists(wav_path):
                try:
                    pygame.mixer.music.load(wav_path)
                    pygame.mixer.music.play(-1)
                    self.music_loaded = True
                except: pass

    def toggle_music(self):
        if not self.music_loaded:
            self.messageBox(title="No Music", message="Partner, you need to add 'bgm.mp3' to your assets folder first!")
            return
        
        self.music_on = not self.music_on
        if self.music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.draw_whole_screen(self.canvas.winfo_width(), self.canvas.winfo_height())
        
    def load_raw_image(self):
        try:
            bg_path = "assets/background.png"
            if os.path.exists(bg_path):
                return Image.open(bg_path)
        except Exception as e:
            print(f"Asset load error: {e}")
        return None

    def on_resize(self, event=None):
        if event:
            w, h = event.width, event.height
        else:
            w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
            
        if w < 100: w = 1200 # Fallback for unmapped window
        if h < 100: h = 700
        
        if self.raw_bg_image:
            resized = self.raw_bg_image.resize((w, h), Image.Resampling.LANCZOS)
            self.assets["bg"] = ImageTk.PhotoImage(resized)
        self.draw_whole_screen(w, h)

    def clear_all_widgets(self):
        # 1. Clear P1 Widgets
        for w in self.p1_widgets:
            try: w.destroy()
            except: pass
        self.p1_widgets = []

        # 2. Clear P2 Widgets
        for btn in self.buttons.values():
            try: btn.destroy()
            except: pass
        self.buttons = {}
        
        # Destroy specific widget attributes if they exist
        for attr in ['restart_btn_widget', 'menu_btn_widget', 'exit_btn_widget', 'game_music_btn', 'music_toggle_btn']:
            if hasattr(self, attr) and getattr(self, attr):
                try: getattr(self, attr).destroy()
                except: pass
                setattr(self, attr, None)

        # 3. Clear Menu Widgets
        for w in self.menu_widgets:
            try: w.destroy()
            except: pass
        self.menu_widgets = []

    def draw_whole_screen(self, w, h):
        self.canvas.delete("all")
        self.clear_all_widgets()
        
        if self.assets["bg"]:
            self.canvas.create_image(0, 0, image=self.assets["bg"], anchor="nw")
            
        self.draw_music_toggle(w, h)

        if self.mode == "MAIN_MENU":
            self.draw_main_menu(w, h)
        elif self.mode == "FINISHED":
            self.draw_finished_screen(w, h)
        elif self.mode == "HOW_TO_PLAY":
            self.draw_how_to_play_screen(w, h)
        elif self.mode == "RULES":
            self.draw_rules_screen(w, h)
        else:
            # Draw Divider (Solid Line)
            self.canvas.create_line(w//2, 50, w//2, h-50, fill="#3e2723", width=3)
            self.draw_player1_side(w, h)
            self.draw_player2_side(w, h)

    def draw_finished_screen(self, w, h):
        cx, cy = w // 2, h // 2
        
        # Determine Message and Colors
        if self.game.won:
            msg = "YOU WON!!"
            color = "#1b5e20" # Deep Green
            sub_msg = "The bounty is yours, partner!"
        else:
            msg = "DEFEATED!"
            color = "#b71c1c" # Deep Red
            sub_msg = f"Word: '{self.game.word}'\nBetter luck next time!"

        # Background Box for Results
        box_w, box_h = 600, 350
        self.canvas.create_rectangle(cx - box_w//2, cy - 150, cx + box_w//2, cy + 200, 
                                    fill="#fdf5e6", outline="#8d6e63", width=5)
        
        # Result Title
        self.canvas.create_text(cx, cy - 80, text=msg, fill=color, font=("Times New Roman", 60, "bold"))
        self.canvas.create_text(cx, cy + 10, text=sub_msg, fill="#3e2723", font=("Courier New", 20, "bold"), justify="center")

        # Buttons
        btn_style = {"font": ("Courier New", 18, "bold"), "width": 20, "bg": "#ffcc80", "fg": "black", "relief": "raised"}
        
        # New Bounty Button
        btn_restart = tk.Button(self.canvas, text="NEW BOUNTY", command=self.reset_gui_state, **btn_style)
        self.canvas.create_window(cx, cy + 100, window=btn_restart)
        self.restart_btn_widget = btn_restart

        # Main Menu Button
        btn_menu = tk.Button(self.canvas, text="MAIN MENU", command=self.back_to_menu, **btn_style)
        btn_menu.config(bg="#ef5350", fg="white") # Red for menu
        self.canvas.create_window(cx, cy + 160, window=btn_menu)
        self.menu_btn_widget = btn_menu

    def draw_music_toggle(self, w, h):
        # Global Music Toggle (Visible to everyone)
        music_sym = "🔊" if self.music_on else "🔇"
        bg_col = "#a5d6a7" if (self.music_on and self.music_loaded) else "#ef9a9a"
        self.music_toggle_btn = tk.Button(self.canvas, text=music_sym, command=self.toggle_music,
                                        font=("Arial", 16), bg=bg_col, width=3)
        self.canvas.create_window(w - 20, 20, window=self.music_toggle_btn, anchor="ne")

    def draw_main_menu(self, w, h):
        cx, cy = w // 2, h // 2
        
        # Title
        self.canvas.create_text(cx, cy - 180, text="HANGMAN: WILD WEST", font=("Times New Roman", 60, "bold"), fill="#3e2723")
        
        # Menu Background Box - Make it slightly smaller since we have fewer buttons
        box_w, box_h = 420, 260
        self.canvas.create_rectangle(cx - box_w//2, cy - 110, cx + box_w//2, cy + 150, fill="#fdf5e6", outline="#8d6e63", width=4)
        
        btn_style = {"font": ("Courier New", 14, "bold"), "width": 25, "bg": "#ffcc80", "fg": "black", "relief": "raised"}
        
        # Play Button
        btn_play = tk.Button(self.canvas, text="PLAY GAME", command=self.start_setup, **btn_style)
        self.canvas.create_window(cx, cy - 50, window=btn_play)
        self.menu_widgets.append(btn_play)
        
        # How to Play Button
        btn_how = tk.Button(self.canvas, text="HOW TO PLAY", command=self.show_how_to_play, **btn_style)
        self.canvas.create_window(cx, cy + 5, window=btn_how)
        self.menu_widgets.append(btn_how)
        
        # Rules Button
        btn_rules = tk.Button(self.canvas, text="RULES", command=self.show_rules, **btn_style)
        self.canvas.create_window(cx, cy + 60, window=btn_rules)
        self.menu_widgets.append(btn_rules)
        
        # Exit Button
        btn_exit = tk.Button(self.canvas, text="EXIT", command=self.master.destroy, **btn_style)
        self.canvas.create_window(cx, cy + 115, window=btn_exit)
        self.menu_widgets.append(btn_exit)

    def start_setup(self):
        self.mode = "GAME"
        self.p1_done = False
        self.draw_whole_screen(self.canvas.winfo_width(), self.canvas.winfo_height())

    def show_how_to_play(self):
        self.mode = "HOW_TO_PLAY"
        self.on_resize()

    def show_rules(self):
        self.mode = "RULES"
        self.on_resize()

    def draw_how_to_play_screen(self, w, h):
        items = [
            "1. Player 1 sets the target word and a hint.",
            "2. Player 1 locks the bounty.",
            "3. Player 2 tries to guess the word letter by letter.",
            "4. If the man is fully drawn, Player 2 loses!"
        ]
        self.draw_overlay_screen(w, h, "HOW TO PLAY", items)

    def draw_rules_screen(self, w, h):
        items = [
            "1. Words can include letters, numbers, and spaces.",
            "2. Player 2 has 6 attempts before losing.",
            "3. The hint is visible to Player 2.",
            "4. Be fair with your hints, partner!"
        ]
        self.draw_overlay_screen(w, h, "RULES", items)

    def draw_overlay_screen(self, w, h, title, items):
        cx, cy = w // 2, h // 2
        
        # Create semi-transparent overlay using PIL
        overlay_w, overlay_h = int(w * 0.8), int(h * 0.7)
        overlay_img = Image.new('RGBA', (overlay_w, overlay_h), (0, 0, 0, 180)) # Darker alpha
        self.overlay_photo = ImageTk.PhotoImage(overlay_img)
        self.canvas.create_image(cx, cy, image=self.overlay_photo)

        # Title
        self.canvas.create_text(cx, cy - overlay_h//2 + 60, text=title, 
                                font=("Times New Roman", 48, "bold"), fill="white")

        # Items
        start_y = cy - 50
        for i, item in enumerate(items):
            self.canvas.create_text(cx, start_y + i * 45, text=item, 
                                    font=("Courier New", 18, "bold"), fill="white", justify="center")

        # Footer
        self.canvas.create_text(cx, cy + overlay_h//2 - 60, text="Press any key or click to return to Menu", 
                                font=("Courier New", 14, "bold"), fill="white")

    def on_click(self, event):
        if self.mode in ["HOW_TO_PLAY", "RULES"]:
            self.back_to_menu()

    def on_key(self, event):
        if self.mode in ["HOW_TO_PLAY", "RULES"]:
            self.back_to_menu()

    def back_to_menu(self):
        # Force a clean state transition
        self.mode = "MAIN_MENU"
        self.p1_done = False
        self.game = None
        self.saved_word = ""
        self.saved_hint = ""
        # Re-draw the entire screen
        self.on_resize(None) 

    def draw_player1_side(self, w, h):
        cx = w // 4
        
        # Back Button (Always visible on P1 side during setup or while locked)
        btn_back = tk.Button(self.canvas, text=" MENU", command=self.back_to_menu,
                            font=("Courier New", 12, "bold"), bg="#ef5350", fg="white")
        self.canvas.create_window(50, 30, window=btn_back, anchor="nw")
        self.p1_widgets.append(btn_back)

        if not self.p1_done:
            # Title
            self.canvas.create_text(cx, 80, text="THE LAW IS CLOSING IN", font=self.title_font, fill="#3e2723")
            self.canvas.create_text(cx, 120, text="Set the bounty to trap the cowboy!", font=self.input_font, fill="#5d4037")
            
            # Word Input
            self.canvas.create_text(cx, 160, text="Enter Target Word:", font=self.chalk_font, fill="black")
            word_val = getattr(self, 'saved_word', "")
            self.word_entry = tk.Entry(self.canvas, font=self.input_font, width=25, bg="#d7ccc8", fg="black")
            self.word_entry.insert(0, word_val)
            self.canvas.create_window(cx, 200, window=self.word_entry)
            self.p1_widgets.append(self.word_entry)

            # Hint Input
            self.canvas.create_text(cx, 260, text="Enter a Hint:", font=self.chalk_font, fill="black")
            hint_val = getattr(self, 'saved_hint', "")
            self.hint_entry = tk.Entry(self.canvas, font=self.input_font, width=25, bg="#ffe0b2", fg="black")
            self.hint_entry.insert(0, hint_val)
            self.canvas.create_window(cx, 300, window=self.hint_entry)
            self.p1_widgets.append(self.hint_entry)

            # Set Bounty Button
            btn = tk.Button(self.canvas, text="SET BOUNTY", 
                            command=self.set_bounty, font=("Courier New", 18, "bold"),
                            bg="#ffcc80", fg="black")
            self.canvas.create_window(cx, 380, window=btn)
            self.p1_widgets.append(btn)
        else:
            # P1 is done - Solid Opaque Panel to hide words entirely
            self.canvas.create_rectangle(10, 50, w//2 - 5, h-10, fill="#3e2723", outline="#212121", width=2)
            self.canvas.create_text(cx, h//2 - 40, text="BOUNTY ACTIVE", font=self.title_font, fill="#ffcc80")
            self.canvas.create_text(cx, h//2 + 20, text="Target word is hidden.\nGood luck, Player 2!", font=self.chalk_font, fill="white", justify="center")

    def set_bounty(self):
        word = self.word_entry.get().strip()
        hint = self.hint_entry.get().strip()
        
        if not word:
            return 
            
        self.saved_word = word
        self.saved_hint = hint
        self.p1_done = True
        
        # Init Game logic
        self.game = HangmanGame([word], common_clue=hint)
        
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        self.draw_whole_screen(w, h)

    def draw_player2_side(self, w, h):
        cx = int(w * 0.75)
        
        if not self.p1_done:
            self.canvas.create_text(cx, h//2, text="WAITING FOR PLAYER 1...", font=self.chalk_font, fill="#5d4037")
            return

        if self.game.finished and self.mode == "FINISHED":
            return

        # Player 2 is active
        # 1. Title & Hint
        self.canvas.create_text(cx, 60, text="SAVE THE COWBOY!", font=self.title_font, fill="#3e2723")
        self.canvas.create_text(cx, 90, text="Guess the secret word to cut the rope!", font=self.input_font, fill="#8d6e63")
        if self.game.clue:
            self.canvas.create_text(cx, 130, text=f"HINT: {self.game.clue}", font=self.clue_font, fill="#d84315")

        # 2. Word Display
        spaced_word = " ".join(list(self.game.current_state))
        self.canvas.create_text(cx, 160, text=spaced_word, font=self.word_font, fill="#212121")

        # 3. Hangman (further up)
        self.draw_hangman(cx + 100, 380)

        # 4. Keyboard (further down)
        self.draw_keyboard(cx - 160, 420)

    def draw_keyboard(self, start_x, start_y):
        # Only draw if not finished (including the delay period)
        if self.game.finished: return

        cols = 9 # More columns to save vertical space
        gap = 5
        btn_size = 35 
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 " + "!?,.-'\"@#()&/[]"
        
        for i, char in enumerate(letters):
            r = i // cols
            c = i % cols
            x = start_x + c * (btn_size + gap)
            y = start_y + r * (btn_size + gap)
            
            display_char = char if char != " " else "SPCE"
            btn_font = ("Courier New", 8, "bold") if char == " " else ("Courier New", 10, "bold")
            
            state = "disabled" if char in self.game.guesses else "normal"
            bg_color = "#8d6e63" if char in self.game.guesses else "#d7ccc8"
            
            btn = tk.Button(self.canvas, text=display_char, font=btn_font,
                            command=lambda ch=char: self.guess_letter(ch),
                            bg=bg_color, relief="raised", state=state)
            
            self.canvas.create_window(x, y, window=btn, width=btn_size, height=btn_size, anchor="nw")
            self.buttons[char] = btn

    def draw_hangman(self, center_x, base_y):
        # Scale down slightly for split screen
        scale = 0.7
        # Pole
        self.canvas.create_line(center_x-70, base_y, center_x-70, base_y-250*scale, fill="black", width=6) 
        self.canvas.create_line(center_x-70, base_y-250*scale, center_x+35, base_y-250*scale, fill="black", width=6)
        self.canvas.create_line(center_x+35, base_y-250*scale, center_x+35, base_y-180*scale, fill="#8d6e63", width=3) 

        err = self.game.errors
        head_cx, head_cy = center_x+35, base_y-160*scale
        
        if err >= 1: # Head + Cowboy Hat
            # Head
            self.canvas.create_oval(head_cx-25*scale, head_cy-25*scale, head_cx+25*scale, head_cy+25*scale, outline="black", width=3)
            # Cowboy Hat
            # Brim
            self.canvas.create_oval(head_cx-35*scale, head_cy-35*scale, head_cx+35*scale, head_cy-25*scale, fill="brown", outline="black", width=2)
            # Top of hat
            self.canvas.create_rectangle(head_cx-20*scale, head_cy-55*scale, head_cx+20*scale, head_cy-30*scale, fill="brown", outline="black", width=2)

        if err >= 2: # Body
            self.canvas.create_line(head_cx, head_cy+25*scale, head_cx, head_cy+100*scale, fill="black", width=3)
        if err >= 3: # L Arm
            self.canvas.create_line(head_cx, head_cy+40*scale, head_cx-30*scale, head_cy+80*scale, fill="black", width=3)
        if err >= 4: # R Arm
            self.canvas.create_line(head_cx, head_cy+40*scale, head_cx+30*scale, head_cy+80*scale, fill="black", width=3)
        if err >= 5: # L Leg
            self.canvas.create_line(head_cx, head_cy+100*scale, head_cx-30*scale, head_cy+150*scale, fill="black", width=3)
        if err >= 6: # R Leg
            self.canvas.create_line(head_cx, head_cy+100*scale, head_cx+30*scale, head_cy+150*scale, fill="black", width=3)

    def guess_letter(self, char):
        if self.waiting_for_finish: return
        
        if self.game.guess(char):
            # Update UI immediately to show current state (revealed letters or new error)
            self.draw_whole_screen(self.canvas.winfo_width(), self.canvas.winfo_height())
            
            if self.game.finished:
                self.waiting_for_finish = True
                # If lost, wait 3 seconds to show the final leg
                if self.game.lost:
                    self.after(3000, self.finish_game)
                else:
                    self.finish_game()

    def finish_game(self):
        self.waiting_for_finish = False
        self.mode = "FINISHED"
        self.draw_whole_screen(self.canvas.winfo_width(), self.canvas.winfo_height())

    def reset_gui_state(self):
        self.mode = "GAME"
        self.p1_done = False
        self.game = None
        self.saved_word = ""
        self.saved_hint = ""
        self.draw_whole_screen(self.canvas.winfo_width(), self.canvas.winfo_height())

if __name__ == "__main__":
    app = HangmanGUI()
    app.mainloop()
