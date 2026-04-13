• Funding open source projects through donations
• History of Python and Django development
• Origin of the name "Django" (from Django Reinhardt, a gypsy jazz guitarist)
• Different pronunciations of "Django" (e.g. "The Djungo", "The Django")
• Andrew Godwin's personal history and start in programming (PalmPilot, BASIC, web development, PHP, and Django)
• Andrew Godwin's first open source project, ByteHoard
• Meeting Simon Willison, co-creator of Django, and switching to Django from PHP
• Andrew Godwin's introduction to Python through Django and his subsequent becoming a core developer
• The development of South, a Django migrations framework, and its eventual integration into Django 1.7
• Andrew's experience at the first DjangoCon and how it contributed to the popularity of South
• Andrew's transition from PHP to Python, citing limitations of PHP and the ease of use of Python
• Andrew's thoughts on why people choose Python, including its ease of use, documentation, and community
• The role of significant whitespace, documentation, and testing in making Python appealing
• The importance of community and resources, such as Sphinx and Read the Docs, in contributing to Python's popularity
• The importance of documentation in software development, with a focus on writing documentation first to inform API design and user experience.
• The benefits of writing documentation as a way to solidify understanding and ensure a clear user experience.
• The distinction between reference documentation and overarching guides, such as getting started guides and tutorials.
• The role of documentation in facilitating transitions between different versions of a project.
• The challenges faced by open source maintainers in maintaining a broad perspective and understanding the needs of users across different versions.
• Django's flagship feature is its admin interface, which allows for rapid development and data entry
• Django has a built-in ORM, migrations, and query framework
• Other notable features include a GIS framework, forms framework, templating language, and views and URL routing framework
• Django has extensive documentation, including tutorials and reference documentation
• Django has a strong focus on security, with built-in features like CSRF protection and middleware
• Django's components are optional and can be easily removed or replaced
• The GIS framework is pluggable and supports multiple backends, including PostGIS
• Django has a large and diverse community, with notable users including Instagram, Eventbrite, and government agencies
• Django is a widely used framework with thousands of users, including large companies such as Pinterest, Spotify, and Mozilla.
• The framework's flexibility and ability to work behind the scenes make it difficult to identify which sites use Django.
• Django prioritizes stability and predictability, with a focus on building reliable and scalable applications.
• The framework's age and maturity contribute to its stability and wide adoption.
• Django Channels, a feature being developed by Andrew Godwin, is seen as a key area of innovation and excitement in the Django community.
• Development of websockets and its stabilization around 3-4 years ago
• Websockets as a protocol for bidirectional communication between browser and server
• Advantages of websockets over HTTP for certain types of applications
• Challenges of implementing websockets in Python and Django
• Need for a general protocol framework in Django to handle multiple protocols
• Development of Channels to create a framework for the future of the web
• HTTP/2 and its changes in communication paradigm
• Importance of real-time communication and protocol support for the future of the web
• Andrew Godwin introduces his project "Channels", an asynchronous library for Django
• Channels allows for long polling, websockets, and HTTP/2 support
• Andrew discusses the challenges of implementing websockets and HTTP/2, and how Channels addresses these issues
• Jerod Santo asks about the typical way of running Django in production, and Andrew explains that it depends on the setup, but Channels can be used as a separate server that accepts multiple types of connections
• Jerod asks about implementing HTTP/2 at a proxy layer, and Andrew explains that while it's possible, native support in the framework is often required for advanced features like server push
• Jerod asks about the relationship between server push and websockets, and Andrew clarifies that server push is a way to push resources to the browser, not a replacement for bidirectional communication.
• Django Channels is a part of the Django project, but was developed as a separate application due to concerns about its design and maturity.
• Channels provides an abstraction layer for real-time communication, allowing developers to switch between different implementations (e.g. WebSockets, server-sent events).
• The project is designed to enable asynchronous systems across a network, and is based on a distributed communication and queuing system.
• Channels is more ambitious in its scope than other channel implementations, as it aims to solve the problem of asynchronous I/O in Python.
• The project has the potential to enable intercompatibility across languages with a general protocol for message parsing.
• Channels is not suitable for every project, and developers should consider whether real-time communication is necessary for their needs.
• The project's design is influenced by the language CSP (Communicating Sequential Processes), which is used for concurrent programming.
• Andrew Godwin has experience with long-term projects and sustainably funding open source projects, having successfully funded the development of Django features through Kickstarter.
• Funding open source projects with a specific feature or goal in mind
• Mozilla's Open Source Support grant system (MOSS) and its use in funding Django features
• Formalizing a process for funding and managing open source projects
• The Django Software Foundation's role in handling money and payouts
• The need for sustainable funding models to maintain open source software
• The use of crowdfunding platforms like Kickstarter for funding specific projects
• The importance of appealing to both businesses and individuals in funding open source projects
• The need for clear communication and a well-defined business model to secure funding
• Andrew Godwin discusses his experience with open source projects and how having a strong reputation and existing codebase can influence funding.
• He expresses concern about the privilege of having free time to work on open source projects and the need for more sustainable solutions.
• Andrew praises the Python community for its friendliness, help, and outreach, and advises open source project leaders to prioritize community building.
• He recommends the podcast Request For Commits for its discussion of open source business and sustainability.
• Andrew provides resources for learning about Channels and Django.