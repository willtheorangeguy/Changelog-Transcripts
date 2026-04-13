• Jason Miller discusses his project WMR (initially intended as a joke)
• Alternate names are suggested for WMR, including Windows Me Returns and Waldo's My Roommate
• Jason explains the initial intention behind the name and the team's struggles to come up with a better one
• The conversation devolves into humorous discussions about rodents and taxonomy
• Nick Nisi offers to write a Neovim plugin that will submit PRs to update the project's README with new names
• Jason Miller confirms that WMR is a tiny all-in-one development tool for modern web apps
• Modern web app definition: A modern web app assumes modern browsers, UX, dependencies, and toolchain optimized for ES modules and TypeScript.
• WMR (Web Modular Router) stance: Focus on supporting newer dependencies without compromising their performance to support older modules.
• Comparison to existing tools: Closest to Vite, Snowpack, and es-dev-server in terms of ESM-first bundlers/non-bundlers.
• Goal: To create a tool that minimizes developer effort by removing unnecessary configuration steps and using default settings based on project requirements.
• Default settings extraction: WMR extracts possible defaults from the code written, rather than imposing them as configurations.
• Optimization techniques: WMR uses compression thresholds, TCP window sizes, and other evidence-based defaults to optimize production output.
• WMR's similarity to config inference and style inference
• WMR generates a Rollup config based on the codebase in production mode
• Development process: WMR doesn't bundle, instead ships modules over HTTP as requests
• Optimizing module loading by skipping unnecessary transformations
• Node dependency management through streaming install from npm registry
• Inference of dependencies and exports for optimized development experience
• Inference of file extensions for imports in WMR
• Rollup bundling process and native ESM usage
• Concatenation of modules for faster loading
• Minification and Brotli compression of dependencies
• Rewriting of bare specifiers to URLs
• Support for TypeScript and JavaScript files without extensions
• Debug environment variable for plugin execution stats
• Default template shipping with .js extension, but supporting TypeScript by default
• TypeScript support for JavaScript projects
• WMR (Web Modular Router) tooling and its relationship to Preact
• Export maps as a way to publish modern JavaScript packages
• Bundler ecosystem and standardizing modern code shipping
• Development experience improvements with HTTP/2, ES modules, and hot module reloading
• WMR export maps implementation could be extracted into a separate package for broader use
• Preact is the default in create-wmr due to its testbed role, but API is independent of Preact
• Prerendering in WMR can be adapted to other frameworks and libraries like Vue, React, or Svelte
• Create-wmr package should allow easy adaptation to different frameworks through config files
• Collaboration vs. competition between tools and libraries in the ecosystem is a complex issue
• Discussion of using a faster language for JavaScript transformations and minification with esbuild
• Review of the Web Modernization Report (WMR) and its experimental PR, which uses esbuild and has shown great performance
• Rationale behind not publishing WMR's underlying packages as independent projects
• Overview of WMR's benefits, including ease of use and speed for development and production apps
• Discussion of scaling limitations and potential issues with large projects (e.g., 2,000 source files)
• Explanation of how npm dependencies are cached and affect performance
• WMR (Workspaces Manager) is built on top of Rollup and uses its standard tools for production, including Terser for minification.
• The default browser support for WMR is modern browsers, but it includes a one-file plugin that runs bundles through Babel to create polyfilled files for legacy browsers.
• The main difference between WMR's production output and other tools is minimal, and Rollup is considered the "gold standard" for production output.
• WMR's server is designed for development and bundling purposes only, not intended as a production server; it was created to give an accurate local representation of production.
• Next.js is a runtime that serves applications, whereas WMR aims to be a static-site generator-focused tool, with the ability to bundle frontends using its middleware.
• Users can integrate WMR with other tools like Eleventy for more complex use cases, and it supports plugins for features like page-based routing.
• Introduction of Jason Miller and his work on WMR
• Links to Jason's online presence (Twitter, GitHub)
• Show notes with links to discussed topics
• Discussion of Jason's contribution to web development tools
• End-of-episode wrap-up and appreciation for guest's effort
• Outro with Horse JS comment about Node.js dark mode