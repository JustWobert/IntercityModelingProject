import os
import tkinter as tk
import FileReader

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Reader Application")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Enter file path:")
        self.label.pack(pady=10)

        self.file_path_entry = tk.Entry(self, width=50)
        self.file_path_entry.pack(pady=5)

        self.read_button = tk.Button(self, text="Read File", command=self.read_file)
        self.read_button.pack(pady=10)

        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.pack(pady=5)

        self.mainloop()

    def read_file(self):
        file_path = self.file_path_entry.get()
        if not file_path:
            file_path = "UKRailStationPopPlace.csv"
            print("File not provided [code 309] : using default data")
        elif not os.path.isfile(file_path):
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "File Read Error [code 404] : invalid file path. are you sure the file location is correct?")
            return

        Pairs = FileReader.FileReader(file_path)
        pairs_list = Pairs.read_file()

        if Pairs.listOfPairs is not None:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, pairs_list)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "File Read Error [code 400] : are you sure the file isn't empty?")


run_app = Application()