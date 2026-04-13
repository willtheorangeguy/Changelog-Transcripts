• Pika is a project aimed at moving the JavaScript ecosystem forward
• The project addresses issues with modernizing the ecosystem, including the use of Webpack and transpiler bloat
• Pika includes several sub-projects, such as Pika/web, which allows for direct installation and loading of ES modules in the browser
• ES modules (also known as ES6 modules) are a native module system for JavaScript, introduced in 2015
• Pika aims to make modern JavaScript more accessible by simplifying package management and code loading in the browser
• CommonJS was inherited from Node.js's early days and is still used by npm.
• Modern ES modules are now supported in modern browsers, allowing for native JavaScript modules.
• The "import/export" syntax is supported in most modern browsers, but some features like dynamic imports are still being fleshed out.
• Pika's website determines what packages are ES module packages using the "module" entry point in package.json.
• About 6% of npm packages now support ES module builds, and this concept grew out of a proposal to avoid adding a new file extension (.mjs).
• The Node team is working on supporting ES module syntax compatibility, but it's been a complex problem.
• Node may no longer require the .mjs file extension for ES modules, and could introduce a "type" property in package.json instead.
• Pika will continue to use Node.js as the JavaScript entry point and main function
• ES modules native to the web are discussed, with the idea being that they can be used directly without Pika
• Problems with importing packages by name or path in the browser due to lack of lookup mechanism
• Pika/web is a bundler that fixes these issues by running on dependencies rather than the whole codebase
• Pika/web purifies npm packages for use with ES modules, abstracting away complex package relationships and file paths
• Limitations of Pika/web include reliance on package authors doing the right thing and potential issues with hijacking module systems to load non-JS files
• Node-specific packages and their interaction with ES modules
• Compiling everything to JavaScript, .js files, and loading assets in a web-standard way
• The need for tooling on the consumer's part and its avoidance by package authors
• Handling JSON files in Node package manager and Pika/web
• Performance gains from using HTTP/2 standard and caching with ES modules
• Using Pika/web to avoid bundler complexity and achieve simpler development environments
• Integrating TypeScript, Babel, or other tools into the workflow without adding extra tooling
• The goal of Pika/web to make it easy for developers to use ES modules without needing additional tooling
• Pika/web allows for importing dependencies by name and transpiling experimental features
• The Babel plugin for Pika/web rewrites import statements in the build process
• PikaPkg.com is an index of modern, web-focused packages for npm
• Pika/pack is a tool for package creators to simplify building and publishing packages
• Pika/pack allows package creators to define a build pipeline with specific plugins and settings
• The goal of Pika/pack is to standardize the build process and release process for packages
• Discussion about a potential integration between Pika/pack and npm for easier package management
• Mention of an RFC (Request For Comments) created by the npm team to explore integrating Pika/pack or moving towards the same system
• Introduction of Deno plugin, which allows publishing packages that can be consumed by Deno without needing to know how it works
• Example of a "Five" package on npm, which outputs numbers in different languages and is used as an analogy for illustrating the benefits of Pika/pack
• Discussion about how plugins can simplify packaging and distribution of libraries with specific requirements or dependencies
• Mention of the importance of web-friendliness and ES module support for packages that need to be used in a web environment
• Examples of existing packages, such as Lodash, which have separate modules for different environments (e.g. Node vs ES module)
• Wasm-pack and Pika/pack allowing non-JavaScript source languages (like Rust) to be built into npm packages
• Potential to simplify web development with direct ES module loading, reducing the need for bundling
• The "view-source" feature being brought back through this approach
• Open-sourcing of Pika project and invitation to community involvement
• Future goal of making Pika irrelevant