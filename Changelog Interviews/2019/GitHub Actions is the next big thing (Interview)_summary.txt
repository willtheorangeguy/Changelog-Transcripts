• Ecosystem Engineering: managing external APIs, identity, marketplace, and billing to make GitHub useful to users
• Platform team: created a platform group to make GitHub a platform for software development, rather than just a feature company
• GitHub Marketplace: created to bring new, interesting tools to market, making it easier for smaller teams to compete with larger companies
• Barrier to entry: having some traction, with criteria including user value and usage
• Future of developer tools: niche tools that solve specific problems, rather than trying to do everything
• Cloud and platform encroachment: companies like Microsoft, Amazon, and Google entering the developer tool space
• GitHub Actions allows workflow automation within GitHub, running code for the first time.
• GitHub Actions is a beta feature that allows developers to define workflows in a file within their repository.
• The feature is considered "low-key revolutionary" and potentially extremely disruptive.
• The development of GitHub Actions took about a year, with a shift from pure workflow conduction to arbitrary code execution.
• The goal is to give customers the raw compute and flexibility to define their own workflows, rather than dictating specific integrations.
• GitHub Actions is being used for a wide range of tasks, from building and deploying to checking for best practices.
• The feature is seen as being in the spirit of Git itself, allowing developers to use it in the way that best suits their needs.
• Git and Git adoption: freedom creates overhead, but Actions aims to simplify workflows
• Prosumer approach: "Okay, you can do anything" and letting the community create and share workflows
• Heroku's Buildpacks idea: providing pre-made solutions for common use cases
• Actions replacing bots: taking away the execution and letting users focus on building activities
• Workflow automation: making it easier for developers, especially in large businesses, to implement automation
• WordPress plugin ecosystem comparison: finding and installing pre-made solutions to simplify development
• Actions as a tool for making every GitHub user a potential integrator, and better understanding the community's needs.
• GitHub Actions and their potential to onboard new users
• How Actions work: using workflow files, Docker containers, and the visual editor
• Workflow files and their syntax (HCL subset)
• Individual actions as Docker containers with access to GitHub token and repository
• The Actions environment as a VM for security and scalability
• Services behind the scenes to trigger and orchestrate workflows and actions
• Limitations and future plans for the GitHub token and secrets
• The flexibility of Docker containers within Actions
• GitHub Actions needs beefier machines to handle complex workflows, especially for continuous integration (CI) in GitHub.
• The team is exploring options to provide more compute resources for workflows that can be parallelized.
• The current limitation of running parallel actions on a single VM is being addressed to allow for more flexible and independent execution.
• The dependency tree is crucial in determining how actions are executed, and the team is working to improve its visualization.
• GitHub Actions is in beta, and the team is focused on gathering feedback from users to inform its development.
• Feedback has been varied, with some users using Actions to orchestrate outside tools and others using it for automated packaging and workflow improvements.
• The team acknowledges that Actions is still in a "prosumer" state, requiring users to have some technical expertise to use it effectively.
• A visual editor is being developed to make it easier for users to create workflows without requiring extensive technical knowledge.
• The visual editor is built using a separate service that runs inside an iframe within the GitHub application.
• Development of a new editor for workflows, inspired by the Actions editor
• Building a parser to ensure the new editor's output is contractually correct
• Using an iframe to decouple the new editor from the main application
• Discussion of GitHub's shift to a microservices architecture and the challenges of managing multiple technologies
• Exploring the possibility of moving GitHub Actions to an organization-level, rather than just a repository level
• Addressing the need for better authorization management and unified business identity
• The importance of iteration and feedback before expanding to larger, more complex ideas
• Competition between GitHub Actions and external CI products
• Potential impact on vendors and partners in the CI market
• Balance between providing a free alternative and supporting commercial vendors
• Future possibilities for actions to be monetized and sold
• Discovery and visibility of actions on the Marketplace
• Supporting both open-source and proprietary actions
• Implementing a rating system for Marketplace apps to improve signal-to-noise ratio
• Developing a discovery story to help users find relevant GitHub Actions
• Overhauling categories and education piece for users to understand tools and their use cases
• Investing in the producer side of GitHub Actions
• Plans to make it easier for users to find and install GitHub Actions
• Bet on the extensibility of the GitHub experience, making it easier for users to integrate outside tools
• Vision for GitHub Actions to revolutionize software development workflow
• Feedback from beta customers has been positive, with some seeing it as a game-changer
• Actions is a network of integrations that simplifies workflows and provides a simpler experience for developers
• The goal is to allow developers to build the best editors, error trackers, and other tools without having to start from scratch
• Partners can use Actions to extend their existing business and create new interactions with customers
• The future of Actions includes bringing compute to more users, expanding the beta program, and adding new features such as the Content Attachments API
• Actions will enable new and interesting ways to extend the GitHub experience, including adding buttons, running actions, and sending results back to the site
• The ultimate goal is to help users have the exact experience and workflow they want, with a focus on code execution, workflow management, and arbitrary code execution
• Pay tiers for compute resources
• Potential for paid upgrades for larger compute cycles
• Opportunities for GitHub to expand its features
• Separate layer for GitHub Actions