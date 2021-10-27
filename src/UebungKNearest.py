import pandas as pd
from sklearn.impute import KNNImputer
import seaborn as sn

mydata = pd.read_csv('Iris_missing.csv')
mydata2 = pd.read_csv('Iris.csv')
del mydata['Id']

features = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

""" remove Nan values """
def dropValue(df):

    df = df.dropna()

    return df

""" replaces NaN values with mean value"""
def missingValueMean(df):

    for iCol in features:
        var = df[iCol].mean()
        df[iCol].fillna(var, inplace=True)
    return df

""" compute distance between the features"""
def missingValueRms(df1,df2,features):

    myRms = 0
    for iCol in features:
        temp = df1.loc[:,iCol]-df2.loc[:,iCol]
        myRms = myRms +sum(temp**2)
    myRms = myRms/df1.shape[0]/len(features)
    myRms = myRms**0.5
    return myRms







if __name__ == "__main__":

    myList = list(mydata)
    myList.remove('Species')
    print("------------------------------------------------")
    print(mydata)
    print("------------------------------------------------")
    mydata = missingValueMean(mydata)
    print(mydata)
    print("___________________________________________________")

"""
    imputer = KNNImputer(n_neighbors=3)
    data_imputed_knn = mydata.copy()
    myArray = imputer.fit_transform(data_imputed_knn.loc[:,myList])
data_imputed_knn.loc[:,myList] = myArray
print(myArray[0][1])                       """



"""" for iCol in features:

        distance = missingValueRms(mydata2, mydata, myList)
        print(distance) """


"""
    print(mydata.isna())

    mydata = dropValue(mydata)

    print(mydata.shape[0])

    print(mydata.isna())   """

