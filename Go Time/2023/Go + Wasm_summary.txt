• Introduction to WebAssembly as a memory-safe sandboxed execution environment for cross-platform code execution
• Common use cases for WebAssembly, including bringing functionality to web browsers (e.g. Figma), games, and data analysis tools
• Discussion of performance benefits of using WebAssembly over JavaScript, especially for complex computations and edge computing applications
• Edge computing as a key area where WebAssembly is gaining momentum due to its ability to scale quickly and efficiently
• Comparison with JavaScript's JIT compilation process and V8 engine, highlighting the near-native speed advantage of WebAssembly
• Using Go code with WebAssembly
• Compiling existing Go code to WebAssembly using tools like TinyGo
• Benefits and challenges of using WebAssembly for performance, binary size, and data exchange between native code and WebAssembly code
• Strategies for serializing and deserializing complex data structures in memory between native layers and WebAssembly
• Use cases for WebAssembly at DevCycle, including feature flagging tool that requires a common WebAssembly codebase across multiple environments and languages
• Experience of the DevCycle team with the maturity of the WebAssembly community and its adoption by other companies
• WebAssembly's growth and maturity
• Expanding use cases for WebAssembly beyond browser execution (server-side, edge runtimes)
• Early adoption of WebAssembly by companies like DevCycle
• AssemblyScript as a tool for building WebAssembly modules
• Challenges with writing efficient code in AssemblyScript
• Trade-offs between ease of development and performance optimization
• Optimization challenge with a global CDN network built on Go codebase
• Initial WebAssembly performance was too slow, evaluated variables in 2-3 milliseconds each
• Reduced data passed across module boundary by identifying and removing unnecessary data
• Implemented static buffer for passing data between host and Wasm module
• Avoiding memory allocation and sharing memory more efficiently led to significant improvements
• Measured performance using Go benchmark tests and CPU profiling tools, including pprof and Node.js's native support for WebAssembly
• Identified slow calls within the WebAssembly code through detailed analysis of CPU profiles
• WebAssembly optimization and tooling
• Investigation of memory size issues and potential leaks
• Use of AssemblyScript compiler plugins for profiling and debugging
• Comparison of different languages for compiling to WebAssembly (C++, Rust, Go, AssemblyScript)
• Impact of garbage collection on performance in WebAssembly applications
• WebAssembly performance issues are often due to garbage collection and memory management
• Garbage collection in WebAssembly is currently the responsibility of the runtime, but a proposal aims to expose it to the host runtime for more efficient management
• C++ has an advantage over other languages when compiling to WebAssembly due to manual memory management, which can improve performance
• Concurrency model differences are a challenge when working with WebAssembly, particularly in environments like Go where concurrency is expected
• A proposed solution involves creating multiple instances of the WebAssembly module and shuffling between them for concurrent access
• Platform-specific code may be required for optimal performance in certain languages or use cases
• WebAssembly (Wasm) may replace container-based runtimes like Kubernetes and edge workloads by 2030 due to its advantages in security, speed, and scalability.
• Current barriers to Wasm adoption include language support, profiling, and tooling.
• The WebAssembly community is working on several key changes, including the component model, multi-threading, and native garbage collection support.
• A higher-level language that executes efficiently in Wasm is necessary for widespread adoption.
• The security benefits of Wasm may lead to its use in mission-critical applications where security is a top concern.
• Wasm's speed and small binary size can also result in significant cost savings compared to traditional containerized runtimes.
• Discussing cost advantages of small, portable, and fast runtimes at the edge
• Unpopular opinions on bringing laptops into movie theaters and using Kubernetes
• Criticism of Kubernetes as overused in the tech industry, particularly for smaller companies or edge workloads
• Nostalgia for Heroku and its ease of use for deploying code, but criticism of its scalability and pricing issues
• Discussion of the benefits of usage-based billing for edge runtimes and services
• AI hype cycle is compared to previous tech fads (NFTs, 3D printers)
• Large language models (LLMs) are valuable but not yet artificially intelligent
• ChatGPT has real-world value in tasks like coding and document creation
• The term "AI" is misleading, as it implies a level of intelligence that LLMs do not possess
• AI should be evaluated for its incremental improvements, rather than expecting perfection
• There are potential dangers to using AI when the correct answer is unknown
• Self-driving cars are an example of AI's incremental progress
• AI and its potential applications
• Lane following technology on highways
• Limitations of current AI systems
• Potential uses of large language models
• Comparison to compilers and understanding complex systems
• Self-driving cars and AGI
• Public transportation as an alternative to self-driving cars
• Challenges in implementing high-quality public transit, especially in rural areas