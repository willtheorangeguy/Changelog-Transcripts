• Sponsorships and acknowledgments
• DigitalOcean's new dedicated virtual CPU droplets
• Practical AI podcast introduction and welcome to the show
• Guest introduction: Victor Debia, research engineer at Cloudera Fast Forward Labs
• Victor Debia's background and career path leading up to his work at Cloudera
• Early interests in human aspects of computer science
• PhD in information systems with focus on quantitative user behavior studies
• Internship at IBM Research where exposure to AI began
• Transition from applying models to implementing custom-built models in TensorFlow and Keras
• Career progression as postdoc, research scientist, and joining Cloudera Fast Forward Labs
• Work in human-computer interaction (HCI) and AI, focusing on user experience and accessibility
• Two main lines of work: 1) using AI to make user interaction easier, and 2) making AI more accessible to non-experts
• Concept of "democratizing AI" and its goals and challenges
• Examples of projects in this field, including Data2Vs and TJBot
• Machine learning in the browser is a relatively new area with healthy skepticism
• Two main aspects of machine learning: training and inference
• Training involves creating a model that learns mappings between input data and target, typically done on back-end languages like Python or Java
• Inference involves using trained models to perform tasks at test time
• Browser limitations (single-threaded, sandbox environment) make it challenging for ML in the browser, but also offer benefits
• Three benefits of doing machine learning in the browser: privacy, ease of distribution, and interactivity and latency
• JavaScript ecosystem overview, specifically focusing on TensorFlow.js as a tool for enabling machine learning in JavaScript
• TensorFlow.js allows building, training, and performing inference both in the browser and Node.js environments
• TensorFlow.js is a library for building machine learning models using JavaScript in the browser or on the back-end with Node.js
• It allows developers to design, build, train, and perform inference on machine learning models using JavaScript
• TensorFlow.js has three main approaches: online workflow, where training occurs directly in the browser; offline workflow, where models are trained remotely and then deployed locally; and hybrid workflow, where models are trained initially offline but then fine-tuned online
• The online workflow is suitable for small models with limited data and allows inference to occur without leaving the client device
• TensorFlow.js allows for various model training and deployment scenarios
• Three potential flows: online, offline, and hybrid (combining both)
• Online flow involves training models on user data in the browser without sending it to a backend server
• Offline flow trains models using large datasets and hardware, then converts them for use in JavaScript applications
• Hybrid flow allows fine-tuning of pre-trained models using user data in the browser
• TensorFlow.js offers a converter tool for converting pre-trained models from TensorFlow.python into web format for use in JavaScript applications
• Performance limitations of training large models in the browser
• Importance of model optimization and export for deployment in the browser
• Typical use cases for TensorFlow.js, including small models trained offline and deployed for inference in the browser
• Real-world examples of using TensorFlow.js, such as Airbnb's user onboarding process
• Constraints of training and deploying high-performance models in the browser
• Uploading sensitive data (e.g. driver's licenses) to a server without storing it
• Providing users with control over their own sensitive data, rather than companies holding onto it
• Designing interactive experiences in the browser using camera input
• Using object detection models like HandTrack.js for real-time tracking of human hands
• Browser-based AI models
• Security concerns with browser-based AI
• Ability to download and use model files offline
• Developers' responsibility for securing models
• Users' potential misuse of models
• Companies' hesitation to port models to browsers due to security risks
• Discussion about AI in web browsers and its potential to change how users interact with web apps
• Mention of HandTrack JS, a model for hand tracking and gesture recognition
• Expectation that AI will enable new types of interactions beyond mouse and keyboard control
• Researcher's view on the opportunity for more natural user experiences through speech, voice, computer vision, and pointing gestures
• Challenges related to the size and optimization of AI models, with current limitations in terms of data storage and transfer
• Compressing models with little loss of accuracy for production and web applications
• Connection between compressing models and federated learning
• TensorFlow.js role in implementing federated learning on a global scale
• Federated learning concept, including client-side model training and sending updates to the server
• Experimental implementation of federated learning model in TensorFlow.js GitHub repository
• Discussion on the rise of gestures and richer interactions in user interfaces
• Comparison of Apple's 4ML and Google's ML Kit for device capabilities
• Use of TensorFlow.js to leverage device processing capability
• Explanation of TensorFlow Lite, its purpose, and relationship with TensorFlow.js
• Model optimization and compression techniques for resource-constrained environments
• Transferability of research from TensorFlow Lite to TensorFlow.js
• Introduction to JavaScript basics for non-experts and getting hands-on experience with TensorFlow.js
• Resources and tutorials for learning TensorFlow.js
• Overview of TensorFlow.js APIs: low-level linear algebra API and layers API (similar to Keras)
• Recommendation to start with the layers API tutorials for beginners
• Ability to convert existing models from other formats (e.g. Keras) using the TensorFlow.js converter
• Importance of refreshing JavaScript knowledge before diving into TensorFlow.js
• Experimenting with layers in a neural network
• Using pre-trained models for image detection and inference
• CovNet Playground, a tool for experimenting with convolutional neural networks
• Semantic image search, using images as input and finding similar images based on content
• Pre-trained models for feature extraction, including Inception, VG16, VG19, EfficientNet, NASNet, and MNASNet
• Decisions that need to be made by a data scientist when implementing semantic image search, including selecting a model and similarity metrics.
• Creating an environment to explore and compare the performance of different model architectures
• Visualizations for comparing feature embedding spaces and model performances
• Comparing the efficiency of models with varying numbers of parameters (e.g., VGG16 vs EfficientNet B2)
• Exploring data type-specific performances in ComNet Playground
• Introduction to TensorFlow.js and related projects
• Announcement of various communities where listeners can reach out for conversation
• Sponsors: Fastly, Rollbar, Linode
• Hosts: Daniel Whitenack and Chris Benson
• Music: Breakmaster Cylinder
• Show information: changelog.com for more shows and weekly email updates
• Closing: Thanks for tuning in, see you next week