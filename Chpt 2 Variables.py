type = input('Enter farenheit or celsius:') #select and input temperature
temp = float(input('Enter todays temperature:'))
if type == 'celsius' 'Celsius':
    print(temp, 'Degrees celsius converted to farenheit is', temp / 5 * 9 + 32)    
elif type == 'farenheit':
    print(temp, 'Degrees farenheit converted to celsius is', (temp-32) * 5 / 9)
else:
    print('Not valid Temperature') #Convert to other temperature format based on input
