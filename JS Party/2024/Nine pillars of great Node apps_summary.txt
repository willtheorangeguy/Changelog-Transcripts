• The Nine Node Pillars document was created by four people, led by Matteo Collina, who wanted to share good practices for building enterprise-ready Node.js apps.
• The pillars are meant to be a collection of hard-won knowledge from experience working with companies and helping them avoid common mistakes.
• Some pillars are generic and applicable to many applications, while others are more specific to Node.js.
• The nine pillars include:
	+ Do not block the event loop
	+ Monitor Node-specific metrics and act on them
	+ Use Node LTS versions in production
	+ Automate testing, code review, and conformance
	+ Avoid dependency creep
	+ De-risk your dependencies
	+ Avoid global variables, config or singletons
	+ Handle errors and provide meaningful logs
	+ Use API specifications and automatically generate clients
• Unwieldy dependencies in JavaScript projects
• npm and Node.js solving the problem of reusing software at scale
• Risks of using outdated or unnecessary modules (e.g. Request module still downloaded 70 million times per week despite being deprecated)
• Importance of keeping codebases "liquid" to adapt to changing needs
• Choosing between using existing dependencies vs. building custom solutions
• Factors to consider when selecting dependencies, including maintainability and long-term stability
• De-risking dependencies through involvement in open source projects and understanding codebases and their ecosystems
• The importance of knowing the project's maintenance status, team behind it, and intentions for future maintenance.
• Avoiding global variables, configs, and singletons
• The historical context of globals in JavaScript, especially in the browser
• Problems with NODE_ENV=production and its misuse
• Importance of understanding scopes and JavaScript mechanics before learning frameworks
• How "what works in the small does not work in the large" applies to code organization and scalability
• Importance of setting environment variables in deployment
• Handling errors and providing meaningful logs in applications
• Implementing a graceful shutdown pattern to avoid crashing the system when an error occurs
• Using API specifications (such as OpenAPI) and automatically generating clients to ensure consistency across APIs and prevent reinventing the wheel
• Logging: finding the right balance between logging too much or too little, and using log levels effectively
• Discussion on whether OpenAPI or GraphQL is better for API design
• Overview of TypeSpec, an open-source tool from Microsoft for defining and generating API specs
• Importance of understanding the event loop in Node.js for writing efficient code
• Common pitfalls when working with the event loop, including blocking it with CPU-intensive tasks
• Advice to "slow down to go faster" and take the time to design and architect systems correctly
• Monitoring event loop utilization to prevent performance issues
• Node-specific metrics and their importance in evaluating system performance
• Key metrics to watch in a Node.js application:
	+ Event loop utilization
	+ Heap used vs. heap total (memory usage)
	+ CPU usage
• Using Node LTS (long-term support) versions in production for reduced risk of breaking changes, enhanced security, and improved stability
• Node.js version 10 discussion
• Backwards compatibility in Node.js
• Trade-offs between innovation and backwards compatibility
• Automating testing, code review, and conformance
• Importance of standards and conventions in software development
• Role of tooling (linters, style guides, Prettier) in enforcing standards
• TypeScript support in Node.js
• Personal opinions on using TypeScript vs. JavaScript
• Discussion of JSR (Deno's new registry) for publishing TypeScript packages
• Variability in tooling and options reduced with JSR, but still requires transpilation for application authors
• The importance of supporting maintainers financially through initiatives like the Open Source Pledge
• Encouragement to companies to consider contributing resources or funding to open source projects and their maintainers
• Benefits of getting involved in open source as a developer, including personal reward and community contribution