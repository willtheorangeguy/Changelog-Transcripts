• The hosts discuss what features they would remove from the Go programming language.
• The benefits of a smaller language include ease of learning and reading/maintaining code.
• John Calhoun shares his experience with C++ and Python, noting how languages can evolve and make it difficult to read old code.
• Daniel Marty is mentioned as joining the discussion.
• Removing friction among teammates through simplicity
• Benefits of a smaller language with fewer ways to do things
• Readability and maintainability of code
• Limitations of complex features like generics and type hierarchies
• Importance of simplicity for team collaboration and personal productivity
• Subjectivity of simplicity and readability in coding
• Potential for research or benchmarking to measure code readability
• API design principles and the idea that "less is better"
• Discussing trade-offs between language simplicity and expressiveness
• Considering adding more expressive features to Go, potentially making it less readable
• Evaluating the impact of expressiveness on code readability in different contexts (small teams vs large teams)
• Comparing readability of Go with other languages, including Ruby, based on community size and team dynamics
• Discussing the removal of the ".import" feature in Go programming language
• Daniel explains what .import does and its implications on readability
• Pros and cons of .import discussed, including potential benefits for saving key presses but drawbacks for code analysis tools
• Personal opinions on the priority of removing or keeping .import
• Discussion of .import functionality and its use cases
• Example of Go.design library using .import for DSL (Domain Specific Language)
• Explanation of why .import is not commonly used in production code
• Comparison with Ginkgo testing framework and RSpec
• Overview of underscore imports and their usage
• Criticism of magical side effects caused by certain import patterns
• Discussion on implementing import rules to prevent confusion
• The discussion revolves around the implementation and use of inits (init functions) in a programming context.
• Inits were intended for initialization tasks, but they can lead to global state and "magic" code.
• Using inits with packages requires careful consideration due to their side effects and reliance on package space state.
• A humorous example of using inits with the reflect package to implement a time.sleep function is proposed as a satirical argument for their use.
• The conversation touches on related topics, such as avoiding global state and importing packages directly instead of relying on strings or names.
• The importance of earning success through hard work and waiting
• Discussion about internal tooling at DoorDash, including Retool integration to reduce engineering time by a factor of 10x
• Elimination of manual data entry and error-prone processes after integrating Retool
• Disadvantages of one-line if statements in code, such as breaking left alignment and potential for shadowing variables
• Preference for avoiding one-line if statements and instead using alternative formatting or pulling expressions out of the if statement
• Discussion of overused language features and their potential drawbacks
• Naked returns in programming and their implications
• Confusion between naked returns and naming result parameters
• Debate on the necessity and effectiveness of using named return values
• Comparison of explicit coding vs implicit coding
• Explanation of how named return values work
• Named return variables in Go and their uses
• Removing or modifying the "naked return" feature in Go
• Potential consequences of removing named return parameters and the need for alternative solutions (e.g. lint tools)
• Discussion on labels and the "go-to" statement in Go, with a focus on avoiding spaghetti code
• Considerations for removing certain features from the language or standard library
• Difficulties in following and reasoning about code written using labels
• Use of labels to break out of nested loops
• Labels allowing breaking a particular loop (contrasted with using flags)
• Discussion of go-to statements as being somewhat reasonable but not often used
• Exploring the use of continue statements instead of labels for jumping between loops
• Personal preferences and experiences with using labels in code
• Labeling as "magic" or having a dark magic feel to it
• Discussing the possibility that some users may have legitimate reasons to use labels despite general reservations about their use
• Discussion of go-to statements and their potential replacement with other methods
• Use cases for go-to statements (e.g. code generation, breaking out of loops)
• Arguments against using labels (e.g. they're rare, can be confusing)
• Comparison of readability and the importance of context in understanding code
• Potential solution: replacing labels with a direct parent reference
• Difficulty with using else statements in Go programming
• Avoiding the need for else statements through early returns or alternative logic
• Readability and maintainability of code with minimal indentation and tabs
• Debate over whether to use tabs or spaces for indentation in code
• The issue of excessive whitespace in codebases, especially on GitHub
• Removing the ability to return an interface in Go
• Discussion on returning concrete types vs interfaces
• Potential performance optimization implications
• Plugin package in the standard library and its limitations
• Runtime loading of other Go code using plugin package
• Usage and effectiveness of the plugin package
• Discussion on limitations of Go's plugin system
• Portability and ease of use concerns for cross-platform development
• Unfinished capabilities and missed opportunities in the plugin system
• Potential reasons for lack of adoption (not good enough yet or chicken-and-egg problem)
• Comparison to other standard library packages, such as container packages (list, heap, ring)
• Generics and their potential impact on package development and standard library inclusion
• Importance of deciding which packages deserve standard library inclusion
• Concerns about the amount of resources being invested in the development of generics for Go
• Proposal to improve the compiler's support of interfaces instead of generics
• Potential consequences of focusing on generics: making some use cases obsolete
• Personal experience with using interfaces in Go and learning to work around missing features
• Evolution of thought: from initially opposing generics, to being open-minded and considering potential uses for them
• Questioning whether too much time was spent on developing generics
• Generics as a feature in the language are discussed, with the speaker acknowledging their value in certain contexts but also highlighting the trade-offs involved.
• The compiler's limitations and potential improvements, such as better inlining and performance optimizations, are mentioned.
• A humorous aside about inventing solutions to unrelated problems (e.g. hoverboards, pill for hair growth) is included.
• Daniel's opinion on language development is discussed, with the speaker agreeing that the language may need to slow down and take more time to add features.
• The importance of community feedback and taking time to consider the impact of new features is emphasized.
• A discussion about generics and their potential benefits versus the effort required to implement them is included.
• Robert and Ian's advice on considering both the benefits and drawbacks of new language features before adding them is mentioned.
• Discussion of the simplicity and minimalism of the Go programming language
• Upcoming episode featuring Kelsey Hightower on distributed systems going wrong
• Future episodes and series discussed briefly
• Promotion of subscribing to the podcast, voting on Twitter, and sponsors
• Recap of the episode's wrap-up