• go.work files and their similarity in syntax to go.mod
• use directive in go.work files for specifying directories and modules
• Change Log Weekly newsletter
• Go 118 features, specifically fuzzing and generics (mentioned but not discussed)
• GoFumped tool for stricter code formatting and Daniel's contributions to Go
• Discussion about Michael Matlub's role on the GoTools team at Google
• Introduction of Michael to the podcast
• Reference to "big subjects" not being discussed
• Mention of generics and fuzzing, and their lengthy development time
• List of topics to be covered, including:
  • strings.cut function in Go
  • Why strings.cut is a useful feature despite initial skepticism
• Discussion of implementing NetIP as a replacement for net.ip in Go
• Comparison of old and new IP address data types in Go
• Advantages of NetIP, including performance improvements and ability to compare without allocation
• Backwards compatibility concerns with NetIP implementation
• Possibility of helpers to switch between old and new IP address types
• Discussion of releasing new implementations alongside existing ones for backwards compatibility
• Support for various VCS systems, including Git
• Build info with dependencies
• Automated detection of vulnerabilities in dependencies
• New build info API to access version information inside the binary
• VCS stamping for build info
• Improved module version resolution in Go 118
• Discussion about the version number 118 and its interpretation as Semver
• Explanation of GoFump tool behavior with and without spaces, including differences in functionality
• Clarification that both tools now use the same parallelization method
• Description of how GoFump formats files and directories in parallel, but initially had issues with tiny files consuming CPU overhead
• Discussion of optimizing chunking groups of files for efficient parallel processing
• Discussion of coding habits and best practices
• Benefits of code formatting tools
• Use of intentional mistakes for testing purposes
• Red-green testing in TDD (Test-Driven Development)
• Suspicions about code that works first time without errors
• Introduction to the Pacer redesign in the garbage collector
• General discussion of the importance of timing and edge cases in software development
• Discussion about low-level system improvements and their interest to programmers
• Ryan mentioning a "pacer" he didn't know about before, and being glad that such work is done for free by others
• Michael mentioning the importance of runtime improvements and appreciating the team's work
• Conversation about the number of Michaels on the Go team and whether all have been accounted for
• Discussion about reading about a specific issue (44167) with a link to the full proposal design
• Talk about community contributions, including those from outside the Go team or popular contributors
• Introduction to Ship It podcast and its weekly episodes about getting ideas into the world
• Discussion of Apple's M1 chip and its compatibility with Go programming language
• Support for ARM64 architecture in Go
• Implementation details of supporting the M1 chip, including adding glue code and signing binaries
• Work done by the Go release team to make releases smooth despite changes in macOS
• Improvements in newer x86-64 machines and introduction of new environment variables (e.g. GOAMD64) to target specific versions
• Explanation of how targeting a specific architecture can lead to performance improvements
• CPU cost considerations for running different code
• Optimizations and improvements in Go runtime garbage collector
• New features in Go templates, including break and continue statements and short-circuiting Boolean operators
• Overview of Go workspaces, a feature coming in Go 1.18, which solves the problem of managing multiple modules at once
• The concept of workspaces in Go allows for multiple main modules
• Workspaces enable working across multiple modules at once
• This feature addresses a common complaint from the Go user survey about working with multiple modules being cumbersome
• Initially, people were overusing modules due to learning and experimentation with new features
• Now, it's recommended to have one module per repository unless specific use cases require otherwise
• Workspaces are enabled through the creation of a Go.work file with similar syntax to Go.mod files
• Adding support for workspaces and modules required significant changes to the Go command
• Complexity in module loading code was a challenge, but once resolved, most tools benefited from it
• Tools that call into the Go command get workspace features automatically with a .work file present
• VS Code and other teams made changes to understand and pass in .work files for this feature
• An experiment allowed people to try out the new feature using an environment variable or a development version
• Code generation is not well-integrated with Go, leading to issues like stale files.
• Generics will likely reduce the need for code generation in many cases.
• Reflection is difficult to write because of lack of feedback mechanisms.
• The TriProposal, which aimed to improve error handling, was unpopular but potentially impactful.
• Bringing back the TriProposal and revising it could lead to better error handling practices.
• Discussion about wrapping error messages in Go
• Importance of explicit error handling in Go
• Potential for Go to become too familiar and resistant to change
• The value of rigorous process in adding new features and maintaining backwards compatibility
• Criticism of Go for ignoring programming language development in the past 15 years, but considering its stability as a reason for its success
• The challenges of contributing to a project with JavaScript due to its complex features and the resources required for a new interpreter engine.
• The difficulties of creating a new JavaScript engine without the resources of a huge multinational corporation.
• Discussion of recent Go topics, including Generics and fuzzing in Go 1.18.
• Call to action for listeners to participate in discussions and share the show with others.
• Thanks to sponsors Fastly and Brakemaster Cylinder, and appreciation for listeners.