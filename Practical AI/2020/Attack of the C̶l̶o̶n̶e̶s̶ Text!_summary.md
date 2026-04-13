• Bandwidth for Changelog is provided by Fastly and Rollbar helps them fix things quickly
• The podcast Practical AI covers artificial intelligence, machine learning, and data science
• Daniel Whitenack and Chris Benson co-host the podcast, discussing various topics in AI
• A listener named Jack Morris joins the conversation, a researcher at University of Virginia and incoming Google AI resident
• Jack shares his background, studying computer science and math at UVA and interning at Google through their FUBAR program
• The speaker was in their second year at UVA when they encountered an Easter egg on Google that led to a terminal window with coding challenges.
• The challenges were similar to those found on platforms like LeetCode and HackerRank, but the speaker had a hard time solving one particular problem involving rabbits and rabbit holes.
• The speaker's experience with this challenge did not lead to immediate job opportunities, but they later applied for Google's AI Residency program and got an internship through it.
• They are now participating in a research internship at Google as part of a 1.5-year fellowship and plan to pursue a PhD in computer science or artificial intelligence.
• The speaker initially became interested in AI through its applications on the application side, particularly natural language processing (NLP), but later became more interested in the underlying technologies.
• Encoding sentences into vectors for comparison
• Limitations and problems in NLP models
• Adversarial examples in NLP
• Behavioral testing of NLP models
• Biased training data affecting model performance
• Adversarial attacks on computer vision models
• Convolutional neural networks and image classification
• Adversarial examples in text analysis
• Adversarial examples in NLP context
• Definition and types of adversarial examples
• Importance of robustness vs safety in NLP models
• Use cases for exploring adversary examples (e.g. toxic comment classifiers)
• Introduction to ChangeDog++ membership program
• Generating adversarial examples to retrain NLP models
• Defining adversarial examples in NLP, including semantics and character level changes
• Methods for generating adversarial examples, including hand-curation and automated techniques
• Challenges of detecting imperceptible changes in text sequences
• Importance of model robustness and potential solutions
• Discussing the challenges and limitations of testing NLP models for robustness against adversarial examples
• Introducing the concept of adding an output to identify malformed or unnatural inputs
• Comparing NLP model testing with unit testing in software engineering
• Exploring potential use cases for identifying and preventing unexpected behavior in NLP models
• Discussing the possibility of integrating such capabilities into text editors, word processors, or other tools
• Open source project for generating adversarial examples in NLP
• Problem with current approaches: reuse of similar ideas and code, difficulty in reimplementing results and comparing things
• Counterfeited word embeddings: a pre-processing step for Glove vectors to make them more suitable for thesaurus-based tasks
• Many papers use counterfeited word embeddings to generate adversarial examples
• Generating adversarial examples is a combinatorial search problem that many people solve in similar ways
• Idea of breaking down the process into components to construct attacks from different papers
• Overview of the library "text attack" and its goals for a beginner
• Project scope: tackling NLP attacks from 1936 to 1941
• Library limitations: what not to address with this library
• System overview: components of the text attack system
• Common use cases: embeddings, sentence encodings, and clustering
• Components:
  • Transformation (changing words or characters)
  • Constraint (ensuring changes are acceptable)
  • Goal function (defining success criteria)
  • Search method (deciding which transformations to keep)
• Developing greedy or approximate heuristics for searching adversarial examples
• Data augmentation in NLP, including using transformations to preserve semantics
• Integrating data augmentation with other components of the library
• Open-source library development, including contributions from others
• Potential users of the library: general users, researchers studying model robustness, and those testing/improving models using text attack
• Discussion about TextAttack and its potential to aid research in robustness of models
• GitHub repo for TextAttack is well-organized and easy to use
• Plans for future contributions to the attack recipe section
• Comparison to other libraries in vision, such as Cleverhans and Foolbox
• Goal of making tools like TextAttack easier to use to advance the field
• Transition into new position as AI resident and thoughts on future of AI
• Importance of creating systems with basic knowledge and understanding of language
• Conversation wrap-up and appreciation
• Future episode mention
• Sponsor acknowledgments
• Call for listener requests
• Show production credits
• Episode teaser and outro