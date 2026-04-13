• Discussion of the article "Go evolves in the wrong direction"
• Concerns about increased complexity with generics in 1.18
• Debate on the value of iterators in 1.23, including potential complexities and benefits
• Comparison to generics, which were also seen as adding complexity but ultimately beneficial
• Potential for iterators to simplify code and error handling, despite added complexity
• Mention of push/pull semantics being "wonky" and needing adjustment
• Debate about adding error handling to the language through a regular for loop or range loop
• Discussion on consolidating iterator patterns and providing a standardized way to iterate in the language
• Argument that languages must become more complex over time to maintain backwards compatibility and simplicity
• Comparison of Go's performance with Rust, including the use of SIMD instructions
• Debate about whether certain types of software should not be written in Go (e.g. embedded firmware, GUIs)
• Discussion on garbage collection and its potential impact on real-time systems
• Difficulty with custom encoding/decoding in Go
• XML handling issues, particularly with namespaces and canonicalization
• Avoiding Go for certain tasks like SOAP and Excel macros
• Go's ability to handle any software concept (it is Turing complete)
• Importance of choosing the strongest language for a project or startup
• Focusing on conceptual thinking rather than specific languages
• Discussion on the limitations and suitability of Go for certain types of software
• Importance of nuance when evaluating programming languages for specific tasks
• Tooling as a consideration when choosing a language
• Problem with thinking in terms of language-specific solutions rather than problem-solving
• Alternatives to Make files written in Go, specifically Mage vs. Taskfile
• Mage as a build system for Go code
• go:linkname directive and its limitations in Go 1.23
• Changes to the go:linkname directive in Go 1.23
• Impact on existing code that uses the directive
• Discussion of Russ Cox's proposal to lock down the directive
• go:linkname usage in assembly and coroutine functionality
• Article "Go. Don't name packages common nouns." and its author's suggestions for naming conventions
• Package naming conventions
• Avoiding common nouns in package names
• Use of prefixes (e.g. p for Crunchy platform)
• Importance of clear and concise package names
• Dangers of overly long or ambiguous package names
• Personal opinions on naming conventions versus standardization
• Usage of underscores in file names versus package names
• Criticism of Rust's emphasis on memory safety and borrow checking
• Leslie Lamport's paper "Computation and State Machines" and its influence on Kris' thoughts on programming
• The issue of programmers being more focused on using the right tools rather than thinking deeply about the problem
• The concept that software engineers often lack training in languages that allow for deep thought and documentation
• Go as an example of a language that allows for simplicity and ease of development
• Concerns about the "monkey typing code" mentality and the industry's reliance on tools over thought
• Critique of Rust's marketing approach and its perceived replacement of C as a necessary step towards solving software problems.
• Concerns about Rust's emphasis on memory safety and borrow checking as a solution to software problems
• Criticism of the industry's reliance on tools and languages to fix problems rather than addressing underlying issues with programming concepts and understanding
• Discussion of the importance of teaching programmers how to think critically and write good code, rather than relying on language features
• Comparison of Rust to other languages, such as Assembly and Lisp, in terms of their suitability for writing good software
• Argument that the industry's focus on new languages and tools has diverted attention away from more fundamental issues with programming education and practice.
• Learning a programming language is not just about syntax, but also about understanding its paradigms, normal libraries, and idiomatic code.
• A language's culture and community can be difficult to learn and understand, especially when it differs from one's own cultural background.
• Focusing on conceptual understanding and mapping ideas into the language is more important than relying solely on a specific programming language or toolset.
• The industry needs to focus on learning how to think critically and intensively about problems, rather than just relying on technical skills.