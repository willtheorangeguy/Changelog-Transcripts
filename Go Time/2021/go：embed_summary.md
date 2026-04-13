• Problems Gophers are facing with the Go tool
• Modules as a solution to incorporating open-source software
• Go's built-in support for modules
• Cloud native operations and GitOps
• Book "Cloud Native Patterns" by Cornelia Davis, CTO of WeWork
• Discussion on pasting without formatting in editors
• Introduction of Mark Bates (Go contributor) and Wayne Ashley Berry (principal engineer at GoDaddy)
• Artistic background of guest, Wayne Ashley Berry
• GoEmbed feature in Go 1.16
• Purpose of GoEmbed: embedding files inside the binary for web applications and other use cases
• Web application example: simplifying deployment by including images, style sheets, JS, templates, etc. within the binary
• Alternative solutions for file management: cumbersome or transparent methods that required compiling in files or using external scripts
• New solution (GoEmbed) is transparent and simplifies shipping binaries with all necessary files
• Example of Hugo static site generator and Buffalo web framework demonstrating the need for embedding files within the binary
• Problem of keeping Go files in sync with embedded files
• Use of build scripts to manage embedded files
• Comparison with Go modules and streamlined process
• Discussion of alternative solutions, including Packer and Packager
• Reference to maintenance burden on tool maintainers
• List of tools for embedding files, including Go bin data and static
• Analogy of "paving the grass" in software development
• Go team's approach to addressing real-world problems with Go tools
• Modules as a solution to incorporating open source software
• Built-in support for file embedding in Go tool
• Go can have shared tools across projects.
• Using GoEmbed for embedding secrets in binaries may not be a good idea due to potential client access and decompilation risks.
• Embedding license information or build version into a binary using Go tags or embed is possible.
• The Go linker can replace variables with specific values, but requires scripting setup.
• Go embed allows file system embedding, string, or slice of bytes embedding.
• Using Go embed eliminates the need for ld flags and reduces potential errors.
• Equinix Metal overview
• Cloud infrastructure on bare metal
• Features: 60 Second Deployers, hourly pricing, customer success team, x86, Intel, AMD, ARM support
• GoEmbed: embedding files into Go strings using a directive in source code
• File resolution is relative to the source code and can be recursive using wildcards (e.g. templates/*)
• Limitation of Go file path matcher does not support multiple consecutive wildcards
• Using Go embed comments to specify which directories and files to include
• Editor support for GoVet warnings and build errors when using Go embed comments
• Specifying multiple directories and patterns in Go embed comments
• Embedding entire directories with recursive embedding
• Ignoring dot and underscore files in Go embeddings by default
• Using underscore file names as a common pattern in the Ruby on Rails world
• Tooling support for displaying expected embedded files, such as using `go list` command
• Discussing Go tooling and debugging
• Explaining the purpose of embedding files in Go
• The importance of understanding language opinions in Go
• Critique of importing underscore embed for embed functionality
• Registration of packages and side effects in Go
• Best practices for using embed in Go projects
• Retool is a platform for building internal tools quickly
• It allows users to assemble apps in minutes by dragging and dropping pre-built components
• Users can connect to various databases or APIs, including GraphQL and GRPC
• The platform empowers users to work with all data sources seamlessly in one app
• Retool is highly hackable and flexible, allowing users to build custom solutions
• The platform can be used with either a cloud service or on-prem hosting
• Examples of creative uses of the platform are shared by users, including embedding ASCII images and Quines (self-printing programs)
• Go's embed feature allows embedding groups of files at the top level
• This feature was previously allowed within functions but was later dropped for simplicity and consistency
• The FS is meant to be used globally and is read-only, but can be swapped out entirely
• There are two types of file systems: embed.fs and io/fs
• io/fs is an interface that allows multiple types to implement being a file system
• It's recommended to write functions to take the fs.fs interface instead of referencing globals directly
• Using fs abstraction for versatility
• Embedding files and using a read-only interface
• Switching between embedded and OS files based on command line arguments or flags
• Development mode vs. build time behavior
• Pros of the new file system concept
• Interfaces for working with files, including parsing and processing
• Potential uses in cloud providers' clients for S3 buckets or other storage services
• Writing interfaces for different storage systems (e.g. S3, Postgres) that mimic regular files
• Discussing the IO package in Go and its features for abstracting away file I/O operations
• Introducing the new package IO FS, which allows abstraction of an entire file system
• Comparing IO readers to actual files on disk, highlighting their differences
• Mentioning the possibility of mocking out properties that don't apply to IO readers (e.g. file size, modification time)
• Announcing the segment "Unpopular Opinions"
• Carl sharing his opinion on government funding for open source software development
• Discussing current methods of funding open source projects, including corporate sponsorship and Patreon models
• Carl arguing in favor of a system where governments fund open source software development
• Addressing potential criticisms to this idea, such as supporting individual developers rather than projects.
• Discussing the idea of using government funding to support open source software development
• Considering the benefits and limitations of having government-funded developers work on specific features
• Exploring ways for open source maintainers to earn a living
• Proposing that the government should open-source its own software when possible
• Debating the use of mocks in programming, with some arguing against using them due to their limitations
• Discussing the importance of testing code against real databases rather than mocking them
• Touching on the concept of FS.FS and whether it is considered a mock or an interface
• Discussion about bacon and its varying types
• Host expresses unpopular opinion that bacon is overrated
• Comparison of British and American-style bacon
• Mention of a cocktail with bacon in New York
• Talk of vegans and carnivores, and potential for differing opinions on meat
• Listeners discuss favorite meats and agree to save more discussion for another episode
• Mention of a personal experience with someone setting fire to the speaker's trousers
• Confusion between Carl Johnson, a video game character, and Mark Bates, the speaker
• Discussion about fake bacon and vegan diets
• Commentary on "Impossible burgers" being unhealthy despite their name
• Humorous exchange about carbon offsetting in reverse
• Discussion about creating carbon and the origin of elements
• Mention of Neil deGrasse Tyson and the possibility of getting him on a future episode
• Reference to a previous episode where they discussed black holes and it was considered "embarrassing"
• Promotion for the changelog plus plus membership and ad-free experience
• Credits and announcements for upcoming episodes