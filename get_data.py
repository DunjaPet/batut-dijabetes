#!/usr/bin/env python
# coding: utf-8

#########################################################
## Author: Dunja Petrovic
## This is the 1st script in data pipeline. It is downloading 14 files from the site https://data.gov.rs/sr/datasets/dijabetes/
## and saving them in newly created folder 'Data' inside the main project folder. It relies on the hardcoded names and urls 
#########################################################


from urllib.request import urlretrieve
import os

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'data')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)




# Downloading the files from https://data.gov.rs/sr/datasets/dijabetes/



url =                   [
                        'https://data.gov.rs/sr/datasets/r/1be52d31-1af0-4441-aa93-3593b7e8fd0e'
                       ,'https://data.gov.rs/sr/datasets/r/76c7f5ba-9378-4818-a394-b36165245f30'
                       ,'https://data.gov.rs/sr/datasets/r/ec19b957-e7d6-45a5-8321-0893258b2618'
                       ,'https://data.gov.rs/sr/datasets/r/c8a76d70-ec4e-4618-a858-31f89fce647a'
                       ,'https://data.gov.rs/sr/datasets/r/b618411b-adae-44e4-84db-6fb1ad955a44'
                       ,'https://data.gov.rs/sr/datasets/r/5182de0c-67da-49ce-9974-1dbbfdd9eb21'
                       ,'https://data.gov.rs/sr/datasets/r/548c3133-458e-4f92-ab7a-c690306c09da'
                       ,'https://data.gov.rs/sr/datasets/r/dc86f7e2-de21-4785-acb5-3161fffaf748'
                       ,'https://data.gov.rs/sr/datasets/r/79d98f28-2c0d-48a8-bbc8-41f106d9e2f7'
                       ,'https://data.gov.rs/sr/datasets/r/aead0882-a4da-46b9-ada7-fe753fef4312'
                       ,'https://data.gov.rs/sr/datasets/r/3a976dd0-1a3e-4a27-9614-18df3223c9d9'
                       ,'https://data.gov.rs/sr/datasets/r/36bf0f8c-27fc-4058-9eb0-d16056b8a413'
                       ,'https://data.gov.rs/sr/datasets/r/e548dcb6-0c71-49b3-8d7e-f6240d177203'
                       ,'https://data.gov.rs/sr/datasets/r/27498d6c-c86e-4bca-9eec-72e74a1bcd3d'
                       ]




filenames =                [
                            os.path.join(final_directory, 'filijale.xlsx')
                            ,os.path.join(final_directory, 'sifremtp.xlsx')
                            ,os.path.join(final_directory, 'mtp_realizovani2021.csv')
                            ,os.path.join(final_directory, 'mtp_realizovani2020.csv')
                            ,os.path.join(final_directory, 'mtp_realizovani2019.csv')
                            ,os.path.join(final_directory, 'mtp_propisani2021.csv')
                            ,os.path.join(final_directory, 'mtp_propisani2020.csv')
                            ,os.path.join(final_directory, 'mtp_propisani2019.csv')
                            ,os.path.join(final_directory, 'atc_realizovani2021.csv')
                            ,os.path.join(final_directory, 'atc_realizovani2020.csv')
                            ,os.path.join(final_directory, 'atc_realizovani2019.csv')
                            ,os.path.join(final_directory, 'atc_propisani2021.csv')
                            ,os.path.join(final_directory, 'atc_propisani2020.csv')
                            ,os.path.join(final_directory, 'atc_propisani2019.csv')
                            ]




for url, name in zip(url , filenames ):
    urlretrieve(url,name)

