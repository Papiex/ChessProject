from controller import Controller
from view import View

if __name__ == "__main__":

    view = View()
    chess = Controller(view)
    run = chess.run_menu_selection()
