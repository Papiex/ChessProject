from controllers.main_controller import Controller
from views.main_view import View


if __name__ == "__main__":

    view = View()
    chess = Controller(view)
    run = chess.run_main_menu_selection()
