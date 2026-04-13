• Introduction to Spotlight series on Node.js
• Interview with James Snell about H2 implementation for Node.js
• Discussion of current state and challenges of implementing H2 in Node.js
• Debate over whether H2 should be a module or part of Node's core
• Importance of keeping Node's core small and focused
• Defining what belongs in Node Core vs. separate modules
• Importance of keeping Node Core small and focused on web fundamentals
• URL parsing as an example of a functionality that could be moved to a separate module
• Discussion on H2 protocol and its differences from H1, including binary framing, stateful header compression, and implications for web application design and performance
• Security as a top priority for the next year
• H2 protocol will be designed to be highly spec-compliant and prioritizes security over performance
• H1 was not fully compliant with the specification, which led to several security issues
• H2 servers will require TLS connections by default due to browser implementation requirements
• Node's reputation as a TLS terminator is a limitation that needs improvement for better performance
• H2 enables new extensibility models and possibilities for new kinds of protocols
• New proposals for other layered protocols are emerging within the working group
• WebSockets' relationship with H1 is being considered as a precedent
• The framing model in H2 will allow for experimentation without the pain of introducing WebSockets like before
• Potential innovations could come out of it, but require collective experience and testing
• Criticisms of the H2P protocol include:
  • Inefficient header compression (staple header compression)
  • Repetitive headers leading to waste in transmission
  • HPAC's stateful compression model adds complexity
  • Maintaining state tables can be resource-intensive
• Additional complexity in H2 compared to H1
• Flow control and prioritization in H2
• Impact on proxy software vendors and protocol criticism
• Server affinity issue with H2
• Performance benefits of using H2 efficiently (e.g. better request handling)
• Memory usage trade-off for increased performance
• H2 protocol offers a significant savings of header bytes, potentially saving users money on bandwidth costs
• The adoption of H2 requires careful consideration due to trade-offs in security and API compatibility with H1
• Status messages are removed in H2, which may break existing applications that rely on them
• Designing an application specifically for H2 is necessary to take advantage of its capabilities
• H2 is more suitable for internal server-to-server communication rather than user-facing web servers
• The H2 project is currently being worked on by a single developer with plans to grow the team and accept open-source contributions
• H2 protocol implementation and integration into Node.js
• Discussion about deprecating the H1 protocol in favor of H2
• Decision to offer both H1 and H2 as options for developers
• Implementation challenges and future plans for HTTP development in Node.js
• Consideration for a module-based approach for H2 implementation
• Discussing the size and complexity of an ecosystem
• Need for input on code direction
• Best ways to provide feedback and get involved (repo, open issues, pull requests)
• Code stabilization and distinct areas needing help (tests, performance benchmarks)
• Linking repo in show notes
• Closing down Node Interactive