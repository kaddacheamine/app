ffrom kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(400, 600))

        # Create the text input for displaying the result
        self.result_input = TextInput(font_size=32, halign='right', readonly=True, multiline=False)
        layout.add_widget(self.result_input)

        # Create the button grid
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['C']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current_text = self.result_input.text

        if instance.text == '=':
            try:
                result = str(eval(current_text))
                self.result_input.text = result
            except Exception as e:
                self.result_input.text = 'Error'
        elif instance.text == 'C':
            self.result_input.text = ''
        else:
            self.result_input.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()
