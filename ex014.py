print('Conversor de temperaturas!')
print('')
t = float(input('Digite a temperatura em °C:'))
f = (t*9/5)+32
k = float(t+273.15)
print(f'A temperatura de {t}°C corresponde a:\n{f:.2f}°F!\n{k:.2f}°K!')
