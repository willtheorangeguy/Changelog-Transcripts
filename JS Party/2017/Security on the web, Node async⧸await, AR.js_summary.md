• Google's announcement about Internet security flaws
• SHA-1 hashing algorithm has been cracked
• Discussion on the impact of SHA-1 being broken
• Explanation of how SHA-1 works and its uses in Git
• Concerns about the ease of forging hashes and the potential for malware injection
• The speaker discusses the relatively insecure nature of "shot one" and how its continued use has been debated in the security community since 2005.
• Alternative algorithms are available that don't have the same problem, but shot one is still widely used due to Linus Torvald's skepticism.
• Google and German researchers publicly revealed a method to crack shot one, making it clear how they did so.
• The attack requires significant computing power (over 100 years of time) but will become more feasible as technology advances.
• Using "shot two fifty six" is recommended instead, which has higher entropy and is essentially the same algorithm with some improvements.
• Multi-hash is a format that allows for optional support of different encryption algorithms and hashing functions to future-proof applications.
• Security on the web is a multilayered concept, and breaking one layer doesn't make the others secure
• Using Cloud Slayer or SSL/TLS can provide security, but it's not enough
• A single weak link in authentication can compromise the entire system, making a chain or linked approach more effective than an onion metaphor
• OAuth initially used extra encryption to protect against HTTP without TLS, but later dropped this practice when using TLS
• TLS can be compromised by certificate authorities being hacked, so relying solely on it for security is not enough
• Mozilla Observatory is a useful resource for checking website security and providing a prioritized list of improvements
• PCI determines algorithms for storing credit card numbers and other sensitive data
• Don't implement security measures yourself, use well-known libraries instead
• Cryptographic techniques like SHA-1 are not recommended, use alternatives like Bcrypt or Sodium encryption
• Use CI tests to check for known vulnerabilities in dependencies like NPM packages
• Utilize services that scan open-source modules for vulnerabilities and offer patching solutions
• Node.js version 7.6 release
• V8 engine update and ABI changes
• Async/await feature now enabled by default in Node.js
• Performance concerns and comparisons to callbacks and promises
• History of promise standardization and competing standards (A+, B, C, D)
• Dominic Nicola's work on promoting a unified promise standard
• Browser API inconsistencies for IO handlers
• Benefits of having a standardized async/await feature
• Discussion of native promises in Node.js and their limitations
• Comparison of native promises to other libraries such as Bluebird
• Async await feature as syntactic sugar for promises
• Error handling with promises, including error eating and tracking
• Performance considerations with async/await
• Indifference towards code preferences and the lack of controversy
• Node's error handling conflicts with the way node handles errors
• Production systems have issues with promises swallowing errors
• A style argument exists between object-oriented and functional programming approaches to promises
• Callback hell is a common issue in asynchronous coding
• Async functions and generators are alternative mechanisms for asynchronous coding that don't swallow errors
• Coroutines and the co library are used in some cases, particularly in China
• The async module was an early attempt at bridging the gap between callbacks and promises
• Community growth and imitation in software development
• Comparison of node bots and web application development
• Challenges with sequential actions and asynchronous programming
• Performance arguments for promises vs native functions
• Personal preferences and opinions on callback hell and promise usage
• Feature Project of the Week: ARJS
• ARJS (Augmented Reality for JavaScript) is a library that uses ARToolkit and A-Frame to blend augmented reality with digital markers
• ARJS can be used with Android phones, but not iOS phones due to technical limitations
• The library allows developers to create interactive 3D objects that appear as holograms when viewed through a phone or device
• A-Frame is a popular tool for creating WebGL VR in the browser and is being used as the foundation for ARJS
• The library has good documentation and runs at 60 frames per second on devices such as the Nexus 6
• Discussion of Leap Motion device and its capabilities
• Possibility of using Leap Motion with augmented reality applications
• Mention of Mayo armband for hand tracking
• Comparison of Leap Motion and Mayo armband features
• Idea of combining Leap Motion with other technologies (e.g. Maya) to create interactive experiences
• Reference to past examples of innovative demos (e.g. Emscripten compiling Doom)
• Discussion of future possibilities in augmented reality, including drawing shapes on paper and manipulating them in 3D space
• WebGL programming experience
• A-Frame and 3JS libraries used for development
• Regal library as an alternative to 3JS, with improved tooling and debugging
• Makola Lysenko's work on Regal and its features
• Bits.coop consulting business and its cooperative model
• Observatory security checker from Mozilla
• Marco Kosaka's talk on computer pixel reading
• Discussion of Maria Kosaka's talks and her approach to explaining complex concepts
• Plans to feature library, project, or talk spotlights every other week
• Mention of links in show notes for further information
• End of episode announcements (rating, subscribing, etc.) 
• Upcoming live podcast schedule (Fridays at 3 p.m. U.S. Eastern)