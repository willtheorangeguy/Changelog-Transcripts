• The podcast discusses what's new in the Go cryptography libraries
• Introduction to the panel: Filippo Valsorda, Roland Shoemaker, and Nicola Murino
• Discussion of learning Latin at school and its relation to the podcast topic (quantum)
• Explanation of "nunc" meaning between pre-quantum and post-quantum
• Introduction of post-quantum cryptography and its purpose
• Discussion of NIST's draft selection for new cryptographic algorithms, including Kyber and SPS
• Pros and cons of implementing these new algorithms, including increased byte usage and potential slowness
• Key exchange mechanisms for post-quantum cryptography
• Comparison between X25519 and Kyber (ML-KEM) in terms of performance and key size
• Impact of SHA3 on performance, particularly with SSH connections
• FIPS-140 compliance and the "LED" requirement
• Challenges of implementing post-quantum signature algorithms due to increased key sizes
• Effects on certificate signing and transparency
• Discussion about email notifications for certificate statements and potential security implications
• Explanation of cipher suite ordering and its complexity
• Introduction to TLS 1.3 and its configuration changes, including reduced configurability and automatic ordering
• Backward compatibility issues with previous TLS versions (TLS 1.0-1.2) and the importance of ordering in securing connections
• Use of special logic for determining algorithm priority based on hardware support and user-specific needs
• Cryptography involves math that considers the specifics of implementation, not just the result.
• AES is difficult to implement in software due to side-channel attacks, but can be mitigated using bit slicing or reimplementing hardware-like logic.
• Reverse-engineering and game modding can be a useful skillset for security engineers.
• QUIC (Quick UDP Internet Connections) is an open-source protocol that replaces TCP with encryption by default.
• QUIC aims to simplify the internet's layered architecture, which has become complicated over time.
• QUIC implementation in Go and its goals
• Interoperability issues between QUIC and TLS implementations
• New TLS API in Go 1.21 that avoids breaking changes with QUIC Go
• Cryptobyte library for efficient parsing of certificates
• Performance improvements from using Cryptobyte (80% faster)
• Future plans and roadmap for QUIC implementation in Go
• Discussion of upcoming SSH changes
• New implementation to avoid passive network connections
• Limitations of existing packets and messages in SSH protocol
• Introduction of the "ping" message for emulation of keystrokes
• Importance of backward compatibility in software development
• Maintenance of Crypto SSH library and its synchronization with OpenSSH
• SHA2 support and migration away from SHA1 hash function
• Breakage of SSH connections due to lack of SHA2 support
• Introduction of a new interface for advertising supported algorithms
• Complexity of OpenSSH protocol and its evolution over time
• Issues with certificate handling and the need for configurability
• Merge of a change to make math/rand in Go 1.22 cryptographically safe by default
• Discussion on upcoming changes to SSH, including algorithm configurability
• The importance of configurability in certain situations
• Browsers are updated regularly making it easier to remove old algorithms
• Old algorithms like ARC4 should be avoided due to security concerns
• Tests for SSH functionality need improvement to prevent breakage with new versions of OpenSSH
• There is a problem with tests on Windows 11 that needs investigation
• Unpopular opinions were shared on topics such as loud keyboard typing and AI-generated code
• The administrative burden on doctors and dentists in the US
• Discussion of a multicooker as an alternative to a full kitchen for cooking
• Comparison of kitchen setup in Italy vs Germany
• Personal anecdotes about being a bad cook and using a multicooker from Natalie Pistunovich