import pandas as pd

def load_data():
    df=pd.read_csv('data/Eastren_region_indicators.csv', dtype={"GOVERNORATE_ID": str})
    df = df.sort_values('Year', ignore_index=True)
    return df

def get_avg_value(indicator, dff):
    dff = dff[dff['Indicator Name'] == indicator]
    dff.loc[:, 'Indicator Value'] = pd.to_numeric(
        dff['Indicator Value'], errors='coerce')
    average_value_1 = dff['Indicator Value'].mean()
    rounded_num = round(average_value_1, 0)
    return rounded_num

def get_difference(dff, target_year):
    # Filter the DataFrame for the target year and the previous year

    target_data = dff[dff['Year'] == target_year]
    previous_year = target_year - 1
    previous_data = dff[dff['Year'] == previous_year]
    # Merge the target and previous data based on 'Indicator Name'
    merged_data = pd.merge(target_data, previous_data, on='Indicator Name', suffixes=(
        '_target', '_previous'), how='inner')
    # Calculate the difference between the indicator values
    merged_data['Difference'] = merged_data['Indicator Value_target'] - \
        merged_data['Indicator Value_previous']
    # Calculate the percentage change from the previous year
    merged_data['Percentage Change'] = ((merged_data['Indicator Value_target'] -
                                        merged_data['Indicator Value_previous']) / merged_data['Indicator Value_previous']) * 100
    # Return all the percentage changes as a list
    percentage_changes = merged_data['Percentage Change'].tolist()
    return percentage_changes