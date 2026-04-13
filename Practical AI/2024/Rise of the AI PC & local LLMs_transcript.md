[0.00 --> 8.66]  Welcome to Practical AI.
[9.14 --> 19.56]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.22 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 32.38]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.62 --> 48.70]  Hello and welcome to another fully connected episode of the Practical AI podcast.
[48.70 --> 60.44]  In these fully connected episodes, Chris and I keep you connected with everything that's happening in the AI world and hopefully share some resources with you to help you level up your machine learning game.
[61.00 --> 62.42]  My name is Daniel Whitenack.
[62.54 --> 68.14]  I am CEO and founder at Prediction Guard, where we're safeguarding private AI models.
[68.40 --> 74.24]  And I'm joined as always by Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[74.56 --> 75.26]  How are you doing, Chris?
[75.40 --> 76.50]  Doing great today, Daniel.
[76.54 --> 76.92]  How are you?
[76.92 --> 78.34]  Oh, I'm doing well.
[78.48 --> 79.02]  Yeah, yeah.
[79.14 --> 80.54]  Lots going on.
[80.62 --> 83.10]  Lots of fun stuff in the AI world.
[83.38 --> 98.34]  But Chris, I have to say, so one of our listeners pointed out something which I realized afterwards as well on our last fully connected episode, the one about GPT-4O or Omni.
[98.78 --> 103.56]  We played some clips of the voice assistant and we talked a little bit about the model.
[103.56 --> 107.42]  And the model, of course, was released and we were using it.
[107.94 --> 113.66]  But the voice back and forth wasn't yet plugged into GPT-4O.
[113.90 --> 116.50]  So they're just, I think, releasing that shortly.
[116.50 --> 126.44]  So I think there was a bit of general confusion in the community about because when you click that button, it's like you just take over into the voice interface.
[126.44 --> 129.42]  And it's like I was on GPT-4O.
[129.56 --> 136.42]  And so probably could have been maybe handled a bit better on our end and maybe therein too.
[136.42 --> 138.50]  But OpenAI got us, I guess.
[139.06 --> 140.64]  We were fooled.
[141.14 --> 142.70]  But yeah, still really cool stuff.
[142.92 --> 147.24]  Still the things that we talked about are still what GPT-4O is.
[147.36 --> 152.34]  But just wanted to clarify that for our listeners if they had listened to that previous episode.
[152.34 --> 159.84]  While we're doing that, I realized I had made a mistake on that same issue after the show that I wanted to confess on.
[160.10 --> 165.22]  I had watched all the videos over and over again about the video portion doing that.
[165.36 --> 173.56]  And then when we were in the show, I had what I'll claim as a senior moment where I was thinking, I watched so much of the video, I was thinking, oh yeah, I did that.
[173.78 --> 177.50]  And so it wasn't afterwards I was like, no, that was the videos I was watching.
[177.58 --> 178.24]  What was I thinking?
[178.24 --> 179.92]  So anyway, I wanted to confess.
[180.04 --> 182.88]  So we had a couple of blunders on that one, but having fun.
[183.14 --> 183.58]  There you go.
[183.70 --> 191.02]  In our eagerness and excitement to talk about GPT-4O and record it very quickly afterwards, we got got.
[191.34 --> 193.12]  We both got got there.
[193.34 --> 194.36]  So all good.
[194.68 --> 195.38]  We'll move on.
[195.46 --> 201.08]  Well, for listeners who don't know, the show is fairly spontaneous if you haven't been following us long.
[201.50 --> 203.18]  And we dive into stuff pretty quick.
[203.30 --> 206.28]  And occasionally we fumble a little bit with that.
[206.50 --> 207.08]  Yeah, yeah.
[207.08 --> 212.96]  So thanks for journeying with us through this wild and crazy world of AI.
[213.58 --> 220.28]  Now, I think something that's been on my mind quite a bit, Chris, with some recent announcements,
[220.28 --> 231.94]  but also things that have been kind of developing over the past months is this area of local offline AI and AI PCs.
[232.32 --> 235.56]  There's sort of people are using this terminology AI PCs.
[236.70 --> 238.00]  Current marketing hype.
[238.00 --> 240.26]  Yeah, the current marketing hype.
[240.50 --> 247.90]  So I thought maybe we could dig into a little bit of that today and talk through kind of what exactly does that mean?
[248.04 --> 250.40]  How are people using AI models locally?
[250.66 --> 251.76]  What is an AI PC?
[252.50 --> 257.78]  What are the relevant kind of types of models and optimizations that can run locally?
[257.78 --> 265.80]  All of that seems to be a big, well, it's a little bit hard to parse out some of that maybe if you're new to the space.
[266.00 --> 274.28]  And, you know, what is a GGUF versus a Ollama or, you know, all of these things, you know, coming out.
[274.28 --> 276.98]  So, yeah, I thought that would be good to dig into.
[277.14 --> 282.98]  And I know that you have been interested in kind of AI at the edge for some period of time.
[283.34 --> 300.76]  How do you see, whether it's a staff laptop or maybe a heavy compute node in a manufacturing plant or something where you'd want to run AI, quote, at the edge or locally, let's say generally locally or offline.
[300.76 --> 305.42]  What are the reasons that people would sort of want to go that direction?
[305.92 --> 311.16]  Well, I think, you know, this is kind of a thread we've talked about off and on on different episodes over time.
[311.92 --> 318.16]  And, you know, AI models are hosted in software and they're going to always be wrapped in that.
[318.34 --> 324.52]  And as we, you know, the software expands from the cloud all the way out into every device that we're already using.
[324.52 --> 336.40]  And so it's only natural that as AI becomes more accessible and cheaper to deploy that it's going to you're going to start having models, you know, that are kind of ramping up existing software out there.
[336.48 --> 339.34]  And there's, of course, we're going through all the hype that's associated with that.
[339.42 --> 344.98]  But the way I see it is simply just a natural evolution of where software development would go.
[345.10 --> 349.58]  And to your point a moment ago about the hardware side, we don't talk about that a lot.
[349.64 --> 351.68]  We're very software focused in general.
[351.68 --> 354.04]  But the hardware side is really going through a revolution.
[354.28 --> 359.70]  I know that you I know that in your business, you have partnership with Intel and are seeing that in that capacity.
[359.70 --> 361.64]  And I certainly see that in my day job.
[362.28 --> 373.26]  And so there are so many more hardware capabilities coming out to support these functions, many of which will function or are targeting low power, disconnected environments.
[373.74 --> 375.88]  And so this is a timely topic.
[375.88 --> 387.56]  And if you look back for precedent before that, we've always seen over the years in software and cloud development, kind of a shifting back and forth between local capability.
[387.76 --> 394.32]  Suddenly you get a new generation of hardware and things will go a little bit more local and you'll have your own equipment and then things will move back into the cloud.
[394.32 --> 398.32]  And that natural give and take is part of the flow.
[398.46 --> 415.00]  And I think right now we've been so cloud focused the last few years because that was really the only available option that now we're we're seeing a lot of new capability rolling out on both hardware, software and models that are going to enable edge functionality to really explode over the next few years.
[415.00 --> 425.20]  Yeah, I was asked I was at a conference last week and I was asked which direction things would be going either local AI models or hosted in the cloud.
[425.38 --> 441.80]  And I think the answer is definitely both in the same way that there is a place for if you just think about databases, for example, as a technology, there's a place for embedded local databases that operate where an app application operates.
[441.80 --> 450.68]  There's a place for databases that run kind of at the edge, but on a heavier compute node that serve maybe some environment.
[451.26 --> 459.00]  And there's a use case for databases in the cloud and sometimes those even coexisting for various reasons.
[459.24 --> 461.70]  And in this case, we're talking about AI models.
[461.94 --> 464.40]  So I have a bunch of files on my laptop.
[464.94 --> 467.36]  I may not want those files to leave my laptop.
[467.36 --> 474.20]  So it might be privacy reasons that I want to, you know, search those files or ask questions of those files with an AI model.
[474.20 --> 487.72]  So privacy security type of thing or in a health care environment, they may have to be air gapped or offline sort of thing or public utilities sort of scenario where you can't be connected to the public Internet.
[487.72 --> 498.76]  But then it might just be also because of latency or inconsistent networks or flaky networks where you have to operate sort of online, offline.
[498.98 --> 501.42]  There's a whole variety of reasons to do this.
[501.96 --> 513.94]  But yeah, there's also a lot of ways that, as you said, this is rapidly developing and people are finding all of these various ways of running models at the edge.
[513.94 --> 524.04]  And we can highlight if you're just into this now and getting into AI models, maybe you've used OpenAI's endpoint or you've used an LLM API.
[524.38 --> 534.28]  If you wanted to run a large language model or an AI model on your laptop, there's a variety of easy ways to do that.
[534.40 --> 538.08]  I know a lot of people that are using something like LLM Studio.
[538.62 --> 542.92]  This is just an application that you can run and test out different models.
[542.92 --> 548.50]  There's a project called Ollama, which I think is really nice and really easy to use.
[548.60 --> 549.78]  You kind of just spin it up.
[549.92 --> 562.48]  You can either spin it up as a Python library or as a kind of server that's running on your local machine and interact with Ollama as you would kind of an LLM API.
[563.44 --> 567.96]  And then there's things like LLama CPP and a bunch of other things.
[567.96 --> 582.82]  These I would kind of categorize as local model applications or systems where there's either a UI or a server or a Python client that's kind of geared specifically towards running these models locally.
[582.82 --> 602.04]  And then there's a sort of whole set of technologies that are kind of Python libraries or optimization or compilation libraries that might take a model that's maybe bigger or not suited to run in a local or lower power environment and run that locally.
[602.04 --> 612.36]  So if you're using the Transformers library from HuggingFace, you might use something like Bits and Bytes as a library to quantize models, shrink them down.
[612.90 --> 618.14]  There's optimization libraries like Optimum and MLC, OpenVINO.
[618.32 --> 621.56]  These all have some have exist for some period of time.
[621.56 --> 628.44]  Actually, I think in the past we've had the Apache TVM project on the show and we talked about OctoML.
[628.78 --> 635.28]  So this is not a new concept because we've been sort of optimizing models for various hardwares for some time.
[635.28 --> 641.60]  But these optimization or compilation libraries are also usually kind of hardware specific.
[641.88 --> 653.92]  So you optimize for a specific hardware, whereas other of these local model systems are maybe more general purpose, less optimized for hardware specifically.
[654.40 --> 660.78]  I don't know if you've got a chance to try out any of these systems, Chris, running some models on your laptop.
[661.14 --> 662.26]  I have a little bit.
[662.32 --> 662.98]  I've used Alama.
[663.18 --> 664.68]  I think that's my go-to.
[664.68 --> 670.96]  And you have like an M1 or M2, M3, whatever M there is now, MacBook?
[670.96 --> 673.30]  Yeah, I have an M2 that I have.
[673.46 --> 679.24]  I have a couple of different laptops, one that's old and one that's, well, I guess an M2 is old by today's standards.
[679.48 --> 682.06]  So I may have to upgrade that one pretty soon.
[682.36 --> 684.68]  But yeah, I've used Alama primarily.
[684.88 --> 689.14]  I probably haven't used as many of the tools as you have given the business that you're in.
[689.14 --> 706.74]  I think one of the things that I'm really interested in as people are doing this now is understanding, you know, because we're really focusing on this kind of the infrastructure, the plumbing of making all this work locally and doing the integrations with the cloud.
[706.74 --> 736.74] 
[736.74 --> 748.02]  So as we're talking about that, I wanted to throw that in as another topic that I think is going to be really, really important and hasn't had nearly as much attention as the fundamental infrastructure.
[748.02 --> 751.02]  Yeah, I think that gets probably to a couple of things.
[751.18 --> 769.70]  One is that one current major difference between sort of hosted cloud models and offerings versus local models is likely you're not going to run a mix of 10 different LLMs on your local laptop all at the same time, all loaded into memory.
[769.70 --> 777.88]  That would be a pretty significant, at least right now, a pretty significant ask to kind of switch between models in that way.
[778.38 --> 789.86]  But there are certainly cases where, you know, I think the market is showing that people want to not be restricted to one model family and they're spreading out their usage against multiple models.
[790.08 --> 796.32]  So that definitely needs to happen in the cloud and from, you know, model providers.
[796.32 --> 803.50]  But that doesn't mean you couldn't throw in the mix a selection of local models as well for specific purposes.
[803.70 --> 811.28]  And I think that gets to the other thing that you're talking about, which is kind of data integration, automation, pipelining, all of that sort of thing.
[811.38 --> 812.82]  I saw a comment on LinkedIn.
[812.82 --> 833.10]  I think it was even this morning that those that are really winning in the AI space are those that have taken what they've learned kind of from automation, data pipelining, data integration in previous cycles of data science and integrated those with generative models at various stages.
[833.10 --> 843.34]  Because a lot of a lot of the value, and I've seen this too, a lot of the value that you get out of these models is not the models themselves, but the system that you build around them.
[843.84 --> 850.64]  And, you know, that involves a lot of data integration and automation and maybe even routing between different models.
[850.64 --> 855.72]  In the case that we're talking about here, maybe even routing between local models and cloud models.
[856.42 --> 869.46]  And so, yeah, I think that that's really stressed, especially as you talk about running these models kind of everywhere, quote unquote, across cloud and local and on-prem and data center environments.
[870.18 --> 871.18]  But, yeah, it's interesting.
[871.42 --> 874.64]  I don't myself have an AI PC yet.
[874.64 --> 876.96]  Maybe at some point I will.
[877.30 --> 881.16]  But, yeah, I'm excited to see where all this goes.
[882.00 --> 882.04]  Indeed.
[882.40 --> 892.56]  I think as we push forward, I think one of the things that I'd like to see, especially for local, whereas, you know, we have, you know, we mentioned a few minutes ago, Alama and some of the other tools for infrastructure.
[892.56 --> 908.06]  I was actually, as we were talking here, I was looking through Jan LeCun's various posts because he was proposing recently in the last week or two prior to this conversation, kind of a way of structuring different model interactions.
[908.06 --> 912.06]  And from a responsibility standpoint that they're doing at Meta.
[912.64 --> 917.16]  And, of course, at my employer, we have our own version of that on how we structure different things.
[917.16 --> 939.60]  But really interested in seeing if the community kind of comes around with kind of an open framework, you know, best practice framework around how to do that, you know, be able to do it on a laptop, on an M2, M3, M4, be able to have those interactions locally and a framework that would span between that local and the cloud interactions so that you have something.
[939.60 --> 943.98]  And I don't think that right now everyone seems to be doing that on their own.
[943.98 --> 951.52]  And there's a lot of similarities between them, but there doesn't seem to be kind of a standard approach to how that all comes together.
[962.62 --> 969.26]  If you're anything like me, you have a certain tendency to put things off until the very last minute.
[969.26 --> 975.86]  Seeing the dentist, going to the doctor, home improvements, that never ending chore list of yours.
[976.36 --> 984.64]  And while most of the time it works out just fine, the one thing in life that you really cannot afford to wait on is setting up term coverage life insurance.
[985.28 --> 990.16]  You've probably seen life insurance commercials on TV and thought, yeah, I'll look into that later.
[990.66 --> 992.06]  No, later doesn't come.
[992.36 --> 993.68]  This really isn't something you can wait on.
[994.00 --> 996.60]  Choose life insurance through a ladder today.
[996.60 --> 1000.40]  Here's what we love about ladder and why we allow them as a sponsor.
[1000.90 --> 1002.08]  They are 100% digital.
[1002.50 --> 1004.94]  No doctors, no needles, no paperwork.
[1005.34 --> 1010.70]  When you apply for $3 million in coverage or less, just answer a few questions about your health in an application.
[1011.30 --> 1015.38]  Ladder's customers rate them 4.8 out of 5 stars on Trustpilot.
[1015.68 --> 1018.56]  And they made Forbes best life insurance 2021 list.
[1018.88 --> 1021.72]  You just need a few minutes and a phone or laptop to apply.
[1022.02 --> 1024.56]  Ladder's smart algorithm works in real time.
[1024.56 --> 1026.60]  You'll find out if you're instantly approved.
[1026.76 --> 1027.68]  No hidden fees.
[1027.88 --> 1028.94]  You can came to any time.
[1029.26 --> 1033.54]  Get a full refund if you change your mind in the first 30 days.
[1033.92 --> 1039.50]  Ladder policies are issued by insurers with long proven histories of paying claims.
[1039.86 --> 1043.18]  They're rated A and A plus by A.M.
[1043.26 --> 1043.64]  Best.
[1044.10 --> 1047.52]  Finally, since life insurance costs more as you age now.
[1047.94 --> 1048.58]  Yeah, right now.
[1048.84 --> 1050.56]  Now's the time to cross it off your list.
[1050.56 --> 1057.90]  So go to ladderlife.com slash practical AI today to see if you're instantly approved.
[1058.16 --> 1062.64]  Again, that's ladder.com slash practical AI.
[1062.76 --> 1068.26]  L-A-D-D-E-R life.com slash practical AI.
[1068.26 --> 1084.68]  Well, Chris, there's an increasing number of options.
[1084.68 --> 1098.86]  If you were to explore this space and kind of that interaction of local models with your systems, there's an increasing number of choices of, quote, AI PCs, which I think is a hyped term now.
[1099.32 --> 1102.12]  One of them, you mentioned Intel.
[1102.24 --> 1104.06]  Intel coming out with AI PCs.
[1104.06 --> 1110.36]  I think Lenovo is shipping some with Intel's Core Ultra processor.
[1110.88 --> 1113.96]  I think the name is Meteor Lake, the code name at least.
[1114.46 --> 1120.26]  And similar probably to as a response to maybe what's more familiar.
[1120.38 --> 1124.80]  I already mentioned the M1, M2, M3, et cetera line from Apple.
[1124.80 --> 1139.36]  But NVIDIA is also working hard on, like, the GeForce RTX AI PCs, which there've been kind of gaming PCs with, like, GPUs in them for some time.
[1139.36 --> 1151.06]  But I think most of these, quote, AI PCs are more of an integrated type of processor or system where it's not just, like, an add-on to the laptop.
[1151.52 --> 1162.30]  But in the case of, like, the Core Ultra or the M2, there's actual processing in the architecture that is optimized for executing models.
[1162.62 --> 1166.14]  And so they're sort of AI-ready, shipping AI-ready.
[1166.14 --> 1174.14]  And that brings up kind of some interesting questions in my mind, which are, well, how do all of these AI PCs compare?
[1174.52 --> 1179.56]  If I'm about to get myself an AI PC, where should I go?
[1179.70 --> 1190.60]  And in thinking about that and looking at some of these benchmarks, I was really encouraged to see that ML Commons, which is the organization behind ML Perf,
[1190.60 --> 1205.38]  which is a set of benchmarks and working groups that have been working for some time to benchmark various systems for performance on running AI workloads, machine learning workloads.
[1205.38 --> 1227.72]  They've just announced this spring an ML Perf, which is really geared towards essentially an application or a workload that you could run across these various AI PCs or maybe AI-enabled edge machines and that sort of thing,
[1227.72 --> 1239.22]  to really do kind of LLM-based workloads and do some benchmarking for both training and inferencing on these, quote, clients.
[1239.58 --> 1242.86]  So they're kind of referring to these generally as clients.
[1242.86 --> 1253.54]  So they say the new ML Commons effort will build ML benchmarks for desktop, laptop, and workstations for Microsoft Windows and other operating systems.
[1254.18 --> 1255.48]  So quite interesting.
[1255.62 --> 1261.68]  I'm glad that this, as far as I can tell, someone in our, again, you know, sometimes we get things wrong.
[1261.68 --> 1270.46]  So someone in our audience can correct us, maybe David from ML Commons, who's been on the show before, he can correct us if something's already been published.
[1270.58 --> 1273.56]  But I couldn't find this sort of set of benchmarks.
[1273.72 --> 1277.48]  I think it's a work in progress, but really excited to see this when it comes out.
[1278.02 --> 1281.32]  Yeah, I think it'll be interesting as these laptops come out.
[1281.32 --> 1293.90]  But it's hard to imagine that the entire industry doesn't have to go full in on this regardless and thus kind of making the distinction of an AI laptop a little bit of a redundant thing.
[1293.90 --> 1305.14]  Because there's a point, and maybe we've already arrived now, where the idea of purchasing a new laptop that is not an AI laptop is a ridiculous thing.
[1305.14 --> 1312.54]  You know, it becomes a must-have feature to have going forward, and therefore all laptops kind of have to go that direction at some point in the year.
[1313.00 --> 1313.20]  Yeah.
[1313.68 --> 1325.56]  Well, I definitely think that that could be one downside of this whole thing is that there's, I mean, I know the prices will go down, but these things are really expensive right now.
[1325.56 --> 1331.90]  So there is going to be a sort of disparity of those already for some period of time.
[1331.90 --> 1343.42]  If you're a new developer, maybe an indie developer, that purchase of that MacBook is a pretty significant expense for you already.
[1344.42 --> 1352.14]  And, you know, myself, I just use a refurb ThinkPad from like four years ago, you know, not an AI PC.
[1352.14 --> 1363.94]  It's a Core i5 and, you know, not a terrible laptop, but definitely not anything that anyone would necessarily be jealous of.
[1364.28 --> 1370.14]  Now, I can run some models on this laptop, you know, using Ollama and other systems.
[1371.02 --> 1374.06]  And I think that that gets down to maybe another element of this.
[1374.06 --> 1388.30]  So there's going to be on one side, these clients that get increasingly sophisticated and build in more AI enabled or accelerating functionality into their chipset and into their hardware.
[1388.30 --> 1398.12]  But there's also going to be increased sophistication on optimizing models that can't run locally such that they can run locally.
[1398.12 --> 1414.30]  And this is where people might kind of I think this is also a point of common confusion that I've heard in workshops that I've given at conferences and other places where people kind of look at let's say it's Llama 3 or something like that.
[1414.48 --> 1415.98]  I want to run Llama 3.
[1416.38 --> 1421.98]  While you go to Hugging Face, the top downloaded Llama 3 is the base model.
[1421.98 --> 1425.74]  And then you've got these fine tunes for instruction or chat.
[1426.20 --> 1442.88]  And then you've got all of these other flavors of Llama 3 like, you know, GGUF, GGML, QAT, AQ, AWQ, you know, all sorts of like acronyms that are really difficult to understand.
[1443.06 --> 1446.94]  So maybe it would help to just break this down just slightly.
[1446.94 --> 1455.96]  Usually there's usually when a model is released, they release a base model or the pre-trained model or whatever it's called, a base model.
[1456.08 --> 1460.74]  So that's that kind of shortest name usually, the meta, you know, Meta Llama 3.
[1461.32 --> 1470.88]  That usually is maybe a good model that you might fine tune off of, but not generally the best model to start with because it's a base model.
[1471.02 --> 1475.36]  It's not fine tuned for any sort of set of general instruction following or chat.
[1475.36 --> 1482.50]  And they usually release along with that then a set of fine tune models for instruction or chat.
[1482.58 --> 1487.88]  So you've got Meta 3 or Llama 3 instruct, which is usually the better model.
[1488.12 --> 1493.08]  And then you've got this whole world of community members out there that build pipelines.
[1493.22 --> 1494.84]  So we had Noose Research on.
[1495.06 --> 1501.40]  They have pipelines built so that when a model is released, they can create all these different flavors of it,
[1501.40 --> 1507.70]  which include flavors for running these optimized in certain ways.
[1507.86 --> 1513.00]  So these would be these other acronyms that we can dig into a little bit.
[1513.10 --> 1521.84]  But these are most of the time either additional fine tunes or quantized versions or somehow optimized versions of these models
[1521.84 --> 1525.56]  that are meant to be run in kind of a diverse set of environments.
[1525.56 --> 1542.18]  What's up, friends?
[1542.30 --> 1544.54]  Do you remember when ChatGPT launched?
[1544.72 --> 1545.18]  I do.
[1545.42 --> 1549.68]  It felt like the LLM was this magical tool out of the box.
[1550.02 --> 1553.44]  However, the more you use it, the more you realize that's just not the case.
[1553.44 --> 1554.68]  The technology is brilliant.
[1554.80 --> 1559.34]  Don't get me wrong, but it's prone to issues like hallucination on its own.
[1559.42 --> 1560.02]  But there's hope.
[1560.34 --> 1561.72]  There is still hope.
[1562.12 --> 1566.66]  Feed the LLM reliable current data, ground it in the right data and context.
[1566.88 --> 1571.60]  Then and only then can it make the right connections and give the right answers.
[1571.98 --> 1578.72]  The team at Neo4j has been exploring how to get results by pairing LLMs with knowledge graphs and vector search.
[1578.72 --> 1585.82]  Check out their podcast episode about LLMs and knowledge graphs throughout 2023 at graphstuff.fm.
[1585.94 --> 1589.78]  They share tips on retrieval methods, prompt engineering, and so much more.
[1590.04 --> 1590.72]  Don't miss it.
[1590.98 --> 1592.58]  Find a link in our show notes.
[1592.98 --> 1593.84]  Yes, check it out.
[1594.08 --> 1596.88]  Graphstuff.fm, episode 23.
[1596.88 --> 1621.42]  Well, Chris, I kind of started getting into the alphabet soup a little bit.
[1621.42 --> 1631.94]  I don't know if you're sometimes as confused as I am with all of these model names, but they're getting increasingly long.
[1632.68 --> 1637.22]  You know, one of the – finish your point there and then I have a question for you afterwards.
[1637.60 --> 1638.66]  Yeah, yeah, sure.
[1638.80 --> 1646.18]  You know, I was just going to highlight a few of these different quantization methods so that people could maybe have them in their mind.
[1646.18 --> 1650.98]  So there's the flavors that are GGML or GGUF.
[1651.28 --> 1652.62]  You might see those letters.
[1652.86 --> 1656.04]  This is GPT-generated unified format.
[1656.46 --> 1657.98]  That's what that stands for.
[1658.46 --> 1670.18]  And this is an optimization of a model that will take that model that maybe requires a GPU to run as larger and creates a C++ replica of the LLM.
[1670.18 --> 1691.04]  And allows you to run it in quantized versions, meaning that the parameters of the model are taken from, you know, numbers that might have 32 or 16 digits behind the period and get that down to 2 or 4 or 8, that sort of thing, which makes the model smaller and more efficient.
[1691.04 --> 1698.74]  So these are mostly geared towards CPU, sort of CPU or laptop kind of environments.
[1699.00 --> 1708.00]  There's also GPT-Q, which is really a focused kind of quantization method, but it's still meant for GPU only.
[1708.00 --> 1720.98]  So these usually ship in similar kind of formats to previous models, but they do kind of some calibration-informed quantization to get that model smaller.
[1721.26 --> 1733.22]  There's QAT, which is quantization-aware training, which, as it might sound, involves some actual training, retraining of the model to inform the quantization.
[1733.22 --> 1739.48]  There's others like AWQ, and this is another quantization method.
[1739.58 --> 1762.12]  So all of these sort of letters that you see, if you're wondering what those are, those are all kind of referring to these different kind of flavors of the model that might be generated for either running the model in an optimized way locally on a CPU, on a laptop, or optimized still on a GPU, but in a smaller format that's more efficient.
[1762.12 --> 1765.72]  What are your thoughts on the CPU derivative?
[1766.10 --> 1773.20]  What are your thoughts on performance and capability relative to its own base model and its GPU siblings?
[1773.66 --> 1791.34]  Yeah, I mean, I think that the reality right now, and then maybe where it's headed, I think the reality right now is the CPU-based models, even you can run some models that are even 7 billion parameters or something in some quantized version.
[1791.34 --> 1821.32]  On a CPU, you're not going to run those.
[1821.32 --> 1824.42]  Usually, that's going to still live in the cloud.
[1824.42 --> 1839.20]  But if you have some sort of private use case where something can't leave the laptop, or maybe it's like you're deploying laptops in a disaster relief scenario, and there's going to be not that much connectivity, right?
[1839.20 --> 1843.20]  It's still enough throughput to get responses.
[1844.02 --> 1852.70]  So if you had chat over your disaster relief docs and that on your laptop, it's still enough to get an answer in that scenario.
[1853.46 --> 1855.40]  And people can push it pretty far.
[1855.62 --> 1859.18]  I think the difference is just, again, it's not one or the other.
[1859.40 --> 1861.40]  It's the use case, I guess.
[1861.40 --> 1871.86]  Yeah, I think, and just to add to that use case slightly, I think there's also disconnected or partially connected mobile platforms where you can't necessarily rely on the cloud access.
[1872.06 --> 1875.02]  And you have devices that are out there as well.
[1875.02 --> 1883.06]  Just to lump that in, kind of pulling around full circle for a moment back to the laptops, these AI laptops coming out.
[1883.06 --> 1892.88]  Kind of thinking back to the natural kind of segregation of responsibilities that we have in software development, aside from just the AI world.
[1893.16 --> 1906.98]  Would you imagine that a reasonable level of support in those would be to be able to actually do training on like 7 billion size models, the smaller range that are so much more of those?
[1906.98 --> 1912.26]  That maybe in the not so distant future, I'm training a model, it's in that range.
[1912.60 --> 1916.18]  My own laptop can handle that, not just for inference, but for training.
[1916.30 --> 1919.26]  And then for very large models that's still cloud-based.
[1919.34 --> 1923.88]  Do you think that that is a reasonable level that we might see AI laptops able to support?
[1923.88 --> 1933.78]  I mean, I think that you can see some people trying some more training or rather fine-tuning sorts of things on diverse hardware.
[1933.78 --> 1950.24]  I think basically what I'm seeing right now is still primarily inference on local machines and utilization of things like in-context learning and RAG-type workflows to integrate data rather than fine-tuning locally.
[1950.50 --> 1955.20]  So I think that that's kind of the reality of where it is.
[1955.20 --> 1970.36]  I think there's a possibility in the future, maybe of some type of training type of scenarios that will happen, maybe not on client devices, but spread across client devices.
[1971.16 --> 1979.94]  So it's been a while since we've talked about federated learning, but it will be interesting to see if that kind of rears its head in this world.
[1979.94 --> 1987.06]  I know that there's been efforts to kind of train LLM adapters in a federated way.
[1987.28 --> 1995.58]  And there's some papers about this and share kind of parameter-efficient updates to weights across different client devices.
[1995.58 --> 1997.44]  That seems really intriguing to me.
[1997.88 --> 1998.84]  But yeah, I don't know.
[1998.92 --> 1999.98]  We'll see where it goes.
[2000.10 --> 2001.22]  Maybe I'll be proved wrong.
[2001.22 --> 2008.60]  But I think I'm increasingly more of a proponent of most people don't need to fine-tune.
[2009.32 --> 2015.84]  A lot of it can be done with RAG and chaining and agents and selecting the right models.
[2016.50 --> 2022.88]  So I think that, especially as models get better, that will be the case kind of moving forward.
[2023.28 --> 2028.38]  But yeah, I am looking forward to getting an AI PC and putting it through its paces eventually.
[2028.38 --> 2032.28]  Yeah, right now my M2 is through my employer.
[2032.54 --> 2039.78]  So my next one will be, I'm hoping to be either an M4 or I'm thinking about possibly a non-Apple one as well.
[2040.10 --> 2045.54]  So the M4s are supposed to be able to do quite a bit more than the earlier generations.
[2045.92 --> 2048.80]  So looking forward to being able to pursue this.
[2049.24 --> 2050.14]  Yeah, yeah, definitely.
[2050.14 --> 2056.96]  Well, I hope our audience will include a few links to some blog posts about these quantization methods
[2056.96 --> 2062.62]  and some of the systems like OLAMA and LMStudio and others that we talked about.
[2062.76 --> 2066.66]  I would encourage everyone to get hands-on and try your own hand at it.
[2066.70 --> 2070.56]  And you'll get a sense for the performance of these models locally.
[2070.82 --> 2072.56]  So definitely give it a try.
[2072.96 --> 2073.10]  All right.
[2073.26 --> 2074.36]  Well, thanks a lot, Daniel.
[2074.48 --> 2075.94]  That was great information today.
[2076.14 --> 2076.96]  It was a good show.
[2077.20 --> 2078.52]  And thanks for bringing that.
[2078.96 --> 2079.20]  Yep.
[2079.20 --> 2080.04]  We'll talk to you soon.
[2080.14 --> 2088.74]  All right.
[2088.92 --> 2091.42]  That is Practical AI for this week.
[2092.22 --> 2093.26]  Subscribe now.
[2093.42 --> 2098.42]  If you haven't already, head to practicalai.fm for all the ways.
[2098.42 --> 2104.82]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[2105.36 --> 2110.02]  Sign up today at practicalai.fm slash community.
[2110.66 --> 2117.56]  Thanks again to our partners at fly.io, to our beat freaking residents, Breakmaster Cylinder, and to you for listening.
[2117.92 --> 2119.68]  We appreciate you spending time with us.
[2120.00 --> 2121.22]  That's all for now.
[2121.22 --> 2123.14]  We'll talk to you again next time.
[2123.14 --> 2123.24]  We'll talk to you again next time.
[2123.24 --> 2134.10]  Game on!
