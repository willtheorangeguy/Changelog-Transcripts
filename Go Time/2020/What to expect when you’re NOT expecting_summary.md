• eBPF and Delve tracing systems discussed
• Possibility of replacing ptrace with eBPF-backed tracing system on Linux
• Introduction to Go Time podcast and GopherCon session
• Discussion of bugs, their definition, and prevention methods
• Expert panel includes Hannah Kim from the Go team and Grant Seltzer-Richman
• The speaker discusses the absurdity of writing code with no bugs
• Definition of a bug as unexpected or incorrect behavior
• Discussion on how bugs can emerge from interactions between different parts of code or simple mistakes
• Explanation that debugging is not just removing bugs but understanding what's causing them
• Importance of having a quick feedback loop when debugging
• Different methods for debugging, including adding print statements and using tools like Delve and the FMPT package
• Use of test code as a way to debug and identify bugs
• Discussion of debugging tools and their limitations
• Description of Delve as a debugger for Go
• Explanation of how a debugger works, including setting breakpoints and inspecting program state
• Comparison of debugging methods, including print statements and traditional source-level debugging
• Importance of gaining insight into a program's behavior when debugging
• Real-time interaction with debugging tools
• Delve debugger capabilities
• Dwarf information in binaries for debugging
• Optimization options in Go compiler
• Integration of Delve with VS Code plugin
• Debug adapter protocol standardization
• Communication between debuggers and editors
• Overview of Retool and its benefits for building internal tools
• DoorDash's experience with manual data entry and long turnaround times in their internal tooling process
• How Retool helped DoorDash cut engineering time by a factor of 10x and eliminate error-prone manual processes
• Rohan Chopra's quote on the value of Retool for empowering teams and reducing dependency on engineering
• Introduction to eBPF (Extended BPF) and its ability to add logic to the Linux kernel
• Go program tracing with eBPF, specifically using uProbes to attach scripts to source code symbols
• eBPF runs in its own virtual machine inside the Linux kernel and doesn't stop the program from running
• The advantage of eBPF is that it allows for inspection without attaching to the process, making it useful for debugging and testing
• Use cases include strace-like functionality for Go programs, fault injection, and simulating external dependencies
• eBPF programs can be written in a subset of C (called BPF) and compiled using an LLVM-backed compiler
• The Linux kernel includes a verifier that checks the bytecode before loading it
• The technology has been around since early 2000s but the ecosystem has developed significantly within the past two years
• Facebook contributes to the EBPF community
• The ecosystem is developing and now is a good time to start using EBPF
• Community helps each other with EBPF development and definition of best practices
• Using EBPF can be powerful but also requires caution
• Delve has an API for tracing, but it's not as efficient as EBPF due to context switching
• Using EBPF in production could be easier and safer than traditional methods
• Tooling for Go development in VS Code
• History and transition of VS Code Go plugin maintenance from Microsoft to Google's Go team
• Current projects and priorities on Go tool team
• Features being worked on, including using GoPlace as a default language service and improving debug experience with a new adapter protocol
• Delve: current status, plans for future releases, and upcoming features such as core dump creation during interactive debugging
• Delve only supports a subset of Go architectures, but it does support popular ones like AMD 64 and ARM 64.
• There are outlier architectures that Go supports but Delve doesn't, such as PowerPC 64 and S390X.
• Apple Silicon is an interesting case, with Delve using LODB server as the backend on macOS due to issues with the mock kernel documentation.
• The scope of the Delve source code has grown and become more complex over time.
• New features in Go can have varying impacts on Delve, sometimes providing benefits for free, while other times requiring coordination with the Go team.
• The conversation starts with a discussion about baseball metaphors
• Discussion turns to whether baseball is a good sport
• Participants mention that baseball is not widely played outside of the US, some Asian countries, and Latin America
• Derek states that he doesn't think baseball is exciting, but others disagree
• Unpopular opinions are discussed, including one person's opinion that Linux would make the world better
• Another guest mentions using Linux due to its compatibility with various apps and platforms
• A conversation about Delve and contractual obligations wraps up the discussion
• Closing remarks and goodbyes
• Upcoming episode with Ellen Corbis discussing Go in other languages
• Sponsor announcements (Fastly, Linode, LaunchDarkly)
• Personal anecdotes about kids asking for jokes via Alexa
• Explanation of a joke about ducks floating on water