from examples.customui.base.View import View


class Label(View):
    def __init__(self, text):
        self.text = text

    def update_text(self, new_text):
        self.text = new_text

    def show(self):
        return f"{self.text}"

    def __repr__(self):
        return self.show()
