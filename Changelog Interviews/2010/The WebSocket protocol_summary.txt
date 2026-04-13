• Introduction to the ChangeLog podcast and its coverage of open-source topics
• Overview of the podcast's guests and their expertise in WebSockets
• Explanation of what WebSockets are and how they work
• Discussion of the benefits of WebSockets, including bi-directional communication and real-time capabilities
• Explanation of how WebSockets are used in various projects, including Pusher App and Socket.io
• Overview of the guests' projects and how they utilize WebSockets
• Discussion of the current state of browser support for WebSockets
• Support for additional browsers and fallback techniques in Socket.io and Push Your App
• Socket.io's use of feature detection for deciding what transport to use, including fallbacks to older browsers
• Push Your App's use of WebSocket.js and flash socket to emulate WebSocket connections
• Priority list for transports in Socket.io, with WebSocket and Flash as top choices
• Fallback to long polling, HTML file, or other transports when WebSocket and Flash fail
• Comparison of WebSocket and long polling, including buffering of messages between disconnections
• Scaling issues for Socket.io, including ensuring sticky requests and using message queues or Redis servers
• Using HTTP load balancers to direct requests to specific server instances
• HA Proxy load balancing system used in PusherApp
• Load balancing in Node.js, including frameworks like Connect and Multinode
• Using WebSockets in iPhone applications, current limitations and potential future support
• Browser-side implementation and communication of the WebSockets protocol
• Applications built with Socket.io and Pusher App, including Dnode, chat applications, and games
• TrueStory application and its collaborative features, leading to the development of Pusher App's event-binding API
• Examples of real-time applications using Pusher App, including Twitter feeds and Groupon purchases displayed on Google Maps.
• WebPad: a drawing application that shows drawings in real-time on the web
• Pushar channels: can be single or multiple per application, depending on the use case
• Channels: an abstraction on top of WebSockets, allowing efficient communication with hundreds of users
• Triggering events: can be done using a JavaScript API, allowing for custom functionality
• EventSource: a new HTML5 protocol for one-way communication from server to browser
• Socket.io: a library that provides a single API for WebSockets, supporting multiple browsers and use cases
• Current state of WebSockets
• Full duplex communication
• Guillermo's work with WebSockets
• Promise of unified API with browser and proxy support
• Resources for learning about WebSockets
• Open source projects
• Node.js projects, including Hummingbird demo and socket.io
• Redis and its use in real-time applications
• EM WebSocket for Ruby event machine clients
• Node.js YUI-3 bindings and Telehash
• Web development tools and technologies, including WebSockets
• Ease of building real-time, full duplex pipes
• Complexity of the application landscape for web developers
• Choice and responsibility that comes with new technologies
• Impact of new technologies on developer difficulty and productivity