• Introduction and setup of the podcast
• Discussion about the Crypto library in Go and its history
• History of the Crypto library's addition to the standard library (10-11 years ago)
• Goals and design principles of the Crypto library
• Focus on providing Go developers with what they need, rather than competing with other cryptography toolkits
• Emphasis on security and avoiding unnecessary complexity
• Discussion about explicitly not implementing certain features in the standard library to avoid potential vulnerabilities
• Discussion of new features in the Go crypto library
• RSA backend change, replacing math/big with a custom implementation (big/mod)
• Performance improvements for RSA decryptions and signatures
• Introduction of a new package (crypto/ecdh) for elliptic curve Diffie-Hellman key exchange
• Removal of low-level concepts from API to improve user experience
• Discussion on deprecating old elliptic curve API and designing a new one
• Explanation of why a new API is being implemented (e.g. security concerns with old implementation)
• Mention of using formally verified code generator for certain parts of the new API
• Reference to RSA being outdated and slower, and how elliptic curves are preferred in cryptography
• Discussion on the compatibility guarantee in Go and its limitations in making changes without breaking existing code
• Explanation of why some security issues cannot be fixed due to backwards compatibility concerns
• The importance of maintaining backwards compatibility in software development
• Deprecation process: what it means, and how it differs from removal
• Vulnerability patches for deprecated packages: current policy and considerations
• Hash function deprecation (e.g. MD5, SHA1) due to security concerns
• TLS protocol version deprecation (e.g. TLS 1.0, 1.1)
• Default settings vs. application developer control in software development
• The origin of the "go debug" environment variable, which was initially used to turn on SHA-1 and is now a more general mechanism for preserving behavior.
• The trade-off between configurability and security, where having too many options can lead to insecurity if not managed properly.
• The removal of automatic cipher suite ordering in TLS, which allowed developers to express their opinion on preferred encryption methods but was ultimately removed due to concerns over security risks.
• Two specific attacks: the Bleichenbacher '98 attack, which exploits timing vulnerabilities to decrypt RSA-encrypted data; and the Bleichenbacher 06 attack, which creates fake signatures by adding garbage data to a signature.
• Discussion on the math behind cryptographic signatures and approximations
• Vulnerability in YouTube DL self-update code due to hardcoded exponent
• Backward compatibility issues with Go debug flags and proposed solutions
• New policy for Go debug flags to preserve backward compatibility and introduce metrics for tracking usage
• Future plans to remove unnecessary Go debug flags based on collected metrics and analysis
• Fallback roots for TLS certificates and the uniqueness of the Go language in not providing a bundled set of root certificates
• A new API was added to register a default set of root certificates for trust
• This solved a problem but introduced the need for an additional certificate bundle update mechanism
• The mozilla certificate bundle is now part of the golang.org/x/crypto module as a separate sub-module
• A bot automatically updates the list and sends notifications when changes occur
• There have been issues with the automated PRs, including forgotten status code checks
• Discussion about introducing new packages in the standard library due to changes in the world since the original code was written
• The math/rand package is being rewritten as v2 with a more secure default algorithm (Cha-8) and removing the read method to prevent misuse
• Compatibility promise issues with math/rand
• Deterministic random number generation in math/rand
• Cryptography library maintenance and API improvements
• Simplifying AEAD (Authenticated Encryption with Associated Data) encryption
• High-level APIs for non-repeating nonce (number used once) generation
• Exposing secure defaults to users, rather than requiring knowledge of arcane details
• Cryptography libraries and making mistakes
• Post-quantum algorithms in standard library
• API design choices and potential future consequences
• Experience with existing algorithms (e.g. RSA) vs new ones
• List of planned changes to crypto package, including SSH and TLS
• Maintaining and updating packages like SSH
• Changes to CI companies' security
• Support for keystroke obfuscation in OpenSSH
• Interview with Nicola and possible future episode
• Discussion of terminal text editors (Emacs, Vi/Vim, Pico, Joe)
• Opinions on the best text editor
• Using Alpine email client is necessary for the conversation
• Pico text editor is being discussed and praised as easy to use
• The speaker has struggled with Emacs and Vim, finding them difficult to learn
• The conversation turned to keyboard shortcuts and mouse usage in programming
• Plan 9 is mentioned as a system that relies heavily on mouse interaction
• Elliptic curves standardized by the National Institute of Standards and Technology (NIST)
• Criticism of NIST's involvement in cryptography
• Conspiracy theories surrounding NIST and NSA collaboration
• Alternative elliptic curves not developed by NIST
• Defense of NIST's elliptic curves, citing improved formulas for them
• Discussion of a proposal to deliver something in a suitcase
• Mention of a burlap sack with a dollar sign on the side as an alternative option
• Reference to a "theater kid" perspective and desire for drama
• Discussion of international border crossings and potential restrictions
• Acknowledgment of lack of knowledge about the history of something, but assurance that it is secure
• Comparison of NIST curves and their perceived safety and effectiveness
• Mention of opposing opinions on the matter
• Prediction or expectation of criticism and backlash for an unpopular opinion
• Taking hostages of babies and kids with a political opinion should be condemned by everyone
• New music album available on Spotify and Apple Music
• Changelog beats is now a thing, includes special remixes and video game-inspired tracks
• Upcoming episodes of the show on quantum stuff, Halloween theme, and more
• Countdown timer
• Game start signal
• Game duration (approximately 13 minutes)
• Score or round number (number 9)