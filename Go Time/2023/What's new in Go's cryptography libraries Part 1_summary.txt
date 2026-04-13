• Introduction and background on the crypto library in Go
• History of the crypto library: added to standard libraries from the beginning, designed by Adam Langley
• Importance of having cryptography code in the standard library
• Focus on providing Go developers with what they need for secure development, rather than competing with other toolkits
• Efforts to keep the code secure and reducing complexity
• Discussion of what is new in the crypto library (but no specific details mentioned)
• Discussion of the RSA backend change and its replacement with a new implementation
• Criticism of the math/big library for cryptography due to performance and security issues
• Introduction of the bigmod library as a replacement, written specifically for cryptography
• Update on the speed and security improvements in Go 1.21's RSA decryptions and signatures
• Development of the new crypto/ecdh package for elliptic curve Diffie-Hellman key exchange
• Explanation of the design principles behind the new crypto libraries and their benefits over previous implementations
• Introduction to Whitfield Diffie, a pioneer in public key cryptography
• Discussion of why RSA is being replaced with elliptic curves
• Compatibility guarantee in Go language and its implications on making changes without breaking existing code
• Management of deprecated packages and APIs in the Go standard library
• Handling security vulnerabilities in deprecated packages
• Examples of when visible changes are necessary, such as updating default protocols or hashes
• Disabling TLS 1.0 and 1.1 by default to improve security
• Use of the "godebug" mechanism for preserving legacy behavior in Go standard library
• Discussion of SHA1 deprecation and its implications
• Limitations of configuring behavior through APIs and need for special flags or environment variables
• Importance of prioritizing cipher suite ordering to prevent exposure to security risks
• Cryptographic attacks, specifically the Bleichenbacher 98 and 07 attacks
• Vulnerabilities in RSA implementations, including hardcoded exponents
• Go debugging features and their impact on backwards compatibility
• Fallback root certificates added to Go in version 1.21 for improved TLS handling
• Plan to use metrics and telemetry data to manage legacy behaviors and remove unnecessary debug flags
• Implementing a new API for certificates in Go
• Creating separate modules for certificate bundles and updates
• Discussion on introducing AI bots to automate tasks
• Review of the math/rand package and its upgrade to v2
• Plans for creating higher-level APIs for cryptographic primitives
• Exploring changes to the crypto packages, including AADs (Authenticated Encryption with Associated Data)
• Cryptography libraries are too complex for users to use securely
• Post-quantum algorithms will be added to the Go standard library in the next 2-3 years
• SSH package is being updated and has started to rot
• Terminal text editor debate between Emacs, Vim, Pico, and Joe
• Filippo Valsorda disagrees with Roland Shoemaker's opinion that Pico is the best terminal text editor, preferring Joe instead
• Discussion about the use of mice in Plan9 operating system
• Criticism of cryptography efforts that sabotage post-quantum and other cryptographic methods
• Discussion of older curves and their benefits, including those not developed by NIST
• NIST curve security and the publication of improved mathematical formulas for them in 2016
• Challenge to find the hash used to generate certain curves, with a $12,000 bounty
• Unpopular opinion that NIST curves are secure and reliable
• Discussion of delivery methods for the bounty, including a suitcase or burlap sack
• Mention of upcoming episodes on related topics, including quantum cryptography