• Real-time web feeds and technologies
• PubSubHubbub protocol for real-time web updates
• XMPP (Extensible Messaging and Presence Protocol) for messaging and presence
• WebSockets for real-time communication between web servers and clients
• Superfeeder and its use of PubSubHubbub and other protocols
• Benefits of real-time web technologies, including reduced bandwidth usage and improved efficiency
• Evolution of the web from read-only to real-time subscription-based models
• Comparison of different protocols and technologies for real-time web messaging
• PubSubHubbub protocol allows feeds to be updated in real-time
• Users can subscribe to feeds through a third-party hub
• Discovery of hubs is done through links in the RSS feed itself
• Hubs collect updates from publishers and fan out to subscribers
• Publishers can designate their own hub, such as GitHub for its public timeline
• Large hubs exist, including Google Hub, WordPress.com hub, and Superfeeder
• Technologies like PubSubHubbub enable new era in web design, with server-to-server communication and real-time updates.
• Gowalla's Superfeeder and PubSubHubbub
• Comparison with Twitter's streaming API
• Differences between PubSubHubbub and XMPP
• Reliability and handling missed updates
• Scaling and storage of large amounts of data
• Real-time update feature vs. pulling feed independently
• Limitations of RSS feeds and potential loss of content when offline
• Asynchronous processing techniques for handling offline data
• Superfeeder's architecture and use of XMPP and Ruby
• Normalization of RSS formats to Atom
• Use of Event Machine and its limitations
• Comparison of Node, Twisted, and Event Machine
• Issues with Event Machine's DNS resolution and asynchronous implementation
• Use of Redis and other NoSQL databases
• Redis's cluster node feature and potential alternatives
• Discussion about Redis and its differences from other NoSQL stores
• Redis's low-level approach and lack of native JavaScript support
• Web development landscape changes with the need for NoSQL solutions and queuing systems
• Use of RabbitMQ and limited use of queue systems
• Development of Superfeeder and its initial internal component status
• Superfeeder's monetization strategy and implementation of the PubSubHubbub protocol
• Handling non-PubSubHubbub enabled feeds with third-party polling or push services
• Superfeater's features and functionality
• Avoiding polling techniques used in Superfeater
• Data anomalization and its implementation
• Pricing and cost structure for Superfeater
• Popular feeds and their identification
• Superfeater's scalability and data handling
• Open source projects mentioned (Redis, Node.js, Chef)
• Use of Chef for server management and deployment
• Issues with Chef receipts and updating them
• Goal to create a generic way to describe servers and IPs for cloud deployment
• Automating benchmarks across different cloud services (Rackspace, Slicehost, Linode, EC2)
• Optimizing performance per dollar spent across cloud providers