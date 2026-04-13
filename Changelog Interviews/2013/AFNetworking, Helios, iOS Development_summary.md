• The hosts Adam Stakovak and Andrew Thorpe discuss the guest Matt Thompson, the mobile lead of Heroku, and his open source projects.
• Matt Thompson talks about how he got started with open source while working at Gowalla, a now-defunct app.
• He introduces AF Networking, a project he created while at Gowalla, and explains its purpose and how it took on a life of its own.
• The hosts mention that several for-profit companies have released pieces of their companies in open source, and ask Matt about the "AF" in AF Networking.
• Matt explains that AF stands for Alamo Fire, the old name of Gowalla, and how the project started as a mobile games company.
• The hosts discuss how Matt went from working at Gowalla to Heroku and how he and Kenneth work together, despite not directly collaborating.
• Matt mentions that AF Networking has no direct connection to Heroku and is maintained separately in his free time.
• He discusses how his role at Heroku is to increase the number of mobile developers on the platform, and how AF Networking can help achieve that goal.
• AF Networking and its limitations for making HTTP requests
• Helios, an open-source backend-as-a-service for mobile, built on top of Rack and focusing on iOS
• The complexities of developing mobile applications and the importance of focusing on the client
• The relationship between AF Networking and Helios, with Helios providing a layer of abstraction for networking
• The use of AF Incremental Store, a project under the AF Networking umbrella, for combining AF Networking with Core Data
• The benefits of using Helios for quickly building mobile applications with data services
• The ability to link Core Data models to Helios for automatically generating REST web services.
• Helios is a framework for building mobile applications, providing plumbing and other services such as push notification registration, logging, and analytics.
• It's designed to be easy to use, even for developers without extensive web service experience.
• Helios is still in beta and has been actively developed since its launch in April.
• The framework is expected to have a "heroku feel" on its website and will continue to evolve with features like AF Networking 2.0.
• Helios is currently being used by a small group of early adopters and developers are encouraged to experiment with it.
• The "get out of beta" plan involves improving documentation and adding more features.
• The framework is expected to anticipate future usage and development trends in mobile app creation.
• Frustration with setting up PostgreSQL as a web developer
• Importance of user experience and accessibility for beginners
• Challenges of using the command line and Homebrew for database setup
• Need for user-friendly tools like PostgreSQL.app
• Collaboration with Heroku and the creation of PostgreSQL.app
• Role of PostgreSQL.app in making database setup more accessible to newcomers
• Complexity of developing applications and the need for helper applications
• Induction app: a polyglot database client that was ambitious but difficult to execute
• AF Networking: a library for networking that combines nsurlconnection with other tools
• Philosophy behind AF Networking: using nsurlconnection as the highest level of abstraction
• Design and functionality of AF Networking, including the use of nsoperation and block-based callbacks
• Discussion with an Apple engineer about the possibility of including AF Networking in the standard library
• Apple's history of being conservative in introducing new technologies to their public API
• The introduction of NSURLConnection and its limitations
• The benefits of the new NSUrlSession framework in iOS 7
• How AFNetworking adapts to NSUrlSession and improves upon it
• The new serializer feature in AFNetworking 2.0 that abstracts away the concept of serialization
• The complete rewrite of AFNetworking 2.0, which keeps half of the old code and builds upon the new APIs
• The upcoming release of AFNetworking 2.0, with the first release candidate going out on Thursday
• Discussing solutions for managing GitHub releases
• CocoaPods and its relationship with GitHub
• AFNetworking vs RestKit and their differences
• Premium support model for open-source projects
• Tension between gift culture and market-based compensation in open-source development
• Discussion of monetization strategies for a project
• Introduction of a "support" model where users can financially support the project
• Mention of Chad's article on "open products" and the idea of "bring your own carrot"
• Introduction of AF Networking 2.0 and its focus on real-time communication and server-sent events
• Explanation of server-sent events and its implementation in AF Networking 2.0
• Discussion of the "rocket" manifesto and its ideas on building modern applications
• Mention of JSON patch and its use in AF Networking 2.0
• Upcoming release of AF Networking 2.0
• Integration of Event Source and JSON Patch with AF Incremental Store
• Server-Sent Events solving a key problem with AF Incremental Store
• Future of official and third-party extensions with 2.0 release
• Importance of open-sourcing code and contributing to the community
• Personal interests and hobbies, including hang gliding and learning to fly
• Shout-outs to Why the Lucky Stiff and Sean Inman for their contributions to the community
• Discussion of a person's attendance at a conference and a class they taught
• Reference to the person's status as "410 gone" and being "not real gone"
• Mention of the person's work in open source and mobile development
• Discussion of the role of a job at Heroku and marketing vs. growth
• Appreciation for The Changelog and their efforts in humanizing open source.