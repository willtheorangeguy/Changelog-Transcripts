• The state of HTTP/2 in Node.js and its implementation
• HTTP/2's impact on Node.js and its potential addition to NodeCore
• The importance of keeping NodeCore small and focused on web fundamentals
• The distinction between web fundamentals and supporting utilities in Node.js
• The potential addition of HTTP/2 to NodeCore and its implications for the Node community
• The definition of what should be included in NodeCore and what should be left to modules
• The differences between HTTP/1 and HTTP/2 and their implications for Node.js
• Node.js and HTTP/2 protocol support 
• HTTP/2's new way of thinking about web applications and APIs 
• Performance and concurrency in HTTP/2 
• Security and compliance with the HTTP/2 specification 
• Mitigating security issues through strict spec compliance 
• TLS support in HTTP/2 
• Performance improvements through TLS termination 
• Opportunities for new kinds of APIs and protocols in HTTP/2 
• New extensibility models and possibilities for innovation in HTTP/2 
• Issues with the HTTP/2 protocol, including Header Compression and state table maintenance
• HTTP/2 introduces stateful connections, which add complexity and require server affinity over long-lived connections
• This introduces serialization of requests and responses, and shared state tables across multiplexed requests
• James Snell disagrees with the decision to use stateful connections, believing a more efficient binary coding of data would have been sufficient
• HTTP/2 also introduces additional complexity with its own flow control, prioritization, and dependency of streams
• Node.js must provide an API for these new features, but it's unclear how much complexity to expose to developers
• The worst-case scenario for HTTP/2 is the server affinity issue, which can lead to proxy software vendors having significant problems
• Despite the complexity, HTTP/2 offers performance benefits, including using sockets more efficiently and saving bandwidth
• However, this comes at the cost of increased memory usage and tradeoffs in terms of API and security
• HTTP/2 protocol implementation in Node.js
• Breaking changes in Node's API with HTTP/2
• Deliberate choice to use HTTP/2 due to its benefits
• Challenges in adopting HTTP/2, including its immaturity
• Offer both HTTP/1 and HTTP/2 in Node.js
• Native module approach for HTTP/2 implementation
• Community decision on whether to integrate HTTP/2 into Core or offer it as a separate module
• Feedback and input are needed to determine the future of the code
• James Snell wants people to submit issues and pull requests to the repo, rather than contacting him personally
• The code is currently in a state of flux and could use help with testing and performance benchmarks
• There are specific areas where help is needed, including tests and performance benchmarks
• The repo will be linked in the show notes for those who want to contribute