• Introduction to Go Time podcast
• Sponsorship by Stack Impact and Arden Labs' series of Go Training
• Guest introduction: Filippo Valsorda, Cloudflare employee working on Go projects
• Hello Gopher project explained:
  • Simplifying the process for non-Go developers at Cloudflare
  • Solving issues with GoPath and repository setup
  • Providing a straightforward way to bootstrap a project without needing to set up GoPath
• Discussion of common confusions and challenges with GoPath and contributing to repositories
• The user is happy with the adoption of a tool or feature
• A user reported an issue that was resolved by referring to documentation
• Brian and Carly haven't had a chance to try out the tool yet
• GoPath is mentioned as a solution for setting up development environments in Go
• It's discussed how GoPath solves one problem but not all, especially for contributing and Git cloning
• Hello Gopher is introduced as a drop-in replacement that works with normal Go projects
• Hello Gopher is compatible with existing Go structures and doesn't interfere with colleague's settings
• The tool is agnostic to the vendoring tool used
• The speaker discusses the demo "WhoAmI" which uses public SSH keys from GitHub
• WhoAmI uses the GitHub API to collect and match public keys with their corresponding user profiles
• The tool logs in users via keyboard-interactive login, even if they don't have any matching public keys
• It then attempts to find a matching username and surname by cross-referencing the matched keys with a database
• The speaker runs into issues trying to test the demo on their own machine due to multiple SSH keys being used
• They discuss potential uses of the tool, including exposing information leakage via SSH login
• Implementing TLS 1.3 protocol
• Using CryptoTLS instead of OpenSSL for TLS implementation
• Cloudflare's deployment of TLS 1.3 stack in Go
• Fallback system for TLS 1.2 in case of failure
• Comparison of security and bug tracking between CryptoTLS and OpenSSL
• Recommendation to use Go's native TLS implementation instead of OpenSSL
• TLS 1.3 offers improved performance and robustness over TLS 1.2
• TLS 1.3 cuts an entire round trip of communication with the server
• This results in significant latency reduction, especially on mobile networks
• The Cloudflare crypto team's work includes deploying code to the world and researching secure protocols
• A talk by Filippo (or George Dunkesley) discussed the black magic of Sego and how to make it tolerable
• There is a talk on TLS 1.3 given at 33C3, but no published material on the Go part
• Discussion of an attempt to SSH into an HTTP server, highlighting the differences between protocols
• Introduction and advertisement for Stack Impact, a performance monitoring service for Go applications
• Filippo's work on crypto and TLS at Cloudflare and his interest in Caddy
• The reproducibility of Go binaries, allowing for identical builds across different machines
• The concept of binary transparency, where builds are logged to prevent backdoors from being hidden
• The challenges of achieving reproducible builds with other languages and projects, such as Debian
• Go supports multiple architectures and operating systems
• The resulting binary would change for different platforms (Windows, Linux, ARM)
• 32-bit Spark is not supported on a Raspberry Pi
• Go can run on mainframes and other legacy systems
• Latency profiling and Camly Store are being discussed in the show document
• Latency profiling tools are not as well-surfaced or publicized as CPU profiling tools
• GoTracer provides profiles for blocking, I/O, network, and scheduling poses
• Recordings of past talks or conversations
• GoTime logo design
• Gopher Eyes website and its features
• Chrome DP project and its capabilities
• Camlistor archiving system
• Various mentions of community projects and contributions (Gopher avatar, custom avatars)
• Implementing a headless browser for load pages and taking snapshots
• Using Go to write scripts for steering a browser, clicking inputs, sleeping, and taking screenshots
• Discussing integration tests using a browser
• Shoutouts to pre-alpha dep tool and GPS library
• Interviewing Sam Boyer about tools and rendering
• HelloGopher's user flow goals and making sure users can build projects outside GoPath
• Using make files as documentation for project workflows and recipes
• Discussion about a makefile being reviewed and destroyed
• Comparison of using a makefile to writing bash code, with the latter being more straightforward
• Introduction of Arden Labs as a sponsor for their Ultimate Go training series
• Explanation of the benefits and features of the training series
• Joking about makefiles and phony declarations
• Discussion about the "Gopherization" phenomenon on social media platforms
• Route 53 DNS management and load balancing for Kubernetes services
• Creation of named endpoints in load balancers and fixing DNS to point to those load balancers
• Integration of Kubernetes load balancing and endpoints on AWS and GCP
• Sourcegraph, a code navigation tool that allows browsing across repos and GitHub universe
• Play with Docker project on GitHub
• Embedding a Docker in Docker instance for web browser access
• Multiple terminals embedded in web browsers with Docker support
• Creating Kubernetes clusters within the web browser
• Open source project discussion, including Ponzu CMS and Buffalo website integration
• Free Software Friday shoutouts, including:
  • Dominic Honef's static check tool (StaticCheck)
  • Brian Kettleson's GopherCon website development using Ponzu CMS and Buffalo
  • GoTime FM Patreon listing
• Patreon discussed as a way to support Dominic's work
• Benefits of Patreon for developers mentioned, including saving time and money
• Discussion of VimGo and how the speaker donates an equivalent amount to what they would pay for a commercial IDE
• Zim project introduced, a fast and feature-rich shell replacement for zsh
• Go 1.7.5 and 1.8 RC3 releases announced and discussed
• Go 2.0 discussions mentioned, including potential features like generics and JVM backend
• GCC Go usage questioned, with the speaker wondering if it's still maintained or widely used
• Invitation to Ian Lance Taylor to discuss GCC Go on a podcast
• Embarrassing moment at Gopher Con with Dimitri
• Discussion about the speaker's dinner and a particular question asked by Ian
• Wrap-up of the show, thanking guests and sponsors
• Announcement of upcoming shows, including Matt Ryer's appearance next week
• Personal anecdote about running into Matt Ryer in Florence
• Closing remarks and thanks to sponsors and team members