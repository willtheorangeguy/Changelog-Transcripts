• Discussion of returning guests Christopher Hiller and Josh Goldberg
• Josh Goldberg's background and work on TypeScript ESLint and Mocha
• Modernization of Definitely Typed project using dprint
• Comparison of Prettier and dprint, including speed differences
• Changes to ESLint configuration (flat config) and its impact
• Overview of the latest developments in TypeScript ESLint
• ESLint has introduced a new config format called "flat config" in version 9
• The old config format was soft-deprecated in version 8 and is not supported by default in version 9
• The main issues with the old format were:
	+ Confusion around how to handle extended configs versus overrides
	+ Subtle weirdnesses when referencing plugins, especially for ECMAScript modules
	+ A convoluted and hard-to-maintain system that required significant resources
• The new flat config format is considered a more modern and maintainable solution
• Some users are experiencing difficulties with the transition due to:
	+ Lack of communication about the change and its reasons
	+ Plugin authors not having updated their plugins to support the new format
	+ Users not understanding why the change was necessary
• Adoption and support for ESLint with TypeScript
• Confusion over flat config support and ESLint version support
• Challenges of supporting new syntax in TypeScript and keeping up with both projects
• Internal workings of TypeScript ESLint (converting TypeScript AST to ESLint)
• Implementation of rules in TypeScript ESLint, including navigating the abstract syntax tree
• Existence and creation of plugins for TypeScript ESLint
• ESLint plugin and parser basics
• Biome and its simplified configuration approach compared to ESLint
• Standard setups for TypeScript projects, including Create TypeScript App
• Evolution of ESLint preset configs based on user feedback and trends
• Strict vs. recommended lint rules and examples of rules that are too onerous or unpopular
• User interaction with linter rules and disabling them with comments explaining the reason
• ESLint rule disabling analysis and potential for creating a new rule
• ESLint Comments plugin for enforcing good practices around ESLint comments
• Proliferation of tools for resolving issues in linting and configuration
• Create TypeScript App and the need for a modern, general-purpose scaffolder
• Template maintenance and updating issues with existing solutions
• Discussion of the with statement in JavaScript and its uses
• Restricting scope using the with statement
• Shadow realms (TC39 proposal) and their relation to the with statement
• Disuse of the with statement due to deprecation concerns
• TypeScript adoption and support for the with keyword
• Tooling flexibility and importance of supporting non-standard use cases
• Typed linting in ESLint and its limitations compared to other linters
• Difficulty of implementing type-aware linting using JavaScript and ESLint's architecture
• Future developments and challenges in integrating typed linting with other linters
• New way of setting up type linting using parseroptions.projectservice (project service)
• Project service vs language server: they use same APIs but serve different purposes
• Benefits of project service: easier, faster, and more correct setup for type linting
• Request for feedback on how to explain project service option in documentation
• Discussion about SquiggleConf conference on dev tooling, hosted by Josh Goldberg
• Boston conference experience for attendees with dietary restrictions
• Squiggleconf.com and its use of Astro framework
• User research through conversations at Squiggleconf
• Mocha testing framework: history, features, and challenges as a maintainer
• Burnout and maintenance challenges in open-source projects
• Plans to improve Mocha, including supporting aggregate errors
• Discussion of future plans for Mocha
• Rewriting the Mocha website and improving user experience
• Adding support for alternative runtimes (e.g. Bun, Deno)
• Providing a way to mock modules in Mocha
• Exploring use cases for loaders in ESM (ES Module) development
• Alternatives to Jest for testing in Node (e.g. Vitest, tsimp/tsx/tsnode)
• Discussion of Jest and Mocha as testing frameworks, with Jest being preferred due to its simplicity and ease of configuration
• Importance of code coverage and the challenges of achieving it with parallel runs or across different tools
• Josh Goldberg's personal preference for using Vitest for unit testing and end-to-end testing
• The need for a reliable way to merge services and achieve seamless integration between different testing frameworks
• Josh Goldberg's future plans, including stabilizing TypeScript ESLint V8, splitting out the Create TypeScript App into separate projects, and converting JavaScript code to TypeScript with his tslift tool
• Challenges of developing tools that can convert or migrate code between different languages or versions
• The potential for AI to be used as a last resort in solving complex coding problems
• Use of AI to generate code and improve it through feedback loops
• Limitations of AI in solving complex coding issues
• Benefits of using AI-assisted tools for specific tasks such as working with ASTs
• Challenges of using AI when working on less common tech areas
• Introduction to TypeScript ESLint v8 project service and preset shareable configs