• Changelog is sponsored by Rollbar for real-time error monitoring and analytics
• Interview with Paul Bigger, founder of CircleCI, about their use of Rollbar
• Rollbar's importance in large-scale operations
• Discussion with Florian Rival from Facebook about using React and WebAssembly to create a game engine
• Overview of the game engine project called GDevelop and its transition to web-based development using WebAssembly and mScripten
• The speaker discusses running a game as a WebAssembly module using mscripten.
• The process involves taking UI code, converting it to WebAssembly, and bundling it into a JavaScript module.
• Once converted, the game can be run in the browser without the need for native code.
• Options for writing WebAssembly include using existing languages like C++ or Rust, or AssemblyScript, a type-script compiler for WebAssembly.
• The speaker encountered a major issue with large bundle sizes (up to 3MB) but notes that this is improving and may be acceptable for some applications.
• Another challenge mentioned was integrating the WebAssembly module with JavaScript code without introducing memory leaks.
• The ultimate goal of using WebAssembly in this case was to create a seamless integration between React UI components and an existing codebase.
• React and its applications in mobile and web development
• Porting interfaces to React for improved performance
• Using WebAssembly for native code reuse and packaging
• Integrating WebAssembly with JavaScript frameworks like React
• Debugging issues when calling functions between WebAssembly and JavaScript
• Performance requirements and limitations of WebAssembly
• Multi-threading and scripting capabilities in WebAssembly
• Challenges with memory management and error handling in WebAssembly
• Importance of testing when working with compiled languages and WebAssembly
• Need for automated generation of types and flow control in WebAssembly libraries
• Use of Flow and TypeScript for typing JavaScript code
• Benefits of using a strong typing system, especially for large applications and long-term maintenance
• The importance of type checking when working with complex systems or codebases.
• Challenges of transitioning from traditional programming to web development and using technologies like WebAssembly.
• Key differences between JavaScript's mental model for object lifetime and WebAssembly, specifically the need to manage memory and garbage collection manually.
• Potential solutions and future developments in WebAssembly, including improved garbage collection and easing usage with additional safety features.
• Manual memory management in WebAssembly
• Availability of tooling for debugging memory leaks
• Source maps and debugging flags for C++ code in Chrome debugger
• Difficulty testing interface between JavaScript and C++ codebases
• Importance of automatic generation of bindings and typings for bridging the gap
• Challenges with manual memory management and testing for correctness
• Reusing native code bases, such as C++ or Rust, by compiling them into a native library for use in iOS or Android apps
• Using WebAssembly to run code in web applications and progressive web apps, with examples of this being done successfully
• The potential for WebAssembly to enable "app-like" experiences in web applications, despite not offering the same level of performance as native mobile apps
• The benefits of using WebAssembly, including its sandboxing utilities and access to large ecosystems like NPM
• The speaker discusses the trade-offs between developing with JavaScript and other languages, citing both strengths (e.g. ease of installing packages) and weaknesses (e.g. complexity from numerous dependencies).
• They argue that React and the JavaScript ecosystem are now better suited for creating advanced interfaces.
• The conversation touches on the need to improve tooling around dependency management, including providing more visibility into what is being imported.
• The speaker reflects on the evolution of JavaScript as a language, noting its shift from a scripting language to a more robust one with added features like typing.
• They compare this development to other languages, such as C++, which are also introducing new features.
• Tree shaking and code splitting in WebAssembly
• Standard library usage and limitations
• Dead code elimination in C++ compilers
• Dynamic libraries and optional dependencies in WebAssembly
• Standardizing JavaScript libraries for WebAssembly development
• Balance between innovation and robust ecosystem
• Problems with package removal from NPM
• Importance of immutability for packages
• Benefits of modern JavaScript module bundling
• Speed and simplicity of publishing and reusing code
• React as an example of efficient component reuse
• Developing a new C++ library for WebAssembly
• Comparison of the tooling process to npm
• Importance of refactorability and composability in creating ecosystems
• Discussion on typing and its benefits in refactoring code
• Need for small modules with simple interfaces
• Ability to add or remove components without breaking things
• Discussion of a safety net feature
• Comparison of GDevelop and React for building a website
• Use of Gatsby as a game engine with no typing required
• Impression of Gatsby from the user's perspective, highlighting its performance and development experience
• Comparison of modern web development tools, including Webpack and auto reloading
• Gatsby website's speed improvement
• Benefits of using React for scalability and flexibility
• Server-side rendering and pre-rendering optimization techniques
• Importance of auto-reload and fast iteration in development
• Hooking up C++ code base for automatic recompile after changes
• Using a package like .json to run mscripten and compile C++ to web assembly module
• Setting up a development environment for C++ code in VS Code
• Automating the build and test process using npm scripts
• Using Storybook to test and display React components quickly
• Discussing the trade-off between manual build steps and automated integration
• Exploring options for integrating C++ or Rust code into Webpack or Create React App
• Discussion of webpack, including whether newer versions of create-react-app still require ejecting to customize webpack configurations
• Use of label macros for internationalization in a React application using a library called lingui
• Manipulating JavaScript Abstract Syntax Trees (AST) with macros to extend language syntax and create custom languages within the language
• Comparison of compile-time abstractions in Babel versus runtime abstractions in Ruby
• Discussion of cost-free abstractions, including their benefits and potential drawbacks
• Challenges of debugging applications built with these technologies
• Discussion of software development and game creation using visual programming
• Introduction to the game engine GDevelop and its open-source nature
• Live stream wrap-up and upcoming schedule for JS Party on Thursdays at 1 p.m.
• Shoutouts to partners Fastly, Rollbar, Leno Cloud Servers, and Breakmaster Cylinder