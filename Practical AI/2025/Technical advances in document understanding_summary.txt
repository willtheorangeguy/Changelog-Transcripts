• Introduction to the Practical AI Podcast and its goal to make AI technology accessible
• Discussion on building and shipping AI products at scale and the complexity involved
• Introducing Shopify as a commerce platform for businesses, including features like templates and AI-powered tools
• Personal stories and gratitude from Daniel Whitenack and Chris Benson for listeners and the show's progress
• Topic discussion: Document processing and its importance in industry, particularly with the rise of generative AI
• Document processing workflows in businesses
• Importance of document processing models in modeling and productivity
• Overview of different types of document processing models: OCR, LVMs, document structure models, and DeepSeek OCR
• History of OCR technology and its evolution with advancements in AI
• Current state of OCR technology and its increased effectiveness
• Processing pipeline for OCR (Optical Character Recognition)
• Comparison with Language Models (LLMs) processing pipeline
• Input: image vs text; output: probabilities of characters or tokens
• OCR model architecture: pre-processing, region detection, and character prediction using convolutional neural networks or LSTMs
• Historical context: evolution from recurrent neural networks to transformers and current approaches
• Discussion of convolutional and Transformer architectures in machine learning
• Introduction to Fabi, a collaborative analytics platform for exploring data
• Critique of the "old way" of data exploration, including wrestling with multiple tools and legacy BI systems
• Overview of Fabi's all-in-one environment for data exploration and analysis
• Comparison of OCR models with other architectures for document structure and layout recognition
• Discussion of document structure models, specifically Dockling and its family of models
• Document structure models predict document structure without text extraction
• They identify layout primitives such as rectangles and shapes
• A layout model classifies regions as titles, paragraphs, headings, tables, etc.
• Output is a structured representation in JSON, Markdown, or HTML format
• Often used in combination with OCR models to overcome limitations of raw OCR
• Can be computationally heavy and may require GPU to run
• Use cases: complex documents, two-column papers, whitepapers, data sheets
• Structure preservation in documents is crucial for certain applications
• Dockling models can handle complex document structures and preserve structure better than OCR models
• These models are still widely used, despite being computationally expensive
• They are useful for processing documents that will be fed into RAG systems (retrieval augmented generation pipelines)
• Preserving the structure of documents in RAG systems leads to better results
• Dockling or similar document structure models are a good way to do document processing for input to RAG pipelines
• These models can be used to represent documents in a structured format, such as Markdown, without needing to render them into a different format.
• Discussing language vision models that take image and text input to generate text output
• Describing how language vision models are created by combining large language models with vision transformers
• Explaining the process of fusing text and image embeddings to generate output tokens
• Comparing language vision models to OCR and docking systems in terms of interpretability and functionality
• Speculating on future developments and next steps for language vision models
• DeepSeq's OCR model uses a different processing pipeline that splits images into smaller tokens to preserve resolution and context.
• Current vision language models assume a fixed image resolution, which can lead to loss of information in documents.
• DeepSeq's approach allows for a compact token sequence representation without resolution limitations.
• The model preserves shapes of characters, line breaks, alignments, and tiny mathematical equations or notation.
• Resolution refers to the number of pixels in an image, with most vision language models resizing images to 256x256 pixels, losing contextual information.
• DeepSeq's approach tiles images at original resolution while maintaining global page context.
• The model is larger than previous ones and requires GPUs to run, but may lead to improved performance in future iterations.
• Discussion on the diversity and innovation in multimodal models, particularly in document processing
• Comparison of RAG (Reactive Attentional Graph) systems with large language models
• Explanation of different approaches to multimodal models and their development timeline
• Use cases for upgrading RAG systems in organizations
• Closing remarks, including a mention of Thanksgiving and future episodes