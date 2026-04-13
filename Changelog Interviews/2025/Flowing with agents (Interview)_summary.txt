• Amp is a coding agent that uses AI to modify code based on natural language instructions
• Amp is multi-model, using multiple LLMs, and doesn't require users to select specific models
• Cody is an older coding agent that is still used in the enterprise for non-agentic workflows
• Gen AI phenomenon has led to a shift in technology, requiring a new approach for agentic models like Amp
• The future of coding agents is seen as a force multiplier, but still requires delicate handling and understanding of their capabilities and limitations.
• Model intelligence and limitations
• User frustration and expectations vs. model capabilities
• Drift in model performance and degradation in quality
• Code review as a bottleneck in using AI tools
• Strategies to address model quality issues, such as switching inference providers and using multiple model families
• Recent report of quantized model rollout and impact on model quality
• Importance of user intuition and skills in effectively using AI tools
• Specific example of Claude Code losing functionality and requiring user input to correct it.
• Amp operates similarly to other agents, using a for loop wrapping an agentic LLM
• The loop takes user input, feeds it into the model, and generates a response, including tool calls
• Tool calls are executed, and responses are fed back into the loop until complete
• Sub-agents are specialized tools that perform targeted tasks within the agent
• The client-server architecture allows for server-bound models and syncing of agentic interactions (threads) to the server
• Threads are like transcripts of interactions, including user questions, tool calls, and results
• The server-side store enables team-wide views of how others are using the tool and sharing of best practices
• Amp can be installed via npm and has a CLI architecture inspired by NeoFetch
• Discussion of command line tools and the challenge of making them visually appealing
• Introduction of a new terminal UI framework built in-house for Amp
• Elimination of flicker in the terminal UI and special shout-out to Tim Culverhouse
• Importance of history and context in coding conversations
• User experience and interactions with coding agents, including the concept of "Agent Flow" and "Document-Driven Development"
• Standardization of context and behavior for coding agents through the use of agents.md files
• Personal approaches to coding and user experience, including the use of roles and prompts to guide agent behavior
• Development process for a project enhancement proposal (PEP) system to formalize project ideas and decisions
• Importance of clear direction and guidance for a project, and how to provide it using a PEP system
• Distinction between two types of development workflows: one where a clear plan is generated, and another where the workflow is more exploratory and iterative
• Use of PEPs to document project ideas, decisions, and learnings, and to facilitate team collaboration and knowledge sharing
• Borrowing of Python's PEP system and status tracking to organize and manage PEPs
• Importance of having a structured process for documenting and reviewing project ideas and decisions.
• The speaker, Adam Stacoviak, discusses his use case for Amp, a tool that allows him to work on long-running tasks while multitasking
• He mentions his agent flow, which involves using a model to generate code and logs, and storing them in a repository
• The logs serve as an audit trail, providing context for reviewing code and understanding the high-level intention behind it
• Adam Stacoviak describes the logs as containing the "what and why", with the builder logs capturing the journey of the developer during implementation
• He also mentions the knowledge base, which contains institutional knowledge and is used to store long-term knowledge
• The conversation touches on the benefits of using Amp, including increased productivity and the ability to work asynchronously
• Adam Stacoviak and Beyang Liu discuss the potential of Amp to be used in a pull request workflow, providing an audit trail of the plan that generated the code
• They also mention the tool's built-in notification sound, which has become Pavlovian for Adam Stacoviak, signaling that it's time to check on the status of a task.
• Amp is a coding agent used by the team, with around 80-90% of code generated using it
• Iterations on prompts, tool definitions, and sub-agent combinations have improved Amp's performance
• Adam Stacoviak created a product manager role using Amp and had it review output from other agents, including Claude Code
• Beyang Liu explains the pricing model and the trade-off between cost and quality
• Cheaper pricing may lead to model quality degradation and a perverse incentive to nerf models
• Time saved and additional value created by using Amp are considered more important than cost
• Adam Stacoviak's perspective on using coding agents as a skill to be learned and flexed
• Importance of context and clarity in relationships, including with machines like Amp
• Discussion of leveraging Amp for specific tasks and workflows
• The importance of efficient token usage with Amp
• The difference in behavior patterns between senior engineers and non-technical users
• Recommendations for efficient token usage, including creating targeted and short threads
• The use of Amp to improve a Bash script for archiving and compressing media files
• The development of a new tool, 7zarch, for advanced archiving and compression
• The user is concerned about using Amp efficiently and is worried about the context window collapsing and forgetting context.
• Beyang Liu explains that the user's approach is not uncommon and that the company is still learning about how to use Amp effectively.
• Beyang Liu mentions that the context window limit was previously around 200k, but now it's much higher and the quality has improved beyond 70k.
• He suggests that the user should start fresh for each task and not accumulate too much context, as it can lead to confusion and degradation in performance.
• The user agrees that they were using Amp inefficiently and that the company's approach is more intuitive and better suited to professional engineers.
• Beyang Liu mentions the tension between being prescriptive and allowing users to use Amp in their own way, and suggests that the company will provide more visual indicators and best practices in the future.
• The user suggests that the company should not change the way Amp works, but rather add a slash command for users who want to read documentation and use an alternate version.
• The context window and how to leverage threads is a black box for some developers
• The context window is analogous to the human brain's working memory and has limitations
• Overloading the context window can lead to latency, degraded quality, and confusion
• MCP servers can inject irrelevant tool definitions, adding to the context window and causing issues
• Using roles and props can be more efficient and reduce token costs
• Threads can be composed like functions, allowing for more efficient agent flow
• Analogies between human brain function and agent flow can help developers understand the context window and threads
• The conversation turns to discussing the inception of Amp and the process of raising an agent.
• Design constraints of AI models in the application
• Building a spike to experiment with new technology
• Discovering new workflows and capabilities of AI agents
• Importance of thinking from first principles and relearning assumptions
• Sharing learnings and insights with the user community through the podcast
• Discussing the podcast's format and reach
• Advice on publishing and promoting content on YouTube
• Encouraging the hosts to maintain the fun and whimsical tone of their podcast
• Praising the work of Thorsten, a Sourcegraph employee, on the podcast and as a writer
• Discussing the growth and progress of Sourcegraph and its mission to help developers
• Describing the hosts' passion for building developer tools and their desire to continually improve and innovate
• Sharing personal anecdotes and experiences with the hosts and Sourcegraph's journey
• Discussing the intersection of technology and human experience, and the joy of coding and software development
• The contrast between the beauty of nature and the monotony of coding
• The development of AI and its potential to capture human-like intelligence and reasoning
• The concept of a "universal pattern matcher" and its ability to fit any observable pattern
• The hype and skepticism surrounding AI, with some viewing it as a solution to all problems or a threat to human existence
• The potential for AI to be a useful tool, rather than a replacement for humans
• The need to approach AI with a nuanced perspective, recognizing its limitations and capabilities.
• Pattern recognition and automation in technology
• Mindset for approaching new technologies: exploration and curiosity vs. skepticism and criticism
• Benefits of using coding agents for building tools and applications outside one's expertise
• Open source software and its potential future with the rise of coding agents
• Impact of coding agents on the use and development of libraries and APIs
• Discussion of using Amp's agentic coding tools without needing to choose a specific model
• Importance of sampling multiple coding agents to find the best fit
• Future plans for experimenting with new models and reducing latency in Amp
• Upcoming release of Amp on September 17th
• Discussion of making the Raising Agents podcast more frequent and production-level