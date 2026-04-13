• Discussion about web development trends and future directions
• Two extreme approaches: JAMstack and server-side rendering with HTML over the wire
• HTMX as a library for HTML over the wire approach, developed by Carson from Big Sky Software
• HTMX's benefits: language and framework-agnostic, no need for WebSockets, improves UX expressiveness of plain HTML
• Comparison with other libraries like Hotwire, Livewire, and Turbolinks
• Feross Aboukhadijeh's perspective on reducing JavaScript code and trying new approaches
• Overview of HTMX features: dependency-free, small size (10k), can be included via CDN or build step
• HTMX allows developers to issue AJAX requests and refresh HTML content declaratively using HTML attributes
• The library aims to remove limitations on HTML's expressivity and move towards the original web model of HTTP requests and returned content
• HTMX reduces boilerplate code and makes it easier to manage complex UI interactions
• The library encourages a simpler, factored approach to backend templates and URL hierarchy
• HTMX is a front-end only library that can be easily sprinkled into existing applications with minimal impact on the backend
• The incremental approach of starting simple and using HTMX for specific needs helps avoid technical debt and over-engineering
• React vs. HTMX in web development
• Industry pressure to use the latest technology
• Concerns about code deprecation with fast-moving libraries like React
• Comparison of HTMX's stability and lack of rapid updates with newer technologies
• Active Search example demonstrating how HTMX can handle complex interactions with attributes only
• Discussion of HTMX's APIs, extensions mechanism, and design philosophy
• HTMX provides attributes for active search functionality
• Attributes include hx-post, hx-push-url, and hx-swap-oob
• Server-side integration can be achieved with plugins or by writing custom code
• Empty results can be handled through various methods, including triggering an event or using the oob swap attribute
• HTMX is extensible and has a plugin mechanism for adding custom attributes and functionality
• Discussion of similarities between HTMX and Tailwind CSS in terms of HTML-centric design
• Concept of "locality of behavior" where behavior is tied to specific code units (e.g. buttons) rather than separated into different files or locations
• Trade-offs with DRY principle, where localizing behavior can sometimes lead to repetition
• Comparison between server-side and client-side rendering, including limitations and considerations for offline-first and multi-client applications
• Discussion of REST vs GraphQL APIs, with some arguing that the term "REST" has lost its original meaning in modern web development
• Importance of decoupling JSON APIs from web applications
• RESTful APIs are often misapplied in modern web development due to the shift from XML to JSON
• JSON is not hypertext and does not lend itself to the same principles as RESTful APIs
• The industry has moved towards more generalized frontend query languages to avoid the complexity of traditional RESTful APIs
• There should be a distinction between web app-specific APIs and general-purpose APIs for clients
• HyperScript is an embedded programming language designed for front-end development, inspired by older scripting languages like HyperTalk
• The creator of HyperScript discusses its inspiration from HyperTalk, a programming language used in the past for working with events
• HyperScript allows embedding event handlers directly into HTML using a natural language-like syntax
• It offers advantages over traditional JavaScript event handling by being more general and able to handle various types of events triggered by different libraries or frameworks
• The syntax is designed to be frontend-focused, DOM-friendly, and event-friendly, allowing for easy and intuitive interaction with the DOM
• HyperScript has a "do this, then that" style similar to AppleScript, but with a more concise syntax
• The language is intended for capturing small events and simple interactions, not for creating large codebases
• Feedback on using natural language-like syntax in programming languages can be an issue, as users may try to add words that are not understood by the language
• HyperScript prioritizes read time over write time, aiming to make the code easy to understand once written
• HyperScript's syntax allows for asynchronous code without callbacks or promises
• Code can be written in a synchronous style, with the runtime handling asynchronous operations internally
• The language automatically resolves promises and creates them as needed
• This approach collapses the distinction between synchronous and asynchronous functions
• A downside of this approach is that it doesn't currently support launching multiple parallel asynchronous operations at once
• HyperScript can still handle asynchronous situations using a "settle" keyword to wait for events to complete
• Web app animation issues
• HyperScript async runtime benefits (smoother transitions)
• HTMX and HyperScript compared (practical vs experimental approaches)
• Show notes with referenced resources available
• Discussion of web development concepts and ideas