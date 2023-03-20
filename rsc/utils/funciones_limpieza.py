import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter(action='ignore', category=FutureWarning)



def labelencoder_simple(column):
    """
    Función que realiza el labelencoder más simple.
    Se le pasa la columna a codificar y devuelve la columna modificada.
    """

    le = preprocessing.LabelEncoder()
    le.fit(column)
    result = le.transform(column)

    return result



def OneHotEncoder_simple(df, column_df):
    """
    Función que realiza OneHotEncoder. Argumentos: df y la columna a codificar. 
    Devuelve el df con la columna codificada y la columna origen borrada.
    Las nuevas columnas añadidas son renombradas con el nombre original de la variable y una etiqueta numérica (n variables codificadas)
    """
    
    one_hot_encoder = OneHotEncoder(sparse=False)
    result = pd.DataFrame(one_hot_encoder.fit_transform(column_df.values.reshape(-1,1)))
    renombre = []

    for column in result.columns:
        string = column_df.columns[0] + "_" + str(column)
        renombre.append(string)

    result.set_axis(renombre, axis=1,inplace=True)

    df = df.join(result)
    del(df[column_df.columns[0]]) 
    return df
