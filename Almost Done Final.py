import json, requests

print("Welcome to weather program made by Hunter Brooks")

base_url = "https://api.openweathermap.org/data/2.5/weather"

apikey = "366a5432e9b6656a17ef9c9ff1433891"

#Check api connection test
response = ""
i = 0
try:
  city = "Chicago"
  zipcode = "60007"
  response = requests.get(
    f"{base_url}?q={city},{zipcode}&units=imperial&APPID={apikey}")

except:
  print("API connection has failed")

else:
  print("API connection has succeeded!")

#Double Check Connection
if (response.status_code == 200):
  print()
  print("Backup check: Connection was a success")

elif (response.status_code == 400):
  print("Backup check: Connection failed")

if i == 3:
  print("Final attempt to connect!")
  print()
  print("If this fails please restart program.")

#Enter city or zipcode
pickone = ""
again = ""
while again != "stop":
  print()

  #Ask user which they would like to enter in
  print("Please enter whether you want to enter a city or zipcode.")
  pickone = input("Please type the word city or zipcode: ")

  #if they picked city
  if pickone == "city":
    city = input("Enter a city: ")
    url = f"{base_url}?q={city}&units=imperial&APPID={apikey}"

  #If they picked zipcode
  if pickone == "zipcode":
    zipcode = 0
    while True:
      try:
        zipcode = int(input("Enter a zipcode: "))
      except ValueError:
        print("Zipcode must be a valid integer.")
        continue
      else:
        break
    url = f"{base_url}?q={zipcode}&units=imperial&APPID={apikey}"

  #Print the connection url
  #print(url)
  print()

  #print out all the stuffs
  response = requests.get(url)
  unformated_data = response.json()

  #print(unformated_data)

  temp = unformated_data["main"]["temp"]
  print(f"The current temp is: {temp}")

  temp_max = unformated_data["main"]["temp_max"]
  print(f"The max temp is: {temp_max}")

  print()
  #ask user if they want to continue on
  again = input("Type stop to end progam or hit enter to continue: ")

print("Stopping Program")
