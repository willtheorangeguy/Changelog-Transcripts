• Introducing special guest Justin Fagnani
• Background on Justin's work at Google and creation of Lit
• Overview of Lit as a library for building web components
• Importance of Lit being tied to the Web Components standard
• Evolution of Lit from its origins with Polymer to its current state
• ES2015/ES6 browser support and module system limitations
• Web component specs (template element, custom elements, shadow DOM, HTML imports)
• Polymer's evolution from an HTML-centric library to JavaScript modules
• Lit's design as a direct successor to Polymer, with a focus on JavaScript containers and template literals
• Lit's use of tagged template literals for efficient rendering and minimal DOM updates
• The main entry point to lit HTML is a render function that looks like React's render, which takes a template expression and a container to render into.
• There are two phases: initial rendering and updating.
• Initial rendering involves creating an HTML template element, populating it with strings from the template, and marking dynamic expressions.
• The first time the template is rendered, it's cloned and appended to the container.
• During updates, lit checks if the same template was used previously; if so, it skips DOM manipulation and only updates data.
• A "parts" data structure is created during initial rendering, which maintains direct JavaScript references into the DOM and remembers old values.
• This technique enables fast updates with minimal memory overhead.
• The "template instantiation" or "DOM parts" proposals aim to bring this technique into browsers.
• lit maintains a lookup table for each template, containing bindings and last values, as well as pointers to their locations in the DOM.
• When an update comes through, lit checks if data has changed and updates accordingly.
• Subtemplates are handled recursively, using the same process as initial rendering.
• Conditional subtemplates are also handled, with the ability to swap between templates based on conditions.
• Using an array to manage references in template literals
• Template literal syntax and how it handles expressions and values
• Dynamic HTML limitations and the need for bounding dynamicism
• Template composition and conditional statements handling most cases
• Handling very dynamic cases with template cloning and potential security risks
• Comparison of Lit's approach to React's "dangerously set inner HTML" function
• Core principles: simplicity and minimalism
• Web components interoperability as a guiding principle
• Implementation details (Lit and Polymer) should be transparent to users
• Key features:
  • Declarative templating
  • Declarative reactive properties
  • Easy in-line styling
  • Single file components
  • Reactive lifecycle helpers
• Goal of unopinionatedness: making it easy for developers to write web components without needing Lit
• Hope that browser will standardize some features and make them available as a built-in base class
• Lit Element and its development history
• Concerns about adding Lit Element due to potential churn on audience
• Early versions of Lit Element were simple, around 10-12 lines of code
• Decision to keep Lit Element small and focused only on essential features
• Additional features added to Lit Element, including decorators, attribute reflection, and reactive controllers
• Reactive Controllers as custom hooks without the hook magic
• Base class "Reactive Element" that sits under Lit Element with reactivity but no template system
• Built-in support for React and Preact rendering in web components
• Lit is a library for building web components and its main goal is interoperability with other frameworks
• The ecosystem around Lit is still developing, but users often combine it with other libraries like routers and state management systems
• There are some Lit adapters available for popular frameworks like Redux and MobX
• Google has been experimenting with creating an application framework built on top of Lit
• They have also been working on integrating web components and Lit into React, Vue, and Angular
• Next.js integration is in progress, allowing users to use web components inside JSX templates
• The goal is to provide a cross-framework design system that can be used across different front-end frameworks.
• Adoption of web components and Lit across big companies
• Use of Lit in design systems, such as Adobe, Alaska Airlines, IBM, and others
• Increased use of web components in desktop applications and Chrome OS
• Investment by large corporations in web components due to cost savings and stabilization factors
• Concerns about governance and ownership of Lit by a corporation
• Concerns about Lit's potential for lock-in and dependency on the team
• Efforts to mitigate these concerns through simplicity, documentation, and open governance
• Exploring open governance models, including putting Lit under actual open governance
• Discussion of web components' adoption and success metrics (e.g. Chrome user metrics, NPM downloads)
• Challenges in promoting web components as a platform-first approach, including marketing and identity issues
• Balancing marketing of lit with its role as a low-level web component tool
• Challenges in marketing web components and lit's unique value proposition
• The branding exercise behind creating the "lit" name and unified messaging
• Leveraging shadow DOM for scoped styles and design system consistency
• Current state of browser support for custom elements and shadow DOM
• Lit doesn't handle styles directly, relying on browser behavior
• Shadow DOM can be limiting due to encapsulation requirements
• Open Stylable Shadow Roots proposal aims to address backwards compatibility and developer needs
• Constructible style sheets limitations hindered previous project's use of Shadow DOM
• Encapsulation vs. flexibility debate in web development standards
• Discussing migration path for users
• Kudos to Angular team for helping with custom elements
• Governance and standards discussion
• Upcoming changes in web development, including declarative shadow DOM and scoped custom element registries
• Excitement around JavaScript decorators and template instantiation
• Importance of accessibility in web components
• Scoped custom element registry proposal and Chrome's implementation
• Lessons learned from maintaining Lit, including the power of continuity and incremental progress.
• Plans for Lit 3.0 with minimal breaking changes
• Future focus on ecosystem building methods and community involvement
• Discussion of RFC (Request for Comments) process
• Reference to UpView as a model for community-led projects
• Mention of Angular's "big tent" approach and its community engagement
• Desire for the web platform to have an embeddable, high-performance subset
• Comparison of Flutter's output on the web to "hot garbage"
• The web is considered the greatest software delivery platform ever.
• Cross-platform development requires prioritizing the web due to its sensitivity to code size.
• A better solution for cross-platform development is desired.
• Lit.dev is a project where Justin's work lives, including links to social media and Discord channels.
• Justin also has a Twitter presence, despite expressing a desire to stop using it.
• He mentions missing 2018 Twitter's simplicity and the current state of online platforms as "whack-a-mole".
• The conversation concludes with discussion on upcoming Lit features, such as routing and state management.