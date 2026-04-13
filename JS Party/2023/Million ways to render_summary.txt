• Million.js: an open-source project aiming to make React and other virtual DOM environments faster
• The current React virtual DOM has a bottleneck in its reconciliation process, where it diffs every node in the DOM, leading to slow performance with large DOMs
• Million.js uses a block virtual DOM approach, which inverts this control by using static analysis to determine what nodes are dynamic and need to be updated, skipping unnecessary diffing of static nodes
• The project was started as a high schooler's experiment, but evolved into a more complex solution after trying to directly replace React's virtual DOM and failing, leading to the development of the block virtual DOM concept
• Million.js is similar in philosophy to Solid and Qwik, which use fine-grained reactivity or signals to pinpoint specific DOM nodes that need to change.
• Blockom concept introduction and limitations
• Million's accessibility to developers through React or Preact
• Virtual DOM optimization with a compiler vs runtime analysis
• Limitations of Million: UI libraries, conditional rendering, and component structure
• Compiler warnings and rules for blocks page
• API surface layer: plugin, forward component, and block call
• Compatibility with Next.js, Gatsby, Astro, Vite, WebPack, and other build tools
• Optimizer mode experimental use
• Runtime model limitations and requirements
• Core virtual DOM and loader component pattern
• Compatibility with React and other frameworks (Solid, Svelte, Preact)
• ESLint plugin development for Million
• Next.js integration and client component requirements
• Name origin of Million and mascot introduction
• Potential impact on React performance and conversations with the React team
• Making React apps faster without requiring 20 years of experience or knowing every performance optimization
• Introducing faster rendering strategies for dynamic pages and content-heavy applications
• Legacy code optimization and updating, especially in older companies with complex React applications
• Using Million as a low-effort experiment to improve performance on specific components or use cases
• Addressing the trade-off between UX and DX (developer experience) in web development
• Educating developers about when and how to use Million for various application types
• Overcoming technical constraints, such as non-deterministic components, for wider adoption
• Million is a project that aims to make React faster by peering into the virtual DOM
• The team behind Million was inspired by projects like Solid.js and Preact Signals, which challenge traditional approaches to React development
• Million's innovative approach includes block virtual DOM and off-screen rendering
• The JavaScript community is experiencing a surge in innovation, with new rendering solutions and projects like Deno, Bun, and Qwik pushing the boundaries of what's possible
• The project aims to make it easy for developers to try out new technologies and share their discoveries with others
• Million has a Discord channel where developers can contribute documentation and code, and users are encouraged to explore the project and provide feedback.