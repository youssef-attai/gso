from examples.customui.Button import Button


class IncrementButton(Button):
    def __init__(self):
        Button.__init__(self, text="+")
