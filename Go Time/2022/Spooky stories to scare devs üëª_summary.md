• Discussion of tech horror stories
• Guest Dee Kitchen discusses her career in scary things and her package bluemonday (an HTML sanitizer)
• Guests discuss their preferences for salty vs sweet popcorn
• Kris Brandow explains why he finds horror movies boring due to their predictable plots
• Matt Ryer shares his dislike for horror movies with inconsistencies in physics
• Discussion of HTML sanitization and the use of Java OWASP Open Web Application Security API
• Mat Ryer shares a horror story about a $1,000 bill from Google Cloud Platform (GCP) due to an API key change and retry mechanism
• Johnny Boursiquot shares a similar experience with AWS Lambda and S3 bucket writes triggering infinite loops and high costs
• Dee Kitchen shares an anecdote about working for a company that man-in-the-middle's the internet, and how one of their customers wrote an infinite loop in their client, causing 8 million requests per second to flood their logging system.
• A company experienced a catastrophic outage due to a greedy regex in their system
• The regex caused all machines to freeze and lose connectivity, affecting all aspects of the service (DNS, TLS, HTTP)
• The team took 4 hours to recover from the incident
• Lessons learned include the importance of understanding regular expressions and having robust break-glass procedures
• A junior developer demonstrated bravery by reverting a potentially problematic change, but was later told not to try to fix it
• Strategies for tackling scary or high-risk tasks in software development
• Importance of documentation and tracking steps taken during complex processes
• Role of blameless culture in software development teams, focusing on system failures rather than personal ones
• Benefits of admitting mistakes and learning from them as an early career developer
• Imagination and creativity in podcast storytelling (campfire setting)
• Old computers being used as heaters due to high energy costs
• The "CPU Hot" program from the Amiga era that made CPUs hot
• Horror stories about IT professionals' experiences with difficult projects and clients
• A personal story about a contractor who was tasked with renaming an Active Directory, despite Microsoft Professional Services advising against it
• Discussion of the perils of distributed systems and integration
• Humorous conversation about marshmallows being cooked by old computers
• Assessment coordination across multiple schools for 3,000-4,000 students
• System integration issues and unexpected scale-related problems
• Personal consequences of a system failure on students and personal reflection
• Engineers' sense of consequence and responsibility in high-stakes situations
• Balancing abstraction and awareness of consequences to prevent burnout
• Importance of anticipating and mitigating potential risks and consequences in software development
• A Kubernetes cluster using Istio had an unsecured auth policy that was not visible to users, allowing anyone with a JSON web token to access the public API.
• The incident went undetected for 9 months, and when it was discovered, fixing the issue required re-examining all auth policies in the system.
• A related discussion on overly secure environments mentioned how IP firewall rules can lead to unexpected behavior and debugging difficulties.
• Another conversation revolved around password security, with a humorous exchange about default PIN numbers (1234) being too easy to guess.
• The panelists shared their experiences with "zombie code" (inactive but still present code) and the importance of regular code reviews to identify such issues.
• A final story was told about accidentally inserting a semicolon in a SQL statement, resulting in unintended updates to a production system.
• Update query without WHERE clause causes massive data corruption
• Restoring database from backup takes significant time and effort
• Importance of input sanitization in Go programming
• Most open source projects lack basic security measures like input validation
• Unpopular opinion: Sanitizing inputs is crucial, but often neglected
• Importance of revisiting fundamentals in software development, particularly assembly language
• Benefits of learning about the history and evolution of computing, such as understanding logic gates and computer architecture
• Value of starting with lower-level programming concepts and working up to higher-level ones
• Discussion of how people often accidentally follow this path in their careers without realizing it
• Idea of creating a university that teaches software development from a foundational level upwards