• The hosts discuss the podcast and recommend other shows
• Kurt Mackey explains how he pitches Fly.io to developers
• He discusses the limitations of platforms like Heroku and Vercel
• Fly.io is introduced as a no-limits platform for developers
• Daniel Whitenack introduces a new topic: real-time speech assistance advancements
• Qtai is a non-profit lab launched in Paris with funding from three donors: Xavier Niel, Rodolfo Saadeh, and Eric Schmidt.
• The lab aims to conduct open-source research independent of major labs and to bring innovation to the AI field.
• France has a strong engineering culture and mathematics emphasis that attracted big American players like Facebook.
• The French ecosystem is diversifying with more startups and research institutions emerging.
• A unique aspect of the French system is allowing PhD students to work in private companies or non-profits, gaining access to resources like GPUs.
• Qtai was formed as a response to the desire for independence from large American companies and to allow French researchers to lead their own projects.
• Open science and democratization of AI/AGI through open source and transparency
• Importance of explaining research methods, mistakes, and decisions made during the research process
• Releasing code and training pipelines for touch models as part of open sourcing efforts
• Comparison between nonprofit and commercial labs in terms of resources, agility, and decision-making processes
• Nonprofit's focus on core deep learning and avoiding competition with large text-based LLMs
• Distinct advantages of nonprofits, including agility, ability to release commercially friendly licenses, and focus on on-device models
• Race to the top in benchmarks for AI performance
• Importance of on-device models and potential applications
• Discussion of Postgres database capabilities, extensibility, and scalability for AI
• Timescale's work with Postgres, including PG Vector Scale extension for large-scale AI apps
• Enabling developers to build AI apps using expertise they already have through PGAI extension
• Moshi: a speech-based foundation model integrating text as modality for real-time dialogue
• Qtai lab's research direction on Moshi for fluid conversation and low latency
• The speaker describes their team's work on a framework for speech-to-speech models and their goal of combining text knowledge with top-of-the-line audio modeling techniques.
• The team had an edge in this area due to their expertise in audio modeling and the lack of research in this field at the time.
• They worked on MIMI, a highly compressed representation at 12.5 hertz, to get close to text-like representations.
• The team then moved on to modeling speech and handling full duplex interactions.
• The speaker discusses the history of research in speech-to-speech models, noting that pre-GPT models were rule-based and less successful than deep learning models.
• They attribute the success of recent models like GPT and chatGPT to their ability to perfectly understand human requests and bring this capability to the audio domain.
• Audio processing as a wave oscillating at high frequencies requires special representation to be understood by transformer models.
• Early successes in audio modeling include WaveNet and Jukebox, but they had significant computational requirements.
• The technology has progressed with advancements from Nel Zegidur and the development of discrete representations at low sample rates.
• Challenges remain in feeding large amounts of audio data into transformers due to autoregressive steps and context constraints.
• Recent innovations include using RQ transformers to model dependencies between tokens, reducing autoregressive steps, and handling multiple audio streams for real-time processing.
• The full duplex aspect allows for two separate audio streams: one for the user and one for Moshi.
• The model is trained to generate users' replies during pre-training, but in released models, it only tries to model its own stream.
• Discussion of chatbot capabilities and limitations
• Exploring the use of APIs for open-source development
• Mention of training data and personality traits in AI assistants
• Versatility of multi-stream approaches to text-to-speech, speech-to-text, and automatic speech recognition
• Applications of this approach in generating long scripts and synthetic data
• Plans to release code for fine-tuning and adaptability
• Introduction to WorkOS and its AuthKit product
• Explanation of AuthKit's features and benefits in authentication
• Discussion of WorkOS and AuthKit
• Benefits of using WorkOS, including ease of use and free plan for up to 1 million users
• Data preparation for training a conversational AI model
• Challenges in preparing data, including:
	+ Needing both text and audio pre-training datasets
	+ Difficulty in obtaining high-quality audio recordings with clearly separated speakers
	+ Needing specific instruct data sets that are geared towards oral interactions
• Bootstrapping process to train a TTS (text-to-speech) model and fine-tuning the model for oral style
• Challenges with training a model for multimodal interactions (audio and text)
• The size of the model, specifically its 7 billion parameters
• The trade-off between model complexity and efficiency
• Distillation techniques and their impact on model efficiency
• Future plans to reduce model size and increase usability
• Excitement about advancements in optimization and architecture beyond Transformers
• Framework evolution and concerns with abstraction leakage
• Competition to apply current models versus exploring new architectures
• Future of coding, potentially achieving perfect code with minimal effort
• Potential changes in the next few years, but specifics not discussed
• Inspiration and collaboration in open models, open source, and open science spaces
• Upcoming episodes or future discussions
• Promotion of ChangeLog newsletter and its benefits