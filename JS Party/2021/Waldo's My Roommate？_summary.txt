• Jason Miller's new tool for modern web apps
• WMR (a development tool) and its name being disputed by the team
• The origins of WMR and its initial concept as a joke
• Preact and its creator, Jason Miller, also discussed in relation to WMR
• Discussion of funny acronyms and their meanings
• Proposal of alternative acronyms for WMR (Windows ME Returns)
• Debate over whether a gopher is a rodent or not
• Introducing new acronym suggestions such as WMR (Wicked Mr. Renderer) and Where's My Refund
• Discovery that WMR was already used by the IRS for their tax refund service
• Nick's personal anecdote about having a roommate named Waldo
• Definition of modern web app: modern browsers, UX, and dependencies
• Two possible answers for "modern web app"
• Characteristics of a modern web app: ES 2017 or newer, optimized tool chain for ES modules and TypeScript
• Problem with bundler setups: layers of abstraction added in, hurting readability
• WMR's approach: focus on recent, newer stuff while still supporting older dependencies
• Comparison to existing tools: closest to Webpack, Vite, and Parcel
• Goal of WMR: remove itself from developer's field of view, minimal configuration required
• WMR extracts configuration defaults from user code instead of providing pre-set defaults
• Webpack's optimized chunks configuration is supported in WMR for production output
• Default settings are based on concrete, obvious values that developers would likely specify anyway
• WMR infers configuration and styling from user code, similar to compiler type inference
• In development mode, WMR doesn't bundle but instead ships modules over the wire as HTTP requests
• Comparison is drawn with other tools like Skypack, Snowpack, and Vite for their similarities in dev server capabilities
• Optimizing JavaScript module loading and transformation for the web browser
• Creating a custom AST transformer and Rollup-compatible plugin API to reduce processing time
• Using a memory cache, minimal AST transformations, and token-based transformations for fast module loading
• Streaming dependencies from the npm registry instead of installing them locally
• Analyzing package files in real-time and conditionally writing necessary files to disk
• Avoiding potential security risks by not running package install scripts or writing temporary files
• Inference feature: automatically fetching dependencies based on usage in code
• Exposing an export map for each module, allowing WMR to determine which files are externally accessible.
• Inference of source text for importing dependencies
• Streamed file delivery to browser for instant dependency loading
• Lightweight roll-up bundling without minification or mangling
• Minification and Brotly compression pass after initial load
• File extension inference for importing JavaScript files in TypeScript projects
• Support for direct ESM imports with rollup plugin API
• Handling of script tags in HTML documents with full file extensions
• Discussion of inference in WMR (Web Magic Router) and its relation to Create React app and Webpack semantics
• Introduction of a debug environment variable that prints out plugins executed on every request
• Explanation of file extensions and their role in VS Code and JetBrains auto-import features
• Mention of TypeScript support in WMR and how it is used for scaffolding projects
• Discussion of the Preact team's use of TypeScript and JS doc based types
• Explanation of ambient types in TypeScript and their usage in WMR
• Description of CSS modules and import prefixes supported by WMR
• Overview of type definitions provided by WMR for default configurations
• Relationship between WMR (Web Mobile Runtime) and Preact
• Requirement for using Preact with WMR, or ability to use anything else
• Need for tooling that supports modern JavaScript projects in development
• Export maps as a way to publish modern JavaScript packages
• Convergence of browser support and node.js versions supporting modern JS
• Development experience improvements through smaller bundles and readable code
• HTTP2 setup and certificates in WMR
• Independent modules and plugins for WMR
• Export maps implementation for bundlers
• Preact-agnostic design with optional JSX support
• Create WMR package and scaffolding for Preact
• Pre-rendering and CSS optimization features in WMR
• API for automatic pre-rendering and linking
• Framework agnosticism, including Svelte and React
• Custom plugins and config files for WMR
• Forking or creating alternative packages for WMR
• Collaboration versus competition in tool development
• Building a new tool for Preact and its potential impact on the ecosystem
• Abstraction levels and how to determine which layers are most useful
• Implementing Export Maps, including shared implementations and reference implementations
• Custom AST transformer and its relationship to WMR and Babel compatibility
• Using faster languages in tool development (e.g. ESBuild for JavaScript transformations)
• Deciding which components of a tool should be published independently
• The team's decision-making process and the importance of considering different perspectives
• Features of WMR (Web Matrix Router) that make it an attractive tool for development
	+ Easy setup with NPM init WMR
	+ Fast project creation and directory setup
	+ No need to install separate packages, such as dash G
• Discussion on the breadth and scale of WMR's capabilities
	+ From prototyping to production-ready applications
	+ Potential limitations on complex web app development
• Personal anecdote about building a custom web client with WMR
• Investigation into scaling issues with ES modules and performance constraints
	+ Experiments and benchmarks being conducted by the WMR team and Chrome/V8 teams
	+ Cart and horse situation between module streaming performance and project size limitations
• WMR's dependencies can become bloated if not managed properly
• Scaling issues may arise with large numbers of source files
• Hot module reloading can help mitigate these issues
• Production considerations: WMR is a solid rollup config, similar to standard configurations
• Production output quality comparable to other tools like Webpack
• Rollup-based production output is considered the "gold standard"
• Server-side concerns for complex applications and large numbers of modules
• Using WMR's built-in server is not recommended for production environments
• Deployment options and differences between WMR (Web Micro Renderer) and production servers
• Middleware support in WMR for proxies and other setup
• Distinction between WMR as a development tool vs. a production server
• Comparison with Next.js, including its role as a runtime and server
• WMR's goal of generating static apps vs. hosting hybrid applications
• Use cases for combining WMR with Eleventy or other static site generators
• Hot module replacement in Eleventy and page-based routing with plugins and recipes
• Running npm init WMR in the terminal to set up a new project
• Warning about the potential for directory changes and loss of files
• Jason Miller as guest, discussing his work on cool new tools for web development
• Links to WMR and show notes with resources discussed on this episode
• Discussion of future episodes and sponsorships