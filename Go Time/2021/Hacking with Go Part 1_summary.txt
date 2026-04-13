• Introduction to Joakim Kennedy and Juan Andrés Guerrero-Saade as occasional Go community members
• Discussion of what "hacking" means in the context of the conversation (security research)
• Common programming languages used for hacking: C, C++, Delphi, compiled Python
• Challenges of reverse-engineering malware binaries, including stripped symbols, missing debug information
• Advantages of using Go due to its inclusion of additional data structures that make it easier to reverse-engineer
• The difficulty of reverse-engineering Go binaries due to the lack of understanding of the Go paradigm and the linker's behavior
• The presence of extraneous information in Go binaries that can make analysis difficult
• The myth that Go is an easy language to reverse-engineer, which is actually not true
• How the linker needs debug information to function correctly, making it difficult to remove
• The ability to reconstruct type definitions and function names from the binary using reflection and runtime data structures
• The challenges of writing malware in Golang due to its features and efficiencies
• The value of using scripts to undo debug stripping and put back function names for easier analysis
• How Go's fascist design allows for easy separation of standard library functions from user-written code
• The difficulty of analyzing large binaries with thousands of functions, and the usefulness of processing scripts to simplify this process.
• Discussion of challenges in reverse-engineering modern languages such as Go and Rust due to statically linked libraries
• Comparison of reversing C++, Go, and Rust, with each presenting unique difficulties
• Importance of function names and types in understanding binary behavior
• Obfuscation techniques used by malware developers, including naming functions with misleading or confusing titles
• Discussion of the cat-and-mouse game between malware developers and security researchers
• The balance between the fun and complexity of coding and hacking
• The growing seriousness and consequences of hacking, including nation-state involvement and cybercrime
• The distinction between different "hats" in cybersecurity: white hat (defender), black hat (attacker), red team (simulated attacker), blue team (defender)
• CTFs (Capturing the Flag) competitions for learning about hacking and cybersecurity in a controlled environment
• Different types of Capture the Flag challenges
• Reversing binary code in various programming languages (Go, Rust, Nim)
• New generation of malware writers using modern languages instead of Assembly or C
• Challenges of reverse-engineering code with features like defer statements and concurrency
• Impact of new language features on reverse-engineering (e.g. Go 1.18 generics)
• Variations in Go compiler settings and target platforms cause issues for malware detection
• Go 1.7 beta 1 had a unique data structure with a 32-bit int size, which caused issues in malware detection
• Russian threat actors rewrite their code in different languages to evade detection
• Zebrocy group has used multiple programming languages, including Delphi, Python, and Rust, for their malware
• Go's concurrency features are attractive to malware authors due to ease of use and strong encryption libraries
• InfoSec Twitter community is known for hot takes and insults, with users often going at each other spitefully
• Discussion of using Go for cross-compilation and its benefits
• Malware development community in Go and red teaming community's understanding of Go
• Psychology of white-collar crime and hackers thinking they can get away with it
• Importance of good coding practices and version control for malware development
• Nation-state-sponsored attackers starting to use Go and Rust for malware
• Current state of nation-state malware, using C++ and highly engineered code
• Future possibilities of AI-generated malware and nation-state attacks in the next episode
• Attack chains and exploit development require extensive knowledge of the target system
• JavaScript is often used as a first-stage vector for malware operations
• VBScript was used in the Love Bug malware attack
• Node.js can be used to package JavaScript malware into a single binary
• The InfoSec community lacks robust engineers, with many reversers and threat-hunters coming from non-engineering backgrounds
• There is an opportunity for Go developers to get involved in security and improve outdated tooling
• Open-source solutions like Osquery are viable options for security detection
• Software developers may have a poor security posture due to reliance on unsecured package managers (e.g. Brew, npm, Pip)
• Different generations have varying levels of internet savviness, making some more vulnerable to scams
• Software developers have more critical information at risk if compromised
• Open source communities should not rely on commercial products but instead use open source alternatives
• GDPR has little genuine value and is primarily "feel-good security posturing"
• Overly complex cookie settings on websites can be annoying and intrusive