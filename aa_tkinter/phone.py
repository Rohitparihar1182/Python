import phonenumbers
from phonenumbers import timezone,geocoder,carrier
phone=phonenumbers.parse("+917839558297")

timezone=timezone.time_zones_for_number(phone)

Carrier=carrier.name_for_number(phone,'en')

region=geocoder.description_for_number(phone,'en')


print(timezone,Carrier,region)