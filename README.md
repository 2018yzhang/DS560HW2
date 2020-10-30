# RandomNumsAndExecuteFunction
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4049824.svg)](https://doi.org/10.5281/zenodo.4049824)

## Introduction
RandomNumsAndExecuteFunction project is created for DSCI 560 Homework 2 and 4. It generates numbers randomly, executes function using these numbers, and visualizes it. There are three scripts:
* **GenerateNums.py**：It generates 1000 integers over the range 0-100 randomly and saves it to a CSV file.
* **ExecuteFunction.py**: It uses the result of GenerateNums.py and generates new numbers using y=3x+6.
* **Graph.py**: It generates a graph to show the relationship between the result of GenerateNums.py and the result of ExecuteFunction.py.

As for the notebook **Run3Scripts.ipynb**, it executes GenerateNums.py, ExecuteFunction.py, and Graph.py in order and shows the visualizations of them. 

## Installation  
1. To install and execute this project, you need clone this repository to your computer. 
    ```
    git clone https://github.com/2018yzhang/RandomNumsAndExecuteFunction.git 
    ```
2. If you don't have the package, virtualenv, you need to install your virtual environment using ```pip install``` firstly. 
    ```
    pip install virtualenv
    ```
3. Before you create a blank virtual environment for the project, please move into the project folder using ```cd``` command.
4. When you are in the project folder, you can create your virtual environment and name it.
   For macOS and Linux:
   ```
   python3 -m venv [YourEnvName]
   ```
   For Windows:
   ```
   py -m venv [YourEnvName]
   ```
5. To activate your virtual environment, you need to use following command:
   For macOS and Linux:
   ```
   source [YourEnvName]/bin/activate 
   ```
   For Windows:
   ```
   .\[YourEnvName]\Scripts\activate
   ```
   If you run it successfully, it should look like this:
   
   ![Image of activate](/samplePhoto/activate.png) 
   
6. Install all dependencies in the requirement.txt using:
   ```
   pip install -r requirements.txt
   ```
## Execution Scripts Under Virtual Environment
Now, you are able to execute scripts under the virtual environment you created using ```python [ScriptName].py```.
1. Execute GenerateNums.py to generate 1000 random integers. 
   ```
   python GenerateNums.py
   ```
   After execution, your terminal should like:
   
   ![Image of gen](/samplePhoto/afterGenScript.png) 
   
   There will be a CSV file generated in the project folder called, RandomNums.CSV.
   
2. Execute ExecuteFunction.py to invoke the function y=3X+6 using numbers from RandomNums.CSV as the input.
   ```
   python ExecuteFunction.py
   ```
   After execution, your terminal should like:
   
   ![Image of fun](/samplePhoto/afterExeScript.png) 
   
   There will be a CSV file generated in the project folder called, GeneratedNumsByFunction.CSV.
   
3. Execute Graph.py to draw a relation graph between the numbers from RandomNums.CSV (X) and GeneratedNumsByFunction.CSV (Y).There
   ```
   python Graph.py
   ```
   After execution, your terminal should like:
   
   ![Image of graph](/samplePhoto/afterGraphScript.png) 
   
   There will be a png image file generated in the project folder called, RelationGraph.png. 
   
## Notebook Execution in Binder
You can click below image and execute Run3Scripts.ipynb through Binder.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/2018yzhang/RandomNumsAndExecuteFunction/master?filepath=Run3Scripts.ipynb)

## Package Comparison
Install ```Matplotlib``` manually using below command:

```pip install matplotlib```

The dependency list showed below by using ```pip freeze```. You can also check it in the ```requirement.txt``` file.

![Image of graph](/samplePhoto/ExtractedList.png) 
