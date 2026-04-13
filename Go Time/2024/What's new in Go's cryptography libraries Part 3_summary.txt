• Fencing terminology and history
• Upcoming Go 1.23 features, including encrypted client hello (ECH) and hybrid public key encryption (HPKE)
• ECH's API implications and potential exposure in the standard library
• Post quantum connections and key exchange algorithms
• Crypto TLS and protocol changes for improved security
• Implementing post-quantum secure cryptography (ML-KEM) in Go
• Supporting only one parameter size (768) initially and possibly expanding later
• Exposing ML-KEM in Crypto TLS for interoperability with other implementations
• Collecting metrics and feedback on the new implementation
• Testing the release candidate to identify potential issues before the final release
• Addressing interoperability concerns with other implementations of ML-KEM
• Planning to support post-quantum key exchange in Open SSH, possibly using a different algorithm (NTRU)
• Potential changes to the x/crypto package and deprecation of certain packages
• Proposal to move important packages from golang.org/x/crypto to standard library
• Purpose of moving packages is to simplify and clarify the purpose of x/crypto module
• Packages will be moved gradually, with some requiring changes before being moved
• SHA-1 deprecation and removal process discussed, including Go debug flag and environment variable for disabling SHA-1 in crypto SSH
• ISO compliance and FIPS requirements mentioned as factors in SHA-1 usage
• Plan to remove SHA-1 support entirely in future release (Go 1.24)
• Other improvements to be made to crypto packages, including exposing supported algorithms and simplifying algorithm selection
• Algorithm negotiation errors will be more structured and easily understandable
• Support for new hashes (SHA-256) has been fully implemented
• Fixed bugs related to mismatch between key type and algorithm type in SSH
• Implementing BoringSSL Test Suite (BoGo) to test Go TLS stack and improve interoperability with other implementations
• Sharing test vectors across different cryptography implementations to ensure consistency and correctness
• Mount Wycheproof is in Australia, not America
• Filippo Valsorda admits to spreading fake news about the location of Mount Wycheproof
• Discussion of changes in Go 1.23, specifically in the crypto/rand package
• Plans to improve crypto/rand by making it more efficient and user-friendly
• New API for generating random strings with a specified character set
• Critique of password requirements on websites that are too restrictive
• Mention of browser games and prompt hacking exercises as examples of password security challenges
• Discussion on lightning talks and submissions
• Security focus at conferences, including a talk by Zvonimir on Go vulnerability analysis
• Vulnerability scanning and reporting, including the potential for false positives
• Use of govuncheck to manage vulnerability reports
• Importance of testing release candidates, especially for unusual codebases
• Maintaining open source software, including Nicola Murino's unpopular opinion that companies should pay for open source software they rely on
• The value of sustainable funding and support for open source projects
• The limitations of contributing patches or features to open source projects, which can create maintenance burdens for project maintainers.
• Discussion of the benefits of having a fixed location to work on computers
• Laptops vs desktops: preference for using a desktop PC and avoiding portability
• Pigeons as misunderstood animals, not "flying rats", but rather dependent on humans
• Rats as pets vs. pests, with some members having positive experiences with pet rats
• Discussion of release planning and aligning with the Go language's release cycle