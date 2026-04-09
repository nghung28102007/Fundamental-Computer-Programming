#1
import requests 
url = 'https://api.chucknorris.io/jokes/random'
try:
    response = requests.get(url)
    joke = response.json()
    print(joke['value'])
except:
    print("Error")
#2
key = '4b501d493663e144467a3d93beaa1dd6'

try:
    user_city = input("Enter the city name:")
    url1 = f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={key}&units=metric"
    data = requests.get(url1)
    weather = data.json()
    print("current weather is:",weather['weather'][0]['description'])
    print("the temperature is:",weather['main']['temp'])
    
except Exception as e:
    print(f"Error is: {e}")

#3
from flask import Flask, jsonify
app = Flask(__name__)
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>')
def prime_api(number):
    is_it_prime = check_prime(number)

    data = {
        "Number": number,
        "isPrime": is_it_prime
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run()


#4
import json
from flask import Flask, jsonify
app = Flask(__name__)

def airport_search(icao_search):
    with open('airports.json', 'r') as search:
        data = json.load(search)
    for airport in data:
        if airport['icao'].upper() == icao_search.upper():
            return airport
    return None

@app.route('/airport/<icao>')
def return_airport(icao):
    search = airport_search(icao)
    if search:
        return jsonify(search)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)






