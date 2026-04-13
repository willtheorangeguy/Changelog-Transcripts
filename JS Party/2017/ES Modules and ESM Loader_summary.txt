• History of ES modules
• Dojo and its early module system
• ServerJS community and Narwhal's synchronous module pattern
• CommonJS spec and its influence on NodeJS module system
• AMD spec and its attempt to address limitations of NodeJS module system
• Browserify and bundling of modules in web applications
• Asynchronous loading vs bundling for web applications
• The CommonJS community and ServerJS had issues defining a standard for promises, resulting in multiple specs
• ES modules were influenced by Python's module system, which included features like import * from module, causing issues with scope and namespace collisions
• The spec was revised to use new syntax and address the issues of the previous version, but it remained in a "weird state" before the implementation of new processes at TC39
• ES modules were finalized before many implementations existed, leading to concerns about compatibility with Node.js
• John-David Dalton got involved in addressing edge cases and gotchas in implementing ES modules in Node.js, particularly related to the .mjs extension and transpilation issues
• Discussion of ESM (ECMAScript Modules) parse detection and the introduction of new file extensions
• Proposal for "Unambiguous JavaScript Grammar" to determine ESM files by import or export statements
• Concerns about unintentionally changing parse goals when refactoring code with implicit strict mode
• Overview of current status of ESM implementations in browsers (Edge, Firefox, Chrome, Safari)
• Mention of the loader spec and its relationship to SystemJS
• Discussion of AMD (Asynchronous Module Definition) vs CommonJS and their role in compiling modules for web use
• The debate over AMD vs CommonJS module systems
• The idea of compiling down to a single format, such as AMD, for cross-browser compatibility
• The rise of Babel and its impact on the need for module system arguments
• Criticisms of Node.js requiring JavaScript use for web development
• Disagreements over whether Node.js improved or hindered toolchain innovation
• Node module system limitations for web use
• Browserify and AMD loading without build pipelines
• Standardization of tools and features in technology
• Synchronous vs asynchronous builds and their impact on performance
• Future developments in dynamic imports and bundle size reduction
• Service workers and background code updates as potential solutions
• Discussion of web page loading issues and the impact of JavaScript parsing time
• Criticism of current build system contributing to the problem
• Introduction of project of the week: Lodash 5 ES6+ only loader for Node 4+
• Explanation of how the loader works, including caching and transpiling
• Benefits of using the loader, such as removing compile steps and supporting multiple Node versions
• Details on configuring the loader with options like unambiguous module grammar and commonjs carryover
• Discussion of future plans and the possibility of using the loader in browsers without tooling
• Using gzipped modules for Node.js projects
• ESM (ECMAScript Module) loader with built-in gzip support
• Benefits of using the ESM loader, including smaller package size and faster loading times
• Potential drawbacks of using gzipped files, such as increased CPU usage for decompression
• Lodash 5's new architecture, which will not have an index file or main monolithic include, and will instead use cherry-picked modules
• Node.js caching behavior and its impact on startup costs
• Lodash 5 is changing its approach from providing all functionality upfront to giving minimal functionality and allowing users to opt-in to more features
• Rollup and Webpack will need to be updated to work with the new module system used by Lodash 5
• The Fantasy Land specification is being discussed as a potential standard for interoperability of algebraic structures in JavaScript
• John-David Dalton's pick: contributing to open-source projects like Babel, MomentJS, and Mocha
• Mapzen JavaScript API is being recommended as an alternative to Mapbox for integrating maps with websites or apps
• Goodbye statement from John-David Dalton