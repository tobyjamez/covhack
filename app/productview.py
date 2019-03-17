from kivy.uix.button import Button
from comm import add

class ProductView(Button):
    def __init__(self, data_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = data_dict['name']
        self.text = str(data_dict['name'] +
                        " | " + data_dict['price'] +
                        " | " + data_dict['provider'])

    def on_press(self):
        super().on_press()
        try:
            response = add(self.name)
        except:
            return None
        if response != 200:
            self.text += " ERROR: Cannot add to basket"
