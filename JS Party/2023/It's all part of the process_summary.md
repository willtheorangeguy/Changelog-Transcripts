• PR etiquette and best practices for open source projects
• Importance of clear descriptions in pull requests
• Communicating change effectively through code reviews
• Managing reviewer count and ensuring efficient review processes
• Rollback strategies for large-scale production codebases
• Approaches to merging pull requests, including auto-merge on GitHub
• Considerations for different types of changes (e.g. data migrations)
• Applying feedback and iteration in the development process
• Effective code review involves being nice and not a jerk
• Asking questions about intent is crucial for understanding the code change
• Reviewers should aim to catch their own mistakes by reviewing their own PRs first
• Linting and styling issues can be resolved before reviewing the PR, and arguing over them in comments can be unproductive
• Breaking up complex changes into smaller parts and adding notes about intent and content can help reviewers focus on key areas
• Utilizing tools like Graphite or Reviewable to enhance review processes can be helpful
• Scheduling synchronous reviews with the team for large change sets can improve efficiency and feedback
• Codifying levels of feedback (e.g. blocking, recommended, nit) can clarify importance and help reviewers focus on critical issues
• GitHub PR states (insufficient, yes/no, or nothing)
• Automating review tasks such as checking unit tests and code coverage
• CI system versus PR review for stylistic checks and other tasks
• Project maturity and ability to automate tasks
• Enforcing code quality through bots and automated comments
• Balancing CI system complexity with build time and cost
• Continuous deployment vs. continuous integration
• Automated releases and their potential risks
• Continuous deployment as the healthiest model
• Decoupling deployments and releases with feature flags
• Benefits of frequent deploys for bug fixes and risk reduction
• Feature flags as a glorified boolean check, used for hiding work-in-progress or testing new features
• Use cases for feature flags include experimentation, beta testing, and kill switches
• Difference between user-controlled and engineering-controlled feature flags
• Role of SDKs and services like LaunchDarkly in managing feature flags
• Integration with A/B testing and experimentation
• Best practices for creating tickets and interacting with them
• Importance of including sufficient detail in a ticket
• How to determine if a ticket has enough information for anyone on the team to pick it up
• Value of labeling "done" and accepting criteria in a ticket
• Common issues with bug reports, such as lack of reproducibility or proprietary code
• Use of forms and issue templates in bug reporting
• Types of updates that make sense to post back to a customer-reported issue
• Importance of communication and updates throughout the resolution process
• The importance of providing updates on urgent issues to customer support teams
• Using tickets or issues as a central location for communication and updates
• Keeping a log of progress and updates in the ticket itself, especially for complex tasks
• The use of draft PRs as a way to share updates and get feedback from the team
• Debating whether to use "ticket" or "issue" to describe a piece of work, with no clear consensus
• Importance of thinking about software as a social sport to improve communication and collaboration
• Contribution to open source projects by employees is key to adopting best practices and norms from businesses and enterprises
• The need for more contributors, maintainers, and investment in the open source ecosystem to ensure its security and stability
• Code reviews are an inefficient form of code review (jokingly)