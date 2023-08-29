import tkinter as tk
import tkinter.ttk as ttk
from typing import Any
import sv_ttk

class CustomNameApp(tk.Tk):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.game_name = tk.StringVar()
        self.game_name.set("Discord Custom Game Name Editor")
        self.title(self.game_name.get())
        
        # Increase screen size
        self.state('zoomed')
        
        # Area where all frames will be placed
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        
        # Place all frames
        self.frames = {}
        for F in (PromptFrame, GameNameFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        # Show the first frame
        self.show_frame("PromptFrame")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()        
        
class PromptFrame(ttk.Frame):
    
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller
        
        # Configure frame grid
        self.rowconfigure(tuple(range(1,4)), weight=1)
        self.rowconfigure((0,4), weight=25)
        self.columnconfigure(tuple(range(3)), weight=1)
        
        # Prompt Text
        prompt_label = ttk.Label(self, text="Enter the name of the game you'd like to see displayed on your Discord status:")
        prompt_label.grid(row=1, column=1)
        
        # Prompt Entry
        self.prompt_entry = ttk.Entry(self, width = 80)
        self.prompt_entry.grid(row=2, column=1)
        self.prompt_entry.focus()
        
        # Prompt Button
        submit_button = ttk.Button(self, text = 'Submit', command = self.submit_button_command)
        submit_button.grid(row=3, column=1)
        controller.bind('<Return>', lambda event = None: submit_button.invoke()) 
        
    def submit_button_command(self):
        self.update_string_var()
        self.controller.show_frame("GameNameFrame")
        self.controller.title(self.controller.game_name.get())
        
    def update_string_var(self):
        self.controller.game_name.set(self.prompt_entry.get())
        

class GameNameFrame(ttk.Frame):
    
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        
        # Configure frame grid
        self.rowconfigure(tuple(range(1,5)), weight=1)
        self.rowconfigure(2, weight=5)
        self.rowconfigure((0,5), weight=25)
        self.columnconfigure(tuple(range(3)), weight=1)
        self.columnconfigure(1, weight=2)
        
        # Display confirmation message
        confirmation_label1 = ttk.Label(self, text="This window has been successfully renamed to:")
        confirmation_label1.grid(row=1,column=1)
        
        confirmation_label2 = ttk.Label(self, textvariable=controller.game_name, font=('Comic Sans', 36))
        confirmation_label2.grid(row=2,column=1)
        
        confirmation_label3 = ttk.Label(self, text="You can now *Add It* to Discord's Registered Games under Activity Settings!")
        confirmation_label3.grid(row=3,column=1)
        
        confirmation_label4 = ttk.Label(self, text="Feel free to minimize this window now, but don't close it otherwise Discord will no longer register it!")
        confirmation_label4.grid(row=4,column=1)

def main():
    app = CustomNameApp()
    sv_ttk.set_theme("dark")
    app.mainloop()

if __name__ == "__main__":
    main()