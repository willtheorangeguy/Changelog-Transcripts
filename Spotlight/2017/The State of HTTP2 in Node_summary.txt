• State of HTTP/2 implementation in Node
• Impact of HTTP/2 on Node's performance profile and APIs
• Decision on whether to include HTTP/2 in NodeCore or as a module
• Definition of web fundamentals and criteria for inclusion in Core
• Importance of keeping NodeCore small and focused on basic web protocol support
• New features and complexities introduced by HTTP/2, such as stateful header compression and multiplexing
• Discussion around Node.js and HTTP/2 protocol
• Importance of security in Node.js with HTTP/2
• How HTTP/2 supports better security through compliance to specification
• Browsers requiring TLS for HTTP/2 connections
• Limitations of Node's current TLS performance
• Excitement about developers using HTTP/2 and its potential
• New features and applications enabled by HTTP/2, such as push streams
• Criticisms of the HTTP/2 protocol, including staple header compression limitations
• Binary coding vs stateless compression for headers
• Complexity of HTTP/2 protocol (flow control, prioritization)
• Server affinity issue with HTTP/2 and proxy software vendors
• Performance benefits of HTTP/2 (efficient socket use, reduced failures)
• Tradeoffs between HTTP/2 features (e.g. header compression, TLS) and API complexity
• Breaking changes to Node's API for HTTP/2 adoption
• The challenges of adopting HTTP/2 as it requires deliberate design and implementation.
• Potential use cases for HTTP/2 include server-to-server communication within protected environments.
• James Snell is working on the HTTP/2 implementation, but it's open-source and contributed by multiple developers.
• The Node organization is developing HTTP/2 under a GitHub repo (github.com/nodejs/http2).
• It may be possible to use both HTTP/1 and HTTP/2 simultaneously, with clients negotiating which protocol to use per socket.
• Deprecating HTTP/1 is considered premature due to its fundamental role in the Node ecosystem.
• Implementing HTTP/2 as a native module is being explored as an alternative to integrating it into Core.
• Request for help from the community
• James Snell mentions stabilizing and testing aspects of a project
• Areas where help is specifically needed (tests, performance benchmarks)
• Repository link provided for reference
• Conversation importance due to Node Interactive's closure