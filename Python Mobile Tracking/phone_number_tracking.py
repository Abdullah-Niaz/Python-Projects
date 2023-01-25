import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Take a number input from the user & it should be in string
number = input("Enter the Phone Number With Country Code  ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, "en")
geo = geocoder.country_name_for_number(phone, "en")

print("\n\n\n", phone, "\n TimeZone ",
      time,  " \n Name of company ", car, geo, "\n\n")
