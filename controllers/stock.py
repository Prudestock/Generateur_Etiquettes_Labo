class LabelController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["label"]
        self._bind()

    def _bind(self):
        pass