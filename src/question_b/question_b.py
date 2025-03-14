def get_fahrenheit(celsius):
    return (9/5) * celsius + 32

print("{:<10} {:<10}".format("Celsius", "Fahrenheit"))
for c in range(0, 21):
    f = get_fahrenheit(c)
    print("{:<10} {:<10.1f}".format(c, f))