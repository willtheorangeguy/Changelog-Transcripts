• Paul Vixie discusses the limitations of the internet protocols, including DNS, which were not designed for the scale of the modern internet.
• He notes that the internet was originally built as a laboratory toy by government contractors, and its protocols were not designed to handle the current level of traffic and complexity.
• Vixie argues that DNS is in need of revision, citing its limitations in handling large responses and the resulting fragmentation issues.
• He contrasts the simplicity of the original UDP protocol with the complexities of TCP, which requires kernel state and can be inefficient for certain types of traffic.
• Vixie discusses the issue of fragmentation, which is poorly supported and does not work as intended, and notes that Path MTU Discovery is a flawed solution.
• He expresses frustration with the limitations of the current internet protocols and the inability to make significant changes to them.
• Concerns about the potential for a Y2K-style debacle due to quantum computing and the need for post-quantum crypto
• Discussion of the limitations of TCP and the potential for a new internet protocol
• Introduction of QUIC (HTTP/3) as an alternative to TCP, using UDP instead
• Proposal to make QUIC live inside TCP, and the potential drawbacks of this approach
• Reflection on the cycle of innovation and the tendency for each new generation to reinvent solutions without fully understanding the history and context behind them
• DNS is an eventually consistent request-response protocol that relies on caching to scale
• The binary format of DNS messages is not extensible and causes issues when trying to add new features or internationalized domain names
• Internationalized domain names (IDNs) were not supported until the introduction of nameprep, which converted data into base-64
• Paul Vixie would start with an extensible encoding, such as a binary version of JSON, to make it easier to add new features and representations
• The cost of developing and implementing new features is typically borne by companies that see it in their best interests, either through funding open source development or through government contracts
• Designing and implementing a new version of DNS (DNS 2) and letting people opt-in to it, similar to HTTP/2, is a possible approach to updating the protocol.
• DNS protocol limitations and potential replacement
• Benefits of a new DNS protocol, including improved performance and security
• Challenges of creating a new protocol, including fragmentation and standardization
• Incentives for adopting a new protocol, including improved internet performance and security
• Comparison of DNS to blockchain and cryptocurrency development
• Hardware considerations for implementing a new DNS protocol, including NICs and hardware support
• Long-term prospects for a new DNS protocol, including the potential for it to become ubiquitous like HTTP/2 and 3
• Challenges of achieving critical mass and standardization for a new protocol
• Discussion of Ethernet packet size limitations and the idea of increasing packet size as network speeds increase
• Reason for not increasing packet size: backward compatibility and the need to connect new networks to existing ones
• Limitations of "jumbograms" (larger packet sizes) in current use
• Implications for future DNS development and the need for application-level fragmentation or handshake overhead
• Discussion of the difficulty of upgrading Ethernet infrastructure and the need for incremental upgrades
• Ideas for resolving the issue, including new ICMP message types and Ethernet-level packets
• Mention of alternative uses of DNS, such as for security purposes (e.g. using DNS for communication between "honey pot" systems)
• The history of DNS and its initial scope
• Using DNS for email reputation and spam prevention
• Examples of DNS being used for license key lookups and antivirus signatures
• DNS tunneling for secure data transmission
• The flexibility and resilience of DNS as a protocol
• The common phrase "it's always DNS" and its implications for developers
• The evolution of online services and the shift from enterprise services to cloud-based solutions
• The concept of "permissionless innovation" and the impact of TCP/IP on the internet
• The story of OpenDNS and its early success in providing a global anycast DNS service
• OpenDNS's decision to intercept DNS queries and forward them to Google, associating user interests with IP addresses
• The controversy surrounding OpenDNS's actions and Google's response
• The impact of DNS intermediaries on the internet, including the creation of EDNS and ECS
• The current state of DNS and the challenges it poses to users and developers
• Paul Vixie's DNS setup: using a personal DNS server on his laptop, and running his own DNS server at home
• Using a DNS resolver like Cloudflare (1.1.1.1) or Google, and how to configure a Pi-hole to use these resolvers
• Personal DNS Firewalls and ThreatSTOP
• Configuring Pi-hole to resolve directly to the root nameservers without an intermediary resolver
• The benefits and drawbacks of running a personal DNS server, and the history of DNS on the internet
• ISP DNS servers and their past practices, and the shift towards more secure and private DNS options
• Pi-hole and its impact on DNS resolving at the network level, and its potential to control DNS traffic across a network
• Discussion of Personal DNS Firewall and Pi-hole as alternatives to using ISP-provided DNS services
• Challenges of implementing Pi-hole, including setup and configuration requirements
• Alternative approach using open-source name servers such as Unbound
• Benefits of using a local DNS server, including ad-blocking and family-friendly DNS lookups
• Criticism of relying on third-party DNS services, including potential data collection and ad optimization
• Author's preference for using open-source solutions and controlling one's own network
• Reflection on the author's career and what keeps him involved in the industry
• The need for a sense of purpose and belonging in work
• The comfort of having a team and customers to protect
• The inevitability of aging out of a career
• The importance of honest coworkers and feedback
• The fun and engaging conversation about DNS and Paul Vixie's career