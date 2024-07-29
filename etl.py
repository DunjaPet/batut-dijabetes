#!/usr/bin/env python
# coding: utf-8

#########################################################
## Author: Dunja Petrovic
## This is 2nd script in data pipeline. It is loading the data files from 'Data' folder
## and doing few transormations. The output are 4 csv files written in the main project folder
#########################################################

import pandas as pd
import os
import re
import numpy as np
import logging

# configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler("etl.log"),  # Log to a file
        logging.StreamHandler()  # Also log to the console
    ]
)


current_directory = os.getcwd()
data_directory = os.path.join(current_directory, r'data')
data_directory


# File routines

logging.info('Started file routines')


regex = re.compile(r'\d+')

def extract_okrug(text):
    pattern = r'\b(\w+)\s+okrug\b|\b(grad\s+Beograd)\b'
    if pd.notna(text):
        match = re.search(pattern, text)
        if match:
            return  match.group(1) if match.group(1) else match.group(2)
    return None   

atc_prop_df = pd.DataFrame()
atc_real_df = pd.DataFrame()
mtp_real_df = pd.DataFrame()
mtp_prop_df = pd.DataFrame()

for (dirpath, dirnames, filenames) in os.walk(data_directory):
    for file in filenames:
        file_path = os.path.join(dirpath, file)

        if file.endswith('.csv'):
            logging.info(f"Reading File {file}")
            df = pd.read_csv(data_directory+'\\' + file ,sep = ";", encoding='windows-1250',on_bad_lines='skip')
            # add year column
            year = regex.findall(file)[0] 
            df['Godina'] = year  
            # extract okrug from filijala   
            df['Okrug'] = df['Filijala'].apply(lambda x: extract_okrug(x))    
            # drop Filijala
            df.drop(['Filijala'], axis=1,inplace=True)
            # fill empty okrug
            df['Okrug'] = df.Okrug.fillna('Nepoznat')
            # group files by filename
            base_filename = re.sub('\d+','', file)
            
            if base_filename == 'atc_propisani.csv':
                atc_prop_df = pd.concat([atc_prop_df, df], ignore_index=True)

            elif base_filename == 'atc_realizovani.csv':
                atc_real_df = pd.concat([atc_real_df, df], ignore_index=True)

            elif base_filename == 'mtp_realizovani.csv':
                mtp_real_df = pd.concat([mtp_real_df, df], ignore_index=True)

            elif base_filename == 'mtp_propisani.csv':
                mtp_prop_df = pd.concat([mtp_prop_df, df], ignore_index=True)   

            else:
                logging.info (f"Skipping unsupported file: {file}")

                            
        elif file.endswith('.xlsx'):
            logging.info(f"Reading File {file}")
            if file == 'filijale.xlsx':
                filijale = pd.read_excel(data_directory+'\\' + file)
            if file == 'sifremtp.xlsx':
                sifremtp = pd.read_excel(data_directory+'\\' + file)
                
        else:
            logging.info(f"Skipping unsupported file: {file}")

mtp_real_df['SifraPomagala'] =  np.nanmax(mtp_real_df[['SifraPomagala','SifraLeka']].values , axis=1)
mtp_real_df.drop(['SifraLeka'], axis=1,inplace=True)

# Save concatenated DataFrames

atc_prop_df.to_csv(os.path.join(current_directory, 'atc_prop.csv'),encoding='windows-1250', index=False)
atc_real_df.to_csv(os.path.join(current_directory, 'atc_real.csv'),encoding='windows-1250', index=False)
mtp_real_df.to_csv(os.path.join(current_directory, 'mtp_real.csv'),encoding='windows-1250', index=False)
mtp_prop_df.to_csv(os.path.join(current_directory, 'mtp_prop.csv'),encoding='windows-1250', index=False)

logging.info(f"Saved files in: {current_directory}")


logging.info('Finished file routines')


