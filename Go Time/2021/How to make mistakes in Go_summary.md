• Common mistakes in Go programming
• Importance of learning from mistakes for improvement
• Interview with Teiva Harsanyi, author of "100 Go Mistakes - How to Avoid Them"
• Example of a common mistake: returning a nil receiver instead of a nil value
• Explanation of why a nil receiver is allowed in Go and how it can lead to issues
• Discussion on how to fix the issue by returning a nil value directly
• The issue of nil values vs pointers in Go and the potential for bugs when using custom error types
• Discussing how to avoid this issue, including returning explicit nil values or using slices of errors instead of custom types
• Mark Bates' opinion that returning a pointer receiver with a nil value is "too magic" and Johnny Boursiquot's agreement with this statement
• Teiva Harsanyi's explanation of the type system and how it leads to the issue, as well as his suggestion that interfaces can also be returned in Go
• The discussion of concurrency in Go and whether it's always faster than sequential solutions, with Teiva Harsanyi agreeing that people often think it is
• Goroutines in Go vs threads in Java
• Merge sort algorithm as an example for concurrency
• Thresholds for parallel execution to avoid inefficiency
• Benchmarking and profiling for determining optimal concurrency settings
• Risks of overusing concurrency and channels in applications
• Importance of weighing complexity and maintainability against performance gains
• Mistakes in Go programming and potential language changes
• Shadowing and magic "ok" variable in Go
• Use of generics in Go and its potential benefits and drawbacks
• Concerns about performance problems with generics and concurrency
• Abuse of concurrency in Go and the importance of proper usage
• The early days of concurrency in Go only had channels, with other primitives like WaitGroups and contexts being added later.
• Johnny Boursiquot discussed a personal experience where he used goroutines for concurrent API requests, but encountered issues with 429 HTTP status codes due to excessive requests.
• The conversation shifted to the importance of considering system constraints when using concurrency, such as databases, networks, and file systems being bottlenecks, not the language itself.
• Mark Bates and Mat Ryer agreed that this concept is crucial for developers to understand, especially when it comes to performance issues.
• Teiva Harsanyi discussed a potential memory leak issue with time.After(), which can create new channels on each iteration, leading to increased resource consumption.
• Context.WithTimeout creating a channel and its potential issues
• Using timer.NewTimer from the time package as an alternative solution
• Avoiding use of time.After in functions that are repeatedly called
• API footprint management: exporting vs. unexporting packages and types
• Misuse of capitalization for exporting in Go, with recommendation to default to lowercase letters
• Difficulty in understanding interfaces and explicit declarations
• Unexported types and interfaces within methods for convenience
• Advanced technique with potential drawbacks (hidden things can be hard to understand)
• Using interfaces for documentation purposes rather than strict requirements
• Introducing "Unpopular Opinions" segment on the podcast
• Discussion of Mark Bates' appearance after being stuck on a desert island
• Johnny Boursiquot's unpopular opinion: making mistakes to learn is beneficial and acceptable
• Importance of building and testing software to learn from mistakes
• Mark Bates' joking about Mat Ryer's book being a "mistake" and his own sales not doing well
• Promotion of Teiva Harsanyi's book "100 Mistakes"
• 35% discount code for listeners to buy the book with
• Giveaway of a free copy of the book
• Joking about Mark Bates giving himself a title like "The King of Mistakes"
• Reviewing a book by reading it out loud in a dry tone
• Discussing sending a copy of the book to someone (Teiva)
• Planning to write down and record content without having read the book
• Acknowledging that mistakes will likely be made in the process