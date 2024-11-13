from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import requests

class WeatherApp(App):
    def build(self):
        self.api_key = "04a2fa20419dafbd3d7330a04c906330"

        self.username = "Goldliak47"
        
        self.password = "123456789"

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        layout.add_widget(Label(text="Enter the city name:"))
        self.city_entry = TextInput(multiline=False)
        layout.add_widget(self.city_entry)

        get_weather_button = Button(text="Get Weather")
        get_weather_button.bind(on_press=self.get_weather)
        layout.add_widget(get_weather_button)

        self.weather_label = Label(text="Weather:")
        layout.add_widget(self.weather_label)

        self.temperature_label = Label(text="Temperature:")
        layout.add_widget(self.temperature_label)

        self.humidity_label = Label(text="Humidity:")
        layout.add_widget(self.humidity_label)

        self.wind_speed_label = Label(text="Wind Speed:")
        layout.add_widget(self.wind_speed_label)

        return layout

    def get_weather(self, instance):
        city = self.city_entry.text
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            self.weather_label.text = f"Weather: {data['weather'][0]['description']}"
            temperature_celsius = data['main']['temp'] - 273.15
            self.temperature_label.text = f"Temperature: {temperature_celsius:.2f}°C"
            self.humidity_label.text = f"Humidity: {data['main']['humidity']}%"
            self.wind_speed_label.text = f"Wind Speed: {data['wind']['speed']} m/s"

        except requests.RequestException as e:
            self.show_error_popup(f"Could not get the weather data. Error: {e}")

    def show_error_popup(self, error_message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=error_message))

        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    WeatherApp().run()
