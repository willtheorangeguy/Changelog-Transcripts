• Building maintainable software
• Distinguishing between prototyping and production-ready codebases
• Identifying the scope and purpose of a new project
• Balancing maintenance and development goals in early stages
• Considering resource constraints and finite time for maintenance
• Assessing whether a problem is solvable with software
• Striking a balance between short-term needs and long-term maintainability
• Defining maintainability and its various aspects
• Differentiating between operating and maintaining software
• The concept of "failure locality" and how it relates to maintainability
• Linters and basic documentation as a starting point for maintainable code
• Unmaintainable code characteristics, including:
  - Fundamentally untestable code
  - Heavy use of globals
  - Unclear or changing scope and intent in software design
• The importance of clear scoping in software development
• Distinguishing between testable and correct code
• Technical debt as a necessary part of evolving software
• The gradual creep towards unmaintainability due to lack of maintenance and refactoring
• The subjective nature of what makes software "maintainable" or "unmaintainable"
• The role of the business in ensuring sufficient resources for maintaining software, including time, space, and personnel
• The importance of maintaining a clean and organized codebase
• The concept of "Gardening Week" as a time allocated for codebase maintenance
• The need for structured processes for codebase maintenance, rather than relying on individual efforts
• Comparison to other industries (such as trash collection) where specialized teams are dedicated to maintenance tasks
• Debate over whether it's better to have a formalized "Gardening Team" or regular gardening weeks
• Concerns about making codebase maintenance a mandatory rotation for all engineers, rather than a specialized task
• Trade-offs between gardening/maintenance and product engineering
• Importance of maintenance engineering as a distinct discipline
• Distinguishing between "good" and "maintainable" code
• Technical debt: good vs bad debt, and understanding its implications
• Value of maintenance work in software development, and the need for awareness and responsibility among engineers
• Definition of good code vs maintainable code
• Subjectivity of maintenance and codebases
• Role of technology in maintainability (linters, formatting)
• Difficulty in pinning down and measuring maintenance
• Importance of documentation and processes for team handoff
• Comparison to simplicity and ease of use concepts
• Lack of a scientific method for evaluating maintenance
• Accumulation of minor issues ("papercuts") in codebases can lead to a negative experience
• The Go community lacks a shared set of patterns and best practices
• A "manual of style" could help establish guidelines for idiomatic Go, but will always involve some subjectivity
• Writing down and codifying community-accepted practices is necessary for improving maintainability
• Correctness criteria are subjective, including maintainability, which can be measured by the ratio of time spent researching to time spent making code correct
• Go's simplicity contributes to maintainability
• Errors as values improve glanceability and maintainability
• Panic-driven development can be problematic
• Go is analyzable and enumerable, making it easy to answer basic questions about code structure
• Generics would make Go more maintainable for some developers
• Compile-time guarantees for shared access to global immutable state are desirable
• Avoiding separate teams or feature teams in favor of generalist roles is an unpopular opinion
• Discussion on team membership and rotation, including being "on-call"
• Importance of engineers understanding all layers of the stack
• Need for exposure to different areas of software development, such as support and security engineering
• Critique of semantic versioning without clear definition of backwards compatibility
• Warning against creating complex versioning systems that are hard to manage
• Discussion of an unpopular opinion that URL paths should not include variables, especially in APIs
• Reference to Roy Fielding's views on opaque URLs and the use of query parameters instead
• Mention of poll results on Twitter regarding unpopular opinions
• Sharing of personal experiences with unpopular opinions, including alternatives to semver (Semantic Versioning)