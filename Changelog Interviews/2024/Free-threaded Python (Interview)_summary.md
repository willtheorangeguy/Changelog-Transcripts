• Introduction to Core.py podcast and its hosts
• Discussion of the podcast's format, usually just the two hosts but occasionally featuring a guest
• Idea behind starting the podcast: to demystify the Python core development process and encourage people to contribute
• Features of the podcast, including highlighting contributions from regular people
• Personal anecdotes from the hosts, including Pablo's fast speech and Łukasz's experience keeping up
• Discussion of closed captioning at PyCon and its benefits for attendees
• Upcoming topic: Python 3.13, specifically its biggest feature
• The Global Interpreter Lock (GIL) is a lock that prevents multiple threads from executing Python code at the same time
• The GIL is necessary because Python's reference counting system requires a lock to prevent multiple threads from mutating objects simultaneously
• The GIL limits concurrency, but not parallelism, meaning multiple threads can switch between executing Python code quickly, but only one thread can execute Python code at a time
• There are special cases where the GIL can be dropped, such as when a thread is performing a long-running computation or waiting on a blocking network connection
• The GIL is more than just a lock, it's also a condition variable, which can lead to unpredictable behavior and make it difficult to reason about thread scheduling
• The GIL is a major contributor to Python's reputation as being slow for certain workloads, but it also has the benefit of making other operations, such as dictionary access, faster and more predictable
• The GIL's effect on scalability is a major concern, but it's not the only factor contributing to Python's speed limitations.
• Removal of the global interpreter lock (GIL) in Python
• Potential performance benefits of GIL removal, but also potential costs and complexities
• Loss of single-threaded performance, need for fine-grained locking, and potential for deadlocks and other concurrency issues
• Availability of a build of Python (3.13t) that does not have the GIL, but requires manual compilation
• Consequences of GIL removal, including loss of optimizations that rely on the GIL
• Strategy for implementing the GIL removal, including gradual rollout and experimental builds
• Need for community feedback and testing to determine whether the benefits of GIL removal outweigh the costs.
• The introduction of free-threading in Python is a complex change that may impact performance and stability
• The community is encouraged to try out the new version and provide feedback on its scalability and usability
• The main challenge is ensuring thread safety, particularly with C extensions and other code that relies on shared resources
• Early indicators suggest that the community is enthusiastic about the new feature and is actively working on adapting their code
• Despite initial concerns, the number of bugs and crashes has been lower than expected, and developers are making progress in identifying and fixing issues
• The team is recommending that developers try out the new version, but with caution, and only if they have a clear understanding of the potential risks and rewards.
• The current state of free-threaded Python is experimental and not yet production-ready due to stability concerns
• Library maintainers are encouraged to test the free-threaded version to identify potential issues
• The free-threaded version is expected to become a supported feature in future Python versions (3.14 and 3.15)
• The JIT feature in Python 3.13 is an experimental addition, not yet a mature JIT like V8 or Java hotspot
• The JIT feature is intended to provide a foundation for future optimizations, but is currently 0% faster than the non-JIT version
• The Python core team is working on implementing a JIT that can dynamically compile code to machine code.
• JIT compiler for Python being developed
• Need to balance JIT compiler with memory usage
• Excitement around new JIT approach leveraging LLVM
• JIT approach simplifies implementation and leverages existing optimizations
• Discussion on Python release cadence and its impact on users and developers
• One-year release cadence has brought predictability but also created impression of rapid change
• Concerns about releasing features too quickly and impacting planning for big projects
• Python 3.9 release was rushed due to a new parser being introduced
• Frequent releases (e.g., every 6 weeks) can provide predictability and allow for more flexibility in development
• However, frequent releases also increase the complexity of testing and maintaining compatibility
• Smaller changes in each release can make it easier for libraries to adapt and for users to take advantage of new features
• NumPy's compatibility with new Python versions has improved significantly, with wheels available on day one for major releases
• The conversation starts with a joke about a cheese shop from Monty Python, and how it relates to the name "Python"
• The discussion moves to the topic of naming conventions for Python packages, and how they are often recursive acronyms
• The conversation also touches on the topic of release cadence, and finding a balance between frequency and reliability
• The group discusses the challenges of making Python available on iOS, including limitations in the build system and APIs available on the platform
• They mention the PyScript project, which allows running Python in the browser, and the efforts to make Python available on iOS
• The discussion concludes with a description of the current state of iOS support, and the challenges of packaging Python on the App Store.
• Embedding Python in iOS apps is now supported, making it easier to create mobile apps with Python.
• The infrastructure for embedding Python has been simplified, reducing the burden on developers.
• The next step for the BeeWare project is to build a workflow for creating Python applications from scratch.
• The goal is to make it easy for developers to create Python applications for mobile devices.
• The Python community hopes to see a significant improvement in the usability of Python's free threading feature.
• Removing the GIL (Global Interpreter Lock) is seen as a key step towards making Python more efficient and competitive with other languages.
• The community hopes to see a significant impact from the removal of the GIL and the introduction of free threading.
• Improved error messages and user experience are also a priority for the Python community.
• Upcoming changes to the Python interpreter, including new performance-optimized features
• Improved error messages
• Potential for significant performance improvements, including GIL removal
• Plans for the podcast core.py, focusing on Python internals and development
• Future collaboration and discussion with the podcast hosts