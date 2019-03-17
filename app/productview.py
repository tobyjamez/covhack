from kivy.uix.button import Button

class ProductView(Button):
    def __init__(self, data_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = str(data_dict['name'] +
                        " | " + data_dict['price'] +
                        " | " + data_dict['provider'])
