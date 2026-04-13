• Sponsorships and advertisements for various companies
• Introduction to the Practical AI podcast and its hosts
• Guest introduction: Anais Dodis-Georgiou from Influx Data
• Anais' background in chemical engineering and transition into data science
• Conversation about a specific project or role that involved automation
• Transitioning from biotech to a developer-focused role
• Role as a developer advocate and its responsibilities
• Misconceptions about data scientist roles and the need for clearer communication
• Importance of connecting companies with communities through developer advocacy
• Career path, including taking a data science boot camp and transitioning into developer advocacy
• Time series data is any data with a timestamp attached to it
• Examples of time series data include stock prices, weather/temperature data, and industrial IoT monitoring
• Time series data is present in almost every industry, including healthcare and DevOps monitoring
• The value of time series data lies in its ability to help prevent risks and damage to processes and people
• Influx has customers using the platform for a variety of use cases, including monitoring farm growth, solar panels, and particle accelerators at CERN
• Time series data exists everywhere due to its presence in all industries that have sensors or need to monitor environments
• The speaker personally finds working with time series data valuable due to its universal application
• Large Hadron Collider and Higgs boson discovery
• Explanation of subatomic particles and the Higgs boson's role in particle physics
• Discussion of the term "God particle" and its origin
• Standard model of particle physics and the importance of finding the Higgs boson
• Time series data analysis and application to various types of data, including images and text
• Use of LSTMs (long short-term memory networks) for image classification and analysis
• InfluxDB is a time series database that stores and ingests large volumes of data with high write speeds
• Time series data typically has timestamp and value (e.g., stock price) pairs
• Queries on time series data can include filtering, aggregation (e.g., average), and analytics (e.g., Chande Momentum Oscillator)
• InfluxDB supports two query languages: Flux for 2.0 versions and InfluxQL for 1.x versions, with Flux being more readable and JavaScript-like
• Time series analysis and its purpose
• Buckets of analysis: forecasting, anomaly detection, and statistical elements
• InfluxDB and its built-in tools for time series data
• Automatic provision of tools for various functions by Influx
• Choosing the right forecasting method based on statistical assumptions
• Understanding underlying assumptions for classical forecasting methods and neural nets
• Time series analysis and its complexities
• Identifying a real problem to solve in time series data
• Choosing suitable tools for analysis, such as scikit-learn
• Understanding data attributes like lag, auto-correlation, and correlation between datasets
• Determining whether the problem requires univariate or multivariate analysis
• Using statistical methods versus machine learning/AI methods for certain problems
• Time series data with InfluxDB
• Neural network training and deployment process
• Online vs offline machine learning (streaming data vs batch processing)
• Statistical methods vs machine learning and neural nets
• H2O.ai and BigQuery integration with InfluxDB
• Training neural networks for changing data
• Univariate time series data is best handled with statistical methods.
• Multivariate time series data and forecasts are often better suited for machine learning, specifically neural nets.
• Statistical methods outperform machine learning in univariate time series forecasting according to benchmark studies like Makudaki's comps (MCOMPs).
• A hybrid method of RNN and exponential smoothing outperformed other models in recent benchmark results.
• While statistical methods may not be as effective for multivariate data, the cost-benefit analysis should determine whether extra effort is worth it for more complex forecasting methods.
• The speaker discusses how certain types of neural networks (RNNs and LSTMs) assume that data doesn't exhibit autocorrelation
• Autocorrelation occurs when a portion of time series data is correlated with another portion from an earlier time
• This assumption can lead to overfitting in models, especially in time series data with predictable patterns
• The speaker notes that multivariate data may be less prone to overfitting due to increased complexity and difficulty in fitting the model to specific trends
• Comparing the complexity of processing time series data
• Relationship between sequence-to-sequence models and time series analysis
• Similarities and differences between working with multiple time series versus a single one
• Data preparation and types of models used (RNNs, LSTMs)
• Getting started with InfluxDB: free tier, cloud offering, testing on local machine
• Installing InfluxDB as a single binary
• Telegraph platform and its uses
• Collection agent plugins for data collection
• Input plugins for various sources (sensors, databases, CSV, JSON, Jenkins, MQTT)
• Open-source community around InfluxDB
• Separation of developer and user communities for InfluxDB
• Overlap between database administrators (DBA) and Influx users
• Ease of use for non-technical individuals using Influx
• Time series data and its potential applications in personal projects
• Example use cases: monitoring a vegetable garden or home systems
• Conversation sparks ideas for new projects, such as gardening monitoring
• Practical application of AI and machine learning concepts at home
• Conversation wrap-up
• Request to rate and favorite podcast on iTunes
• Encouragement to share the show with others on social media
• Sponsorships from Fastly, Rollbar, and Linode
• Hosts: Daniel Whitenack and Chris Benson
• Music by Breakmaster Cylinder