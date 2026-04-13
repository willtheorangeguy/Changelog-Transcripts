• HTMX basics
• Carson Gross' background and experience in web development
• History of Intercooler.js and its evolution into HTMX
• Differences between Web 1.0 and 2.0
• Why HTMX hasn't gained wide-scale adoption despite growing interest
• Discussion on rendering patterns and the history of web development
• The evolution of web applications from Web 1.0 to single-page applications (SPAs)
• The rise of mobile devices and their impact on web development constraints
• The increase in JavaScript usage and its performance implications
• The concept of hypermedia and its role in web development
• The HTMX library and its approach to sending HTML back and forth over the wire instead of JSON
• Hypermedia controls (links and forms) are fundamental to the web and encode interactions with remote systems within themselves
• HTMX generalizes hypermedia controls to allow any element to act as a control
• The web development community has not often discussed or extended the vocabulary of the web due to constraints and the need for control
• Legacy and built-in limitations have driven developers towards JavaScript and JSON for user experience and functionality
• The Open Web UI group is working to create better, higher-order components and make existing form elements more extensible
• HTML has been frozen as a hypermedia language since its development, leading to a reliance on JavaScript and JSON for web interactions.
• The concept of transclusion, where a document is included in another document, was discussed as a possible solution to improve usability on the web
• The idea of transclusion was considered in the 1970s and 1980s but ultimately did not become widely adopted
• This led to the development of JavaScript-heavy applications, which created a "thick client" approach that abstracted away from HTML
• The adoption of JSON as a data format further increased the complexity of web development
• The current state of web development is characterized by a lack of understanding of how to work with the browser's primitives, leading to unnecessary complexity and cruft
• React was mentioned as an example of a framework that does not feel natural or intuitive to use
• The discussion also touched on the idea that web developers have been working against the grain, trying to manage complex tasks in JavaScript instead of leveraging the browser's capabilities
• The complexity of state synchronization in web applications
• The overemphasis on single-page application frameworks and complex tooling
• The role of fear of looking dumb and the desire to appear intelligent in enabling excessive complexity
• The fetishization of being a "bus factor" expert and the resulting lack of incentivization for simplicity
• The importance of prioritizing user needs and solving problems that users face, rather than solely focusing on developer experience
• The need for engineering leadership to set standards and prioritize simplicity in web development
• The importance of placing responsibility on the right individuals and teams when making technology decisions
• The concept of "performance management maturity" and how complex stacks can lead to complexity and problems that are difficult to solve
• The idea that teams that struggle with performance issues often have adopted complex technologies that they don't fully manage
• An introduction to HTMX, a JavaScript framework for building web applications using hypermedia controls
• The core attributes of HTMX and how they generalize the concept of hypermedia controls in HTML elements
• Examples of how HTMX can be used for tasks such as lazy-loading and improving user experience through simple patterns.
• Discussion of HTMX's transclusion feature and its similarity to JavaScript's islands architecture
• Introduction of "Ajax with attributes" and the built-in attributes provided by HTMX (hxget, post, patch, put, delete)
• Explanation of how these attributes generalize hypermedia controls and allow for event triggering and request issuance from any element
• Mention of HTTP methods that are not directly accessible from HTML (put, patch, delete) and their importance
• Debate about whether to use the "data-" prefix in attribute names, with Alex Russell stating it's not a significant concern
• Discussion of the benefits of focusing on HTML-first development and welcoming back CSS/HTML experts who were previously overshadowed by JavaScript developers
• Talk of prioritizing performance and user experience over deep JavaScript sessions and complex local data models
• Introduction to the concept of "session depth" and its relation to web app architecture, with a question about when HTMX is not a good idea for a particular task.
• Roy Fielding's dissertation forms the basis of REST and HATEOS/hypermedia as the engine of application state
• Coarse-grained hypermedia interactions vs fine-grained event handling
• Island architecture and integration with broader hypermedia system using events
• HTMX and its suitability for applications with shallow sessions and few interactions (e.g. Google Maps)
• Importance of understanding user session depth and optimizing for it in app architecture
• Trade-offs between client-side infrastructure, runtime offloading, and local data models for syncing
• Need to disaggregate apps into different experiences and optimize each one separately
• Using data to inform decisions on app architecture and user experience.
• The benefits of breaking down complex tasks into more manageable paths or modes
• Prioritizing user success over a single highly engaged user
• Education gaps in engineering leadership and product management regarding data-driven decision making
• Setting benchmarks and using analytics to drive architecture decisions
• Managing technology versus being managed by it, with examples from teams that have successfully implemented this approach
• The importance of management support for large-scale technical changes
• The hype cycle surrounding React and other JavaScript frameworks is creating unrealistic expectations and hindering honest discussions about their limitations.
• Some engineers feel pressured to adopt React due to its perceived ease of hiring and maintenance, despite the potential costs and complexity involved.
• Alex Russell argues that this thinking is based on a flawed assumption that developers who know React are incapable of learning other technologies.
• Carson Chubb discusses how HTMX can be used to "save complexity" by leveraging platform fundamentals and reducing unnecessary JavaScript code.
• The conversation touches on the importance of understanding the web platform as a whole, including CSS, HTML, and JavaScript, for effective development.
• There is a desire to move beyond polarized discussions between React proponents and HTMX advocates, and towards a more nuanced understanding of the trade-offs involved in different technologies.
• Full stack development and the crisis of identity around frontend and backend
• Web Components and HTMX integration
• Lit elements and their ease of use with web components
• The importance of events in integrating client-side enhancements with HTMX
• Generalizing hypermedia controls and making accessibility accessible by default
• Reparenting DOM elements without losing state, a feature that would enable stable transclusion
• Discussion of the importance of JavaScript and its role in web development
• The concept of "three to tango" (JavaScript, CSS, HTML) for a well-functioning web application
• Carson's contribution to paradigm shifts in web development
• Introduction of new Core Web Vital: interaction to next paint
• Browser choice and competition
• Open Web Advocacy Group and their efforts to promote the open web
• Safari's support for PWAs and its limitations
• DHH's experience with Apple's App Store approval process
• Importance of fighting for the open web
• Maintainers in need of marketing help
• Carson's background and software company (BigSky.software)
• Alex Russell's online presence (infrequently.org) and blog
• Montana State University as a potential location for learning from Carson
• HTMX and Lit libraries, with encouragement to play around with them