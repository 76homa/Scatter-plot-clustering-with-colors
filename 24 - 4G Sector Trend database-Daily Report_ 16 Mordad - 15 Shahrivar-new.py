import pandas as pd
import dask.dataframe as dd
import numpy as np
from dask.distributed import Client
from sklearn.preprocessing import LabelBinarizer

def mycal():
    # Create a Dask client (optional but recommended)
    client = Client()
    
    # Read data using pandas
    excel_file_path = 'C:/Users/homa.behmardi/Downloads/24 - 4G Sector Trend database-Daily Report_ 16 Mordad - 15 Shahrivar-new.xlsx'
    sheet_name = 'Report'  # Replace with the correct sheet name
    
    pandas_data = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    print('Read excel Completed....')
    # Convert the pandas DataFrame to a Dask DataFrame
    data = dd.from_pandas(pandas_data, npartitions=10)  # You can adjust the number of partitions as needed
    print('Data Partitioned...')
    # Specify the categorical column
    categorical_columns = ['Sector']
    
    # Apply LabelBinarizer in parallel
    label_binarizer = LabelBinarizer()
    label_encoded = data[categorical_columns].map_partitions(label_binarizer.fit_transform, meta=data[categorical_columns])
    
    print('l5')
    #print('Lable Encode Shape : ', np.shape(label_encoded))
    # Compute the result (this triggers the computation)
    label_encoded = label_encoded.compute()
    print('Lable Computing finished...')
    
    # Get the feature names (unique classes)
    feature_names = label_binarizer.classes_
    
    # Create a DataFrame with the encoded data
    label_encoded_df = pd.DataFrame(label_encoded, columns=feature_names)
    
    # Concatenate the encoded data with the original data
    data_encoded = pd.concat([pandas_data, label_encoded_df], axis=1)
    
    # Optionally, drop the original categorical column
    data_encoded.drop(categorical_columns, axis=1, inplace=True)
    
    # Optionally, save the encoded data to a CSV file
    data_encoded.to_csv('encoded_data.csv', index=False)


if __name__ == '__main__':
    mycal()