• Error handling in Go is explicit and guides the programmer to focus on error handling first
• The language encourages a "sad path" approach where errors are handled early and explicitly
• This approach can be unfamiliar or uncomfortable for developers with different backgrounds or programming styles
• New proposals aim to address potential drawbacks of this approach while preserving its benefits
• Java's checked exceptions were a reaction to C++'s unchecked exception handling
• Checked exceptions require explicit declaration in method signatures, but this leads to numerous declarations
• Go uses "throw" conceptually similar to panic, with pkg/errors package designed for wrapping and unwrapping errors
• Mainstream languages other than Java largely avoid checked exceptions
• Error wrapping is common practice, but some argue only wrap at package boundaries or when adding significant context
• Discussion on error handling in Go
• Consistency vs Inconsistency in error handling practices
• Influence of community and convention on coding styles
• Groupthink and adherence to established patterns without understanding the underlying principles
• Importance of reflexivity and questioning established practices
• Need for standardization in error handling while allowing flexibility
• Discussion around code duplication when dealing with stack traces
• Importance of well-factored code in determining error handling strategies
• Mat Ryer's approach to wrapping errors and providing context
• Dave Cheney's point about package organization and the "Package do-one-thing" mantra
• Trade-offs between verbosity and semantics in error handling
• Peter Bourgon's disagreement with treating errors as values, citing `try` function as an example
• Discussion around the `try` macro and its implications for Go code style
• Concerns about the potential for abuse and misuse of the `try` feature in code reviews
• Debate over whether the `try` feature makes code more readable or just hides complexity
• Discussion on the importance of clear error handling and cleanup in code, particularly in system code and library code
• Questions about the trade-off between allowing fluent style chaining and maintaining clarity around error handling.
• Debate over adding `try` statement to Go for error handling
• Concerns about potential misuse or overuse of `try`
• Discussion of trade-offs between explicit error handling and simplicity
• Questioning whether language features should guide users towards best practices or be optional
• Reflection on the role of Go's error handling in its adoption and popularity
• Reference to survey data showing error handling is not a major complaint among users
• The Go Survey reported error handling as a hard aspect of using Go
• Introducing `try` to improve error handling would be rejected by some, implying rejection of people who find error handling hard
• Wrapping errors in a defer statement is considered an abomination by some, but others see it as a viable solution
• A check handle approach was proposed to address issues with repetitive wrapping, but may not be possible with current performance standards
• Different styles of error handling were discussed, including the convention of not repeating error messages within one function
• The use of `try` might lead to verbosity and potentially discourage people from using error wrapping at all
• Debate on the introduction of "try" statement in Go for error handling
• Concerns about sacrificing explicitness and potential alienation of existing Go programmers
• Discussion on whether to include features that make code shorter, but may not be as clear or maintainable
• Importance of inclusion and making the language more approachable for newcomers
• Proposal to distill the language down to its core principles and use a framework for decision-making
• Error handling in Go and its relationship to code readability
• The use of prefix strings (e.g., "try") for error handling and potential drawbacks
• Concerns about visual overload and clutter from excessive error messages
• Trade-offs between glanceability, readability, and conceptual overhead
• Importance of context and historical artifacts in decision-making process