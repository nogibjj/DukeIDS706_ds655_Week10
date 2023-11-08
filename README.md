# Python Repository to perform data processing using PySpark [![Test](https://github.com/nogibjj/DukeIDS706_ds655_Week10/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_Week10/actions/workflows/test.yml)

This repository uses the [HIGGS Dataset](https://archive.ics.uci.edu/ml/datasets/HIGGS) from the UCI Machine Learning Repository. This dataset has been produced using Monte Carlo simulations. 

The first 21 features (columns) are kinematic properties measured by the particle detectors in the accelerator. The last seven features are functions of the first 21 features; these are high-level features derived by physicists to help discriminate between the two classes. There is an output variable 'label' that identifies the two classes, with 's' indicating the signal process which produces Higgs bosons and 'b' indicating a background process. More Details about the dataset can be found [Here](https://archive.ics.uci.edu/ml/machine-learning-databases/00280/).


We are using the `Pyspark.py` file in the Codes folder to do the following - 
This Python script does the following:

1. Imports necessary libraries.
2. Defines the URL of the HIGGS dataset.
3. Creates a SparkSession, which is the entry point to any Spark functionality.
4. Downloads the HIGGS dataset from the UCI Machine Learning Repository and decompresses it.
5. Reads the downloaded file into a pandas DataFrame.
6. Converts the pandas DataFrame to a PySpark DataFrame.
7. Counts the number of rows in the DataFrame and prints it.
8. Stops the SparkSession.

The HIGGS dataset contains *11,000,000 instances*, each with *28* attributes. The file size is approximately *6.8 GB* when uncompressed.

It is much better to access this large dataset in Pyspark as compared to Pandas in Python. This is because PySpark is designed to work with big data and can distribute the task of reading the dataset across multiple nodes if running on a cluster. This allows it to read and process data in parallel, which can greatly speed up the operation.



Files in this repository include:


## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages.


## 3. Codes
  This folder contains all the code files used in this repository - the files named "Test_" will be used for testing and the remaining will define certain functions
  The `Pyspark.py` file contains the code to read and evaluate the large HIGGS dataset


## 4. Resources
  -  This folder contains any other files relevant to this project. Currently, I have added -


## 5. CI/CD Automation Files


  ### 5(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 5(b). Github Actions
  Github Actions uses the `main.yml` file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions


  ### 5(c). Devcontainer
  
  The `.devcontainer` folder mainly contains two files - 
  * `Dockerfile` defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
  * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
