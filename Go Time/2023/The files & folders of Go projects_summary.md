• File and folder organization in Go projects
• The concept of files and folders on a computer (inodes, metadata, etc.)
• SQLite implementation using a single file
• Differences between file systems (e.g., Mac vs Windows)
• How Go's standard library abstracts away file system differences
• Inode explanation and its relation to file systems
• Files and folders as an abstraction
• Meaning of file extensions in Go (.go, _test.go)
• Using the _operatingsystem or _architecture suffix in file names for specific platform compilation
• Folders as packages in Go
• _test package exception for separating test code
• Internal folder for sharing code within a package but not with the entire codebase
• Discussion on the use of internal packages in Go and potential drawbacks
• Pros and cons of using internal packages for utility functions and organization
• Flexibility of package structure in Go and how it allows for different design approaches
• Circular dependencies as a constraint that enforces good design practices
• Strategies for dealing with circular dependencies, including splitting off third packages
• Designing a package structure with loose dependencies between modules
• Merging packages instead of dealing with circular dependencies
• Starting with a single package and breaking it out as needed
• Managing large files vs splitting code into multiple files
• Understanding file size limits on older machines (e.g. 4GB)
• Using the internal folder for specific types or utilities
• Purpose of cmd and pkg folders in Go projects
• Debate about the usefulness of a separate "pkg" folder in Go projects
• Discussion on why importing main packages can be confusing and lead to thin main packages
• Pros and cons of keeping the main package small and testing it separately from the binary
• Introduction of the "golang-standards/project-layout" repository and its potential for causing confusion due to its name suggesting official endorsement
• Mention of vendor folders and their use cases, including building projects on third-party services
• Discussion of the usefulness of vendor directories in open-source projects
• Potential drawbacks to having a single large package or module (e.g. net package)
• Signs that a project's structure may be problematic (e.g. frequent code changes, large blast radius)
• Importance of cohesion and locality in software design
• Use of tools like gofix for automating code migrations
• Criteria for determining if a package structure is "wrong" (i.e. justification and personal preference)
• Unpopular opinions on Go programming
• Misuse of popular Go features (channels and goroutines)
• Performance optimization in the wrong areas
• Importance of understanding past teachings and best practices (e.g. Martin Fowler's "Patterns of enterprise architecture")
• Criticism of the Go community's tendency to reject established knowledge as "over-engineering" or "Java-thinking"
• Value of benchmarking before adding concurrency or other optimizations
• Criticisms of blindly applying patterns from "Patterns of Enterprise Architecture" in Go development
• Importance of understanding context and nomenclature specific to a programming language
• Value of avoiding dogmatic application of outdated concepts
• Discussion of XML being unfairly maligned, despite its technical merits
• Relational databases not living up to Ted Codd's original vision
• Trade-off between using high-level abstractions vs. understanding underlying mechanics
• The discussion of the relational model and its implementation in SQL databases
• Codd's theoretical approach to database design vs practical performance issues
• History of SQL, including its original spelling as "Sequel" and the trademark issue that led to it being renamed
• Kris Brandow's interest in exploring deeper topics on his show, Go Time