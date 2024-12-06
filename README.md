# Automated Financial Data Pipeline

## Overview
This project is an end-to-end automated data pipeline designed to fetch financial data from Yahoo Finance, process it using PySpark, and store it securely in Azure Data Lake Gen2. The pipeline is orchestrated using Jenkins to ensure daily data updates and seamless automation. This project is a demonstration of key data engineering concepts, designed for scalability, security, and maintainability.

## Features
 
* **Daily Data Ingestion:** Automatically fetch stock market data using the Yahoo Finance API.
* **Data Transformation:** Clean and process the data using PySpark to ensure high-quality outputs.
* **Cloud Storage:** Store both raw and processed data in Azure Data Lake Gen2 with a well-structured hierarchy.
* **Pipeline Automation:** Orchestrate the pipeline with Jenkins for hands-free operation.
* **Secure Design:** Employ RBAC policies and securely manage credentials using Azure Key Vault and Jenkins.

## Future Enhancements
* **Data Visualization**
* **Advanced Metrics**

## Technologies Used

* **Programming Language:** Python (with yfinance for API calls). 
* **Big Data Framework:** PySpark (for transformations and processing). 
* **Cloud Platform:** Microsoft Azure (Azure Data Lake Gen2 for storage).
* **Automation Tool:** Jenkins (for pipeline orchestration and monitoring).
* **Security:** Azure Key Vault and RBAC for secure credential and access management. 
