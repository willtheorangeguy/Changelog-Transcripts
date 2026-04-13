• Introduction and sponsor announcements
• Topic announcement: Practical AI podcast discussing computer vision with guest Chris DeBellis
• Guest introduction: Chris DeBellis, expert in robotic perception and computer vision
• Definition of robotic perception: understanding environment through sensors for robot interpretation
• Examples of robots that use robotic perception: manufacturing, self-driving cars, service robots (e.g. Roomba)
• Role of deep learning in robotic perception: impact on traditional methods like canny edge detection and hough lines transforms
• AlexNet was a pioneering algorithm in deep learning for object classification, and subsequent algorithms have built upon it.
• The trend in computer vision is shifting from traditional approaches to deep learning.
• Object detection and identification are two distinct parts of the task, with deep learning able to handle both simultaneously.
• Convolutional Neural Networks (CNNs) can detect multiple objects within a scene, identify their locations, and even segment pixels to assign them to specific objects.
• The acronym "mask our CNN" refers to a type of algorithm that uses CNNs to segment images into distinct regions or masks.
• Traditional feed forward neural networks are introduced as the foundation for explaining how CNNs work.
• Convolutional Neural Networks (CNNs) use spatial filters, or kernels, to process image data while maintaining pixel relationships.
• Relationship between pixels in images matters for image processing
• Convolutions used in most image-based models, including object detection and classification
• Size of convolutional kernel, combinations of sizes, and values within kernels differ among models
• Limitations of traditional convolutional neural networks (CNN) in robot perception use case
• Mask R-CNN addresses limitations by defining exact location of pixels within an object
• Feature extraction is a crucial step in image processing, where basic features are built up into more complex patterns
• Feature detection in object recognition involves identifying features such as straight lines, curved lines, and specific patterns
• Building from finer feature representations to more complex ones to improve accuracy
• Limitations of bounding box-based object detection (e.g., not considering orientation or rotation)
• Mascar CNN provides a solution by generating masks that fill in the pixels where an object is located
• Applications of mask-based object detection include robotic perception, such as grasping objects with varying orientations
• Comparison of different CNN architectures for object detection (e.g., YOLO, Mask R-CNN) and their respective strengths and limitations
• Difficulty in labeling objects within images, particularly for masks and precise object boundaries
• Challenges of annotating complex shapes and occluded objects
• COCO data set and its use as a foundation for transfer learning and mask annotation
• Time-consuming process of manually annotating images with multiple objects
• Need for efficient methods to annotate large datasets, including potential uses of crowdsource annotation
• Annotation of images at scale
• Limitations of manual annotation with pizza parties or small groups
• Convolutional neural networks (CNN) and region proposal
• Mask RCNN algorithm: mask generation, X and Y coordinates for object pixels
• Benefits and trade-offs of using mask RCNN vs bounding boxes
• Computationally expensive, especially on smaller devices like robots
• Training difficulties due to need for annotated images
• Consideration of inference time for tasks like real-time video processing with Mask RCNN
• Limited GPU power on robotics platforms can slow down inference
• Need for a powerful GPU to run deep learning networks like Mask RCNN efficiently
• Importance of understanding the computational requirements of deep learning networks
• Prerequisites for working with deep learning algorithms: coding skills, particularly in Python
• Ability to code and make changes to code is more important than advanced math and statistics knowledge
• Availability of online resources such as YouTube videos, Stanford courses, and Udacity courses for learning deep learning
• Passion and perseverance are key to success
• Batch normalization can be complex but understanding its purpose is important
• The Matterport mask RCNN repo on GitHub is a valuable resource for learning about the algorithm
• The repo includes Jupyter notebooks, an active community, and clear documentation
• The main files in the repo include model.py, utilities.py, visualizations.py, and config.py
• Getting started with the repo can be done by following the demo Python notebook or reading through the issue posts.
• Contacting the hosts: Daniel and Chris on social media
• Participating in Practical AI LinkedIn group
• Joining online community with Slack at changelog.com/community
• Reaching out to Chris DeBellis on LinkedIn
• Providing feedback and ratings for the show
• Sponsorships: Fastly, Rollbar, Linode cloud servers