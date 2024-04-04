from main import Model
from .home import HomeController


class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)

        self.model.auth.add_event_listener(
            "auth_changed", self.auth_state_listener
        )


    def start(self):
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("signin")

        self.view.start_mainloop()