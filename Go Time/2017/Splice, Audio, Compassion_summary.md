• Splice is a platform that connects music producers with samples and loops
• Matt Aimonetti co-founded Splice in 2013 and has a background in sound engineering and programming
• He previously worked on Merb, a Ruby project, and later moved into the Go community
• Splice's technical stack includes desktop clients, mobile apps, and web presence, all built with Go
• The company handles large amounts of data (over 9 terabytes per day) and requires concurrency, which led to the choice of Go as the primary language
• Creating an abstraction layer for multiple projects
• Implementing lossless compression and deduping to reduce data duplication
• Partnership with Pioneer DJ for hardware sampler integration
• Developing a web-based beat maker and sequencer using Go
• Using Go as the primary language, with TypeScript also being used
• Addressing latency issues through proper context handling
• Discussing performance benefits of using Go, including low memory usage
• Comparing Go to other languages (e.g. Ruby) in terms of syntax stability
• Hiring philosophy: prioritizing problem-solving skills and willingness to learn Go over prior experience with the language
• The interview process at Aimonetti's company involves a coding test in frontend and backend, with the goal of discussing how candidates approach problems rather than grading their ability in Go.
• The test is designed to assess problem-solving skills and willingness to learn, not expertise in Go.
• Go is used for QA automation due to its fast compile language and good tooling, making it easier for non-technical team members to write code.
• Aimonetti believes that Go is an accessible language for beginners and can be a good introduction to programming.
• The community needs to focus on making Go more welcoming and inclusive for new users, rather than emphasizing its features or technical aspects.
• Concurrency is not the only important aspect of Go, and other features such as simplicity and ease of use should also be highlighted.
• Discussion of Go's concurrency features being overemphasized
• Simplicity of the Go language for beginners
• Use of Go in production environments with simple web services
• Challenges of using Go for audio processing and real-time systems
• Development of libraries for audio processing in Go to bridge the gap between Python and C
• Comparison of Go's performance and ease of use compared to Python for audio analysis
• The challenges of using Go for multimedia processing, including type conversion costs and missing tooling.
• The need for basic libraries for audio and video processing in Go.
• The potential for Go to be used for real-time multimedia processing with the help of C libraries.
• The importance of having people motivated to write libraries for complex tasks like data science and multimedia processing.
• Matt Aimonetti's personal experience writing his own libraries for audio and video processing and releasing them as open source.
• The need for more freedom in the Go team to let contributors work on side projects and libraries.
• Matt Aimonetti's recent blog post about a prison outreach program where he helped entrepreneurs-in-training with their pitches.
• Defy Ventures' mission to give a second chance to inmates through entrepreneurship and programming skills
• High recidivism rates in the US prison system (75-85% of inmates return to jail)
• Success of Defy Ventures' program: 3% recidivism rate for graduates with a master's degree from a real university
• Systemic issues in the US prison system, including racial bias and unfair sentencing
• Importance of equal opportunities and access to resources for successful entrepreneurship and programming
• Abstraction layers in modern life (e.g. technology) that can disconnect people and hinder meaningful relationships
• Defy Ventures' programs are available in 23 prisons across the country
• Importance of teaching social skills to engineers
• Value of community service and volunteering for personal growth and team morale
• Challenges of implementing community service in tech companies (e.g. vacation time, background checks)
• Great American Teach-In program for parents to teach students about their work
• Scott Lobdell's autopilot blimp project using Go on Raspberry Pi
• Gokrazy all-Go userland for Raspberry Pi
• Discussion on Gokrazy, a lightweight operating system for Raspberry Pi that runs Go applications
• Features of Gokrazy, including web interface and security benefits
• Mention of Matt Aimonetti's free online book "Go Bootcamp"
• Explanation of Retool, a vendoring project for binaries developed by Twitch TV
• Discussion on video processing in Go, with mentions of projects from Comcast and other companies
• Shout-out to GitLab for their open-source community edition and alternative to GitHub
• Shout-out to Ramya Rao for maintaining the Visual Studio Code Go plugin
• Ramya's contributions to the Go extension in VS Code, including features like a better debugger and test generation
• The importance of community support for her work, with 91 open issues that need help from users
• Discussion of the Language Server Protocol (LSP) and its potential impact on IDEs
• Comparison of Visual Studio Code's speed to other GUI editors, particularly Electron's role in optimizing performance
• Erik St. Martin's #FreeSoftwareFriday announcement featuring React