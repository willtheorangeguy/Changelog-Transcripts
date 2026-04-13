• Background of guest Damian Gryski
• Experience with busking and magic before transitioning to computer science
• Performance optimization and the creation of a performance book for Go
• Importance of considering performance in software development, particularly in infrastructure building
• Approaches to measuring and improving performance in Go applications
• Percentage of Go developers who should care about performance
• Performance optimization is not always necessary for most applications
• Choosing a suitable programming language can significantly improve performance (e.g., Go vs. C)
• Profiling should be the first step to identify bottlenecks before optimizing
• Focus on the biggest bottleneck and make it faster or reduce its frequency of occurrence
• Strategies include batching, caching, minimizing garbage collection allocations, and processor-level optimizations
• Using unsafe and cgo for performance improvements
• Writing Assembly code for specific use cases
• Importance of data structures and algorithms for optimization
• Go's built-in data structures (slices, maps) are sufficient for most use cases
• Learning about esoteric data structures is not necessary, but knowing they exist can be helpful
• Recommended learning approach: focus on a few essential data structures, such as heaps and bloom filters
• Bloom filters, count-min sketches, and treaps are highlighted as interesting and useful data structures
• Damian Gryski's GitHub page features implementations of technical papers in Go.
• The discussion focuses on consensus algorithms such as Paxos, Raft, Chubby, and Zookeeper.
• Paxos is criticized for being dense and difficult to understand, with different interpretations leading to varied implementations.
• Chubby paper highlights the complexity of implementing consensus algorithms and the need to consider edge cases not covered in theory.
• Fuzzing is introduced as a method of randomized testing to identify edge cases and bugs in programs.
• Go-fuzz is mentioned as a tool for making fuzzing easy for Go, using coverage-guided fuzzing to narrow in on interesting inputs.
• The DARPA Grand Cyber Challenge is discussed as an example of automated systems that could detect and patch attacks.
• Discussion of Go-fuzz and its use for finding crashes and comparing implementations
• Release of Go 1.9.3 with minor bug fixes and no major security issues
• Upcoming release of Go 1.10, targeted for mid-February
• Skydive project: an open-source network topology and protocol analyzer
• Metaparticle project: a tool for building abstraction over Kubernetes and Docker
• Discussion of Francesc's videos on Just For Func channel
• Discussion of a tool (kr/pretty) for debugging in Go programming language
• Mention of Richard Musiol's work on WebAssembly compiler for Go
• Excitement about future potential of WebAssembly support for Go
• Thank yous to Damian Gryski and discussion of his upcoming book
• Wrap-up of the podcast, with thanks to listeners and an invitation to submit suggestions or appear as a guest