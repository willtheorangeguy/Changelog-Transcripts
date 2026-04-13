• IVR systems and flowcharts
• Advances in language understanding for more flexible interactions
• Linode cloud servers hosting ChangeLog.com
• Open cloud and vendor lock-in
• Practical AI podcast and community
• Impact of coronavirus on work and education
• Catherine Breslin's background in speech technology
• Research into speech and language technology began around 2010
• The industry grew rapidly with companies building products and services
• The speaker left research to work on products at Amazon and learned about Alexa
• Cobalt was founded by Jeff Adams, a former Amazon employee, to help businesses build speech and language technology
• Virtual assistants contain multiple technologies working together for understanding user requests and taking action
• Speech recognition is the first step in processing user requests from audio to text
• Language understanding technology then determines what actions to take based on the request
• Various entities can be involved in a request, such as specific artists or locations
• The system consists of speech recognition, language understanding, and text-to-speech technology
• The language understanding technology identifies what the user wants to do (e.g. listen to music, get weather forecast) and with whom (e.g. specific artist)
• The system must pick out relevant information from the user's request, such as artists, city, or album
• Design choices are important in building virtual assistants, including how much effort to put on the user and keeping conversations short
• Systems can choose between randomly playing music or asking for further clarification from the user
• Intent recognition and bucketing user requests into different categories
• Identifying entities or concepts within intents (e.g. artist name, album name, city)
• Managing dialogue state and tracking user information across conversation turns
• Limitations in natural language understanding technology affecting conversation dynamics
• Current limitations of systems due to long conversations and inflexibility
• Conversation types and limitations of intent-and-slot models
• Difficulty in tracking conversation history and context over time
• Challenges in understanding ambiguous language and references to previous conversations
• Introduction to AI Classroom online training event by Daniel Whitenack
• Overview of speech technology applications beyond virtual assistants
• Speech recognition technology for transcribing long audio streams
• Automated subtitling for video content accessibility
• Speech recognition has utility in both assistants and other places
• Automatically generated transcripts help search for specific parts of a video
• Speech recognition can monitor conversations for legal reasons, such as financial advice
• Manual transcription is tedious and time-consuming
• A typical speech recognition system breaks down into three parts: lexicon, acoustic model, and language model
• The lexicon maps words to their pronunciations
• The acoustic model models the acoustics of sound and speech, predicting which phonemes are likely to be spoken
• The language model predicts sequences of words based on the input
• Acoustic model predicts sounds likely to be spoken in audio
• Lexicon combines sounds into words
• Language model combines words into sequences of words
• Models can be decomposed into acoustic, language, and lexicon components
• Commercial speech recognition systems typically use these three parts
• Lexicons are often handcrafted by phoneticians
• Acoustic and language models are statistical machine learning models
• They are trained on different types of data (audio and text)
• Recent advancements in deep learning have improved acoustic model performance
• Shift from Gaussian mixture models to neural network acoustic models has significantly improved speech recognition system performance over the past decade.
• Accent affects every aspect of the speech recognition system, including the lexicon, language model, and acoustic model.
• Different accents require separate lexicons and potentially different language models.
• Training an acoustic model with a specific accent in mind can improve its accuracy for that particular accent.
• Variations in speech, including accents and noise conditions
• Impact of different microphones and distances on audio data
• Role of acoustic models in processing audio data
• How accents affect not just sounds but also phrasing and word order
• Use of neural networks in audio data processing
• Encoding audio data into neural network models
• Differences between encoding text, images, and audio data
• Preprocessing audio input to extract frequency distribution
• Performing Fourier transform on small segments of audio
• Using a filter bank with triangular filters spaced according to human hearing sensitivity
• Passing the frequency spectrum through the filter bank to get coefficients for neural networks
• Mention of an ebook and podcast discussing career development in data science
• State of speech recognition technology for high-resource languages
• Current challenges in the field and expected improvements
• Comparison between high- and low-resource language speech recognition
• Availability of data, benchmarks, and knowledge in English language research
• Different dimensions of difficulty in speech recognition
• Noise as a factor affecting speech recognition performance
• Style and context of speech (e.g. formal vs informal, reading text)
• Speaker's position and movement (e.g. standing up to address people)
• Tone and emphasis used by speakers in different situations
• Challenges in transcribing people reading passages aloud
• Difficulty with heavily accented English and specific language domains
• Performance degradation when trying to use general speech recognition models for specific tasks
• Advantages of building high-resource languages into general-purpose speech recognition systems
• Challenges of adapting these systems to work in specific noise types and tasks
• Specific types of condition
• Difficulty in high resource languages with limited data
• Speech recognition systems customized to different domains and scenarios
• Challenges in multiple speaker scenarios or noisy environments
• Additional processing steps for speaker segmentation or identification
• Integrating these steps into existing speech recognition processes
• Identifying speakers in different ways
• Using a single microphone or microphone array
• Microphone placement and number of microphones
• Calculating sound travel time to locate voice sources
• Comparing two-microphone vs. multiple-microphone systems
• Separating speakers in a room using microphone arrays
• Limitations of microphone arrays in certain situations (e.g. online conferencing)
• Using voice characteristics to identify and separate speakers
• Diarization: identifying who is speaking when in a conversation
• Field-specific terminology and jargon
• End-to-end approaches for speech recognition
• Single neural network model that can perform entire process without separate language or acoustic models
• Advantages of streamlined process and ease of comprehension
• Google's research in this area
• Challenges with end-to-end methods, including need for large amounts of data
• The benefits of separating speech recognition models into acoustic and language components
• Difficulty in collecting large amounts of audio data for model adaptation
• Comparison to the acceleration of natural language processing (NLP) in recent years
• Concerns about a similar acceleration in speech and AI technologies
• Limited availability of speech data compared to text data on the internet
• Availability of more data vs methodologies in speech recognition
• Shared tasks and datasets within the speech recognition community
• Comparison between image classification (e.g., ImageNet) and speech recognition
• Difficulty in transcribing audio compared to text data
• Importance of large amounts of unlabeled data for building models
• Need for larger annotated datasets in speech recognition
• Transfer learning in speech recognition
• Using English acoustic models for new languages
• Amount of data required for transfer learning (100 hours to 1000 hours)
• Automated annotation and its contribution to large datasets
• Semi-supervised learning using automatically transcribed data
• Gains from automatic transcription vs. fully annotated data
• Excitement about future developments in speech technology
• Building and scaling speech technology for new languages
• Accessibility of voice interfaces for people with disabilities
• Potential applications in virtual assistants and technology access for underserved populations
• Development of voice technology for people with medical conditions affecting speech
• Future plans to widen access to this technology for a broader range of people
• Introduction to the podcast episode
• Hosts: Chris Benson and Daniel Whitenack
• Producer: Jared Santo
• Sponsors: Fastly, Linode, and Robar
• Advertising opportunities for sponsors
• Contact information for sponsoring the show (changelog.com/sponsor)