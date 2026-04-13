• The process of proposing language changes for Go involves submitting an issue with a formal template that outlines the proposal's goals, implementation details, and impact.
• Proposals are reviewed by the team on a weekly basis, considering a mix of easy and complex proposals, as well as those that align with their priorities.
• The template includes questions such as "Has this been proposed before?" and "Is this backwards-compatible with existing Go programs?" to help filter out low-quality or redundant proposals.
• GitHub issues are used for proposing language changes, but searching them can be difficult due to the large number of issues (over 50,000).
• Some interesting proposal examples include automatically implementing interfaces with a single method (issue 21670) and allowing functions to auto-implement interfaces.
• Function vs method distinction in Go
• Automatic implementation of interfaces by functions
• Verbosity and explicitness trade-off
• Proposal for function values as iterators
• Iteration patterns in Go, including use of channels
• Discussion on a language feature proposal for custom ranging
• Concerns about readability and explicitness of iteration code
• Potential issues with error handling in iterator implementations
• Channels being a "footgun" (a contentious opinion)
• Ranges being simple but potentially confusing due to edge cases
• Proposal for type inference in make and new functions
• Benefits of reducing verbosity in certain situations
• Suggestions for indicating type inference, such as using three dots or a keyword
• Composite literals being made more powerful
• Making maps auto-instantiate when assigned a value
• Reducing the need for make() and new() with composite literals
• Eliminating make() and new() altogether in favor of curly braces for creation
• Lazy evaluation proposal, allowing functions to be passed as arguments that only evaluate when needed
• Discussion of proposals to improve the Go programming language
• Counter-proposal to make anonymous functions less verbose and use function parameters more often
• Proposal to change the 'int' type to be arbitrary precision
• Implications of making 'int' type arbitrary precision, including potential for slower performance due to runtime checks
• Corollary proposal to have an arbitrary precision float type in the language
• Discussion about using float64 for money and potential issues with floating point numbers
• Explanation of why Go doesn't have a separate type for floats like it does for ints/uints
• Introduction of a proposal for a new type to handle overflows, specifically an "oint" that panics when overflowing
• Debate on the merits of adding this new type and its potential impact on code safety and compatibility
• Footguns in Go: Channels as the biggest issue
• Freezing the language to slow down new feature additions
• Unpopularity of Daniel's opinion due to potential impact on proposals
• Kris Brandow's unpopular opinion that semantic import versioning is an inherent design flaw and cannot be fixed
• GORM project's approach to skirt around the issue by putting old code behind a /v2 module path
• Diamond dependency problem and its challenges
• Compatibility issues between version 1 and 2 of a module
• New tooling, such as package sites, to alleviate upgrade difficulties
• Impact on users already using version 2 with Dep or other systems
• Future plans for handling "diamond dependencies"
• Discussion of proposals for the Go language