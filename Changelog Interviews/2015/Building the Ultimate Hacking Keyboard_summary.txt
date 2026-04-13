• Ultimate Hacking Keyboard (UHK) development and features
• Lazlo Monto's (Latsy) background and name conventions in Hungary
• Sponsorship and partnership with TopTile and The Change Log
• Lazlo's experience as a TopTile network member and blog post on TopTile blog
• From the Ground Up, How I Built the Developer's Dream Keyboard blog post on TopTile blog
• The guest's blog post on building a developer's keyboard was featured on the TopTile blog and received a huge response
• The post was also featured on java.dzone.com and received attention on SlashDot, with a huge ripple effect and 2,000 subscribers gained
• The guest discussed the history of their project, the Ultimate Hacking Keyboard, and its development
• The guest's early life and exposure to computers, starting with a Commodore 64 at the age of 6
• The guest's journey to becoming a software developer and the challenges they faced, potentially related to their non-native English language and location in Hungary
• Programming allows for breaking down problems and solving them
• Early exposure to programming through PC and web development
• Transitioned from programming in multiple languages to focusing on JavaScript
• Defined as a polyglot due to familiarity with multiple languages and frameworks
• Approach to problem-solving involves choosing the most suitable language and framework
• Has worked with various languages including Java, .NET, Python, JavaScript, and C
• Has experience with GUI, command line, client, and server applications
• Has worked on designing hardware and soldering microcontrollers
• Has a background in programming microcontrollers and understanding software stacks
• The Ultimate Hacking Keyboard's crowdfunding campaign is on CrowdSupply, not Kickstarter.
• CrowdSupply is similar to Kickstarter but has additional features, including PR and manufacturer contact assistance.
• The campaign has already reached 104% funding and ends this Sunday.
• The creators built their own connections with manufacturers, but the additional services provided by CrowdSupply are an option.
• A successful crowdfunding campaign requires proactively building a subscriber base before launching.
• The campaign is live on CrowdSupply and a link will be included in the show notes.
• The show is a discussion about the Ultimate Hacking Keyboard (UHK) and its crowdfunding campaign
• The conversation will cover the software and hardware behind the UHK, as well as its creator's experience
• The UHK campaign is ending on December 13th, and backers will be able to take pre-orders
• After the campaign, pre-orders will cost $220, and shipping is expected to begin in July 2016
• The conversation will delve deeper into the UHK's features and the process of creating hardware and software that work together
• The creator's experience with TopTal, a platform for freelance software developers, is also mentioned
• Design principle: stay on the home row and never leave it, with a universal approach in every application
• Split keyboard to separate hands and allow for positioning and orientation of keyboard halves
• MOD layer for navigation and layer switching
• Navigation block on JKLI keys, with layer switcher key on MUD key
• Keys outside of the alpha-numeric block mapped to the alpha-numeric block with the MOD layer
• Keyboard splits at the 6 key, with symmetry as the reason for the placement
• Four layers: base layer, MOD layer, mouse layer, and FN layer for MIDI shortcuts
• Keyboard exposes standard USB descriptors, no special drivers needed
• The UHK keyboard's design allows for efficient access to modifier keys and shortcuts.
• The keyboard is designed to be ergonomic, with a split design that allows for comfortable typing and mouse navigation.
• The keyboard's compact, truly split design is reconfigurable and can be used in various positions.
• The speaker's goal was to create a keyboard that addressed the issues of existing ergonomic and mechanical keyboards.
• The speaker wanted to create a keyboard with open-source underlying software, including firmware and electronics design files, and a GPL-licensed agent.
• The speaker's goal was to improve productivity and ergonomy for software developers.
• Motivations behind open source development
• Frustration with proprietary devices and their limitations
• Desire to empower people through open source software development
• Importance of community and open source in software development
• Past experiences influencing current views on open source development
• Technical aspects of open source development and hardware rebuilding
• Discussion of the Ultimate Hacking Keyboard (UHK) and its open-source components
• Review of the UHK's GitHub repositories, including agent, electronics, firmware, and bootloader
• Explanation of the agent application and its planned development into a GUI configuration tool
• Discussion of the mouse function and its accuracy
• Explanation of the Node WebKit (NWJS) runtime and its use in the UHK project
• Description of the UHK's capabilities, including its multiple layers of functionality and programming options
• Inertia in keyboard pointer movement is a useful feature
• Add-on modules can be mounted to the main keyboard for additional functionality
• Modules are optional and can be purchased separately
• The protocol for module communication will be open-sourced for third-party developers to create their own modules
• A developer kit and CAD data will be published for module creation
• Hackers can 3D print their own modules using the open-source protocol
• Modules are mechanically constrained to specific locations between the keyboard halves
• Pogo pins provide electricity and data for modules
• The keyboard can be broken apart to accommodate custom modules
• The open-source protocol allows for forking and modification of existing modules
• Users can potentially 3D print their own modules and connect them to the keyboard
• The goal is to cram as much functionality as possible into the hardware.
• The agent is a crucial component that has been discussed in previous emails.
• The firmware and electronics project are open-sourced and available on GitHub.
• The electronics project uses KiCAD, an open-source electronic design automation suite.
• The project is building on existing open-source software and platforms.
• The firmware sends key press and release events to the right keyboard half, which maintains a matrix of keys and decides which layer is active.
• The firmware exposes three different USB interfaces: keyboard, mouse, and a generic HID interface.
• The firmware uses a lightweight USB library called Luffa for AVR microcontrollers.
• USB library and keyboard matrix
• Left and right keyboard halves and their communication
• Key press and release handling
• Layer switcher keys and USB reports
• Ultimate hacking keyboard and its potential for customization and hacking
• The importance of open-source hardware and software
• The role of the keyboard in the lives of hackers and tinkerers
• TopTile's commitment to enriching developers' lives
• Sponsor mentions and recommendations
• Linode's promotion of their cloud servers and the code "ChangeLog10" for a discount
• Latsy's software development background and potential "super secret" project
• The Ultimate Hacker Keyboard (UHK) and its unique features, such as add-on modules and stainless steel inserts
• The UHK's open-source component and its potential for customization and extension
• Plans to build future keyboards, such as an 80% version, based on the UHK's hardware-software architecture
• The UHK's extensibility and flexibility, allowing users to design keyboards of other shapes and forms
• Customizability of the UHK for various applications, including games and IDEs.
• Remapping keyboard keys for specific applications or games
• Configurator application for customizing keyboard layout
• Plans for future development of the configurator application
• Support for developers who create modules but lack 3D printing capabilities
• Availability of developer kits for sale
• Requirements for developing physical modules (hardware skills and experience)
• Challenges of creating physical modules with complex electronics and materials
• Incurring costs with hardware and learning as you go
• Importance of practice and patience
• Creating a new voice tool and ordering necessary components
• The concept of being a platform and its implications
• Making promises to developers and users through a product
• The makeup and durability of the product
• Supporting and investing in the product's development and community
• Discussion of packaging and sharing of a project
• Mention of integrated hardware and software
• Comparison to other products
• Reference to a "brave statement" made about the product's design
• Discussion of revealing details and getting people excited about the project
• Question about an open-source piece of the project
• Mention of firmware and other components
• Discussion of repositories and the project's structure
• Documentation is lacking in the project.
• The speaker plans to add documentation to the project over time.
• The project is new and open-source, and the speaker wants it to be easily digestible and hackable.
• The community may provide feedback and guidance to the speaker.
• The speaker is asking for patience and understanding from those trying to contribute to or hack the project.
• Funding for a project has been secured through Crowd Supply
• The project team is under pressure to deliver results quickly
• Priorities for the project include creating molds for plastic parts and finalizing the design
• The mold-making process will take 3-4 months, so it's crucial to start as soon as possible
• The current prototype is the 5th generation and will be iterated upon to improve manufacturability
• Next steps include contacting a company to create the final product
• Developing molds and add-on modules
• Creating firmware and agent software
• Partner's mechanical engineering expertise
• Comparison to outsourcing to China
• Hidden costs of outsourcing
• Advantage of having a local partner
• Involvement of multiple people in the project
• Discussion of Andres' mechanical solutions being robust and professionally designed
• Mention of Andres being a great mechanical engineer and perfectionist
• Question about something super secret about Andres that is not known by others
• Andres' self-description as a perfectionist who takes code quality seriously
• Discussion of Andres' ability to work in a team despite being a perfectionist
• Fears of creating something that might be perceived as awesome or terrible
• Courage required to make and deliver something real
• Perfectionism vs. releasing something despite fear of failure
• Fear of success and the pressure to deliver a successful outcome
• The impact of fear on the person creating something and potentially holding them back
• The speaker is talking about a significant phase in their life
• The speaker wants to achieve something and thinks it can be a great offering for many
• The speaker is asked about their "programming hero"
• The speaker mentions John Carmack and Jeff Atwood as influences
• The speaker discusses the achievements of John Carmack, specifically his work on the Doom engine, and Jeff Atwood, specifically his creation of the Stack Exchange
• Discussion of the ease of talking to a smart and capable guy
• Mention of Stack Exchange and its ripple effect
• Reference to Trello and its use at ChangeLog
• Discussion of Stack Overflow and its importance
• Mention of Dean Camera and his Lufa library
• Discussion of heroes in software development
• Explanation of the purpose of the "heroes" segment on the show
• The influence of others on the person's actions
• The person's heroes and role models
• The difference between game developers and software developers
• The UHK (Universal Human Interface Keyboard) and its open-source software
• The person's interests and projects outside of UHK work
• Interest in Angular 2 and building an agent on top of it
• Current API flux as a barrier to exploration
• Interest in microcontrollers and IoT platforms
• Discussion of building a smart home if time allowed
• Mention of an ultimate hacking keyboard and its open source platform
• Invitation to share the show on social media
• Discussion of a new product or project involving Lassie
• Request to share the product with a keyboard
• Announcement of a future release date and encouragement to share the product with others
• Closing thoughts from Lassie and appreciation for the audience
• Host's closing remarks and thanks to listeners and supporters
• Membership options and benefits
• Changelog membership and access to exclusive content
• Sponsorship and partnerships with CodeShip, TopTile, Harvest, and Linode
• Promotion of changelog tea and discount offer
• Farewell and closing remarks