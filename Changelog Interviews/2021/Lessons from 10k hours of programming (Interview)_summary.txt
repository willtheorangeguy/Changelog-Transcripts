• 10,000 hours to master a skill, as quoted from Malcolm Gladwell's Outliers
• Reflections on 10,000 hours of programming, including lessons learned and experiences
• The importance of practicing correctly and avoiding repeated mistakes (DRY principle)
• Math calculation of 10,000 hours (2,000 hours/year x 5 years)
• Matt Rickard's career and experiences (programming since age 15, various jobs and projects)
• Specific programming lessons learned from 10,000 hours of experience (31 points)
• Discussion of the "Heptagon of Configuration" (a pattern of configuration evolution)
• Configuration as a cycle of development, from hardcoded values to templating and domain-specific languages (DSLs), and back again
• Iteration and complexity as necessary for growth and flexibility
• The importance of learning from past experiences and codifying best practices
• The concept of bundling and unbundling in industries, and its relation to software development
• The cyclical nature of progress, where it may appear as a circle but is actually a helix of improvement
• The idea of "DRY" (Don't Repeat Yourself) as a concept that can be both beneficial and limiting, and the importance of knowing when to break the rules
• The challenge of balancing abstraction and encapsulation, and the risks of premature optimization and over-engineering
• Discussion of the meaning of "Don't Repeat Yourself" (DRY) in software development
• Clarification that DRY refers to knowledge duplication, not code duplication
• The importance of abstraction in software development and the tendency to over-generalize
• The "rule of three" for abstraction, where a piece of knowledge should be abstracted after it has been used three times
• The difference between duplication and abstraction, and the trade-offs between the two
• Comments on code commenting best practices, including the use of doc strings and in-line comments
• The importance of writing code that is self-explanatory, rather than relying on comments to explain how it works
• The distinction between commenting in library authors and application code developers
• The value of writing comments as apologies to one's future self, explaining decisions and acknowledging complexities
• Comments in code should be in-line and describe why something is done, not how it's done.
• If code looks ugly, it's likely a sign of a fundamental mistake in the design.
• Browsing the source code is often faster than searching for answers on Stack Overflow.
• Looking at the source code is especially helpful when dealing with dependencies and libraries.
• Context matters, and the advice to look at the source code may not apply in all situations, such as when using tools and APIs.
• Importance of understanding library dependencies and being willing to read their source code
• Learning from the best examples of code, such as the Go standard library
• Emulating the path to greatness by studying the work of experts in the field
• Identifying great examples of code through various means, including paying attention to the media, content, and online platforms
• The importance of using other people's code and being willing to take dependencies on battle-tested libraries
• Balancing the need for dependency management with the potential for "not-invented-here syndrome" and dependency hell
• The role of experience and skill level in determining one's approach to code reuse and dependency management
• Deciding whether to use a library or write code from scratch
• Factors to consider when choosing a library, including context, proven ground, and community support
• Risks of overusing libraries, including potential for code bloat and community changes that affect the project
• Importance of considering business decisions and context when making decisions about dependencies
• Discussion of cyclomatic complexity and its impact on code maintainability
• Discussing the importance of code deletion and simplicity
• Cyclomatic complexity and its relation to test cases
• Corollaries to the statements "Most code out there is terrible" and "Use other people's code religiously"
• The benefits of deleting unnecessary code, including improved unit test coverage and reduced maintenance time
• Emotional attachment to code and the difficulty of deleting one's own code
• Confidence in one's abilities and the role of version control in code deletion
• The importance of deleting code to see a better future and reduce noise in the codebase
• Importance of organizing code into modules, packages, and functions
• Premature code splitting and its consequences
• The art of deciding where API boundaries exist
• Risks of over-organizing code, including cyclic dependencies and fatigue
• Naming variables correctly, and the importance of variable names being descriptive enough to convey meaning
• Balance between clarity and brevity in variable names
• Conventions in variable names (e.g. err vs. error)
• The importance of following community conventions for clarity
• Dave Cheney's rule for variable names: the further away a thing is from being used, the more verbose or more information should be in the variable name
• Technology diffusion: the idea that technology does not diffuse equally across communities
• Learning from sub-communities: the importance of cross-pollination of ideas between frontend, backend, data analysis, etc.
• The importance of looking beyond specific technology camps and ecosystems to find and implement good ideas from other areas.
• Cross-pollination of ideas between different tech communities, such as Go and JavaScript.
• The example of to-do comments in codebases and the idea of self-destructing to-do's coming from the Rust community and being implemented in other languages, such as Ruby, Python, and Elixir.
• The value of paying attention to and learning from other communities, rather than sticking to a specific "camp".