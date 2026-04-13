• The importance of testing in Go programming
• Understanding the point of testing: to describe code promises and ensure functionality
• Unit tests as a way to verify function behavior
• Test coverage and its role in ensuring software reliability
• Limitations of 100% code coverage, including the risk of over-testing and brittle code
• The need for balance between testing and development to avoid over-engineering
• Understanding test coverage: it's not just about touching all lines of code
• Unit testing vs integration testing
• Definition of integration testing: within-project components working together, vs external services
• Integration testing as a combination of functional and non-functional testing
• Challenges of integration testing due to project-specific dependencies and scales
• Balance between mocking/stubbing and actual integration testing with live traffic
• Canary deployment as a method for continuous testing in production
• Recording real HTTP traffic as test files
• Using "golden files" to save test results and assume they're correct if the tests can't run with the actual services
• Advice for testing in Go, including:
  • Running integration tests less often than unit tests
  • Using flags to select which tests to run
  • Separating main binaries for exercising the system vs. unit testing
• Handling flaky tests and dependencies that change over time
• Flaky tests can damage testing culture
• Strategies for dealing with flaky tests (e.g. isolating them, labeling as flaky)
• Reasons why tests may be flaky (e.g. concurrency issues, non-determinism)
• Importance of testability in design and API development
• Trade-offs between usability, testability, and maintainability
• Challenges of testing concurrent code and global state
• TDD (Test-Driven Development) and its applicability
• Different approaches to designing and implementing APIs
• The importance of testing and validation in software development
• Risk assessment and the impact of code on business operations
• Personal preferences and philosophies on coding practices
• Balancing TDD with other design considerations and realities
• Design emerges from document-driven development
• Behavior-Driven Development (BDD) discussed as an alternative to Test-Driven Development (TDD)
• Concerns about BDD's effectiveness and limitations
• Importance of consistency across the codebase when choosing a testing approach
• Discussion of using standard library versus external frameworks for testing
• Discussion about avoiding third-party packages for testing in favor of the standard library
• Mention of testify package as an example of a popular testing framework
• Debate on whether assert-style functions should be included in the Go standard library
• Concerns about adding opinionated APIs or features to the standard library
• Discussion of table-driven tests and their benefits, including ease of use and encouragement for more cases to be added
• Problem with table-driven tests: difficulty in running specific input cases
• Alternative approaches to avoid this problem: using maps instead of slices, naming test cases, and using subtests
• Best practices for writing table-driven tests: separating test cases, using check functions, and returning teardown functions from setup functions
• Discussion on the evolution of error handling in Go: from os.Error to an interface
• Comparison of setup and teardown facilities: TestMain vs. custom setup/teardown functions
• Concerns about global state in testing
• Dangers of abuse with global state
• Importance of context in writing test code
• Different testing needs depending on project complexity
• Need for good testing philosophies and care for test code