import pandas as pd
import numpy as np

def get_data(file):
    data = pd.read_csv(file)
    return data

def null_analysis(df:pd.DataFrame):
    '''get % of null values in the dataset'''
    total_values = np.product(df.shape)
    total_null = (df.isnull().sum()).sum()
    proportion_null = (total_null / total_values)*100    
    print("The Telcommunication dataset has ",proportion_null,"% null values.")
    
def describe_data(df:pd.DataFrame,n:int):
    '''n is a number in the range 0-100, used to filter the dataframe, returning the columns
    with more than n% of null values'''
    dataset = df.isnull().sum()
    dataset = pd.DataFrame(dataset,columns=['null'])
    dataset['%null'] = (dataset['null']/df.shape[0])*100
    dataset['type'] = df.dtypes
    dataframe = dataset[dataset['%null']>=n]    
    return dataframe    
    
def clean_data(data:pd.DataFrame):
    data.columns = data.columns.str.replace(' ','_')
    data.columns = data.columns.str.replace('/','_')
    
    #Convert dates to datetime
    data['Start_ms']=pd.to_datetime(data['Start_ms'])
    data['End_ms']=pd.to_datetime(data['End_ms'])
       
    ''' Column Bearer Id should be a unique identifier and since we have a large dataset we drop the null rows'''
    data = data[data['Bearer_Id'].notna()]
    
    for i in data.columns.to_list():
        if data[i].dtype == 'object':
            data[i] = data[i].fillna(data[i].mode()[0])
        else:
            data[i]=data[i].fillna(data[i].median())
            
    return data