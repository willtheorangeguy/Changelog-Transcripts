• Discussion about the upcoming podcast episode on Node.js and security
• Introduction of guests Adam Baldwin (head of security at npm) and Christopher Hiller (aka BoneSkull)
• Explanation of how the podcast episode was requested by a listener over a year ago
• Discussion with Adam Baldwin about recent news that his team joined npm as their internal security team
• Adam Baldwin shares his first contribution to open source, a fix for a cross-site scripting bug in the npm registry
• Conversation about common types of vulnerabilities and how they can vary across different ecosystems
• Discussion about Node.js-specific security concerns due to its asynchronous nature and shared client-server codebase
• npm 6 announcement mentions concern about security of open source code
• Developers tend to trust security of open source code more than their own code
• Two extremes of programmer mindset: trusting own code and completely relying on others' code
• Difficulty in automating static analysis of JavaScript code, requiring human validation
• Discussion of using TypeScript for improved safety and strong types
• Schrödinger's npm: a concept where developers are not given information about vulnerabilities until they're necessary to know
• Improved npm audit with actionable security alerts and guidance for developers
• Plans to support registry mirrors with audit features through API documentation
• Continuous integration (CI) as the ideal place to run npm audit for better results
• Actionable mitigation steps, including updating dependencies without breaking semver contracts
• Addressing transitive dependency issues and chain of PRs needed for updates
• Future tooling and security-focused plans within npm, including improved application security practices and infrastructure.
• Internal audits are now being done by npm
• PGP signing packages is a new feature in development
• Plans for publisher signing are underway, but no timeline has been set
• npm-audit is still under development and lacks confidence-level indicators for thoroughly audited packages
• Native modules require fuzzing to ensure security, due to unique vulnerability types
• Context matters when evaluating the severity of a vulnerability in dependencies
• Suz Hinton discusses her idea for a project involving a network of small circuit boards with microcontrollers and OLED screens that can communicate with each other.
• The project is open-source, allowing others to use the design as a building block for their own projects.
• The circuit boards would be extensible and could take in environment input from sensors.
• Jerod Santo suggests using it as a mood ring-like device that measures bodily functions.
• Christopher Hiller shares his idea of making a roguelike video game with stealth elements, and Jerod Santo suggests involving his 6-year-old daughter in the project to create unique art assets.
• Adam Baldwin proposes an experiment to build an interface where typing sentences in Morse code is translated into another sentence through timing.
• Discussion of learning Morse code and its practicality in a hypothetical emergency
• Idea to create an Alexa skill for the Changelog's "JS Party" podcast
• Complexity and time constraints of building a custom API for the Alexa skill
• Alternative solution: using an existing service that integrates with podcasts and Alexa
• Adam Baldwin's comments on security discussions and community engagement