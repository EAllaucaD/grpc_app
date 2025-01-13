# **APP WITH GRPC AND PYTHON**

## 📋 Table of Contents

1. [📖 About the Project](#-about-the-project)
2. [🛠️ Tools Used](#%EF%B8%8F-tools-used)
3. [📋 Prerequisites](#-prerequisites)
4. [🚀 Project Usage](#-project-usage)
5. [📜 Preview]()

---

## 📖 About the Project

This project is an implementation of a basic gRPC client-server application using Python. It demonstrates how to set up a client and server communicating over gRPC. The server offers a simple "Hello" service that returns a greeting message based on the name provided by the client.


## 🛠️ Tools Used

Python

gRPC (Python package for implementing gRPC servers and clients)

Protocol Buffers (For defining services)

os (Used to manage paths for module imports)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

**Python**

Install the necessary Python packages. To do that, run the following command to install the required packages:
```
pip install -r requirements.txt
```

---

## 🚀 Project Usage

### 1. Clone the Repository
```bash
git clone
```
### 2. Commands

Navigate to the folder where you have your .proto file (proto folder), and then run the following command to generate Python files:
```
    python -m grpc_tools.protoc -I=proto --python_out=server --grpc_python_out=server proto/service.proto

```
This will generate the required Python files (service_pb2.py and service_pb2_grpc.py) inside the server directory.




### 3. Execute

After generating the required files, you can set up the server.
Navigate to the server directory and run: 

```
python server.py
```
The server will be running on localhost:50051 by default and is waiting for connections from clients.


Open the client.py file and ensure that sys.path is correctly set up to import the server-generated files and run: 
```
python client.py
```

You can create a new team and delete a team by entering the ID.

## 🎨 Preview
