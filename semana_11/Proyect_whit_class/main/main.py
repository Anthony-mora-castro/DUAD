import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from menu.show_menu import show_menu

def main():
    show_menu()

if __name__ == "__main__":
    main()


