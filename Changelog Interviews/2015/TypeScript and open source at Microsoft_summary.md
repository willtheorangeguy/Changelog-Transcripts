• Microsoft's TypeScript team is discussed, with Jonathan Turner and Anders Hausberg as guests
• Introduction to Jonathan Turner, program manager, and Anders Hausberg, technical fellow, on the TypeScript team
• History of TypeScript, started in 2011 as a way to address maintenance and scalability issues in large JavaScript codebases
• Description of TypeScript's purpose, to provide a typed superset of JavaScript for growing applications
• Mention of other projects, such as Google's GWT and Microsoft's ScriptSharp, that aimed to address similar issues
• Discussion of the team's decision to productize TypeScript, rather than just a internal tool
• Anders Hausberg's background and work on Delphi and Turbo Pascal, and his correction of his native language's name as "Delphi" rather than "gif"
• The goal was to create a "best of breed" solution that solves problems on the community's terms, not on the creator's terms.
• The team put on a "javascript hat" to determine what a javascript programmer would want, and found that they needed features like classes, modules, interfaces, and static typing.
• The team's design goal was to leverage existing effort in the javascript ecosystem and not create a new language, but a superset that compiles to plain javascript.
• The team aimed to make typescript usable in existing codebases and not require a new coding style.
• Typescript was first used internally by 3 teams, including the team that would eventually become monaco, before it went public in October 2012.
• The team estimates that it took 6-12 months to go from ideation to having a usable prototype.
• The team's vision evolved and became less ambitious, focusing on tooling and error checking rather than trying to use type information to execute code more efficiently.
• Typescript plays a role in Microsoft's future direction, particularly in embracing open source and community involvement.
• Open-source development and its benefits
• Microsoft's evolution towards open-source, from early hesitation to embracing it
• The importance of open-source for appealing to the JavaScript community
• Comparison of proprietary and open-source models, citing Delphi and Turbo Pascal as examples
• The changing landscape of software development and financing, with a focus on open-source companies
• Sudden adoption of Angular 2 and other frameworks driven by TypeScript
• Initial reaction to Microsoft's open-source efforts in JavaScript in 2012 was mixed, with suspicion and enthusiasm
• Importance of self-hosting and dog-fooding to understand the JavaScript community and its needs
• Microsoft's decision to open-source TypeScript and its tooling, rather than just the compiler
• Key innovation: making the compiler an API and architecting it for incremental and lazy execution to enable sub-100ms responses on large projects
• Unexpected improvements in VMs and hardware, enabling previously impossible feats in JavaScript development
• Discussion of TypeScript and its optional typing system
• Comparison to traditional typing systems in languages like C# and Java
• Explanation of TypeScript's gradual typing system as a dial that can be adjusted from 0 (dynamic) to 100 (static)
• Description of how TypeScript's type system is not about providing absolute guarantees, but rather plugging holes in the "swiss cheese" of JavaScript
• Mention of structural typing and its advantages in TypeScript
• Loose typing in JavaScript can be replaced with type annotations using TypeScript
• TypeScript allows for flexibility and extension of existing systems
• Tooling and correctness are major benefits of TypeScript
• Performance benefits are not a primary advantage of TypeScript, but correctness is
• TypeScript delivers features from the future today, allowing for compilation to lower versions of JavaScript
• Delivering features from the future is a repeat phenomenon, as it takes time for ECMAScript standards to permeate the JavaScript ecosystem
• TypeScript is a transpiler and downleveler, providing a compelling combination of type safety and feature delivery
• Feature selection for early adoption is based on compatibility, implementability, and alignment with ECMAScript standards
• The TypeScript team considers features that are proposed for ECMAScript standards and implements them early, but may remove them if they are not ratified or supported by browsers
• Reflect dot realm is a runtime library feature that can be polyfilled.
• Modules in ES6 were late to land and their standardization is still ongoing.
• TypeScript had to make a "best guess" effort to implement modules, which turned out to be mostly correct.
• Backwards compatibility is crucial for TypeScript, and it will continue to support older features alongside new ones.
• The TypeScript specification includes additional features not present in ES6, such as type inference and generics.
• The TypeScript roadmap can be found on the GitHub site, which roughly outlines upcoming features.
• The compiler's API is an important feature that allows users to customize and extend the compiler.
• The compiler is implemented in TypeScript and has around 50,000 lines of code, with most of it written by Andrew.
• Discussion of compiler improvements and the development process
• The compiler's speed and weight were significantly improved
• The importance of incrementalness in compiler design
• Divergence between traditional compiler writing methods and modern requirements
• Implementing lazy type systems and incremental data structures for faster performance
• Challenges of implementing a language service that is resilient to errors and changes in the code
• The compiler's use of immutable data structures and functional programming principles
• The development of a language service that can be used in various text editors and IDEs.
• The speaker discusses the benefits of using functions and closures in JavaScript, specifically in the context of type checkers and compilers.
• The speaker suggests that open-sourcing knowledge and code is a way to institutionalize expertise and pass it down to future generations.
• The speaker highlights the importance of reading code, discussing code with others, and contributing to open-source projects to gain a deeper understanding of the code and its community.
• The speaker notes that the increased adoption of TypeScript in recent years may be due to the excitement around ES6 features, which have made it more feasible to write complex projects in JavaScript.
• The speaker mentions that large projects such as Angular and Dojo 2 will be using TypeScript in their next major releases.
• Development of TypeScript and its relationship with ES6 and Angular
• Merging of philosophies between TypeScript and Angular to create a stronger and more capable language
• Introduction of annotations and decorators, and their potential impact on the JavaScript ecosystem
• Collaboration between Microsoft, Google, and other JavaScript communities on TypeScript and Angular
• The importance of open source and collaboration in advancing the future of JavaScript and TypeScript
• Getting started with TypeScript for developers, including installation and tooling for Microsoft and Node.js developers.
• The speaker recommends cloning the TypeScript repository and running the TypeScript compiler for the most up-to-date language features.
• The language service is open-source, resulting in a wide range of high-quality plugins for popular editors, including Sublime Text, Adam.IO, Eclipse, and WebStorm.
• There is good coverage of TypeScript in development tools and IDEs, including build tools like Grunt and Gulp.
• The Definitely Typed repository contains a vast collection of type definitions for various JavaScript frameworks, with over 1,000 frameworks covered.
• Provisioning tools like tsd allow for easy management of type definitions in projects.
• The speaker highlights the power of open-source communities in creating such resources.
• Resources for learning TypeScript include samples on the website, a handbook, and the TypeScript specification.
• The TypeScript specification is available in various formats, including markdown, on the GitHub site.
• The speaker mentions a roadmap for the future of TypeScript on the website.
• TypeScript 1.4 is current release, 1.5 is in alpha/beta stage with ES6 compatibility focus
• 1.5 release will close gaps in ES6 compatibility, leaving only a few features to add
• ES7 features, such as async/await, are being explored
• Support for JSX and decorators is also being considered
• Roadmap: 1.6 will round out missing features, 2.0 will be ES6 and ES7 complete
• Future goals include module bundling and integration with build systems
• TypeScript type system is ongoing and will continue to evolve
• Ongoing work includes integrating new language features into type system theory
• Future of TypeScript: ES6 and module support will be ongoing topics, new development tools and deeper integration with build systems will be explored.
• TypeScript as a solution for large JavaScript codebases
• Adoption of TypeScript for improving productivity and maintainability
• Importance of simplicity and programmer productivity in language design
• Community involvement and participation in TypeScript development
• Opportunities for users to contribute to TypeScript and help with its mission
• Typescript 1.5 is an alpha release and is looking for adoption and support
• Options for implementing Typescript 1.5 include plugin models and external code review systems
• The Typescript codebase is now on GitHub and contributors are encouraged to participate in language design
• A contributor license agreement is required for contributing code to the Typescript codebase
• External tools like Gerrit are being used to streamline the code review process
• Typescript can be used today and "inched" into more fully adopting it
• The Typescript team is looking for community involvement and feedback on language design
• The Typescript website now features logos of companies and projects that are using Typescript