• Zach Leatherman is a guest on JS Party and has been full-time on Eleventy for over a year.
• He talks about his experience with Eleventy and how it's still going well.
• There was a rumor that Eleventy was re-architected from the ground up to use GraphQL and React, but Zach denies this.
• Eleventy does support TypeScript and JSX in version 2.
• The topic of TypeScript is discussed briefly, with some jokes about TS Party vs JS Party.
• Zach talks about new features in Eleventy, including a .11d.ts file that can be used with the ES build.
• He mentions that there was a contribution to enable this feature using ES build.
• Zach discusses his work on WebC, a server-rendered single-file component format for web components.
• He explains that WebC aims to handle common complaints about web components from framework authors.
• Discussion of WebC and its features
• Changes to Eleventy 11d2 release, including removal of BrowserSync dependency and implementation of dev server
• Investment in plugin ecosystem, including Edge rendering plugin
• Explanation of Edge rendering plugin capabilities and use cases
• Background on why BrowserSync was removed from the project
• Comparison of implementing hot reloading vs using Node's built-in features
• Edge functions and their limitations (50ms execution time)
• Netlify's on-demand builder and caching layer
• Eleventy's role in generating templates for Edge functions
• Integration of Eleventy with Netlify and Dino
• Unique approach to combining build and Edge templates
• Tension between build time and request time performance in the JavaScript ecosystem
• Comparison with other frameworks like Remix and Fresh
• Importance of portability and having a static site builder core functionality.
• Tightly coupling Eleventy with VEAT bundler is avoided to ensure long-term viability
• Eleventy-VEAT plugin allows for coexistence and benefits of both tools
• Regular Eleventy build vs VEAT plugin: asset bundling, client JS zeroing, plugin ecosystem
• Eleventy's simplicity and lightweight nature make it suitable for many sites with minimal maintenance required
• Plugin ecosystem enables scaling up from basic usage to more complex projects
• Importance of minimizing dependencies for long-term project maintenance
• Transitioning from individual contributor to engineering leader
• Coaching engineers through leadership transition
• Offering free exploratory sessions for coaching services
• Discussing a major release (11.82) and its breaking changes
• Upgrading helper plugin for migration assistance
• Comparison between 11d, Astro, and other projects in the HTML space
• The need for multiple frameworks to improve the web and the benefits of having an "HTML first" approach
• Comparison between Astro, 11ty, and WebC (Zach's new template syntax) in terms of their approaches to client-side JavaScript and component authoring experience
• Maintenance issues with certain template syntaxes, such as None Jokes for 11ty
• Features and benefits of WebC, including its bundling and asset bundling capabilities
• Demos showcasing the simplicity and effectiveness of WebC in creating interactive components without requiring client-side JavaScript.
• React limitations and restrictions on component content
• Comparison with Astro templates and WebC's freeform content approach
• Progressive enhancement in WebC and its benefits
• Control over progressive enhancement of individual components
• Balance between authoring control and automation in frameworks
• Relationship between WebC and Eleventy templating libraries
• Potential use cases for WebC at page level or within other template languages
• Discussion of WebC and its capabilities
• Comparison with other templating libraries like Liquid
• Use of JavaScript render function tag for arbitrary code execution
• Introduction to web components specifications and custom elements registry
• Importance of staying close to platform standards for longevity and maintainability
• Web components and their benefits
• Lifecycle methods and event listeners for custom elements
• Deduplication of client-side JavaScript and CSS
• WebC asset bucketing feature and its advantages
• Future plans for ECMAScript modules in 11d and static site generators
• Potential to improve compatibility with configuration files
• Unlocking first-party ESM for Node.js
• Concerns about Node.js VM module and experimental mode
• TypeScript support and compilation
• WebC integration with island architecture and partial hydration
• Island lazy loading vs progressive enhancement overlap
• Astro's islands architecture and individual component control
• Preact and island-based architecture
• Progressive enhancement and JavaScript off scenarios
• Demonstrating intermediary steps with WebC, showing pre-JS versions vs JS-enabled versions
• Handling page load cases where JavaScript is slow or unavailable (e.g. network latency)
• Using HTML parsing and compilation with WebC in Eleventy
• Potential expansion of compilation beyond Eleventy
• Discussion on WebC (Web Component) compilation and its limitations
• Potential use cases for WebC and tradeoffs in implementing it
• Eleventy Lang's relationship with WebC and other dependencies
• Nick's request to implement TypeScript support in browsers using WebC
• Zach's caution about adding extra dependencies and keeping up with specifications
• Discussion of Tailwind and its potential struggles with feature updates
• Zach's introduction to his website, Mastodon account, and upcoming appearances
• Scheduling a future episode for discussing WebC version 2
• Completion timeline: Next week
• Confirmation of readiness: Yes