• Introduction to Dan Abramov and Eric Clemmons
• Discussion on Dan's role in the React team and his current involvement with BlueSky
• Eric Clemmons shares his experience with React, including its early adoption and success
• Click to Component library mentioned as a tool for improving developer experience (DX)
• Amal Hussein asks about their React love stories
• Overview of the evolution of React and its impact on web development
• Discussion of why some developers' initial enthusiasm for React has waned over time
• Mention of Suspense and concurrency features as potential reasons for decreased performance focus in React
• Developers' personal experiences with React, including its benefits (e.g. improved performance) and challenges (e.g. API design)
• Comparison between early adopters' experience of React and the current state of the framework
• Discussion of how React's success has led to a broader adoption of JavaScript ecosystem tools and technologies
• React's early adoption and its shift from client-side components to server-side rendered revolution
• The evolution from traditional server rendering (PHP, Rails) to single-page apps with JavaScript-only approach
• React's role in popularizing the single-page app paradigm, especially with the introduction of Create React App
• Challenges with SPAs, including performance issues and complex mental model requirements
• React uses a client-side rendering approach, where the initial UI is generated on the server
• Server-Side Rendering (SSR) in React was made possible by using the `renderToString` function to generate an HTML string from the client-side app tree
• Next.js built upon this concept and introduced filesystem-based routing and built-in code-splitting
• The performance of `renderToString` was a concern, but optimizing it would not have been effective due to its synchronous nature
• Facebook used React's Suspense API to address their performance issues with SSR by streaming server rendering
• Using React led to significant performance improvements (from 800ms for PHP to 40ms) and enabled efficient UI composition and data fetching
• The speaker discusses how React has evolved over time to address web problems such as data fetching, latency, and caching
• They compare current React to 10-year-old React, noting that it's honed in on solving real web problems with better abstractions
• Eric Clemmons mentions the "uncanny valley" problem where server-side rendered applications send serialized HTML that looks interactable but isn't
• Dan Abramov explains how Suspense and Server Components address this issue by sending code in chunks, allowing for interleaving of data and UI
• The conversation touches on Facebook's use of BigPipe technology to stream pagelets (independent sections) with their own dependencies, which inspired the development of React's Suspense API
• Code chunking allows for faster processing and better prioritization of what loads first
• React Server Components (RSC) combines traditional request/response mental model with client-side paradigm
• RSC solves the problem of data fetching as a first-class React primitive by allowing components to span both server and client worlds
• Traditional React can't handle components that depend on data from multiple sources, but RSC allows for splitting component execution between server and client
• Async components in React
• Server Components (RSCs) allowing async operations on the server
• Avoiding performance issues by executing async tasks ahead of time on the server
• Client-side vs server-side rendering
• Compositionality and reusability of full-stack components
• Changing mindset from client-first to server-agnostic programming
• Client-first mentality can lead to misinterpretation of React components accessing databases
• Misconceptions about RSC (React Server Components) mixing client-side and server-side code in the same file
• Conceptual shift from traditional data fetching to making it first-class within components
• Potential for animations between trees by sending JSX and re-rendering without DOM destruction
• Network tab behavior: sending HTML for initial load, JSX tree for navigations
• Embedding interactivity into tags through JSON format and module IDs for client-side code download
• The structure of React Server Components allows them to be sent as a tree-like JSON object, enabling progressive loading and streaming of content
• This approach also enables sending less JavaScript code to the client by running some logic ahead of time on the server
• Server Components can return client components, which can then be executed on the client-side, allowing for dynamic behavior
• The use of Server Components automatically enables code splitting, where only necessary code is sent to the client
• This model also allows for nested client components within Server Components, further reducing the amount of code sent to the client
• Bundler integration is required for benefits of server-side rendering
• 'use client' and 'use server' directives mark boundaries between client and server code
• Directives are not just about marking components as client or server, but rather where the boundary between client and server data transfer occurs
• Migration from Next.js pages directory to app directory involves moving page component to a separate file and adding 'use client' directive at top of that file
• Server components serve similar function to getServerSideProps in old Next.js and Astro templates
• Tightly integrating with bundler allows for smarter optimization, but maintaining intentional boundaries between client and server code is important.
• Discussion of bundler capabilities and limitations in handling server-client separation
• Conceptual shift in thinking about server and client as two separate programs with doors into each other
• Challenges in retrofitting existing bundlers to support this paradigm
• Overview of React Server Components (RSC) specifications and their evolution
• Role of bundlers like WebPack, Parcel, and Turbopack in supporting the RSC paradigm
• Need for custom linting rules and type enforcement to ensure best practices with server-client separation
• Comparison of Next.js's early adoption and support for RSC versus other frameworks
• Server Components design started in 2017 at Facebook with an internal post "What comes after GraphQL"
• Technical limitations prevented Facebook from deploying Server Components
• Sebastian left Meta to continue developing Server Components elsewhere
• Vercel invested in and supported Sebastian's vision for Server Components, leading to significant development and resource allocation
• Next.js was rewritten to support Server Components, creating a moat around the platform that others may struggle to catch up with
• The goal is to make Server Components framework-agnostic and easily adoptable by other frameworks
• React Server Components (RSC) and its relationship with Vercel
• Commercial vs open-source perspectives on RSC
• Apple's vertical integration model and its influence on RSC design
• Misconceptions about the name "React Server Components" and its conceptual meaning
• Getting started with RSC, with Next.js being the most complete implementation
• Production-readiness of RSC as of February 2024
• React App Router's stability and readiness for production use
• The need for more resources and best practices to help developers understand the conceptual model of App Router
• Similarities between App Router and early versions of React in terms of maturity and learning curve
• The importance of composability in web development, particularly with animations
• Desire for deeper, first-class support for animations in React, enabling easier composition and animation of components.