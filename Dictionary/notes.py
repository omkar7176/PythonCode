'''
***_Internet_***
- The internet is a global network of interconnected computers and servers that allows people to communicate, share information, and access resources from anywhere in the world. 
- The Internet standards describe a framework known as the Internet protocol suite. 
- This model divides methods into a layered system of protocols.

*__layers__* It is under the Internet topic

a. Application layer:
- Provide services to directly to end users or applcation processes.
- Example - HTTP, HTTPS, FTP, SMTP, POP3, DNS IMAP.
- functions of applcation layer is Data prsentation encryption and application level protocols.

b. Transport Layer:
- Provides end-to-end communication, error dection , correction  and flow control etc.
- Example - TCP, UDP
- functions of transport layer is segmenting data, error checking and flow control.

c. Network Layer:
- Responsible for routing the data between different networks.
- Example. IP, DHCP, ICMP
- Logical Addressing, routing and path determination.

The Internet provides a variety of information and communication facilities; contains databases, email, hypertext, etc.

***_World Wide Web_**
- The World Wide Web, or simply the web, is a system of interconnected documents and resources, linked together by hyperlinks and URLs.
- Invented by Sir Tim Berners-Lee in 1989 while at CERN.
- a way for scientists to share information more easily. 
- Developed core technologies: HTML, HTTP, and the first web browser/editor.

Core Technologies:
- HTML(full form): The language for creating web pages.
- HTTP (full form): The protocol for transferring web pages.
- Web Browsers: Software for accessing and navigating the Web (e.g., Chrome, Firefox, Safari).

Components:
- Web Servers: Computers that host websites and deliver content.
- Hypertext: Documents containing text, images, videos, and links.
- URLs (full form): Addresses of the web resources.

- The Web is the only way to access information through the Internet.


***__URL (Uniform Resource Locator)__***
- A URL is a human-readable text that was designed to replace the numbers (IP addresses) that computers use to communicate with servers.
- A URL consists of a protocol, domain name, and path (which includes the specific subfolder structure where a page is located) like-

       protocol://WebSiteName.topLevelDomain/path
- Protocol – HTTP or HTTPS.
- WebSiteName – geeksforgeeks, google etc.
- topLevelDomain- .com, .edu, .in etc.
- path- specific folders and/or subfolders that are on a given website.


***__IP address__***
- An IP address (Internet Protocol address) is a unique numerical assigned to every device connected to the internet. 

It has two primary functions: 
- identifying the host or device on a network and 
- detecting the host on the network.

- It is almost like a set of rules governing the structure of data sent over the Internet or through a local network. 
- An IP address helps the Internet to distinguish between different routers, computers, and websites.
- IP addresses are used for data routing, but they're also essential for network security. 
- Firewalls can use IP addresses to determine whether to permit or restrict incoming traffic based on the traffics source. 


***__Transmission Protocols/ Network protocols__***
- Transmission Protocols are a set of rules that governs the communication and exchange of data over the network or internet. 
- Both the sender and receiver should follow the same protocols in order to communicate the data.
- Any language has its own set of vocabulary and grammar which we need to know if we want to communicate in that language. 
- Similarly, over the network or internet whenever we access a website or exchange some data with another device then these processes are   governed by a set of rules called the transmission or network protocols.

** Working of Network Protocol **
- The internet and many other data networks work by organizing data into small pieces called packets. 
- Each large data sent between two network devices is divided into smaller packets by the underlying hardware and software.




***__Need of Protocols__**

***__Types of network protocols__***
1. TCP - The TCP is also known as a connection-oriented protocol.
2. UDP - 

***_Protocols_***


### 1. HTTP (HyperText Transfer Protocol)

- **Type**: Application Layer Protocol
- **Function**: Used for transmitting hypertext documents on the World Wide Web.
- **Working**: When a user enters a URL in a web browser, the browser sends an HTTP request to the web server. The server processes the request and responds with the requested web page, which the browser then renders.
Use to access the data.

### 2. HTTPS (HyperText Transfer Protocol Secure)

- **Type**: Application Layer Protocol
- **Function**: A secure version of HTTP, used for secure communication over a computer network.
- **Working**: HTTPS is a protocol that secures communication & data transfer between the user's and web browser & website.

### 3. FTP (File Transfer Protocol)

- **Type**: Application Layer Protocol
- **Function**: Used for transferring files between a client and a server like upload and download.
- **Working**: FTP operates on a client-server model. using FTP protocol Users can upload, download, rename, delete, and manage files on the server.

### 4. SMTP (Simple Mail Transfer Protocol)

- **Type**: Application Layer Protocol 
- **Function**: Used for sending emails from a client to a server.
- **Working**: SMTP handles the email sending process by transferring the email from the sender's mail server to the client mail server, using a process that ensures the email is routed correctly through the network.

### 5. POP3 (Post Office Protocol version 3)

- **Type**: Application Layer Protocol
- **Function**: Used by client email to receive emails from a server.
- **Working**: POP3 downloads emails from the server to the client’s device and optionally deletes the email from the server after downloading, which means emails are stored locally on the device.

### 6. IMAP (Internet Message Access Protocol)

- **Type**: Application Layer Protocol
- **Function**: Receive clients emails from a server, keeping them stored on the server.
- **Working**: means that all youur emails is saved on your Internet service provider(ISP) server.

### 7. DNS (Domain Name System) - In Book OPT - By KK

- **Type**: Application Layer Protocol
- **Function**: Translates human-readable domain names (like www.example.com) into IP addresses.
- **Working**: When a user types a domain name into a browser, the DNS server solves the domain name to its corresponding IP address and render on the correct web page on the browser.

### 8. DHCP (Dynamic Host Configuration Protocol)

- **Type**: Network Layer Protocol
- **Function**: Automatically assigns IP addresses and other network configuration to devices.
- **Working**: When a device connects to a network, the DHCP server assigns it an available IP address from a predefined range, also with other necessary network settings like subnet mask and gateway.

### 9. TCP (Transmission Control Protocol) - IN BOOK - By KK

- **Type**: Transport Layer Protocol
- **Function**: Ensures reliable, ordered, and error-checked delivery of data between applications.
- **Working**: TCP establishes a connection between the sender and receiver before transmitting data. It breaks data into packets, sends them to the receiver, and ensures all packets are received and reassembled in the correct order.

### 10. UDP (User Datagram Protocol) - IN BOOK By KK

- **Type**: Transport Layer Protocol
- **Function**: Provides a simpler, connectionless communication model with no guarantee of delivery, order, or error checking.
- **Working**: UDP sends packets called datagrams from the sender to the receiver without establishing a connection. This makes it faster but less reliable than TCP, often used for real-time applications like video streaming or online gaming.

### 11. IP (Internet Protocol) - IN BOOK

- **Type**: Network Layer Protocol
- **Function**: Defines the addressing and routing of packets of data so they can travel across networks and reach the correct destination.
- **Working**: IP uses IP addresses to identify devices on the network. It routes packets of data from the sender to the receiver based on their IP addresses, fragmenting and reassembling packets as needed.

### 12. ICMP (Internet Control Message Protocol)

- **Type**: Network Layer Protocol
- **Function**: Used for diagnostic and error-reporting purposes in network communication.
- **Working**: ICMP sends messages to indicate network issues like unreachable destinations or timeouts. It is used by network tools like ping and traceroute to diagnose connectivity problems.

These protocols collectively enable various functionalities required for internet and network communication, ensuring data can be sent, received, and managed effectively across different devices and networks.


***__Data transmission across the internet__***
1)Data Packaging and Routing
2)Transmission Protocols
3)Data Transmission Methods
4)Wireless Transmission
5)Ensuring Data Security




***__DNS__***
1. DNS is required for the functioning of the internet.
2. a full domain name is a sequence of symbols specified by dots.
3. DNS is a service that translates the domain name into IP addresses.
4. This allows the users networks to utilize user-friendly names when looking for other hosts instead of remembering the IP addresses.
5. The domain name system is divided into three different sections: generic domains, country domains, and inverse domain.

6. Generic Domains
-  It defines the registered hosts according to their generic behavior.
-  It uses three-character labels, and these labels describe the organization type.
7. Country Domain
The format of country domain is same as a generic domain, but it uses two-character country labels. 
(e.g., in for India, us for the United States) in place of three character organizational abbreviations.
8. Inverse Domain
The inverse domain is used for mapping an address to a name. 
When the server has received a request from the client, and the server contains the files of only authorized clients. 


***__Working of DNS__***
Of course! Here's a simple explanation of how DNS works:

1. **User Types URL**:
   - You type a web address (like www.example.com) into your web browser.

2. **Browser Checks Cache**:
   - Your browser looks in its memory to see if it already knows the IP address for that web address.

3. **OS Checks Cache**:
   - If the browser doesn't know, it asks your computer's operating system, which also keeps a list of recently used addresses.

4. **DNS Resolver**:
   - If the operating system doesn't know, it asks a DNS resolver (usually provided by your Internet Service Provider).

5. **Root DNS Servers**:
   - The DNS resolver first asks a root DNS server where to find the server for the top-level domain (like .com).

6. **TLD DNS Servers**:
   - The root server directs the resolver to a top-level domain (TLD) server, which handles addresses ending in .com.

7. **Authoritative DNS Server**:
   - The TLD server tells the resolver which authoritative DNS server knows the exact IP address for www.example.com.

8. **Resolver Caches and Responds**:
   - The resolver gets the IP address from the authoritative server.

9. **Browser Connects to Web Server**:
   - The resolver sends the IP address back to your browser, which uses it to connect to the web server hosting
   the website.

10. **Web Server Sends the Page**:
    - The web server responds by sending the webpage to your browser.

11. **Browser Displays the Page**:
    - Your browser displays the webpage so you can view and interact with it.

In summary, the DNS translates the easy-to-remember web address you type into your browser into a numerical IP address that computers use to locate and communicate with each other on the internet. This process involves several steps of checking and asking different servers, but it all happens very quickly, usually in just a few seconds.






***__Client-Server Model__***


### Client-Server Model

1. The client-server model is a network architecture where multiple clients request and receive services from a centralized server.   
2. This model is foundational in many types of networks, including the internet, and is used in various applications such as web services, email, and file sharing.
3. A server provides a service for many clients not just for a single client.
4. Therefore, we can say that client-server follows the many-to-one relationship. 
5. Many clients can use the service of one server.
6. For example, the client-server application program allows the user to access the files, send e-mail.


#### How It Works:
1. **Client Requests**: A client sends a request to the server for services.
2. **Server Responds**: The server processes the request and sends the response back to the client.
3. **Service Delivery**: The client receives the response and can then use the requested services.

### Advantages of the Client-Server Model:

1. **Centralized Resources**:
   - Centralized management of data and resources makes it easier to maintain, update, and secure.

2. **Scalability**:
   - Servers can be upgraded to handle increased load, and additional servers can be added to balance the load among them.

3. **Security**:
   - Centralized control allows for consistent security policies and easier monitoring.

4. **Ease of Maintenance**:
   - Software and updates can be managed centrally, making it simpler to deploy updates and maintain the system.


### Disadvantages of the Client-Server Model:

1. **Single Point of Failure**:
   - If the central server fails, all clients are affected and cannot access the services or resources.

2. **Performance Bottlenecks**:
   - High demand on the server can lead to performance issues if the server is not adequately equipped to handle the load.

3. **Cost**:
   - Setting up and maintaining a robust server infrastructure can be expensive.

4. **Complexity**:
   - The server requires professional management, including configuration, security, and updates, which can add complexity.
















'''