• Importance of good release engineering for core infrastructure
• Jean-Sébastien Padron's experience as a contributor to RabbitMQ and FreeBSD
• Challenges of debugging complex systems with multiple software versions
• The role of communication in release engineering, especially for open-source projects
• Benefits of good release engineering, including improved user satisfaction and feedback
• Importance of making money in open-source projects
• Challenges and risks associated with release engineering for RabbitMQ
• Definition and characteristics of core infrastructure components (RabbitMQ as an example)
• Comparison between RabbitMQ and FreePSD (operating system) regarding release engineering
• Examples of failed release engineering efforts (RabbitMQ security bug fix/ break-in change, FreeBSD 5.0 release cycle)
• Trade-offs between shipping a new version quickly vs. taking time to stabilize the code base
• Importance of timely software releases and updates
• Impact on user confidence and willingness to consume future changes
• Relationship between release engineering and user happiness
• Comparison of RabbitMQ and FreeBSD as core infrastructure
• Considerations for companies using these systems (e.g. cars, gaming, streaming)
• Real-life example of a customer issue with RabbitMQ in Paris
• RabbitMQ is involved in message exchange between car and key
• Importance of core infrastructure, such as RabbitMQ, being transparent but often overlooked
• Teleport Access Plane for unified access to computing resources
• Release engineering process for FreePST, including fixed interval between major releases and minor releases
• Use of a calendar tool for release planning, including code freeze, beta releases, and final release dates
• Importance of communication and flexibility in the release process
• The FreeBSD release engineering process was introduced after FreeBSD 5 and has undergone changes to adjust the timeframe between releases for easier user understanding.
• The FreeBSD calendar is published on the FreeBSD.org website and announced on mailing lists, providing a clear schedule of upcoming releases.
• The development process takes place in an internal Git repository hosted by FreeBSD, with read-only mirrors available on GitHub; there are discussions about introducing alternative tools like GitLab.
• The community can communicate with developers through various mailing lists focused on specific topics or branches.
• Users can participate in FreeBSD development by finding tasks on the Bugzilla bug tracker or solving problems they encounter while using FreeBSD.
• Submissions for patches can be made through pull requests on GitHub, mailing lists, or Bugzilla after opening an issue.
• Release cycle and timeline for FreeBSD
• Differences in versioning between FreeBSD and other operating systems
• Principles of Least Astonishment (POLA) in FreeBSD release engineering
• Importance of compatibility and deprecation in major releases
• Timeline for major and minor releases in FreeBSD
• Comparison to RabbitMQ's current release engineering process
• Inspiration from other open-source projects, including Darktable and Mesa library
• Distributed team meetings and challenges with graphics drivers
• Discussion of FreeBSD and its stability in comparison to other systems
• Importance of balancing shipping updates quickly with ensuring software stability
• Challenges of testing graphics drivers on various hardware configurations
• Shift from including graphics drivers in the core FreeBSD source code to packaging them separately
• Software development process involving testing, feedback, and updates
• Importance of communication with contributors and users in release engineering
• Limiting the impact of mistakes and being honest about them
• AirLong (Yoz) web server used for a previous project
• Hot code reloading feature of AirLong
• Packaging Debian packages for the service
• RabbitMQ software development process, lack of hot code reloading
• RabbitMQ code changes can be problematic if not handled correctly
• Migration from state V1 to V2 requires careful handling
• Clustered systems make this process even more complicated
• Packaging AirLong VM with configuration management tools is challenging
• RabbitMQ's plugin system and microservices architecture contribute to complexity
• Containerization has helped simplify packaging and deployment
• Kubernetes cluster operators can help manage complex deployments
• Kubernetes' challenges with stateful distributed systems
• Limitations of RabbitMQ in containers and Kubernetes environments
• Hot code reloading feature not available in RabbitMQ, but potentially achievable through bug-fix only patch releases
• Benefits of hot code reloading for users and developers
• Open discussion on release engineering practices and user experience
• Goodbyes spoken multiple times 
• Timing and duration of goodbyes vary 
• No other conversation or topics discussed