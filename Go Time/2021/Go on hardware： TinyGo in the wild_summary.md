• Introduction to the podcast and its format
• Discussion of TinyGo, a tool for building hardware with Go programming language
• Interview with guests Vladimir Vivian, Tobias Thiel, and Ron Evans about their work with TinyGo and Go in hardware development
• Mention of Natalie's background as a hardware student engineer at Intel
• Overview of the episode's topics: TinyGo and using Go to build hardware
• A friend's skepticism about running Go on microcontrollers sparks a challenge to prove it possible.
• The speaker writes a simple program and deploys it on a microcontroller, demonstrating its functionality in Morse code.
• Ron shares his own experience of wanting to run Go on microcontrollers for years and eventually discovering TinyGo.
• Vladimir discusses how he got into working with hardware and low-level programming using Go, including building a webcam from scratch.
• The group explores the potential of using Go for system programming and hardware development.
• The speaker was looking to use TinyGo for a project but found that it wasn't suitable
• They switched to using Go on a Linux operating system, which allowed them to do more complex tasks
• The speaker discussed how Go can be used to stream live video content from hardware connected to a Linux box
• Vladimir mentioned that the speaker's work is similar to one of the first applications of Go running on embedded Linux: video systems
• The conversation turned to computer vision and how Go is well-suited for this task, with specific mentions of GoCV and industrial/commercial users in China
• The speaker discussed using IOCTL calls directly to drivers, bypassing Sego
• They mentioned that the type system and memory layout of Go match one-to-one with C, making it easy to interface with C code
• Building a custom smart home system using Arduino microcontrollers
• Using TinyGo to create a Wasm application for controlling and monitoring devices remotely
• Mention of RFC 2324 (Coffee Pot Protocol)
• Discussion of coffee vs. tea as a competitive brewing topic
• Use of MQTT messages over Wi-Fi for network communication
• Use of Arduino Nano 33 IoT microcontroller with Wi-Fi capabilities
• Community Hardware Hack Day event
• Arduino's role in open source hardware and community support
• Unpopular opinions on technology vs. what we do with it
• Go programming language usage at Arduino
• Sponsoring of Community Hardware Hack Day by Go team
• Comparison of Nano 33 IoT and Nano IoT BLE boards
• Processor differences between the two boards (SAM D21 vs NRF52840)
• Incompatibility issues due to different hardware stacks
• Support for Go programs
• Memory safety and tooling advantages of Go over C
• Concurrency in Go
• Honeycomb: a production monitoring platform that provides a unified understanding of complex systems
• Firehydrant: a reliability platform for teams to automate incident response
• Known limitations of using Go for hardware projects
• Recommendation to read Tobias' book on Go for hardware projects
• TinyGo can run on small microcontrollers with limited memory, such as the Arduino Uno and ATtiny85 chip
• CircuitPython has a great developer experience but is limited by its memory usage
• Python's steady growth makes it a good choice for beginners, but it also has drawbacks
• The transition from Python 2 to 3 was a massive failure that the Python core team acknowledges
• TinyGo is not yet at version 1.0 due to concerns about stability and long-term compatibility
• Comparison between languages (Python vs other statically compiled language)
• Preference for statically compiled languages with static types
• Discussion on device security and its challenges compared to cloud security
• Question about TinyGo's implementation of Go runtime on microcontrollers
• Explanation of TinyGo's architecture and how it uses internal tooling and LLVM framework
• Limitations of TinyGo in terms of runtime and standard library abilities without an operating system
• Examples of common tasks that are not possible or require low-level hardware calls
• Implementing interfaces for reader-writer closers in TinyGo
• Current state of TinyGo and its hardware capabilities
• Community adoption and usage of Windows for industrial computing
• Future predictions for TinyGo and programming for hardware
• Potential for a single dominant language (Go) due to context switching difficulties
• The speaker discusses the next frontier in software development, including Web3 and truly distributed computing.
• WebAssembly (WASM) is mentioned as a key technology for this space, along with WASI.
• TinyGo is highlighted as an essential tool for using Go with WebAssembly, allowing it to run on smaller devices.
• The speaker shares examples of projects that are using TinyGo, including Astro and the proxy WASM project.
• He also mentions other applications of TinyGo, such as front-end development in Go (Vecti) and retro-style gaming on a web interface (WASM 4).
• The speaker discusses the importance of having a compiler for a programming language, and notes that TinyGo is not separate from Go but rather an implementation.
• He also mentions a project by ARM to provide support for LLVM on ARM-based microcontrollers.
• The perception that open source projects are only valuable when they attract financial support
• The challenges of sustaining a project without external funding or recognition
• TinyGo's current status as a niche project compared to standard Go, but potential for growth through WebAssembly adoption
• The importance of hardware development and the need for more diverse participation in this field
• Critique of C programming language for being outdated and potentially hazardous due to its widespread use in critical systems
• Discussion about Elixir running on Embedded systems
• Debate about the lack of significantly new concepts in software development over the past 20 years
• Criticism of various frameworks and methodologies (e.g. Agile, Extreme Programming, Kanban)
• Unpopular opinions:
	+ Software development has not seen significant innovation in 20 years
	+ The industry should stop disqualifying people for using "antiquated" tools (e.g. C, Emacs, Bash)
• Bad software is inevitable
• Personal anecdotes about life-changing programming experiences
• The importance and impact of spreadsheets in software development
• The barrier between professional programmers and everyday people
• Losing control over open-source software after releasing it
• Unpopular opinions on software and human behavior
• Discussion of "Zoom fatigue" and its impact on in-person events
• Hybrid events and their benefits (environmental friendliness, accessibility)
• Virtual event etiquette (name tags, social distancing indicators, options for physical contact)
• Challenges faced by new speakers presenting online
• Improving the virtual conference experience through technology and innovation
• Discussion of the prevalence of pumpkin-flavored products in various categories
• Proliferation of "pumpkin everything" trend
• Panelists' reactions to and jokes about the trend
• Recap of the conversation and appreciation for panelists
• Show wrap-up, including thanks and preview of upcoming episode