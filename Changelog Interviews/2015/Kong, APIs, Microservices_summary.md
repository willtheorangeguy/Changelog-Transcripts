• Ahmad Nasri discusses his background and history, including growing up in Syria and later moving to Canada
• He talks about his childhood in Syria, where he had access to the Internet through a long-distance dial-up connection to Lebanon
• Nasri discusses the diversity of his upbringing, attending a Shiite school and having friends from different Christian and Sunni backgrounds
• He mentions his interest in technology and the Internet from an early age, and how he would access the Internet through a service provider called Siberia based in Lebanon
• Life under dictatorship in Syria, with restrictions on internet access and surveillance
• Bribes and corruption to get around restrictions
• Getting internet access through the government and starting to use it for entrepreneurial purposes
• Finding and selling cheat codes for computer games
• Visiting neighboring countries to import restricted items, such as PlayStation magazines and Pepsi
• Learning English and discovering the world through online resources
• Using cheat codes and smuggled electronics due to trade restrictions and boycotts
• Selling cheat codes to younger kids as a business venture
• Using a low conversion rate to price cheat codes, making them affordable for kids
• Targeting younger kids as customers due to their gullibility
• The interviewee's entrance into the software industry was through writing cheats for Neopets and later creating bots.
• The evolution of the cheating industry involved hardware hacking and learning about the internal workings of the PlayStation device.
• The interviewee transitioned from video game-related activities to mobile devices, specifically smartphones, and began creating software for the Symbian S60 operating system.
• The interviewee's family moved from Syria to Canada, with his parents having applied for immigration 19 years prior to their arrival.
• The family's experience was "fresh off the boat," with no prior connections to Canada and a complete start over in a new country.
• The speaker's father had a cosmopolitan upbringing and traveled extensively, providing the speaker with a foundation for understanding different cultures.
• The speaker experienced culture shock when arriving in Toronto, including the city's tall skyscrapers and cold weather.
• The speaker's career began with computer science studies in Syria, but they were not accredited in Canada, leading them to pursue self-directed learning and eventually becoming a developer.
• The speaker's career progressed through various roles and technologies, ultimately leading to their current position as head of engineering at MashApe.
• The discussion will shift to Kong after a commercial break.
• Kong is an API management and abstraction layer for APIs and microservices
• It allows secure and easy configuration of APIs and microservices at scale
• Kong is unopinionated about API architecture and format, supporting various standards and approaches
• It focuses on the HTTP layer, providing control and management of APIs in a way that is agnostic to backend or actual API operations
• Kong was originally part of the MassShape API marketplace, which had to support multiple API standards and approaches
• The term "microservices" is often used interchangeably with SOA, but microservices focuses on the HTTP layer and is more about deployment and management of components
• The industry's focus on standards and architecture can lead to chaos and confusion, but ultimately, users care about the product, not the underlying technology
• APIs are considered products that require dedicated product teams and marketing efforts.
• APIs share common attributes and needs, such as authentication, logging, and rate limiting, that can be abstracted away and provided by a layer in front of the APIs.
• Kong was built to address the need for a global distribution of proxy services across multiple regions without adding delay or losing context of the data.
• Companies with multiple APIs and applications, such as Netflix, face maintenance and scaling issues with authentication, logging, and rate limiting.
• Abstracting away these common tasks and moving them to the proxy layer, such as with Nginx, can simplify API management and reduce maintenance efforts.
• Kong is built on top of Nginx and provides a RESTful API for configuring Nginx servers and proxy mechanisms.
• Kong allows for dynamic configuration and customization of Nginx, including authentication, using a scripting language like Lua.
• Kong provides a single point of control for managing multiple APIs and services, eliminating the need for manual configuration and synchronization across clusters.
• Kong's architecture allows for multiple endpoints and services to be represented as a single entity, or as separate entities with customized logic and authentication.
• Kong is designed to be non-opinionated, allowing users to choose how to configure and use the platform.
• Kong can handle high traffic and scale to meet the needs of large enterprises, with thousands of public and private APIs and billions of calls per day.
• Kong's architecture is built on top of Nginx's efficiency and lightweight design, with minimal added resource usage and network latency.
• Kong's plugin architecture allows for easy addition and removal of logic pieces on top of API routes.
• Plugins can be enabled or disabled per API or per consumer
• Rate limiting can be customized per consumer for specific use cases
• Transformation plugins can be used to change requests before they hit the upstream server, helping to bridge the gap between API versions
• Authorization is a complex topic that can be handled in different ways, depending on the application, and can be implemented at the Kong layer or application-specific
• Consumer entities in Kong can have multiple credentials across multiple authentication methods
• A single consumer can have different authentication methods for different platforms or products, allowing for more generic and customizable access control
• There are potential drawbacks to the consumer idea, including a learning curve and the need to undo existing bad practices in API tooling.
• Brainwashing by competitors and the limitations of proprietary API management tools
• Kong's advantages as an open-source, free, and fully-supported alternative
• Comparison of proprietary tools to Kong in terms of resource usage and adoption
• The potential for developers to think in a single, limited way when using proprietary tools
• Kong's decision to make itself free and open-source to promote access and freedom
• Discussion of Kong's technology choices, including Nginx, Lua, and Cassandra
• The benefits of using Lua as a scripting language and its embeddability in applications
• Nginx and OpenResty
• Lua vs JavaScript in Nginx
• Kong plugin layer and JavaScript adoption
• Cassandra as a dependency for Kong
• Scalability and performance considerations
• Regional deployment and latency issues
• The speaker discusses the challenges of managing a distributed database for a mobile application with users worldwide.
• The use of Cassandra as a database solution to address concurrency and clustering issues.
• Comparison of Cassandra with other databases like Postgres and MySQL in terms of complexity and cost.
• The speaker's experience with decentralized systems and databases, and the potential intimidation factor for newcomers.
• The addition of Postgres support to the Kong platform as a pragmatic choice for users who don't require the full capabilities of Cassandra.
• The plugin architecture of the Kong platform, including the creation and use of custom plugins.
• Event-driven lifecycle in Kong
• Authentication methods triggered during request processing
• Custom plugin logic and event-based functionality
• Open-source benefits and community engagement
• Third-party plugins and integrations, including MaxCDN, RunScope, and Datadog
• Nginx plugin and premium services
• GUI interface for Kong and community-developed frontends
• Encouragement of innovation and community collaboration
• The company's approach to open sourcing its API management tool, Kong, and its motivations for doing so
• The difference between personal and business projects and the importance of justifying open source projects' existence
• MashApe's company culture and history of open sourcing products, including its API marketplace and analytics product
• The company's philosophy on monetizing open source products, focusing on services and value add rather than charging for the software itself
• The enterprise edition of Kong, which is the same as the open source version with no additional features or costs, but with additional support and services available
• Discussion about whether a customer needs or wants to invest in Lua or customization, and how the company provides professional services for integration and customization.
• Getting started with Kong, including how to access the website, GitHub repository, and documentation.
• Distribution packages for various Linux distros, including Debian, CentOS, and Red Hat.
• CloudFormation template and AMI for AWS users.
• Dockerized versions of Kong and Cassandra.
• Support for DigitalOcean, Heroku, and Microsoft Azure, with plans to automate the process for these providers.
• Status of Kong, including production readiness and future development plans.
• Kong is an open-source product with a dedicated team and full-time development.
• The next release will include cluster awareness for Kong nodes.
• PostQuest will be introduced as a database choice for developers.
• The community drives the roadmap, with feedback and guidance from GitHub issues and Gitter chat.
• The company prioritizes issues based on community feedback and demand.
• A GitHub plugin called Zenhub provides a Trello-like view of issues with a plus one feature.
• The company encourages community engagement and feedback to improve the product.
• The speaker's programming hero is Grace Hopper, who coined the term "debugging" and is credited with inventing the concept of debugging in programming.
• The speaker loves Hopper's quote "You manage things, you lead people" and has come to understand the difference between management and leadership.
• The speaker believes that management is about controlling and directing, while leadership is about inspiring and empowering.
• The speaker has had experience in both management and leadership roles and prefers leadership, which they find more appealing and challenging.
• The speaker criticizes the term "human resources" and the way it dehumanizes people, preferring to refer to team members as "people".
• The speaker believes that the lack of understanding of what motivates human beings, particularly technologists and developers, is a key issue in the software development industry.
• The joy of coding and development is a primary motivator for developers and programmers.
• Creating, innovating, and changing the world through technology is what drives them.
• Financial incentives are not the primary motivator for developers.
• Leaders and managers must understand and tap into the intrinsic motivations of their teams.
• A career in technology is a good fit for those who enjoy problem-solving and creating.
• Personal fulfillment and happiness are key benefits of a career in tech.
• Alternative careers or hobbies may be considered only as a last resort or due to external circumstances.