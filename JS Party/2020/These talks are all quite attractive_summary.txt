• Node.js loader hooks as an experimental API for loading modules
• Ability to hook into the module loading process and perform actions such as logging, creating virtual modules, or rewriting loaded modules
• Use cases include instrumentation of Node.js processes for security, APMs (Application Performance Monitoring), and transformations like TypeScript or YAML loaders
• Potential for multiple loader hooks to be used together is unclear
• Current limitations include being able to use only one loader at a time
• Ability to mock or stub modules by changing them with a proxy is demonstrated
• Loader hooks as a solution for problems with dependencies and transpilation
• Vladimir de Turckheim's talk on loader hooks and their potential to change how modules are loaded in Node.js
• Security concerns with loading modules from URLs or streams, but no need to worry about it
• The "module attributes" feature that may allow for ES6-importing CommonJS modules in the future
• Vladimir de Turckheim's example of using loader hooks to load a gist without downloading it first
• Node.js as a universal runtime with loader hooks allowing for loading and compiling any language that can run on V8 or WebAssembly
• Marian Villa talking about her nonprofit organization PionerasDev, which teaches young women in Colombia how to code
• The growth of PionerasDev from 5 girls in 2015 to over 1,200 young women learning to code
• The Pioneras program helps young women from low-income backgrounds learn coding skills and find jobs in tech.
• The program was started in 2015 in Medellin, Colombia and has since expanded to three cities: Cali, Barranquilla, and Medellin.
• Participants start with no prior experience and learn through mentorship and self-study, eventually leading to job placement.
• The program relies on volunteers to share knowledge and mentors to provide guidance.
• Pioneras is expanding to rural areas in Colombia and has inspired similar initiatives in other Latin American countries.
• Discussion about the potential dangers of taking technology too far
• Robots used to automate tasks on Google Cloud, including CI, release management, and doc monitoring
• Bots watching bots, with safeguards in place to prevent errors
• Introduction to Probot, a framework for building GitHub Apps that interact with webhooks
• Comparison between Probot and GitHub Actions, including their similarities and differences
• Discussion of the benefits and trade-offs between using Probot and GitHub Actions
• Levels of automation for GitHub Actions and Probot
• Comparison between GitHub Actions and Probot
• Integration between Probot and Actions
• Use of Cloud Scheduler and Octokit in Probot
• Future plans for Probot, including potential integration with Actions
• SME.io service for local webhook testing
• Benefits and limitations of using Probot and Actions
• EventSource API: a unidirectional WebSocket implementation for sharing payloads between servers
• SME.io and SME client: a server-client architecture for Probot apps to receive webhook payloads locally
• Node.js worker threads: a feature inspired by web workers, allowing multiple threads within the same process to share data efficiently
• Worker threads vs. main thread: distinction between asynchronous tasks running on the event loop versus managed threads
• Constraints of worker threads: minimal restrictions compared to web workers, with most Node.js libraries available and accessible through require
• Restrictions on worker thread capabilities compared to main thread
• Stability of worker threads in Node.js versions 10 and 12
• Limitations of worker threads (e.g. no replacement for multi-process model)
• Use cases for worker threads (CPU-intensive work, image processing, machine learning)
• Shared memory and array buffers with worker threads
• Links to Rich Trott's talk and related resources are available on PalaceFamilySteakhouse.com
• Contributing to worker threads requires knowledge of Windows, C++, and debugging
• The test-worker-prof test has been stubborn and needs fixing
• Anna Henningsen wants to work on startup performance and snapshotting features for workers
• The V8 API has poor documentation