• Incident.io: a platform for whole organizations to get involved in incident response
• Importance of incident response due to increased customer expectations and choice
• Current tooling has not kept pace with how people operate, leading to poor incident response solutions
• Incident.io's goal is to provide a structured, automated way to manage incidents, allowing teams to focus on the problem rather than the process
• Ideal incident workflow involves core defaults with customizable features for each company's specific needs
• Key principles of good incident response include:
	+ Keeping context all in one place
	+ Clear roles and responsibilities
	+ Structured coordination and communication
	+ Good internal and external communication
• Incident.io's goal is to provide an opinionated tool for incident response, building on core principles rather than being highly customizable.
• The company aims to create a scalable solution by focusing on essential features while allowing for extensions and integrations.
• The product has its roots in the experiences of Chris Evans, who worked on a basic solution at Monzo to simplify on-call processes.
• Incident.io was inspired by the limitations of existing tools, which often have "rough edges" due to no one owning or maintaining them.
• The company's founders drew from their experience working with complex systems and incidents in finance and e-commerce.
• The simplicity of Incident.io is intentional and reflects the company's focus on ease of use.
• The product's core feature allows users to create incidents with minimal onboarding, using one slash command or message shortcut in Slack.
• Incident.io uses an "osmosis" approach, where users are encouraged to learn by doing, and are given pointers and nudges as they progress.
• The company has a unique advantage in building the product because its founders knew what features they wanted from experience with similar problems at Monzo.
• Incident.io is used within the company for various use cases, including service outages, complicated bugs, and low-severity incidents to leave a trail of thought process and understanding.
• Using Incident.io for these types of incidents has benefits such as leaving a good trail for others to follow and acting as a structured way to hand over work.
• Discussion of using Incident.io for incident management and response
• Importance of having a low-cost entry point for reporting incidents
• Benefits of using a structured approach to handling incidents, including ease of escalation and communication with customers
• Statistics on the number of incidents reported and severity levels (91 total incidents, 8 major severity incidents over a year)
• Explanation of incident severity levels (critical, major, minor) and how they are used in Incident.io
• Discussion of organizational change and acceptance of incidents as opportunities for team assembly and problem-solving
• Overview of Incident.io's production setup, including use of Go app on Heroku and cloud providers for infrastructure management
• Monolithic Go binary architecture
• Service-based internal structure
• Asset handling through Go binary and Netlify
• Image serving complexity with Slack
• Feature flag management for testing new features
• Public product roadmap and community engagement for customer feedback
• Prioritization of feature development based on customer input
• Consideration of runbooks as a future feature
• Clarifying the concept of runbooks and their relationship to incident management
• Discussing the idea of capturing steps taken during incidents as knowledge to be reused
• Exploring how Incident.io's structure for storing information can help with incident analysis and recommendations
• Considering the integration of monitoring tools and data into Incident.io's system
• Emphasizing the importance of simplicity in product development and focusing on the 80% use case
• Sharing favorite blog posts, including one about learning from incidents in Formula 1 and another called "Incidents are for everyone"
• Current tooling is focused on engineers, not other teams such as customer support or executives
• Incidents involve multiple teams beyond engineering and require a more comprehensive approach
• Incident.io aims to build a tool that caters to the needs of non-engineering teams
• Simplifying and condensing complex information to facilitate communication between teams
• Learning from failure is key, and embracing incidents as opportunities for growth and improvement