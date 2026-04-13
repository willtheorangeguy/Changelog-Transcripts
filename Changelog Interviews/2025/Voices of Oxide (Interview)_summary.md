• Low-level firmware development for computer systems, specifically the initial power-on sequence
• Comparison with BIOS and understanding of the role of smaller processors in enabling larger processors to turn on
• Use of custom-built boards and a "first principles" approach to design
• Writing culture and documentation practices at Oxide, including Request for Discussion (RFD) and living documentation
• Cliff Biffle's experience with Rust programming language and its adoption at Oxide
• Cliff Biffle's background and interest in Rust, starting from his work at Google in 2015
• Product not suitable for the speaker
• Building an engineering org from scratch
• The team's use of Rust for software development
• The Helios operating system and its use of C
• Comparison of Rust with Go and its suitability for firmware development
• Hubris operating system and its development process
• Tock operating system and its limitations for the speaker's needs
• The growth and deployment of the Hubris operating system
• Hubris kernel is approximately 1,000 lines of code but requires additional components to be useful
• Hubris runs on various devices, from sub-$50 microcontrollers to large service processors
• Multiple instances of Hubris exist on a full rack system, including service processors, root of trust, and manufacturing tools
• There are around 20-30 copies of Hubris across a full rack system
• The reasons for multiple copies include security requirements and the need for a separate root of trust
• Cliff Biffle mentions the possibility of merging the service processor and root of trust functions in the future
• Oxide may start making its own chips in the future, possibly through a collaboration with AMD
• Hubris is open-source and used by several companies, including some startups and Volvo, although Volvo is hesitant to contribute due to certification requirements
• The developers mention that more work needs to be done to make Hubris more user-friendly for non-Oxide customers
• The team discusses issues with fans malfunctioning in the building, which can be caused by software crashes or firmware updates gone wrong
• Discussion of a chip and its fan kicking up due to a watchdog service processor issue
• Comparison of working at Oxide to being in a TV show, specifically referencing The Office and Silicon Valley
• Personal anecdote about the CEO being based on a real person and having a monkey
• Conversation about the potential of Oxide being featured in a TV show
• Discussion of churn at Oxide, with reasons including personal preferences, remote work not working for some, and past work trauma
• Mention of uniform compensation and its benefits for employees
• The benefits of a uniform compensation system, where everyone is paid the same amount of dollars
• Cliff Biffle's experience with salary disparities at Google, and how he likes the fairness of the current system
• The role of equity and ownership in the company, and how it contributes to a sense of being "all in this together"
• The company's hierarchy and management structure, and how Cliff views being a manager as a role, not a position of authority
• The process of updating the Oxide system, and the challenges of making it self-service and automatic
• Mupdate is a procedure for updating the software on compute sleds
• The priority was to have a robust support procedure for recovering the software on any compute sled, regardless of state
• The update process is complex, involving hundreds of components, including software updates to service processors, root of trust, bootloader software, host OS, and control plane software
• The update process is simplified for operators, who only need to think about policy, not the underlying software updates
• The update system involves downloading a large zip file (2-3 gigs) from the company's download site and uploading it to the rack via API
• The process is designed to accommodate air gaps, where the rack is not connected to the internet
• The company's Hubris operating system is one of the components updated as part of the Mupdate process, which talks to the service processor to update other components.
• The challenge of updating software at a low layer, such as BIOS, which is not designed to be interacted with by automation.
• The company's goal of delivering non-disruptive updates without rebooting customer VMs, currently achieved by live-migrating VMs to other sleds while updating.
• The complexity of mechanically moving VMs to other sleds, which is a bin packing problem, and ensuring there is enough capacity to do so.
• The need to create an experience for operators that communicates the trade-offs of keeping capacity free for updates versus allowing the possibility of updates being paused.
• The potential for failed updates in the self-service world when a new version is released.
• Non-disruptive updates
• Challenges with intermediate states in self-service updates
• Ordering of updates to prevent backwards compatibility issues
• Sleds failing or being unavailable during updates
• Automation and testing to prevent update failures
• Point of no return and rollback issues
• Downtime required for updates
• Non-disruptive updates for future development
• Hot swapping and avoiding reboots
• Upgrading software and potential risks
• Bifurcated code paths and their consequences
• Guardrails for change management to prevent failures
• Novel testing strategies, including fuzzing and property-based testing
• Updates as a project, including challenges and timelines
• Self-service updates and non-disruptive updates
• The acquisition of Joyent and the formation of a new vision for the company
• The role of Rust in facilitating the development of reliable and automated systems
• The use of the RFD (Request for Discussion) process for collaboration and feedback
• The advantages of Rust in ensuring memory safety and preventing versioning issues
• The use of tools like Dropshot and Progenitor to generate open API specs and clients
• The confidence in the correctness of the code due to Rust's strictness and type system
• The contrast between the experience with Node.js and the experience with Rust
• Rust compiler and its value in solving complex problems
• OxCon: a company-wide meetup for remote teams
• Oxide company design and brand story
• Ben Leonard's role in designing Oxide's branding and UI
• Industrial design and how it informs the product and brand
• Balancing consistency and creativity in design
• Limitations of manufacturing and materiality in design
• Challenges with color matching and material consistency
• Compromises made in design due to manufacturing constraints
• Industrial design and hardware limitations
• Importance of design language and values in branding
• Balance between investment in design details and cost
• Variety and scope of work at Oxide that keeps Ben Leonard engaged
• The benefits and challenges of working with a new brand
• The tension between consistency and change in brand identity
• The impact of company growth on design needs and opportunities
• The creative process and the role of design in a company's success
• The importance of design in setting a company apart and showing intention and trust