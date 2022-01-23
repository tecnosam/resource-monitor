# resource-monitor
A software that lets users monitor a PC's computing resources in real time
The system comes with both a REST-API and a web socket channel

## How to run
1. Make sure you have python 3.8+ installed
2. Create a virtual environment
3. run <code>pip install -r requirements.txt</code> to install the required modules
4. run <code>python -m app</code> in the terminal/command-prompt
5. To test, run the python script in tests/rest_client.py
6. Feel free to change the host and port


## routes
### 1. GET /
   This route to is to get all information about PC
### 2. GET /battery
   This returns the PC's battery percent
### 3. GET /memory
   This returns the PC's memory information
### 4. GET /network
   This returns the PC's information about it's connected network devices
### 5. GET /processor
   This returns a list of processes and their information
