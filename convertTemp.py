# this program converts the temperature
# Just plug in the temperature at your
# location and this will pop out a 
# conversion!


# these two 'def' blocks are FUNCTIONS

def conv_2_f(temperature=None):
 return round((temperature * (9.0/5.0)) + 32.0, 2)

def conv_2_c(temperature):
 return round((temperature - 32.0) * (5.0/9.0), 2)
   

print("This program converts the temperature!")
print("Just enter the temperature at your location and I'll convert it for you.\n")

# get the temperature
the_temp = input("So what's the temperature there today? ")

if float(the_temp) < 39.0:
   print("\nEither it's REALLY cold there or you're talking Centigrade..... I'll convert that to Farenheight")
   unit = 'F'
else:
   print("\nThats either REALLY hot or your talking Farenheit.... I'll convert that to Centigrade")
   unit = 'C'

if unit == 'C':
  conversion=conv_2_c(float(the_temp))
else:
  conversion=conv_2_f(float(the_temp))


print("OK, I've converted " + the_temp + " to " + str(conversion) + unit)
