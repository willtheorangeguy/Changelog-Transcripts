• SQLite pronunciation debate
• SQLite update: usage, development pace, and features
• Fossil SCM: definition, capabilities, and licensing
• Fossil SCM licensing: public domain and commercial use
• Comparison with Git and GitHub usage
• SQLite code churn and testing efforts
• Richard Hipp discusses his business model, which relies heavily on support contracts for SQLite
• The company has a small team, with Richard Hipp and three others working on support and development
• SQLite is often used in embedded systems, cell phones, and the internet of things, but is also used in large-scale applications like Bloomberg and Expensify
• Richard Hipp code reviews and develops SQLite code daily, often in response to customer needs or new ideas
• The company has a distributed team and has kept its business small and sustainable
• Richard Hipp mentions the Litestream project and other tooling that is making it easier to use SQLite in production environments
• The company has relationships with Expensify, Bloomberg, and other companies that use SQLite in their applications
• Richard Hipp's preference for SQLite's small company feel and coding style
• Benefits and limitations of staying small and focused
• Discussion of Ben Johnson's Litestream project and its potential to make SQLite massively scalable
• Richard Hipp's thoughts on the balance between focusing on SQLite's core features and exploring new ideas
• SQLite's file format and legacy applications
• Potential for a column store option in SQLite
• Trade-offs and complexities of implementing a column store in SQLite
• Considerations for library size and space constraints on edge devices
• SQLite's reliability is due to Richard Hipp being a bad salesman
• Richard Hipp wrote his own web server, Althttpd, to power SQLite.org due to difficulty with configuring existing servers
• Althttpd is a simple, secure, and easy-to-understand web server
• Richard Hipp prefers writing his own tools and software rather than relying on others
• This approach has allowed him to implement features and optimizations not possible with existing software
• Althttpd's design includes features such as dropping into a chroot jail and being statically linked
• Richard Hipp discusses the challenges of hosting a website and fighting off malicious robots
• He shares an anecdote about detecting a specific robot by looking for a misspelling in its user agent string
• Hipp emphasizes the importance of controlling one's own tools and code, using SQLite and Fossil as examples
• He explains how using a custom parser generator allowed him to add new features and maintain backwards compatibility
• The conversation touches on the idea that having the right tool can make hard jobs easier, and that controlling one's own tools allows for fine-tuning and optimization
• Hipp mentions that he uses commercial web browsers, standard compilers, and other tools, but still chooses to write his own custom tools for certain tasks
• The conversation also touches on the challenges of hosting one's own email and the difficulties of creating a unified system for doing so.
• Discussion of Richard Hipp's editor, "e", and its potential for widespread adoption
• SQLite's development history and its creator's surprise at its success
• Fossil, a version control system created by Richard Hipp, and its development process
• Comparison of Fossil to other version control systems, including Git and Mercurial
• Richard Hipp's goals for Fossil, including meeting the standards of DO-178B and working from shared hosting environments
• Key features of Fossil, including its distributed nature and automatic pushing of changes to a server
• Fossil's development style suits SQLite's needs, while Git's style suits the Linux Kernel's needs
• Fossil uses SQLite to store all its data, making it a self-hosting opportunity for SQLite development
• Fossil is a single-file, non-distributed system for version control, bug tracking, and wiki management
• Fossil has a feature for syncing all repositories with a single command
• Fossil's branching and merging model is similar to Git's, but with branch names retained and easily accessible
• Fossil's relational database design allows for following branches forward and backward in time, enabling situational awareness
• Fossil's web interface is a GUI that can be accessed by typing "fossil ui" in the command line, and it provides a rich interface for viewing repository information.
• Fossil has a peer-to-peer capability, allowing users to use it without setting up a server.
• Fossil's branching and merging capabilities allow users to keep all history, even if files are deleted or changed.
• Fossil has a "shunning" system that allows users to remove unwanted or copyrighted artifacts from the repository.
• Fossil's philosophy emphasizes recording all history, including mistakes and failures, as a way to promote humility and transparency in development.
• Benefits of Fossil's branch-based version control system
• Comparison of Fossil and Git
• Fossil's relational database vs Git's key-value database
• Potential integration of Fossil's ideas into other version control systems
• Relational database in Git
• Use of mirrors to combine Fossil and other version control systems
• Ability to query Git as if it were a SQL database
• Discussion of using a relational database, specifically SQLite, to store data
• Comparison of SQLite's public domain license to BSD-style license used by Fossil
• Reasons behind switching from public domain to BSD-style license
• Challenges of maintaining public domain code
• Comparison of Fossil's self-hosting capabilities to hosted services like GitHub
• Discussion of the value of self-hosting and the importance of taking care of oneself (freedom through self-sufficiency)
• Fossil as an ultralight backpacking tent for taking care of oneself
• Importance of community and collaboration in software development
• Need for a hub or directory of Fossil instances for federated collaboration
• GitHub's focus on the "hub" aspect, rather than just Git
• Possibility of Fossil repositories on GitHub, but challenges and work required
• Idea of "fossilizing" Git by incorporating Fossil's features and principles
• Benefits of a unified repository management system for developers
• Development of Pikchr, a tool for creating diagrams in Markdown documents
• Pikchr's origins in the legacy language Pic from Bell Labs
• Pikchr's integration with the Markdown standard for fenced code blocks
• Efforts to encourage other Markdown engine developers to adopt Pikchr
• Discussion of Richard Hipp's presence on the show and his ideas on freedom in programming