
#porcentaje
def dirt(x):
    x = x[0]
    porcentaje = (x*100)/6302
    return f'The percentage of Nan values in this column is of, {round(porcentaje,2)}%.'