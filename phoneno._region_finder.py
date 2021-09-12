# we have to install a package phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone

phone_number=input("enter your phone number with country code\n")

#parasing string to phone no.
ph_number=phonenumbers.parse(phone_number)

#check weather this no. is possible or not
possible=phonenumbers.is_possible_number(ph_number)
if possible==True:
    print("this phone no. is possible")

    #check weather this no. is valid or not
    valid=phonenumbers.is_valid_number((ph_number))
    if valid==True:
        print("this phone no. is valid also")

        #find region and network sevice provider
        region=geocoder.description_for_number(ph_number,"en")
        service_provider=carrier.name_for_number(ph_number,"en")

        #program to get timezone
        Timezone=timezone.time_zones_for_number(ph_number)

        #now print all information
        print("region of this phone no is:",region)
        print("servive provider of this phone no. is:",service_provider)
        print("timezone for this phone no. is:",Timezone)
    else:
        print("this phone no. is possible but not valid",ph_number)
else:
    print("this phone no.is not possible",ph_number)




