• Introduction of David Chase and his background in programming languages compilers and runtimes
• Explanation of the components involved in a compiler and its phases (scanning, parsing, semantic analysis, etc.)
• Description of the Go compiler process (characters -> AST -> SSA) and optimization
• Discussion of escape analysis and its role in identifying memory allocation
• Overview of contributing to the Go compiler (importance of benchmarks and starting with lowering code from generic SSA)
• Clarification on the current state of the intermediate Go Assembler step
• Discussion of compiler internals and recommended reading
• Overview of various compiler books, including those by Andrew-Appel
• Reference to the LCC compiler as a relatively small and easy-to-understand example
• Explanation of the Go compiler's complexity due to its success and portability
• Mention of potential improvements to the Go compiler, including lazy import and mid-stack inlining
• Discussion of upcoming features for 1.10 and 2.0, including:
	+ Improved debugging experience for optimized code
	+ Cooperative scheduling enforcement within tight loops
	+ Generational collection work and write barrier optimizations
• Go language vs implementation discussion
• Advantages of multidimensional slices in Go
• Generics as a potential feature for Go
• Compiler optimizations and speed considerations
• Importance of simplicity and readability in compiler design
• Formal verification of compilers and its challenges
• Trusting Trust paper mentioned as relevant to compiler security
• Verified code and testing
• Compiler verification for different targets (e.g., x86/64, ARM)
• Balance between compiler speed and optimization complexity
• Potential for using LLVM as a backend for Go
• Pie preferences of the Go compiler team
• Discussion about pies and pie preferences
• Recommendation for Emeril Lagasse's banana cream pie at his restaurant
• Proposal to consider hosting GopherCon at a location with good food options, specifically including the pie mentioned earlier
• Review of recent Go projects and news
• Discussion of Oak game engine and its potential for use on PocketCHIP
• Overview of PocketCHIP as a small, portable computer with Linux capabilities and discussion of its uses
• Mention of new book "Concurrency in Go" by Katherine Cox-Buday
• Discussion about a well-written post on cluster schedulers
• Shoutouts for open-source projects and individuals, including Dave Cheney's Go blog and errors package
• Review of GopherCon 2019 and its contributor day
• Stats from Jess Frazelle on new open CLs
• Thank you to Steve Francia and others who contributed to the GopherCon remote event
• Discussion about MacPorts and its quality compared to Homebrew
• David Chase shared his experience with a tech toolchain on a laptop 5 years ago
• The setup included MacPorts, Track, Python, SQLite, Mercurial, Emacs in bash-mode, and code processing
• The project was for a website that formatted code into a mathematical style
• The conversation was part of the GoTime.fm podcast