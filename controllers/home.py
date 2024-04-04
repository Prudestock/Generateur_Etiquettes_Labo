class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        #self.frame.signout_btn.config(command=self.logout)
        pass

    def logout(self):
        #self.model.auth.logout()
        pass
