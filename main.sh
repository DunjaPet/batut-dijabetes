#!/bin/bash
#########################################
## Project batut-dijabetes
## Author: Dunja Petrovic
## Date July 2024
#########################################

# Usage : bash main.sh
src=$(pwd)

echo "downloading data from https://data.gov.rs/sr/datasets/dijabetes/"
python get_data.py

echo "transforming data"
python etl.py

echo "Pipeline completed"
