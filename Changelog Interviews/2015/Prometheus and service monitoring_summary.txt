• Julius Volz from SoundCloud joins the show to discuss Prometheus, an open-source service monitoring system written in Go.
• Prometheus was created as a solution for SoundCloud's need for a robust monitoring system after leaving Google, where they had access to a comprehensive infrastructure.
• The initial motivation for Prometheus was to fill a gap in the open-source world for infrastructure tools, as SoundCloud felt "naked" without the extensive tools they had at Google.
• Julius and another ex-Googler, Matt Proud, worked together to develop Prometheus, starting with client libraries for instrumenting services with metrics.
• The conversation will delve into the data model, query language, and other features of Prometheus.
• The speaker and a colleague started building Prometheus in their free time in 2012.
• The project eventually became SoundCloud's standard monitoring system and time series database.
• The speaker discusses the movie Prometheus (2012) and its coincidence with the project's name.
• SoundCloud was migrating from a monolithic web application to a set of microservices in 2012.
• The company was using an in-house cluster scheduler called Bazooka, which predated Docker and Kubernetes.
• SoundCloud's monitoring system at the time was using StatsD and Graphite, but it had performance issues.
• Counting data in 10-second intervals
• Scalability issues with StatsD and Graphite combination
• Limitations of Graphite's inherent data model
• Difficulty in querying and analyzing metrics with multiple dimensions
• Challenges in identifying specific hosts or services instances
• Encoding instance and port information in metric names
• Comparison of monitoring definitions and tools (Nagios, service monitoring)
• Discussion of limitations of Nagios, including its data model and UI
• Introduction of Isinga as a drop-in replacement for Nagios with a better UI and scalable mechanism for executing checks
• Comparison of Ganglia with Nagios for host monitoring
• Explanation of the goals and motivation behind developing Prometheus, including the desire to replace existing tools and create a new, more integrated ecosystem
• Description of the features and capabilities of Prometheus, including its ability to collect and store numeric time series data, and its query language
• Discussion of the development of Prometheus at SoundCloud, including the process of introducing the project to the company and overcoming initial resistance.
• Development of a project to improve monitoring and dashboarding
• Ecosystem components were missing and no dashboarding solution existed initially
• Project was improved over time and became more mature and stable
• Killer use case was the instrumentation of containers on the Bazooka or in-house Heroku system
• This use case convinced people that the project was worth it and led to a strategic bet to switch to it
• Project was open-sourced in January 2015, and the goal was to keep it independent from any single company
• Initially, only a few people knew about the project, but it gained traction after open-sourcing and communication efforts
• StatsD was still running, but Prometheus was used for new services and had become the primary monitoring solution
• The community had grown rapidly, with contributions from various companies, including Google and CoreOS
• Prometheus was being adopted by various companies for their internal monitoring, including DigitalOcean
• Prometheus is a data monitoring system originally developed by SoundCloud, now maintained by some of its former employees
• It is designed to replace legacy systems, with a focus on architecture, data model, query language, and other details
• TopTile is a network of freelance software developers, where the company and developers consider themselves as one team
• The company was founded by two co-founders who met while freelancing as software developers
• Prometheus uses a "pull" architecture, where the server retrieves data from targets rather than data being sent to it
• The system has client libraries for exposing metrics, such as countermetrics, gauges, histograms, and summaries, to the Prometheus server
• Prometheus stores metrics locally in local storage, which is currently a file-based storage.
• The goal is to have single server nodes that are independent of the network, allowing for easier debugging during outages.
• Prometheus has experimental support for writing to OpenTSDB and InfluxDB, but not reading from them.
• Local storage is not meant for long-term storage and is intended for a couple of weeks or months.
• The design of Prometheus is intentionally simple to ensure reliability.
• High availability can be achieved by running two identical Prometheus servers.
• Prometheus can collect data from instrumented jobs, but also has exporters for non-instrumented systems, such as Linux hosts and HA proxy.
• Exporters transform native metrics into Prometheus metrics and expose them on an HTTP endpoint.
• The push gateway is used to track short-lived jobs or batch jobs.
• Prometheus can be used to scrape metrics from the push gateway.
• After data is collected and stored, it can be visualized through Promdash, Grafana, or dynamic HTML templates.
• Prometheus also supports alerting, allowing users to use the same powerful query language to formulate alert conditions.
• Alert management system explained, including central place for alert routing and management
• Prometheus server and alert manager roles clarified
• Visualization side of Prometheus discussed, including built-in graphing and prom dash
• Difference between built-in graphing and prom dash explained
• Alert management and configuration discussed, including role of built-in UI and prom dash
• Query language and data model explained, including how they work together
• Time series data model in Prometheus described, including use of labels and dimensions
• Memory limits in Prometheus and how to calculate headroom
• Multidimensional aspect of Prometheus labels and their use in querying
• Vector-based matching algebra in Prometheus
• Best practices for using Prometheus labels, including avoiding high cardinality
• Common mistakes in using Prometheus labels and their consequences
• Prometheus data model and how it handles labels and metrics
• Use of Prometheus for metric and label naming, and console and dashboard building
• Importance of careful label management to avoid creating too many time series
• Discussion of DigitalOcean services and a free month promotion
• Review of push vs pull in Prometheus and monitoring
• Explanation of the benefits of pull over push in certain environments
• Advantages of pull, including ease of manual access to targets and reduced data transfer costs
• Scalability aspects of pull and the potential for increased data transfer costs
• Comparison of the data transfer methods in StatsD and Prometheus
• The use of UDP packets for counter metrics can be prohibitive for high-traffic services, and can lead to lost data if packets are lost
• Prometheus model of tracking counter increments on the service side ensures that data is not lost even if a scrape fails
• Exposing rates instead of counters can lead to missed peaks in rates if a scrape is missed
• Prometheus supports other types of metrics besides counters, including gauges
• The getting started guide for Prometheus is accessible through the Prometheus.io website and provides a "Hello World" style guide for setting up a Prometheus server
• Prometheus is easy to get started with due to its simplicity and ease of deployment, thanks to its Go-based architecture and pre-built binaries
• To get started with Prometheus, one needs to create a configuration file and point to it, after which Prometheus will start scraping data and storing it in a local directory
• Getting started with Prometheus, including setting up a running server and scraping example services
• Example services to get started with, including Prometheus instrumenting itself and the Node Exporter
• Community resources for getting started and asking questions, including Twitter handle, mailing list, and IRC channel
• Contributing to Prometheus, particularly in the area of front-end development
• Requesting help from the open-source community, specifically seeking front-end developers interested in infrastructure projects
• PromDash and Prometheus front-end development
• Refactoring and improving Prometheus UI
• Alert manager redesign and implementation
• Long-term storage integration
• Contributing to Prometheus GitHub projects
• Julius' programming heroes: Bjorn, John Carmack, Rob Pike, and Dimitri Vyokov
• Prometheus internship and community contributions
• Upcoming database shows
• August 14th recording mention
• Unknown opponent for an upcoming show
• Teasing out next show details
• Signing off and farewell messages