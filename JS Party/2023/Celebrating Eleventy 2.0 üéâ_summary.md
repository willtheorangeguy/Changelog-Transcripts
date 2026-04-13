• Zach Leatherman returns as guest to discuss his experiences with Eleventy over the past year.
• He discusses the upcoming release of Eleventy 2 and its new features, including use of GraphQL and React.
• The conversation turns to the re-architecture of Eleventy 2, which was not done from scratch, but does include TypeScript support.
• Zach talks about WebC, a server-rendered single-file component format for Web Components that was released by Eleventy.
• He discusses the changes made in Eleventy 2, including stripping out the Browsersync dependency and implementing its own dev server.
• The conversation also covers the investments made in the plugin ecosystem, particularly with regards to edge rendering and customized content.
• Eleventy edge functions allow server-side rendering and access to cookies, geolocation, and post requests
• Edge functions have a runtime limit of 50 milliseconds, making them lightweight and speedy
• Netlify handles the deployment process, using Deno in the cloud to run Eleventy builds on request
• The development workflow involves adding an edge shortcode to demarcate dynamic code blocks
• Eleventy's core functionality is still a static site generator, with a build-first approach
• Support has been added for Vite, allowing users to use both Eleventy and Vite together
• The plugin ecosystem enables expanded compatibility with more tools and features.
• The JavaScript ecosystem's focus on simplicity and minimizing dependencies
• Eleventy 2.0 release and its breaking changes, including the default dev server experience switch from Browsersync
• Upgrade helper plugin for easy migration from 1.0 to 2.0
• Similarities between Eleventy and Astro in terms of HTML-first approach and minimal JavaScript runtimes
• WebC as a new template syntax focused on Web Components and HTML, potentially succeeding outdated templates like Nunjucks
• Eleventy's WebC allows for component authoring without client-side JavaScript requirement
• WebC components can be progressively enhanced with client-side JavaScript interactivity
• Components can have multiple progressive enhancement strategies built in
• WebC has full control over what the progressive enhancement of a component is
• WebC supports web components and can be used to build entire pages
• WebC integrates with other template languages, including Liquid and Nunjucks
• WebC allows for arbitrary JavaScript rendering and extension support
• WebC compiler can register web components automatically
• Dynamic pages and component registration work seamlessly together
• Eleventy 2 combines with WebC for optimized static site generation
• Asset bucketing feature allows control over loading JavaScript and CSS assets
• ECMAScript modules (ESM) are a priority for future development in Eleventy 3.0
• ESM will enable asynchronous configuration files and wider compatibility
• Node's VM module does not work as well with ESM, is still experimental
• Discussion on upcoming features in 3.0 and beyond
• Explanation of "islands" (lazy-loading) in Astro and its relationship with progressive enhancement
• Use case scenarios where JavaScript might be disabled or delayed
• Demonstration of using islands for intermediary steps in web development
• WebC compiler functionality and compilation process
• Potential expansion of compilation into other areas of web development
• Discussing the flexibility of WebC to be extended by users with custom CSS processing pipelines
• Warning against adding extra dependencies to process cutting-edge features in CSS, which can lead to maintenance issues
• Mention of TypeScript implementation in browsers and potential integration with WebC
• Brief discussion about Eleventy lang and potential future development
• Zach Leatherman's availability and social media presence (Mastodon) for connecting with users