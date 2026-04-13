• Abstractions and interfaces in Go programming
• Definition of an interface as a way to define behavior
• Structural typing vs explicit typing (duck typing)
• Implicit implementation of interfaces through methods
• Use of interfaces for decoupling packages and dependencies
• Benefits of using interfaces for dependency injection
• The benefits of using interfaces in Go, including decoupling and separating concerns.
• How Go's interface system allows for implicit satisfaction of methods, making it easier to switch between implementations.
• The advantage of not exposing unnecessary interfaces or methods, only what is necessary for others to work with a package.
• Single-method interfaces and their utility in creating function types that can be used as handlers.
• Using the "type" keyword to create new types based on existing ones, including functions, and putting methods on them.
• Method chaining and fluent APIs being challenging to use with interfaces
• Difficulty with Go's strict typing and type aliasing
• Overlapping interfaces and how they can be used, but are brittle and prone to compile errors
• Upcoming changes in Go 1.14 regarding overlapping interfaces
• Single-method interfaces and their usefulness for writing closures and handlers
• Discussion on the benefits and drawbacks of using interfaces in programming
• The concept of abstraction and how it can enable other developers to build upon existing code
• The importance of starting with simple structs rather than immediately creating interfaces
• The potential downsides of designing code around multiple implementations of an interface, such as over-engineering or causing unnecessary complexity
• Examples from the Buffalo project illustrating the challenges of balancing flexibility and simplicity in design
• Development of the Buffalo framework's new API
• Debate on whether a framework should be opinionated or pluggable
• Concerns about making all components of Buffalo too customizable and overwhelming for users
• Discussion of design process and how experience and iteration are necessary to create effective solutions
• Introduction of interface-based plugins in the new CLI project
• Explanation of how interfaces enable plugin development and customization
• Idea of using targeted interfaces to allow developers to hook into complex processes
• Contexts and cancelation
• Wrapping functions with interfaces (e.g. middleware pattern)
• Cancelable io.Copy operations
• Reader interface for controlling read behavior
• io.MultiWriter and io.TeeReader for debugging purposes
• Avoiding interference when observing code behavior (Heisenberg principle)
• Discussion of method missing in Ruby
• Comparison with Go, which has a compile-time error for undefined methods
• Rails and its use of method missing for magic behavior
• Go's error interface and its uses
• Returning specific error types vs. using the generic error interface in Go
• Sentinel errors in Go
• Discussion of sentinel errors in Go programming
• Trade-offs between using context package for error handling and making errors strongly-typed
• Use of interface embedding for errors with extra methods
• Limitations of wrapping errors with the `errors` package
• Best practices for handling errors, including explicit mechanisms for API responses and UI display
• Debate on whether to use prefixes for interface names, with some arguing it's idiomatic in other languages but not in Go
• Importance of consistency in naming conventions within an organization
• Discussion of how to handle style guides vs. idiomatic code in open-source projects
• Unpopular opinion: main package and function design promotes global scope and makes testing difficult
• Suggested improvements for CLIs, including exporting the main function and using context
• Discussion of Go programming language and its design
• Methods for organizing code in Go (functions vs packages)
• Limitations of Go's main function and scope
• Suggestions for revising Go's main function and scope in a hypothetical v2 version
• Lighthearted banter between hosts and guests