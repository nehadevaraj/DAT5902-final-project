# DAT5902 - Professional Software and Career Practices final project by Neha Devaraj (ID number)


## Madrid's weather data anlysis:

This project focuses on analysing daily weather data for Madrid between the years of 1997 to 2015. the data includes various meteorological parameters such as temprature, humidity, dea level pressure, wind speeds, precipitation, etc. I found the dataset on the Kaggle.com website, under "Weather Madrid 1997 - 2015", location: Barajas Airport, Madrid. Data: The Weather Company, LLC.

## Installation:
I set up the necessary environments before running the code by ensuring that all the required dependencies were installed. While some libraries such as unittest, pandas, and os come bundled with Visual Studio Code, I had to personally install additional packages using the Python package manager, pip. For example, "pip install Scipy", "pip install matplotlib" and "pip install seaborn". These commands took care of installing the scipy, matplotlib, and seaborn libraries, which are vital for performing statistical analyses and creating visualizations in the my_functions.py module. Then, I cloned the repository into Github. I checked if the unit tests were successful or not after I connected my repository to CircleCi.

## Project structure:

#### my_functions.py:
Contains utility functions for data manipulation, statistical analyses, and plotting graphs.
The module includes functionalities such as reading CSV files (read_csv_file), converting a specified column to datetime format (convert_column_to_datetime), setting the 'CET' column as the index (set_cet_as_index), calculating the Pearson correlation coefficient between two columns (calculate_correlation), determining the Kendall rank correlation (calculate_kendall_correlation), and computing the Spearman correlation (calculate_spearman_correlation). Additionally, the module provides visualisation functions for plotting max and min temperatures over time (plot_temperature_over_time) and temperature anomalies over time (plot_temperature_anomaly_over_time). These functions leverage the Pandas library for data handling, Scipy for statistical computations, and Matplotlib and Seaborn for creating insightful visualizations. I made 8 test suites, but more visualisation functions can be made, especially with the dataset I used (Madrid Daily Weather 1997-2015.csv).

#### test_suite.py:
Includes a suite of unit tests for functions defined in "my_functions.py".
This module, test_suite.py, serves as a comprehensive test suite for the functions defined in the associated my_functions.py file. The suite employs the unittest framework to validate the correctness and reliability of each function, ensuring their intended behaviors and functionality are consistent. The tests cover a range of scenarios, including reading a CSV file (test_read_csv_file), converting a column to datetime format (test_convert_column_to_datetime), setting a column as an index (test_set_cet_as_index), calculating Pearson correlation coefficients (test_calculate_correlation), determining Kendall rank correlations (test_calculate_kendall_correlation), and computing Spearman correlations (test_calculate_spearman_correlation). Additionally, graphical functions for plotting max and min temperatures over time (TestPlotTemperatureOverTime) and temperature anomalies over time (TestPlottingFunctions) are tested. The test suite provides a robust validation mechanism to ensure the functionality and reliability of the implemented utilities within the my_functions.py module.


#### Madrid Daily Weather 1997-2015.csv:
My chosen dataset that is used for analysis. The suite employs the unittest framework to validate the correctness and reliability of each function, ensuring their intended behaviors and functionality are consistent. The tests cover a range of scenarios, as mentioned above in the "my_functions.py" section. The scenarios include reading a CSV file (test_read_csv_file), converting a column to datetime format (test_convert_column_to_datetime), setting a column as an index (test_set_cet_as_index), calculating Pearson correlation coefficients (test_calculate_correlation), determining Kendall rank correlations (test_calculate_kendall_correlation), and computing Spearman correlations (test_calculate_spearman_correlation). Additionally, graphical functions for plotting max and min temperatures over time (TestPlotTemperatureOverTime) and temperature anomalies over time (TestPlottingFunctions) are tested. The test suite provides a robust validation mechanism to ensure the functionality and reliability of the implemented utilities within the my_functions.py module. To execute the test suite, run python test_suite.py in your terminal, and any failures or errors will be reported, aiding in the identification and resolution of potential issues during development or maintenance.


## Installation:
I made sure to set up the necessary environment before running the code by ensuring that all the required dependencies were installed. While some libraries such as unittest, pandas, and os come bundled with Visual Studio Code, I had to personally install additional packages using the Python package manager, pip. For example, "pip install Scipy", "pip install matplotlib" and "pip install seaborn". These commands took care of installing the scipy, matplotlib, and seaborn libraries, which are vital for performing statistical analyses and creating visualizations in the my_functions.py module. If you encounter any missing dependencies during execution, it's crucial to go through this installation process to ensure your Python environment is properly configured. Make sure that the installed libraries match the versions compatible with your project for smooth and error-free functionality. Then, I cloned the repository into Github. I checked if the unit tests were successful or not after I connected my repository to CircleCi.


## Usage:
1. Reading the CSV file
2. Data processing
3. Statistical analyses
4. Plots
5. Unit testing
6. Continuous integration



