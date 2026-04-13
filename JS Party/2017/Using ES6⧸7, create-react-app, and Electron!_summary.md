• Introduction of JSParty and its hosts
• Discussion of the hosts' recent vacation and being temporarily replaced by others
• Topic for discussion: using ES6 and ES7 features, trade-offs, and specific features rather than "buckets"
• Rachel shares her limited experience with new language features, mentioning arrow functions and template literals
• Alan discusses his disagreement that arrow functions make code more readable, citing issues with implicit returns and patterns
• Discussion of the use of arrow functions and their impact on readability in larger systems
• Semantics of arrow functions and lexical scope
• Complexity reduction by avoiding older syntax
• Debate over defaulting to arrow functions or traditional functions
• Pitfalls of using class syntax with implicit returns
• Ambiguity between lexically bound functions and unbound functions
• Potential gotchas when using class syntax with arrow functions
• Discussion on the new rules and classes in programming
• Lexically bound ambiguity and its elimination
• Use of compilers for legacy browser support
• Babel as a tool for compiling code to ES5 or older versions
• Adoption rates of newer features like object spreads and array spreads
• Debate over whether it's worth using a compiler for modern browsers that support new features
• IoT projects and JavaScript usage
• Common JavaScript features in frameworks like Vue, React, and Ember
• Features not widely used or accepted
• Issues with implementing modules in Node due to conflicting specifications
• Proxies as a feature that is not well-suited for current use cases
• Metaclasses and similar concepts being discouraged in favor of other approaches
• Proposals in the language spec that may not gain traction
• Decorators: Their use and potential for simplifying code, but also possible overcomplication
• Comparison between function components and class components in React
• Create React App: Its purpose, features, and benefits for managing a React project with ease
• React CLI tools and the suggested set of tools for building a React application
• Create React App was created to address feedback about lack of supported tools working together
• It started as a hackathon project and has since grown into a robust toolset with its own configuration and build system
• The toolset includes ESLint, Webpack, CSS, and Babel configurations that are hidden from the user to ensure compatibility and ease of use
• Users can either stay within the defined boundaries and receive updates or "eject" and configure their project manually
• A key feature in Create React App's 1.0 release is its integration with Webpack 2, which natively supports imports and exports without requiring Babel compilation
• This change allows for improved static analysis and better optimization of bundle size and tree shaking
• The speaker is discussing a platform or tool that has its own primitives and module system, similar to Node.js
• They are reframing their thinking about this tool and finding it interesting because it crosses boundaries of old tools
• The tool is compared to being like "grunt" or "babble", but also acts as a piece of glue between different systems
• It needs to understand ES6 modules natively in order to perform tasks like tree shaking
• The speaker mentions reading about updates to React and Create React App, including the addition of new features to JEST
• JEST is discussed as a testing framework that allows for unit tests and functional style tests without needing a browser
• It's mentioned that JEST has become a default choice for testing due to its support from Facebook
• The speaker highlights new features in the latest release, including immersive watch mode, better snapshot format, and automatic coverage reporting
• They also discuss how Create React App now includes JEST by default and provides a test directory with a test already written
• Finally, they touch on the issue of writing tests in the same JavaScript as components while using Babel and Webpack.
• Discussion on a framework's caching strategy and service worker implementation
• Fears of accidentally caching everything without a way to break out
• Service workers in React and how they can automatically update components
• Content Security Policy (CSP) as a default feature in Ember CLI
• Toolkit-style CLI helper features for solid generic defaults
• Distinguishing between a boilerplate generator and a living, evolving tool
• Comparison of create React app to Rails scaffolding
• Code splitting with Webpack
• Dynamic imports with async/await syntax
• Standards track for asynchronous imports
• Create React App support for code splitting
• Reducing JavaScript bundle size for PWAs
• Standardizing configuration for React apps
• Comparison to Ember CLI and Glimmer updates
• Future goals for frameworks: compiling to modern features, not ES5
• Current limitations in compiler performance benefits for developers
• Configuring Babel settings to optimize compilation and target features
• Trade-offs between development ease and performance considerations
• Electron project as the current topic of discussion
• Overview of Electron, its history, and key features
• Examples of successful applications built with Electron, including MongoDB's DB admin tool and Voltra music app
• Comfort level with Node.js and Electron
• Differences between building web apps with Node vs Electron
• NPM modules and their accessibility in Electron
• Cross-browser environment for running HTML in headless mode
• Comparison of Adobe Air/Flex and Electron
• Discussion on the benefits of using desktop applications, including increased engagement and attention
• Discussing the desktop's continued value
• GitHub's desktop apps and their transition to Electron
• Experience with moving from native applications to Electron
• Webpack 2 features, specifically tree shaking
• Critique of tree shaking as a crutch for bad coding practices
• Tree shaking benefits in certain situations
• Introduction of new project (CodeSomething) that optimizes code at compile-time
• Use of minifiers and multiple tools for optimization
• Discussion of immutable data structures and functional programming
• Recommendation of an Anjana Vakil talk on JS Confu about immutable data
• Discussion of immutable data structures and the ECMA spec
• Recommendation of the book "Hackers" by Steve Levy as a resource for learning about early hacker culture
• Description of the book's three parts, including its focus on the Tech Model Railroad Club at MIT, the homebrew computer club, and the gaming industry
• Mention of an appendix titled "The Last Hacker" which explores Richard Stallman's role in hacker culture before the GNU project
• Discussion of other resources for learning about early hacker culture and tech movies that hold up well
• Bandwidth partner: Fastly.com
• Episode editor: Jonathan Youngblood
• Theme music producer: Breakmaster Cylinder
• Closing remarks and thanks for listening