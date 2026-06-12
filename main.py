from kivy.app import App
from kivy. uix. boxlayout import BoxLayout
from kivy. uix. button import Button
from kivy. uix. textinput import TextInput
import numpy as np

# ===== CORE =====
def tent_keystream(N, x0, mu):
    epsilon = 1e-12
    x = x0
    K = np.zeros(N, dtype=np.uint8)

    for _ in range(100):
        x = mu*x if x < 0.5 else mu*(1-x)
        x = (x + epsilon) % 1

    for i in range(N):
        x = mu*x if x < 0.5 else mu*(1-x)
        x = (x + epsilon) % 1
        K[i] = int((x * 1e6) % 256)

    return K

# ===== UI =====
class MyLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.x0 = TextInput(hint_text="x0")
        self.mu = TextInput(hint_text="mu")

        btn = Button(text="Encrypt")
        btn.bind(on_press=self.encrypt)

        layout.add_widget(self.x0)
        layout.add_widget(self.mu)
        layout.add_widget(btn)

        return layout

    def encrypt(self, instance):
        x0 = float(self.x0.text)
        mu = float(self.mu.text)

        data = np.array([1,2,3,4], dtype=np.uint8)
        K = tent_keystream(len(data), x0, mu)

        print("Encrypted:", np.bitwise_xor(data, K))

MyApp().run()
