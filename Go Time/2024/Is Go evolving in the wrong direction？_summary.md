• Chat GPT and LLMs: the limitations of current technology, the importance of grounding models in reliable data, and potential solutions such as pairing with knowledge graphs
• Go language evolution: complexity, added features (generics, iterators), and their impact on users and developers
• Generics: whether they add significant complexity to the language and improve usability for everyday users
• Iterators: concerns about potential pitfalls and inconsistencies in using iterators, but also potential benefits of standardizing this functionality
• The speaker discusses the addition of new iterator syntax in Go, which they think will be useful and not overly complex.
• They note that the push-pull semantics are "wonky" but that their initial concerns about complexity may be unwarranted.
• The speaker compares the situation to generics, which was initially difficult for long-time Go programmers to adjust to but ultimately simplified code.
• They argue that having a standardized pattern for iterators will simplify code and make it easier to understand.
• The speaker thinks that old iterator styles can be deprecated over time, allowing for eventual consistency in iterator implementation.
• Discussion of Go's simplicity vs added complexity
• Argument about Go's performance in comparison to Rust
• Reddit thread on whether software should be written in Go or not
• Criticism of Go for real-time and high-performance applications
• Defense of Go's garbage collection and memory management
• Debate on using Go for GUI development
• Discussion of custom JSON decoder building tools and their importance
• Discussion of XML canonicalization in Go programming language
• Challenges with parsing XML in Go, particularly with namespace handling
• Comparison of Go libraries for encoding/decoding data (e.g. JSON)
• Soap usage in Go and its avoidance
• Excel macros and their potential dangers
• Debate on software types that should or shouldn't be written in Go
• Leslie Lamport's work on distributed systems and teaching concurrency
• Quote from Lamport's paper highlighting the importance of conceptual thinking over language choice
• The importance of using the strongest language for a project, rather than trying to force a specific language on the project
• Limitations of Go as a language, including its inability to handle certain tasks such as real-time systems or GUIs
• Trade-offs between choosing the right tool and being flexible with language choices
• The idea that thinking about problems in terms of specific languages can be limiting
• The potential benefits of using alternatives to Make files for Go projects
• Comparison of Go's features with other programming languages, specifically Makefiles
• Discussion of Mage as a tool for building and managing projects in Go
• Critique of YAML syntax and its difficulties
• Alternative use cases for Makefiles and Mage
• Introduction to Speakeasy, an SDK workflow management platform
• Discussion of the current state of APIs and their development
• The Go team is locking down the "go link name" directive, which allows referencing unexported objects or symbols in other packages.
• This change will break code that has used this directive to access private variables or functions in other packages.
• The directive was intended for use with assembly code and accessing runtime components, but users have found ways to misuse it.
• The proposed change aims to prevent people from accessing unexported things in other packages, which is not what the language wants to happen.
• The "go link name" directive has been used in various situations, including accessing default cipher suites for TLS 1.3 and referring to assembly code.
• The Go team considers this change necessary but acknowledges it will break existing code that relies on this directive.
• Discussion about Go language coroutine functionalities and their limitations
• Critique of an article suggesting that package names should not be common nouns, with examples from the Go community
• Debate on the merits of prefixing internal packages with a letter vs using descriptive names
• Analysis of naming conventions in software development and potential pitfalls (e.g. reusing standard library package names)
• Discussion of the difficulty of establishing hard-and-fast rules for naming packages and preferring shorter, more descriptive names
• Reference naming conventions in code
• Use of common nouns as package names
• Use of underscores in package and file names
• Line length and function name length
• Unpopular opinions on software development practices and languages (specifically Rust)
• Critique of the emphasis on type safety and memory safety in programming languages
• Memory safety problems and the potential of Rust to solve them
• Criticism of Rust's approach as masking deeper issues with software design
• The need for software engineers to think deeply about problems they're trying to solve
• Insufficient training and languages for deep thinking in software development
• Comparison between programming languages, including C and Go, for simplicity and ease of use
• Importance of documentation and collaboration in software development
• Criticism of Rust's "replace C" approach as impractical and overly simplistic
• Focus on teaching people to write correct software rather than relying on tools or AI
• Concerns about the industry's emphasis on quantity over quality of software engineers.
• Rust's borrow checker and memory safety features are intended to minimize the impact of mistakes, not eliminate them
• Human error will always be a factor in software development, no matter how many tools or protections are in place
• The industry has given up on teaching critical thinking and instead relies on tools and language features to solve problems
• This approach dilutes the effort to truly improve software development and does not address the underlying issues
• There is a disconnect between the industry's focus on social justice and its treatment of issues like AI training data and model subjugation
• The primary problem with software today is not a lack of memory safety or type safety, but rather how developers think about code and write programs.
• Learning any new programming language requires more than just understanding its syntax; it also involves learning the language's paradigms, normal libraries, and idiomatic code writing.
• Pretending that a language is easy to learn can do a disservice to the community by setting unrealistic expectations for developers.
• Understanding the cultural nuances of a programming language and its community is crucial for effective use of the language.
• Siloing concepts into specific languages due to ease of learning can lead to a lack of conceptual understanding among developers.
• Importance of conceptual understanding vs. language-specific expression
• Leslie Lamport's paper on notation and its implications for recognizing similarities in different fields
• Difficulty of explaining technical concepts to non-technical people
• Value of being able to think critically and understand underlying principles
• Rust as a macro-level concept for learning how to think, rather than just a programming language
• Critique of the industry's tendency to focus on language-specific details over conceptual understanding