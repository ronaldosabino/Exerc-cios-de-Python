# Conversor de temperaturas
# Escreva um programa que converta uma temperatura em °C e a converta para °F

c = float(input('Digite uma temperatura em °C:\t'))
f = (c * 9/5) + 32

print('\n{:.1f}°C é equivalente a {:.1f}°F'.format(c, f))
