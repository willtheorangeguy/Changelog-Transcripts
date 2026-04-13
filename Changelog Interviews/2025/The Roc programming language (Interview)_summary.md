• Richard Feldman discusses the lineage of Roc, a programming language, and its connection to Elm, which he previously championed.
• Roc aims to be a more versatile language than Elm, suitable for a wide range of domains and applications, not just frontend web development.
• Elm is praised for its compiler design, error messages, and ergonomic approach, which have been influential in the development of Roc.
• The conversation touches on the "Velvet Underground phenomenon," where Elm's influence can be seen in other languages and projects, even if it remains a niche language.
• Roc is intended to be a successful language in industry, not just a hobby or niche project, with Feldman's goal being to use it in production and make it widely adopted.
• Measuring success in Roc development by user adoption and feedback
• Current production use of Roc, but with a focus on robustness and stability
• Plans to release the first numbered version (0.1.0) with a rewritten compiler in 2026
• Prioritizing usability and feature completeness for Advent of Code 2025
• Design decisions and intentional "no" to certain features (e.g. maybe types, optional types, self-hosting)
• Evolution of Roc's design and syntax, influenced by Elm but distinct
• Current syntax more similar to mainstream languages like TypeScript
• Syntax changes in Roc and how they differ from Elm
• Syntax transition being a polarizing issue for some users
• Semantic changes in Roc, including static dispatch
• How static dispatch works in Roc, and how it differs from JavaScript's prototypal inheritance
• Explanation of 100% type inference and its benefits
• Custom equality in Roc and how it is implemented through a function named "equals"
• Roc's design allows for custom equality and operator overloading without requiring formal declarations or trait hierarchies.
• The language's simplicity and lack of special syntax make it easy to understand and use.
• Roc's compiler performance is a top priority, and self-hosting is not considered necessary or desirable.
• The language has a strong focus on safety features, including automatic memory management and trust in third-party code.
• Roc is not considered a "general-purpose" programming language, but rather one that excels in certain areas.
• Roc's goal is to make scripting safe and secure
• Roc can prevent script-based attacks by allowing the user to swap out the platform with a sandboxed alternative
• Platforms in Roc are a concept that formalizes the idea of building on top of existing frameworks or libraries
• Each platform provides a domain-specific API and IO primitives tailored to its use case
• SafeScript is a sandboxed platform that can be swapped in to prevent script-based attacks
• Platforms can be thought of as an interface or API that application authors consume
• Platforms are composed of a public API and a lower-level implementation that provides IO primitives and other services.
• Roc code is a platform-agnostic language that allows developers to write code that can run on various platforms, including iOS, JVM, and others
• Roc code can be embedded into existing codebases, making it easy to integrate into existing projects
• Roc has a strong focus on runtime performance, aiming to be faster than Go but not as fast as Rust or C++
• Roc uses unboxed data structures and automatic reference counting for memory management, similar to Rust and C++
• Roc's compiler optimizations are provided by LLVM, which is also used by Rust and C++
• Roc has a unique feature called "opportunistic mutation" that allows for efficient updates to immutable data structures
• Opportunistic mutation as a performance optimization in Roc
• Reference counting vs. traditional garbage collection
• Reliability of reference counting in Roc compared to manual reference counting in Objective-C
• Benefits of reference counting for incremental memory management and avoiding GC pauses
• Comparison of Roc's performance and semantics to Go and other languages
• Error handling and null/undefined values in programming languages
• The benefits and design of Roc's Result type for handling optional values
• Centralizing error handling around the Result type
• The concept of algebraic data types (ADTs) and their benefits
• Anonymous ADTs in Roc, allowing on-the-fly construction of ADT instances
• How anonymous ADTs can be used to improve error handling and data modeling
• The ergonomic benefits of Roc's anonymous ADTs compared to other languages
• Roc's handling of errors, which involves automatically tracking and unioning possible errors in a function call
• Explicit error propagation using the question mark operator
• Purity inference, which uses the exclamation mark operator to indicate effectful functions and enforces that only effectful functions can call other effectful functions
• Compiler-enforced rules for effectful functions, including the use of an exclamation point at the end of their name and only being able to call other effectful functions
• Using purity for benefits in the compiler, such as evaluating constants at compile time and eliminating the need for initialization
• Properties of pure functions, including the ability to cache results and run concurrently without issues
• Operator overloading and the restriction on mixing pure and effectful functions in the same function
• Compiler warnings vs hard errors for IO in pure functions
• "Inform but don't block" design philosophy for non-blocking compilation problems
• Warning system for preventing compile errors from blocking workflows
• Separation of compile-time and runtime errors for preserving developer flexibility
• Deployment story for Roc, including cross compilation, dynamically-linked libraries, and WebAssembly
• Current limitations of the Roc compiler, including lack of static dispatch and Lambda set specialization bugs
• Anticipated benefits of a future rewritten compiler, including better performance and fewer bugs.
• Language design philosophy prioritizes simplicity and a small set of primitives
• Presence of for loops is a topic of debate in functional programming circles
• Roc has a concept of first class effects, but lacks a first class concept of mutation
• Implications of lacking a first class concept of mutation include ergonomic issues and potential for bugs
• Roc intentionally lacks an arbitrary C FFI, and platform-specific integrations are preferred
• Library story and working with other people's code is a key aspect of the language
• Roc's dependency management system is designed for simplicity and security, with a focus on caching and immutable dependencies
• roc run command downloads dependencies to the home directory
• design for caching in the home directory, not local directory
• version ranges based on Go's minimum version selection
• compiler selects lowest minor version that satisfies all constraints
• major version changes require API compatibility and are enforced in Elm, but may not be enforced in Roc
• Roc code generation with LLMs, including a built-in primer for the language
• challenges of training LLMs with a small and potentially unrepresentative dataset
• comparison to historical concerns about new programming languages lacking established ecosystems
• Challenges of introducing a new programming language
• The impact of large language models (LLMs) on language adoption and user experience
• Ease of getting started with a new language due to LLMs
• The role of LLMs in porting libraries and ecosystems to new languages
• Potential for new languages to break out and gain traction
• Recommended use cases for the Roc programming language
• Community resources for the Roc language (Zulip chat)
• Roc language discussion and its features
• Pros and cons of trying out Roc before its 0.1.0 release
• Opportunities for contributing to Roc's development
• Zulip channel for Roc beginners and introductions
• Richard Feldman's podcast, Software Unscripted, and its online presence
• Strange Loop conference and potential successor events