• Development of an open-source gaming engine called GDevelop using React and WebAssembly
• Porting C++ game engine to WebAssembly using Emscripten compiler
• Replacing UI code in C++ with a React application
• Using AssemblyScript as an alternative to writing WebAssembly from scratch
• Challenges and gotchas, including large bundle sizes and memory leaks
• Seamless integration of React with existing codebase
• Porting existing interfaces to React
• Using WebAssembly to bind native code with JavaScript frameworks
• Benefits of using WebAssembly for desktop applications
• Debugging issues in WebAssembly modules
• Importance of testing and validation when bridging compiled languages to dynamic languages like JavaScript
• Tooling and typing systems (e.g. Flow, TypeScript) for ensuring type safety and maintainability
• Challenges of transitioning from a web background to using WebAssembly, particularly regarding garbage collection and manual memory management
• Importance of understanding object lifetime in WebAssembly for proper usage and avoidance of crashes
• Limited availability of tooling for debugging memory leaks in WebAssembly
• Difficulty in writing tests that bridge between C++ codebase and JavaScript
• Possibility of using WebAssembly for mobile applications through native libraries or progressive web apps
• Advantages of WebAssembly, including sandboxing utilities and access to npm ecosystem
• JavaScript ecosystem's strength is its ability to install any module with npm, but also its weakness due to the potential for overwhelming dependencies.
• The process of standardization in JavaScript can be slow compared to native languages like C++.
• WebAssembly has limitations, such as not having code-splitting or tree shaking, which can lead to unnecessary dependencies.
• There is a balance between innovation and robustness in ecosystems.
• Tooling improvements are necessary to address the issue of 1,000 dependencies and sub-dependencies.
• JavaScript is evolving towards a more robust language with features like ES6 and typing.
• WebAssembly and native languages are moving in the same direction, incorporating features like tree shaking and dead code elimination.
• The feedback loop in JavaScript development is key to its ecosystem's success, allowing for rapid iteration and creation of libraries.
• Gatsby framework performance and benefits
• Auto-reloading and iteration speed improvements
• React and Storybook for development and testing
• Combining C++ with JavaScript and React for hybrid application
• Build steps and manual build vs automated integration with Webpack
• Babel macros and metaprogramming in the JavaScript ecosystem
• Discussion about recompiling and breakpoints in native development on mobile
• Comparison of native development experiences between Xcode and Android Studio
• Introduction to GDevelop game engine and its visual programming system
• GDevelop's open-source nature and potential for integrating WebAssembly with JavaScript