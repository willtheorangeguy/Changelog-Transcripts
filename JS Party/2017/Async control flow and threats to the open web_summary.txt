• Async Flow Control
• History of async programming in JavaScript (callback, promises, generators)
• Problems with early async implementation (callback hell)
• Evolution of async solutions (Backbone, Promises A)
• Current state of async programming in JavaScript (standardization, tooling)
• Managing state over time is a complex problem in modern JavaScript applications
• Asynchronous programming can lead to "callback hell" and difficulties with flow control
• Kyle Simpson uses the Legend of Zelda analogy to describe how code flow can fork and become non-linear, making it hard for developers to understand
• Teaching JavaScript often involves choosing between explaining low-level concepts like callbacks or higher-level abstractions like async/await
• Callbacks have limitations, including:
  • Lack of memory: callbacks don't inherently store state with them
  • Difficulty managing time as a complex state in the application
  • Inability to pair state with callbacks without introducing ad-hoc patterns like thunks or closures
• Problems with callbacks: "callback hell"
• Need for cancelable async actions and state management
• Inversion of control issue with callbacks
• Syntax promotes non-local, non-sequential reasoning, making code hard to understand
• Promises are a better solution due to their design and ability to un-invert control
• Future of the web: concerns about proprietary alternatives and loss of open standards
• Debate over the role of companies like Google and Microsoft in shaping web standards
• Criticism of W3C's structure and Apple's use of veto power to limit innovation
• Discussion of TC39's consensus-based process for JavaScript standardization
• Concerns about digital rights protection (DRM) being integrated into the web platform
• Fear that vendors will gain control over content and user experience, undermining open web principles
• Existential threat to the open web from content producers being forced to use restrictive monetization models and account for piracy
• Concerns about user privacy and control being taken away by ad networks and personalized advertising
• Discussion around the principle of constituencies, prioritizing users over developers and implementers when making decisions about web platform functionality
• Importance of security and performance in maintaining the web's competitive edge against proprietary competitors like app stores
• Analysis of progressive web apps and blurring lines between web and native apps, with a focus on user needs and currencies (e.g. battery life, bandwidth)
• Discussion on the limitations of web development due to its focus on backwards-compatibility
• The potential drawbacks of being too focused on compatibility, including slower innovation and creation of workarounds
• Comparison with other industries, such as Apple's hardware, where upgrading is necessary for optimal performance
• Backwards-compatibility as a fundamental aspect of the web's inclusion and neutrality
• Introduction to the project of the week: Blake2b-WASM, a WebAssembly implementation of a secure hashing algorithm
• Discussion on the potential of WebAssembly to improve performance in web development, including moving complex tasks off the main thread.
• WebAssembly (WASM) and its implications on web development
• Potential shift towards using languages like C, Go, or Rust for web applications
• Impact of WASM on "View source" functionality and debugging tools
• Possibility of Node.js supporting WASM and changing the way JavaScript is used
• SIMD extensions being pulled from TC39 due to WebAssembly
• Pressure release valve effect of WebAssembly on JavaScript language development
• Performance comparison between WASM implementation and native modules in Node.js
• Introduction of Atomics and Shared Memory features in ES2017
• Discussion of JavaScript's Atomics API and its similarities to Go's message passing structures
• Importance of shared memory between workers in JavaScript and potential performance benefits
• Picks discussion:
	+ Alex Sexton: Blake2b-WASM
	+ Mikeal Rogers: Quest MCT powder for keto diet
	+ Kyle Simpson: Fluent Web Conference (co-chairing)
	+ Alex Sexton: Preact.js as a lightweight alternative to React
• Recommendation of talk "Into the void 0" by Jason Miller at JSConf EU