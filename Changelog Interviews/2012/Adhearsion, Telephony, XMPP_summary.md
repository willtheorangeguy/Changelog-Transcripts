• The Change Log is brought to you by Pusher, a company hiring a system engineer for evented systems.
• The hosts, Adam Stachowiak and Wynne Netherland, introduce the episode and discuss their previous show on telephony.
• They welcome Ben and Ben from Adhesion, an open-source framework for voice applications, and discuss its features and architecture.
• Adhesion is compared to frameworks like Ruby on Rails, providing a clean API and integration points for developing voice applications.
• The hosts ask about the architecture of Adhesion and its stack, with Ben Klang explaining it's a fully-featured framework, not just a library.
• Adhesion 2.0 framework for building telephony applications
• Support for multiple telephony backends, including Asterisk, Prism, and cloud-based services like Tropo
• Modular design to add support for new backends in the future
• Ability to abstract telephony APIs from the DSL
• Goal of making applications portable across supported backends
• Cloud support, including cloud deployment and use of cloud providers like Tropo
• Practical applications of Adhesion, including IVR, Call Center, and distributed call centers
• Example of using Adhesion to build a dictation service with transcribers around the country
• Future possibilities for cloud-deployed Adhesion telephony applications
• Ability to use modern programming languages with existing libraries
• Replacing legacy telephone systems that are not programmable or maintainable
• Advancements in telephony technology, such as Skype and WebRTC
• Enabling new applications with rich communications channels
• Overview of Adhesion 2.0's plugin system and its similarities to Railties
• Anatomy of an Adhesion plugin and its functionality
• Architecture of an application, including the use of a controller and MVC-like structure
• Comparison of Adhesion's architecture to Ruby-based systems
• Introducing call controllers in Adhesion 2, which brings an MVC-like approach to voice applications
• Using the phone call as a view and rendering audible input and output
• Manipulating the call view with controllers and applying combinations of views
• Integrating with data sources or models to provide dynamic menus or capture user responses
• Applying the classic MVC pattern to voice application scenarios
• Using routing DSLs to match incoming calls and variables
• Addressing challenges in creating global applications, including phone number inconsistencies and internationalization
• Discussing time zone challenges in real-time interaction with users
• Plans for a follow-up Adhesion conf, which was half again larger than the original in 2011
• Goals and achievements of the Adhesion framework
• Number of contributors and users of the framework
• Adhesion's use by government agencies, including the Department of Defense and the US Army
• Potential for Adhesion to be used as a prank calling system or for other malicious purposes
• History of the framework, including its initial presentation and early adopters
• Current use of Adhesion in corporate voice networks and its potential for hosted PBX services
• Future plans for Adhesion, including potential support for video and other adapters.
• Modes of operation for the platform, including lecture mode and active speaker mode
• Limitations of video support, including transcoding and the "Brady Bunch" effect
• Adhesion's role as a third-party control layer, handling authentication and IVR
• Use cases for IVR, including translation services and non-traditional applications
• Multiple interface modes for calls, including web browser, mobile app, and voice call
• Open-source XMPP protocol and its potential for flexible communication channels
• Development of XMPP-based libraries and tools, such as Blather and XMPP bots
• XMPP protocol capabilities and use cases
• Adhesion project and its use of XMPP and Blather
• Background of the speaker and their work with physics, Ruby, and software engineering
• Ben Zero's background and experience in systems administration and telephony
• The Adhesion project and its evolution, including its shift from a traditional phone system to a modular, middleware-based approach
• Discussion of programming heroes and influences
• Mention of notable Ruby programmers and projects, including:
	+ Jeff Smick and Blather
	+ Celluloid project
	+ Tony's concurrency framework
	+ Mike Perham's work
	+ JRuby project
• Introduction of Adhesion 2.0 and its connection to Celluloid project