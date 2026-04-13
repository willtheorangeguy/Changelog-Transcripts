• Nick Fitzgerald's background: former Mozilla developer tools team member, author of sourcemap library
• Rewriting sourcemap library in Rust and WebAssembly, leading to significant performance improvements
• Working on a project involving running JavaScript using WebAssembly, compiling JavaScript engine to WebAssembly (SpiderMonkey)
• Project goals: improving latency for JavaScript execution, enabling JavaScript use in serverless environments where traditional JIT compilers are not available
• Introducing Wizer tool: takes snapshots of WebAssembly modules, allowing for faster initialization and startup times
• Comparison with v8 isolate startup times
• Explaining the concept of a v8 isolate as a isolated environment for JavaScript execution
• Isolates: self-contained JavaScript execution environments to prevent security vulnerabilities
• Motivation: enable JavaScript in environments where it's not typically available, such as Fastly's Compute@Edge platform and serverless environments
• WebAssembly (WASM) instances: sandboxed environments with linear memory and capability-based security
• Performance benefits: faster startup times, ability to create multiple instances quickly, and reduced overhead compared to native JavaScript execution
• Trade-offs: reduced throughput for long-running functions due to interpreter-only implementation
• Module linking proposal: enables bundling of WebAssembly modules similar to WebPack, for improved performance and security
• Moving CPU-intensive code to Rust for compilation to WebAssembly
• Linking compiled modules into JavaScript programs
• Wizer: tool that creates snapshots of dynamic environments for fast startup
• Applying optimizations like in-line caching and profiling to ahead-of-time compilation
• Goal of achieving browser-like performance through compiled JavaScript with profiling data
• Profiling and recompilation of WASM workers
• Long-term goal: dynamic linking of WebAssembly modules using Interface Types
• Limitations of current WebAssembly module interactions (e.g. no good way to communicate advanced structures)
• Introduction of Interface Types, a type grammar for defining communication between WebAssembly modules
• Importance of interface types in preventing supply chain attacks and limiting blast radius
• Interoperability between JavaScript on WASM and other environments (e.g. web browsers, Node.js)
• Copying data between modules has implications for memory management and sandbox properties
• Modules should be self-contained relative to data, with minimal communication between them
• Data ownership and access can be achieved through interface types and accessor methods
• Overhead of calling between modules is higher than function calls within a module, but still relatively low
• WebAssembly's capability-based security model makes it suitable for plugin architectures in applications like games and digital audio workstations
• Running JavaScript in a browser through WASM would only make sense if the environment is particularly constrained or needs to offload compute-heavy tasks
• WebAssembly's security model and sandboxing
• Benefits of running code in separate sandboxes
• Importance of not trusting unverified or external code
• Discussion on "Trust things less" as a guiding principle for coding and software development
• Introduction to Breakmaster Cylinder, the producer of JS Party's music