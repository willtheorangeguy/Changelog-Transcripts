• Go's growth and specialization within Google
• Internal vs external community work on Go
• Brad Fitzpatrick's role as public face of open source Go
• Process for contributing to Go project
• Upcoming changes to contribute process (pull requests, etc.)
• Codenames for Go releases ( proposal from Brian Ketelsen)
• Discussion about adding GoTime to the website
• CL (change list) 41146 and its approval process
• Proposing changes to the standard library, including requirements for proposals and submitting code without a strong use case
• Adding code to GitHub instead of the standard library for flexibility
• Domain name registration and management, including tips for purchasing domains
• Discussion about the Go 1.9 release and plans to get the community more involved in bug triage and code review
• Gardening tasks and triaging bugs
• Organizing a shared presentation for meetups on contributing to projects
• Exploring the concept of "Bugmash" or collaborative bug-fixing events
• Improving the contributing process and documentation for Go project contributors
• Using tooling to accept GitHub pull requests and convert them into Gerrit changes
• Discussion about the _Help Wanted_ tag in GitHub for Go and its limitations
• Challenges of labeling issues as "beginner-friendly" due to varying difficulty levels
• Alternative approaches to labeling, such as bite-sized tasks or time-chunks
• Brad Fitzpatrick's hobby project involving home automation and motion detection using Go
• Use of OpenCV and FFMPEG in the project
• Generating GIFs from video footage and sending them via Telegram
• Ideas for improving the project, including object recognition with Google Vision API
• Sony MiniDiscs with unknown music content
• Difficulty accessing old floppy disks and digital storage devices
• Nostalgia for early computing experiences, including dial-up internet and cassette tapes
• Discussion of the TV show "Halt and Catch Fire" and its portrayal of the 1970s and 1980s computer industry
• Mention of the HBO series "Silicon Valley"
• Introduction to Camlistore (Perkeep) as a personal storage system and its development in Go programming language
• Brad Fitzpatrick discusses his past involvement with Camlistore and his current role in reviewing contributions from another developer
• The development of Camlistore's LetsEncrypt integration is explained, including its impact on ease of use and security
• Brad mentions the potential for subdomain rate limiting issues with LetsEncrypt and plans to address this issue
• Go team burnout and frustration with repetitive tasks are discussed, as well as motivations for a potential Go 2.0 release
• The idea of goroutines being Go's unique feature is expressed, and concerns about other languages copying them are mentioned
• Brad mentions Crystal language, a Ruby-like language that has adopted goroutines and channels, but notes it still needs work on its standard library
• Discussion about language features and how they compare to Go
• Goroutines and channels as a key aspect of Go's design
• Other languages experimenting with lightweight tasks or goroutines, but struggling to implement them effectively
• Crystal language's attempt to incorporate Go-like features, but ultimately falling short
• The importance of code readability in Go and its impact on productivity
• Why people might be hesitant to try Go due to its perceived complexity
• Projects attempting to create runtime environments for other languages (e.g. Python in Go)
• Prospects for adding Generics to the Go language
• Ian Lance Taylor's efforts to design a proposal for Generics, and potential plans for a Go 2 release
• periph.io as an alternative to Gobot for GPIO and I2C/SPI
• Dave Brophy's code generation tool at github.com/dave/jennifer
• React bindings for GopherJS at github.com/myitcv/react with Preact support
• Discussion on removing items from the Go standard library, including HTTP
• Potential changes to the Go language around the 10-year mark
• The Go team's decision to include HTTP in the standard library and its implications
• Debate over what should be included in the standard library and how it affects usability and adoption
• Discussion of promoting external libraries versus maintaining internal ones
• Concerns about maintenance, fragmentation, and the need for better package discovery tools
• Ideas for analyzing and optimizing the Go ecosystem, such as using GitHub data and machine learning
• Proposal to make bigints automatic and efficient
• Removing `new` keyword from Go language
• Simplifying declaration of slices and arrays
• Getting rid of naked return statements
• Changing string and byte slice handling in Go to reduce confusion and overhead
• Introducing a "view of memory" type to accept both strings and byte slices, with read-only access.
• Free Software Friday segment on the podcast
• Shoutouts to open-source projects: Changelog website and GoTime website's search feature, Buffalo for web development in Go, GopherCon and GopherAcademy websites
• Discussion of production use cases for Buffalo in Go
• Mention of previous production environments used on the show (Caddy, Hugo)
• Code review and shipping code discussed
• Shoutouts to contributors to libraries for sensors and Arduino projects
• Easter pig project and barbecue data streaming mentioned