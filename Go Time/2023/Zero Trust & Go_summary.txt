• Definition of zero trust: eliminating the distinction between LANs and WANs
• Origins of zero trust at Google as BeyondCorp initiative
• Growing pressure for remote workforces before COVID-19 led to adoption
• Early days were slow with some organizations using VPNs instead
• White House had an initiative around zero trust
• Current state of zero trust: better tooling, more innovative approaches
• OpenZiti's approach: programmable network, mesh networking, strong cryptography
• Key difference from other solutions: SDKs for embedding into applications
• Ziti is an open-source network overlay solution that provides a full-stack mesh with logging, monitoring, and metrics capabilities
• The design allows for flexibility in choosing which layers to use, and can be used as a standalone mesh or as part of the larger Ziti stack
• Michael Quigley's work on OpenZiti has led him to create an open-source project called zrok, which demonstrates the potential of Ziti for building private sharing networks
• Ziti's overlay network and zero-trust architecture enable peer-to-peer communication without exposing peers publicly
• The conversation turns to how Ziti was built in Go, and how the language has become a favorite among its developers due to its performance and concurrency features
• Michael Quigley shares his experience with switching from JavaScript to Go for building Ziti, citing the ease of adoption and the idioms that make concurrent programming simpler
• The community adoption and marketing efforts for OpenZiti are discussed, including the challenges of explaining a unique concept like zero-trust overlay networks to developers familiar with traditional VPNs
• Michael Quigley emphasizes the importance of speaking to Go developers in their own language and showcasing how Ziti's SDKs can be used with simple, idiomatic Go code.
• Traditional zero trust architecture involves commercial products like Zscaler as network proxies
• The speaker's approach is different, establishing an overlay network and mesh connectivity
• Key components of traditional zero trust include identity validation and proxy mediation
• Misconceptions about zero trust involve treating it like a VPN or bolting it on through gateways
• Integrating zero trust into existing systems requires careful configuration and consideration of performance impacts
• The use of zero trust in certification processes is unclear, but may require vetting of components
• Zero trust architecture discussion
• Potential for AI to be integrated into smart routing implementation
• Multi-tenancy in the overlay network
• WAN optimization layer and Transwarp protocol
• TCP vs. user space protocol performance
• Nyquist theorem and subnyquist sampling
• Identity and access management in zero trust architectures
• Zero trust access control using Ziti
• Use of local LLMs for writing tasks and editing text (specifically Karen the Editor)
• Integration with DevOps pipelines through smoke testing and CI components
• Measuring zero trust success with usage metrics (traffic, services, endpoints)
• Operational metrics (delay/latency before and after overlay use)
• Tracing capabilities to see request lifespan and location span
• Ziti's tooling maturity for tracing and other features
• OpenZiti tooling and tracing connections
• Contribution guidelines for open source repos
• Hacktoberfest and external contributions
• Zrok SDK and ease of use for building peer-to-peer applications
• Go SDK and simplifying identity concepts and cryptography
• Custom protocols on top of UDP, including haptic data in telepresence streams
• Synchronization of arbitrary streams using UDP
• Benefits and trade-offs of using UDP for telepresence applications
• Potential for zero-trust architectures to be adapted for packet loss scenarios
• Repacketization in Ziti overlay networks
• Packet loss and retransmission in overlay networks
• Comparison of TCP and UDP protocols
• Unpopular opinions on:
  • The future of content ownership and streaming
  • The potential for a "Bandcamp-like" platform for movies
• Discussion of networks
• Sharing of tools and links in show notes
• Invitation to reach out to hosts and guests via GitHub