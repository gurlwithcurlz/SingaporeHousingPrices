# Selina 1 April 2019
# Holmusk assessment
# Program to merge .csv files that were provided from the link 
# https://data.gov.sg/dataset/resale-flat-prices) 


# Import relevant modules
import os
import pandas as pd

# Set directories and filenames
csv_dir = os.getcwd()
dataFolder=os.path.join(csv_dir) 
    # This is where I saved the individual .csv files
mergedFilename='All_Resale_FlatPrices.csv'
    # This is my output filename with merged data
output_file=os.path.join(dataFolder,mergedFilename)

# Now do a walk to get input filenames
filename_list=[]; # List of all the .csv files - which are long and complicated..!
for root, folder, filenames in os.walk(dataFolder):
    for thisFileName in filenames:
        if thisFileName.endswith('.csv') and thisFileName.startswith('resale'):
                # Make sure it's only the relevant input files, that start with 'resale'
                # and are .csv format
            filename_list.append(thisFileName)
            

# Now read in .csv data into dataframe, and concatenate
#df_temp={};
for ff in range(len(filename_list)):
    input_filename=os.path.join(dataFolder,filename_list[ff])
    if ff==0:
        rawinput_data=pd.read_csv(input_filename)
    else:
        new_inputdata=pd.read_csv(input_filename)
        rawinput_data=pd.concat([rawinput_data,new_inputdata],sort=True,ignore_index=True)
        #rawinput_data=tempval

        
# # Ok, now clean up some of the data..
# # The potential problematic columns would be :
# # town, flat_type, flat_model (strings)
cleaned_data=rawinput_data;
cleaned_data['flat_type']=cleaned_data['flat_type'].str.replace('MULTI-GENERATION','MULTI GENERATION')
cleaned_data['flat_model']=cleaned_data['flat_model'].str.upper() 
    # When checking, noticed upper and lower cases were mixed
cleaned_data['flat_model']=cleaned_data['flat_model'].str.replace('PREMIUM APARTMENT.','PREMIUM APARTMENT')

# Ok, now write data to file
output_file=os.path.join(dataFolder,mergedFilename)
cleaned_data.to_csv(output_file,index=False)
