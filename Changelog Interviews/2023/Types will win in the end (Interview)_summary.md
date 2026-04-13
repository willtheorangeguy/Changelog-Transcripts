• Origins of Sorbet and its development at Stripe
• Type checking in Ruby and its adoption by large organizations
• Challenges of convincing developers to adopt type checking in Ruby
• Influence of TypeScript and other type systems on the development of Sorbet
• Importance of type checking in large, complex codebases
• Comparison of Sorbet to other type systems, such as RBS
• Transition from prototyping to long-term development with type checking
• Impact of changing programming languages and environments on developers
• Jake's interest in types and programming languages started in university, but he didn't realize he wanted to work with them until later
• He joined Stripe's type team and was mentored by experienced developers, allowing him to dive into the work immediately
• The team worked on various projects, including an ahead-of-time compiler for Ruby, which was ultimately not pursued due to latency concerns
• Sorbet is now used in over 99% of Stripe's production Ruby files, with the majority of files using the "typed true" or higher checking levels
• The use of Sorbet has significantly improved developer productivity, particularly with features like accurate jump to definition and code exploration
• The team has seen a network effect, where developers self-select to use Sorbet's stricter checking levels due to its benefits in understanding and refactoring code
• Challenges of large codebases with dynamic languages like Ruby
• Difficulty of static analysis due to Ruby's metaprogramming features
• Sorbet's approach to type checking in Ruby, including opt-in type checking and escape hatches for metaprogramming
• Balance between type checking and metaprogramming in Ruby
• Use of linters in combination with type checkers like Sorbet
• Method missing in Ruby and its implications for type checking
• Discussion of first-party Ruby official types and their potential relationship to Sorbet
• Sorbet is a type checker for Ruby that was initially seen as one more type checker, but eventually gained backing from companies like Stripe and Shopify, leading to consideration by the Ruby Core team.
• The Ruby Core team decided to implement type annotations without changing the Ruby syntax, and created RBS (Ruby Signature) files, which have a different syntax than Sorbet annotations.
• RBS files are already shipped with Ruby 3.0, and can be used with a type checker like Steep, but Sorbet does not currently parse them.
• Sorbet's developers are prioritizing other features over parsing RBS files, but may do so in the future.
• The Ruby Core team's implementation of type annotations is seen as a first step towards integrating types into the language, but the process may take time.
• Discussion of Sorbet's name and branding
• Comparison of Sorbet to TypeScript
• Explanation of gradual type checking in Sorbet
• Discussion of control flow-sensitive typing in Sorbet
• Example use case of control flow-sensitive typing in Sorbet
• Comparison of Sorbet's adoption and type definition support to TypeScript's
• Discussion of challenges in adding type support to existing Ruby libraries
• Making the Sorbet development process easier for application developers and library developers
• Using third-party gems to analyze and generate type annotations for gems like Active Record
• Challenges and limitations of this approach, including complexity and performance issues
• RBI (Ruby Interface) files vs. RBS (Ruby Standard) files, including syntax and functionality differences
• Sorbet's performance and optimizations, including incremental type-checking and avoiding unnecessary work
• Stripe's codebase size is estimated at 15 million lines, making it larger than Shopify's
• Comparing codebases by lines of code may not be accurate, bytes would be a better metric
• Sorbet can be adopted incrementally, starting with static type checking and runtime library installation
• Editor support for Sorbet is available through VS Code extension and language server protocol
• Tracking adoption is important, especially for larger companies, to give stakeholders visibility into progress
• TypeScript is compared to Sorbet, with the idea being to make it easier for developers familiar with TypeScript to understand Sorbet's type system
• Types will win in the end, according to Jake Zimmerman, as they provide a strong vocabulary for structuring thoughts and are essential for large codebases
• Jake Zimmerman's background in type systems is discussed, including his experience with Standard ML and its influence on other languages like Rust
• Sorbet's name is discussed, with Jake Zimmerman mentioning that he is not a fan of Sorbet, but likes the ice cream equivalent
• The challenges of searching for information about Sorbet due to its name being overloaded with non-programming results are mentioned
• The importance of a good domain name is discussed, with Jake Zimmerman mentioning that he was able to secure the Sorbet.org domain for a Stripe project
• Conclusion of the conversation
• Acknowledgment of the guest's participation