import requests
import matplotlib.pyplot as plt

<<<<<<< HEAD
# Function to get weather data
=======

>>>>>>> c162d26 (Initial commit: Added expense tracker project)
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

<<<<<<< HEAD
    # Check if the request was successful
=======
    
>>>>>>> c162d26 (Initial commit: Added expense tracker project)
    if response.status_code == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    else:
        print(f"Failed to get weather data for {city}. Error: {data.get('message', 'Unknown error')}")
        return None, None

<<<<<<< HEAD
# Main function
def main():
    api_key = "596d7eb06751e8aace53bf36c4e16da3"  # Your actual API key
=======

def main():
    api_key = "596d7eb06751e8aace53bf36c4e16da3"  
>>>>>>> c162d26 (Initial commit: Added expense tracker project)
    cities = ["New York", "London", "Tokyo", "Sydney", "Moscow"]
    temperatures = []
    descriptions = []

    for city in cities:
        temp, desc = get_weather(city, api_key)
        if temp is not None:
            temperatures.append(temp)
            descriptions.append(desc)
            print(f"City: {city}, Temperature: {temp}°C, Description: {desc}")

<<<<<<< HEAD
    # Plotting the results
    if temperatures:  # Only plot if we have temperature data
=======
    
    if temperatures:  
>>>>>>> c162d26 (Initial commit: Added expense tracker project)
        plt.bar(cities, temperatures, color='blue')
        plt.xlabel('Cities')
        plt.ylabel('Temperature (°C)')
        plt.title('Weather Data Aggregator')
        plt.show()

<<<<<<< HEAD
# Ensure the main function runs when the script is executed
=======

>>>>>>> c162d26 (Initial commit: Added expense tracker project)
if __name__ == "__main__":
    main()






