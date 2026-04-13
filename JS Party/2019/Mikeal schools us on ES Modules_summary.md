• ES Modules (ESM) are a native module system for JavaScript in the browser
• ESM is not widely used yet due to its limited functionality and compatibility issues
• The goal of ESM is to create universal modules that can run everywhere without a compiler
• Migration from compilers to ESM requires significant changes to ecosystem infrastructure
• Import maps can be used to manage module imports, but current implementation has limitations
• Node.js and browser ecosystems require different approaches due to their unique constraints
• Discussion of module loading and dynamic loading in JavaScript
• Differences between browser and Node.js constraints for module loading
• Challenges with implementing ES modules (ESM) in Node.js, including compatibility issues with Webpack
• .mjs file extension and package.json "type" field as signals for ESM interpretation
• Webpack's difficulties in handling native ESM and its impact on developer workflow
• Prioritization of supporting a native module system in Node.js
• Adoption of ESM in Node is still a work in progress
• Using ESM with Rollup requires configuration and may not be straightforward
• There are difficulties in porting between ESM and CommonJS
• Incrementally switching from CommonJS to ESM can be done, but it's recommended to do it at the module level rather than file by file
• Native ESM modules can coexist with CommonJS modules, but interactions between them can be complex
• Better tools for managing native ESM are expected in the future
• There is potential for exciting new projects and opportunities in the Node ecosystem as a result of the adoption of ESM.
• Node.js and browser support for ESM (ECMAScript Modules)
• Dynamic hooks into the module system no longer work
• Transpiling languages at import time no longer supported
• Experimental and buggy custom loader interface for dynamic loading
• Ability to require imports in CommonJS modules using vanilla JavaScript
• Potential benefits of migrating to ESM include better performance
• ESM-focused modules are more likely than migrating older CommonJS modules
• Challenges with porting existing Node.js ecosystem to ESM due to differing patterns and dependencies
• Reg package manager solves issues by statically linking modules and providing a hash-based data structure for caching
• Browsers are moving towards isolated HTTP caching for each domain
• CDN versions of popular libraries (e.g. jQuery) will no longer be shared across domains
• Fingerprinting is a technique used by advertisers, but also has implications for caching and resource loading
• Reg is a new package registry that uses data structures to enable efficient caching and deduplication
• Reg allows for subfile data deduplication, reducing the amount of data transferred when updating packages
• There is a need for a standard interface for mapping HTTP APIs across different platforms (e.g. Node.js, Lambda, service workers)
• A standardized interface would allow for more efficient deployment and management of services across different environments
• Discussion around limitations of npm module compatibility
• Introduction to CSS Subgrid feature in Firefox 71 browser
• Overview of Web Almanac resource providing web-related knowledge and data
• Mention of Mikeal Rogers' GitHub repository for tracking trending projects and metrics
• Discussion about Postwoman API request builder project
• Introduction to Kitty terminal emulator, its features, and speed advantages