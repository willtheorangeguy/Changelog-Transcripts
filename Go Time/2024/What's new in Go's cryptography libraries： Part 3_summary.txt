• Introduction to Go Time podcast and sponsors
• Review of PagerDuty issues with FireHydrant's signals feature
• Discussion of incident management and on-call processes for modern engineering teams
• Fencing trivia and fun conversation between hosts
• Preview of upcoming Go 123 episode topics, including crypto/TLS changes
• Protocol changes for secure DNS and reducing privacy leakage
• New API for hybrid public key encryption (HPKE)
• Post-quantum connections using new algorithms, specifically Chosen Problems
• Experimental implementation of post-quantum hybrids in crypto/tls
• Request for testing and feedback on release candidate with post-quantum features enabled
• Release candidate testing: importance of identifying bugs early in the release process
• Using Canary builds vs Release Candidate builds to test compatibility with internal production environments
• Post-quantum cryptography interoperability issues between Go implementation and other implementations
• Go module configuration for using Release Candidate builds and automatically fetching new versions
• SDK generation for APIs, including challenges and opportunities presented by code generators
• Speakeasy's approach to generating high-quality SDKs through a combination of code generation and human expertise
• Description of API and SDK
• Open SSH support for post-quantum algorithms
• Moving crypto/ssh from xcrypto to go.crypto
• Interoperability between SSH implementations
• Lattice-based vs NTRU encryption algorithms
• Deprecating packages in x/crypto
• Reorganizing golang.org/x/crypto module
• Merging important packages into the standard library
• The speaker discusses upcoming changes to the Go module, which will remove support for SHA-1 (SHAWN) signatures due to security concerns.
• A previous attempt to remove SHAWN support led to complaints from users who relied on private-public key infrastructure.
• To mitigate this issue, a debug flag was added that allows users to opt-in to retaining SHAWN signature verification.
• The goal is to remove the debug flag in Go 1.24 and no longer allow SHAWN signature verification.
• The speaker notes that SHA-1 signatures are still allowed for legacy purposes when verifying existing signatures.
• In the Crypto SSH library, a new environment variable allows users to disable SHAWN by default.
• Future work includes improving algorithm negotiation and exposing negotiated algorithms to users.
• The speaker also mentions recent improvements to support for new hashes in the SSH protocol.
• Issues with RSA algorithm implementation in SSH
• Mismatch between key type (ktype) and algorithm type leading to bugs
• History of protocol evolution leading to current issues
• Plan to integrate the Boring SSL test suite into Go's TLS testing
• Importance of using a comprehensive test suite, such as Bogo, for TLS testing
• Discussion about choosing alerts and the importance of semantic correctness
• Proposal for sharing test vectors across implementations in cryptography
• Mention of project "White Proof" (located in Australia, not America) and its goal of sharing test vectors
• Plans to improve crypto/rand package, including a single-pass cleanup and changing how it handles errors
• Discussion about making the crypto/rand package more efficient by avoiding allocations
• Proposal for a new API that generates random strings from a given character set
• The speaker thinks password generation rules are a bad idea
• A browser game was mentioned where the goal is to create syntactically valid passwords with increasingly arcane rules
• Password hacking and crypto-SSH were discussed as topics in upcoming conferences
• The Go programming language's vulnerability analysis tooling was highlighted as one of the most advanced available
• Automatic scanners can trigger false vulnerabilities and introduce untested features when fixed quickly
• Govon check was mentioned as a way to improve signal-to-noise ratio for vulnerability reports
• The importance of testing release candidates, especially for unusual or complex codebases
• Life insurance commercials lead to procrastination, but it's essential to consider term coverage life insurance
• Ladder offers digital, hassle-free life insurance application process with no doctors or paperwork required
• Open source software is often used for free, but maintaining and evolving it requires significant time and effort
• Supporting open source projects through sponsorship can ensure their long-term sustainability and quality
• Contributing patches to open source projects without proper review can be detrimental to the project's maintainability
• Preference for desktop PCs over laptops due to portability
• Unpopular opinion about pigeons, considering them "okay" rather than pests
• Discussion of a "box" or dedicated workspace for the computer
• Mention of a time-activated safe as a possible solution for secure workspaces
• Brief mention of pet rats and their benefits vs. problems with wild rodents
• Gophercon event promotion and discussion of aligning with Go release cycle