• NATS is an open-source messaging system that was created in 2010 as part of Cloud Foundry project at VMware
• NATS was designed to provide a simple, location-independent, and scalable way to connect applications
• It was created by Derek Collison as a response to the limitations of RabbitMQ, which was too complex and inflexible
• NATS aims to provide a "dial tone" for messaging, allowing applications to communicate with each other without worrying about the underlying infrastructure
• It has been rewritten in Go and has seen significant adoption and success, with many companies using it to power their distributed systems
• NATS provides a simple and efficient way to handle one-to-many and many-to-many communication patterns, and supports both push and pull messaging models
• It has been designed to be location-independent, allowing applications to communicate with each other regardless of their physical location
• NATS has been used in various use cases, including command and control, telemetry, eventing, and more.
• Discussion of NATS's performance limitations with Go
• Need to address Go's disk IO and concurrency issues
• Introduction of JetStream and its impact on data persistence
• Derek Collison's personal experiences with Rust, Zig, and Mojo
• Discussion of event loops and io_uring interactions in various languages
• Pros and cons of using Zig and its ability to control direct IO
• Overview of the challenges of scaling NATS and the need for fine control over disk IO
• Discussion of customer requirements and the need for a billion message passes per second
• Explanation of subject-based addressing lookup and the challenges of indexing it
• Challenges with indexing and subject-based addressing in large-scale message systems
• Plans to solve these challenges in the next version of the server (2.12)
• Shift from a closed-source to an open-source project, including the release of NATS in 2010
• Impact of Kubernetes on the market and the decline of Apcera's ACV
• Decision to spin off NATS and create Synadia in 2017, based on a bet that edge would dominate interaction models within a decade
• Expectations for edge computing to require different tools and approaches than cloud computing
• Assessment of how this bet has played out so far
• Synadia's founding and mission to serve critical production needs
• Open-source software (OSS) and the challenges of commercializing it
• NATS and its involvement with CNCF, including potential relicensing and controversy
• Derek Collison's involvement with the CNCF and NATS, including his role on the founding governing board
• The CNCF's relationship with NATS and other projects, including the concept of "fit" and "valuation"
• The BSL license and its implications for OSS and commercialization
• The controversy surrounding Synadia's consideration of the BSL license and potential implications for OSS and vendors
• The need for a broader discussion about OSS, commercialization, and the value of open-source projects
• Derek Collison's concerns about the CNCF's evaluation of NATS for graduation
• Concerns about the CNCF's evolving criteria for project graduation
• The role of the CNCF's Technical Oversight Committee in formalizing evaluation criteria
• The impact of the CNCF's requirements on Synadia's business model
• The importance of diversity in code contributions to a project's success
• The potential for conflict between a project's business model and the CNCF's goals
• The role of brand equity in a project's success, specifically with regards to the NATS name.
• Disagreement over NATS' fit with the Cloud Native Computing Foundation (CNCF) and its potential for leaving the CNCF
• Discussion of Kubernetes' history and its role in the cloud provider mobility
• NATS' history and its relationship with the CNCF, including its incubation and graduation status
• The CNCF's position on projects leaving the organization, and its stance on NATS
• The concept of "graduation" from the CNCF and its implications for projects
• The emotional and financial aspects of projects leaving or staying with the CNCF
• The potential for companies to fork projects and abandon the original if they don't meet the CNCF's standards
• The nuance and complexity of the CNCF's processes and decision-making
• Confusion and anger from the open-source community due to Synadia's decision to relicence NATS from the Apache 2.0 license to the MIT license
• Derek Collison's explanation of the decision, citing the need to create a business model that aligns with Synadia's goals and the changing landscape of the CNCF
• Discussion of the challenges of driving revenue in open-source projects and the importance of contributions in various forms, including commercial agreements
• Criticism of the media for conflating the relicensing of NATS with Synadia's decision to leave the CNCF
• Derek Collison's frustration with the lack of dialogue and the negative reactions from the community
• Discussion of the potential consequences of a single company driving mission-critical functionality in open-source projects
• Discussion of NATS governance and the lack of a TOC (Technical Oversight Committee) to provide direction and oversight
• Comparison to the CNCF governance model, which is more limiting and governed by other entities
• Derek Collison's experience with trying to graduate NATS from the CNCF due to code contribution issues
• Modular project's license change to AP2 with additional constraints and potential implications
• Discussion of trademark and intellectual property ownership and transfer when a project joins the CNCF
• Proposal to establish a TOC or TSC (Technical Steering Committee) for NATS to provide more diverse open source governance
• Trademark dispute between Synadia and the CNCF
• Synadia's frustration with the CNCF's handling of the trademark issue
• CNCF's suggestion that Synadia change the trademark to avoid a costly legal fight
• Synadia's successful defense of the trademark and subsequent agreement to transfer ownership to the CNCF
• Criticism of the CNCF's handling of the situation and lack of clear agreements or communication
• Discussion of the need for clear agreements and expectations in collaborations and partnerships
• Discussion about transferring trademarks to open source community
• Consideration of a commercial fork with a permissive license (BSL)
• Concerns about open core model and vendor lock-in
• Decision not to pursue BSL and instead to expand commercial offerings through composition
• Commitment to post a list of features to be added to the AP2 server without delay
• Plans to offer additional security features and appliances through commercial offerings
• Emotional decision-making and the importance of nuanced discussions in open source software
• The phenomenon of "rug pull" and its impact on the community
• The need for a dialogue on the underlying issues and ecosystem failures
• The concern that customers are funding development through VC dollars, rather than a sustainable business model
• The importance of maintainers in the success of a project
• The need for a broader discussion on how to improve the ecosystem and the role of organizations like the CNCF and Linux Foundation
• Concerns about CNCF's approach to stability and longevity of projects
• Potential disruption when maintainers leave projects
• Discussion of symbiotic relationships between projects and their maintainers
• Open-source funding and budget allocation at Synadia
• Addressing "entitlement" mentality in open-source users
• Balancing accessibility and sustainability in open-source projects
• Importance of care and consideration in open-source development and community building