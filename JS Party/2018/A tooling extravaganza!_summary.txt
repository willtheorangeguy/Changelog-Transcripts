• Build tooling in JavaScript
• Modern build setup: Babel, Webpack, Rollup, Parcel
• Legacy tools: Gulp, Grunt
• Transition from Gulp/Grunt to modern tools
• Evolution of dependency management and analysis
• Comparison of Broccoli and Webpack
• Broccoli was discussed as a build tool that excelled in speed due to its dependency tree caching mechanism
• Webpack was criticized for being slow with certain assets, such as Sass compilation
• HappyPack was mentioned as an attempt to implement Broccoli's caching mechanism on top of Webpack
• Turning off minification in dev mode was suggested as a way to improve development speed
• The debate between Grunt and Gulp was revisited, with both sides sharing their opinions on the matter
• Framework-specific CLIs were discussed as being mostly wrappers around existing tools but providing value through conventions and ease of use for beginners
• The trend towards framework-specific CLIs and whether they will have a lasting impact on build tooling was debated
• The possibility of a Webpack killer, such as Metro or Parcel, was discussed
• Definition of "eject" in Create React App
• Evolution of build tooling and module management in JavaScript
• Potential for build tooling to become less of an issue as transpilation becomes transparent
• Discussion of CLI vs server-based build tools
• History and comparison of CommonJS, AMD, and UMD module systems
• Current use and recommendations for linters (e.g. ESLint), formatters (e.g. Prettier), and type checkers (e.g. Flow, TypeScript)
• Discussion on Prettier and ESLint usage in development
• Challenges with adopting new tools and setting up configurations
• Use of Airbnb defaults for ESLint and Prettier configuration
• Custom rules creation with ESLint for specific use cases
• Functional testing with Selenium, WebDriver, and Cypress.io
• Value of QA teams and manual testing vs. automated functional testing
• Difficulty in hiring skilled testers due to overlap between engineering and QA roles
• The importance of gradual releases to prevent widespread issues
• Comparison of Jest/Enzyme testing with traditional browser testing
• Discussion of Continuous Integration (CI) tools and their usage at Stripe
• Differences between CI in open source vs. business environments
• Stripe's use of Jenkins and other CI tools for automated testing, building, and deployment
• The role of a dedicated team in maintaining and optimizing the CI pipeline
• Discussion of Continuous Integration (CI) tools for Mocha
• Use of Travis CI and AppVeyor for CI testing with multiple versions of Node
• Publishing artifacts to S3 for debugging purposes
• Comparison of IDEs, including Vim, VS Code, and Atom
• Discussion of plugins and configurations for Vim and VS Code
• Mention of collaboration features in VS Code
• Vim vs Neovim discussion
• Yarn vs npm comparison and opinions on their strengths and weaknesses
• Trade-offs between Yarn and npm (speed vs consistency)
• History of Yarn and its impact on the npm team and ecosystem
• Final advice: use whatever package manager works for you, or try switching to see which one suits your needs better