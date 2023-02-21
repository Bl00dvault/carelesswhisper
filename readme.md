# Aggressor Messenger/CARELESS WHISPER

## TODO:
- Create diagram of data movement
- Create function interconnection map (done, see Static Code Analysis Section)
- Create file to function map
- Better define modules/functions
- Split program into multiple parts based on use case
- Need to account for netsh/iptables forwarding in layer2
- Account for while loop in listening for connections

#### Target
The intended target of this tool is any system utilizing UDP with defined data transfer packets (i.e., messaging). Note, this is not intended for layer 2/3 transport device, but the identified system running UDP applications.

#### End Result
The end result is a MitM capability to intercept data at the target destination and forward, drop, or modify data received.

#### Use Cases
- Intercept UDP traffic on target system:
  - Read the data transferred
  - Parse data based on defined schema, and place into defined "queue" based on data received
  - Forward traffic to a different destination
  - Drop traffic


## Description
Aggressor Messenger/CARELESSWHISPER is designed to intercept UDP data, parse data based on specific schema if necessary, and forward the traffic to the intended host. To handle UDP messages which can be sent in multiple frames, the queue system will store multiple messages in memory and forward them after conditions are met.

Program will:
- Find available interfaces on device
  - Enumerate for IP
- Using interface:
  - Find listening UDP ports
- Capture traffic on said ports
  - @warning: Need to work on threading to listen on multiple ports
- Analyze traffic received
- Place ID'd traffic into queue
- Do [XXX] with queue

## Modules
- Menu
- UDP Message Transport
  - Send UDP
  - Receive UDP
  - Store UDP
- Binary Message Creation
  - Bits vs. Bytes
- Data Queue
  - Create repository in memory (or on disk?) of data received
  - Send the received data after certain conditions are met

## References
### Threading
- Research Topics
  - Mutex
  - Semaphore

### Static Code Analysis
- Pylint ran against code will outline some good coding practices to use
    - Install: pip install pylint
- Pyroma will check dependencies created with a SetupTools and setup.py or setup.cfg
    - Install: pip install pyroma
- Radon will rate functions and classes
    - Usage: "radon cc [filename].py" 
    - Install: pip install radon
- Pyan3 will visualize function calls (call graph)
    - Usage: pyan3 app.py menu.py --uses --no-defines --colored --grouped --annotated --svg > app.svg
    - Install: pip install pyan3==1.1.1
    - Dependency: add 'dot' with the value of 'C:\Program Files\Graphviz\bin\dot.exe' to system environment variables
    - Dependency: Make sure to install graphviz using the windows installer, not pip if you want it to work
        - Link: https://graphviz.org/download/

### Links
- Static Code Analysis
  - https://luminousmen.com/post/python-static-analysis-tools
  - https://towardsdatascience.com/static-code-analysis-for-python-bdce10b8d287
- Python Troubleshooting Searches
  - https://www.tutorialspoint.com/python/python_multithreading.htm
  - https://sira.dev/2019/06/24/layer-2-socket-programming.html
  - https://stackoverflow.com/questions/7436801/identifying-listening-ports-using-python
  - https://stackoverflow.com/questions/10086572/ip-address-validation-in-python-using-regex
  - https://stackoverflow.com/questions/45097727/python-sockets-port-forwarding/45101773
  - https://donghaoren.org/blog/2012/udp-forwarder
  - https://stackoverflow.com/questions/1874331/python-port-forwarding-multiplexing-server