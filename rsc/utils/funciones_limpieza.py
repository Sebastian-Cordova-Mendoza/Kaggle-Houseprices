import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter(action='ignore', category=FutureWarning)


#Función que realiza el labelencoder más simple. Se le pasa la columna a codificar y devuelve la columna modificada
def labelencoder_simple(column):
    
    le = preprocessing.LabelEncoder()
    le.fit(column)
    result = le.transform(column)

    return result

#Funicón que realiza OneHotEncoder. Columna a codificar como argumento y 
def OneHotEncoder_simple(column_df):

    one_hot_encoder = OneHotEncoder(sparse=False)
    result = pd.DataFrame(one_hot_encoder.fit_transform(column_df[["LotShape"]].values.reshape(-1,1)))
    renombre = []
    for column in result.columns:
        string = column_df.columns[0] + "_" + str(column)
        renombre.append(string)
    result.set_axis(renombre, axis=1,inplace=True)
    
    return result
