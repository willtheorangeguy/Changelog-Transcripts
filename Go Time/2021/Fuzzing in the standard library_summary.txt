• Fuzzing in Go and its role in automated testing
• Benefits of fuzzing: finding security vulnerabilities, crashes, and edge cases
• Katie Hockman explains fuzzing as a third-party objective observer of code
• Jay Conrod describes the aim of the fuzzer: to find problems that might not be expected or written about in tests
• The goal of fuzzing goes beyond contracts and documentation, aiming for resiliency in case unexpected inputs are encountered
• Fuzz testing can identify valid but untested inputs, such as nested parentheses
• Expected behavior following a failure is not always clear-cut and depends on the code and its context
• Contracts can be used to define the expected behavior of functions and guide the fuzzing process
• Panics are one way to indicate a crash, but errors or other responses can also be acceptable
• The fuzzer can act like a test by checking properties and reporting failures with t.error
• The mutator uses a combination of random and smart mutations to generate realistic-looking data
• The fuzzer has several components, including coverage guidance and corpus learning
• Compiler instrumentation is used to add counters at the basic block level to help the mutator find interesting inputs
• There are no controls for CPU and memory usage yet, but a fuzz time flag and parallel flag can be configured
• Running frequency and configuration will depend on the specific use case and may involve continuous integration with OSS-Fuzz
• Designing native support for fuzz testing in Go
• Limitations of current fuzz testing implementation (e.g. can only run one target at a time)
• Importance of feedback from users on how to improve the fuzz testing experience
• Use of compiler instrumentation to implement fuzz testing
• Comparison with other fuzzing engines, such as LibFuzzer
• Design process for native support, including decisions about using existing fuzzing engines or creating a custom engine
• Security considerations and positioning Go as a secure programming language
• Team's involvement in the project, including Jay Conrod's experience working on the go command and compiler runtime
• Design considerations for fuzz testing in Go led to resistance and iteration among developers
• Fuzz testing was influenced by existing tools like go-fuzz and incorporated feedback from a growing group of people
• The resulting API is simple and familiar, making it easier for developers to integrate fuzz testing into their test suites
• Making something simple is a complex task that requires multiple iterations and contributions from many people
• Decisions were made about what features to prioritize in the beta period and what could be added later
• Feedback is still needed during the beta period, particularly regarding issues with compatibility and design
• Discussion on generating test data for fuzz testing
• Go's design principles and how they enable familiar code for fuzzing process
• Innovative ways to use differential fuzzing capabilities
• Storing and using interesting values in a build cache for fuzzy testing
• Coordinator/worker pattern for distributing work among multiple processes
• Regression testing with stored crashes in test data directory
• Importance of having good regression tests for reducing fear and anxiety in software development
• f.fuzz function takes a testing.t and allows for fuzzing to be done within existing unit tests
• Benefits of using f.fuzz include being able to leverage existing unit tests and seed corpus entries
• The f.fuzz function is not executed by default and only runs when explicitly specified with the -fuzz flag
• Using f.fuzz does not significantly impact testing speed or add latency
• The design process for f.fuzz involved deciding on its structure and functionality, including whether to take a testing.t or testing.f
• The f.fuzz function takes an empty interface but expects a function, allowing for flexibility in the type of data it can accept.
• Discussing error handling for URL parsing and fuzz testing
• Decision-making in test code about skipping errors vs. investigating further
• Go function design and implicit type conversions
• Feedback on explicitness of type conversions and potential issues with implicit conversions
• Discussion of preserving fuzz test coverage when changing function signatures
• Planning to create a public "trophy list" for bugs found by go-fuzz users
• Importance of reporting security vulnerabilities in a controlled manner
• Discussion of the issue with pasting in software
• Importance of simplicity and explicitness in programming languages (Go)
• Value of good documentation and the role of tech writers
• Unpopular opinion: copy-pasting formatting from original source should be preserved when sharing content
• Humorously discussing the possible Twitter suspension for promoting a "bad" opinion