• Listener request on evolving alongside JavaScript syntax
• Discussion on adopting new syntax and tooling
• Nick Nisi: adopts new syntax when ESLint can parse it out of the box without build tools
• Feross Aboukhadijeh: also conservative, but uses compilation tools to support new syntax
• Jerod Santo: somewhere in the middle, not opposed to tooling, but waits for compelling reasons to change
• History of JavaScript syntax: ECMAScript edition 3 (1999), abandoned ES4 due to complexity issues, ES5 published in 2009
• ES5 and ES6/ES2015 confusion
• Babel's role in transpiling ES6 code to ES5-compatible code
• Yearly cadence of new ECMAScript standards (e.g., ES2020, ES2021)
• Differences between function and arrow functions syntax
• Hoisting behavior of function and arrow functions
• Choosing between function and arrow functions based on specific needs
• Discussion on the arrow function syntax in JavaScript and its optional aspects
• Complexity of the syntax with multiple versions (zero argument, one argument, multi-argument) and rules for using parentheses and curly braces
• Debate over whether to use `const` or `let` for variable declaration, with some preferring `const` for safety and others preferring `let` for efficiency
• ES6 features in JavaScript, including classes, template literals, and default parameters
• Debate about "There's more than one way to do it" (TMTOWTDI) mindset and whether it leads to bikeshedding or flexibility
• Importance of consistency in code style and the use of tools like formatters (e.g. `go fmt`, Elixir's `mix format`)
• Discussion of variable declarations (`var`, `let`, `const`) and how they coexist due to historical reasons, rather than design choice
• Critique of arrow functions syntax with multiple variants and their potential for confusion
• Destructuring assignment in JavaScript
• Modules and importing in ES6
• Transitioning codebases to new syntax (e.g. from ES5 to ES6)
• Standard: an opinionated ESLint rule set for enforcing coding style
• Prettier: a tool for forcefully formatting code
• Updating API callbacks to promises
• Transitioning from ES5 style prototypes to class syntax in JavaScript
• Strategies for upgrading codebases to modern JavaScript features, including manual refactoring vs relying on tools
• Template strings and their benefits, with discussion of potential drawbacks (e.g. additional ways to create strings) and use cases (e.g. multi-line strings)
• Common tags and tagged templates as a way to simplify working with template strings
• Discussion of multi-line string handling and features in JavaScript
• Disadvantages of private properties and classes, with Feross Aboukhadijeh expressing concern over limiting user flexibility
• Features not used or underutilized by Feross Aboukhadijeh, including generators and symbols
• Feross's new app, Virus Cafe, a platform for two-minute video chats between strangers on deep questions
• Challenges of balancing openness with moderation in social apps
• UI/UX considerations and the importance of subtle social cues in differentiating social apps
• App anxiety due to uncertainty about what happens when tapping "start"
• Feedback from users indicates they're dropped into a chat without explanation
• Users report having great experiences on the app, with some using it for 12 hours or more
• An audio-only mode is being added based on user feedback and behavior (blocking cameras)
• Conversations have revealed that people feel comfortable sharing personal stories when their camera is blocked
• The tech stack includes Next.js, React Hooks, Chakra UI, WebRTC, and WebTorrent for P2P connectivity
• Discussion of WebRTC and its complexities
• Use of SimplePeer library for simplifying WebRTC API
• Importance of relay servers (TURN/STUN) in WebRTC applications
• Open-source project status (not open-source yet)
• New font "FiraCode" and its ligature feature
• Personal experiences with coding fonts and switching to FiraCode
• Ligature fonts display multiple characters as a single glyph
• iTerm2 disables GPU rendering when ligature support is enabled
• Kitty terminal emulator supports ligatures in a fast way
• Terminal.app compatibility with ligatures is unknown
• Cursive letters and italics are not rendered by ligature fonts