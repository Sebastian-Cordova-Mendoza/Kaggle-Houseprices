from sklearn import preprocessing


#Funció que realiza el labelencoder más simple. Se le pasa la columna a codificar y devuelve la columna modificada
def labelencoder_simple(column):
    
    le = preprocessing.LabelEncoder()
    le.fit(column)
    result = le.transform(column)

    return result
