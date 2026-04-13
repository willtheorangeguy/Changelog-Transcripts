• Object-oriented programming languages
• Discussion of what makes a language object-oriented
• Comparison to other languages, specifically Java
• Introduction to Shannon Skipper from Square, discussing the opportunity for developers to build apps for sellers on the Square platform
• Square's Node SDK in TypeScript and its use cases
• Go Time discussion about object-oriented design in Go
• Interview with Rona about her workshop on object-oriented design in Go
• Debate over whether Go can be considered an object-oriented programming language
• Interview questions and answers suggesting people think Go is not OOP
• Decision to give a workshop on using Go for OOP
• Feedback from others after posting about the workshop, confirming interest in the topic
• Discussion of resources supporting both sides of the debate
• Multiple features of a programming language
• Comparison with Java and other object-oriented languages
• Limitations of single inheritance in Java and Ruby
• Use of interfaces and generics as workarounds
• Comparison with Go's approach to object-oriented design
• Addressing concerns that Go is not object-oriented
• Features missing in Go
• Lack of object-oriented programming (OOP) features
• Importance of hierarchy and composition in programming
• Inheritance and its alternatives
• Constructors and the lack thereof in Go
• Difficulty in defining types and allowing modifications
• Writing defensive code without constructors
• Best practices vs common practices in coding
• Challenges for developers new to Go language
• Discussion on Go language being object-oriented or not
• Mention of Go FAQs stating it's both yes and no
• Explanation of how Go's interface concept provides a different approach to programming
• Comparison with other languages like C++ and Java regarding type hierarchy and method definition
• Reference to the lack of type hierarchy in Go making objects feel more lightweight
• Discussion about whether Go is fully object-oriented
• The importance of allowing users to decide their own best practices and creative approaches in programming
• The need for a more open discussion among developers, with less influence from established "veterans"
• Reference to Rob Pike's quote on object-oriented design, but inability to find the source
• Design of APIs and handlers as functional programming
• Use of interfaces in design, but often using functions as interface instead
• Limited use of objects due to their ephemeral nature in certain contexts
• Historical influence of language design on coding practices
• Benefits of generics in storing models into databases or repositories
• Honeycomb as a fast analysis tool for revealing application truths
• Problems with traditional troubleshooting methods and tool sprawl
• Benefits of using Honeycomb, including reduced context switching and improved understanding of production issues
• Relationship between writing Go code and object-oriented programming (OOP) concepts
• Reevaluating OOP ideas based on actual coding experience versus academic teaching.
• Encapsulation and its relation to abstraction and generalization
• The ability to encapsulate information without hierarchy or composition
• Distributed systems and the need for aggregation of data
• Interfaces and their role in defining abstractions
• Generics/templates as a means to plug in functionality into something else
• The use of generics/templates being unnecessary when encapsulation is present
• C++ does not have interfaces but has classes with pure virtual functions
• C++ cannot pass objects of a class that was not written by the user
• Generics are needed for certain cases, such as working with derived types in a linked list or storing any kind of model in a repository
• Maps are generic types and always require generics
• Discussion about the generic maps and slices in programming
• Connection between generic types and object-oriented programming (OOP)
• Elimination of workarounds due to language maturity
• Differences between Go and traditional OOP languages
• Separation of data and behavior concepts in Go
• Critique of oversimplification by focusing only on structs as classes
• Discussion of whether Go is an object-oriented language
• Comparison with other languages such as JavaScript and Java
• Mention of a conversation with the speaker's boyfriend about object orientation in programming
• Reference to Ron Pike's criticism of object-oriented programming on Wikipedia
• Reflection on the concept of separating data from functionality as a key aspect of object-orientation
• Criticism of object-oriented programming (OOP) for being heavy
• Comparison to lightweight objects and natural-feeling code structure
• Use of pseudocode with colors to make OOP more accessible
• Teaching background and teaching interview preparation
• Ability to express complex pseudocode without significant thought or coding effort
• Red/black tree testing is problematic
• Difficulty in coding a red/black tree without prior knowledge or googling
• Importance of understanding edge cases in data structures
• Need for a generic library to simplify working with complex data structures
• Discussion on creating impossible tests for beginners and how to evaluate their skills
• Strategies for assessing a candidate's proficiency, such as starting with basics and testing them on specific areas they claim expertise in
• The speaker feels that hiring someone who cannot meet the high expectations of the team is unfair.
• They think they are raising the bar too high, making it difficult for others to match their skills.
• The speaker tries not to be unreasonable when interviewing candidates and assesses if they can learn during the process.
• They present challenges that require internalization and practical application, such as problem-solving under constraints.
• The goal is to see how candidates think and act in real-time, rather than just solving pre-existing problems.
• Opportunities given to the speaker and their potential for growth
• People's loyalty when given opportunities and a chance to prove themselves
• The importance of trying new things and investing in one's potential
• Embracing failure as an opportunity to learn and grow
• Addressing preconceived notions and biases based on past experiences
• Acuity platform is in beta and focuses on Kubernetes native application delivery, Argo CD, and GitOps
• Co-founders Jesse Suin and Alexander Matusenchev discussed their vision for the platform
• They aim to provide a fully managed Argo CD solution and improve developer experience with new tools and ecosystems around Argo
• Acuity wants to integrate multiple tools into its DevOps platform and deliver a user-friendly interface that enables developers to achieve what they need in just a few clicks.
• Mention of Argo CD enterprise readiness
• Explanation of what makes Acuity platform unique (audits and analytics out of the box)
• Comparison to previous experience at Intuit
• Promotion of LaunchDarkly platform for software delivery, innovation, and deployment
• Brief mention of host's background in C++ and development
• Mention of a jobs fair where an idea was discussed
• Discussion about a requested workshop or presentation
• Mention of procedural code and Go programming language
• Questions about the reasoning behind the request for the workshop
• Exclusion of certain patterns and approaches due to incompatibility with team's coding style
• Explanation of past reorganization efforts and unsuccessful middleware pattern implementation
• Discussion on the concept of object-oriented programming and its benefits
• Comparison between Go and other programming languages (Pascal and Java)
• Explanation of how object-oriented thinking makes coding easier
• Reflection on why some people may not understand or utilize object-oriented principles in their work
• Mention of a real-world problem that led to the development of an object-oriented language
• The speaker mentions Go being compared to Pascal as a child of its branches
• The speaker's familiarity with Pascal is limited and they don't see similarities between the two languages
• The speaker believes that knowing about language histories can be useful but not always necessary
• The discussion turns to C++ and JavaScript, both having many features that are rarely used
• The importance of letting go of unused features in programming and focusing on maintainable code is emphasized
• Discussion of people's reluctance to use a certain concept
• Use cases for a particular technique (with billing mentioned as an example)
• A quote from Rob Pike about a professor using multiple classes for a simple lookup
• Comparison of Java and Go programming languages regarding type awareness and explicitness
• Concerns about creating complex code bases for simple tasks in non-Go programming languages
• Go is explicit and requires clear design choices
• Packages should meet the open/closed principles
• Type assertions can be used to extend functionality
• Designing extensible code is challenging
• Interfaces are key for encapsulating and extending functionality
• Clear documentation and teaching others are difficult without proper understanding of the problem
• The speaker is trying to write a package that is extendable and usable
• Different programming languages have different requirements for writing packages
• In Go, the speaker does not need to expose interfaces like in other languages
• Writing a good package requires thinking about how people will use it
• The speaker struggles with teaching how to write good packages
• Defining what makes a package "good" is unclear
• Discussion of why the command-line tool "curl" is effective and does not require redesigning
• Reflection on defining when object-oriented programming (OOP) tasks are complete
• Transition to a more lighthearted tone, discussing "aha moments" in career development
• Mention of an upcoming workshop that will guide participants through a maze-like exploration of OOP concepts
• The moment when one realizes they can do something (in this case, coding)
• Lack of confidence and the importance of trial by fire
• Succeeding in something previously thought impossible
• Interview experiences and advice to "just go" and not wait
• Unpopular opinion on AI-generated code tools and their limitations
• The relationship between AI and coding, specifically whether AI systems can write code or understand object-oriented programming (OOP)
• The idea that AI may not need to follow the same constraints as humans when creating code
• The possibility of using bots for static analysis or dynamic analysis to evaluate if something is complete or open/closed
• The value of collecting opinions from non-professional developers about Go and other languages, rather than teaching them the language
• Evolution of best practices in Go
• Influence of Go on other languages and industry
• Openness to being influenced by non-Go developers
• Unpopularity of opinions and the "hall of fame"
• Relationship between Go and Object-Oriented Programming (OOP)
• Security audits and pen testing for tech startups
• Discussing code and business logic, with a focus on identifying scary parts that may break functionality
• Mention of the importance of prioritizing and checking complex code segments
• Comparison to a TV show "Severance" regarding intuition about potentially problematic areas
• Credits for partners and thanks to listeners