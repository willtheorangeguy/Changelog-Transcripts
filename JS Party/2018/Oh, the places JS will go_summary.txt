• Introduction to new panelists: Suz Hinton, Kevin Ball, and Feross Aboukhadijeh
• Discussion on JavaScript's ubiquity and versatility
• Highlighting fringe/edge/weird uses of JavaScript with a focus on IoT and WebUSB
• Exploring WebUSB and its potential for device interaction
• Discussion on the capabilities and limitations of WebUSB
• Native device support in browsers
• WebUSB spec for secure communication between devices and web pages
• Device discovery and notification when plugged into computer
• Security concerns related to sandboxing and permission-based access
• Comparison to existing methods of installing hardware drivers and autorun features on Windows
• Feross Aboukhadijeh shares his experience with creating a prank script that shut down computers immediately when turned on.
• Discussion of WebUSB and its capabilities for web pages to interact with devices, including reverse-engineering protocols and creating alternative interfaces.
• Status of the WebUSB spec, currently in draft status, available to 56% of users globally, but not widely adopted by IoT manufacturers yet.
• Feross Aboukhadijeh's work on WebTorrent, a torrent app that runs in the browser, using WebRTC for peer-to-peer networking and data transfer.
• Introduction of WebRTC's data channel, allowing direct connections between clients without a server intermediary.
• Discussion on TCP and UDP protocols
• Use of WebRTC for peer-to-peer connections and cutting out middlemen like servers
• Elimination of permission prompts due to lack of direct access to user's device capabilities
• Introduction to Comlink library, an RPC mechanism for browser-to-browser communication
• Explanation of STUN and TURN services in WebRTC for NAT traversal and connection establishment
• Limitations of one-way exchange of information for peer-to-peer connections
• Challenges with decentralized networking using WebRTC
• Centralization trade-offs for usability and accessibility
• Comparison to BitTorrent and DHT data structure
• Potential use of trustless servers as a decentralized alternative
• Limitations and complexities of building decentralized social networks
• Discussion on blockchain-based solutions and decentralized file sharing
• Brave's native support for WebTorrent in the browser
• Discussion of Domain-Specific Languages (DSLs) and their potential in JavaScript using Babel
• Babel as a compiler for creating new language features, rather than just transpiling future JavaScript versions
• Idea of creating a DSL for WebUSB or other specific use cases to make it easier for developers to work with
• Example of Parseltongue, a Harry Potter-themed programming language developed using ASTs
• Ability to extend JavaScript using Babel and create custom languages that compile down to JavaScript
• Potential examples of DSLs in different domains, such as JSX for HTML or a DSL for WebUSB
• Designing Domain Specific Languages (DSLs) for ergonomics and mental model matching in code
• Using DSLs with protocols like torrents and WebUSB
• Managing DSL changes through code organization and build steps
• Potential applications of DSLs for games and other domains
• Discussion on using tools to create DSLs, such as Babel
• Humorous exchange about Jerod Santo writing a rap about the JS Party