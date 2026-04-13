• Simon Eskildsen's journey at Shopify, from 100 to 100,000+ requests per second, and his experience with growth and infrastructure migration
• Shopify's storefront redesign, moving from a monolith to a more scalable architecture
• Simon's background and learning style, being a "learn-by-doing" person without an academic background in computer science
• Competitive programming, a concept where programmers solve complex problems within a set time limit, often using algorithms and coding skills
• Comparing competitive programming stress to working on Black Friday at Shopify
• The pressure and responsibility of working on Black Friday, with a focus on system monitoring and troubleshooting
• The impact of remote work on Black Friday preparations and team dynamics
• Engineering approaches and solutions for scaling systems at Shopify, including sharding, podding, and load shedding
• Addressing the limitations of current database infrastructure for multi-tenancy and prioritizing traffic between merchants
• Using the MySQL protocol to send arbitrary strings back with query results for load shedding and traffic prioritization
• The speaker proposes adding resource metrics to query results to enable more informed API throttling and load shedding.
• The addition of metrics has a minimal overhead of 1-2% in benchmarks.
• The speaker is working on a patch for MySQL to expose these metrics.
• The patch is still experimental and being rolled out internally, but aims to enable data analysis and load shedding.
• The speaker discusses their approach to learning and understanding systems, including "back of the napkin math" for quick estimates of performance and feasibility.
• This approach involves developing a deep understanding of system components and their performance characteristics from the bottom up.
• The speaker emphasizes the importance of developing expectations about system performance and feasibility before implementing solutions.
• The importance of using "napkin math" to estimate and understand system performance by breaking down complex systems into simple, manageable components
• The example of estimating MySQL's transaction rate by identifying the fsync operation as the bottleneck and estimating its impact on overall performance
• The discovery of a "first principle gap" between the estimated and actual performance of MySQL, leading to further investigation
• The revelation that MySQL's batching mechanism, "group commit", was the reason for the discrepancy in estimates
• The use of Elon Musk's example of estimating rocket costs to illustrate the importance of understanding system complexity and inefficiencies
• The discussion of the importance of regularly re-evaluating and refining one's understanding of complex systems to close the "first principle gap"
• Inefficiencies in system design can be identified through simple calculations and estimations, known as "napkin math"
• Time spent researching and investigating a problem can be reduced through the use of napkin math
• Redis performance issues can be solved by considering the number of connections and implementing a proxy
• First principles understanding of a system is key to performing napkin math and making informed decisions
• Contributing to and referencing existing resources, such as the mentioned repo, can aid in developing a first principles understanding
• "Yak shaving" and starting from a place of uncertainty can be mitigated by knowing where to start and how to break down complex problems.
• Reading compressed data can be faster than uncompressed data due to memory bandwidth limitations
• Napkin math can be a useful tool for feasibility studies and problem-solving, but requires an understanding of system principles
• Implementing a solution without proper understanding can lead to "programming through the wall"
• Exploration and learning are key to avoiding analysis paralysis and finding the best solution
• Napkin math can be used for financial estimates and data storage calculations
• It's essential to have a basic understanding of systems and principles to use napkin math effectively
• Techniques and tips for using napkin math effectively include creating a simple problem, thinking about the math solution, and diving deeper into complexity.
• Don't overcomplicate napkin math, focus on the biggest bottlenecks
• Use units when doing napkin math to avoid errors
• Use WolframAlpha to handle conversions and units
• Simplify calculations by dropping insignificant digits
• Use Fermi decomposition to break down complex problems into simpler ones
• Estimate numbers within an order of magnitude, rather than precise values
• Using Fermi decomposition to estimate the number of piano tuners in Chicago
• Understanding the limitations of napkin math and its purpose in estimating within an order of magnitude
• Identifying opportunities by comparing estimated supply and demand
• Applying napkin math to estimate costs and identify discrepancies, such as unexpected machine usage
• Using decision trees to determine the level of detail needed for further analysis
• Estimating revenue and expenses in a business opportunity using napkin math
• Building intuition through repeated use of napkin math in estimating and problem-solving
• Discussion of recognizing when an idea or solution won't work
• Anecdote about a firefighter's decision to evacuate a building and its connection to mastery and deliberate practice
• Application of napkin math in the speaker's career, including specific examples and its frequency
• Promotion of the speaker's newsletter, where he shares examples of napkin math in real-world problems
• Humorous discussion about the speaker not using actual napkins, but rather an iPad, and the potential for merchandising "Simon-branded" napkins