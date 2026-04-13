• Space shipping and coding challenges
• Orbital Sidekick's hyperspectral imaging satellites and data processing
• Software development for space applications, including image processing and analysis
• Redundant systems and failover mechanisms for satellite components
• Challenges of writing code for hardware that can't be easily updated or debugged
• Importance of long-term support and reliability in space applications
• The challenge of balancing speed and agility in the aerospace industry, where traditional processes are slow and new startup culture wants to move fast
• Difficulty in scaling software development for satellites, where lead time for development and deployment is long
• Concerns with software dependencies, maintenance, and security in space, including patching vulnerabilities and dealing with CVEs
• Need for careful consideration of library and package usage, including compilation and build decisions
• Importance of parity between space processing and ground processing to ensure accurate results
• Balancing innovation and rapid development with the need for long-term sustainability and maintainability
• Difficulty in managing dependencies and complexity in space software development, including imagery analysis and automation scripts
• Challenges of designing a system that transmits large amounts of data from a satellite to the ground, and the benefits of prioritizing and processing data in real-time.
• The difficulty of debugging and troubleshooting issues in a satellite system, with a 90-minute window between passes and limited access to the satellite's systems.
• The contrast between the traditional, slow-paced culture of the aerospace industry and the startup culture of the company, with its emphasis on moving quickly and launching multiple satellites to test and refine the system.
• The shift from traditional on-ground testing to an approach that allows for faster iteration and deployment, with a focus on launching and testing satellites quickly and efficiently.
• The contrast between the Apollo-era culture, where a clear goal and deadline drove the mission, and the current era, where the goal is to add value to customers in a flexible and iterative way.
• The cost of launching payloads into space has decreased significantly, making it more accessible to startups.
• The industry is seeing a "quantum leap forward" in terms of speed and cost, with companies like the one Andrew Guenther is involved in, launching satellites for a fraction of the cost it would have taken in the past.
• The Federal Communications Commission (FCC) regulates the industry, with companies needing an FCC license to launch satellites and transmit radio waves.
• The FCC has issued fines for space junk and is working to establish regulations for the industry.
• The lifespan of satellites is typically around 5-10 years, with the satellite itself decaying from orbit after a certain period.
• Companies are developing technology to reduce communication delays between satellites and the ground, with the goal of enabling near-real-time data transfer.
• The conversation begins with a lighthearted discussion about naming a new internet system, with a comparison to the Outernet and the high bar set by naming the satellite Goose.
• The topic shifts to inter-satellite communication networks and the challenges of managing the increasing number of satellites in low Earth orbit.
• Andrew Guenther discusses the issue of collisions between satellites, citing instances where close calls have been reported, and the potential for significant loss of capacity if a collision were to occur.
• The conversation takes a humorous turn as Andrew shares a story about the Vatican claiming his company's satellite by mistake, and the subsequent "clerical error" correction.
• The discussion touches on the complexities of managing satellite tracking and the need for accurate identification to avoid collisions and loss of capacity.
• Career day at a kid's school
• Andrew Guenther's job working in space
• Andrew's kid's reaction to his job
• Pinkeye and other illnesses that come with having kids
• A crazy problem Andrew had to fix in space involving a satellite's radio connection
• Andrew's solution to the problem, which involved writing a custom script to assemble fragmented image files
• The challenges of working with satellite imagery and the importance of having a good team and vendor partners
• Andrew's personal experience and memories of working on the project
• Meta's Linux distribution and operating system infrastructure
• Anita Zhang's role as a D manager, supporting a team that contributes to Systemd and eBPF-related projects
• Meta's infrastructure, including a shared pool of machines called Twshared and a mix of compute, storage, and AI fleet
• CentOS and Fedora ELN use in production and testing environments
• Rolling release model and upgrades, including use of Fedora ELN and CentOS Stream
• In-house automation and tooling, including repo syncing and container orchestration
• Use of containers, isolation, and updates for jobs and workloads
• Twshared container scheduler and agent architecture
• Agent sets up namespaces and starts Systemd inside container
• Logs are preserved with a sidecar service
• Systemd units are translated from job spec
• Host profiles allow for dynamic allocation of resources
• Meta contributes to upstream open-source projects, but also maintains its own packages for faster release and testing
• Rolling OS upgrades are done with ABI boundaries in mind to minimize compatibility issues
• Release frequency and large host count require careful management to debug and maintain consistency
• Management of Nvidia drivers and isolation of GPU resources
• Team structure and roles (production engineers, system engineers, software engineers)
• Meta's on-prem infrastructure and machine pool, including containerization and service abstraction
• Common infrastructure services used internally (load balancing, package management, configuration management)
• Challenges facing the OS team and infrastructure, including AI fleet stability and determinism
• Homogenization of host hardware (CPU, RAM) and shift to larger hosts for bin packing and resource optimization
• Impact of AI on infrastructure and adaptation of infrastructure to meet specialized compute needs
• Meta's use of single-size hosts for compute tasks led to 18% total cost optimization and 11% performance increase
• Development of ASICs for inference and training tasks
• Use of FPGAs for development and testing of ASICs
• Implementation of Systemd and systemd-journald for logging and monitoring
• Use of immutable file systems and rolling updates for host management
• Efforts to replace syslog with systemd-journald and implement Senpai for memory auto-resizing
• Plans to upstream Senpai into Systemd
• Exploration of using immutable file systems and A/B switching for upgrades
• Discussion of using Systemd sysext for immutable filesystems
• Meta's open-source contributions and whitepapers
• Use of open-source technologies by Meta
• Meta's approach to sharing knowledge and solutions freely
• OctoPrint and Gina Häußge's experience with open-source and crowdfunding
• Gina Häußge's background and the development of OctoPrint
• Discussion of filament diameter and how it has changed over time
• Support for various 3D printers in OctoPrint, including those with proprietary firmware and closed-source systems
• Concerns about proprietary systems locking users out of accessing and customizing their printers
• The role of open-source software in 3D printing and the potential for proprietary companies to dominate the industry
• OctoPrint's release process, including testing and release candidates, to ensure stability and security
• The difference between OctoPrint and OctoPi, with OctoPi being the image that OctoPrint is installed on
• Gina Häußge's test rig, which uses three Raspberry Pi 3s and a fourth Raspberry Pi 4 (flash host) to automate testing and flashing of SD cards
• The process of automating testing and release of new OctoPrint versions, including creating a test matrix, writing JSON files, and triggering GitHub Actions
• Gina Häußge's background as a software engineer, including her work in Enterprise Java and her decision to leave her job to focus on OctoPrint
• The use of GitHub Actions to automate the testing and release process, including building updated images and running end-to-end tests
• Gina Häußge's background and decision to leave her Java job and work on OctoPrint full-time
• Gina's initial self-funding model through community support and small donations
• Open-source model and Gina's feelings on the open core model
• Gina's funding model and revenue stream from users and business sponsorships
• OctoPrint's user base and tracking of anonymous installs
• Gina's reaction to the success of OctoPrint and its impact on her life and career
• Gina's reflection on her previous job in enterprise Java and her current work on OctoPrint
• Difficulty switching between Python and JavaScript due to different syntax and habits
• OctoPrint's future development and maintenance, including updating the tech stack and communication layer
• Challenges in pushing developers to update their plugins for new versions
• Legacy issues, including Python 2 support and difficulties in updating the UI
• Wish to have made different architecture decisions in the early stages of the project
• Challenges in learning and adapting to new technologies and approaches over time
• Gina Häußge's software development experience with Tornado and Flask
• Importance of asynchronous connections for performance
• Gina's mistakes in the past, such as mixing single-threaded and sync code
• Growth of 3D printing and software development over the past decade
• Challenges of maintaining and updating software over time
• Benefits of automating tasks, but potential pitfalls
• Gina's approach to releasing software, including avoiding releases on Fridays
• The importance of testing with real users and gathering feedback
• Gina Häußge discusses her projects and interests in 3D printing and open-source software development
• She talks about her recent focus on creating print-and-play board games and her previous projects, such as creating environment sensors for the Chaos Communication Camp
• Gina's "superpower" is her ability to solve problems and come up with creative solutions, and she attributes this to her experience as a Java engineer and her use of 3D printing to bring her ideas to life
• She shares her habit of listening to audiobooks to help quiet her brain and fall asleep, and her trick of listening to books she has already read
• The conversation also touches on Gina's involvement with the OctoPrint project, a successful open-source project for controlling 3D printers, and the importance of community funding and support for open-source projects