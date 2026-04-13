• Introduction to SpiderMonkey and its history
• Overview of Yulia Startsev's background and career path
• Discussion of her involvement with TC39 and compiler development
• The role of perseverance in software development
• Importance of diversity in browsers for a healthy web ecosystem
• Overview of Yulia's work on the SpiderMonkey team, including proposal reviews and engagement with the committee
• Yulia Startsev's current work is focused on Gecko, the DOM engine in Firefox, specifically on loading JS modules into workers
• She has a livestream where she gives guided tours through complex features implemented in Firefox, currently paused due to her starting university
• Her livestream will resume with a series on top-level await proposal, which she was involved in specifying and implementing in Firefox
• Yulia is pursuing a master's degree in computer science, focusing on compilers and languages, and finds it rewarding to apply theoretical knowledge to practical work
• The panel discusses the benefits of continuing education throughout one's career, including refreshing their understanding of concepts and applying new knowledge to real-world problems
• Challenges of continuing education in a career
• University-style education, exams, and their limitations
• Language design and the importance of formal specification, soundness, and performance
• Compiler development and its connection to language design
• Collaborative decision-making in language development (e.g. TC39)
• The human side of technical work, including communication and collaboration
• Introduction of TC39's 4-stage process for proposing new language features
• Stage 0: Idea generation and discussion in Discourse (TC39 website)
• Stage 1: Problem statement and investigation, including creation of a proposal repository on GitHub
• Stage 2: Drafting the final spec text and ironing out problems
• Stage 3: Reviewing the proposal for potential issues before implementation
• Stage 4: Specification and implementation
• Competing ideas and implementation options are debated within proposals or through forks, with decisions made through discussion rather than voting.
• The development of ES5 was delayed due to the complexity of the original specification, leading to a "backpocket" proposal for incremental improvements.
• A similar backpocket proposal was considered for private fields, but ultimately decided against in favor of the original solution after careful evaluation.
• Polyfillable implementations are an important consideration in language design, and proposals must be carefully reviewed to ensure they can be polyfilled if necessary.
• The JavaScript committee has a set of unwritten "intrinsic" values that guide their decision-making, including prioritizing polyfillability and protecting critical features of the language.
• The committee is working on formalizing these intrinsics into the normative text of the specification.
• Decision-making in the committee requires unanimous agreement not to block a proposal; one person can hold up progress if they object.
• The process allows for constructive feedback and discussion, with a focus on providing reasons for blocking or rejecting a proposal.
• Political machinations in deciding on technical standards
• Governance models for standardization bodies
• Argumentation Theory and study of decision-making processes
• Differences between HTML and ECMA governance structures
• Browser vs embedder interests in JavaScript proposals (example: realms proposal)
• Proposal to integrate HTML APIs with JavaScript
• Availability of realms proposal for testing through polyfill or Firefox browser
• Realms as a feature to provide better permissioning for Node.js packages, allowing developers to restrict modules' access to certain resources.
• Encapsulation of logic using realms to maintain program integrity, rather than relying on security features.
• Discussion around running malicious code in realms and its potential consequences.
• LavaMoat project as an example of using realms to restrict package permissions.
• Compartments proposal as a related concept allowing for restricted access to certain APIs.
• Realms' limitations as a security boundary, with emphasis on integrity rather than strong security.
• The browser loads HTML and starts parsing it incrementally
• Script tags are encountered, triggering script loading and execution
• With modules, the entire module tree is fetched and parsed ahead of time before evaluation
• SpiderMonkey engine engages at the point where code is ready to be parsed, taking care of parsing and executing scripts
• Modules have a different representation than regular scripts, with a list of other scripts to load
• Deferred module loading proposal allows developers to delay execution of modules until they are needed
• Current implementation can lead to slow startup performance due to the need for both fetching and parsing of modules before evaluation
• React's use of algebraic effects to hide asynchronous code complexity
• Exposing the module loader for custom logic around loading
• Deferred module evaluation as an alternative approach
• Impedance mismatch between async and sync in web development
• Language design considerations for mental model and problem-solving
• The importance of simplifying complex web concepts for developers
• Buying domain names and trying to acquire specific ones
• Importance of being timely when registering domains like .xxx
• Creative uses for domain names (e.g. Feross.org, hag.codes)
• Personal stories of struggling to obtain desired domain names
• Proposal to create a podcast about the topic of domain names