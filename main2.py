from matplotlib import pyplot as plt # importerer nødvendige bibliotek

x_coords_1 = []
y_coords_1 = []
x_coords_2 = []
y_coords_2 = []     # Lager en tom array med koordinatene til de ulike dataene
x_coords_3 = []
y_coords_3 = []
x_coords_4 = []
y_coords_4 = []


def get_values_from_files(file, cond):
    x = []
    y = []
    with open(file, 'r') as file:
        file_content = file.read()
        content_lines = file_content.split('\n')
        for j in content_lines:
            sep_values = j.split(',')
            x.append(float(sep_values[0]))
            if cond:
                y.append(float(sep_values[1]))
            else:
                y.append(float(sep_values[1]))
    return x, y


x_coords_3, y_coords_3 = get_values_from_files('temp.txt', True)
x_coords_4, y_coords_4 = get_values_from_files('co22.txt', False)


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x_coords_3, y_coords_3, 'g-', label="Temp")
ax1.legend(['Temp'], loc="upper left")
ax2.plot(x_coords_4, y_coords_4, 'r-', label="Co2")
ax2.legend(['C02'], loc="upper right")

ax1.set_xlabel('Årstall')
ax1.set_ylabel('Temperaturendinger')
ax2.set_ylabel('Endring i CO2-masse hvert år')

plt.show()
