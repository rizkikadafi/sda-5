from utils.app import *


def main():
    if Confirm.ask("\n[bold]Keluar Program"):
        return program1.stop()


title = "[text_title]Program 1: Title Program 1"  # untuk di tampilkan sebagai judul
name = "Nama Program 1"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 list 1.
🔷 list 2. 
🔷 list 3.\n"""  # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
