[0.00 --> 8.66]  Welcome to Practical AI.
[9.14 --> 19.56]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.22 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 32.38]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.86]  Learn more at Fly.io.
[47.30 --> 51.68]  What's up, friends? I'm here with a new friend of ours over at Assembly AI.
[51.68 --> 64.70]  Founder and CEO Dylan Fox. Assembly AI is where you can turn voice data into insights, chapters, transcripts, summaries, and so much more with their leading speech AI models.
[65.28 --> 69.38]  So Dylan, give me a glimpse into what you're doing with speech AI models at Assembly AI.
[69.38 --> 78.94]  So at Assembly, we're building industry-leading speech AI models for various tasks like speech-to-text, streaming speech-to-text, speech understanding,
[79.22 --> 85.30]  to help developers easily convert voice data, whether it's live or pre-recorded, into super accurate text.
[85.52 --> 90.40]  And then to help developers extract a ton of information and metadata around voice data,
[90.44 --> 94.22]  or even around the text that they just were able to convert from that audio data.
[94.22 --> 100.46]  So these are things like picking out entities or PII that was spoken in voice files,
[100.76 --> 106.12]  or summarizing voice and audio data down into custom summaries.
[106.44 --> 112.38]  It's things like being able to detect how many speakers spoke and who said what and what the names of different speakers were.
[112.64 --> 121.02]  So we bundle all those things into a super simple API with really great docs that developers can just sign up to for free to start,
[121.02 --> 128.58]  use the API, build into their apps, and then build these really cool AI apps and products and workflows and automations on top of voice data with.
[128.70 --> 129.84]  I dig it. Okay.
[130.06 --> 133.30]  Can you take me a little deeper into the opportunity for developers?
[133.42 --> 139.54]  Because it seems like there's a lot of voice data out there, and there's a lot of trapped value in that voice data.
[140.10 --> 143.10]  There's so much voice data being created on the internet now.
[144.06 --> 149.54]  Podcasts, videos, phone calls, voice messages, audiobooks, virtual meetings.
[149.54 --> 157.66]  This is crazy. And you can now transform and understand all this voice and audio data in ways that were not even possible a year or 18 months ago.
[157.66 --> 162.80]  And so what we're seeing with the help of these new AI models that we're creating at Assembly,
[163.00 --> 171.40]  developers and organizations are just racing to build all these new applications, workflows, automations that leverage the voice data they have,
[171.56 --> 179.64]  either within their organization or within their product, to build really cool new products and services and workflows that are just like taking off in the market.
[179.64 --> 185.26]  And so at Assembly, we're building the industry-leading models for all those different apps and workflows,
[185.38 --> 192.92]  whether it's speech-to-text or speaker diarization or speech-understanding capabilities to summarize voice data or extract entities from voice data,
[193.18 --> 198.14]  or mask PII from phone calls for various types of automations that might be built.
[198.40 --> 204.68]  And we're exposing that through a super simple, super scalable API that's just constantly being updated and constantly getting better.
[204.68 --> 212.84]  And so we're seeing just a crazy amount of developers and companies just build really cool apps and services on top of our API every day.
[213.10 --> 219.48]  It's really only just getting started, especially with the model updates that we have planned over the second half of the year that are coming out.
[219.66 --> 222.56]  They're really excited to launch to the developers on our API.
[223.42 --> 227.12]  Okay. Constantly updated speech AI models at your fingertips.
[227.52 --> 229.94]  Well, at your API fingertips, that is.
[229.94 --> 232.36]  A good next step is to go to their playground.
[232.36 --> 240.14]  You can test out their models for free right there in the browser, or you can get started with a $50 credit at AssemblyAI.com.
[240.34 --> 243.16]  Again, AssemblyAI.com.
[247.52 --> 252.14]  Welcome to another fully connected episode of the Practical AI podcast.
[252.62 --> 254.24]  This is Daniel Whitenack.
[254.34 --> 260.74]  I am the founder and CEO of Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[260.74 --> 265.16]  who is a Principal AI Research Engineer at Lockheed Martin.
[265.74 --> 274.54]  In these fully connected episodes, Chris and I will keep you fully connected with some of the things happening in the AI news and trends,
[274.68 --> 280.02]  and we'll also discuss a few topics that will help you level up your machine learning game.
[280.28 --> 280.92]  How are you doing, Chris?
[281.28 --> 281.82]  Doing good.
[281.88 --> 282.80]  How are you today, Daniel?
[282.90 --> 284.16]  I think you're traveling, aren't you?
[284.16 --> 294.46]  I am in transit, so hopefully the hotel Wi-Fi slash hotspot holds out, and we can keep it going.
[294.80 --> 305.30]  But yeah, going over to GopherCon UK, which should be fun to talk to a few Go programmers about AI and integrating it into Go applications.
[305.50 --> 306.20]  So that should be fun.
[306.20 --> 306.72]  Fantastic.
[307.54 --> 308.18]  Sounds good.
[308.32 --> 308.66]  That's it.
[308.78 --> 317.78]  Incidentally, for people who may have just joined the show, that's actually how Daniel and I originally met way back was through the Go programming community.
[317.96 --> 319.56]  So this is a throwback there.
[320.08 --> 320.70]  Yeah, yeah.
[320.74 --> 321.46]  It should be fun.
[321.80 --> 326.40]  This is actually my first GopherCon UK, so that'll be good.
[326.40 --> 326.44]  Good.
[327.08 --> 334.26]  Well, Chris, one of the things that had occurred to me maybe, I don't know, last week or this week or sometime,
[335.02 --> 347.76]  was seeing a lot of people kind of on general AI threads or on social media talking about how AI is only as good as the data that's fed into it.
[347.76 --> 354.74]  Or, you know, AI, doing AI in the enterprise or in a real world environment is all about data.
[354.92 --> 360.12]  It's not about the models or, you know, some type of comments like that on social media.
[360.22 --> 360.88]  Have you seen these?
[361.36 --> 361.72]  I have.
[361.82 --> 362.28]  I have.
[362.48 --> 371.52]  And I've actually been glad to see that versus all the hype of some of the other topics that we've been dealing with over recent time.
[371.62 --> 373.98]  So let's get into some data conversation.
[374.52 --> 375.38]  Yeah, yeah.
[375.38 --> 383.50]  Basically, my thought was, well, what, I guess, one, what do people even mean when they say something like that?
[383.50 --> 393.18]  And then second, I think from a practical kind of boots on the ground standpoint, if you're doing data science, AI, machine learning stuff,
[393.22 --> 404.94]  there's probably a huge number of types and kind of categories of data that you might run across or have a chance to be exposed to.
[404.94 --> 422.10]  And so I thought it may also be good to kind of break down and categorize some of those things to give people a little bit of a landscape of types of data or things that they might run across in the AI space or things that they might even have to curate in their own company.
[422.10 --> 424.48]  So, yeah, that's kind of what I was thinking.
[424.48 --> 435.68]  I guess in that first point, what do you think people mean when they refer to this, you know, AI is only as good as the data you bring to it or it's all about data?
[436.22 --> 438.72]  What are people trying to get out there, do you think?
[438.72 --> 444.02]  Well, I think it is the constraint around and limitation to the models that you're trying to build.
[444.24 --> 448.86]  So, you know, when we build AI models, they are self-training.
[448.98 --> 450.56]  We're not teaching it what to do.
[450.72 --> 455.08]  And so you're presenting the data that you want to build the model out of.
[455.10 --> 460.40]  And the model is only as good as what the data that it's going to be able to train on is.
[460.40 --> 467.02]  And so the quality of the data and the robustness of the data is absolutely crucial.
[467.28 --> 471.94]  And we, you know, it's funny, over the last few years, there's been so much hype.
[472.04 --> 474.38]  You know, we've talked about generative AI and stuff.
[474.96 --> 480.00]  Folks tend to get caught up in the hype and they tend to think of kind of the AI being on its own.
[480.54 --> 482.88]  And I think that's today's topic.
[483.12 --> 488.82]  That's one of the things we've been wanting to bring people around to is there's been a certain amount of disappointment and misunderstanding.
[488.82 --> 495.86]  And at the end of the day, your model is only as good as the data that you're bringing so that it can train on.
[496.46 --> 506.42]  And so it's a moment to get back to basics, maybe leave some hype behind and recognize that if you don't get this part of it right, you're not going to have a very good outcome.
[506.42 --> 520.40]  Yeah. So you mentioned a few things there I'd love to pick apart, which is this idea of there's some kind of provenance to a model that has to do with the data.
[520.56 --> 527.52]  So it may be good to remind people that a model, when we're talking about an AI model, is really composed of two things.
[527.52 --> 536.72]  It's composed of code that executes functions and adds things together and kind of essentially does a data transformation.
[537.18 --> 548.94]  So maybe it's an image in and a label out that's a label, whether it has a cat in the image or not, or maybe it's text in and a generated next token out.
[548.94 --> 558.38]  And these are data transformations and that code that executes those data transformations is, you know, written in code, just like normal code.
[558.50 --> 561.88]  But it includes a bunch of parameters that need to be set.
[562.40 --> 572.38]  And by a bunch, you know, maybe people are familiar from seeing models now, but that might be, you know, 7 billion parameters, 70 billion parameters, 400 billion parameters.
[572.38 --> 587.14]  So in order to set those parameters to do that data transformation, there needs to be data that is used to fit those parameters, often called that training process.
[587.70 --> 597.18]  Now, one element of this, Chris, is if you imagine like Llama 3.1, which is a recent addition to our world, has whatever, 400 billion parameters.
[597.18 --> 604.00]  You could imagine that maybe you're not going to fit that many parameters with a small amount of data.
[604.84 --> 611.16]  And so there's some relation between the complexity of the model and how much data is needed to fit it.
[611.48 --> 624.54]  And that may in itself be something that people aren't quite grasping often is that the bigger the model you want to use, the more data you need to have to train it, which is why these data sets have got larger and larger.
[624.54 --> 627.68]  And I think that's important to call that out.
[627.68 --> 641.68]  And that as people are getting into the idea of training their models, there's a certain amount of understanding what's realistic for you and your capabilities and your organization's capabilities to do up front.
[641.84 --> 650.70]  And I think that's why there's a set of concerns about how you're going to enter into the process to begin with, which I think you're covering here.
[650.82 --> 653.44]  But I don't think that's very clear for a lot of people.
[653.44 --> 660.36]  I think they, you know, when they use foundation models, when they're going to go create their own and stuff like that.
[660.46 --> 669.52]  And I think the data you have available and the quality of the data and the amount of data, to your point about complex models, is really crucial to consider up front.
[670.02 --> 675.02]  If someone is interested in taking their organization forward, how do you start thinking about this, Daniel?
[675.08 --> 680.38]  How do you frame the whole issue of what data you have and what you can do with that data?
[680.38 --> 690.74]  I think this is something we've highlighted on the show before, but people sort of have this perception that, oh, we've got a bunch of documents in a file store.
[690.86 --> 691.94]  We've got a big database.
[692.38 --> 698.38]  We should be able to do AI or do machine learning with that data, right?
[698.38 --> 703.16]  And the situation is definitely more complex than that.
[703.28 --> 710.16]  So I would say that there's really two things maybe that people need to kind of have in their mind.
[710.30 --> 717.24]  One is the type of task that you're wanting to do, which maybe is also related to the type of model that you'll use.
[717.24 --> 724.40]  And also, what is the state of the structure of the data that you have?
[724.48 --> 726.20]  So let's give an example.
[726.38 --> 735.88]  So let's say that you want to do object detection, which is the task of taking in an image and detecting what objects are in that image.
[735.88 --> 739.78]  So that's a computer vision task.
[739.88 --> 744.26]  You usually require some type of convolutional neural network.
[744.26 --> 755.62]  And some of this you could kind of search through and find the type of task that you are trying to do and then kind of the typical model that is used to do that.
[755.62 --> 765.74]  And you might find, oh, these typical models that are used for object detection usually need thousands and maybe millions of images to train on.
[766.30 --> 772.00]  So that may trigger in your mind, well, first of all, do I have enough imagery to train that model?
[772.40 --> 779.14]  If you do have enough data to train the type of model that you're interested in, then maybe you do that.
[779.48 --> 784.90]  But oftentimes what people need to do is fine tune a model, not train a model from scratch.
[784.90 --> 796.80]  So that would be taking a model that already exists, maybe is posted on Hugging Face in a repo that is already trained for some type of task related to what you're doing.
[796.88 --> 799.08]  So maybe a similar object detection task.
[799.28 --> 804.68]  And then you kind of continue the training on from that point with your small amount of data.
[805.24 --> 810.26]  Now, the second piece to that is, like I mentioned, how structured or unstructured your data is.
[810.26 --> 826.86]  So if I just have a bunch of images in a file store, that really doesn't do me any good for that object detection task because they're not pre-labeled with labels that I would be able to use to further train one of those models.
[826.86 --> 835.36]  So another relevant thing here is, is your data unstructured or unlabeled or structured or labeled?
[835.64 --> 850.88]  And in the case of training a supervised type model, which is a model that requires some labels to be trained, like an object detection model or sentiment analysis or machine translation, maybe,
[850.88 --> 856.12]  then you need those labels in order to further train your model.
[856.66 --> 867.10]  So just to kind of recap what I just said there, there was the element of determining what task and what kind of model is needed and how that maps to your data.
[867.10 --> 872.96]  And then whether you have enough data or not enough data for pre-training or just fine tuning.
[873.24 --> 878.80]  And then finally, if you have labeled or unlabeled data or structured or unstructured data.
[879.34 --> 880.60]  Let me ask you a question here.
[880.78 --> 894.90]  To your point about computer vision, in my own experience across a couple of different companies in computer vision projects, I've used YOLO, which is one of the very common convolutional models that's out there.
[894.90 --> 904.00]  And doing that, we've had to go through labeling process, but you're using YOLO as a foundational model that you're building upon.
[904.28 --> 923.46]  Is that in your thinking about that, if you have a set of maybe a few thousand images that you're using on YOLO, is there ever a good reason to potentially say, well, maybe I don't want to use a foundational model, even though it requires more data to train?
[923.46 --> 928.18]  Would I ever want to go create a new computer vision model to work with?
[928.26 --> 930.60]  Is there ever, how do you think about that?
[930.68 --> 935.78]  Because that's come up in topics a number of times as projects got started and stuff.
[935.90 --> 941.74]  How do you think about when to go use somebody else's foundation model versus maybe trying to do something like that on your own?
[942.10 --> 951.52]  Yeah, I think that it kind of comes into this element of how big of a model is needed and how complicated of a problem you're trying to solve.
[951.52 --> 967.04]  So certainly for something like object detection, especially if you have a bunch of labels that you're trying to detect in your imagery, and generally that task is fairly complicated task, I guess, in terms of even how we would think about doing that data transformation.
[967.04 --> 973.12]  Then it likely needs a more complicated model, which means more data to train that model.
[973.12 --> 998.36]  And in most of those situations, whether you're talking about object detection or machine translation or speech synthesis or speech transcription, these sorts of tasks, most of the time companies would be much better off doing a fine tuning and not a training from scratch, either because they don't have enough data internally to train a model from scratch, or they don't have it labeled appropriately.
[998.36 --> 1004.36]  Or maybe they just don't have a big enough compute cluster to do that training.
[1004.36 --> 1010.58]  And so they could benefit then from a pre-trained model that would do fine tuning on that.
[1011.12 --> 1018.44]  But maybe other tasks like a sentiment analysis or a forecasting problem where you're forecasting a time series.
[1018.44 --> 1028.38]  It's not that you couldn't do that in the fine tuning approach, but that it may only take, you know, five seconds or five minutes to train that sort of model.
[1028.54 --> 1039.12]  And on a small amount of data, like thousands of samples, not millions of samples, and that could achieve your goal very well and be a small model that you could run performantly.
[1039.12 --> 1042.64]  So in those cases, of course, you would be training a model from scratch.
[1048.12 --> 1050.72]  This is a Changelog Newsbreak.
[1051.00 --> 1054.06]  The Phylum Research Team writes, quote,
[1054.06 --> 1084.06] 
[1084.06 --> 1097.02]  In other words, among all new packages published to NPM in the past six months, about five out of every seven packages are T-spam, end quote.
[1097.70 --> 1104.10]  I first covered the unintended consequence of the T-Protocol's crypto rewards back in February.
[1104.38 --> 1105.58]  That was episode 83.
[1106.10 --> 1109.98]  It appears the damage is even worse than previously discovered.
[1110.48 --> 1111.68]  What a mess.
[1112.56 --> 1113.56]  That is one big pilot.
[1114.06 --> 1118.88]  You just heard one of our five top stories from Monday's Changelog News.
[1119.28 --> 1131.66]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1132.12 --> 1135.56]  Once again, that's changelog.com slash news.
[1141.46 --> 1142.22]  All right.
[1142.22 --> 1146.70]  Well, Chris, we've talked a little bit about training, pre-training.
[1146.70 --> 1155.24]  So there's this first category of data, which is training data or pre-training data, sometimes might be called.
[1155.78 --> 1162.16]  And this would be the data that you're taking a model where the parameters have not been fit, an untrained model.
[1162.16 --> 1169.84]  And you are doing the first fitting or training of those parameters with this training or pre-training data.
[1169.84 --> 1177.96]  Now, along with that training or pre-training data, of course, you may have tests or holdout or evaluation data.
[1178.06 --> 1184.80]  This is a second category of data that you might have, which may just be a holdout from that training set.
[1184.80 --> 1194.86]  It might be a public kind of benchmark type of test set for a particular task like machine translation or something like that.
[1195.22 --> 1202.96]  Or maybe it's data that you're going to use and have humans review or something like that.
[1202.96 --> 1205.10]  But anyway, it's a test set.
[1205.24 --> 1206.06]  It's an evaluation set.
[1206.14 --> 1208.30]  It's held out from that training or pre-training.
[1208.88 --> 1214.62]  So you have a volume of data and you're maybe taking like arbitrarily 20% of that data and setting it aside.
[1214.74 --> 1215.56]  Is that what we're getting at?
[1215.94 --> 1216.20]  Yeah.
[1216.38 --> 1216.58]  Yeah.
[1216.58 --> 1229.26]  And of course, if you look up like how much you should hold out or how you should construct test sets or evaluation sets, that's a very complicated rabbit hole that you could go down.
[1229.36 --> 1236.62]  But I would say at the most simple level, yes, you can take whatever your training set is and hold some out.
[1236.62 --> 1252.56]  And oftentimes you would do that randomly so that, you know, there's no kind of if your data is stratified, meaning it has some structure to it in terms of what comes first and last, then you could randomize that and get a little bit better sample.
[1253.20 --> 1260.90]  And that'll then allow you to train your model or fit your model and then make predictions on that test or evaluation set.
[1260.90 --> 1275.58]  So you can calculate a metric, maybe that could be accuracy or F1 score or in the case of machine translation, blue or comet, or in the case of time series forecasting, some mean squared error, mean absolute error type of thing.
[1276.08 --> 1280.40]  And that then allows you to gauge, well, am I doing better than random?
[1280.86 --> 1283.66]  Do I have any predictive power to my model, I guess?
[1284.30 --> 1286.32]  And it's relative to that training data set.
[1286.32 --> 1288.00]  So, you know, specifically.
[1288.00 --> 1298.72]  So it's assuming that the model is accurate against the training set that you had there or other data that you may introduce later that is very consistent with what you would see in the training set.
[1298.78 --> 1299.62]  Is that accurate?
[1300.10 --> 1300.78]  Yeah, exactly.
[1300.78 --> 1317.92]  You want to hold out enough to where you have confidence that when your model sees new samples that you would likely see in a kind of production scenario, then you're able to make predictions on those new samples and get ideally a prediction.
[1318.00 --> 1319.78]  Some type of predictive power.
[1319.78 --> 1324.54]  A result that is useful for the task that you've trained on.
[1325.32 --> 1330.06]  And there's public benchmark data for a lot of different tasks as well.
[1330.18 --> 1337.50]  If people are looking for that, people might be familiar if you just search like open LLM benchmarks or leaderboard.
[1337.68 --> 1339.66]  There's a bunch of leaderboards for LLMs.
[1339.66 --> 1340.90]  But there's also public.
[1340.90 --> 1345.06]  You may want to search like shared task data.
[1345.80 --> 1352.42]  Often this benchmark or evaluation data comes out of peer-reviewed workshop type of scenarios.
[1352.74 --> 1357.38]  So if people aren't aware, there's these research conferences in the AI world.
[1357.54 --> 1365.04]  And research conferences are the primary way that people publish academic AI research.
[1365.04 --> 1371.82]  And at these academic AI research conferences, there's sometimes things called workshops.
[1371.82 --> 1378.88]  And this isn't like, I mean, there's learning that goes on, but it's not like a learning workshop like you go to at an industry conference.
[1378.88 --> 1386.38]  It's a workshop to work on specific problems related to research problems related to a topic.
[1386.64 --> 1392.64]  And then share results together around usually a common shared task.
[1392.76 --> 1399.68]  So there might be a workshop for computer vision related tasks or machine translation related tasks.
[1399.78 --> 1404.76]  There's one called WMT, which always has a shared task around machine translation.
[1404.76 --> 1411.34]  And there's many other types of shared tasks that publish peer-reviewed benchmark evaluation data.
[1411.86 --> 1418.58]  And how would you, just going for a moment back to the previous thought process around training data and test data,
[1419.04 --> 1424.68]  how does benchmark data sets, how do they fit in to your notion of training and test?
[1424.76 --> 1425.76]  Are you using them afterwards?
[1426.52 --> 1428.36]  How does that fit into your process?
[1428.36 --> 1439.08]  Yeah, so if you are doing a task that is the same or very similar to an existing benchmark that's out there,
[1439.56 --> 1447.34]  some or all of the data related to that benchmark may form either test or training data for you
[1447.34 --> 1451.44]  when you're doing your fine tuning or evaluation, right?
[1451.44 --> 1457.56]  So let's say, for example, you're training a machine translation model from English to Arabic.
[1458.22 --> 1462.94]  You could go and look at a bunch of different benchmarks related to machine translation,
[1462.94 --> 1467.70]  and they'll have many, many different language pairs, including English to Arabic potentially.
[1468.38 --> 1476.58]  And so you may use a portion of that data for evaluating your model or for adding to your training data set.
[1476.58 --> 1486.54]  However, if you're doing machine translation maybe to a new language pair that isn't represented in any of those academic benchmarks,
[1486.54 --> 1495.12]  this would be the scenario where your company's maybe trying to do something that hasn't been represented in the academic research world yet,
[1495.64 --> 1503.38]  like a manufacturing company that's wanting to detect defects in certain types of products using a computer vision model.
[1503.38 --> 1511.50]  There's likely not a shared task for that, other than the fact that there are many computer vision shared tasks.
[1511.72 --> 1522.38]  And so a way to think about it in that scenario is if my company is trying to design this new model to detect defects in chips
[1522.38 --> 1526.54]  or in other types of products on a manufacturing line,
[1526.54 --> 1533.90]  I could go to a shared task and look at, well, what are the best models that people are using these days
[1533.90 --> 1541.10]  for the task of the relevant computer vision tasks like object detection or something like that.
[1541.10 --> 1547.70]  And so in that case, the benchmark or the shared task data would represent more of a gauge for you
[1547.70 --> 1553.58]  or like a starting point to determine maybe what types of models you want to be considering.
[1553.58 --> 1556.92]  If I'm doing that, is that fine tuning the model?
[1557.10 --> 1564.24]  Is that actually like at this point you're talking about creating a new model rather than using foundation or am I misunderstanding that?
[1564.74 --> 1565.58]  Yeah, good question.
[1565.84 --> 1575.00]  So really, this is maybe part of the categorization where there's overlap and maybe people tend to get confused.
[1575.00 --> 1583.66]  So there's kind of one set of categories which is related to the type of data and the way that you're using that data.
[1583.80 --> 1588.00]  So you're going to be using some data for training your model or pre-training a model,
[1588.44 --> 1595.46]  some data for fine tuning a model or adapting a foundation model,
[1595.64 --> 1602.06]  and some data for evaluating or testing or benchmarking a model.
[1602.06 --> 1606.40]  So those are the categories of data that you would use in this process.
[1607.02 --> 1611.38]  Now, where you source that data could be from public benchmark data.
[1611.78 --> 1618.24]  It could be from data that is internal to your company that likely isn't public,
[1618.26 --> 1620.78]  or it could be a combination of the two.
[1621.58 --> 1628.12]  And so that's kind of you want to be thinking about both about how you're using the data and for what purpose,
[1628.12 --> 1633.08]  and also being creative with where you might get it from, right?
[1633.08 --> 1633.68]  Gotcha.
[1634.06 --> 1640.40]  As you're mixing data from your own organization with some of this benchmark data
[1640.40 --> 1647.98]  and trying to align that so that you have the benefit of trying to maybe fine tune on a model
[1647.98 --> 1650.54]  and use benchmark data to drive that,
[1650.86 --> 1656.78]  but you're also trying to introduce your own new capabilities based on data that your company has,
[1656.78 --> 1665.00]  how do you get those two sets of data to end up being a high quality data set without a lot of differences between it?
[1665.08 --> 1668.02]  As you're trying to kind of get the best of both worlds,
[1668.18 --> 1671.00]  taking advantage of that, which is already there,
[1671.54 --> 1677.18]  but bringing some new capabilities out that your company or your organization can leverage.
[1677.42 --> 1681.60]  How do you think about merging those two desperate sets of data
[1681.60 --> 1685.34]  so that you end up getting a good training set to do some fine tuning with?
[1685.34 --> 1686.18]  Yeah.
[1686.54 --> 1693.06]  So I think this really depends on how close the task that you're really trying to accomplish is,
[1693.64 --> 1699.30]  how close that task is to the public data that's out there.
[1699.74 --> 1703.34]  And in certain cases, it may be very close.
[1703.36 --> 1706.12]  Like I mentioned, the Arabic translation example,
[1706.32 --> 1711.58]  there's language or by text or parallel text data from English to Arabic.
[1711.58 --> 1714.08]  There's a lot of that data out there.
[1714.16 --> 1716.38]  And if that's a specific task that you're doing,
[1716.96 --> 1725.68]  maybe you are using that in your initial training and then fine tuning with your domain specific data on top of that later on.
[1726.08 --> 1732.18]  Whereas other cases, you may just treat that public data as a good starting point,
[1732.18 --> 1737.70]  or you might even just look at what models are trained on that public benchmark data
[1737.70 --> 1742.80]  in order to understand which foundation model you're going to use and fine tune
[1742.80 --> 1747.86]  or which model you could pull off of hugging face to then fine tune
[1747.86 --> 1751.64]  because it was high ranking on this benchmark,
[1751.86 --> 1754.00]  which was close to the task that you're doing.
[1754.56 --> 1756.28]  And then you can fine tune on top of that.
[1756.28 --> 1761.44]  So yeah, remember, you're not always, I guess, doing the pre-training step of this.
[1761.56 --> 1763.80]  You may only be doing the fine tuning step.
[1764.46 --> 1767.80]  And also, I would encourage people to think about, I guess,
[1767.84 --> 1771.44]  this mix of data within your organization and data outside.
[1771.82 --> 1776.66]  So there's a lot of data on repositories like hugging face
[1776.66 --> 1782.58]  that might be useful to your company if adapted in a very specific way.
[1782.68 --> 1785.18]  So let me give a simple example.
[1785.18 --> 1788.72]  So there's a benchmark out there called SQUAD,
[1789.08 --> 1794.32]  which is a question answering, extractive question answering type of benchmark.
[1794.90 --> 1799.24]  And this was used to train models very specifically for question answering.
[1799.54 --> 1804.24]  So not the kind of general purpose large language models that are out there.
[1804.58 --> 1810.34]  But you could take the SQUAD dataset, which has essentially in the input,
[1810.34 --> 1818.06]  it has paragraphs of text and some question that's asked and answered in that paragraph of text,
[1818.06 --> 1822.46]  and then paired with the appropriate answer that's extracted out of that.
[1823.00 --> 1827.56]  And so it's very possible if you're doing a question answering sort of task,
[1827.56 --> 1832.16]  you could test whatever model you're using on that SQUAD output.
[1832.16 --> 1837.96]  But even if you're using like an LLM, you could structure that data in a way that you could test
[1837.96 --> 1840.78]  the LLM's performance on that benchmark.
[1841.30 --> 1847.76]  Or you could take that data and structure it into prompts for fine tuning an LLM.
[1848.22 --> 1853.38]  Even though this dataset was made prior to this latest wave of LLMs,
[1853.38 --> 1860.36]  it's still relevant and can be used for various purposes related to even these Gen.AI models.
[1860.58 --> 1862.46]  So there's a lot of stuff out there.
[1862.54 --> 1868.60]  And I think it would benefit companies to kind of explore the datasets available in the space
[1868.60 --> 1874.12]  that they're thinking about and not just write them off if they're not labeled exactly like they
[1874.12 --> 1879.48]  want them labeled because they still may be useful with some strategic post-processing.
[1879.48 --> 1883.06]  Just to combine, since you brought up Gen.AI along the way,
[1883.14 --> 1886.34]  and obviously that's on people's minds over the last couple of years a lot,
[1886.86 --> 1891.24]  we've talked on a number of episodes about how popular RAG is,
[1891.60 --> 1897.80]  which is retrieval augmented generation, which lets them take their own data that they have available
[1897.80 --> 1904.78]  and use it with a generative model so they may have an interface to company data and stuff.
[1905.26 --> 1907.86]  Does any of what we're talking about here apply to that?
[1907.86 --> 1912.82]  In terms of the, as we're looking at data and what you're using and data quality,
[1912.98 --> 1917.06]  and they're starting to think, you know, because maybe their manager has come to them and say,
[1917.14 --> 1920.02]  hey, we'd like to use, I've heard about RAG, I want to use this.
[1920.52 --> 1925.72]  Is there any overlap in this process that, you know, or are they totally separate?
[1926.18 --> 1931.86]  I think we mentioned this on a few previous episodes where a lot of times what people consider
[1931.86 --> 1939.16]  like adding their data to these Gen.AI models is not actually even changing the model at all.
[1939.26 --> 1941.94]  So it's not even fine tuning the model.
[1942.10 --> 1944.60]  It's not, certainly not pre-training the model.
[1944.72 --> 1947.48]  What it's doing is augmenting the prompts.
[1947.86 --> 1955.54]  So, you know, using a retrieval mechanism, pulling something out of their data and injecting it into the prompts of these models.
[1955.54 --> 1959.36]  So that's data that's being used to augment these models.
[1959.60 --> 1966.14]  And so if you think about how this fits in, there's the data that, just trying to pull it all together here,
[1966.22 --> 1970.56]  there's the data that Meta used to pre-train LAMA 3.1.
[1970.82 --> 1978.76]  We don't have access to that full data set, but they use some very large data set of text to pre-train LAMA 3.1.
[1978.76 --> 1988.34]  They then used a curated set of prompts to fine tune LAMA 3.1 for instruction following,
[1989.06 --> 1992.42]  which is the instruct version of LAMA 3.1.
[1992.88 --> 2003.08]  And then you, you know, Chris could download LAMA 3.1 and quote, add in your own data using this RAG-based approach.
[2003.08 --> 2008.30]  But you're not actually changing any of the parameters of the LAMA 3.1 model.
[2008.30 --> 2009.52]  You're not updating it.
[2009.70 --> 2017.06]  It's just you're running it and injecting your model then as a sort of knowledge base or via augmentation.
[2017.36 --> 2022.40]  So in that whole chain of events, you had training data or pre-training data.
[2022.54 --> 2027.70]  You had test and evaluation and benchmark data, which was used to benchmark LAMA 3.1.
[2027.92 --> 2032.30]  You had fine tuning data, which was used to fine tune the instruct version.
[2032.30 --> 2043.02]  And then you have kind of the knowledge base or augmenting data, which is then injected at runtime to improve the performance of the model.
[2043.26 --> 2045.44]  And that kind of gets, I guess, the full chain there.
[2046.08 --> 2046.16]  Gotcha.
[2046.32 --> 2049.00]  Now, that was a great explanation for the differences between them.
[2049.00 --> 2060.44]  Well, Chris, we've talked a lot about data and I, hopefully some of that discussion is useful for people in terms of the categories of data in their mind.
[2060.44 --> 2067.24]  But there's also some interesting things, of course, with all of this data being used.
[2067.58 --> 2078.34]  There's the chance of misuses of data, which have always been popular to be talked about, especially in Europe around things like GDPR.
[2078.34 --> 2082.64]  But most recently with this EU AI Act.
[2082.74 --> 2095.34]  And I know one of the things that you texted me earlier was the fact that the EU has this AI Act and it's enforceable now or it went into force recently.
[2096.20 --> 2096.64]  Is that right?
[2097.12 --> 2097.62]  It did.
[2098.02 --> 2100.84]  So it's been a couple of years in development.
[2100.84 --> 2114.36]  It had originally been back in April 21st of 2021, had been proposed by the European Commission and then the European Parliament passed it on the 13th of March of this year.
[2114.50 --> 2119.84]  And then it was unanimously approved by the EU Council on May the 21st.
[2119.94 --> 2126.56]  And it has come into effect on August 1st, which, as we record this, was less than two weeks ago.
[2126.56 --> 2134.92]  And it has a number of provisions and they are coming into being over a variable time basis.
[2135.44 --> 2140.26]  Some are kind of coming into being very quickly or within the first few months.
[2140.62 --> 2143.96]  Some of them are going to take as much as three years to come into effect.
[2144.08 --> 2154.02]  But it is, in its own right, really the most comprehensive legal treaties of artificial intelligence in the world so far.
[2154.02 --> 2160.74]  Obviously, there have been some we had in the United States, the White House had issued some stuff.
[2160.94 --> 2167.98]  But we have not had an AI legal framework get passed through the United States Congress.
[2168.70 --> 2170.82]  And so the EU has done that.
[2170.90 --> 2173.38]  They've done the first very large one.
[2173.38 --> 2176.84]  And it's gotten its fair share of criticism.
[2177.26 --> 2180.16]  But it's done a pretty good job, I think.
[2180.30 --> 2190.40]  I say that as a non-legal mind, about trying to address some of the concerns that have been enunciated over the last few years about AI capabilities,
[2191.06 --> 2194.58]  particularly in terms of risk, with some risk categories there.
[2194.74 --> 2197.34]  Have you had a chance to take a look at some of those?
[2197.34 --> 2198.66]  Yeah, it's interesting.
[2198.92 --> 2206.36]  I mean, this gets to the things that I love thinking about on this podcast, which are the practical sides of this.
[2206.60 --> 2211.94]  So for those of you out there in Europe and likely, as we've seen on this show in the past,
[2212.06 --> 2217.76]  regulations originating in Europe tend to make their way over to the U.S.
[2217.76 --> 2223.46]  or even kind of broadly to what people tend to do globally.
[2223.46 --> 2231.66]  And so me as a practitioner, am I going to be regulated by these risk categories of AI?
[2231.94 --> 2239.72]  And so it's useful, I think, to know them and kind of understand how your systems fit in and where you're likely to see some regulatory burden.
[2240.82 --> 2246.24]  And yeah, there's kind of low, moderate, high and band risk.
[2246.44 --> 2248.16]  There's some type of scale like that.
[2248.16 --> 2258.80]  On the low end, you've got things like systems like spam filters or video games that don't really have mandatory regulations.
[2258.80 --> 2262.94]  And you could kind of decide if you follow guidelines for that.
[2263.32 --> 2269.86]  And it goes all the way up to band systems, which are things that are unacceptable risks.
[2269.86 --> 2288.06]  Right. So maybe using AI systems to provide people with a social score that would impact their government services or actually malicious use of AI to influence the behavior of children or something like that.
[2288.38 --> 2296.70]  Yep. The actual categories, just to call them out, is unacceptable risk, high risk, general purpose AI, limited risk and minimal risk.
[2296.96 --> 2299.26]  Yeah. So you're sorry. I didn't mean to cut you off. Keep going there.
[2299.26 --> 2309.90]  No, no, you're good. Yeah. So what have you seen in terms of things that did anything surprise you in terms of things that might have been judged risky,
[2309.90 --> 2316.18]  that maybe a good number of people are even exploring right now that they could face regulation?
[2316.64 --> 2324.18]  They're really looking at what AI capabilities are trying to, you know, what outcomes are they trying to achieve?
[2324.18 --> 2331.40]  And, you know, by way of example, we talked about unacceptable risk is that highest category, which are those banned things.
[2331.56 --> 2340.54]  And that really comes down to AI capabilities that are seeking to manipulate human behavior, you know, explicitly.
[2340.54 --> 2349.88]  And those that might use a real-time remote biometric identification, you know, there are certain use cases with things like facial recognition,
[2349.88 --> 2354.40]  where it could fall into the unacceptable risk, depending on what you're trying to do with it.
[2354.40 --> 2368.52]  And then things, you know, we've talked about things like social scoring in, you know, in China, those types of things where you're essentially applying a scoring to human behavior to try to influence how people are behaving.
[2368.52 --> 2384.78]  Those types of applications where the AI is making changes to how humans are operating to their behaviors are very typical of those that would be found in the banned versions of AI that would be considered unacceptable risks.
[2385.36 --> 2386.60]  And so that's a good example.
[2386.60 --> 2402.48]  So it is important to note as part of that, that across the board, military and national security applications of AI are exempt from the scoring under this law, just to note that up front.
[2402.48 --> 2415.90]  So obviously there can be things that happen in a national security or defense, you know, context that might be considered a very high-risk thing, but because of the nature of what you're trying to do, it would be allowed.
[2415.90 --> 2418.52]  So I wanted to note that early on in the process here.
[2419.74 --> 2429.16]  How much, Chris, do you think these risk categories, certainly there's specific things that the act has in mind.
[2429.28 --> 2436.60]  You know, we can actually see examples of things like the social scoring piece in China and that sort of thing.
[2437.26 --> 2445.68]  But other things like, well, there's going to be new types of things that are done with AI that maybe weren't anticipated.
[2445.90 --> 2446.64]  By the act.
[2446.64 --> 2457.16]  So how much do you think these categories will be able to actually capture some of that net new functionality that maybe was not anticipated by the regulators?
[2457.80 --> 2466.40]  I think it does a reasonable job of trying to capture that because rather than going after specific applications, they hit categories.
[2466.40 --> 2490.98]  So as an example, the high-risk category, which means that it is something that is allowable, it's not banned, but it would be highly regulated and it would typically apply to things, for instance, in health, healthcare, safety, fundamental rights of people, recruitment, critical infrastructure management, law enforcement, justice.
[2490.98 --> 2503.60]  All of those are areas where the law explicitly says this is an application in which you're regulated in because the potential for bad outcomes is legitimately there.
[2503.60 --> 2508.16]  Although it is allowed because there's potential for very good outcomes as well.
[2508.28 --> 2514.72]  But, you know, the higher the risk, the more they explicitly are looking to offer the regulation.
[2514.72 --> 2524.88]  But conversely, for very low-risk applications, they go down to the point of, for minimal risk of having zero regulation whatsoever, if you classify that.
[2525.04 --> 2534.74]  So that might be a video game or a spam filter, you know, that you're playing where the video game is not trying to adjust behavior or something, but just pure entertainment.
[2534.74 --> 2564.72]  They say, you know, they say, you know, they're going to be able to do that.
[2564.72 --> 2571.76]  I think enforcement's supposed to start, you know, fairly early on and certainly on the risks.
[2572.34 --> 2582.52]  And I don't know if there's a specific date or if it started off the bat on August 1st, but I know they were talking about, you know, things rolling out in a six to 36-month timeline.
[2582.52 --> 2598.92]  So certainly over the next six months, by the end of that, we should start hearing about the fact that EU is, you know, and I suspect there will be news stories that we're following on how different applications that once upon a time they might have just done it.
[2599.34 --> 2604.52]  And now they are, you know, there may be a legal battle or regulatory battle to get that in.
[2604.52 --> 2614.28]  And that's now part of the AI landscape, especially if you are either global or operating primarily, you know, in Europe, then this is the new reality.
[2614.28 --> 2626.10]  And I suspect to your point earlier that it will be some form of this will start taking hold in the U.S., throughout Asia, you know, all across the world.
[2626.10 --> 2631.98]  This will gradually take hold over the next few years as other laws pass, which will probably be somewhat similar.
[2632.36 --> 2641.98]  Yeah. Well, it is super interesting to see these things develop, and I'm sure that we will see more and more develop around this in the coming days.
[2642.16 --> 2655.90]  And this is, of course, mostly focused around risk, but there's other types of regulation that, you know, we've talked about on the show before, even in the U.S., related to the executive action around AI and other things.
[2655.90 --> 2659.46]  So, yeah, it'll be interesting to see how this plays out, Chris.
[2659.50 --> 2663.70]  And I look forward to chatting on the show about it here with you.
[2664.22 --> 2671.18]  Oh, I'm sure we're going to have an episode or two come up where an interesting story comes out on how regulation is applying.
[2671.42 --> 2675.94]  And so, yeah, we probably have some interesting things to talk about in the months ahead.
[2676.22 --> 2678.56]  All right, Chris. Well, I hope you have a good rest of your day.
[2678.66 --> 2682.50]  Thanks for talking through all the data and AI act stuff with me.
[2682.70 --> 2685.36]  Thanks a lot, man. That was great explanation. Talk to you next time.
[2685.90 --> 2696.54]  All right. That is Practical AI for this week.
[2697.28 --> 2703.54]  Subscribe now. If you haven't already, head to practicalai.fm for all the ways.
[2703.94 --> 2709.92]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2709.92 --> 2715.18]  Sign up today at practicalai.fm slash community.
[2715.76 --> 2722.70]  Thanks again to our partners at fly.io, to our Beat Freaking Residents, Breakmaster Cylinder, and to you for listening.
[2723.06 --> 2724.82]  We appreciate you spending time with us.
[2725.18 --> 2728.28]  That's all for now. We'll talk to you again next time.
[2739.92 --> 2762.18]  Bye.
