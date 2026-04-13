• Introduction to Go Time podcast and its discussion on new developments in crypto library
• Review of topics not covered in part one, including CLS 1.0, math/big, Crypto ECDH, SHA-1 deprecation, and future plans for safer APIs
• Discussion on moving from pre-quantum to post-quantum cryptography, including the term "nunc" (a middle ground) and its relation to quantum technology
• Explanation of post-quantum cryptography and its purpose to prevent potential breakage by quantum computers
• Introduction to new NIST drafts, a competition among independent groups for cryptographic proposals
• NIST's selection of post-quantum algorithms for key exchange and digital signatures
• European governments and scientists agreeing with NIST's selections
• Comparison between X25519 and Kyber (newly named ML Chem) in terms of performance
• Diffie-Hellman algorithm being broken, leading to the use of alternative methods like Kyber and Dilithium
• Standardization on certain algorithms for post-quantum cryptography
• Performance impact of using SHA3 hash function in common operations like SSH connections
• FIPS 140 compliance requirements for cryptographic libraries
• Increased data size with new post-quantum algorithms
• Certificate signing and key exchange issues with larger keys
• Post-quantum signature algorithms resulting in significantly larger keys and signatures
• Implications for internet connection speed and security protocols
• Cypher suite ordering and its complexity, and the need to simplify configuration options
• Comparison of tls rsa with as 256 gcm shot 384 and tls ecdhe ecdsa with 3dcbc shot cypher suites
• Removing configuration options for cipher ordering
• Impact on backwards compatibility and potential issues with old devices
• Importance of handling ordering to ensure secure connections
• New approach allowing the system to decide ordering based on user device capabilities
• Discussion of AES implementation in software, difficulties, and side channel attacks
• Introduction to bit slicing technique as a solution for efficient AES implementation
• Discussion of Minecraft and redstone-based computer building as potential source for innovative cryptography ideas
• Relationship between reverse engineering games and security engineering skills
• Quick protocol, its origins, and its role in HTTP/3
• How Quick replaces TCP with UDP and encrypts headers by default
• Impact on middle boxes (hardware devices that interfere with network traffic)
• TLS handshake implementation issues with Quick
• Changes to crypto tls package to support Quick implementations
• Forking issue resolved with new API for Quick implementations
• Backwards and forwards compatibility concerns
• Discussion on hiding away implementation details in internal packages
• Roadmap discussion for Quick implementation
• Overview of open source LLMs surpassing ChatGPT performance
• Impact of commoditized data models on AI development
• Comparison of ASN.1 and JSON formatting in Go
• Speeding up certificate passing by 80% with optimized code
• SSH protocol changes, including a new "ping" extension to avoid keystroke detection
• Backwards compatibility issues and formal approval process for shipping features
• Maintenance of the xcrypto ssh library, with Niccola taking over maintenance after funding from clients
• Open SSH's removal of SHA-1 support and the delay in implementing SHA-2 extensions
• GitHub's blog post about transitioning to SHA-2 and pressure on other organizations to do the same
• Breakage caused by the transition, including issues with Fedora and Arch Linux
• Nicola's experience with the painful upgrade process and introduction of a new interface for multi-algorithm support
• The complexity of the SSH protocol, including key types, signature algorithms, and certificate standards
• The need for a more streamlined approach to handling multiple algorithms and protocols
• Proposals to freeze library versions and maintain compatibility
• ACL merge in Go, making math/rand cryptographically safe by default
• Discussion of upcoming changes in SSH, including configurability and improved defaults
• SFTP-go project and its benefits for open-source projects
• Importance of tests, particularly xcrypto tests against OpenSSH
• Discussion about a reverted commit and its impact on builds
• Unpopular opinion: using an old-style keyboard with loud keystrokes is beneficial for hacking
• Debate about the value of AI-generated code and its potential job security benefits
• Filipo's unpopular opinion: using Copilot in cryptography code, but only for writing error messages
• Discussion on company donations to open-source projects and their limitations
• Proposed solution: offering non-monetary incentives or services to support maintainers
• The speaker discusses making a simple tomato sauce with vegan meatballs using a multi-cooker.
• They mention their limited cooking skills, claiming to be a terrible cook despite being Italian.
• The conversation shifts to the speaker's approach to cooking, emphasizing simplicity and minimal ingredients.
• A discussion about German apartment rentals and the standard lack of kitchen equipment in new apartments is mentioned.
• A humorous anecdote about Italians vs. Germans having kitchens in unfurnished apartments is shared.
• The episode ends with a lighthearted comment on unpopular opinions and a plug for the podcast's sponsors and social media channels.