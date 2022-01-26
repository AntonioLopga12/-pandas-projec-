
#porcentaje de valores 'Nan', por columna.
def dirt(sha):

    dic = dict(sha.isna().sum())

    for col,nan in dic.items():
        percent = (nan*100)/dic.shape[0]

    print(f'La columna {col} tiene {round(percent*100,2)}% de valores Nan!') 
                 