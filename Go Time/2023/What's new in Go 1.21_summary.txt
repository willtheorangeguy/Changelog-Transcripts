• Go 1.21 release discussed
• Carl Johnson explains the importance of generics in the standard library
• Generics added to standard library for real-world experience before being committed to the language
• Slices package now leverages generics for convenient functionality
• New built-ins and tool improvements mentioned but not discussed in detail
• New logging capability, "slog", part of the standard library
• Discussion on how developers will adapt to using the new slog instead of other popular logging packages like logrus
• Go's log package has always been simple and basic
• Many third-party logging packages exist (e.g., logrus, zap, log15)
• A new structured logging package is being added to the standard library
• Structured logging allows for more detailed information in logs
• It provides benefits when using a centralized logging store, such as searchability and analytics capabilities
• The new package is pluggable, allowing users to format logs in various ways (e.g., JSON, logfmt)
• The maps package has seen additions, including functions for cloning and copying maps
• Discussion of iterators being added to a library or framework
• New cmp package in the standard library for comparison functions
• Generic constraints and their usage in the new cmp package (cmp.ordered)
• History of the constraints package and its removal from the Go 1.21 release
• Built-in min and max functions in the future
• Clear function to remove "not a number" (NaN) values from maps
• Clarification on type inference improvements in Go 1.21 generics
• Prevention of the "loop variable closure bug" in Go with a new flag and experiment feature
• Profile-guided optimization (PGO) going GA in Go, with improved performance through machine learning-based optimization
• Go 1.21 experiment feature for automatic loop variable declaration and how it will handle existing code
• Profile-guided optimization can improve performance by up to 10% with minimal effort
• This approach is more passive and generates insights for later refactoring and optimization
• The main challenge is gathering real-world data to build the profile optimization against
• Once set up, it's a "free money" solution that saves CPU resources in perpetuity
• Forward and backwards compatibility with the Go toolchain has been added, allowing automatic version updates
• WebAssembly support is experimental and mostly exciting for backend use cases, such as serverless functions and edge computing
• WebAssembly used for plugins in Go SQL compiler sqlc
• Protecting users from plugin code execution with sandboxing using WebAssembly
• Introducing flags.func in Go 1.21, which simplifies command line flag parsing
• Contributing to the Go project and finding "low-hanging fruit" issues to implement
• Carl Johnson's unpopular opinion: XML is better than YAML for certain use cases
• Defending XML as a markup language suitable for documents with complex formatting
• Criticizing YAML for its arbitrary interpretation of version numbers in strings
• JSON has flaws including no support for timestamps or date times
• YAML is error-prone and difficult to use due to quoting requirements and specific indentation rules
• XML is sometimes preferred over YAML due to its namespace feature, but can be confusing and not easily readable by humans
• Human readability vs machine efficiency in data formats is a trade-off
• Tools like CUE are emerging as potential replacements for YAML in configuration files
• Discussion of working with XML and YAML
• Comparison of JSON, XML, and YAML as configuration languages
• Proposal to abstract away from lower-level details in software development
• Mention of the "waterfall paper" and its proposed software development process
• Promotion of Kris Brandow's blog post on the topic