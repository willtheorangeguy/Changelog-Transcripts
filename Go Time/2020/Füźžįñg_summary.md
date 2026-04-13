• Fuzzy Wuzzy was a bear and the topic of fuzzing
• Introduction to Changelog, its sponsors (Fastly, Rollbar, Linode), and Digital Ocean
• Discussion on fuzzing: what it is, how it works, and its benefits
• Guest appearance by Katie Hockman, author of a draft design for bringing fuzzing as a first-class concern to Go
• Introduction and discussion with Filippo Valsorda and Roberto Clapis
• Testing and unit test discussions
• Lack of industry standard for mutation techniques in fuzzing
• Discussion on corpus entries prioritization and modification methods
• Different fuzzers working differently, which can be beneficial
• Potential applications of fuzzing in non-security contexts
• Fuzzing vs. unit testing: fuzzing finds unexpected input or edge cases
• Benefits of fuzzing in identifying bugs and dependencies not caught by unit tests
• The limitations of string splitting and joining in the strings package
• The importance of testing for edge cases such as nil slices or empty strings
• The concept of differential testing and its uses, including identifying bugs in code
• An example of using a fuzzer to find a bug in the Go standard library that had been present for 12 years
• The effectiveness of fuzzing in finding problems, including a case where it found a bug before it was released
• The options available for fuzzing in Go, including GoFuzz and FuzzGo
• GoFuzz vs FuzzGo: comparison of features and purpose
• Build steps required for fuzzing with GoFuzz
• Limitations of GoFuzz, including need to learn new workflow and source-to-source transformation
• Importance of coverage in fuzzing, including AFL's use of coverage to guide mutations
• Example of using GoFuzz to discover vulnerabilities in the HTTP library
• Discussion of fuzzing as a form of "adversarial training" for code.
• Fuzzing tools compete with each other to improve results
• Reverse engineering code can allow fuzzing engine to tell what input is needed for certain statements to pass
• Seeding the corpus provides a head start for the fuzzing tool and allows it to build on existing knowledge
• Seed corpus serves as both a starting point for mutation and a regression test, checking for previously fixed bugs
• Best practices for corpus management
• Whether to store the corpus in Git or another repository
• Sharing the corpus amongst team members
• Running the fuzzer on a local machine versus using continuous integration
• Programmatic vs manual corpus generation
• Corpus size and maturity of the technique as factors in best practices
• Continuous fuzzing as a workflow
• Discussion of fuzzing and continuous integration in software development
• Introduction to OSS Fuzz, a project by Google for open-source projects
• Retool as a solution for building internal tools more efficiently
• DoorDash's experience with integrating Retool and its benefits
• New proposal for Go fuzz functions, including design and implementation details
• Implementing testing.f interface based on testing.tb interface
• Discussion of strong types and interaction with fuzzing engine
• Comparison to unit tests and running functions
• Parameters and structure of inputs in the corpus
• Definition and generation of corpus entries by f.add function
• Potential impact of Go generics on the design
• Discussion about the f.add function and its role in seeding the corpus
• Explanation of how f.fuzz runs a function with similar argument types as f.add
• Comparison of proposed design to existing Go code and testing conventions
• Goal of making fuzzing easy to understand and use, similar to writing unit tests
• Examples of current fuzz targets being overly simplistic or lacking properties to check
• Importance of fuzzing beyond just finding panics and introducing invariants and checks
• Discussion on the future of built-in fuzzing in Go
• Discussion on assertions and testing in the context of encoding and decoding
• Fuzz testing a cache implementation with a hash map as a reference point
• Testing serializers with fuzzing to check output consistency and performance implications
• Importance of defining expected behaviors in testing and using fuzzer targets for meta-testing
• The importance of testing actual properties rather than just providing examples
• Writing property assertions for fuzz targets is more effective in tests
• Unit tests are necessary but can be limited in identifying edge cases
• Fuzzing is useful for finding where code breaks and can identify edge cases that developers may not consider
• Writing test targets allows for future interaction with the code and ensures consistency during refactoring
• A fuzzing engine acts as an objective, third-party entity that can identify bugs without being biased by developer assumptions
• Discussion about a simulation being revealed
• Emergent intelligence in machines and chaos theory
• Fuzz testing and machine learning algorithms
• Importance of variations in input for realistic results
• Comparison between human design and algorithmic fuzzing
• Risks and benefits of using algorithmic fuzzing to test code
• Promotion of Pixie, a debugging tool for Kubernetes
• Pixie is an API that lives inside a platform, harvests data, and exposes interfaces for getting needed information
• Pixie is like a decentralized Splunk and provides edge intelligence without code changes
• The team behind Pixie aims to bring it to market by the end of 2020
• Links to the beta are in the show notes
• Computer science can be more enjoyable with social skills, which may be undervalued in tech
• The InfoSec community is a good example of excellent community support and social interaction
• Importance of social skills in security
• Kindness and professionalism of the Go security community
• Criticism of traditional security communities' attitudes
• Designing APIs for human understanding, not just machine interaction
• Common misconceptions about API design and user abilities
• Lighthearted discussion about Pythagoras and humor in math
• Photography and popular opinions vs. actually-held opinions
• Dogs in the office are causing problems
• Filippo is allergic to dogs and doesn't want them brought to work
• Other people are scared of dogs too
• Service dogs are allowed as an exception
• Management allowing dogs in the office shows they're cool, but causes conflicts and discomfort for others
• A colleague jokes about banning foosball tables next
• Discussion of dogs in the office
• Roberto's unpopular opinion about liking the color yellow
• Rob's skepticism and joke about Roberto's taste in colors
• Introduction of a podcast within the podcast, featuring a yellow gopher
• Joke about getting the gopher closer to the webcam until Matt screams
• Wrap-up and farewell to guests
• Clips and highlights from past episodes
• Polls about unpopular opinions
• Host: Matt Reier with special guests Katie Hockman, Roberto Clapis, and Filippo Valsorda
• Producer: Jared Santo
• Music provided by Beat Freak Breakmaster Cylinder
• Episode sponsors: Digital Ocean, Retool, Pixie, Fastly, Linode, Rollbar