• Fuzzing explained: a form of automated testing that manipulates inputs to find bugs
• What sets fuzzing apart from unit testing: it's not just random input manipulation, but also uses intelligence to prioritize and mutate inputs
• Situations where fuzzing is helpful: parsers, decoders, code with unknown or unexpected input structures
• Fuzzing vs. unit testing: fuzzing tests for properties of output, rather than specific outputs
• Examples of fuzz test targets: checking that separator never appears in returned slices, returned slices are less than original string length
• Benefits of fuzzing: finding bugs and panics that wouldn't be found through manual testing
• Design of fuzz tests requires thinking about specific properties and edge cases
• Fuzzing can test for properties such as crashing, differential testing, and property testing
• Differential testing has found many bugs by comparing the output of different implementations
• Go-fuzz is a common tool for fuzzing in Go, but it requires a separate build step and corpus management
• Other tools like fzgo aim to simplify the process and integrate with the Go command
• Fuzzers often use coverage information to guide their mutations and find interesting paths in code
• Fuzz testing has advanced to dynamically influencing code execution based on insights into the code
• Adversarial training-like concept where two models compete to improve each other's performance
• Reversing-engineering capabilities, allowing fuzzers to figure out correct input for if statements
• Trade-offs between randomization and prioritization of certain inputs in fuzz testing
• Developer must decide how much fuzz testing to use, depending on goals and feedback loop needed
• Origins in security world, but proposal aims to make fuzz testing more accessible to developers
• Fuzz test targets are designed to be close to regular unit tests for low friction adoption
• Seeding the corpus is used to give fuzzing tool a head start, similar to unit testing
• Seed corpus can serve as regression test and can be updated with new crashes and interesting findings
• Corpus management practices are still an open question, including where to store it and how to share it amongst team members
• Fuzz testing limitations and best practices
• Proposal for new fuzz testing features in Go
• Discussion on continuous integration and ClusterFuzz
• Overview of OSS Fuzz project by Google
• Design and API details of the proposed fuzz testing functions in Go
• f.fuzz function structure and purpose
• Design goals: simplicity, integration with existing Go testing tools
• Interaction between f.add (corpus seeding) and f.fuzz functions
• Impact of Go generics on the design
• Fuzz target writing: current limitations and potential improvements
• Assertions in fuzzing: beyond just "doesn't panic"
• Example use cases: differential fuzzing, cache implementation testing
• Fuzzing can be used to test serializers and ensure they work correctly with reused buffers.
• Fuzzers can find unexpected edge cases that unit tests may miss.
• The goal of fuzzing is not just to provide random input, but to find realistic variations in input that could break the system.
• A fuzzer's lack of understanding of the code's intentions is actually a strength, as it allows for the discovery of new edge cases.
• Fuzzing can be seen as a form of "meta-testing" or abstract testing, where the focus is on defining expected behaviors rather than specific inputs and outputs.
• Unit tests are still necessary, but fuzzing provides additional value by asserting actual properties and behaviors.
• There's no inherent risk in allowing fuzzers to potentially discover new edge cases that could break the system.
• The importance of social skills in the tech industry
• Katie's entry into computer science due to its potential for building with others, not just solving math problems
• The high level of social interaction required in InfoSec and API design
• Filippo's unpopular opinion that dogs should be banned from the office
• Roberto's confession that he likes the color yellow, which is met with skepticism by his fellow panelists
• Discussion of a tweeted picture
• Mat Ryer's fear of gophers
• The difficulty in recording audio while using a webcam with a gopher nearby
• Conclusion and wrap-up of the podcast episode