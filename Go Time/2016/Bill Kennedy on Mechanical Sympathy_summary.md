• Introduction of episode 6 guests, including Bill Kennedy from Ardan Labs
• Discussion of interesting projects, including:
	+ Acksin's StatsD to Google Analytics hack
	+ Manul, a vendoring project using Git submodules
• Overview of potential drawbacks and issues with Git submodules
• Discussion of Mechanical Sympathy, its origin and application in programming
• Bill Kennedy explains his perspective on data-oriented design and Mechanical Sympathy in the context of Go programming language
• Importance of understanding the data and its relationship to the hardware
• How CPU caches work and the impact of cache misses on performance
• The concept of "Mechanical Sympathy" and how to be sympathetic with the hardware by working with data in contiguous blocks
• Predictable access patterns and their importance for efficient memory usage
• Temporal and spatial locality, including working with data that is located next to each other or at the same time
• Examples of inefficient memory usage, such as linked lists and multidimensional arrays iterated over in a non-contiguous way
• Performance differences between CPU cache and RAM
• Transaction lookaside buffer and its impact on memory performance
• Introduction to Go's slice data structure and its advantages
• Sympathetic code: writing code that is harmonious with the hardware and operating system
• Data-oriented design and its benefits, including improved readability and maintainability
• Separating data from behavior in programming design
• The importance of leveraging slices and functions for efficient coding
• False sharing: duplicated data in cache lines causes performance issues when one thread writes to it
• Data-oriented design: keeping related data together can help avoid false sharing and improve performance
• Slices and contiguous memory: using slices instead of arrays or linked lists can help improve performance by reducing cache misses
• Struct layout: packing fields tightly without unnecessary padding bytes can improve performance for large datasets
• Hardware caching: understanding how the hardware caches work is crucial to writing efficient code
• Discussion of data-oriented design and performance optimization in Go
• Importance of understanding cache behavior and struct layout
• Strategies for grouping related data together and minimizing false sharing
• Bill Kennedy's approach to solving problems as a data manipulation problem
• Resources available on the Go Training GitHub repo for learning more about CPU caches, Linux operating system, and scheduler behavior
• A lighthearted discussion about people cosplaying as Bill Kennedy at GopherCon
• Announcements of workshops and events at GopherCon, including a NATS workshop and a remote meet up platform started by Carlisia and Bill
• Plans to grow the remote meet up platform with more speakers and locations.
• Plans to publish an event announcement and tweet about a meetup with limited attendance
• Compose.io sponsoring the meetup and providing a plus account for 100 attendees
• Bill Kennedy's efforts to promote the platform and encourage others to start their own MeetUps
• Open source projects mentioned: CORAL, Go Validator, go-plus, autocomplete-go, go-metalinter, tester-go, LRUcache, Vagrant, Vault, Consul
• Discussion about a barbecue Gopher mascot and available merchandise