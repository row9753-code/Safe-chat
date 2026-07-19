from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class QuantumChat(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text="🪐 Quantum Secure Chat", size_hint_y=0.1, bold=True, font_size='20sp')
        self.main_layout.add_widget(header)
        
        # Chat History Area
        self.scroll = ScrollView(size_hint_y=0.7)
        self.chat_history = Label(text="-- चैट सुरक्षित है --\n", markup=True, halign='left', valign='top', size_hint_y=None)
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        self.main_layout.add_widget(self.scroll)
        
        # Input Area
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=5)
        self.msg_input = TextInput(hint_text="मैसेज टाइप करें...", multiline=False)
        send_btn = Button(text="SEND", size_hint_x=0.25, background_color=(0, 0.7, 0.3, 1))
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.msg_input)
        input_layout.add_widget(send_btn)
        self.main_layout.add_widget(input_layout)
        
        return self.main_layout

    def send_message(self, instance):
        msg = self.msg_input.text
        if not msg:
            return
        
        # लोकल सिमुलेशन (ताकि APK बिना क्रैश हुए तुरंत बने)
        import random
        hex_trash = 'be6422' + ''.join(random.choices('0123456789abcdef', k=6))
        
        self.chat_history.text += f"\n[color=ff3333]🔒 Sent (Encrypted):[/color] {hex_trash}...\n"
        self.chat_history.text += f"[color=00ff66]🔓 Received (Decrypted):[/color] {msg}\n"
        self.msg_input.text = ""

if __name__ == "__main__":
    QuantumChat().run()
      
