• Debate over the pronunciation of WebAssembly (WASM) as "wozm" or "waezm"
• Introduction to WebAssembly and its goals: efficient low-level bytecode for the web
• Explanation of streaming compilation and how it reduces parsing time on mobile devices
• Breakdown of WebAssembly's compilation process, including segmentation and separate compilation of sections
• Discussion of WebAssembly as a compilation target, not a programming language
• Clarification that WebAssembly is neither specific to the web nor an assembly language, but rather a bytecode
• Redesigning Java bytecode to create a global virtual machine developed in the open
• WebAssembly as a generic, low-level instruction set for creating universal applications
• Potential use cases beyond web development, such as operating systems and native applications
• Browser vendors working on optimizing WebAssembly compilation performance
• Current limitations of WebAssembly accessing DOM and other APIs through JavaScript bridges
• Future plans to improve WebAssembly's ability to access external resources directly
• Garbage collection limitations in WebAssembly compared to languages like C and Rust
• Current workarounds for garbage collection in languages compiling to WebAssembly
• Need for first-class support for underlying garbage collector in WebAssembly
• Performance benefits of using WebAssembly, particularly for number-crunching tasks
• Examples of successful porting of tools to WebAssembly, such as the Sourcemaps project
• Limitations of current WebAssembly optimizations and potential for future improvements
• WebAssembly may be slower than JavaScript in some cases due to limitations in virtual machine knowledge and optimizations.
• React's new architecture uses compilation and computation techniques similar to those used by WebAssembly.
• Glimmer Virtual Machine for Ember, which compiles to WebAssembly, aims to improve performance but its effectiveness is still uncertain.
• Current challenges include garbage collection and the bridge between JavaScript and WebAssembly, as well as limitations in platform-specific APIs.
• Emscripten provides a standard library and implementation for C and C++ projects compiled to WebAssembly, making it easier to port existing tools.
• Multi-threading support is currently limited due to shared array buffer restrictions, but browser vendors are researching ways to unlock this feature.
• Discussion about the benefits and limitations of using WebAssembly for multi-threading
• Potential issues with exposing real threads (e.g. pThreads) in WebAssembly
• Proposal to create a global interpreter lock for JavaScript, similar to Ruby's GIL
• Browser vendors' reluctance to implement multi-threading due to complexity and resource constraints
• Importance of distribution and learnability in language development, enabled by compilation and runtime capabilities in the browser
• Current toolchain using LLVM to output WebAssembly, with experimental projects and potential for bootstrapping
• Discussion about compiling JavaScript engines (e.g. JavaScript Core, ChakraCore) to WebAssembly and running them in web workers or across different browsers
• Current limitations of WebAssembly for just-in-time compilation
• Toolchains and languages that can compile to WebAssembly (over 20)
• Production-readiness of different languages (Rust and C++ are the most production-ready)
• Garbage collection in WebAssembly and its impact on performance
• Memory management and trade-offs between file size and performance
• Nuances of performance comparisons between WebAssembly and JavaScript
• Future developments, including dynamic systems libraries and host bindings
• The caching story for WebAssembly is a challenge, particularly with standard library stuff like malloc and free.
• There are discussions about providing a unified way to handle these issues, potentially through CDNs or caching compilation.
• Caching can help reduce excess file size and improve code reuse.
• WebAssembly has already been adopted in various projects, such as SourceMap, often transparently.
• It's recommended to focus on performance-critical areas like algorithms, graphics, and SIMD (single instruction, multiple data) for initial adoption.
• The goal is to make WebAssembly an implementation detail, much like machine code, allowing developers to focus on their language of choice without worrying about compilation details.