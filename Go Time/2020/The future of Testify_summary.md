• Testing frameworks and their role in Go
• Controversy surrounding testing frameworks in Go
• Different types of testing frameworks (e.g. assertion libraries, frameworks like Ginkgo)
• Trade-offs between different testing frameworks (e.g. simplicity vs. structure)
• The history of Testify and its purpose
• Overview of the testing process in code
• Use of testing frameworks to improve code quality through automated tests
• History of Testify and its early adoption
• Purpose of Testify: to simplify test writing and save community time
• Comparison of Assert and Require packages in Testify
• Benefits of using Require package over Assert package
• Discussion of the automated generation of Require by inspecting Assert
• Design decisions and trade-offs in creating Testify
• Testify wraps the testing tier and is similar to global functions
• Behavior-driven tests (BDD) are discussed as an alternative style of testing
• BDD uses natural language to describe test cases and can be more readable than unit tests
• BDD focuses on user behavior, whereas TDD is more technical
• Property-based testing generates random inputs to test functions and find edge cases
• Fuzz testing/fuzzing is mentioned as a method for testing code with unexpected input
• Fuzz testing of user input with Plush library in Buffalo project
• Discussion on mocking external resources (databases, etc.) for unit tests
• Importance of code coverage and debate around 100% vs. 90% coverage
• Mark Bates' approach to database testing: using a real database instead of mocking or stubbing
• Integration testing vs unit testing and mocking
• Importance of context in determining the right approach
• Using interfaces for abstraction and mocking out complex dependencies
• Techniques for mocking databases and third-party services
• Use of mini-mocks and default implementations to control time and ENVs
• Discussion on whether to assert implementation details in mocks
• Time manipulation in dynamic languages
• Maintaining a project like Testify (size, popularity, community requests)
• Balancing feature addition vs. API complexity
• Edge cases and assertion libraries (Testify's strengths and weaknesses)
• "Good enough" attitude towards software development
• Community ownership and inclusiveness in open source projects
• Pros and cons of a large API in Testify
• Potential for API tightening or v2 release
• The conversation begins discussing ways to write unit tests, specifically using strings.Contains() instead of equals().
• Boyan Soubachov mentions that Testify is due for a version 2, citing breaking change requests and a desire to simplify the API.
• A survey has been created on Google Forms at cutt.ly/testify to gather community feedback on what changes or features to include in version 2.
• Mark Bates jokingly suggests removing certain functions from Testify, including Require and Assert.
• Boyan Soubachov shares an unpopular opinion that change can be overrated, and sometimes it's best to leave things alone due to the reliability and positive feedback of code that rarely changes.
• The conversation devolves into a humorous discussion about timezones and Mark Bates' suggestion to remove them.
• Discussion of Unix time as a measurement alternative
• Apple Watch capabilities and custom watch face limitations
• Possibility of displaying Unix time on an Apple Watch through complications
• Limited usefulness of Unix time due to its expiration in 2038