#%% remove duplicates in columns
import pandas as pd 

students = [
            ('Ankit', 34, 'Uttar pradesh', 34),
            ('Riti', 30, 'Delhi', 30),
            ('Aadi', 16, 'Delhi', 16),
            ('Riti', 30, 'Delhi', 30),
            ('Riti', 30, 'Delhi', 30),
            ('Riti', 30, 'Mumbai', 30),
            ('Ankita', 40, 'Bihar', 40),
            ('Sachin', 30, 'Delhi', 30)
         ]
# Create a DataFrame object with duplicated columns
my_data = pd.DataFrame(students, columns =['Name', 'Age', 'Domicile', 'Marks'])

my_data[['Marks2']] = my_data['Marks']

my_data = my_data.rename(columns = {'Marks2' : 'Marks'})

# Print a original dataframe
my_data


# %% function that finds duplicated columns
def getDuplicateColumns(df):
    '''
    Get a list of duplicate columns.
    It will iterate over all the columns in dataframe and find the columns whose contents are duplicate.
    :param df: Dataframe object
    :return: List of columns whose contents are duplicates.
    '''
    duplicateColumnNames = set()
    # Iterate over all the columns in dataframe
    for x in range(df.shape[1]):
        # Select column at xth index.
        col = df.iloc[:, x]
        # Iterate over all the columns in DataFrame from (x+1)th index till end
        for y in range(x + 1, df.shape[1]):
            # Select column at yth index.
            otherCol = df.iloc[:, y]
            # Check if two columns at x 7 y index are equal
            if col.equals(otherCol):
                duplicateColumnNames.add(df.columns.values[y])
    return list(duplicateColumnNames)

#%% apply function to dataframe (my_data)
# Get list of duplicate columns

duplicateColumnNames = getDuplicateColumns(my_data)

print('Duplicate Columns are as follows')
for col in duplicateColumnNames:
    print('Column name : ', col)

newDf = my_data.drop(columns=getDuplicateColumns(my_data))

# code source:https://thispointer.com/how-to-find-drop-duplicate-columns-in-a-dataframe-python-pandas/
