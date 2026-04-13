• App structure importance
• Maintainability through good structure
• Expectations for organizational structure based on project type
• Go's unique constraints, such as package grouping and nested folders
• Best practices for structuring code, including starting with a flat structure and refactoring later
• Emergence of structure from work done, rather than trying to plan it upfront
• Designing main package structure
• Refactoring Go code for maintainability
• Importance of consistency in code organization
• Contextualizing design decisions based on project size and team complexity
• File naming conventions in Go (e.g. main.go, foo.go)
• Handling responsibility-based packaging vs. modular design
• Using existing patterns and conventions in legacy codebases
• Importance of organizing code by domain vs. following a predefined framework or convention
• Difficulty in explaining concepts such as dependency injection and separating concerns to developers new to Go
• Trade-off between being productive quickly and doing things the "perfect" way from the start
• Value of refactoring and making time for it, especially in long-term projects
• Need for managers and teams to understand and support the importance of refactoring
• Refactoring is not just about fixing code, but also a learning exercise
• Experience plays a significant role in developing good coding habits and structures
• Junior developers may struggle with the concept of refactoring, but it's an essential part of the development process
• Joining a team with experienced developers or contributing to open source projects can be helpful for new developers
• There is no one "best practice" for package design or layout in Go, and it's better to write code and refactor as you go rather than trying to follow specific rules
• Trade-offs between monorepos and microservices
• Benefits of monorepos for code management and deployment
• Challenges of implementing and maintaining large monorepos
• Importance of tooling and team structure for successful monorepo use
• Discussion on file size limits and structuring Go projects
• The importance of visual intuition and making decisions based on navigating a project's folder structure
• Idiomatic Go practices and expectations for organizing code
• Reasoning about code organization and how different people may organize projects in unique ways
• Breaking up packages and when to refactor them, using nesting and sub-packages
• Using internal packages to hide dependencies and prevent cyclical imports
• Challenges with testing and black-box testing when using internal packages
• Naming conventions for sub-packages and the trade-off between repetition and clarity
• Cyclical dependencies and imports
• Design issues and refactoring
• The importance of "moist code" (repeating common concepts) vs. trying to dry up code with abstractions
• The "three strikes rule" for repeated code: refactor after seeing it three times
• Cyclical import problems often stem from over-separation of concerns or trying to map database relations directly to code structure
• Importance of context and project requirements in structuring code, rather than relying on rigid patterns or rules
• Discussion on approaches tried in software development that did not work well
• Mistakes made in package organization, such as having too many nested packages and unnecessary dependencies
• The importance of simplicity in coding and avoiding over-engineering, especially with Go
• The concept of "do the minimum" and deferring decisions to a later time when more information is available
• Wrap-up of the 1-hour session
• Promotion of Go Time Slack channel
• Recommendation to read Ben Johnson's article on structuring Go applications
• Encouragement to ask questions and participate