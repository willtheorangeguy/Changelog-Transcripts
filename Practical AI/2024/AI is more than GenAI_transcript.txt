[0.00 --> 25.00]  Welcome to Practical AI. If you work in artificial intelligence, aspire to, or are curious how
[25.00 --> 32.64]  AI-related tech is changing the world, this is the show for you. Thank you to our partners at Fly.io,
[32.98 --> 37.30]  the home of changelog.com. Learn more at Fly.io.
[47.92 --> 53.84]  Well, our friends over at SpeakEasy have the complete platform for API developer experience.
[53.84 --> 60.72]  They can generate SDKs, Terraform providers, API testing, docs, and more. And they just released
[60.72 --> 68.00]  a new version of their Python SDK generation that's optimized for anyone building an AI API.
[68.44 --> 76.24]  Every Python SDK comes with Pydantic models for requests and response objects, an HTTPX client for
[76.24 --> 81.80]  async and synchronous method calls, and support for server-sent events as well.
[81.80 --> 87.78]  SpeakEasy is everything you need to give your Python users an amazing experience integrating
[87.78 --> 96.66]  with your API. Learn more at SpeakEasy.com slash Python. Again, SpeakEasy.com slash Python.
[96.66 --> 115.08]  Welcome to another episode of Practical AI. This is Daniel Whitenack. I am the founder and CEO
[115.08 --> 124.08]  at PredictionGuard. And I would normally be recording with my co-host, Chris, but he has had to be out for
[124.08 --> 132.00]  for a couple weeks. And I was thinking during this time, I've been doing a bit of teaching at different
[132.00 --> 140.08]  conferences, and I've kind of honed in on a set of interesting learning materials that I thought would
[140.08 --> 145.96]  be a great thing to share here. We have these episodes normally called Fully Connected Episodes.
[145.96 --> 151.28]  And these are where Chris and I keep you kind of connected to everything that's happening in
[151.28 --> 158.76]  the AI news and trends, but also try to provide some learning resources. And what I found as I've
[158.76 --> 166.52]  gone to different conferences and given workshops is that sometimes there's a bit of confusion around
[166.52 --> 176.12]  two things. One is that AI equals generative AI. And that's, you know, not surprising because there's
[176.12 --> 181.96]  so much that we hear about generative AI, even on this podcast. We've, of course, talked about it
[181.96 --> 189.76]  a lot that there's this association that sort of anything AI is generative AI. But then there's another
[189.76 --> 199.62]  thing, another notion, which is this idea of not knowing kind of how generative AI came about, and it
[199.62 --> 206.14]  kind of popped out of nowhere, when in reality, there was a sort of progression towards generative AI,
[206.38 --> 212.90]  and it fits within a landscape of AI and machine learning and data science that has been going on
[212.90 --> 219.32]  for some time. So I thought it would be good in this particular Fully Connected episode, or this episode,
[219.32 --> 225.28]  where it's actually just me. So sorry to disappoint those out there that don't want to hear more of
[225.28 --> 233.08]  my voice, but it's just me today. And I'm gonna go through some of this kind of distilled set of
[233.08 --> 241.96]  learning resources that kind of set AI within the context of a wider set of methodologies and a history
[241.96 --> 249.60]  of development. And then also maybe help us understand the landscape of AI methodologies
[249.60 --> 256.30]  beyond generative AI, and how those things are still used quite a bit and might even be combined
[256.30 --> 261.84]  with generative AI in very interesting ways. So that's what we're going to embark on today is
[261.84 --> 269.14]  a little bit of a tour of AI machine learning history, setting generative AI in that history.
[269.14 --> 274.26]  And along the way, we'll talk about kind of the practical things and the knowledge that
[274.26 --> 279.28]  you might want to go out and research more if you're interested in any of these different kinds
[279.28 --> 286.52]  of techniques that are still used quite widely outside of generative AI. So let's go ahead and get
[286.52 --> 295.48]  going. There's kind of a first generation or first phase in my mind of what I think of with AI and
[295.48 --> 303.36]  machine learning. And that's kind of 2017 and prior. Or a lot of times what I think of since I've only
[303.36 --> 310.06]  been alive for a certain period of time, and been working professionally, I kind of think of this as
[310.06 --> 317.88]  the 2010 to 2017 period, that I would label kind of that data science, statistical machine learning
[317.88 --> 324.34]  period. This is the time when I first started getting into data science when I came out of academia.
[324.34 --> 332.50]  And this phase of data science machine learning is really focused on kind of small scale model
[332.50 --> 338.42]  building and models that were sometimes neural networks and sometimes they weren't neural networks.
[338.70 --> 346.54]  They might be gradient boosted machines or decision trees or other things like this. And during this
[346.54 --> 354.10]  phase of data science, AI machine learning development, the kind of primary role of those working
[354.10 --> 363.14]  in this field was to curate a set of example inputs and kind of known outputs. We talked about this a
[363.14 --> 367.74]  little bit in a previous episode when we talked about it's all about the data, but this would be
[367.74 --> 375.14]  training data where we have example inputs and known outputs. And then we also have a software function,
[375.38 --> 383.00]  which is parameterized. And what I mean by parameterized is think about what a software function does.
[383.00 --> 389.08]  A software function is a data transformation. I have inputs to that software function and I have outputs
[389.08 --> 395.56]  of that software function. And if you think about some software functions, they could be parameterized or
[395.56 --> 404.12]  they could have parameters. So let's take the example of object recognition, right? That the software function
[404.12 --> 412.52]  that executes that executes that data transformation of an image in and a set of labels out or maybe just a set of
[412.52 --> 419.58]  binary out. Is there a cat or is there not a cat in this image? That's a data transformation from an image to a label.
[420.00 --> 427.12]  And inside of that software function, we could think about a really dumb software function that could execute this.
[427.12 --> 435.36]  So for example, think about all of the pixel values of that image. I put that image in my software function.
[435.68 --> 444.30]  I could just calculate, you know, the percentage of red pixels in that image. And if that percentage is above a certain number,
[444.48 --> 451.12]  greater than or equal to, I could say it's a cat. And if it's less than I could say not cat. That's a really terrible
[451.12 --> 460.00]  function to do this data transformation, but it would operate in software, right? Now, me as a developer,
[460.00 --> 468.32]  I could choose an appropriate percentage for that parameter, the parameter that is the percentage of
[468.32 --> 474.94]  red pixels. And that might be an expert knowledge that I encode into the system, but I would hard code it.
[475.42 --> 480.98]  But maybe I don't know the exact value for that parameter. And so what am I to do?
[480.98 --> 489.06]  Well, I could, as a software engineer, as a developer engineer, I could actually execute in a separate process
[489.06 --> 495.56]  that's iterative and actually try all the parameters under the, you know, that are possible,
[495.56 --> 502.28]  all of the values for percentages that are possible. And because I have a set of example inputs and
[502.28 --> 509.12]  example outputs, I could try that set of parameters for all of my example inputs and outputs and just
[509.12 --> 515.38]  choose the one that gives me the best results. In other words, the most accurate results. And then
[515.38 --> 521.62]  I would set that as an ideal parameter, which was found or fitted or trained. And that's what's
[521.62 --> 529.20]  happening in a training process in this kind of 2010 to 2017 statistical machine learning, supervised
[529.20 --> 535.54]  learning way of going about things. Now I'm being a little bit general here. Obviously there's a whole
[535.54 --> 541.60]  variety of other methods that are maybe unsupervised methods. If you're curious about those, you could
[541.60 --> 548.16]  look at clustering. There's kind of semi-supervised methods and other things. You can look at those.
[548.54 --> 554.18]  And I'll talk about actually some of that here in a second. But generally that's how the process would
[554.18 --> 561.76]  go. I would choose a function that would be parameterized. I would put in a set of example inputs
[561.76 --> 568.78]  and known outputs to a training function that's iterative. And I would find the ideal set of those
[568.78 --> 575.40]  parameters. And then once I found the ideal set of those parameters, then I can use that ideal set
[575.40 --> 582.96]  of parameters in my function to process new inputs, which is called inference or prediction. Now that
[582.96 --> 588.68]  function, if you think about what is the model in this case, the quote unquote model, the machine
[588.68 --> 595.62]  learning, the statistical model here, the machine learning or statistical model here would be the
[595.62 --> 601.52]  combination of the software function and the set of parameters that are needed to execute that software
[601.52 --> 608.94]  function for inference or prediction. Those together in my mind form the model. You need both of them.
[609.28 --> 615.18]  And that's why people are maybe confused about how to license models, because some people might use
[615.18 --> 620.64]  licenses for code, some people might use licenses for data, and other people might make up their own
[620.64 --> 628.36]  because they don't know which one is right. So this is kind of that 2010 to 2017 era of data science
[628.36 --> 633.34]  machine learning. And this is still used widely. If you're curious about this, you might listen to the
[633.34 --> 641.86]  episode about broccoli AI, AI that's good for you. This was Bing Soon who created this sort of model,
[641.86 --> 650.58]  an NLP classification model for a real use case. And this fits a variety of use cases. So time series
[650.58 --> 657.34]  forecasting, right, where you have a time series, and then you're trying to predict future values, or you have
[657.34 --> 663.70]  images, like I said, and you're trying to predict labels, or you have text input, you're trying to classify that
[663.70 --> 670.94]  into spam or not spam. It's a whole variety of things around classification, which is that labeling,
[670.94 --> 678.08]  regression, which is a prediction of a continuous value, like a, like a score, something like that.
[678.80 --> 683.58]  And so there's, there's a lot of these methods, they're still used very widely. If you want to think
[683.58 --> 690.12]  practically about this, most of these models, especially the smaller scale ones might not even
[690.12 --> 699.04]  need a GPU to train them or to execute the inference, at least at many different scales. But as the model
[699.04 --> 705.48]  grows, of course, it's, it's harder to execute. And in particular, you know, during this phase, neural networks
[705.48 --> 711.74]  were trained and neural networks have been around for a while. And that's just a function that has a bunch of
[711.74 --> 719.72]  these sub functions in it, that take input, again, executing a data transformation. But the goal of this sort of
[719.72 --> 727.70]  neural network is to model more generally, a complicated relationship from input to output, without you sort of,
[727.70 --> 736.82]  from the start, you know, using a lot of your expert information to construct the architecture of that, of that particular
[736.82 --> 746.08]  function, it's more generalizable, maybe. So this is this first phase, again, keeping things practical in this phase,
[746.08 --> 752.08]  there is a practitioner that's oftentimes curating data working with domain experts,
[752.08 --> 759.44]  they might be using an ML ops platform, like a weights and biases, or maybe a larger platform, like a
[759.44 --> 765.56]  Databricks or something like that, to train models often, update them often, store them in a repository,
[766.60 --> 773.46]  monitor them. And so there's a lot of kind of iterative model training, model monitoring, all of those things,
[773.46 --> 787.18]  that still goes on quite a bit in an industry. So that gets us to around the era of or the year 2017. Now 2017, there's some
[787.18 --> 798.48]  interesting things that happen. And that has to do with foundation models, and transfer learning. So in that first phase
[798.48 --> 807.12]  that I talked about, most of what I was talking about was training a model from scratch. In other words, you have a
[807.12 --> 815.52]  software function with a set of parameters, those parameters need to be fit, you use a training process to train those. And
[815.52 --> 822.86]  oftentimes, you might start those parameters out in that training process, either in a random sort of way, or maybe
[822.86 --> 826.80]  according to a specific distribution, or maybe according to a specific distribution, but ultimately, you're kind of
[826.80 --> 834.32]  starting from scratch, you don't have a great place to start with those parameters. In this foundation model world or
[834.32 --> 842.78]  transfer learning, if you remember around 2017, I think Google released BERT around this time, and others released other
[842.78 --> 852.52]  models. And I think what people found was, if you're doing kind of these tasks generally with maybe text inputs or image
[852.52 --> 863.36]  inputs, like with a YOLO model, or, or text inputs, like with a BERT based model, a lot of these tasks were very
[863.36 --> 871.30]  similar one to another. So if you think about doing object recognition, maybe, you know, Google trains a model
[871.30 --> 880.84]  that recognizes 10 different classes in images and airplane and a car, and a dog and a cat and etc.
[880.84 --> 886.46]  And you maybe want to do something specific to your domain or your company, maybe you're an agriculture
[886.46 --> 893.80]  company, and you want to take pictures of bugs on plants and classify those to keep track of what
[893.80 --> 900.86]  bugs are in your field or something like that. Well, that's, that's a very similar task to the general
[900.86 --> 908.48]  object recognition task that this model was already trained on. And so the key piece or the kind of one of
[908.48 --> 915.56]  the key shifts that we saw during this period of foundation models and transfer learning was that
[915.56 --> 924.94]  a large player like Google or, you know, a big tech company or a set of academics actually, might train a
[924.94 --> 931.34]  very large scale model, meaning they might have millions of example inputs and outputs. And the model or the
[931.34 --> 938.90]  function itself might have millions of parameters, and they train on a huge amount of data, that model,
[939.46 --> 945.14]  and output an ideal set of parameters that's a really, really good starting point for anyone
[945.14 --> 952.92]  that wants to downstream, carry on the fine tuning or carry on the training of that in a process called
[952.92 --> 961.46]  fine tuning to produce their own domain specific model. Now, this fine tuning process that that we've
[961.46 --> 970.76]  been talking about, you would need very, a very small scale of data to train or continue the training
[970.76 --> 977.62]  or fine tune that model as compared to the original data set that trained the model from scratch. And if you
[977.62 --> 982.76]  want to kind of get some intuition about this, generally, if you think about the size of the model,
[982.76 --> 988.36]  like one with millions of parameters, or even tens of millions or hundreds of millions or billions of
[988.36 --> 994.92]  parameters, you need a lot of data to fit each of those billions of parameters, you can think if you
[994.92 --> 1001.26]  have billions of parameters and 10 data points, that's not very much data to train billions of
[1001.26 --> 1007.54]  parameters, maybe not enough to train even a linear regression model, you could do maybe a better job
[1007.54 --> 1015.92]  there. So you need a lot of data to train this larger model, which could then downstream be slightly
[1015.92 --> 1023.38]  adapted or slightly tweaked with a smaller set of data for your domain to produce a domain specific
[1023.38 --> 1031.70]  model or a model that's specific to your use case. But the mechanics of this are not dissimilar at runtime,
[1031.70 --> 1039.22]  you still have your new inputs come in to your adapted model, even though it's now a fine tune model,
[1039.22 --> 1044.50]  not a model you train from scratch, and you process those new inputs through the data transformation,
[1044.50 --> 1052.98]  the outputs, there is a very maybe a significant difference here practically, though, because these
[1052.98 --> 1060.42]  models are meant to be more general and be applied to many different use cases. Now, those models are much
[1060.42 --> 1067.14]  bigger, the software functions are much bigger. But more importantly, the number of parameters that go
[1067.14 --> 1075.38]  into those software functions is very large, maybe even gigabytes large or more. So when you execute that
[1075.38 --> 1082.74]  many operations on that sort of input, it's a lot of matrix multiplying, it's a lot of processing and data
[1082.74 --> 1089.78]  transformation. And so this is where we really start to be stressed by this capacity and need for
[1090.42 --> 1098.34]  GPUs or, or other specialized processors that would help us process these very many calculations very
[1098.34 --> 1105.30]  fast, because we want to recognize an image maybe in real time or close to real time, not waiting
[1105.30 --> 1112.74]  seconds or even minutes to process that image. And so practically, there's a need for a different kind of
[1112.74 --> 1120.18]  generation or set of hardware to run these larger models, which were kind of trained as larger
[1120.18 --> 1126.90]  models to handle a general set of use cases, and then followed on with transfer learning after that.
[1126.90 --> 1134.34]  And this is also still quite widely used. So data scientists and data analysts, or machine learning
[1134.34 --> 1142.58]  engineers, or whatever they are, still use these models and still use models like this or do things like this in
[1142.58 --> 1148.18]  practice fine tuning. You probably have heard of whether that's fine tuning a large language model or
[1148.18 --> 1154.58]  fine tuning a non generative type of model, which we'll talk about here in a second. This process of
[1154.58 --> 1161.78]  fine tuning is used very frequently because it requires you to maybe curate less specific training
[1161.78 --> 1169.06]  data. Now I want to go maybe over a couple of asides here that are important to note before we hop to the
[1169.06 --> 1176.10]  latest generation of models. And those couple of asides I think are subtle but important for kind of
[1176.10 --> 1184.66]  the general understanding of this flow and this flow of thought and where things fit into the major picture
[1184.66 --> 1193.22]  here. The first of these asides is let's think about maybe why this foundation model or transfer learning
[1193.22 --> 1203.86]  process actually works. Well as it turns out if you look at one of these models like a BERT model or one of
[1203.86 --> 1210.10]  these other models like an object recognition model, a lot of the processing of that software function,
[1210.74 --> 1218.42]  you can kind of think about it like a lot of the the heft of that function. Most all of those parameters
[1218.42 --> 1227.30]  and those functions and sub functions within within the model are really dedicated to what's called
[1227.30 --> 1234.26]  either feature representation or embedding or creating an internal representation, however you
[1234.26 --> 1243.30]  want to put it. It's about taking that data in whatever mode that's in, so an image or text or audio maybe,
[1243.30 --> 1250.90]  a set of vocabulary and taking that in and transforming that from its original format, maybe a set of pixel
[1250.90 --> 1259.94]  values or a set of vocab indices or something like that in the case of text and actually translating that
[1259.94 --> 1269.22]  input into a really efficient and dense and good representation that can be used for the downstream task.
[1269.22 --> 1279.78]  So if you think about kind of your model function as a big pipe, you know, 90% or more of the flow
[1279.78 --> 1285.86]  through that pipe through that data transformation is dedicated to the translation of whatever that input
[1285.86 --> 1292.02]  is in whatever format like an image or text into this internal representation sometimes called features
[1292.02 --> 1314.18]  or oftentimes called an embedding or a hidden a hidden representation. Then a very small amount, maybe 10% or less of that processing has to do with taking that representation and then performing a downstream task like machine translation or speech synthesis or object recognition.
[1314.18 --> 1331.14]  And so because a lot of that has to do with representing the input, that representation of the input for text or images or audio is then transferable between different text and image and audio tasks.
[1331.14 --> 1338.10]  Like I could have a model like that embeds or represents my text input.
[1338.10 --> 1359.62]  And then I could kind of bolt on various heads onto the front or onto the the end of that model or the end processing of that software function and do things, all sorts of things like machine translation or sentiment analysis or named entity recognition or NLI or different things.
[1359.62 --> 1367.78]  And so this is kind of one of the key pieces that makes this foundation model or transfer learning piece work so well.
[1368.26 --> 1388.38]  Now, the second aside that I would like to mention here is that one of the reasons why we were able to boost the model size and kind of boost the generalizability of this was because one, we kind of were able to understand
[1388.38 --> 1395.76]  about how to make these models more generalizable, as I just mentioned with, you know, this feature representation.
[1396.34 --> 1400.04]  But also, it requires a lot of data to train these.
[1400.24 --> 1414.78]  And one of the things that was figured out, you know, quite interestingly, was that you could do things like have a huge set of images or videos or text or pull, for example, scrape the whole Internet.
[1414.78 --> 1418.12]  And you could construct a task.
[1418.50 --> 1428.34]  In other words, you could construct your example inputs and your example outputs, your training data in an unsupervised way from that large scrape of data.
[1428.60 --> 1431.04]  And let me explain what I mean by that unsupervised.
[1431.04 --> 1442.48]  I mean, in kind of the old days, 2010 to 2017, we would hand curate, you know, this text corresponds to this output and we would manually create that label.
[1442.80 --> 1452.06]  But in this new kind of regime where we boosted the size of these models, we would actually do this in an unsupervised way.
[1452.06 --> 1455.84]  So we would scrape the whole Internet worth of text data, for example.
[1456.22 --> 1472.06]  And then I can construct a meta task, quote unquote, or a set of example inputs and example outputs by just, for example, taking a sentence and removing the last word and then having the last word be the prediction.
[1472.06 --> 1473.88]  And that's an autocomplete task.
[1474.00 --> 1480.18]  Or I could take a sentence and remove a word at the beginning or mask it and have the model try to fill that in.
[1480.58 --> 1482.54]  I can construct that task automatically.
[1482.70 --> 1484.22]  I don't need to have a human do that.
[1484.28 --> 1488.54]  I can actually do it programmatically as I scrape all of this data.
[1488.54 --> 1501.14]  And so you might be seeing where I'm going with this, but tasks like this autocomplete were tasks that were commonly used in the training of these large foundation or base models.
[1501.36 --> 1514.76]  I think mostly with the original intent of having these be transferable to a wide variety of downstream tasks that would be executed via this fine tuning process.
[1514.76 --> 1523.48]  Okay, so those are the two asides about kind of these meta tasks, why those are important.
[1523.70 --> 1527.66]  And then also this idea of feature representation or embedding.
[1527.76 --> 1532.92]  And I'll kind of return to that embedding piece in a bit to kind of set that in context.
[1532.92 --> 1537.08]  But let's get to this final stage of, quote, AI.
[1537.08 --> 1544.30]  And this is, you know, 2022 plus this most recent time maybe people are most familiar with.
[1544.40 --> 1548.88]  And a lot of people hopped on the AI train during this time period.
[1548.88 --> 1551.12]  And we've already talked about this a little bit.
[1551.24 --> 1558.08]  But a couple of things that we haven't maybe talked about on this podcast is in this generative AI phase,
[1558.08 --> 1572.12]  people carried on kind of curating more and more data, increasing model size, using these meta tasks like autocomplete to train these generalizable large foundation or base models.
[1572.12 --> 1579.86]  And as it turns out, if you train a huge autocomplete model on whole Internet's worth of data,
[1580.32 --> 1588.44]  obviously the Internet contains blog posts about coding and tweets and movie scripts and all sorts of things.
[1588.44 --> 1588.68]  Right.
[1588.68 --> 1601.88]  And so if I then have as input to that model a blog post about practical AI is colon and ask the model to autocomplete that,
[1601.88 --> 1612.82]  the probabilities associated with that prediction of those next words would actually predict maybe a quite relevant blog post.
[1612.82 --> 1621.94]  And so now people start to realize, well, wait a minute, because of the scale of this training and the generalizability of this model,
[1622.56 --> 1626.94]  maybe I don't even have to execute this fine tuning process.
[1626.94 --> 1653.32]  Maybe I actually want to just create a large enough model that I can prompt or instruct and then kind of hone in the probabilities of the autocomplete to actually autocomplete what I would autocomplete maybe as a human if I followed these instructions or if I generated this blog post or if I translated this text into a different language.
[1653.32 --> 1683.30]  And that's what people started doing.
[1683.32 --> 1694.82]  And then they'll use their own curated data set, which is still large and very expensive to create, but their own kind of high quality curated data set of prompts,
[1694.82 --> 1706.76]  which might include chat examples and tool usage and various tasks like question answering or machine translation, miscellaneous kind of instructions around summarization.
[1706.76 --> 1720.02]  And this fine tuning data set is then used to further train the model and produce maybe an instruct model or a chat model or a code completion model.
[1720.02 --> 1730.42]  And then we, if we want to consume that model, could use a chat type prompt or a certain instruction to use the model and execute accordingly.
[1731.10 --> 1736.66]  So, yeah, this is kind of how this latest phase of models kind of fits into the history.
[1736.78 --> 1741.14]  And now we're in a phase where primarily we're consumers of these models.
[1741.14 --> 1771.12]  We're not the model trainers.
[1771.12 --> 1772.12]  The primary shift.
[1772.12 --> 1788.84]  And maybe this makes more sense now as you're hearing things, but the creation of optimized prompts, the curation of those prompts, getting domain experts to write and iterate on those prompts, evaluating LLM workflows.
[1788.84 --> 1803.44]  These things are the things that people are thinking about a lot now that they're not the ones training these models, but they're sort of, quote, programming them or executing reasoning over them just at the inference layer.
[1803.44 --> 1811.12]  Now, I mentioned a bit ago, this feature representation or embedding piece of the puzzle.
[1811.32 --> 1816.66]  And we set that in the context of foundation models and transfer learning.
[1816.66 --> 1828.66]  So, I want to circle back to that for just a second as a kind of afterthought here, I guess, which hopefully now you have some context for where those come about.
[1828.66 --> 1856.66]  But we, of course, see those popping up as a very important piece of generative AI workflows because these models, as it turns out, what kind of people learned and started actually on purpose training these models to do, they found out that these internal representations or these embeddings, if I take text and represent it in a very dense, efficient way for use in these downstream tasks.
[1856.66 --> 1865.54]  Actually, text embedded in that space could be used in a semantic search or retrieval fashion.
[1866.18 --> 1884.84]  And so, if I take a sentence about eating great Chicago deep dish pizza and I embed that or represent it into this set of numbers of vector, and then I take another sentence about pizza and I do the same thing, and I take another sentence about flying airplanes and do the same thing.
[1884.84 --> 1897.80]  The two sentences about pizza will be closer, quote unquote, in that vector space, in that according to their vectors that were calculated or their embeddings that were calculated.
[1898.24 --> 1901.34]  They will be closer than the one about airplanes.
[1901.34 --> 1910.34]  And so, this now allows us to semantically search over pieces of text and over other things, connect those things together.
[1911.04 --> 1924.98]  And that has become a key piece, as we've talked about in past episodes, to things like retrieval augmented generation, where we're pulling out information from knowledge bases and injecting that into models.
[1924.98 --> 1932.94]  Now, taking a breath, hopefully, all of that was interesting as we went through those different generations.
[1932.94 --> 1936.56]  I'd like to maybe emphasize a couple of things in your mind.
[1937.26 --> 1944.86]  So, you can see that all of these modeling methods have their place and they're still with us.
[1944.86 --> 1953.98]  So, it's still very efficient and effective to utilize a time series modeling method to do forecasts, for example.
[1954.68 --> 1958.72]  That's in that first generation of models, the statistical machine learning models.
[1958.96 --> 1966.04]  It's still quite relevant if you're, you know, maybe training a new computer vision model for your factory, and that's very specific.
[1966.48 --> 1968.44]  It doesn't need to be general at all.
[1968.44 --> 1993.54]  It doesn't really make sense in many cases to maybe utilize a huge heavyweight vision LLM, for example, or an LVM, a language vision model, to execute at very high throughput on a machine or a manufacturing line for a computer vision model that is trying to find flaws and parts as they're coming off of a manufacturing line.
[1993.54 --> 1999.02]  And efficiency-wise and how that model would have to be deployed, that would be a challenge, to say the least.
[1999.16 --> 2009.60]  And so, maybe you want a very specific model that is a little bit maybe smaller and more accessible, but you also don't need to be training a computer vision model from scratch.
[2009.74 --> 2012.02]  Often, you would start with a foundation model.
[2012.60 --> 2018.20]  And then finally, of course, we're all familiar with a bunch of things that people are using generative AI models for.
[2018.20 --> 2025.16]  So, that's one thing that I'd want to emphasize is all of these types of modeling are still with us and prevalent across industry.
[2025.50 --> 2037.88]  The second thing that I'd want to emphasize is an interesting thing that I've kind of noticed and even talked with someone today about, which is as you have advanced through these different generations of models,
[2037.88 --> 2047.20]  on the more machine learning statistical side, often you had kind of role-wise, you had software engineers or infrastructure engineers on one side,
[2047.86 --> 2056.22]  you had business people or domain experts on the other side, and you had data scientists or data analysts or machine learning engineers in the middle
[2056.22 --> 2065.28]  that would often translate domain-specific problems into models that they would train, which would be deployed by software engineers and infrastructure people.
[2065.28 --> 2072.70]  On the other end of the spectrum, in this generative AI world, often there's not this fine-tuning or training that happens.
[2072.90 --> 2082.16]  And so, often domain experts or business people themselves are prompting these models to accomplish chains of reasoning,
[2082.60 --> 2086.34]  and there's not a data scientist or an analyst in the middle.
[2086.34 --> 2097.42]  And so, there's kind of this shrinking of the zone between domain experts and business people and the direct infrastructure that's running those models,
[2097.62 --> 2099.88]  which is an interesting development.
[2100.60 --> 2107.14]  I think, finally, the thing that I'd like to emphasize is often in an actual business scenario,
[2107.14 --> 2121.26]  the very most intelligent or best or eventually kind of, especially if you're creating a customized, you know, proprietary or very domain-specific approach to a problem or a workflow,
[2121.58 --> 2126.86]  it may involve all of these different types of models or some combination of them.
[2126.86 --> 2135.48]  And so, you can imagine a system, for example, where a user would put in a natural language query and say,
[2135.68 --> 2141.44]  hey, could you forecast out our revenue for two years into the future?
[2142.06 --> 2154.54]  And that may be processed by a generative model to create a tool call that calls a function that uses a statistical or machine learning model to make that forecast,
[2154.54 --> 2161.12]  which returns the answer, which is then interpreted back into natural language by the generative model.
[2161.54 --> 2165.26]  And so, these types of workflows are, I think, some of the most interesting ones.
[2165.92 --> 2172.10]  I guess I said that was the last thing I was going to emphasize, but I've already emphasized this a lot in different shows.
[2172.10 --> 2182.38]  But just to remind people, all of these things that we're executing are software functions and not some sort of fairy dust or sentience that comes about after,
[2182.60 --> 2185.82]  you know, you leave your laptop in the corner of a room for a while.
[2186.34 --> 2195.72]  And so, a lot of the disillusionment that's happening in the AI space is because people think doing AI or this AI transformation
[2195.72 --> 2200.18]  somehow just kind of happens once you, quote, have AI.
[2200.18 --> 2207.82]  But the reality is that these are all software functions, parameterized software functions at different scales, most definitely.
[2208.42 --> 2216.80]  But software functions that need infrastructure to operate and are often integrated into other software systems to be made useful.
[2217.32 --> 2219.56]  And so, engineering is still quite relevant.
[2220.12 --> 2225.76]  Of course, you could argue some of these can write software now if you prompt them in a specific way.
[2225.76 --> 2234.82]  But still, you sort of need to architect that system that does all of that prompting and code generation and integration and execution.
[2235.14 --> 2237.88]  So, there's a lot of interesting things related to that.
[2237.88 --> 2249.24]  Well, it's been fun for me to kind of share this little talk or workshop material with you that I've been talking with people about.
[2249.52 --> 2257.52]  There's a lot of things here, of course, that I haven't covered as part of this episode, but hopefully it gives you an overall sense.
[2257.52 --> 2269.20]  I would definitely recommend people maybe on the generative AI side, if you have yet to kind of play around on the other side, the statistical machine learning side.
[2269.44 --> 2282.60]  If you're technical, maybe you want to just go to something like a Scikit-learn, which is a Python program that even without GPU resources or other things will help you learn about the different types of modeling that is available there.
[2282.60 --> 2286.84]  Those are great examples and you can learn about that.
[2287.38 --> 2304.88]  If you're coming from the more data science machine learning side and you're going to generative AI, of course, I would encourage you to learn about that and think about maybe how you can utilize the best parts of that alongside and with your statistical machine learning workflows.
[2304.88 --> 2311.74]  If you're non-technical in either of these, of course, there's plenty of ways to get hands on with generative models.
[2311.92 --> 2321.92]  But on these other cases, there's still AutoML systems or systems that would allow you to do things in certain domains by uploading data and training models.
[2322.42 --> 2329.22]  If you just search for kind of AutoML, I know H2O had a thing called driverless AI for a while.
[2329.22 --> 2335.10]  And there's various systems like that that you can try and look at interesting results.
[2335.32 --> 2337.96]  So thank you all for bearing with me on this one.
[2338.18 --> 2345.64]  And I'm excited to have Chris back with me for next week's episode, which you'll hear hopefully very soon.
[2346.02 --> 2348.98]  Hope you all have a great week and thanks for joining.
[2348.98 --> 2360.34]  All right, that is Practical AI for this week.
[2361.14 --> 2362.18]  Subscribe now.
[2362.34 --> 2367.34]  If you haven't already, head to practicalai.fm for all the ways.
[2367.74 --> 2373.72]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[2373.72 --> 2378.96]  Sign up today at practicalai.fm slash community.
[2379.54 --> 2386.48]  Thanks again to our partners at fly.io, to our Beat Freaking Residence, Breakmaster Cylinder, and to you for listening.
[2386.84 --> 2388.60]  We appreciate you spending time with us.
[2388.96 --> 2390.14]  That's all for now.
[2390.44 --> 2392.06]  We'll talk to you again next time.
