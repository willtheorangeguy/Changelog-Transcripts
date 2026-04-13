• Introductions and welcome to the show
• Flynn, an open sourced platform as a service, powered by Docker
• Tent protocol, a decentralized communication and data storage protocol
• Background and experience of guests Jeff Lindsey and Jonathan Rudenberg
• Discussion of open source projects and platforms, including Docker and Tent
• Use case driven development for protocol development
• Importance of real-time updates and push notifications in web development
• Evented web and web hooks as core concepts
• Popularization of web hooks by Jeff and its adoption by major services
• Development of adapters and plugins for web hooks
• Creation of Flynn and its relation to past projects and interests
• Local tunnel as a developer tool for ease of use and simplicity
• The speaker discusses their project Local Tunnel, which allows users to expose a local port to the internet using a simple command.
• The project was initially written in Ruby, but was later rewritten in Python to simplify the protocol and improve reliability.
• Local Tunnel's architecture and model are similar to those of Ngrok, which was written in Go by a friend of the speaker while they were working together at Twilio.
• The speaker has decided to merge Local Tunnel with Ngrok, and the new version will be written in Go.
• The speaker also discusses their project Request Bin, which allows users to inspect HTTP requests and debug webhooks.
• Request Bin has been cloned and is being taken to the next level by Runscope.
• The speaker notes that they often write the first version of software, and then someone else takes it and runs with it as a full-time project.
• The challenges of running open-source services that require ongoing maintenance and operation costs
• The idea for Flynn was born from the experience of running services like Heroku and App Engine, which simplified operations and cost models
• The importance of having a platform as a service layer, as exemplified by OpenStack
• Collaboration with Solomon on Docker, which led to the development of Flynn
• The decision to raise $75,000 to build Flynn, with a plan to spend 6 months working on it
• The response to the fundraising effort, with $108,000 raised from companies like Shopify, Lab Division, and others
• The goal of sustainability, with a plan to be ready in 6 months
• The project Flynn aims to provide a set of building blocks for companies to manage their internal services, similar to Heroku.
• The goal is to have a functional internal service within 6 months, with a focus on running small internal apps and services.
• Flynn is designed to be open-source, with the driving reason being to save others time and resources, rather than having companies build their own proprietary solutions.
• Flynn has early relationships with Docker and Solomon, with a focus on making Docker suitable for Flynn's needs.
• The system is designed to be modular and extensible, with independently useful components that can be reused across different applications and projects.
• Flynn allows users to recombine and replace its components, mirroring the component philosophy of Heroku
• The platform wants to separate modules and make them interchangeable, with a high-level architecture in mind
• Flynn's approach is to break down complex problems into smaller, simpler components through an iterative discovery process
• The platform aims to provide an out-of-the-box experience that is still hackable and customizable
• Flynn's philosophy is focused on building tools for building one's own platform or distributed systems, rather than creating a monolithic platform service
• The platform is based on modular components, with a focus on individual components and how they make up a platform service
• Flynn wants to make technology developed for platform services more accessible and decoupled, allowing users to apply it to different areas, such as container technology
• Discussion of when the community can expect to see a repo pop up and commits happen for the Flint project
• Explanation of the high-level planning and getting bearings phase, followed by diving into components and the Flint spec
• Funding model for Flint, targeting corporate sponsorships and avoiding the Kickstarter-esque model
• Review of the funding process and how it was more successful than expected, with a focus on companies rather than individuals
• Discussion of sustaining the project past the initial funding goal, including the possibility of raising more sponsorship and targeting internal platform services
• Explanation of the unique approach and target customers for Flint, focusing on operations teams at medium to small startups
• Quote from Tobias at Shopify on the future of operations and its alignment with Flint's approach
• Abstraction layers between EC2 and Heroku
• Flynn project: goals and philosophies
• Relationship between Flynn and Doku
• Doku as a single-host platform service
• Reusing components between Doku and Flynn
• Cross-pollination with other projects (e.g. Deus, Heroku)
• Relationship with Heroku and potential market share concerns
• Heroku is interested in Flynn, but there are differences in their business models
• Flynn is targeted at companies that need to run something internally for security, control, and latency reasons
• OpenStack was created as a platform for NASA to enable citizen science and participatory missions, but it's not competing with Flynn
• Flynn's MVP is expected this fall, and feedback will be important in its development
• The Flynn team values community feedback and is documenting its philosophies and technical guidelines to guide decision-making
• The Flynn project has a large and active community, with many forks and issues on GitHub
• Flynn community contributions and code participation
• Doku project and its relation to Flynn
• Learning Go programming language for participation in Flynn
• Tent project and decentralized communications platform
• Personal interests and hobbies outside of programming (film editing, music, indie games)
• Programming heroes: Brett Victor, Rob Pike
• The newsletter is sent out every Thursday with updates from the changelog
• The contributors are being ramped up to provide more content on the blog
• A t-shirt is available for purchase through the changelog website
• The speaker thanks Jeff and Jonathan for their work on an open-source project