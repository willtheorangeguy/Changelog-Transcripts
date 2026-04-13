• Combination of quality estimation systems with machine translation
• Quality Aware decoding project: integrating quality predictions into MTE process
• Bringing quality estimation to the MTE process to make MT more aware of its quality
• Role of quality estimation in deciding whether to post-edit or not
• Importance of evaluation technology, such as Comet
• Quality estimation and evaluation in machine translation
• Comet: a widely adopted metric for quality estimation
• OpenQE: an alternative to Comet that doesn't rely on reference translations
• Mbabel's quality controls for translations, including MQM (Multidimensional Quality Metric)
• Comparison of Comet to other metrics like Blue, highlighting its advantages and limitations
• The speaker describes the Blur algorithm, which compares translations to references by looking at individual words and their overlaps
• The speaker explains the brevity penalty in Blur, which penalizes short translations
• The speaker discusses TER (Translation Error Rate) and CHRF metrics, which are similar but differ from Blur
• The speaker describes Comet, a metric that uses large language models to compare word embeddings
• The speaker explains how Comet is trained on human labels for specific tasks, making it more suitable for machine translation evaluation than other metrics
• The speaker compares Comet to other metrics like BERT score, which do not use fine-tuning and can produce inaccurate results
• The speaker mentions a category of quality estimation that does not require a reference, similar to Comet but comparing directly to the source instead
• The distinction between quality estimation and metrics (such as BLUE, CHRF, Comet) in evaluating translations
• How quality estimation serves a different application than metrics, focusing on understanding differences between models or systems at a test set level
• The use of quality estimation for real-time decision-making, such as determining the trustworthiness of a translation
• The history and development of quality estimation, which is said to have seen more research and innovation than metrics
• The convergence of modeling approaches in both fields, eliminating the distinction between them
• Feature-based approaches to quality estimation models, including classical machine learning and deep learning
• Advancements in large protein models and embeddings leading to improved performance
• Challenges in translating words between languages due to one-to-one mapping issues
• Limitations of current quality estimation models, such as discriminative power and hallucinations
• Open problems in quality estimation, including next steps for improvement
• Critical errors in metrics estimation for specific phenomena
• Similarity between embedding spaces and difficulty in differentiation by neural networks
• Named entities and their impact on metric performance
• Challenge sets to test metrics for specific phenomena
• Metrics task share and challenge set subtask
• Analysis of scores and feedback for future work improvement
• Limited data for fine-tuning
• Name identity problem (e.g. translating "Apple" to fruit instead of company)
• Biases in evaluation metrics due to limited label data
• Need to alleviate the name identity problem
• Models fall short sometimes, especially in commercial or sensitive settings
• Larger models tend to have better predictive power, but may not always be beneficial
• Difficulty in training larger models due to increasing GPU costs
• Evaluation of model quality and efficiency, including the concept of "cometinho" (a smaller version of a comet model)
• Limitations of large models for deployment by non-tech companies
• Need to balance model performance with deployability and scalability
• Different architectures or techniques for making models smaller
• KNN MT (Key-Nearest Neighbor Machine Translation) as a method of dynamic adaptation
• Avoiding fine-tuning large pre-trained models by using data retrieval and interpolation
• Challenges of shrinking or compressing large models to make them more efficient
• Translation memories and data storage systems for machine translation
• Importance of localization industry for evaluating and improving machine translation
• Excitement about advancements in evaluation metrics and quality estimation systems
• Combination of quality estimation systems with machine translation processes
• Progress and future potential of combining quality estimation with machine translation
• Excitement about the "quality aware decoding" project for more accurate machine translations
• Human parity between machine translation (MT) systems/models and human translators was claimed a few years ago, but it turned out the used translators were not professional.
• MT models have improved fluency, but still struggle with translating very specific content that requires specialized terminology and expertise.
• Challenges in MT include accurately conveying nuances and context, even if the overall translation looks good.
• Unbabel is working on addressing these challenges through research and hiring more researchers to contribute to its projects.
• Unbabel has offices worldwide and accepts applications for various positions, including research scientists and engineers.
• Guests thanking the host
• Recap of the show's content and posters displayed
• Appreciation for listeners and sponsors (Fastly, fly.io, Breakmaster Cylinder)
• Request to subscribe and share the show with others via word of mouth
• Closing remarks and farewell