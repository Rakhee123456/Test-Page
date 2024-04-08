import random

weather_data = {
    "Sunday":28,
    "Tuesday" : 23,
    "Wednesday" : 18,
    "Thrusday" : 15,
    "Friday" : 20,
}

def predict_weather(temperature):
    if temperature > 25:
        return "Sunny"
    elif temperature > 18:
        return "Cloudy"
    else:
        return "Rainy"
    
for day, temp in weather_data.items():
    predicted_weather= predict_weather(temp)
    if random.random()<0.2:
        unexpected_event = ["metear shower ", "alien invasion"]
        predicted_weather = random.choice(unexpected_event)

print(f"Predicted weather for {day} : {predicted_weather}")

#now predict for new , unseen day(saturday)

new_day = "Saturday"
new_temperature = 22
predicted_weather = predict_weather(new_temperature)
print(f"\n Predicted weather for {new_day} : {predicted_weather}")