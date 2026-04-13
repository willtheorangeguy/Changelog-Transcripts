• The increasing stakes and risks of ransomware attacks, particularly in the US
• Consequences of outdated systems (e.g. Windows XP) being targeted by hackers
• Difficulty in balancing the appeal of hacking "superpowers" with their darker side
• Discussion of industry best practices for remote access and security, including identity-based authentication and unified auditing
• Introduction to Teleport, a solution that provides secure, unified access to cloud resources
• Discussion about hacking and security research
• Favorite programming languages used by hackers
• Differences in malware development, including language and compiler usage
• Challenges of reverse engineering compiled binaries with stripped symbols and no source code
• Benefits of using Go due to additional data included in compiled binaries
• The Go programming language has some unique characteristics that make reverse engineering easier than other languages.
• The linker in Go is designed to include debug information, which can be useful for reversing.
• Reverse engineers can use this information to understand the binary's functionality and reconstruct type definitions.
• However, if all debug information is removed, the linker may break, making it harder to reverse engineer.
• The ease of reverse engineering Go has implications for malware writing, as Golang's features (such as concurrency) are now more accessible to malicious actors.
• The conversation concludes that learning to love reversing Go is possible due to its relative simplicity.
• Debug stripping and function names in compiled code
• Using Go's compilation process to separate standard library functions from user-written ones
• Challenges of reverse engineering Go binaries due to their complexity and dynamic nature
• Comparing simple Go binaries to identify differences
• Issues with compiler versions, imports, linker variations, and target architectures
• Comparison to C++ binary analysis, which also presents challenges due to its compilation process
• Discussion of reversing Rust and its challenges
• Comparison to C++ and Go languages
• Shift from dynamic linking to statically linking libraries as a major hurdle in analysis
• Challenges of dealing with large libraries and unknown function calls
• Unfair treatment of Rust compared to Go
• Potential for improvement in tools and familiarity with paradigm
• Comparison to reversing C++, which is also difficult
• Function naming and identification in malware binaries
• Obfuscation techniques used by malware developers
• Reverse engineering process and challenges
• Balance between making malware difficult to understand and avoiding detection by antivirus software
• The "cat and mouse" game between malware developers and security researchers
• Historical context of hacking and programming as a motivator for some individuals
• The internet has become a playground for nation states and criminals
• Ransomware is widespread and unavoidable in many industries, including healthcare
• Hacking can have a "dark side" where real people are affected by malicious actions
• There is a distinction between red team (pen testers), blue team (defenders), and white hat hackers
• Red teamers simulate attacks to identify vulnerabilities, while blue teamers work to fix them
• White hats are those who work towards improving the general defensive stance of an organization or company
• CTFs (Capture The Flag) are a type of hacking competition where participants try to solve challenges or problems in a simulated environment
• Access to networks by unauthorized parties
• Evolution of cybercrime from simple data theft to ransomware and network infections
• Different categories of hackers: black hats, white hats, and gray hats
• Capture the flag (CTF) competitions as a way for beginners to learn hacking skills
• Reversing capture the flag challenges, such as the Flare-on challenge
• New programming languages like Go and Rust becoming increasingly popular in malware development
• Changes in the paradigm of programming languages used by hackers
• The speaker finds learning Go to be relatively easy due to familiarity with its paradigm.
• Reverse engineering is challenging, particularly when dealing with assembly code and recognizing C-level constructs.
• The speaker suggests that understanding Rust concepts may make it easier for others to reverse-engineer Rust binaries.
• They express difficulty in reversing Rust binaries due to lack of familiarity with the language and internal data structures.
• The introduction of new language features, such as generics in Go 1.18, may cause issues with tooling and require updates.
• The speaker notes that compiler changes can affect parsing of internal data structures, making it difficult to maintain accurate tooling.
• Reverse engineering involves "stealing" information from the air, which can change over time due to compiler updates or optimizations.
• The size of an int in Go changed from 32 to 16 in some beta versions.
• This change caused issues with malware detection, as it threw off the normal analysis.
• The fact that Go is open-source makes it easier for attackers to adapt their code and evade detection.
• Some threat actors rewrite their code in different languages every few weeks to evade detection, making it challenging to keep up with tooling.
• An example of this was seen with a group called Cyberacy, who ported their malware from Delphi to Python to Go to Rust to Nim.
• This makes it difficult and inefficient for analysts to keep building tooling for every possible variation.
• Release of a peer-to-peer library for Go that was later used as the basis for a botnet
• IPFS (InterPlanetary File System) and its relation to the Go programming language
• Discussion on why malware developers with proficiency in Go are relatively rare compared to other languages
• Analysis of ransomware attempting to leverage Go's concurrency features for faster encryption
• Observations on amateurish mistakes made by malware developers, such as using OS-specific libraries and failing to utilize cross-compilation
• Criticism of InfoSec Twitter community for promoting hot takes and personal attacks over constructive discussions
• Discussion of a tool for hacking and its usefulness
• Comparison of cross-compilation to Goal
• Surprise at the effectiveness of the tool against malware
• Explanation of the lack of expertise among "bad guys" in Go programming language
• Comparison between professional hackers and those who moonlight as hackers
• Discussion of the psychology behind white-collar crime and hacking
• Advice on how to anonymize oneself when creating malware with Go
• Nation state sponsored attackers may start using Go and Rust for malware
• Current malware is often written in C++ with high-quality code and infrastructure
• Early days of nation states figuring out how to use new languages like Go
• Russian and Chinese groups are known to be using Go and Kubernetes for malware
• JavaScript is being used for early stages of malware operations, including profiling systems
• Nation states may start producing more sophisticated and professional malware
• Packaging malware with Node.js
• Benefits and opportunities for Go developers in the InfoSec community
• Lack of robust tooling in security space, including reliance on old Python scripts
• Need for more investment and innovation in security solutions
• Discussion of open-source software and its potential impact on security
• Business incentives for companies to work with the InfoSec industry
• Emphasis on fundamentals of computer science in security
• Unpopular opinions expressed about software developers' security posture
• Name squatting and typo attacks on package management systems
• Security vulnerabilities in commonly used development tools (e.g. brew, NPM, pip)
• Comparison of security risks for software developers vs casual Internet users (grandmothers)
• Importance of open-source alternatives to commercial products
• Discussion of decentralized communication platforms like Matrix and their potential drawbacks
• The changing nature of remote work and trust in large corporations
• Unpopular opinions on technology, including the USA being superior and GDPR being ineffective
• Issues with website cookies and user consent
• AI-generated malware as a potential future topic of discussion