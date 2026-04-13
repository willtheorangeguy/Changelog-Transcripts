• Strings.cut function for cutting strings in two
• New IP address representation in Go (net.ip) developed by Tailscale
• Comparison and performance advantages of net.ip over byte slices
• Module workspaces (Michael Matloob's work on the Go Tools team)
• Discussion about other features in Go 1.18 aside from fuzzing and generics
• Backwards compatibility with API changes
• New data type for improved performance
• Helpers to switch between old and new types
• vcs build stamping to track version control system information
• buildinfo function to report dependencies and module versions
• Support for multiple version control systems (Git, Mercurial, Bazaar, Subversion, Fossil)
• Automatic inclusion of version control system metadata in binaries
• The pronunciation of "1.18" and whether it is a decimal number
• Changes to the `go fmt` tool, including its ability to format files in parallel and how it now works similarly to the tool with no space
• Speed improvements when formatting large repositories
• Formatting code and how some developers use editors to format files as they save them
• Using formatting tools as a feedback loop for writing correct syntax and avoiding errors
• The pacer redesign in the garbage collector, which is an area of interest but not an area of expertise for the speakers
• The garbage collector (GC) pacer in Go is being redesigned to improve its performance in edge cases.
• The original GC pacer was designed long ago and has accumulated quirks over time.
• A redesign is underway to address these issues and improve the GC pacer's performance.
• The issue number for more information on the redesign is #44167.
• Go already had support for the M1 chip, but required additional work to get binaries working properly.
• Newer x86-64 machines are also getting improvements in terms of binary optimization.
• Go performance optimization techniques
• ARM64 and x86-64 CPU architecture differences
• Go AMD64 versions and their instruction sets (v1-v4)
• Template functionality in Go (new features for control flow and short-circuiting)
• Break and continue statements in templates
• Go workspaces and multi-module repositories
• Overuse of modules in projects and the new approach to using modules
• The upcoming Go 1.18 release and its features
• Introducing go.work files as a new concept in Go command
• go.work files allow multiple modules to be used within a single workspace
• go.work files have a similar syntax to go.mod files and include a "use" directive to specify directories and modules
• Replaces can still be used, but using the go.work file is preferred
• The introduction of go.work files requires changes in tools that interact with the Go command
• There was an experiment phase where users could try out go.work files with a development version of the Go command
• Discussion about code generation and reflection in Go programming
• Opinions on code generation: some think it should be avoided due to added developer friction, increased build size, and build time
• Bringing back the "try" proposal for error handling in Go
• Discussion of why the try proposal was unpopular and potential issues with its implementation
• The importance of proper error handling in Go code
• Potential benefits of try, including encouraging better error handling practices and reducing the need for shortcuts like "if err != nil {return err;}"
• Concerns about adding new features to Go due to backwards-compatibility promises and maintenance requirements
• Package management and its stability
• Challenges of contributing to JavaScript projects due to constantly evolving language features
• Difficulty in creating a new JavaScript interpreter engine without significant resources (e.g., huge corporation) 
• Discussion of the limitations on individual developers pursuing their own JavaScript engines