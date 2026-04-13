• Go language proposals
• Process behind a proposal
• Initial informal process of opening issues and making requests
• Formalized process for major language features such as generics and error checking
• Teleport product announcement
• Experimental implementation of language changes
• Template for proposing changes and its limitations
• Prioritization of proposals by Go team, including mix of easy and complex ones
• Difficulty in balancing personal opinions with overall impact on the language
• GitHub issues system and its limitations for searching and proposing changes
• Using Google search to filter by site and improve relevance
• Reviewing current proposals, focusing on interesting but non-controversial topics
• Proposal to auto-implement interfaces with a single method
• Discussion of Go's existing behavior for converting methods to functions
• Argument in favor: makes code more concise and consistent
• Counterargument: might lead to implicit interface implementation, potentially leading to confusion or unexpected behavior
• Issues with the "stringer" interface and accidentally implementing it
• Proposal for automatically implementing interfaces through functions
• Discussion of the benefits and drawbacks of implicit implementation
• Issue 43557 regarding function values as iterators and its implications on the language
• Comparison to other languages and concerns about adding multiple ways to do the same thing
• Implementing custom ranging in Go
• Current solutions: building own API, using iterator methods, creating slices for small data
• Using channels as an alternative, but considered a "foot gun" and has inherent overhead
• Proposed language feature for simplifying custom ranging
• Discussion of tradeoffs between explicitness and conciseness
• Concerns about readability and potential misuse with custom iterators
• Error handling in proposed API
• Iterator pattern and its benefits vs drawbacks
• Potential for abuse of iterator pattern
• Channels being considered a "foot gun" for API designers
• Concerns about ranges causing performance issues
• Discussing a proposed syntax change for type inference in Go
• Proposal to infer type from the context when using "make"
• Concerns about adding a new keyword or syntax to indicate type inference
• Debate on whether it's necessary and how it would be used
• Comparison of different approaches, including using three dots again inside make
• Composite literals becoming more powerful
• Auto-instantiating maps with built-in functions like append
• Confusion around make and new functions for instantiating data structures
• Potential changes to make and new usage for better consistency and usability
• Discussion on Go's complexity and how it can be both a strength and a weakness
• A person's typing sound is heard in the background.
• The conversation moves on to discussing a proposal called "lazy values".
• The proposal aims to solve issues with expensive calculations when logging or evaluating data, by allowing functions to be evaluated lazily and only when needed.
• Some discussion about how this could become a proper language feature.
• Concerns are raised about the potential for abuse of this feature and ensuring it's used correctly.
• Function parameters and their use
• Comparison of explicit function passing vs. implicit method calling
• Lazy values and functions proposal
• Counterproposal for making anonymous functions less verbose
• Discussion on language proposals and real code problems
• Ints and Flow64 usage in programming
• Proposal to change int type to arbitrary precision
• Current limitations with fixed-size ints (e.g. overflow and wrapping around)
• Problems caused by lack of protection against integer overflows
• Impact on code portability between 32-bit and 64-bit machines
• Proposed solution: make int infinitely sized, allowing compiler to generate good code
• Discussion about ability to go beyond int 64 with the proposal
• Discussion of large integer types (ints) and their limitations
• Proposing arbitrary precision integers in the language itself
• Implications for bit shifting, using ints as bit masks, and cross-platform code writing
• Potential benefits of guaranteed maximum size for ints
• Concerns about runtime implications, including potential slowdown due to size checking
• Modern computers are capable of handling certain tasks without issues
• Compiler optimization can prevent overflow in some cases
• CPUs can predict branch outcomes, reducing execution time
• Massively large integers or arbitrary precision floats could be useful for specific applications (e.g. financial calculations)
• Discussion of why the language doesn't have a float type
• Mention that it's a carryover from C and the reasoning behind it
• Explanation of single and double precision floats in C
• Comparison of next proposal for handling similar problem
• Introduction of Equinix Metal as sponsor, with features and promotions mentioned
• New types with strict overflow handling
• Issue 30613 discussing the addition of a new type that panics on overflow
• Stricter overflow handling compared to existing int behavior (wrapping around)
• Common problems with overflows in coding, particularly with large data sizes or unexpected inputs
• Suggestions for adding new types to handle overflows instead of manual checks and verbosity
• Adding features to handle overflow silently
• Comparison with Go language and its handling of overflows
• Concerns about potential abuse of new features
• Importance of writing safer code in certain contexts
• Proposal for separate types to handle overflows, but criticism that users must choose between them every time
• Suggestion that the default behavior should be the safe version
• Discussion about making a change to the Go programming language that could be incompatible with existing code
• Concerns about potential reliance on unspecified behavior and overflow handling in Go
• Proposal for introducing a new type to allow explicit overflowing, while defaulting to panicking overflows
• Unpopular opinions segment on the show, where a guest shares an unpopular opinion about channels being a "foot gun" in Go programming
• Discussion about a "foot gun" and its meaning
• Misinterpretation of "food gun" as a device that shoots food
• Proposal to standardize American English pronunciation to avoid such misunderstandings
• Request to open pull requests for America
• Unpopular opinion on Go language development, specifically suggesting it should be frozen again to allow stability and prevent rapid growth.
• Concerns about moving too quickly with the Go language, specifically mentioning modules as an example
• Idea of slowing down and letting other languages experiment while stabilizing the Go language
• Discussion on how this opinion might be unpopular due to potential proposal rejections or holds
• Suggestion to test this opinion through a poll on Twitter
• Discussion about the unpopularity of the V2 Plus module problem in a language
• Consequence that this issue is inherent to the semantic import versioning system
• Suggestion that the design flaw makes it impossible to fix the problem
• Reference to another project, GORM, which skirted the issue by moving old code into a separate branch
• Locking to a commit hash as a way to avoid introducing V2 in the path
• Semantics of import versioning and its necessity
• The problem of diamond dependency conflicts with semantic versioning
• Chris's point that versions 0 and 1 are special cases
• Better tooling like package site being key to addressing these issues
• Discussion on the latest table version (v3) and its implications for users
• Warning about diamond dependency issues in programming
• Concerns about the impact of upgrading from v2 to v3, especially for large codebases
• Difficulty in updating import paths and potential need for manual rewriting
• Sharing a personal anecdote about a friend's struggles with codebase upgrades
• Discussing the end of a conversation about Go language proposals
• Future plans for discussing more Go language proposals and finding "bonkers" ones
• Humorous discussion about live long and prosper from Star Trek
• Conversation wrapping up and thanking guests, including Johnny Borsico
• Discussion of upcoming podcast episode about reading the docs
• Announcements for supporting the show through Changelog++ membership
• Introduction to and farewell from the hosts and producers
• Acknowledgement of sponsors (Fastly, LaunchDarkly, Linode)
• End-of-episode goodbyes and repeated "bye" phrases