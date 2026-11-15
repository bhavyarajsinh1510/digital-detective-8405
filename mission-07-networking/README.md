# Mission 7 — How Computers Communicate

## 1. Task / Objective

The objective of this mission is to understand how computers communicate with each other through networks.

This mission covers different types of networks, DNS, routers, protocols, packet switching, network connectivity, DNS lookup and the process of opening a website.

## 2. Work Completed

### Task 7.1 — Explain Network Concepts

A computer network is a group of connected devices that communicate and exchange information with one another.

| Concept | Explanation | Example |
|---|---|---|
| LAN (Local Area Network) | A network that connects devices within a small geographical area. | Home Wi-Fi or a college computer lab. |
| MAN (Metropolitan Area Network) | A network that connects devices or smaller networks across a city or large campus. | A city-wide network connecting different offices. |
| WAN (Wide Area Network) | A network that covers large geographical areas and connects multiple smaller networks. | The Internet. |
| DNS (Domain Name System) | Translates human-readable domain names into IP addresses. | Translating example.com into an IP address. |
| Router | A networking device that forwards data between different networks. | A home router connecting devices to the Internet. |
| Protocol | A set of rules that devices follow to communicate. | HTTP, HTTPS and TCP. |
| Packet Switching | A method of transferring data by dividing it into smaller units called packets. | Sending information across the Internet. |
| Client-Server | A communication model in which a client requests a service and a server provides it. | A browser requesting a webpage from a web server. |

### Task 7.2 — Observe Network Information

Network connectivity and DNS information can be checked using Terminal.

**A. Connectivity Test**

Command:

```bash
ping -c 4 example.com
```

The `ping` command checks whether a destination can be reached over a network by sending test messages and measuring the responses.

The `-c 4` option sends four test packets and then stops.

This test helps identify whether a destination responds to network requests. It can also display response times and packet loss.

**B. DNS Lookup**

Command:

```bash
nslookup example.com
```

The `nslookup` command queries the Domain Name System to find information about a domain name.

It can display the DNS server that answered the query and the IP address associated with the requested domain.

**C. Role of DNS**

DNS acts like an address directory for the Internet. People remember domain names more easily than numerical IP addresses.

When a user enters a website name into a browser, DNS helps translate that domain name into an IP address so the browser can locate the appropriate server.

### Task 7.3 — What Happens When You Open a Website?

When a user opens a website, several networking operations take place.

1. **User Request:** The user enters a website address, such as `example.com`, into a web browser. The browser acts as a client.

2. **DNS Lookup:** The browser needs the server's IP address. DNS translates the domain name into its corresponding IP address.

3. **Network Communication:** The computer sends network requests through its network connection. The router helps forward data towards the destination network.

4. **Server Connection:** The browser establishes communication with the appropriate web server using networking protocols. For an HTTPS website, a secure connection is established.

5. **HTTP/HTTPS Request:** The browser sends an HTTP request asking the server for the required webpage or resource.

6. **Server Response:** The server processes the request and sends a response containing webpage data and other required resources.

7. **Displaying the Website:** The browser receives the response, processes HTML, CSS and JavaScript, and displays the webpage to the user.

This process allows users to access websites and exchange information across networks.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `ping` | Checks network connectivity with another host. |
| `ping -c 4 example.com` | Sends four connectivity test packets on macOS. |
| `nslookup` | Performs DNS queries to obtain domain information. |
| `nslookup example.com` | Looks up DNS information for example.com. |
| Terminal | Provides a command-line interface for network observations. |
| Web Browser | Used to access websites and observe client-server communication. |

## 4. My Understanding

Through this mission, I understood how computers communicate and exchange information through networks.

I learned that LAN, MAN and WAN represent networks covering different geographical areas.

I understood that DNS translates domain names into IP addresses and that routers forward data between networks.

I also learned about packet switching, where data is divided into smaller packets for transmission across a network.

Protocols such as HTTP, HTTPS and TCP establish rules that allow devices to communicate correctly.

The most interesting concept was understanding what happens when a website opens. It involves several stages, including DNS lookup, network communication, server requests and browser rendering.

This mission helped me understand that accessing a website involves communication between multiple systems working together.

## 5. Difficulties Faced

Understanding the differences between LAN, MAN and WAN and learning how DNS translates domain names into IP addresses were the main conceptual challenges.

It was also important to understand the difference between a router, a protocol and packet switching because they perform different roles in networking.

## 6. How I Resolved Them

I reviewed the purpose of each networking concept and compared them using practical examples.

I studied the `ping` command to understand connectivity testing and `nslookup` to understand how domain names are resolved.

Breaking website communication into individual steps made the overall process easier to understand.

## 7. Evidence / Files

The following file and activities are associated with this mission:

- `mission-07-networking/README.md` — Networking concepts, explanations and observations.
- Connectivity testing using `ping`.
- DNS lookup using `nslookup`.
- Explanation of the website communication process.

Any screenshots or copied Terminal output should be privacy-safe. Personal IP addresses, Wi-Fi names, usernames and other identifying network details must not be published.

## 8. Commit Details

**Commit message:**


"Explain networking concepts and website communication"


**Git commands:**

```bash
git add mission-07-networking/
git commit -m "Explain networking concepts and website communication"
git push origin main
```

The mission should be committed and pushed to GitHub, and the commit and files should be verified on the repository.

## 9. Conclusion

Mission 7 helped me understand the fundamentals of computer networking and how devices communicate over the Internet.

I learned about different network types, DNS, routers, protocols, packet switching and the client-server model.

I also explored basic network commands and understood the sequence of operations that takes place when a website is opened.

These concepts form an important foundation for understanding the Internet, web development and computer communication.