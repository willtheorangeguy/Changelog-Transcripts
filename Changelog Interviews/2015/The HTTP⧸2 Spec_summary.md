• HTTP 2 is the topic of discussion
• Ilya Gregor, an "internet plumber" at Google, is the guest
• The conversation is a deep dive into the HTTP 2 specification
• Topics include binary framing layer, pipelining, multiplexing, header compression (hpack), server push, and TLS
• The conversation also covers the history of HTTP, from HTTP 0.9 to HTTP 1.0 and eventually to HTTP 2
• HTTP 2 is a major improvement over HTTP 1.0, addressing issues such as latency and scalability
• Emergent behavior in HTTP 1.0 and the initial attempt to document best practices
• HTTP 1.1 release in 1999 and its efforts to clean up the spec and introduce common language
• The web's evolution and the limitations of the original HTTP protocol
• The "speedy" project and efforts to change the protocol to address performance issues
• The limitations of HTTP's serial request-response protocol and the need for parallelism
• The use of workarounds such as concatenation and spriting to optimize performance
• The negative side effects of these workarounds, such as increased file sizes and maintenance difficulties.
• The current state of the web is that increasing bandwidth beyond a certain point does not significantly improve page loading speed.
• The experiment that led to the development of Speedy found that after a certain point, upgrading bandwidth no longer had a significant impact on page loading speed.
• However, the same experiment found that decreasing latency had a direct and linear correlation with improving page loading speed.
• ISPs do not typically advertise latency in their marketing, despite it being a significant factor in page loading speed.
• The last mile, or the first couple of hops in a network, can contribute a significant amount of latency, particularly in areas with under-provisioned capacity.
• To improve latency, protocols need to be re-examined to allow for pipelining requests, such as sending multiple requests at the same time.
• The premise for Speedy was to determine what changes to protocols are needed to allow for pipelining requests and improve latency.
• The speaker discusses the importance of prioritizing resources, specifically HTML files, when communicating with a server.
• The discussion highlights the limitations of HTTP/1.1 and the benefits of HTTP/2, which is based on the Speedy protocol.
• The speaker explains that Speedy was an experimental protocol developed in 2008 to improve web performance by allowing servers to send multiple requests and responses concurrently.
• The experiment showed significant performance improvements, and the Speedy protocol was later adopted as a starting point for the HTTP/2 specification.
• The speaker mentions that the HTTP/2 development process began around 2011 and was influenced by the Speedy protocol.
• The discussion touches on the idea of replacing HTTP with a more efficient protocol to improve web performance and reduce latency.
• The speaker notes that efforts have been made to address issues at multiple layers of the network stack, including the TCP layer, where head-of-line blocking is a problem.
• Discussion of HTTP/2 protocol and its development
• Comparison with HTTP/1 and its limitations
• Benefits of HTTP/2, including improved performance and reduced latency
• Key features of HTTP/2, including:
  • Single TCP connection for multiple requests
  • Multiplexing and pipelining
  • Header compression
  • Improved framing and performance
• Backward compatibility with HTTP/1
• Practical considerations for application developers and deployment
• Overview of HTTP/2's impact on web development and modern web protocols
• HTTP2 provides better performance through connection reuse
• Multiplexing: allows multiple requests and responses to be sent over a single connection
• Prioritization: enables clients to specify the priority of requests and responses
• Binary framing: introduces the concept of streams and allows for interleaving of multiple messages
• Flow control: allows clients to express how much data they can receive and when to resume a stream
• Server push: enables servers to proactively send responses to clients, reducing round-trip requests
• New capabilities and patterns of interaction between client and server are now possible with HTTP2
• Room for innovation in delivering web applications with HTTP/2
• HTTP/2 features, including header compression (HPACK)
• Problem with HTTP/1's header compression: metadata not compressed
• HPACK's two mechanisms for compression: Huffman coding and dynamic table
• Benefits of HPACK: significantly reduced metadata transfer
• Overview of HTTP/2 components, including multiplexing, prioritization, and header compression
• Upcoming discussion on implementation and browser support
• Security concerns, including TLS, and the upgrade cycle to HTTP/2
• HTTP 2 requires an upgrade and negotiation mechanism, but is not practically useful for HTTP 2 due to existing middleware interference.
• WebSockets and Speedy have similar issues with middleware interference, requiring HTTPS for reliable deployment.
• Browsers have implemented HTTP 2 with HTTPS as a requirement for public web deployment.
• HTTPS provides an end-to-end encrypted tunnel, making it difficult for intermediaries to interfere with traffic.
• ALPN negotiation is used to determine client and server support for specific protocols, including HTTP 2, during the TLS handshake.
• ALPN negotiation does not add extra latency, making it a transparent and efficient mechanism for determining protocol support.
• Navigation patterns and sensitive information
• Encryption of navigation data
• Performance impact of encryption
• Advantages of modern CPUs in executing crypto
• Cost savings with HTTP/2 due to reduced connections and handshakes
• Certificate complexity and requirements
• Binary framing layer and implementation concerns
• Observability and tooling for binary protocols
• Comparison of HTTP/2 and HTTP/1 implementation and performance
• Client support for HTTP2 has been finalized and is being rolled out
• Firefox and Chrome are already supporting HTTP2 in their stable browsers
• Internet Explorer (Edge) and Safari will also support HTTP2 in the near future
• The community is deprecating SPDY in favor of HTTP2
• There are growing lists of implementations for HTTP2 in various languages
• Several servers, including Twitter, Google, and Facebook, already support HTTP2
• Open-source implementations, such as h2o and h2o, are available
• Other servers, like Engine X and Varnish, are expected to support HTTP2 soon
• Code School's content is updated regularly to provide the latest learning resources
• 20% of Code School's courses are free, including instructor classes on Git, Ruby, and jQuery
• Pay-as-you-go option available for accessing all Code School courses
• HTTP/2 (h2) is the new standard for web performance, replacing HTTP/1
• h1 will not be fully replaced, but rather coexist with h2
• HTTP/2 enables features like server push and binary framing
• Optimizing for HTTP/2 can improve performance, but requires revisiting existing best practices
• Domain charting is an anti-pattern on HTTP/2, and concatenation can be undone for better performance
• Server push and caching offer opportunities for total automation
• HTTP/2 adoption is expected to rise quickly, with both server and client support improving
• Future innovations will explore capabilities like cache invalidations and binary framing
• Book on high-performance browser networking: updates and availability
• Differences between print and online versions of the book
• High Performance Browser Networking (HPBN) website and updated content
• HP2 protocol and its implications for browser networking
• Time to Glass challenge and its relation to browser performance and user experience
• Browser and developer responsibilities for enabling optimal HTTP/2 behavior
• Relationship between HTTP/2 and HTTP/1 performance limitations
• Time to Glass (TTG) and its implications for web development and performance
• Mobile and emerging market considerations for web performance
• Importance of efficient page loading and network optimization