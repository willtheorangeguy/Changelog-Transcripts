• Introducing WorkOS and its features for enterprise SSO
• When is it too early or late to be "enterprise ready"
• Free offerings of AuthKit for developers until 1 million users
• Monetization strategy for WorkOS, charging based on growth and scale
• Wide range of customers using WorkOS, from small startups to large enterprises
• Workflow orchestration and its importance
• Adam Azam's background in workflow orchestration
• How Prefect solved workflow orchestration issues for a previous startup
• Definition of workflow orchestration
• Features and benefits of using Prefect for workflow orchestration
• Pain points with workflow orchestration
• Difficulty transitioning from local to cloud environment
• Need for intuitive infrastructure interface
• Challenges with orchestrating large language models (LLMs)
• Failure cascades and difficulties in expressing contingencies in code
• Importance of treating failure as a first-class citizen in workflow design
• The speaker discusses the challenges of handling failure in workflow orchestration, particularly with machine learning (ML) and language model (LLM) workflows.
• Sources of failure include external services being flaky, deterministic errors from data ingestion or transformations, and changes to data formats or structures.
• ETL (extract, transform, load) type jobs are a persistent problem that exists in workflow orchestration, but ML/LLM workflows introduce new dynamism and uncertainty.
• The nature of errors has changed with LLMs, where parsing errors can occur due to the complexity of responses, making error handling more difficult.
• The speaker highlights the need for new approaches to handle data quality errors, which were not as prevalent in traditional ETL workflows.
• Tools for handling new difficulties in workflow orchestration
• Agentic workflows: dynamic systems that operate in loops and interact with external tools
• Challenges of managing agentic workflows, including resiliency and uncertainty
• Comparison to previous pain points in business development (e.g. Shopify vs manual sales)
• Introduction to Prefect Core: an open-source Python library for workflow orchestration
• Prefect features for building LLM workflows, including retries and caching
• Easy handling of complex dependencies between tasks in a workflow
• Caching output to avoid recalculating answers when possible
• Transactional logic for undoing changes if something fails
• Error handling and custom error handling options
• One-click deployment on various infrastructure platforms (e.g. Kubernetes, Amazon ECS)
• Observability features for tracking and understanding failures in workflows
• Observability and error handling in workflows
• Importance of breadcrumbs for debugging failed workflows
• Using Prefect to handle failures and retries
• Orchestration and switching between different services (e.g. OpenAI, Anthropic)
• Deployment element of Prefect: connecting local development to production environment
• Converting Python code to Prefect workflows and adding superpowers
• Running workflows locally and remotely with Prefect
• Scheduling and exposing HTTP endpoints for on-demand invocation
• Dynamic workflow invocation and manual triggering
• Scheduling vs dynamic workflow execution
• Auto-scaling and handling massive workloads
• Prefect's deployment experience and remote infrastructure support
• Prefect Cloud features, including UI, job tracking, and error summaries
• Workflow monitoring and failure analysis
• Notion AI simplifies workflows by providing personalized responses and integrating with various tools.
• Unlike generic chatbots, Notion AI has context of user's work and multiple knowledge sources (GPT-4 and Cloud).
• Notion AI can search across multiple platforms, including Slack discussions, Google Docs, Sheets, Slides, GitHub, and Jira.
• Prefect's Marvin is an LLM-powered Slack bot that serves a community of 30,000 data engineers with personalized help.
• Marvin has been integrated into Prefect's internal documentation and GitHub issues to provide users with personalized learning interfaces.
• The existing tools for writing LLM workflows were not ergonomic or natural
• The company created Prefect to simplify complex workflows and make them accessible to a broader audience
• Marvin is a Pythonic and ergonomic interface for building LLM workflows using decorators
• Agentic workflows are being used to build complex systems, but can be difficult to debug and manage
• The value of agentic workflows lies in their ability to create deterministic workflows that can easily be debugged and observed
• Differences between LLM workflows and agentic workflows
• The limitations of traditional debugging methods for agentic workflows
• Introducing Marvin as a prompting library and its purpose
• Control flow: expressing dependencies between tasks, ergonomics, and explicit control over LLMs
• Built on Prefect 3 with features like retries, timeouts, caching, and sandboxed code environments
• Distinguishing between LLM workflows and agentic workflows based on their characteristics
• Discussion of Prefect Core and Prefect Cloud as managed workflow orchestration platforms
• Focus on Control Flow and Marvin in relation to LLM workflows
• Concerns about the emphasis on single machine local LLM or agent workflows
• Need for structured outputs from providers like OpenAI to address resiliency issues
• Importance of planning and transactions in LLM workflows
• Potential for human interaction with locally running functions to become obsolete
• Future API development for LLM provisioning and infrastructure management
• Coordination problem across parallelized executions or calls against LLM APIs
• Discussion of orchestration and disaster planning in Prefect
• Adam's presentation on workflows and production
• Review of documents for Prefect, Marvin, and Control Flow
• Invitation to try out Prefect and its tools
• Closing comments and thanks to guests and listeners