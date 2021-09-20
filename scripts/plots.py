import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_univariate(df,col1,col2):
    plt.figure(figsize=(12,8))
    
    plt.subplot(2,2,1)
    sns.histplot(data=df,x=col1,bins=30,kde=True)
    plt.title(f'Histogram of {col1}', size=14)
    
    plt.subplot(2,2,2)
    sns.boxplot(df[col1])
    plt.title(f'Boxplot of {col1}', size=14)
    
    plt.subplot(2,2,3)
    sns.histplot(data=df,x=col2,bins=30,kde=True)
    plt.title(f'Histogram of {col2}', size=14)
    
    plt.subplot(2,2,4)
    sns.boxplot(df[col2])
    plt.title(f'Boxplot of {col2}', size=14)
    
    plt.show()
 
def plot_bivariate(df,col1,col2,col3,col4):
    
    plt.subplot(2,2,1)
    ax1 = sns.scatterplot(df[col1],df['Total_MB'])
    ax1.title.set_text(f'Scatter plot of {col1} against Total_MB')
    
    plt.subplot(2,2,2)
    ax2 = sns.scatterplot(df[col2],df['Total_MB'])
    ax2.title.set_text(f'Scatter plot of {col2} against Total_MB')
    
    plt.subplot(2,2,3)
    ax3 = sns.scatterplot(df[col3],df['Total_MB'])
    ax3.title.set_text(f'Scatter plot of {col3} against Total_MB')
    
    plt.subplot(2,2,4)
    ax4=sns.scatterplot(df[col4],df['Total_MB'])
    ax4.title.set_text(f'Scatter plot of {col4} against Total_MB')
    plt.show()

def plot_3d(df:pd.DataFrame,col1:str,col2:str,col3:str,n:int):
    sns.set(style = "darkgrid")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    x = df[col1].sample(n)
    y = df[col2].sample(n)
    z = df[col3].sample(n)

    ax.set_xlabel(f'{col1}')
    ax.set_ylabel(f'{col2}')
    ax.set_zlabel(f'{col3}')

    ax.scatter(x, y, z)

    plt.show()
