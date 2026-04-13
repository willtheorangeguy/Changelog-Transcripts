• Event-stream malware incident
• npm package event-stream compromised by malicious actor @right9ctrl
• Malicious code injected into event-stream, spreading malware to users
• Dominic Tarr's past involvement with event-stream and his creation of pull-stream
• npm's quick response to remove the package and contain the issue
• Discussion on the implications of the incident on open source and community culture
• Dominic Tarr discusses the maintenance of his package event-stream, which he had largely ignored for five years
• He had hundreds of packages, and found it difficult to keep up with maintenance requests and issues
• He eventually handed over maintenance of event-stream to someone else, but then disowned 340 of his other packages to reduce his responsibilities
• He was unable to access the disowned packages, including event-stream, which made it difficult for him to respond to a subsequent security issue
• A sophisticated social engineering attack was made on event-stream, which ultimately failed to cause significant damage but still wasted people's time
• The attacker's goal was likely to target a specific Bitcoin wallet, which was not fully released yet
• Encrypted material found in minified file of event-stream library
• Community members, including FallingSnow, reverse-engineered the code to discover the encrypted Bitcoin wallet
• Attack was targeted and exploited a vulnerability in GitHub and npm package management
• Deterministic builds and reproducible builds could have prevented or made it easier to detect the attack
• Attack exploited event-stream's permissions, allowing access to network IO and crypto modules
• Potential for similar attacks in the future, and the need for better security measures and tooling
• ERights and its concept of security through controlled access to resources
• Project Xanadu and its influence on the development of the web
• Mark Miller's work on ERights and its application to secure computing
• Secure EcmaScript (SES) and its implementation of secure JavaScript
• Sandboxing and application of secure principles to existing codebases
• Deployment and user-provided code security
• Permissions systems and whitelisting in applications and modules
• Attack vectors and end-user permissions and trust
• Problem of maintaining widely used open source projects without the original creator's interest or involvement
• Difficulty of passing on maintenance responsibilities to new owners or organizations
• Need for sustainable funding models to incentivize maintainers to stay involved
• Challenge of distinguishing between creators who are passionate about their projects and those who have moved on
• Comparison of open source projects to infrastructure, such as roads and bridges, which require maintenance and upkeep
• Discussion around maintenance of abandoned open-source projects and the challenges of passing responsibility to the community
• Analysis of the event-stream example and how it highlights the issue of accidental infrastructure
• Importance of incentives for maintainership, including financial compensation or taking over by those who depend on the code
• Role of the community in taking over maintenance and establishing their own reputation
• Unsolved problems around deprecation, flagging abandoned packages, and adopting abandoned package names
• npm package ownership and the concept of abandoning a package
• The potential for package owners to claim ownership of abandoned packages and create new forks
• The importance of trusting package maintainers and the potential consequences of not doing so
• The trade-offs of using dependencies and the risks of "dependency hell" vs. "Not Invented Here syndrome"
• Heuristics for choosing dependencies, including reputation, personal relationships with maintainers, and code inspection
• Time zones and daylight saving time, and the complexities of coordinating across different regions
• Dominic Tarr's personal experience with the backlash and criticism he received for abandoning his package, and his feelings on the community's response
• Dominic Tarr's approach to the event-stream controversy and his decision not to apologize
• The importance of maintaining a fun and nonchalant attitude when dealing with controversy
• The concept that open source maintainers owe nothing and can't be held responsible for everything
• The benefits and rewards of open source development, including problem-solving with friends and effecting change
• Dominic Tarr's gratitude for the opportunity to share his perspective and enthusiasm for open source
• The importance of sharing and collaboration in the open source community, despite potential risks and challenges.