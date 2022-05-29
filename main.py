from matplotlib import pyplot as plt # importerer nødvendige bibliotek

x_coords_1 = []
y_coords_1 = []
x_coords_2 = []
y_coords_2 = []     # Lager en tom array med koordinatene til de ulike dataene
x_coords_3 = []
y_coords_3 = []
x_coords_4 = []
y_coords_4 = []

with open('co2.txt', 'r') as file1:  #co2- dataen var mest urganisert for mitt bruk. Derfor bruker jeg
                                     # her programmering for å fikse datasettet.
    content = file1.read()
    lines = content.split('\n')

    for x, i in enumerate(lines):    # Gjør dataen lesbar og mer organisert, slik at jeg ikke må
                                     # gå gjennom alt og fikse dataen manuelt.
        i = i.split(",")
        i.pop(-1)
        i[0] = i[0].strip()



        #x_coords_1.append(float(i[0]))

                                     #Legger til dataen til det første datasettet og gjør om til
                                        #koordinater
        #y_coords_1.append(float(i[1]))


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


#x_coords_2, y_coords_2 = get_values_from_files('n2o.txt', False)
x_coords_3, y_coords_3 = get_values_from_files('temp.txt', True)
x_coords_4, y_coords_4 = get_values_from_files('co22.txt', False)



plt.plot(x_coords_1, y_coords_1)
plt.plot(x_coords_2, y_coords_2)
plt.plot(x_coords_3, y_coords_3)
plt.plot(x_coords_4, y_coords_4)
plt.legend(['co2', 'n2o', 'temp', 'vekst av co2 per år'])
plt.show()

print(x)