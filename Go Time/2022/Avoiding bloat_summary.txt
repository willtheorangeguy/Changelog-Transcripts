• Definition of bloat in Go programming
• Types of bloat: code bloat (large codebases) vs binary bloat (large deployment sizes)
• Impact of imports on code size, using protobuf and gRPC as examples
• Statistics on lines of code imported from protobuf (27,000) and gRPC (100,000+)
• Discussion of why people might prefer smaller libraries like Net RPC over larger ones like gRPC
• Code bloat and its impact on build times
• The importance of reviewing and maintaining code dependencies
• Tools for analyzing and visualizing dependencies (Goda)
• Principles for choosing packages with minimal dependencies
• Trade-offs between package size and complexity vs. maintainability
• Codebase organization and dependency relationships in large projects
• Cyclic dependencies in Go codebases can lead to maintainability issues
• Binary bloat: large binaries are becoming more common, but may not be a concern for many users due to fast upload speeds
• Small devices (e.g. Raspberry Pi) have limited storage and may be affected by binary size
• TinyGo is an attempt to address the problem of small device limitations by creating a smaller standard library
• Nostalgia: discussion about older computers, floppy disks, and other retro tech
• Using Go with TinyGo for embedded devices
• Debouncing code in TinyGo for handling button noise
• Comparing Go and C for structured programming
• Discussion on binary bloat and its impact on small devices
• Advantages of using TinyGo for web development (WASM)
• Fmt package size and dependencies contributing to binary bloat
• The benefits and drawbacks of Rust's macro processing and its impact on code complexity
• Code bloat and its relation to technical debt in large projects
• Strategies for managing complexity, including testing, mocking, and integration testing
• Definitions of technical debt, including concepts of cost, prioritization, and mortgage analogy
• Technical debt as the difference between an ideal state and a current state of maintainability or effort required to maintain a codebase
• Designing for flexibility and change
• Avoiding "unchangeable decision" thinking and prioritizing adaptability
• Importance of upfront design and thinking through possible futures
• Abstraction and designing the right abstractions from the start
• Deletability: designing things so they can be easily deleted or removed
• Practicing abstraction and getting it wrong as a learning process
• Designing features for specific use cases vs general solutions
• Reviewing dependencies and codebases with similar standards as own codebase
• Responsibility for reviewing and maintaining dependencies
• Approaches to reviewing dependencies (e.g., reading every line, looking at code quality)
• Time management and productivity while working on a laptop vs large desk setup
• Discussion of productivity environments and tools
• Analysis of the impact of technology on work habits
• Exchanging opinions on text editors and keyboard usage
• Debate about shower gel vs. traditional soap or sponge
• Conversation about personal preferences for computing equipment (e.g. touchpads, touchpoints)
• Discussion of using bar soap as an alternative to traditional shampoo bottles
• Concerns about shower gel usage in areas with soft water
• Preference for rough, rugged soap and towels over soft options
• Suggestions for alternatives such as steel wool or loofahs for personal hygiene
• Personal anecdotes and humorous remarks from the participants