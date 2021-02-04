import pandas

def get_column_data():
    df = pandas.read_excel('file_example_XLS_1000.xls')
    #print the column names
    # print(df.columns)
    #get the values for a given column
    values_id = df['Id'].values
    values_name = df['First Name'].values
    values_gender = df['Gender'].values
    values_date = df['Date'].values

    #get a data frame with selected columns
    # FORMAT = ['Id']
    # df_selected = df[FORMAT]
    return values_id, values_name, values_gender,values_date