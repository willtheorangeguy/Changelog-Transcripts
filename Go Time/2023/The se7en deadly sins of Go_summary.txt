• The Seven Deadly Sins of Go
• Introduction and background on the classical seven deadly sins
• Lining up the classic sins with potential Go coding mistakes (antipatterns)
• Discussion on the order and ranking of the sins
• Kris Brandow chooses sloth as the least worst sin from a moral standpoint
• John Gregory explains lazy coding as the Go version of the sin of sloth, including inadequate comments and lack of context in error handling.
• Importance of contextual comments in code
• Difficulty of understanding code without context, especially with aging codebases
• Value of why vs how in documentation
• Usefulness of contextual comments for debugging and maintaining code
• Limitations of unit tests and commit messages in providing context
• "Haunted gardens" (uncommented code) analogy
• Pride in library development
• Opinionated libraries
• Private APIs and difficulty with extension or modification
• Importance of providing options for users
• Avoiding assumption about how others will use the library
• Overly prescriptive design vs flexibility for users
• Discussion of concurrency in Go and how to avoid "sins" such as trying to use concurrency where it's not necessary
• Critique of AppCache and its attempt to provide a single solution for offline web applications, leading to the lesson that lower-level APIs are better
• Envy as one of the "not so bad" sins in Go programming, and how it can be used to improve code
• Writing Go like another language (e.g. Java) as a common mistake
• The use of channels vs mutexes for concurrency, with some arguing that we've swung too far towards using only channels
• The desire for a built-in way to return multiple values with an error from a channel
• The limitations of Go Time's influence on the future of the language
• Setting up and learning the Go programming language
• The ease of use and simplicity of Go compared to other languages
• The potential for overusing concurrency features in Go, leading to complicated code
• The importance of simplifying and avoiding unnecessary complexity in Go development
• The importance of code organization in Go
• The benefits of following idiomatic Go practices
• The potential drawbacks of using frameworks and dependencies excessively
• The concept of gluttony as overindulgence in unnecessary dependencies
• The value of simplicity and minimalism in coding, especially in web development
• Avoiding over-engineering and unnecessary complexity in software development
• Importance of simplicity and minimalism in coding
• Discussion on using frameworks vs writing custom code
• Error handling in Go programming language, specifically avoiding misuse of panic and proper use of checked errors
• Misuse of dependencies and imports in coding
• Best practices for using panic in Go
• When to use panic vs error handling
• Contextual use of panic, such as during initialization or debugging
• Panicking on user-submitted regular expression input
• Misuse of panic and its consequences ( wrath)
• Analogies between panicking in code and real-life situations
• Panicking versus OS exiting in library code
• Preemptive over-engineering and its relation to unknown unknowns
• The problem with trying to future-proof and handle known unknowns and unknowable unknowns
• Avoiding scope creep and coding for hypothetical features
• Generics and complexity in software design
• The rule of three: considering the likelihood of business plans and decisions changing over time
• Rule of threes for software development: start with simple solutions and refactor only after three iterations
• Preemptive engineering is important to anticipate future changes and improvements
• Content negotiation in protocols (e.g. HTTP) should be implemented from the beginning to allow for flexibility and backward compatibility
• Knowable unknowns are actually known factors that should be anticipated, rather than unknowable variables
• Vampires are overrated in popular culture, especially the romanticized versions
• Shiny-glittery vampires are particularly problematic
• Discussion of horror films and zombies
• Inconsistency in horror genre as a criticism
• Personal experience with ghosts and code being more frightening than supernatural entities
• Unpopular opinions segment:
  • Nobody reads commit messages in codebases
  • Commit messages are often unreliable or misleading
  • Software engineering is about software design, not just coding
  • Go language is one of the best languages for software development
• Designing software with consideration to memory and type safety
• The trade-off between design and other language features
• Unpopular opinions in the Go community (with Kris Brandow's statement "Go is great" being an attempt at a popular opinion)
• Discussion of various topics, including star signs and astrological signs
• Introduction of Johnny Boursiquot as Count Boursiquot/Johnny Golang with Sesame Street-like counting
• Imagination of spooky names for Kris Brandow (Knight of the Living Kris, Nightmare on Kris Street)