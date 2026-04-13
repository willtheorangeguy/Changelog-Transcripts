• Introduction and banter between hosts and guests
• Josh Goldberg introduces himself as an open-source maintainer, contributor, and author of "Learning TypeScript"
• Discussion on the process of becoming an author for Josh Goldberg's book
• Guest Christopher Hiller shares his views on TypeScript, preferring JavaScript with docstrings instead of TypeScript
• Technical discussion on using types in Node.js development without compilation steps
• Christopher Hiller wants to use TypeScript as a linter without compiling code
• Josh Goldberg suggests creating an inverse compiler to compile JavaScript into TypeScript and then run ESLint on it
• The group discusses the difference between compilers, transpilers, and linters
• Josh Goldberg shares his experience with funding himself through open source contributions
• He emphasizes the importance of planning and preparation for a successful open source career
• Kevin Ball asks about Josh's long-term goals for sustainable funding as a full-time open source developer
• The challenges of relying on GitHub Sponsors as a primary source of income
• The benefits and drawbacks of doing open-source work full-time
• The experience of having a company sponsor open-source projects and the importance of community involvement
• The value of sustainably-funded, popular open-source projects and their impact on software development
• The complexities of navigating relationships between companies and open-source communities
• TypeScript ESLint is an open-source project that allows ESLint to lint TypeScript code
• It was initially created as a bridge between ESLint and TypeScript, providing custom ESLint rules and parsing TypeScript syntax
• The maintainer crew includes James Henry, Brad Zacher, Armano2, and Josh Goldberg
• TypeScript ESLint has taken over from TSLint as the primary linter for TypeScript code due to its ability to reuse ESLint infrastructure and features
• It has a performance issue with some configurations taking up to two minutes to run, which is being addressed
• The project still needs to figure out its JavaScript story, including using TypeScript type checker APIs in JavaScript files
• Performance and configuration issues are the main reasons people haven't moved to TypeScript ESLint from TSLint
• TypeScript's performance can be a slowdown for large codebases with many dependencies
• The project builds on ESLint by creating an adapter between TypeScript and ESLint using abstract syntax trees (ASTs)
• The ASTs used by TypeScript, ESLint, and the TypeScript ESLint parser are different and require translation between them
• The project is still early in its development and is working to improve performance and documentation
• Many rules in the TypeScript ESLint parser have yet to be established as "banner headline" rules with clear recommendations for usage
• The difference between ESLint and Prettier, with Josh recommending to use separate tools for formatting and linting
• Annoying lint rules that block code from building, such as unused variable checks in Create React App
• The importance of being in control when using lints, with the ability to disable rules as needed
• Philosophical discussions around how to choose which lint rules to use and when to implement new ones
• Typescript's 99.9% error certainty vs ESLint's probabilistic approach to error detection
• Customizing ESLint rules for specific team needs and company styles
• Suppression comments in ESLint and the idea of giving users feedback on disabling rules
• Teaching strategies for introducing complex concepts, including introducing one major concept at a time and using clear language
• Using graph theory to determine the order of teaching topics and explaining why certain concepts are important
• The importance of clarity in error messages and documentation
• Iterating on educational content based on user feedback and revising it as needed
• Repeating ideas from different perspectives to provide depth and understanding
• Revamping teaching methods to make complex topics easier to understand
• Benefits of interactive examples and hands-on projects for learning
• Challenges of creating interactive content in book format
• Importance of being able to explain technical concepts to non-technical people
• Value of conference-driven development (submitting talks on unfamiliar topics) as a way to learn and teach others