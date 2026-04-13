• Jeremy Rustin, creator of TiddlyWiki, is a programmer with a nearly 40-year career
• He began coding in 1978, working with early processors like the AT60 (SCAMP) and ARM chip
• He programmed the AT60 with a hex keypad and seven-segment display, with no high-level languages or interpreters
• Rustin values the experience of working close to the hardware and relates it to his current work
• TiddlyWiki is a single-page application and JavaScript-based, with a custom fake DOM
• The guest was introduced by a commenter "FND" on the show's ping repo, who described TiddlyWiki as unique and thought-provoking
• The evolution of computers from being close to the machine to making them more human-tractable
• The resurgence of DIY and maker culture with Arduino and similar kits
• Patterns of technological progress repeating over time
• The rapid improvement in computing power and the decreasing cost of technology
• The importance of longevity in software and technology, including the value of legacy code
• The history of programming languages and the impact of Visual Basic on business and industry
• The concept of "hackability" and its relationship to the design of technology
• The speaker defines "hacking" as changing one's environment through engineering or cunning, and believes that not being able to change one's environment is like being in prison.
• The speaker argues that hacking is a fundamental human right, as it allows individuals to improve their surroundings and exercise freedom.
• The speaker suggests that TiddlyWiki is unusual among open-source projects because it is designed for end-users, not just developers.
• The speaker believes that tools like TiddlyWiki can provide end-users with "mini godlike powers" by allowing them to shape digital technology to their needs.
• The speaker argues that developers have a duty to share their skills and techniques with ordinary people, and that tools like TiddlyWiki can facilitate this.
• The speaker provides an example of a volleyball teacher who used TiddlyWiki to create a specialized digital tool.
• Discussing the creation of a lesson planning system that is extensible and hackable, with a focus on the importance of user interface and tool usage in shaping the system's development
• Comparing the development of the system to the use of TiddlyWiki, and how the creator's expertise in volleyball influenced the system's design
• Introducing the concept of "hackability as a human right" and the idea that developers should consider the ethics and philosophy behind their work
• Discussing the importance of extending the capabilities of software to end users, using Git as an example of a tool that allows arbitrary changes to be made safely
• Exploring the idea that the ability to rewind and start over is denied to most people, and how this can discourage experimentation and innovation
• Previewing the discussion of TiddlyWiki and its single-file, extendable, and hackable nature
• Introducing the origin of TiddlyWiki and the motivations behind its creation, including the desire to create a wiki system that is open and accessible.
• The effectiveness of technical communities and wikis
• Importance of refactoring content in wikis
• Two archetypal refactorings: splitting pages and merging pages
• Optimizing information for reuse by breaking it into small chunks
• The concept of micro-content and creating a service like Flickr for text
• Creating a prototype in JavaScript to explore micro-content
• The speaker created a JavaScript demo, TiddlyWiki, to explore ideas, but it gained unexpected attention and was mistakenly thought to be a product.
• The demo allowed users to make changes, but when they tried to save, it would only print out their data in an HTML file.
• The speaker initially thought it was absurd to expect the demo to save changes to an HTML file, but discovered a Firefox extension that used privileged APIs to access the file system.
• This discovery led the speaker to realize that the browser can be treated as a virtual machine, allowing for the creation of new virtual machines by pressing command T.
• The speaker's approach to responding to criticism was to simply write code, rather than reacting to shortcomings.
• TiddlyWiki was developed as a result of this process, using the browser as a virtual machine and storing information in small, semantically meaningful chunks called Tiddlers.
• Developing a word to describe a "Tiddler" and its definition
• Tiddlywiki as a tool for creating small semantic units and writing in a stream of consciousness
• Refactoring and organizing information into Tiddlers
• Exploring and presenting data through Tiddlers
• The uniqueness of Tiddlywiki in its approach to small units of information
• The role of hypertext and its connection to how brains work and information organization
• The flexibility of Tiddlers to contain different types of media
• Mind maps and data structures for representing relationships between items
• Tiddly Wiki's data structure and its similarities to hash maps and NoSQL databases
• The importance of hypertext and linking in expressing relationships between items
• The concept of tiddlers as atomic units of data in Tiddly Wiki
• True Site Pulse's infrastructure monitoring service and the importance of accurate alarming
• Integrations with other tools and services for communicating team information
• Embedding dashboards into existing tools and sharing metrics outside an organization
• The ability to share communication and visualization across teams and externally
• Tilly Wiki is a self-contained application that does not rely on external libraries, but can use them if needed.
• It has characteristics similar to a framework, such as being able to write its own user interface in WikiText.
• Tilly Wiki uses a syntax tree and virtual DOM to minimize DOM updates.
• It treats the entire DOM as transient and moves state into JavaScript variables.
• The latest version of Tilly Wiki was rewritten from scratch.
• Poor quality of original Tiddly Wiki code led to decision to rewrite
• JavaScript evolution and Node.js launch created opportunity for rewrite
• Rewrite aimed to address limitations of single HTML file in browser
• New architecture allows for isomorphic applications (server and browser)
• Wiki content persistence varies depending on configuration (e.g. browser, Node.js, Amazon Lambda)
• Tiddly Wiki is a reusable JavaScript library for handling wiki text
• Engine converts wiki text to HTML and can be used for style sheets and other tasks
• Code is designed to be orthogonal and reusable, with new mechanisms introduced reluctantly
• The importance of presenting complex tools in a sequence of increasing complexity to help users develop a strong mental model of how to use them.
• TiddlyWiki's quine property and its implications for interactive use and augmentation of the user's brain.
• The challenge of persuading people that interacting with computers is practical, as faced by Vannevar Bush and early hypertext pioneers.
• The use cases for TiddlyWiki, including its potential as a hacker tool and a general-purpose, usable tool for anyone looking for a wiki or web-based notebook.
• The evolution of the author's approach to presenting TiddlyWiki, from showcasing its multifaceted nature to focusing on its core use case as a single file wiki.
• GitHub and TiddlyWiki's two pathways for non-developer and developer audiences
• Concerns about the state of TiddlyWiki's GitHub page, including many open issues and pull requests
• A decision to use GitHub issues for discussions, which has led to a large number of open issues
• Plans to implement a more conventional approach to issues, with clear policies for closing
• The need for clear policies on closing pull requests and using GitHub issues as a to-do list
• The use of email as a to-do list due to the complexity of GitHub issues and pull requests
• The challenge of balancing the needs of non-developer users with those of developers
• The challenges of working with a complex, stateless architecture
• The importance of documentation in making the system understandable to new users
• The universality of code as a means of verification and maintenance
• The single-handed development of TiddlyWiki, with a single contributor accounting for 98% of the code
• The ecosystem surrounding TiddlyWiki, including plug-ins and hosting services
• The need for conservatism in core development to ensure backwards compatibility and maintain plug-in compatibility
• The role of the core developer in prioritizing platform stability and encouraging contributions to plug-ins rather than the core.
• Discussion of the nature of working with TiddlyWiki, emphasizing the importance of respecting the ecosystem and the time and effort invested by others.
• The goal of creating a well-informed and purposeful community that can solve problems together.
• The diversity of uses and contexts in which TiddlyWiki is applied, and the satisfaction of writing code for others.
• The need for open source communities to attract attention and contributions, particularly in terms of documentation.
• The importance of introductory documentation and the need for contributors to help improve it.
• A personal anecdote about writing documentation and code for TiddlyWiki simultaneously.
• The identification of Ward Cunningham as a programming hero due to his development of the original Wiki.
• Reflection on the inspiring aspect of open source and community-driven projects, and the encouragement they provide to others.
• Introduction to TiddlyWiki
• Conclusion of the current show and thanking the guest
• Announcements for upcoming shows and guests
• Closing and goodbyes