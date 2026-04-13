• Black Hat Go book discussion
• Author Tom Steele on the meaning of "Black Hat" and how it relates to the book's content
• Working from home tips, including staying hydrated and taking breaks to move around
• Chapter 7: Abusing databases and file systems in the Black Hat Go book
• Book's target audience: people new to Go or security professionals looking for practical tools
• Introduction to Go experience of co-authors
• Using Go for network manipulation (proxies, tunnels)
• Benefits of using Go (cross-compilation, no dependencies, low footprint)
• Book examples and projects (credential harvesting, keylogging, DNS tunneling)
• Co-author's experience with Go (building a library for scripting)
• Discussion on a book about security tools and techniques written in Go
• Importance of writing one's own code to understand underlying mechanisms
• Role of proxies in traffic shaping and inspection, including DNS proxying
• Use of Go to rewrite TLS packages and modify client hellos for firewalls
• Ethics of sharing knowledge about hacking and bypassing security controls
• Argument that sharing this information can help defenders improve their defenses
• Importance of proper authorization and virtual labs for testing and experimentation
• Security testing websites and bounty programs
• Known security techniques and flaws in software
• Importance of knowing potential attacks for developers and defense side
• Parallels with operations, making sure software is operable before shipping
• Balancing security and usability, finding a happy medium
• Go as a foundation for writing secure code, its strengths and weaknesses
• Contextual escaping and its importance
• Go's implementation of contextual escaping and its history
• Common gotchas and security vulnerabilities in Go applications
• Mass assignment and serialization issues
• CSRF (Cross-Site Request Forgery) protection and token usage
• CORS (Cross-Origin Resource Sharing) complexities and challenges
• Frameworks can hide security issues if they're not designed to handle them properly
• Importance of being explicit when handling user input and setting content types correctly
• Relying on well-designed frameworks and packages is acceptable, but developers should still be aware of potential security risks
• Validation of user input is crucial and shouldn't rely solely on struct mapping
• Go's concurrency model can lead to unbound concurrency issues if not handled properly
• Criticism of the Go programming language's cgo package
• Memory safety in Go and potential vulnerabilities due to race conditions
• Importance of fuzz testing for finding bugs and panics in code
• Perception that denial-of-service (DoS) attacks are less critical than memory corruption or remote code execution
• Difficulty in convincing developers to take security issues seriously, particularly if they involve DoS
• Strategies for illustrating the impact of security vulnerabilities, including using proof-of-concept code
• Don't store encryption keys alongside encrypted text or expose them to the internet
• Use least privileges and permissions, don't run as root
• Validate signed ciphertexts stored in databases
• Hash passwords instead of encrypting them
• Use a secure method to generate URLs for password reset links (don't use the Host header)
• Implement proper enum support in Go
• Discussion of a movie that didn't hold up
• Comparison to other movies (e.g. Avengers)
• Criticism of the movie's ending and pacing
• Personal nostalgic reactions to the movie (Mat Ryer, Jerod Santo)
• Mention of a specific sad moment in the movie (Artax drowning)