• The challenges of upgrading a large codebase without tests
• How type annotations can help prevent breaking changes
• Dojo framework and its focus on being TypeScript-first
• Importance of TypeScript support for modern Dojo development
• Nick's comment comparing React to Dojo and Matt's defense of Dojo
• Developer experience is a key focus of the Dojo framework
• TypeScript support is a major factor in this focus
• The original Dojo 2 had class-based components and a composition system called Compose, but it was limited by TypeScript at the time
• In later versions, including Dojo 6, functions were used to provide more capabilities for composing behaviors and affecting types
• Middleware is a key feature of Dojo 6 that allows encapsulating behavior and types in self-contained components
• Middleware can be compared to hooks in React, but they have distinct implementations and usability aspects
• Discussion of Dojo Toolkit's version history and evolution from version 2 to 7.
• Comparison with other frameworks such as React, Ember, and Angular.
• Explanation of how TypeScript is used in modern Dojo for type correctness and iteration.
• Use of the upgrade tool and Code Mods for frictionless upgrades and rewriting code.
• The concept of "TypeScript tax" and how it provides confidence in upgrading.
• Goal of Dojo Framework: to simplify app development and remove complexities
• Comparison with other frameworks: similar to Angular but closer to React in API surface area
• Features:
	+ Build tooling
	+ Testing
	+ Theming and styling components
	+ Router
	+ Data storage and management
	+ Code mods
	+ CLIs for upgrading, testing, and building applications
• Internationalization and localization features
• Accessibility features, including accessible widgets
• Interoperability with the web and the JavaScript ecosystem
• Discussion about using a Dojo library component in another library
• Custom element story and building tools for Dojo components
• Upgrading to new versions of Dojo without losing functionality
• Announcing the release of Linode's cloud server options starting at $5/month
• Overview of upcoming changes and features in Dojo 7, including improved widget usability and consistency, additional widgets, and a theming system with material style components
• Explanation of Dojo 7's focus on revisiting and improving existing widget library, addressing inconsistencies and improving documentation
• Configuration options for themes in Dojo
• Customizing component look and feel
• Changes to the Dojo Framework, including new widget components and API consistency
• Improved documentation with Parade tool, which generates documentation from code
• Switching from Hyperscript to TSX for widgets
• Conversion of class-based widgets to functional widgets
• Dojo 7 improvements focus on build time rendering and reducing configuration requirements for static websites
• Enhanced polyfill handling to only load necessary features and reduce bundle sizes
• Ongoing support for IE11 despite its legacy status and potential end-of-life in October 2023
• Challenges with testing and supporting a large framework, including IE11-specific issues with CSS variables
• Balancing support for enterprise customers and legacy browsers with the need to maintain a reasonable bundle size and push forward the framework
• Designing APIs with TypeScript in mind and accommodating IE 11 constraints
• Balancing polyfills for modern browsers while minimizing code shipped to the browser
• Deferring and lazily loading features in Dojo to avoid bundling unnecessary code
• Upgrading TypeScript support and potential complications with type inference
• Library author vs. end-user perspective on writing types and relying on inference
• Thorough testing in Dojo, including the new test harness
• Blurring lines between unit tests and integration tests
• Defining testing expectations for components, regardless of method
• Dojo test harness as an enzyme-like shallow renderer with its own approach to testing
• Testing reactive components and VDOMs
• Dojo 7's enhanced testing features, including writing partial tests against the full widget
• Support for multiple testing styles and tools, including intern and Jest
• Importance of in-browser testing and functional testing with Selenium
• New concept in Dojo 7: abstraction on the store system with "resources" for easy data providers
• Goal is to remove boilerplate state management (e.g. Redux) and make it seamless for common scenarios like fetching lists or making API calls
• Dojo 8 will expand this concept, allowing developers to create app-level widgets that can be easily hooked up to resources
• Resources aim to simplify complex tasks like caching, validation, and data management by managing these under the hood
• Developer ergonomics and reducing boilerplate code are key goals for Dojo's new design
• Discussion of Dojo 7 widget improvements, including ergonomic gains and reconciliation of state management
• Introduction of "resources" primitive in Dojo 7 for data fetching and pagination
• Comparison with MobX and its separation of state management and data fetching
• Impact on widgets such as combo boxes and type ahead features
• Contribution and development process of Dojo 7, including a large team effort
• Goal of providing more value to end users through larger features and less configuration
• Future direction of Dojo and potential opinionatedness about server-side implementations
• Discussion of TypeScript's role in bridging the full stack and its potential benefits
• Dojo's current focus on expanding front-end capabilities before exploring back-end development
• Dojo's power for building custom tools with TypeScript and ASTs
• Code splitting in Dojo and automatic generation of code splits
• Contributions to Dojo, including getting started on dojo.io and GitHub
• Community involvement through Discord channel and feedback on applications
• Contribution guidelines and tooling for developers to raise pull requests
• Dojo Code Sandbox for testing and reproducing bugs
• Future plans for Dojo 7 and beyond