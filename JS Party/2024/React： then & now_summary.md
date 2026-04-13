• The hosts of JS Party discuss their love for Fly.io
• Kurt Mackey explains how he pitches Fly.io to developers, highlighting its unique capabilities
• He describes the limitations of platforms like Heroku and Vercel
• The concept of a "no limits" platform built for developers is introduced
• Tom O'Kino joins the conversation as a special guest, introducing himself as Chief Product Officer at Vercel
• They discuss the behind-the-scenes story of creating React, including its early days and development
• The speaker discusses the creation and early adoption of React
• Jordan and others on the product infrastructure team developed a prototype for React based on emerging needs in the company
• In-house framework Bolt, which was influenced by Backbone, was used but became too complex as the team grew
• JSX and the idea of components being one unit were initially met with criticism at JSConf
• Pete Hunt later explained the problems React aimed to solve, such as loose coupling between components and high cohesion within them
• React's adoption was gradual and not forced, with no claim that it's a complete solution
• Discussion about a past problem and solution with Pete
• Separation of concerns and JSX syntax in early React
• Importance of component mindset in development
• Shift from top-down to component-oriented approach
• Evolution of UI decomposition and component-oriented development
• Declarative way of describing components and UI
• Limitations of early React and community filling in gaps
• Architecture designed with server-side rendering in mind
• Core team's goal to make external libraries thinner and more expressive
• Introduction of React and its focus on view layer at the time
• React vs framework, definition and purpose
• Early adoption of React in conjunction with other libraries (Backbone)
• Incremental adoption and escape hatches for React
• Facebook's use of React for internal needs, not external marketing goals
• Vercel's business model and open source investment
• Comparison of experience at Facebook vs Vercel on open source development and customer connections
• Business outcomes and funding models for open source technologies (Next.js)
• Improving developer experience in service of user experience
• Moving data fetching code back to the server for efficiency and coalescing data
• Server and client-side benefits: server for data orchestration, client for interactivity and real-time feedback
• React server components and the shift towards a more efficient web application delivery model
• Supporting new devices and platforms beyond mobile
• Raising the baseline for developer experience to create better user experiences
• Continuation of React's influence through Vercel's Next platform
• The evolution of technology and infrastructure management
• Undifferentiated heat loss engineering: manually provisioning compute resources
• The benefits of framework-defined infrastructure (e.g. Next.js) for automating infrastructure management
• Vercel's managed infrastructure and the build output API for deploying apps on demand
• Creating constraints in architecture to enable automatic inference of necessary components
• Constraints for automatic scaling and management of software architecture
• Static vs dynamic resources, including caching and compute requirements
• Stateful resources and databases in AI applications
• Long-lived LLM outputs and efficient on-demand compute
• Connecting to various stateful and dynamic backends
• Primitives and pieces that make sense for LLM-based applications
• Application layer needs for LLM success
• Generative UI (GenUI) and its potential for approachable and sophisticated applications
• Context-aware soft buttons
• On-demand UI with customizable patterns
• Progressive disclosure of features
• LLMs improving user experience and quality of software
• Declarative UI and moving away from imperative coding
• Using AI to describe application behavior and outcomes
• Entering the era of personal software
• Discussion of using AI to generate different sky backgrounds
• Importance of progressive disclosure of complexity in tool guidance
• Role of conferences like React Summit in bringing communities together and sharing ideas
• Benefits of attending conferences in person, including building lifelong friendships and collaboration
• Comparison between virtual and in-person conference experiences
• The importance of local meetups and connecting with people
• The evolution of React and its community, including the reigniting of interest in web development as a platform
• Investment in web technologies and the web platform to make it "win"
• Introduction to WorkOS' AuthKit, an API that covers various authentication methods, including two-factor auth, password auth, and integration with third-party systems
• AuthKit is a tool for adding authentication to any app, not just Next.js
• It comes with a hosted login box that can be customized and has a modular design allowing for headless use of backend APIs
• AuthKit is integrated with the WorkOS platform, making it easy to add enterprise features as needed
• The tool is free for up to 1 million users and is designed to future-proof authentication systems for growth
• Companies that anticipate growing into the enterprise market can start using AuthKit early on to avoid needing to re-architect their authentication stack later
• A browser plugin called Jam helps teams capture bugs quickly for faster debugging
• The plugin hooks into DevTools and captures console logs, network requests, session information, and more
• It creates a link with all the necessary info to debug the issue, eliminating follow-up questions
• Jam aims to save time for developers by making bug reporting easier and faster
• It's free to use and available at jam.dev
• The conversation also discusses React Summit and a talk given by Shruti Kapoor about React 19
• Discussion about new features in React 19
• Clarification on what constitutes React 19 (server components, compiler, and actions)
• Explanation that these are separate but related features, not a single entity called "React 19"
• Mention of server components being introduced around version 18 and now being stable
• Confusion about the lines between different features and their implementations
• Discussion of React and Next.js framework choices
• Impression that React new features are overwhelming for developers
• Explanation of RSCs (React Server Components) being familiar, but Actions a new concept
• Description of Actions as a way to write async transitions as functions for form submission
• Introduction of the Action DOM method for submitting forms client-side and server-side support
• Transition hooks and their changes in React 19
• Form submission states (pending, appending)
• Error handling with transition hooks
• Introduction of the React compiler as a plugin in React 19
• Auto-compilation and memoization features of the React compiler
• Opting into the React compiler through Babel plugins
• Installing a plugin is sufficient for it to work
• Babel plugin works with Vite projects
• Use hook allows reading resources, including context and promises
• Use hook does not follow the same rules as other hooks
• It's possible to compose context in different ways using use hook
• Use hook can read resources such as context, promises, or suspense library results
• It may replace something like React Query for simple use cases
• React Query vs simple use cases
• How React Query interacts with the rendering path
• Whether React Query suspends or replaces rendering
• Use of React Query as an API, not a hook, allowing for conditional calls and placement in components
• Suspense feature in React and its relation to React Query
• React 19 breaking changes: suspense components resolve sequentially instead of asynchronously
• Issue with React 19 causing suspense to act like a waterfall, leading to long rendering times
• Problem fixed by reverting the problematic change
• Discussion about AI and LLMs (Large Language Models) and their potential impact on adoption of new features in frameworks like React
• Adoption of new features not delayed due to LLMs' lack of knowledge; users with different use cases and needs than those who adopt LLMs
• Optimizing code for performance
• Validating AI-generated code
• Using AI as a tool in coding, rather than relying on it
• Benefits of using tools like Cursor AI and Augment to speed up development time
• Adoption of new technologies and potential impact on developer productivity
• The user mentions they posted two days ago and were able to get a side project up and running quickly with the help of Cursor.
• The user compares their experience with Cursor to using chat GPT, saying it has increased their performance more.
• The user expresses a preference for NeoVim over VietzCode.
• The conversation moves to ReactConf and the speaker's experience attending the conference so far.
• The speaker discusses the audience's reaction to new features in React 19 and describes the talks as amazing.
• Meeting new people at the conference
• Community building and mentorship for those newer to JavaScript or the tech industry
• The challenges of feeling alone in struggles, being perceived as an imposter, and having a vulnerable side
• Sharing personal experiences through fireside chats to show that everyone faces challenges
• The importance of empathy and acknowledging that others are facing similar problems
• Feeling like an imposter due to social media perceptions vs. reality
• Recognizing that everyone, even professionals, struggle with code or tasks for extended periods
• Understanding that mistakes and struggles are common among developers
• Emphasizing the separation between one's identity and their work/output (code)
• Conferences provide a deadline to learn new things and stay up-to-date
• Conference-driven development is beneficial for staying motivated and engaged
• Sharing knowledge with others can be rewarding and help you feel like you're doing something worthwhile
• Accessibility in web development is an exciting area that requires careful consideration of various needs and perspectives
• Building accessible components can make a developer better equipped to handle various use cases and user requirements
• The importance of vulnerability and openness in exploring new areas of expertise
• The vastness and complexity of front-end development, particularly in accessibility
• The need to accept that one cannot be an expert on everything and it's okay not to know everything
• Creating accessible components that can be easily embedded and used by others without requiring deep understanding of nuances
• Designing internal components for use within a system rather than exposing them via a UI
• Transitioning from JavaScript to TypeScript
• Discussion of the speaker's initial dislike for type systems in JavaScript
• Benefits of using TypeScript for team collaboration and error prevention
• Use of TypeScript contracts to ensure accurate passing of variables and attributes
• Personal experience with TypeScript eliminating the need for Chrome debugger usage
• Type safety and contract features in TypeScript
• Benefits of baked-in type systems, such as accessibility and reduced developer burden
• Transitioning to typed HTML
• Speaking at conferences: overcoming self-imposed hurdles and preparation requirements
• Encouragement to submit a conference talk topic and apply for a speaking spot
• Conferences and meetups as opportunities to speak
• Debates about React's relevance in the industry
• Importance of learning React, especially for front-end job security
• Transferability of React concepts to other frameworks and technologies
• Shruti Kapoor's appearance on JS Party podcast
• Year-end merch sale at Changelog.com
• Discounts up to 40% off while supplies last
• Partners mentioned: Fly.io and Sentry
• Special offer for Sentry team plan using code CHANGELOG
• Shoutouts to Breakmaster Cylinder (BMC)