# windows-text-generation-inference-example
Text Generation Inference example in Windows (docker, WSL is needed)

## Instructions

First, clone the git repository and navigate to the root folder. Then, follow these steps:

1. Download Docker.
2. Launch Docker Desktop.
3. Open a command prompt with administrator privileges and run the dockerStart.bat file.
   - This batch file sets up the environment by installing the required models and dependencies.
4. Allow firewall access (for server execution).
5. Wait until you see the message "Starting Webserver" indicating that the server is running.
6. Execute "python main.py".
7. Once you have reviewed the results, press Ctrl+C to exit.

To me, this is 10 times faster than usual code.
