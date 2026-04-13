• Intro and discussion about Jerod Santo trying to impersonate Mat Ryer
• Introduction of guest Ian Lopshire and discussion about his background with Go
• Kris Brandow shares his experience learning Go and his initial confusion with the := syntax
• Jerod Santo discusses his own background and experience with various programming languages, including Perl, Ruby, JavaScript, and Elixir
• Discussion about why Jerod is interested in Go, including its simplicity and suitability for building command line applications
• General discussion about Go and other programming languages (Rust)
• Arrays vs slices: arrays are fixed-size groups of data, while slices are resizable
• Why there are two separate concepts: Go is about simplicity, arrays provide fixed-size properties, and typing in the language makes it complicated to make arrays resizable
• When to use each: use slices unless you know better or need an array's specific properties
• Quick assignment syntax: allows for flexibility in type declaration by not requiring explicit type declaration upfront
• Quick assignment vs explicit assignment and its implications on variable shadowing
• Use cases for shadowing: within loops, with goroutines, and in error handling
• Risks and pitfalls of shadowing: bugs, implicit behavior, and debugging challenges
• Modules as the preferred method for dependency management in Go
• Current state of dependency management in Go, including history and best practices
• Module initialization in Go projects
• Idiomatic Go (normative coding practices)
• Capitalization conventions in Go (e.g. ID capitalization, constant naming)
• Use of camel case vs snake case in Go
• Avoidance of globals in Go code (especially public and library-level globals)
• Skinny main functions and testing philosophy in Go
• The Go language has idioms that are nuanced and provide depth to the language.
• Some idioms in Go may not be effective for every developer or situation.
• Reading the Go Proverbs is a good way to get started with learning Go idioms.
• Go is not well-suited for building dynamic web applications like Rails, Django, or Laravel.
• The strong typing and lack of meta-programming features in Go make it less suitable for complex web development.
• Go can be a good choice for building custom solutions that require more engineering effort upfront.
• Focusing on getting started quickly vs. building maintainable software is an important consideration in choosing a language for web development.
• The benefits and drawbacks of building fast versus architecting a system for long-term use.
• Why there isn't a direct equivalent to Rails or Django in the Go community, despite its popularity.
• The idea that existing frameworks and systems can make it less necessary to build new ones.
• Discussion on the pros and cons of using Go's standard library versus external libraries or frameworks.
• A lack of certain features or tools in Go, such as better API building tools and database access methods.
• desire for data to be distributed and accessible without worrying about storage
• critique of SQL and its underlying model, leading to a desire for alternative solutions
• interest in using code generation to simplify interaction with data
• appreciation for languages with built-in features such as DSLs or functional programming facilities
• discussion on package management systems, including Rust's crates system
• mention of missing features from other languages, specifically iterators and FP functions
• debate over handling errors in Go, particularly the use of if err!= nil versus try/catch
• Discussion on handling errors in code
• Importance of adding context to error messages
• Criticism of repetitive if err!=nil {return err;} statements
• Proposal for a Go fork due to perceived shift from practical to academic focus
• Naming suggestions for a potential Go fork (e.g. NoGo, Gone, Stay, Og)
• Twitter polls and their validity
• Unpopular opinions on social media
• Voting as a way of self-expression and importance of sharing opinions
• Show wrap-up and guest thank-yous