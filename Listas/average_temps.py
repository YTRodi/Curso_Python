# --------------------------------------------------- FUNCIONES
def avg_temps(temps):
    sums_of_temps = 0

    for temp in temps:
        sums_of_temps += temp
    
    return sums_of_temps / len(temps)
# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    temps = [21,24,24,22,20,23,24]

    average = avg_temps(temps)

    print('La temperatura promedio es: {} (Redondeado)'.format(round(average)))
    print('La temperatura promedio es: {}'.format(average))