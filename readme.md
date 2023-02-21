# CARELESSWHISPER

## Overview
CARELESSWHISPER is a Python script that allows users to listen, read, and send UDP messages. The program identifies UDP ports open (for sending or receiving) to identify message traffic. The program listens for incoming data and sends outgoing data via the specified port.

## Installation
CARELESSWHISPER uses the following imported packages:

`socket`  
`datetime`  
`psutil`  

To use the program, please ensure these packages are installed.

Once the packages are installed, you can clone the repository by using the following command:

```bash
git clone https://github.com/Bl00dvault/CARELESSWHISPER.git
```

## Usage
To use CARELESSWHISPER, navigate to the cloned directory and run the following command:

```python
python CARELESSWHISPER.py
```

The program will start listening and sending messages through the specified ports. The program uses the current system time to trigger the main function, which then listens for incoming UDP messages.

Please note that the program has not been thoroughly tested, and modifications may be required for optimal performance.

## Functionality
The program includes the following functions and classes:

- trigger_start(): Queries the system datetime to use as a trigger.  
- udp_port_search(mission): Identifies UDP ports open (for send or receive) to identify message traffic.  
- message_fwd_listen(send_port, msghost): Listens for incoming data.  
- message_fwd_send(send_port, msghost): Sends outgoing data via the specified port.  
- draft_message(input, type): Reads through list of created inputs for messages.  
- read_field_bits(byte, bytesz): Function to read int() input data and output as bits with the appropriate field length.  
- Message: Class defining the structure of data messages.  

Please see the code for more detailed explanations of each function.

## Contributing
Contributions to CARELESSWHISPER are welcome! Please open an issue to report any bugs or suggest enhancements.
