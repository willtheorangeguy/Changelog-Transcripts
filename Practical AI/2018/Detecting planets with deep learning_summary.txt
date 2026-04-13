• Sponsor mentions: Fastly, Rollbar, Linode, Hired
• Introduction to Practical AI podcast and its community
• Guest introductions:
  • Andrew Vandenberg (postdoctoral fellow at University of Texas at Austin)
    - Research background in exoplanets
  • Chris Shalhoub (software engineer at Google)
    - Background in mathematics and biomechanical engineering, now working on astronomy project
• The speaker discusses their background and interest in science
• They pitched an idea to collaborate with Andrew on a project involving data from NASA's Kepler mission
• The Kepler mission was launched in 2009 to study exoplanets and determine how common planets like Earth are
• The main goal of the mission is to detect small planets orbiting stars similar to our Sun at distances where liquid water can exist
• Exoplanets are defined as planets that orbit a star other than our Sun
• Kepler uses a giant digital camera to take pictures of 200,000 stars every 30 minutes
• The data collected by Kepler involves measuring the brightness of stars over time to detect subtle changes caused by exoplanet transits
• Brightness of stars measured at regular intervals
• Data munging and tracking star positions in images
• Feature selection for machine learning model to classify dimming signals as planets or not
• Methods for identifying stars and distinguishing between planet and non-planet causes of dimming
• Kepler mission data and classification of dimming signals by astronomers before using machine learning
• Machine learning approach to classifying dimming signals in star brightness over time
• Machine learning approach using light curve data from exoplanet dimming events
• Treating light curves as one-dimensional images and applying convolutional neural networks (CNNs)
• Using CNNs to classify light curves into different categories
• Selecting the basic vanilla CNN architecture due to its simplicity and effectiveness
• Importance of starting with basic models and adding complexity as needed
• Recommendations for working in a new domain or data set, including:
  • Understanding basic neural network architectures (e.g. CNNs, RNNs)
  • Knowing strengths and weaknesses of different architectures and their applications
• Reception of neural networks in the astronomy community
• Challenges with limited training data (only 30,000 examples)
• Use of data augmentation to increase training examples
• Models trained on standard desktop computers, no need for specialized hardware
• Plans to scale up to more training data and use GPUs or TPUs
• Discussion of accessing datasets on Google Cloud
• Discovery of two exoplanets and their characteristics
• Model's ability to find planets missed by previous searches
• One of the exoplanets, Kepler-90i, is a record-breaker with 8 planets around its star
• Challenges in distinguishing between dips in light curves caused by different planets
• Reasoning behind open-sourcing the model
• Potential for others to build on and apply similar techniques
• Availability of NASA data, including Kepler mission data
• Challenges in detecting small planets orbiting far from their stars
• Difficulty separating weak signals from false positives in signal detection
• Challenges in detecting exoplanets with Kepler and other space telescopes
• Importance of precise measurements to identify potential Earth-like planets
• Role of machine learning and neural networks in identifying signals previously missed
• Next steps: separating out false alarms and finding extremely exciting signals of Earth-like planets in long period orbits
• Long-term goal: using these findings to search for signs of life outside our solar system