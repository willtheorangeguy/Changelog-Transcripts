• //go:embed feature in Go 1.16
• Embedding files inside a binary for web apps and other applications
• Problem of managing and deploying additional files (images, stylesheets, templates) alongside a binary
• Comparison with existing solutions (Packer, Pkger, go-bindata, Static)
• Benefits of //go:embed:
  • Simplified deployment
  • Transparency (no need to compile in or maintain separate build scripts)
  • Reduction of maintenance burden on tool maintainers
• Go's //go:embed feature allows embedding files into binaries, simplifying deployment
• Embedding HTML and CSS files can make deployment easier, but may not be suitable for large projects or teams
• Using //go:embed for secrets is not recommended, as they can be easily decompiled
• The feature also allows embedding strings or slices of bytes directly
• It provides a more reliable alternative to ldflags and other hacky solutions for embedding version information
• The Go team has been "paving the grass" by addressing real problems faced by developers, rather than forcing them to use specific tools.
• Discussion about using //go:embed to embed files into Go programs
• How to use //go:embed with variables (string, slice of bytes, embed.fs)
• Relative paths for embedded files are relative to the source code
• Using wildcard patterns to match multiple files and directories
• Limitations of Go's filepath matcher (no support for ***/)
• Best practices for embedding large numbers of files into a single variable
• Multiple go:embed directives can be used for complex embeddings
• Recursion in embedded assets, excluding dot and underscore files
• Discussion on template embedding and default behavior
• Importance of Go tooling in identifying embedded files
• Unintelligible mention of Pkger command
• Exclusion of files starting with underscore by default in Go
• Magic comments and opinions baked into the language
• Embed package and import requirements for embed feature
• Discussion on registration of database packages as a precedent
• Use of _import_embed directive for embedding resources
• Tooling capabilities and potential improvements for detecting embedded resources
• Personal anecdotes of embedded assets (ASCII image, Pikachu, quine)
• Go embed feature allows a program to embed itself and print its own source code
• Feature was initially proposed to allow embedding at the function level, but technical issues and practical concerns led to its restriction to top-level variables
• Embedding files as read-only, thread-safe global variables helps maintain simplicity and avoids mutability concerns
• New io/fs package introduces an fs interface that allows multiple types to implement a file system, making it more versatile and swappable
• Using the FS abstraction can be beneficial for working with files in the local file system, but may not always be the best approach depending on the specific use case.
• The fs package provides a built-in file system interface in Go, allowing for easier testing and development
• The interface is read-only by default but can be switched to use the os file system with command line arguments or flags
• This allows for development mode where files are refreshed automatically without rebuilding
• The fs package has several benefits, including reduced clutter from local file system embedded files and generated code
• It also provides a common point of abstraction for libraries and standard library packages
• Interfaces can now be written for S3 and other storage systems to treat them as virtual file systems
• The io.fs package abstracts away entire file systems in addition to individual files, allowing for more flexibility and testing capabilities
• Government funding for open source software
• Science grant proposal process as a model for software funding
• Potential benefits of government-funded open source development
• Unpopular opinions on using mocks in testing
• Use of real services or emulators instead of mocking
• Use of random numbers in tests to simulate real-world scenarios
• Mark Bates' unpopular opinion that he doesn't like bacon
• Discussion of veganism and carnivore diets
• Favorite meats (Mark Bates)
• Brief discussion about charcuterie options for vegans
• Wayne Ashley Berry's full name and preference for using it
• Carl Johnson's blog and uniform resource indicator
• Discussion about the popularity of the name "Carl Johnson"
• Personal stories about namesakes (Mat Ryer, Mark Bates, Carl Johnson)
• Comparison of fake meat vs. traditional meat
• Jokes and banter about health benefits, carbon offsetting, and Neil deGrasse Tyson