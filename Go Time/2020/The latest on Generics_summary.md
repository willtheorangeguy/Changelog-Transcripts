• Discussion of generics in Go, including recent updates
• Dropping the idea of contracts and using interface types instead
• Release of a translation tool and type checker for testing generics
• Feedback on syntax and semantics, with most feedback being about syntax
• Partnership with type theory experts to inform the design proposal, specifically the Featherweight Go paper
• Purpose of the Featherweight Go paper is to prove that the proposed generic features are sound and can be translated into regular Go programs
• Ad-hoc design in Featherweight Go was driven more by intuition than mathematical background.
• Ian Lance Taylor mentions that he was not involved in understanding the paper and had a hard time with it.
• The importance of parsing without type-checking is discussed, using an example to illustrate how angle brackets cannot work in Go due to ambiguity issues.
• Square brackets vs. parentheses are considered for specifying generic types, with some advantages and disadvantages to each option.
• Trade-offs between the two syntax options include clarity, conciseness, and potential ambiguities.
• Parsing ambiguities with square brackets vs parentheses
• Feedback from the Go community on generics proposal
• IDEs and syntax highlighting tool feedback (e.g. JetBrains)
• Precise semantics for generics still being worked out
• Timeline for moving from draft to formal proposal is uncertain
• Types of feedback sought: things that don't work, expected vs unexpected behavior
• Avoiding complexity-adding features like Turing-complete languages within generics
• Avoiding complexity in Go by comparing and contrasting with C++ and Java
• Concerns about the potential for overuse and abuse of generics, leading to unnecessary complexity
• Need for community-led development of best practices and idioms for using generics effectively
• Plans for adding new standard library packages that take advantage of generics, rather than modifying existing ones
• Discussion on managing the surge of feature requests for the standard library
• Importance of measuring build speed changes over time during the experimental phase
• Discussion of adding new checks to discourage generic code usage
• Effectiveness of generics on Go's appeal to programmers from other languages (Java, C++, .NET)
• Balancing traditional Go practices with added functionality of generics
• Importance of idiomatic ways and community-driven approaches to handling generics
• Unpopular opinions on various topics, including identifiers length and transportation efficiency
• Concerns about variable naming conventions in coding
• The importance of considering the potential drawbacks of language changes when proposing modifications to a programming language
• The challenges and social process involved in evolving a programming language, including the need for an educational process and getting everyone on board with incremental changes
• Historical examples of widely accepted language features that were once contentious, such as garbage collection