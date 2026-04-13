• Go Code pop quizzes
• Guest Miki from Israel joining the discussion at 11:10 PM his time
• Guest Dave from Sydney joining the discussion at 6:10 AM his time
• Discussion of time zone differences and scheduling meetings across different time zones
• Challenges of meeting in different time zones and finding available times
• Introduction round for participants: Dave is a gopher at GitHub, working on backend stuff written in Go
• Pop quizzes in Go: inspiration comes from learning new things, including bugs and student questions
• Mickey shares his experience with pop quizzes and teaching, emphasizing the importance of continuous learning
• The importance of considering non-programmers' perspectives when designing technology
• Developing "blinders" as technologists can lead to overlooking user needs and experiences
• The need for users to feel comfortable making mistakes and trying new things in a low-stakes environment
• Introducing computers and programming concepts at an early age to foster familiarity and comfort with technology
• The value of embracing failure and learning from mistakes in the process of teaching and development
• The speaker discusses the origin of some Go language concepts from mistakes and bugs
• Many Go quizzes come from reading the Go spec and understanding built-in operations like copy()
• The original idea for a quiz came from realizing that many people don't remember that copy() returns a number
• The speaker created a constraint for themselves to fit questions into a tweet
• The goal was to create pop quizzes that can be attempted by anyone, not just experts
• Quizzes are designed to fit within a tweet and are intended to encourage thinking rather than relying on the playground
• Pop quiz format originating from Josh Block's "Java Puzzlers" book
• Short programs with surprising explanations
• Mutation of pop quiz format from short tweets
• Examples of pop quizzes at London Gophers and Japanese Gophers meetups
• Reducing pop quizzes to 20-minute presentations for meetup use
• Value in explaining unexpected answers and encouraging learning
• Concern about posting too many "unexpected" questions, potentially leading to audience expectation
• Difficulty level and fairness in pop quizzes
• Hexadecimal floating point literals in Go programming language
• Twitter quiz format limitations (limited answers, no revisions)
• Example of a particularly difficult question posed by "Tenten" from Japan
• Analysis of why some questions may seem unfair or too easy
• The Go language and its behavior when iterating over a string
• Invalid UTF-8 characters and the "broken rune" or Unicode FFFD character
• The encoding of 16-bit values in Unicode and requiring three characters
• Quizzes that test understanding of the language and its quirks, including code that doesn't compile
• Writing mangled source code to fool others
• Purpose of pop quizzes as an educational tool
• Iterating over strings and their surprising properties in Go
• Unicode and time zone handling in programming languages
• Break statement behavior across different languages
• Commonly overlooked areas in programming (e.g. Unicode, time zones)
• Creating quizzes to test knowledge and catch bugs
• UTF-8 is the assumed default text format
• Many languages still use older encoding systems like ASCII and EBCDIC
• Java uses UTF-16 with surrogate pairs and encoding hacks to handle Unicode characters larger than 16 bits
• Python and Ruby have different handling of encodings, treating them as a property of the string
• Go handles text in a straightforward manner without these complexities
• Programmers coming from other languages may bring preconceptions about how things work
• Quizzes and exercises can help break down these misconceptions and teach new ways of thinking
• The speaker shared a personal anecdote about being convinced that a solution he thought was right wasn't, after trying to implement it in Go
• The challenges of creating unambiguous pop quizzes
• Importance of asking questions in an edge-case-specific way
• Difficulty of running code for certain programs, especially those with edge cases
• Comparison between "got it right" or "got it wrong" and focusing on the lesson behind a quiz
• The competition aspect of writing the shortest version of a program
• Simple quizzes that start with the same form, such as "what does this program print?"
• Printing being the simplest thing in programming and the idea that all other programs are more complicated
• The limited space of the quiz area, focusing on very specific types of problems (programs printing one value)
• The author discusses the benefits of showing quizzes to large groups, citing Linus' principle that "given enough eyeballs, all bugs are shallow"
• A personal anecdote is shared about a quiz on greedy regular expressions in a local Python group
• The value of explanations and counterexamples in learning and teaching is emphasized
• Josh Bloch's Jet Java Puzzlers book is mentioned as an inspiration for the author's approach to quizzes and explanations
• The author reminisces about creating Go present slide decks, which involved revising and refining content over time
• The use of "frowny face" as a valid identifier in programming
• Pop quizzes being used in job interviews and their potential unfairness
• The power imbalance in pop quiz-style questions, where the answer is predetermined by the question writer
• The lack of educational value in multiple-choice pop quizzes
• Negative one-letter values and their explanation
• Rune type as an alias for int64 in Go
• Translucency of rune, byte, and uint8 types
• Rune characters and strings vs bytes
• Pop quizzes as a poor interviewing tool
• Teleport access plane and its features
• Teleport options (cloud, self-hosted, open source)
• Critique of whiteboard coding interviews
• Argument that such interviews are artificial and stressful for candidates
• Comparison to real-world work environments
• Proposal to replace whiteboard coding with practical tasks in a simulated environment
• Pop quizzes as a fun social activity vs. stressful interview scenario
• Perspective of interviewer vs. interviewee on pop quizzes
• Pros and cons of using pop quizzes in an interview process
• Pop quizzes as a tool for language learning
• Voluntary vs. involuntary use of pop quizzes
• Discussion of teaching methods, including the importance of giving students something to think about at the end of a lesson.
• The use of quizzes as a learning tool, believed to be beneficial for encouraging exploration and fun.
• Concerns that too much focus on achieving 100% on a quiz can create a frustrating experience and make learning feel like a chore.
• Preference for the format of in-person meetups or classes over online formats, citing its effectiveness in promoting discussion and engagement.
• The value of having opposing views and dialogue in learning
• Comparison between traditional interviewing style and a more collaborative approach like Heptio's interview process
• Benefits of showing thought process and work during interviews
• Artificiality of team interviews but closer to real discussions than traditional interviews
• Importance of discussing code and trade-offs in real-time rather than just presenting solutions
• The concept of "innovation tokens" by Dan McKinley, where you have a limited number of tokens to try new things and avoid being stuck in the same old ideas.
• The importance of seeking out new voices and perspectives in your field, rather than just relying on established speakers or popular ideas.
• The idea that most successful products or technologies take around 10 years to gain traction and become widely used, with a "wilderness period" before they reach mainstream success.
• The value of perseverance and patience in building a product or technology, as it takes time to build up knowledge and community around it.
• The importance of past struggles and failures for future success
• The concept of "maturity" as blood, sweat, and complexity divided by time
• The Go programming language's history and development process
• The creation of test cases to prevent compiler bugs from recurring
• The tension between learning new technologies quickly vs. waiting for others to mature them
• Australia's adoption of Go for log processing due to specific performance issues
• Trade-offs between sticking with tried-and-true languages vs taking risks with new ones like Go
• Need to balance risk and budget in technological decisions
• Concurrency benefits of using Go in backend systems, such as those at GitHub
• Challenges of staffing teams with expertise across multiple technologies
• Importance of having a set of established and emerging technologies in the stack for discussion and decision-making
• Importance of separating personal and professional social media accounts
• Pros and cons of including social media links on a CV, particularly in tech industries
• The idea that sharing technical knowledge on social media can be beneficial for learning and career growth
• The challenge of balancing sharing online with maintaining a healthy work-life balance
• Using social media as a platform to teach and share technical knowledge, such as through quizzes or interactive challenges
• Discussing the creation and sharing of quizzes at meetups
• Sharing opportunities with ACM for teaching and educating about new topics
• Goal is to educate, not just test knowledge with perfect answers
• Thank you for participating in a short-notice meetup
• Future episode featuring John, Chris, Peter Bergen, and Tim Heckman on Ghost controversy
• Sponsorship information (Fastly, LaunchDarkly, Linode)