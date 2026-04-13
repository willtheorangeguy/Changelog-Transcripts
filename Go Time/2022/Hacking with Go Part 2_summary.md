• Discussion of Ivan Kwiatkowski's work as a senior security researcher at Kaspersky
• Analysis of the SolarWinds attack and its impact on high-profile customers
• Reverse-engineering of malware written in Go, including SUNSHUTTLE and Stowaway
• Examples of other malware families written in Go, such as Brute Ratel
• Ease of use for developers due to statically-built executables
• Difficulty of reverse-engineering Go programs due to goroutines and architecture
• Advantages of using Go for attackers due to its ease of use and difficulty of detection
• Go's unique assembly generation makes it difficult to analyze using traditional methods or automated tools
• The compiler's optimization techniques, such as reusing memory space for local variables, can make variable tracking and renaming challenging
• Return values in Go often require manual handling due to the language's ability to return multiple values and the lack of a standard register for storing them
• Changes in Go convention, such as passing arguments through registers instead of the stack, have improved analysis but not resolved the core challenges
• Go compiler creates code that is difficult for reverse-engineering tools to decompile
• IDA Pro struggles to recreate pseudo C code from Go language, due to its concepts and complexities
• Reverse engineering involves understanding a program's behavior without source code access
• Malware authors often use complex languages like Go to make analysis more challenging
• The ratio of Go lines to assembly code can be as high as 1:100 or 1:1000
• Other languages, such as C and C++, may have similar ratios, but the problem is not the number of assembly instructions, but rather their complexity and unexpected behavior
• Improvements in tooling and pattern recognition are needed for better Go language support
• Go's compiler can jump between different sections of code unexpectedly when debugging
• This can be confusing for reverse-engineers who are used to seeing the flow of instructions in other languages
• Go's compiler optimizes function calls by reusing variables on the stack, making it harder to understand the program flow
• The language is very strict and enforces conventions at compile-time, which can help with reverse-engineering by providing clear expectations about code behavior
• Go's consistency and predictability make it a good choice for hackers and security researchers who are used to dealing with traditional languages
• Discussion of programming languages used by hackers and researchers
• Advantages and limitations of memory-safe languages like Go
• Types of malware and attack methods (lateral movement, stealthy attacks)
• Role of incident response teams and antivirus companies in collecting and analyzing data
• Comparison between working with incident response cases versus analyzing telemetry data from antivirus
• Tips for writing secure software in general, with focus on Go's memory safety features
• Go language and its security features
• Using Go for reverse-engineering malware
• Challenges of reversing Go code due to compiler optimizations
• Tools available for reverse-engineering Go (IDA, Ghidra)
• Importance of understanding basics of reverse-engineering in traditional C or assembly code before moving on to other languages like Go
• Recommended resources for learning reverse-engineering and the Go language
• Practical Malware Analysis book as a resource for beginners
• Using Steam games for reverse-engineering practice (Turing Complete, TIS-100, EXAPUNKS)
• Zachtronics' education program and free game access for universities and educators
• Unpopular opinions on:
  • Cyberspace regulation
  • NFTs being a scam
  • Lack of political will to limit cyber offense tools sales
  • USB-C standardization in Europe
  • Dislike of Apple ecosystem and their revenue stream from charger sales
  • Ambiguity about walled gardens (e.g. Google Play Store, Apple Store) for security and user agency
• The NFT contest and its potential divisiveness among the audience
• Cyber regulation: the difficulty of reaching a consensus on norms for behavior in cyberspace
• The incentives of states to regulate or not regulate cyber offense
• The balance of risk/reward for decision-makers regarding cyber operations
• The possibility that discussions about creating a safer internet are being conducted in bad faith.