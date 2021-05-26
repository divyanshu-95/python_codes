import phonenumbers
from phonenumbers import geocoder#which country
from phonenumbers import carrier#sim
num=input('phone no with code\n')
isp=phonenumbers.parse(num)
iu=phonenumbers.parse(num)
print('the country is',geocoder.description_for_number(iu,'en'),'and the service provider is'
      ,(carrier.name_for_number(isp,'en')))
