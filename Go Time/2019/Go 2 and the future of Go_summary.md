• Discussion of potential changes to the Go language in Go 2
• Removing unnecessary typing requirements (e.g. specifying types when they can be inferred)
• Generics: some panellists are opposed to their inclusion, while others see them as useful but not essential
• Shadowing issues and inconsistent behavior in the language
• Naked returns: desire for consistency and clarity in return statements
• Simplification of the select statement and potentially prioritizing channel operations
• Removal or restructuring of certain packages, including expvar, container/, rpc-related, and net/http features
• Removal of redundant language features
• Simplifying Go's syntax by reducing the number of ways to perform certain actions
• Dropping the `new` keyword
• Adding concurrent data structures and safe types to the standard library
• Providing a typed `sync.Map` implementation in the standard library
• Allowing maps to be used without initialization
• Improving error handling, particularly with regards to verbosity and bubbling up errors
• Improving error handling and stack traces
• Reducing verbosity with error specification proposals
• Distinction between temporary and permanent errors
• Community-contributed packages vs. standard library additions
• Providing visibility into error types and handling options
• Panics as a "stop the world" mechanism, and potential alternatives
• Concerns about panics and errors in Go
• Desire for more control over panic handling at package or function level
• Discussion of implicit context propagation vs explicit passing of context
• Frustration with the visibility of the context package and its usage in Go code
• Example of inconsistency in how context is used across standard library packages
• The Go standard library has inconsistent design and could benefit from formalization and consistency.
• The context package was added late and doesn't follow best practices.
• Go's current router is weak and limiting for building RESTful APIs.
• The community should provide frameworks and libraries to fill gaps in the standard library, rather than relying solely on it.
• Using third-party packages is not "doing it wrong" and is encouraged by the Go team.
• The language has limitations in dealing with unstructured data and evolving problems, making it less suitable for certain use cases.
• Discussion of dynamic vs static typing
• Use cases where Go may not be the best choice
• Potential features to steal from other languages (e.g. centralized package manager)
• Versioned binaries in modules
• Simplifying dependency management and command execution with "go exec" functionality
• Brexit mentioned in passing as a current event
• Go's popularity for building API and RPC services, CLI tools, and its suitability for cloud-based development
• Benefits of using Go for command-line tool development, including static binaries and fast startup times
• History of Go's App Engine implementation and concurrency features
• Challenges of supporting older versions of Go, including compatibility issues and difficulty in migrating users to newer versions
• Importance of the Go community's welcoming nature and newcomer-friendliness
• The Go programming language community is welcoming and inclusive.
• Diverse teams are more effective at building software that serves humans.
• The Go community's growth and focus on beginners is seen as a positive aspect.
• Respectful conversation and challenging each other's ideas is valued in the Go community.
• Personal anecdotes and humor were shared among the panelists.