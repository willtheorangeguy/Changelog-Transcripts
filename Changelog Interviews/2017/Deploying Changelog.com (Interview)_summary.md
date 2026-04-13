• Gerhard Lazu's background and involvement with Changelog.com and its previous infrastructure
• The development of Deliver and eDeliver, tools for deploying Erlang applications
• The switch from using Deliver and eDeliver to a new infrastructure approach
• The timeline and planning for the new Changelog.com website and CMS launch
• The actual launch process and challenges in migrating content from the old site to the new one
• The role of Gerhard Lazu in deploying the new Changelog.com website and CMS
• The discussion of Ansible and its relationship to Deliver and eDeliver
• The challenges and humor in developing and deploying a new infrastructure and website
• Defining goals and understanding what the client wants to achieve
• Separating "What?" from "How?" and understanding the client's approach to infrastructure and deployment
• Asking high-level, big-picture questions to clarify goals and constraints
• Using a story backlog process to prioritize tasks and focus on business value
• Embracing a process of learning and discovery, and sharing what's learned
• Prioritizing tasks based on user needs and constraints
• Preserving original intent and what matters over time using tools like Pivotal Tracker
• Working with a distributed team and across different time zones
• Considering the importance of documentation and preserving context for future team members and developers
• Gerhard Lazu discusses his talk "Not Working Together" about approaching teamwork and knowledge sharing in a team
• Gerhard's experience with working with various teams and approaches to make sure knowledge and learnings are shared and not lost
• The importance of understanding the specific needs and constraints of a project, and asking the right questions to achieve those needs
• Gerhard's process of understanding a project's requirements and limitations, including identifying what is important and what is not
• The use of Pivotal Tracker as a tool for communication and collaboration, particularly in remote work situations
• The importance of understanding the constraints and limitations of a project, including existing relationships and legacy content, in order to make informed decisions about infrastructure and process.
• The importance of using tools like Pivotal Tracker in a disciplined and thorough manner to achieve success
• The value of separating "What?" from "How?" when defining stories and units of work
• The need to capture context and conversations related to project decisions and changes
• The importance of understanding the "Why?" behind project decisions and changes, not just the "How?"
• The role of discipline and attention to detail in using tools like Pivotal Tracker effectively
• The benefits of having a shared understanding and documentation of project decisions and changes through tools like Pivotal Tracker
• The value of using tools like Pivotal Tracker as a reference point and documentation for future projects and phases
• The focus on team dynamics and creating a positive work environment through the use of tools like Pivotal Tracker.
• Docker and containerization
• Moby (Docker's new name)
• Comparison of Docker with other technologies like Garden
• Benefits of using Docker for developers
• Changelog.com infrastructure
• Use of Ansible, Concourse, and Docker
• Elixir application and PostgreSQL database
• CDN (Fastly) and static content distribution
• Linode hosting and server utilization
• Importance of having full backups of the Changelog, including the entire application and database
• Using Amazon S3 for storing backups, including self-expiration after a set period (7 days)
• Automatic backup and restore process, currently manual but being automated
• Use of Ansible and Docker for building and deploying the Changelog
• Potential for lock-in to the hosting provider (Linode) and dependence on Docker
• Discussion of why Kubernetes was not used in the Changelog's development
• Comparison of Kubernetes with Ansible and Docker for building and deploying the Changelog
• Complexity of migrating to Kubernetes
• Comparison of Ansible and Kubernetes for infrastructure management
• Flexibility of current system and ability to switch to different platforms
• Importance of small, manageable steps in system development
• Adapting to changing technology landscape and not getting too far behind
• Measuring tangible benefits against cost of change before implementing new technologies
• Migration from WordPress to a bespoke infrastructure
• Comparison with Kubernetes and mainsteam solutions
• Discussion of the trade-offs and complexities of using Kubernetes
• Retrospective on the migration process and lessons learned
• Highlights of the new infrastructure's features and benefits, including pipeline automation and centralized logging
• Comparison with the old infrastructure and the effort involved in migrating Tumblr redirects
• Unified logging interface and containerization using Concourse
• CI pipeline automates deployment and reduces complexity
• Docker and Garden used for containerization
• Containerization is a valuable concept, with Concourse using Garden for container management
• SSH key management and rotation issues
• Homegrown stack had pain points with components not interacting well together
• Knowledge transfer and documentation are key issues, rather than technical problems
• Considering moving to a hosted platform as a service (PaaS) such as Kubernetes or Cloud Foundry.
• Technical issues with infrastructure and management being addressed
• Institutional issues and the time it takes to fix them
• The importance of focusing on the goal, not the technology or tools
• The developer experience and workflows for different types of applications (e.g. Kubernetes, Heroku)
• Gratitude and appreciation from the hosts for Gerhard's contributions to the community and the Changelog