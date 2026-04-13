• Introduction to the Practical AI Podcast
• Complexity of building and shipping AI products at scale
• Shopify as a commerce platform for AI-powered applications
• Guest introduction: Donato Capitella, principal security consultant at ReverseSec
• Update on Donato's company and work in Gen AI cybersecurity
• Discussion of recent conferences and research in Gen AI security
• Current AI use cases in enterprises are primarily agentic workflows for tasks like customer support
• Enterprises are building their own agentic frameworks using custom loops, prompts, and parsing
• External tools and APIs are being used to expand the capabilities of Large Language Models (LLMs)
• Agentic workflows introduce new security concerns, such as tool exposure and vulnerability to prompt injection attacks
• Authorization and access control have become a major focus for securing agentic workflows
• Enterprises need to ensure deterministic, non-LLM-based ways to determine function calls in specific contexts
• Customer service systems involving LLMs (Large Language Models) are becoming increasingly complex due to interconnected tools and data sources.
• The complexity of these systems is reminiscent of the microservices architecture issue, where alert systems would malfunction due to interconnectedness.
• With LLMs, there's an explosion of data sources being fed into a single prompt, including untrusted parties and potential malicious data.
• This can lead to security vulnerabilities, such as prompt injection, allowing attackers to manipulate the model and create phishing attacks.
• The mixing of untrusted sources in the same LLM context is a hard problem to solve.
• Developing an all-in-one environment for data exploration
• Building advanced analysis capabilities with Python and AI assistance
• Creating interactive data apps and dashboards from ad hoc analysis
• Preventing security breaches by focusing on prevention rather than incident response
• Examples of vulnerabilities in LLM applications, including the "eco-leak" attack on Co-Pilot
• Design pattern considerations for securing data and preventing breaches
• Balancing security with user productivity and functionality
• Balancing governance and chaos in cybersecurity
• Challenges of working with companies that are extremely risk-averse
• Differences between companies that are heavily locked down and those that are more relaxed
• Impact of Generative AI on penetration testing and security assessments
• Changes in metrics, activities, and approaches to dealing with prompt injection and other exploits
• Effort required to jailbreak a Large Language Model (LLM)
• Comparing prompt injection to SQL injection and password guessing attacks
• Guardrails and active response to prevent jailbreaking attempts
• Protecting against jailbreaking attacks in the real world
• Detection feedback loop vs. protection mechanism
• User experience considerations for prompt injection detection
• Research paper on design patterns to secure LLM agents against prompt injection
• Action selector pattern for secure use cases
• Code then execute design pattern (CAMO) by Google
• Reference monitor and data flow analysis for security
• Agency open-source collective building the Internet of Agents
• Inhibiting LLM from using prompt injection to write executable code
• Solving LLM agent security outside the LLM, not an alignment problem
• Discussion of LLM (Large Language Model) feedback loops and the need for stronger controls
• System design problem vs model design problem in addressing potential issues with LLMs
• Introduction to the Spiky package/framework/project and its purpose
• Challenges in pen testing LLM applications, including manual effort and limitations of existing tooling
• Needs for practical, customizable, and isolated testing solutions for LLM applications
• Requirements for a data set generation tool, including flexibility, extensibility, and modularity
• Spiky module uses a headless browser to interact with chatbots
• Development of custom modules for pen testing using Spiky
• Need for flexibility in creating data sets and instructions for specific client needs
• Standard built-in tools and custom modules used in engagements
• Customization process for adapting to new applications and attack techniques
• Evolution of security and AI merging, future industry trends and expectations
• The speaker expresses a desire to have more free time at the end of the day.
• They ponder the future of the industry and wish they knew where it's headed.
• The speaker discusses the need for a shift in cybersecurity mindset from LLM red teaming to secure design patterns.
• They highlight the risks associated with unsecured LLM applications and tools, potentially leading to real-world breaches.
• The speaker expresses hope that someone will figure out prompt injection and jailbreaking solutions for LLMs.
• The conversation wraps up with a thank you and an invitation for the guest to return.