• Deciding when to do a big refactor
• Types of refactoring (code smells vs functionality/requirement)
• Decision-making process for refactoring large projects
• Identifying areas of the codebase that need refactoring
• Emotional vs. practical reasons for refactoring
• Balancing between over-refactoring and not refactoring enough
• Refactoring code vs. rewriting it from scratch
• Distinction between "new requirements" and "code smells"
• Justification for refactoring: is it worth the time and effort?
• "New hotness" vs. using new tech only when necessary
• When to use a refactor versus a total rewrite
• Refactoring vs rewriting: definition of refactoring as making small, incremental changes to the codebase, while rewriting involves creating a new, complete implementation from scratch
• Time constraints: rewriting requires significant time and resources, whereas refactoring can be done in smaller chunks
• Loss of learnings: rewriting loses the historical context and linear history of the codebase, but can also incorporate lessons learned into the new implementation
• Importance of testing: tests are crucial for successful refactoring, as they help ensure that changes do not break existing functionality
• Approaches to refactoring:
  • Isolating the piece being refactored
  • Writing tests to cover use cases and document the refactoring process
  • Refactoring in phases to avoid "going down rabbit holes"
  • Using test-driven development as a guiding principle for refactoring
• Refactoring codebases incrementally through small commits and pull requests
• Importance of preserving Git history during refactoring
• Review process and feedback on large PRs
• Use of feature branches and their potential drawbacks
• Separating tests from code refactorings
• Incremental approaches to refactoring, including the walled garden approach
• Avoiding squashing multiple commits into one, especially in large projects
• Refactoring packages in large web applications
• Managing bundle size and dependencies in Node.js
• Implementing bare imports for optional functionality
• Using paired functions for safe and unsafe operations
• Layering APIs and refactoring internals for performance benefits
• Migrating between front-end frameworks (e.g. React to Angular)
• Challenges of framework migration, including component-level migration
• Benefits of small modules in refactoring, including easier adoption of new libraries
• Challenges of maintaining large applications with many small components
• Difficulty of refactoring due to potential implications throughout the entire system
• Fragmentation in the JavaScript ecosystem as a result of frequent breaking API changes
• Comparison with Python's approach to breaking changes and their impact on the ecosystem
• Advantages of fragmentation, allowing for easier updates to new versions of libraries
• Influence of JavaScript's web origins on its design decisions, particularly regarding backwards compatibility
• Kevin Ball discusses his approach to learning and growth, which involves setting up commitments and habits to force himself into patterns of progress.
• Divya Sasidharan talks about her strategies for managing anxiety and procrastination, including writing down tasks and breaking them down into micro-tasks, as well as committing to daily blogging through micro-blogging.
• Feross Aboukhadijeh shares his pro tip on incorporating small habits of learning into daily workflow, and provides a concrete suggestion of using bash aliases or similar shortcuts for frequently used commands.
• GitHub Actions automates tasks
• Winner-take-all effects can lead to disproportionate benefits from small improvements (1%)
• Cumulative advantage and winner-take-all effects increase productivity and success over time