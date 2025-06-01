import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class WorkoutForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.date_input = TextInput(hint_text="Date (YYYY-MM-DD)")
        self.exercise_input = TextInput(hint_text="Exercise Name")
        self.set_input = TextInput(hint_text="Set Order")
        self.reps_input = TextInput(hint_text="Reps")
        self.weight_input = TextInput(hint_text="Weight (kg)")

        self.add_widget(self.date_input)
        self.add_widget(self.exercise_input)
        self.add_widget(self.set_input)
        self.add_widget(self.reps_input)
        self.add_widget(self.weight_input)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.submit_workout)
        self.add_widget(self.submit_button)

    def submit_workout(self, instance):
        date = self.date_input.text
        exercise_input = self.exercise_input.text
        set_order = int(self.set_input.text)
        reps = int(self.reps_input.text)
        weight = float(self.weight_input.text)

        data = {
            "date": date,
            "exercise_name": exercise_input,
            "set_order": set_order,
            "reps": reps,
            "weight": weight
        }

        try:
            response = requests.post("http://127.0.0.1:8000/workouts", json=data)
            print("Workout submitted:", response.status_code, response.text)
        except Exception as e:
            print("Error sending workout:", e)

        self.date_input.text = ""
        self.exercise_input.text = ""
        self.set_input.text = ""
        self.reps_input.text = ""
        self.weight_input.text = ""

class WorkoutApp(App):
    def build(self):
        return WorkoutForm()
    
if __name__ == "__main__":
    WorkoutApp().run()