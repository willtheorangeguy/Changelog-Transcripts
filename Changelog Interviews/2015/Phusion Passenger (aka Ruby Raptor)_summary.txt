• Introduction to Hong Lee from Fuse and Passenger fame
• Overview of the Ruby Raptor and Passenger app server
• History of Passenger and its goal to simplify Ruby app deployments
• Philosophy behind Passenger: ease of deployment and minimal maintenance
• Comparison to other Ruby app servers, such as Puma and Unicorn
• Discussion of the unique approach of Passenger in integrating with web servers
• Origins of ModRails/Rails integration in 2008
• Name change from ModRails to Passenger
• Development of Passenger to support multiple web frameworks
• Rack's role in allowing multiple frameworks to talk to the app server
• Passenger's evolution to support multiple programming languages
• Business model shift from consultancy to building a business around Passenger
• Scalability issues with the consultancy business model
• The company's education program was delayed by about 5 years
• The company struggled financially for a long time, making less money than expected
• They shifted their business model from consultancy to selling Passenger Enterprise, a paid version with extra features
• They charge a license fee per server per year/month and this model was more successful
• They tried selling support but it didn't work out because their product is too stable
• The founders made sacrifices to prioritize the open-source community and their own freedom and potential
• They started the company when they were young and saw it as a low-risk opportunity
• Discussion of Passenger Enterprise and its improvements
• Introduction of Raptor, a new Ruby app server
• Comparison of Raptor's performance to existing app servers
• Concerns about the perception of Passenger in the community
• Explanation of how Passenger Enterprise funds the development of the open source version
• Discussion of the challenges of changing people's perception of Passenger
• Unconventional marketing tactics used to promote Passenger
• Launch of Raptor as a new project, pretending it was a competitor
• Surprise and reaction of the community when it was revealed that Raptor was actually Passenger 5
• Feedback and bugs found in Passenger 5 beta
• Plans to release a Passenger 5 release candidate in a month
• Discussion on the community's preference for new and shiny things over facts and merits
• The need for a change in perception to keep up with the community's expectations
• Sponsor shoutout to TopTile
• Interview with Daniel Elzon, an elite engineer at TopTile
• Discussion of TopTile's benefits for freelancers and developers
• Update on Passenger 5, aka Raptor, a new version of the software
• Feedback from beta users on the performance and stability of Passenger 5
• Explanation of turbo caching, a feature in Passenger 5 that improves performance
• Comparison of turbo caching to other caching mechanisms, such as Varnish and Nginx
• Introducing a variation of HTTP cache to cache dynamic apps
• Limited usefulness of current HTTP cache
• Caching for anonymous traffic to increase performance
• Per-user cache, but also extending to cache based on user classes
• Innovation in HTTP level caching systems
• Hybrid I/O model in Passenger 5 for safety and security
• Protecting against slow clients with an evented server model
• Using OS level primitives to handle multiple clients
• Shielding application from slow clients and denial of service attacks
• Leveraging multiple CPU cores for improved performance
• Serving Fusion Passenger 5 directly vs using a proxy like Nginx
• Design and trade-offs of a custom HTTP engine in Fusion Passenger 5
• Comparison of Fusion Passenger 5's HTTP engine to Nginx
• Optimizations and features of Fusion Passenger 5's HTTP engine
• Recommendation to use Nginx as a proxy in certain scenarios
• Discussion of CPU branch prediction and indirect branches in Nginx
• Sponsorship discussion: DaysWork time tracking and invoicing software
• Brief discussion of optimization techniques used in Fusion Passenger 5
• Borrowing from Node.js and Nginx, developers have created a more efficient system
• The concept of "borrowing the best parts" from other projects is a winning pattern in open source development
• Traveling Ruby is a new project that aims to simplify the distribution of Ruby apps to users
• The goal is to provide a single executable that works everywhere, eliminating the need for users to install multiple dependencies
• Traveling Ruby allows developers to use pre-built binaries, reducing the complexity of package management and deployment
• The project is already being used by the Cloud Foundry project to simplify the installation of their tool, Bosch
• Containerization using Docker and build systems
• Challenges in building Linux binaries for multiple distributions
• Traveling Ruby's approach to building portable binaries
• Request for community help with Windows support
• Future tool, potentially a complete solution for deployment, similar to Heroku
• Vision for a tool that enables easy deployment to various infrastructures (e.g. AWS, on-premise, DigitalOcean)
• Discussion of the use and development of Passenger 5
• Trademark issues with the name "Raptor"
• Existence of a gem named "Raptor" unrelated to Passenger 5
• Release schedule for Passenger 5
• Discussion of Zed Shaw, author of Mongrel, and his experience and code
• Reference to a past episode of a show featuring Zed Shaw
• Hong Lee's praise for Passenger's creator, mentioning that he's sharp and good at bringing out the "inner troll" in the community.
• Discussion of programming heroes and the lack of specific names mentioned.
• Hong Lee's marketing take and the "bait-and-switch" idea on the rebranding of Passenger.
• Gratitude for Hong Lee's contribution to the open-source community and appreciation for his sacrifice.
• Sponsor mentions: Ninefold (Ruby host), TopTel, and a new time tracking tool called "Dave's work".
• Ability to view processes and logs
• Timeline for release of new admin panel
• Prioritization of Passenger 5.0 stability before new features
• Expected release date in mid-2015
• Plan for future updates and announcement on change log