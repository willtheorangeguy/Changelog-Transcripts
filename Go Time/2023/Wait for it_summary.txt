• Project overview: biopharma-based healthcare solution using distributed microservices and containerized image processing
• Image processing at the edge, solving complex problems with IoT devices and developing Go microservices
• Solution architecture: OEM device, gateway, and machine learning pipelines running on Linux Ubuntu
• Choice of programming language: Go chosen for its simplicity, reliability, popularity in distributed microservices, and built-in concurrency and scalability features
• Intel's involvement and use of Go as the go-to language at the time
• Containerized microservices architecture chosen due to its lightweight and scalability benefits
• Microservices architecture allows for loosely-coupled services that can be added or removed without affecting the overall solution
• Wait For It package used to coordinate service dependencies in a production environment
• Two main options for implementing Wait For It: Docker layer (using vishnubob Bash script) or Go application code layer
• Go Wait For It package chosen due to its homogenous solution and minimal code changes required
• Importance of testing and checking the safety of using such a package before deployment
• Evaluating open source packages and their licenses
• Choosing between Wait For It and net-wait-go packages
• Modifying existing code to make it usable in a project (copy-pasting and modifying)
• Adding error handling and retry logic for unavailable services
• Interacting with core authors/maintainers of the package
• Contributing back to the repo and opening a pull request
• Challenges with open source packages: difficulty in finding replacements for deprecated projects
• Importance of being agile and adaptable when working with open source software
• Trade-offs between using open source packages versus developing solutions in-house
• Considerations for team expertise, customer requirements, and development time
• Learning curve for developers who are not familiar with a particular programming language (in this case, Go)
• Using multiple programming languages for different applications and being open-minded about language choice
• Choosing Go for microservices development due to its suitability
• Importance of open-source community and contributing to it (Intel's perspective)
• Project goals, timelines, and support plans for a specific project
• "Unpopular opinions" discussion, with Sam proposing Christmas spirit year-round
• Discussion of implementing Go wrapping in project
• Importance of prioritizing Christmas spirit with a warm and cuddly tone
• Unpopular opinion on software development: spending too much time testing and not enough time designing and coding
• Focus on gracious failure instead of trying to prevent all edge cases
• Need for shifting priorities in software development