• Introduction to special guest Daniel Ehrenberg (aka Little Dan) and his background in JavaScript standards work
• Overview of Daniel's current role at Bloomberg and its use of JavaScript/TypeScript
• Explanation of ECMAScript and its relationship to JavaScript
• Description of the TC39 technical committee within ECMA and its purpose for standardizing JavaScript
• Discussion of the open process for contributing to the JavaScript language, including participation from outside the committee and collaboration with the open source community
• The process of developing software is discussed, specifically how it has changed from Windows 95/98 to rolling releases.
• A five-stage process for proposing language features is outlined:
	+ Stage 1: Idea discussion
	+ Stage 2: Concrete first draft
	+ Stage 2.7: Design completion with community outreach and implementer input
	+ Stage 3: Writing tests (conformance tests)
	+ Stage 4: Multiple engine implementation and shipping of the feature
• The importance of Test262, an open-source project that tests the full JavaScript language, is highlighted.
• The process of standardizing JavaScript features through ECMA 262 is explained:
	+ Merging PRs for stage four features into the editor's draft specification
	+ Printing physical copies of the standard and its archiving in the Swiss National Library
• The discussion of tail call optimization highlights the complexities and trade-offs involved in standardizing language features.
• The TC39's approach to releasing subsequent standards is praised for being more sustainable and less eventful than previous releases.
• Importance of a trifecta of skills (language design, web development, testing) in language standardization
• Benefits of having tests for language specifications, including implementation speedup and early feedback opportunities
• Discussion of a bug found in the BigInt proposal and how it was addressed through testing
• Introduction to the TC39 test262 repository for contributing to and learning about JavaScript testing
• Excitement about the type annotations proposal for adding syntax to JavaScript for types
• Challenges and trade-offs of implementing type checking in JavaScript, including compatibility and evolution concerns
• Records and tuples as immutable data types
• Original plan to make records and tuples primitives like numbers or strings, but complexity of implementation led to change in approach
• Records and tuples will now be objects, not primitives, which may limit their use with triple equals for comparison
• Possible loss of interning optimization due to generational garbage collection strategy used by modern JavaScript engines
• Upcoming helper methods on maps and sets
• GroupBy method issues and alternatives for filtering and grouping data
• Sync iterator helpers proposal at stage three
• TC39's proposals repo and encouraging community feedback early in the process
• Stage four: Promise with resolvers (explained by Daniel Ehrenberg)
• Promise.withResolvers is a function that simplifies creating promises by returning an object with a promise and resolve/reject functions.
• The original promise constructor was considered too verbose and led to people incorrectly using promises or throwing exceptions instead of rejecting them.
• The idea behind Promise.withResolvers is to encourage correct promise usage, but it has been slow to catch on due to the initial reluctance to use resolve and reject functions properly.
• The function's design and purpose were influenced by debates in TC39 and the evolution of JavaScript features like destructuring and const.
• There are still some lingering issues with using promises correctly, such as the tendency to save off resolve and reject functions or misuse setTimeout.
• Shipping of Stage 4 proposals to browsers
• Standard library proposals in ES2023, including new methods on existing JavaScript classes
• Temporal proposal in Stage 3
• Array grouping proposal, and its evolution from targeting arrays to iterables
• Lodash deprecation and the addition of group by functionality as a standard language feature
• Error cause, allowing for extra information about an error's cause
• ES2024, with stage 4 proposals officially becoming part of it in January
• Pitbull: an unknown reference or joke made by Amal Hussein
• Decorators: a feature in JavaScript that has been developed over several years, with a stable proposal and implementation in TypeScript and Babel
• Temporal: a new date and time library for JavaScript, currently at stage 3, which aims to replace the existing Date object and provide a more robust and timezone-aware API
• Temporal proposal: a date/time library for the web
• Polyfill stability and production readiness
• ISO8601 extension for timezones and calendars
• Stage 2 proposals:
  • Records and tuples (immutable versions of objects and arrays)
  • Module expressions and declarations
• Async context proposal
• Module expressions and declarations (conflict with TypeScript module keyword)
• Bundlers and native JavaScript modules
• TypeScript deprecation of "module" keyword
• Async context benefits for distributed tracing and logging in servers
• WinterCG is a W3C community group focused on standardizing web APIs for server environments
• It's an open group where anyone can participate and work together to define a minimum common API for shared needs between different server environments
• The goal of WinterCG is to bring standardization to higher-level JavaScript server runtimes, making code more portable across platforms
• Standardization efforts include async context, fetch, and other APIs that have varying implementations in Deno, Cloudflare Workers, Node, and others
• The plan is for the standardization work to be published either within the WATWG fetch standard or as a separate specification through an ECMA technical committee
• WinterCG: a community-driven initiative to standardize APIs and improve interoperability between web browsers and services
• Standalone libraries vs. aligning with existing standards (e.g., response.json)
• Socket APIs: exploring the possibility of defining own library for TC, potentially within WinterCG
• Standardizing source maps: correcting ambiguities in the current specification and adding new features (e.g., Pasta Source Maps metadata)
• Task Group 4 (TG4): a subcommittee within TC39 focused on standardizing source maps
• Open source sustainability challenges
• Invited expert program for non-company contributors
• Funding open source projects through consultancy models
• Bloomberg's donation program to open source projects
• Strategies for open source contribution and funding (giving money, time, or hiring staff)
• Balancing individual contributor roles with full-time positions
• Microsoft poaching engineers from companies like Igalia and Bocoup
• Discussion of Igalia's cooperative model and emphasis on equality
• Progress in JavaScript and CSS semantics and spec filling
• Web as the greatest thing humanity has ever made, and its importance for communication, collaboration, and creation
• Lighthearted conversation about choosing between bread and the web