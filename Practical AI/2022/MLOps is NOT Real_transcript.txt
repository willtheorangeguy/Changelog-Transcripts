[0.00 --> 6.68]  You know, the tools for model deployment today are largely not super accessible to data scientists.
[7.00 --> 10.04]  They're more accessible to folks that are machine learning infrastructure,
[10.26 --> 11.28]  so your machine learning engineer.
[11.40 --> 15.32]  And I feel like with the right tools, you should be able to get a data scientist to export,
[15.32 --> 20.72]  you know, their model into a well-defined container that contains a model that then
[20.72 --> 26.36]  you can hand off to an existing DevOps team and IT infrastructure that should not be specialized
[26.36 --> 27.22]  to machine learning.
[27.22 --> 34.18]  That step from a model to the thing that the existing DevOps teams and IT infrastructure could use,
[34.32 --> 35.56]  that can be automated.
[44.56 --> 45.70]  Hello, friends.
[45.86 --> 52.36]  Jared here to tell you about Changelog++, our membership program for those of you who want to directly support our work.
[52.90 --> 56.78]  Your++ membership gets you closer to the metal with extended episodes,
[56.78 --> 62.56]  makes the ads disappear, and takes our audio to the next level with higher bitrate MP3s.
[62.70 --> 66.32]  You can join today at changelog.com slash plus plus.
[77.88 --> 84.10]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[84.10 --> 85.68]  and accessible to everyone.
[86.12 --> 90.42]  This is where conversations around AI, machine learning, and data science happen.
[90.42 --> 96.16]  Join us at practicalai.fm slash community and follow the show on Twitter.
[96.36 --> 98.34]  We're at Practical AI FM.
[98.76 --> 103.40]  Thank you to our partners at Fastly for shipping our pods super fast all around the world.
[103.62 --> 105.46]  Check them out at fastly.com.
[105.46 --> 114.70]  Welcome to another episode of Practical AI.
[114.70 --> 116.70]  This is Daniel Whitenack.
[116.82 --> 119.72]  I am a data scientist with SIL International.
[120.06 --> 125.22]  I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[125.54 --> 126.52]  How are you doing, Chris?
[126.76 --> 127.98]  I'm doing very well, Daniel.
[128.08 --> 133.52]  It's a beautiful spring day here in Atlanta, and we are going to have a good time for the next hour or so.
[133.52 --> 134.74]  Yeah, definitely.
[135.08 --> 136.38]  You know, it's interesting.
[137.06 --> 144.26]  The topic of ML Ops has increasingly come up on the show, and we've had different takes on the topic.
[144.56 --> 149.44]  And I'm really excited today to have a sort of different perspective on that.
[149.50 --> 154.58]  And so welcome back to the show, Luis Ceze, who is CEO of OctoML.
[154.82 --> 155.62]  Welcome back, Luis.
[155.96 --> 156.60]  Thank you, Daniel.
[156.70 --> 157.28]  Thank you, Chris.
[157.36 --> 158.74]  It's great to be back here.
[158.78 --> 161.34]  I had a lot of fun, you know, almost a year ago now.
[161.36 --> 162.34]  It was almost a year.
[162.44 --> 162.98]  It's crazy.
[162.98 --> 164.32]  Lots happened since then.
[164.68 --> 167.68]  And right now, it's also a beautiful spring day in Seattle as well.
[168.08 --> 170.18]  Yeah, it was about a year ago.
[170.40 --> 174.68]  We talked through some things about Apache TVM and OctoML.
[175.20 --> 181.14]  Do you want to give just like a quick update on maybe like the Apache TVM world?
[181.26 --> 187.76]  And then maybe circle back over to OctoML and like what's been happening with OctoML in that meantime?
[188.34 --> 188.82]  Yeah, absolutely.
[188.82 --> 191.34]  So on Apache TVM, lots of progress there.
[191.34 --> 199.10]  The community kept growing nicely and steadily with a lot of fantastic people doing work on machine learning systems, compilers, and so on.
[199.52 --> 202.58]  So TVM, there's a lot of progress on automation and better performance.
[202.58 --> 207.84]  We call it performance automation to make it easier to get to high performance machine learning code in different hardware.
[208.36 --> 212.46]  We held our TVM conference in December last year.
[212.70 --> 213.70]  The largest ever.
[213.86 --> 217.80]  We had just about 1,600 registrants and 1,700.
[218.06 --> 218.56]  That's awesome.
[218.56 --> 223.76]  And 700 people actually attending live and then more folks that consumed the content after that.
[224.12 --> 235.82]  And it was really nice to see contributors to TVM, but also folks from the general machine learning acceleration community and harder vendors participate and cloud providers participate and so on.
[235.82 --> 250.16]  Also related to Apache TVM, we announced the TVM Unity effort, which is essentially an effort on bringing together all the key threads in performance automation, extensibility, and so on.
[250.34 --> 254.88]  And integration with the rest of the ecosystem, you know, front and center on TVM.
[254.88 --> 263.18]  So it's our, you know, view there is really not what we call not too opinionated on how you actually get a model to run well and a harder target.
[263.18 --> 268.26]  It's about how do you actually enable people to do what they want productively, including using other pieces of the ecosystem.
[269.04 --> 271.34]  So yeah, TVM is moving along really, really well.
[271.40 --> 272.18]  So it's great to see.
[272.74 --> 273.90]  And now on the OctoML side.
[274.10 --> 277.12]  So since May last year, we more than doubled.
[277.24 --> 279.02]  The team is about 130 people now.
[279.02 --> 289.16]  We've made significant changes to our platform, to the SaaS platform that uses TVM as one of its key components to automate the process of deploying machine learning models.
[289.72 --> 306.64]  And we recently released also a private accelerated model hub, which is a set of models that are pre-accelerated to a bunch of different hardware so folks can see, you know, the power of the platform in automating the process of getting models from the hands of data scientists into deployable artifacts.
[306.64 --> 318.66]  Yeah, and we also formed a lot of former partnerships with key hardware vendors like AMD, ARM, Qualcomm, and cloud providers like Microsoft Azure.
[319.32 --> 320.66]  Yeah, that's awesome.
[320.82 --> 324.02]  You sort of mentioned this idea of the hub.
[324.18 --> 331.06]  We've definitely seen like model and data hubs sort of like just grow huge over the past year.
[331.06 --> 341.12]  Probably one of the things over the past year that we've really seen explode is like, you know, hugging face with, you know, 30,000 plus models now and other sort of hub environments.
[341.12 --> 355.24]  So, yeah, it's interesting to hear how that kind of idea is impacting a lot of whether it's people trying to optimize models for certain hardware or people just trying to try out things and that sort of thing.
[355.24 --> 361.34]  Has that impacted the types of clients and customers that are coming into OctoML?
[361.58 --> 367.00]  Because like in general, they can access models much quicker and then they realize, oh, these are slow.
[368.30 --> 369.72]  Right. Yeah, no, great point.
[369.88 --> 377.10]  They absolutely has affected not, so not just customers that comes our way, but also, you know, I'll say the entire ecosystem now.
[377.10 --> 387.46]  Because the way I see the maturation of these model hubs is that it's much easier for folks to find models to start from or even find models already do what they need to do and just get them to deployment.
[387.68 --> 400.16]  So they really make it easier for folks to get to a working model that does what they need to do, which means that a lot of the action now shifts to how do you get these models to production to add value as part of an application.
[400.16 --> 409.66]  Right. I know it's great to see our friends at HuggingFace making incredible progress in democratizing, you know, creating new machine learning models and creating communities around it.
[409.92 --> 413.62]  And our point of view on the model hubs is to complement that.
[413.80 --> 420.30]  So we're not talking about not a place where people come and find, you know, new models like HuggingFace and refine those models to create other models.
[420.30 --> 431.54]  It's more about here's some popular models that people can come and see pre-accelerated to a bunch of different harder targets and see how they compare across, you know, edge devices and clouds and cloud instances and so on.
[431.54 --> 445.92]  Yeah. And maybe as a reference, I like to bring this up occasionally in the podcast because a lot of people are focused on that sort of training new models side and maybe like coming up with cool demos and such.
[445.92 --> 451.76]  But, you know, the bulk of what happens in industry in terms of how you run models is inference.
[452.04 --> 455.44]  Right. So have you seen people like come in?
[455.56 --> 475.90]  They're really excited about like the demo that their data scientists, you know, created, but then just really blocked on that sort of like what is the what is the typical kind of process and viewpoint that you see come in to OctoML where they maybe do they already know what they want to do?
[475.92 --> 478.92]  And they're just really blocked on scaling that up.
[478.92 --> 480.92]  Or is it is it something else?
[480.92 --> 498.02]  Yeah, you know, the parts of the flow that we cover is you have a model that you want to deploy and then you have to navigate all of the paths from a model to, you know, what kind of hardware you're going to deploy it on, you know, and for that hardware, what kind of libraries and compilers and tools you should use to actually arrive at a deployable artifact.
[498.02 --> 507.76]  And even just extracting the model from what the data scientists produce, you know, from model to working piece of software is something that takes manual work and then we automate that.
[507.90 --> 512.16]  Right. So but now this might be a good moment for us to step back and talk a little bit about ML Ops.
[512.16 --> 522.06]  Right. So, you know, thinking about the entire flow from data to a deployed model that's actually adding value to a business or adding value to a user, there's several steps.
[522.16 --> 534.24]  Right. So you curate the data to create training data sets and then you think about model architectures and, you know, you train models or you do some architecture search to find out the right architecture for the model that you want.
[534.24 --> 544.82]  And then after that, you need to once you arrive at a model that has the right statistical properties for you want to do, you need to turn that into a working piece of software that you can deploy.
[545.24 --> 548.24]  Right. So and that step is very labor intensive.
[548.24 --> 556.16]  Right. You have to extract code from, you know, it could be a jumbo mass of Python code to go and extract a model that you can put in a box with a clean interface.
[556.16 --> 557.58]  Right. So you have to extract that.
[557.82 --> 562.88]  That terrible button in your notebook that's like export this notebook to a Python script.
[562.88 --> 567.88]  Yeah. And then from there to a working piece of software you can go and deploy is a lot of work.
[567.94 --> 576.46]  And then you have to go and optimize, make sure it has the right performance property such that it has the right latency in case it's interactive or it has the right throughput in case it works in batch.
[576.84 --> 587.60]  All the way to if you're going to deploy it in the cloud, make sure that you find the right cost effect way of doing so with the right, you know, and also have the right reliability and the right expected behavior in deployment.
[587.60 --> 595.44]  Right. So in our opinion, by the way, is that model creation and model training does have its special place in the flow.
[595.52 --> 599.10]  I can I can understand why in ML Ops people, you know, think about those steps.
[599.10 --> 601.34]  But I think everything else comes after that.
[601.40 --> 609.14]  Like, how do you, you know, process a model into how to put a model in a container and how do you monitor that model in deployment?
[609.14 --> 611.88]  How do you build CI, CD integrations and so on?
[612.24 --> 613.80]  All of that should just be DevOps.
[614.14 --> 616.62]  You know, people are building and calling that ML Ops as well.
[616.76 --> 632.56]  I feel like it creates a lot of confusion because the way I think about machine learning models today, you know, if you really zoom out a million feet is they are an integral component of any intelligent application today, which is pretty much any application that we're excited about today is, you know, can be called an intelligent application.
[632.56 --> 640.94]  Right. So it has, you know, natural user interface, can recognize your voice, recognize gestures, it has rich media and it has machine learning components as an integral part of them.
[641.66 --> 644.40]  But machine learning models are not treated as any other piece of software.
[644.50 --> 648.70]  They're treated as this special thing that's just hard to deploy, hard to integrate and so on.
[648.74 --> 654.58]  And we need to get past that, I think, to improve the cadence of innovation of this intelligent application.
[654.58 --> 658.82]  So people don't have to treat machine learning models in any special way.
[658.92 --> 668.40]  And this colors a lot in how I and we see at OctoML, the value that we can add is really enable folks to treat machine learning models as if you were any other piece of software, right?
[668.52 --> 674.88]  You have no idea how relieved I am to hear you say that because that's like a huge hot button issue for me.
[674.88 --> 683.30]  I mean, that's like Daniel's heard me rant about this repeatedly over time is, you know, the model is just part of the software at the end of the day.
[683.52 --> 685.96]  You know, that's it's a model that's not is not usable.
[685.96 --> 700.70]  So, you know, as you're looking at deploying it out as as maybe MLOps kind of, you know, outgrows its its diaper and gets into the big boy pants of DevOps and actually like becomes part of the real world around it and usable.
[701.16 --> 702.28]  How is that changing?
[702.28 --> 712.04]  You know, we talked to a year ago and kind of had some of the same conversation, but I know this is a very fast moving ecosystem and the evolution at it.
[712.12 --> 722.78]  So can you talk a little bit about, you know, like, you know, I shudder to say it is MLOps is kind of growing up and is hopefully it gets further and further recognized, integrated into DevOps.
[723.14 --> 725.96]  How do you see that evolving over time into maturity?
[726.14 --> 727.28]  What does that look like to you?
[727.28 --> 740.98]  Great question. So I'd say that one thing that's changing fast that I think people are starting to understand or have some common view of what MLOps is, because if you ask 10 people what MLOps in this space, what MLOps is, you're probably going to get 12 answers, you know.
[741.10 --> 744.14]  So because some people are going to have multiple answers to that, too.
[744.50 --> 750.26]  Right. So I think there's clarity being brought there on what is it that should be have should have a different name.
[750.26 --> 761.32]  And, you know, if you allow me to be cynical for just a second, sometimes it's people like giving names to things because it makes it easier for you to grab attention from the investment community, you know, from from investors.
[761.32 --> 767.98]  It's easier to grab attention from folks that are more on the cool technology side and let's give a name to something that looks different.
[768.52 --> 774.36]  But I feel like sometimes you give a new name to something that already exists that you can just do better can cause a lot of confusion.
[774.36 --> 780.20]  Right. So and I think that there's some maturity just that's starting to happen on what people call MLOps.
[780.46 --> 789.72]  And I'm glad to see that most of it is going more and more towards, you know, how you deal with data and how you create models, because everything else I think should just be called DevOps.
[789.86 --> 791.80]  Chris, shouldn't even be called MLOps.
[791.92 --> 793.52]  We're building solutions, aren't we?
[793.58 --> 796.50]  We're building big solutions to solve real world problems.
[796.90 --> 799.12]  And these are all parts of that solution.
[799.60 --> 800.50]  That's right. Exactly.
[800.50 --> 809.10]  So and then to answer your I completely agree with that 100 percent and to answer your question more more directly, what I see changing even in that space is a couple of things like one.
[809.66 --> 819.12]  You know, say a year ago, there's a lot more emphasis on end to end fully integrated platform like platforms like you get SageMaker or you get, you know, Azure ML or some other big clothes.
[819.12 --> 827.96]  But now I think there is a lot more attention to best in class for each one of the steps in this flow and have clean, clean integration points.
[827.96 --> 835.02]  Right. So, you know, have tools to deal with data that has a clear integration point with how you move on to to to the training step.
[835.12 --> 842.38]  How do you move on to, say, network architecture search to how do you package the model and how do you actually monitor the model in deployments?
[842.38 --> 851.66]  And our where we sit in that flow is, again, and we have an API that allows you to, you know, we take a model as input and we produce your deployable artifact.
[852.04 --> 852.88]  There's a lot of evolution.
[853.04 --> 859.46]  And I can't talk about all the details because otherwise my marketing folks are going to be mad at me, but you're going to hear more about what we're up to soon.
[859.46 --> 862.32]  But basically, in a word, we're all about automation.
[862.48 --> 872.98]  So automating the manual steps of getting working software model from like, you know, your say your Jupyter notebook, right, your Python scripts and, you know, put it into a container that you can deploy.
[873.24 --> 875.32]  Right. So that's highly specialized to the hardware target.
[875.72 --> 881.04]  But once we do that, if you put this in the right format, you should be able to use your regular DevOps flows.
[881.28 --> 886.76]  Right. So if you have the right API, you can use GitHub Actions, for example, to do CICD on your model.
[886.76 --> 888.42]  As you change your model, you run through this flow.
[888.84 --> 893.64]  And then if you put in the right container format, you can use existing microservices to serve your model.
[893.86 --> 904.14]  Right. So and then if you also put this the right hooks for monitoring, you can collect data from these from these deployed models and put it in, say, in a data dog way of visualizing your data.
[904.44 --> 907.06]  You can put views on top of that to look at model behavior.
[907.06 --> 913.16]  So that means that I think a lot of the work being done in model monitoring today is really, really important.
[913.16 --> 917.04]  But I think it's less about the ML ops part of it of like, how do you collect the data?
[917.16 --> 927.14]  But it's more about how to abstract that way and find higher level behaviors for models that you should you should go and debug, because those things are different than how you debug software today.
[927.24 --> 929.76]  Right. So there was a very long answer to your question, Chris.
[929.82 --> 932.62]  I don't know if it was an answer. It was more like a quick tangent there.
[932.62 --> 942.60]  We are going to ship it. Three, two, one.
[943.08 --> 950.30]  I'm Karhal Azu, host of Ship It, a show with weekly episodes about getting your best ideas into the world and seeing what happens.
[950.76 --> 956.84]  We talk about code, ops, infrastructure and the people that make it happen like charity majors from Honeycomb.
[956.84 --> 960.10]  We act like great engineers make great teams.
[960.30 --> 961.76]  And it's exactly the opposite.
[961.94 --> 965.38]  In fact, it is great teams that make great engineers.
[965.80 --> 969.30]  And they finally win the founders of continuous delivery.
[969.64 --> 972.44]  Start off assuming that we're wrong rather than assuming that we're right.
[972.70 --> 975.32]  Test our ideas, try and falsify our ideas.
[975.48 --> 977.46]  Those are better ways of doing work.
[977.50 --> 979.74]  And it doesn't really matter what work it is that you're doing.
[979.88 --> 981.54]  That stuff just works better.
[981.54 --> 993.16]  We even experiment on our own open source podcasting platform so that you can see how we implement specific tools and services within changelog.com, what works and what fails.
[993.34 --> 997.40]  It's like there's a brand new hammer and we grab hold of it and everyone gathers around.
[997.48 --> 1001.28]  We put our hand out and we strike it right on our thumb.
[1001.50 --> 1005.64]  And then everybody knows that hammer really hurts when you strike it on your thumb.
[1005.72 --> 1007.00]  I'm glad those guys did it.
[1007.08 --> 1008.44]  I've learned something instead.
[1008.44 --> 1013.44]  I think that's a very interesting perspective, but I don't see it that way.
[1013.64 --> 1017.08]  It's an amazing analogy, but I'm not sure that applies here.
[1017.42 --> 1019.70]  Listen to an episode that seems interesting or helpful.
[1019.86 --> 1021.52]  And if you like it, subscribe today.
[1021.68 --> 1022.76]  We'd love to have you with us.
[1022.76 --> 1052.52]  So one thing I was thinking about, Luis, as you were talking about this sort of transition from MLOps to DevOps is just, I guess, the team dynamics that are at play here and the sort of human dynamics.
[1052.52 --> 1060.94]  And I'm just thinking like in my own experience with the teams that I've been on and working on AI models and different applications.
[1060.94 --> 1065.96]  There is this real sense that like you can do a lot with, like you say, GitHub Actions.
[1066.10 --> 1067.04]  I love GitHub Actions.
[1067.12 --> 1068.06]  I do so much with that.
[1068.44 --> 1077.86]  But like that sort of like onboarding into that for someone coming from like a PhD scientist route and they like have like no idea this thing exists.
[1077.86 --> 1078.20]  Right.
[1078.20 --> 1081.76]  And as soon as they find out, like they can, you know, they're smart.
[1081.92 --> 1088.88]  They can grab onto it and use it and figure out ways to use it or things like Datadog, like you're talking about other things out there.
[1088.88 --> 1107.30]  How much of this sort of confusion in the terminology and the workflows here is caused by this sort of mismatch of what teams are aware of and their sort of spheres of knowledge versus like actual functionality differences?
[1107.30 --> 1110.14]  Yeah, I know this is a great question.
[1110.38 --> 1121.04]  So I would say that, you know, a key aspect in the human and team dynamics today is that you have folks that create models, typically data scientists or some people call them ML engineers or data engineers.
[1121.04 --> 1125.24]  And then once they arrive at a model, they hand off to a team if the company is big enough.
[1125.24 --> 1125.44]  Right.
[1125.46 --> 1128.46]  That goes and, you know, turns that into the deployable thing.
[1128.54 --> 1128.72]  Right.
[1128.80 --> 1132.60]  So and that team is still special compared to the DevOps teams.
[1132.76 --> 1142.78]  OK, so these are folks that are more sophisticated engineers that understand machine learning, understand the tooling involved and then put the work and then put that in an art, in a format that you can actually go and deploy.
[1142.78 --> 1152.80]  And he writes that, you know, the tools for model deployment today are largely not super accessible to data scientists per se.
[1152.90 --> 1157.20]  They're more accessible to folks that are machine learning infrastructure, machine learning engineer.
[1157.28 --> 1159.16]  And I think this can also change, by the way.
[1159.16 --> 1175.74]  I feel like with the right tools, you should be able to get a data scientist to export, you know, their model into a well-defined container that contains a model that then you can hand off to an existing DevOps team and IT infrastructure that should not be specialized to machine learning.
[1176.14 --> 1176.26]  Right.
[1176.28 --> 1184.66]  So I think that step from a model to the thing that the existing DevOps teams and IT infrastructure could use, that can be automated.
[1184.66 --> 1191.46]  So and I think there's a lot of work to make that automated because it involves human engineering today, but fundamentally it can be automated.
[1191.74 --> 1194.42]  And once you do that, I feel like you make both things productive, right?
[1194.46 --> 1210.06]  Data scientists can focus on making the models and then the DevOps teams can focus and continue making their applications run well and integrate models if you were any other piece of software and bring best practices to machine learning deployment.
[1210.06 --> 1210.44]  Right.
[1210.54 --> 1210.76]  So.
[1210.76 --> 1215.92]  It's funny when you were when you were talking about that a little bit, I was thinking you're solving two problems.
[1215.92 --> 1224.28]  You're solving the problem that you're describing, but you're also solving the problem that these these data and development capabilities and organizations.
[1224.50 --> 1225.80]  It sounds like high school.
[1225.80 --> 1236.38]  You know, you have the jocks and you have the the nerds and you have different groups socially that are doing stuff and you're going to automate the whole thing and it's going to bring everybody together, which is a good thing.
[1236.56 --> 1238.64]  It's a it's a good thing in this world to do that.
[1238.64 --> 1250.26]  So I'm curious, as you were bringing everyone together, how does that change the dynamics for organizations working for these different individuals that have different functions right now?
[1250.44 --> 1254.52]  And they're often they're a little silo and they're trying to interact as you get those automations.
[1254.80 --> 1256.58]  It sounds like it'll make it more efficient.
[1256.76 --> 1257.94]  How does that look to you?
[1258.28 --> 1261.62]  What kind of workflow are you striving for as you as you achieve this?
[1262.10 --> 1262.54]  Good question.
[1262.66 --> 1264.66]  And again, this is all happening and maturing fast.
[1264.66 --> 1273.10]  Right. So our current view is that with the right automation, again, you could have the folks creating models do the best job they possibly can in creating the models that have the right properties.
[1273.62 --> 1280.52]  Right. So and then on the on the DevOps side, they can focus on continuing deploying models and deploying software the way they they do.
[1280.56 --> 1289.00]  And I think that the dynamics is going to change that in organizations wouldn't have to go and look for people that are actually specialists in both because that's the reality today.
[1289.00 --> 1296.96]  So this team in between, you know, folks that create models and folks that run the regular DevOps, these are people that understand, again, as I said before, understand machine learning.
[1297.40 --> 1305.02]  They understand the tooling around, you know, all the guts of, say, TensorFlow and PyTorch and what are the right libraries to use depending on the hardware target.
[1305.38 --> 1306.78]  What are the right compilers to use?
[1306.84 --> 1308.90]  For example, should you use TensorFlow IT for NVIDIA?
[1308.96 --> 1312.34]  Should you use TVM in case you don't have, you know, broader options of hardware?
[1312.34 --> 1319.18]  And then you have to do performance evaluation to make sure that you're getting the right performance from your model running on the on the chosen hardware.
[1319.48 --> 1321.36]  Often they have to make decisions about the procurement.
[1321.68 --> 1330.26]  So if you're going to deploy it in the cloud at reasonable scale, chances are that your model is going to have a line item on the budget because it's going to cost a lot of money to run at scale.
[1330.34 --> 1332.46]  So you have to go and understand what are the cost implications.
[1333.06 --> 1337.66]  And these are the kind of things that none of these teams are used to are to like it's not their strength.
[1337.66 --> 1340.04]  So DevOps don't understand enough machine learning to do that.
[1340.04 --> 1343.70]  And then data scientists don't understand enough of the systems aspects to do that themselves.
[1343.88 --> 1353.72]  So I think that the dynamics that's going to change is, you know, if we automate this right, you know, companies wouldn't have to go and look for this kind of people that are specialized, that understand this intersection.
[1353.92 --> 1354.06]  Right.
[1354.14 --> 1363.68]  So and I hope this is going to make it even more accessible for users to put models into production because they don't have to go look for people like that.
[1363.68 --> 1368.84]  They don't have to have the expert, the systems expertise coupled to machine learning to make use of machine learning.
[1368.84 --> 1372.70]  Yeah, this point about automation is a really key one.
[1372.88 --> 1381.48]  And I'm trying to find like other you may have some examples outside of the machine learning world where there's reasonable parallels.
[1381.48 --> 1385.92]  But I was just thinking about like cyber, something like cybersecurity or something like that.
[1385.92 --> 1403.16]  Like at a certain point, I think if you look at kind of the history of how things developed, you really like had to have very specialized people having very specialized knowledge to understand like what sorts of vulnerabilities are in my software cybersecurity wise.
[1403.16 --> 1408.04]  And to some degree, like those sorts of people are still very valuable and they have their place.
[1408.04 --> 1422.94]  Then you come along and there's like now systems like I was just looking at one called Sneak where it's like you can just run this automation suite on your software and figure out all the various vulnerabilities and like the open source packages and the dependencies that you're importing.
[1422.94 --> 1427.70]  And like where you're doing something wrong in terms of exposing this or that.
[1427.70 --> 1437.90]  And like that allows any kind of person that can stick that in a kind of DevOps workflow to be able to like enable better security for their application.
[1438.04 --> 1439.74]  Maybe not prevent everything. Right.
[1440.22 --> 1442.42]  But you certainly can do much better.
[1442.42 --> 1452.16]  And I wonder if I don't know if that's a good parallel for what you're talking about here, where some of these things are still at that stage where you really have to know about all of these granularities.
[1452.42 --> 1456.54]  But as automation kicks in, a lot of those things are going to be taken care of.
[1456.68 --> 1458.28]  Yeah, no, that's a fantastic analogy.
[1458.48 --> 1459.40]  Really fascinating, Daniel.
[1459.54 --> 1462.08]  So, yeah, I was thinking when you described it, I was thinking about Sneak exactly.
[1462.22 --> 1462.34]  Right.
[1462.34 --> 1473.34]  So, because, you know, a lot of the tools like Sneak can, you know, plug into your DevOps workflow and say whenever there's new code committed, you're going to kick off your, you know, static analysis to find for vulnerabilities.
[1473.86 --> 1481.30]  You're going to make sure that all the open source code used there has actually been vetted and has checked all of the security properties.
[1481.30 --> 1481.60]  Right.
[1481.70 --> 1487.62]  So and that automation, I think, brought, you know, a significant progress in producing secure code.
[1487.92 --> 1489.94]  The parallel there is valid.
[1489.94 --> 1497.54]  The only thing that I think is so different is that you have very, very different kind of people, like people writing, writing regular code today.
[1497.62 --> 1501.64]  They're subject to the flow, like Sneak would use to go analyze the code.
[1501.74 --> 1503.48]  They're typical software engineers.
[1503.76 --> 1503.96]  Right.
[1504.04 --> 1514.66]  So and then you have some you may not need a security engineer, but even if you did a security engineer, it still kind of thinks like a software developer, except that, you know, they know what all the best practices for security are.
[1514.66 --> 1522.32]  Right. So the kind of automation that we are talking about in machine learning, I think it's a it's deeper and different because of the following.
[1522.32 --> 1534.80]  So, first of all, the difference between somebody who can create models and somebody can write system software and can write software to go and deploy it is so much wider than what you typically have in between folks that worry and don't worry about security today.
[1534.80 --> 1540.52]  And then second, the kind of automation that's needed, it's still pretty deep.
[1540.52 --> 1554.08]  Right. So as you're saying, like, you know, if you're going to export your model from a Jupyter notebook to turn that into, you know, a workable piece of software that you can go and deploy requires a lot of manual software engineering that hasn't been automated yet.
[1554.08 --> 1568.46]  Right. So there's still a lot of work. And I think that kind of automation is not quite as well defined, I would say, and as as, you know, clean as the automation required going and analyze code for security vulnerability.
[1568.46 --> 1573.08]  So as you're talking about this, I'm kind of trying to visualize the description.
[1573.08 --> 1592.02]  And I'd like to ask you, can you give me kind of a concrete example of how this is evolving now that either would have been much harder like a year ago when we spoke last or or at least or maybe even not possible in the sense of given the constraints that most organizations are dealing with?
[1592.14 --> 1598.30]  It could be anything. But what's a typical use case that you feel that you're enabling at this point going into it?
[1598.30 --> 1613.68]  Good question. So let me let me give you one specific example. Suppose that you have a computer vision module in your application today because you're going to go and verify whether images don't have anything inappropriate in them when you upload to a blog interface, let's say.
[1613.80 --> 1618.12]  OK, so the way you do that today, you have to do it happening in the past.
[1618.12 --> 1626.56]  Like I'd say a year ago is to go and maybe you find a model, you're going to probably put quite a bit of work on this model to make sure that it's actually classifying appropriate content correctly.
[1626.66 --> 1631.50]  And so this is all done by the data scientists, data engineers, I would say, and machine learning creators.
[1631.68 --> 1633.52]  Let's let's use that label now.
[1633.52 --> 1637.58]  And then once you once you're right at the model, you have two options.
[1637.68 --> 1645.22]  You just go and say, you know what, let's just use the regular, say, PyTorch or TensorFlow serving mode and just hope that that's fast enough.
[1645.52 --> 1649.84]  If it's not fast enough, then you're probably going to hire a consultant to go and help you.
[1650.34 --> 1653.28]  OK, so you're probably going to hire, you know, go hire folks to do it.
[1653.28 --> 1671.34]  And now I think with tools that, you know, like, you know, TVM, some things that we're building and some other folks that are in this space as well, I'd say are essentially enables one to take that model and go through not just the default path and package with existing libraries that are not optimized for the hardware, but help you choose, you know.
[1671.42 --> 1671.68]  All right.
[1671.70 --> 1675.06]  If you're going to deploy in an Intel processor, what is the right libraries to use?
[1675.06 --> 1680.46]  If you're going to deploy in NVIDIA, should you be using a TensorRT compiler to generate a more performant version?
[1680.46 --> 1687.18]  And wrappers around it to go and run that for you and more easily produce a higher performant, you know, output.
[1687.34 --> 1690.04]  Even in the last year, that's already getting a lot easier.
[1690.32 --> 1697.86]  But even then, after that, you still have to get that output and put an interface around it that has just the right API to integrate in your application.
[1698.22 --> 1701.10]  And that's what we firmly believe that we can automate even that.
[1701.20 --> 1709.84]  Really just go from you upload your raw PyTorch or TensorFlow model to the service, and then you get a package ready to be deployed.
[1709.84 --> 1709.92]  Right.
[1710.40 --> 1712.12]  With the right interface that you define, right?
[1712.20 --> 1712.46]  Yeah.
[1712.58 --> 1720.32]  This might be like a sort of off-the-wall question, but I know also, Luis, that you do some teaching and lecturing and other things.
[1720.32 --> 1731.20]  And I'm wondering, like, in a lot of the workshops, even like the ones that I've taught at various places, a lot of the focus is on the sort of model creation pathway.
[1731.20 --> 1745.46]  And I find, like, increasingly the people that I interact with in industry, once they're sort of in a position, are really, like, not even aware of some of those components that you just talked about, right?
[1745.46 --> 1756.48]  Like, model optimization, like the different ways of serializing models, the different ways of serving models, like batch inference or other ways of applying models.
[1756.80 --> 1769.14]  And, yeah, I'm just wondering if you have any, you know, thoughts on is that true across the way that we're kind of bringing up the next generation of machine learning practitioners?
[1769.14 --> 1773.96]  And are there ways that we can maybe shift the balance a little bit?
[1774.18 --> 1775.10]  That's another great question.
[1775.26 --> 1791.12]  So, you're right that, you know, a lot of the way that folks are learning about machine learning today and getting started with it, you know, they're not thinking about model optimization deployment because, you know, luckily we actually create pretty good tools to arrive at models and test them and make sure that they have the right accuracy and has the right properties.
[1791.58 --> 1795.38]  But chances are that most of those models created wouldn't actually see deployment.
[1795.54 --> 1797.16]  They wouldn't make it to deployment, right?
[1797.16 --> 1802.50]  So, it's good for people to learn, but chances are they wouldn't be deployable.
[1803.00 --> 1806.16]  And honestly, I want it to stay that way even for the sophisticated users.
[1806.44 --> 1807.62]  So, let me talk about the other users.
[1807.70 --> 1816.12]  These are folks that have already done this for a while and now they are improving models in a significant way because they're doing things that haven't been done the way they wanted before, right?
[1816.58 --> 1821.32]  Today, people already have to start worrying about performance too early.
[1821.46 --> 1825.12]  They have to like, okay, if I make this change in my model, am I going to be able to deploy it?
[1825.12 --> 1827.92]  You know, if I go deploy, should I deploy these CPUs or GPUs?
[1827.98 --> 1829.84]  And so, like people should not worry about this.
[1830.14 --> 1841.48]  I want human power, like I want human creativity and ingenuity to go into making a better model and not have to worry about systems aspects too early because that's going to constrain the way they see the model, right?
[1841.48 --> 1849.52]  It's as if like as you're designing, you know, a new feature for a car, you're all thinking about all the sorts of different ways it's going to be used like too early.
[1849.62 --> 1856.34]  And then you're not innovative enough because you get constrained by practicalities before you're able to unlock your creativity, right?
[1856.34 --> 1860.66]  So, I like what, if you don't mind, I just go on a quick side comment.
[1860.74 --> 1869.72]  It's like, I like where Hugging Face is going where it makes it very easy for folks to go start from an existing model, make, you know, modifications from a foundation model, right?
[1869.74 --> 1871.86]  They talk about it and then specialize specific use cases.
[1872.16 --> 1875.86]  And then you don't have to worry about, you know, some of the systems details yet.
[1876.16 --> 1883.24]  When you actually put into deployment, chances are you're going to have to worry about it because performance is going to come and bite you if you don't.
[1883.24 --> 1891.08]  But at the conceptualization stage and model creation stage, I don't think people should worry about details of how these models are going to be implemented, right?
[1891.12 --> 1892.74]  So, I want it to stay that way.
[1893.02 --> 1896.90]  But I want it to stay that way and still allow these models to actually be deployed, right?
[1913.24 --> 1922.38]  So, I'd like to follow up.
[1922.44 --> 1934.24]  It's actually kind of combining what you were just addressing with Daniel's previous question a little bit because the two of you together really got me thinking about a different way in that sense.
[1934.24 --> 1946.08]  And that is, you know, even now with all the model creation and all the detail on that, and yet that's not an industry, you know, we're doing, we're using foundation models and there's a lot of transfer learning.
[1946.40 --> 1949.46]  And typically students aren't doing this off the bat.
[1949.58 --> 1953.26]  They're kind of going through it the hard way to teach the stuff.
[1953.50 --> 1959.04]  But then they get into industry and they're struggling because they only have a narrow focus of the picture.
[1959.04 --> 1973.60]  So, as you're doing this work and as Daniel brought that point up, I'm wondering, does it make more sense then to, by using these kind of tools, to get more of an end-to-end learning process going?
[1974.30 --> 1986.12]  And you're, by providing the right ecosystem and tooling as you're doing, you're essentially saving them from wasting what creativity they have on the wrong thing because you're kind of helping them through that.
[1986.12 --> 1993.00]  But at the same time, you're crucially helping them understand the full end-to-end workflow on how to get it out there.
[1993.16 --> 1997.36]  Is that the way of teaching AI going forward in your view?
[1997.76 --> 1997.86]  Yeah.
[1997.96 --> 2008.68]  So, I'm so glad you brought this up because when I said that they shouldn't worry about all the practicalities of deployment, I meant that they shouldn't be constrained, but they should still have an idea of what would it take to take their models into production.
[2008.68 --> 2013.08]  And the more automated we make that, the more in the loop of model creation you can put it.
[2013.12 --> 2021.84]  For example, like, you know, succeeding where we want to be on taking models, you know, fresh models and deployable artifacts, evaluated benchmarks and so on.
[2022.08 --> 2028.06]  If you make that fast enough and productive enough, you can actually put this in the active loop of as people are developing models, they can just go and try them out.
[2028.06 --> 2034.66]  Right. So, but not like the way it is today where I have to think about is it a CPU or GPU, what kind of GPU and then go and benchmark.
[2034.80 --> 2040.10]  Like if it's just completely automatic and seamless, you can always get for all the versions of your models as it evolves.
[2040.10 --> 2046.94]  You can see how, you know, how well this model will do in production and in various scenarios and just during model creation.
[2046.94 --> 2056.64]  Right. So think of it as an outer, outer loop of what they call network architecture search, even outer loop from that is just like for all the candidates models for what I'm thinking about doing.
[2056.74 --> 2061.82]  Just give me an idea of how well this this way of thinking about the original model would do in production.
[2062.32 --> 2068.24]  If you don't mind me, add one more thing that's not related to what you talked about, Chris, but you made me think of another thing that we've been observing that I think is interesting.
[2068.24 --> 2073.10]  Even though we're talking about a model, say model A or model B and how to take that model to production.
[2073.56 --> 2077.72]  The reality is, as we're talking about models are integral part of applications.
[2078.22 --> 2083.46]  Right. So of bigger applications. And it's not just a single model, by the way, it's all an ensemble of models.
[2083.52 --> 2092.82]  You have computer vision, you have language and you have like decision trees and you all combine this ensemble of models that they might talk to each other directly because there's a data flow from model A.
[2093.06 --> 2095.36]  Output of model A could go to input of model B.
[2095.36 --> 2103.70]  But also, even if they don't, chances are they're actually in a package running some machine in some container in the cloud that interact with each other because of performance.
[2103.82 --> 2111.22]  And like these are all system aspects that we have to worry about because in the end, you're going to have to package all of these into modules that you can actually deploy. Right.
[2111.40 --> 2112.74]  That's a great point you're making.
[2113.08 --> 2116.10]  The ensemble of models is something that's important. Right. So, yeah.
[2116.10 --> 2125.06]  As you're talking about these things and, you know, going from this sort of ensemble and systematic thinking and these things interacting with each other,
[2125.48 --> 2130.42]  I'm wondering about some other jargon that has come up on the show in the past.
[2130.42 --> 2135.16]  And it's, I think, related to some of this automation and workflow sorts of things.
[2135.16 --> 2139.82]  And that's this sort of low code, no code type of type of stuff.
[2139.82 --> 2148.36]  There's increasingly this like messaging around like we're making AI and machine learning systems, low code, no code, etc.
[2148.36 --> 2157.40]  And, you know, I have maybe my own sort of opinions on where we're at on that spectrum and where things could go or might go.
[2157.40 --> 2175.02]  So I was wondering, you know, maybe your perspective on that and like how far can we push the automation aspects and the things that are where are the machine learning engineers and the DevOps engineers really going to sink their teeth into the lower level like code?
[2175.02 --> 2184.44]  And where are those opportunities really for the like low code and automation pieces that are maybe a little bit hyped at the at the moment?
[2184.44 --> 2187.46]  Yeah, so good, good points and juicy, juicy topics.
[2187.46 --> 2206.14]  So I would say that for model creation, I see a path to low code, no code, and it's kind of going that way, at least low code, I can see, I can see a path because there's ways of you, you know, defining the data set, you know, how partition it, their tools now to better label the data and create that it is all has very little to no code.
[2206.32 --> 2211.90]  And then when you think about classes of models, you can imagine just being a high level choice and not a programmatic thing that you write in a piece of code.
[2211.90 --> 2229.02]  And I, I see a path there. But now from that to deployment, I have a harder time, I can see, you know, some code, I don't call it low code, because you still have to figure out like, okay, what is the API again, going back to thing that we keep repeating every five minutes, like models being part of applications, right?
[2229.02 --> 2243.64]  So, you know, they still have to define an API is going to call that model. So, and then to be part of the rest of the application. So that part, I still feel like, again, maybe the rest of the code is already we succeeded. And all of that is already low code and no code. I don't know if that's going to be the case.
[2243.64 --> 2250.64]  But you have to have very, very well defined API for that to work. And that involves some significant amount of code fundamentally, in my view.
[2250.64 --> 2280.64]  And then there's some some other aspects that when you actually taking a model to, to deployment that you have to think about that, you know, I think are important, like, for example, is it latency sensitive, or is it throughput? Like, for example, is it, you know, are you going to care about how long each prediction each inference takes? Or you're going to care about, oh, if I do overall this piece of bucket of data, that you're going to have the right throughput, right? So, and these are things that, you know, you have a lot deeper systems thinking
[2280.64 --> 2289.34]  low code, it still requires a lot of deep understanding of what you're doing, that in the by that time, you're going to require specialized people, that doesn't really matter what it's low code or no code, right? So
[2289.44 --> 2307.10]  I got a follow up. And that would be, you know, if we go back to addressing kind of the low code, no code approach to model creation, and or more specifically, optimization, you know, there are a lot of kind of known things. And you could actually, you know, you can train a model to do the optimization along those lines. And so and we're seeing that
[2307.10 --> 2310.42]  great auto NAS, auto ML works finally happening, right? Yeah.
[2310.42 --> 2335.84]  Yeah, I'm wondering if, you know, one of the challenges is, is we're addressing deployment and recognizing that, you know, people focused for a while on model creation way more than than getting the model out there in a usable fashion, and that we're, that we're getting mature about that now, your organization, and there are others out there, too, that are thinking very deeply about this. Do you think that there's an opportunity for maybe low code, no code approaches,
[2335.84 --> 2365.28]  once that we arrive at more kind of standardization, right now, it's still very early, it feels like, in terms of, of different approaches, so there's a real custom feel to how you're going to deploy, especially when you combine it with all sorts of edge targets with edge being a catch all phrase that could be almost anything. And so there's a ton of specificity to your target at this point. Do you think over time, as those get categorized, and kind of best practices emerge,
[2365.28 --> 2372.78]  that there might be more opportunities? Or do you think that's still going to be a challenge given some of the API concerns and such that you mentioned in your previous answer?
[2373.18 --> 2394.50]  Yeah, I would say that once, again, once how the model is used in an application as well defined in APIs, et cetera, then we're talking about more the evolution of the model, I can see, I can see that being very low, you know, low to no code, because by that time, we've already seen a path to deployment, if you find the box where it fits in, and then I can see the model evolving and having very little code for the model,
[2394.50 --> 2408.76]  for the model updates. And to your point specifically, like if you're going to deploy it on the edge, and you have to see how it works on a wide variety of devices, I also see a path to automation to say like for this model that you created, it's going to work on 85% of the phones, for example.
[2408.76 --> 2421.50]  I think we, you know, going where automation is going, you know, having the ability to benchmark it across all sorts of scenarios where the model is going to be deployed and validate that it's going to work across the set of devices where you care about.
[2421.70 --> 2431.82]  I can imagine a feedback loop with the model creator that says like, okay, for this decision that I've made, it's going to work on these classes of devices, you know, it's a great point. Like it made me visualize that in a clean way.
[2431.82 --> 2438.52]  I can, I can see that happening. But again, only after you've defined where the model fits in the larger application, right? So.
[2438.94 --> 2444.26]  I'm relieved to hear that because I work in an industry where absolutely everything that we target would be on the edge.
[2444.72 --> 2445.00]  Oh, yeah.
[2445.20 --> 2445.62]  Yeah, yeah.
[2445.62 --> 2451.84]  And so if you hadn't given me some hope right there, I was going to start crying on you on that. So thank you. I appreciate that.
[2451.98 --> 2464.58]  I always like to, you know, step back and think about models being part of a bigger application. You know, that big application was written by someone. I had to put a lot of things, by teams, right? They had to think clearly about where is the model going to fit, right?
[2464.58 --> 2471.50]  So once that is defined, I can see a lot of, a lot of the rest being, being automated and being very low, low to no code, right?
[2471.58 --> 2480.88]  So I think that, you know, one, one, you know, way of actually summarizing this, if we nailed how to turn models, trained models, right?
[2480.94 --> 2489.20]  And by that point, you can do this in low to no code into like this agile, performant, reliable pieces of software that you can integrate throughout application.
[2489.20 --> 2507.74]  Once we all nailed that automation, you know, everything's going to get easier, in my opinion, you know, managing applications and also creating better models, because then you have separatial concerns the way that I think needs to be done here, given that machine learning folks are going to think, creators are going to think very differently than the hardcore software engineers that are on the other side of the application building, right?
[2507.82 --> 2510.24]  So we want to make sure it stays that way, right?
[2510.24 --> 2525.64]  Yeah, so maybe as, as you look at, hopefully that future, what is your sense of like, over the next, you know, the next year, when we have you back on the show a year from now?
[2525.86 --> 2536.66]  What are those things that you would really hope that like, are maybe enabled that aren't at the moment and are but are sort of achievable within that kind of timeframe?
[2536.66 --> 2558.68]  Yeah, so I would say, again, being able to get a model that was freshly created by, you know, a data scientist or machine learning without thinking about systems, systems aspect of deployment, you know, having their models benchmark, benchmark, knowing how it runs, you know, know how much it costs, and going to click deploy, it's going to produce a box that the DevOps folks can go and deploy into the application.
[2558.68 --> 2565.80]  I think we have line of sight to that. And I hope next year, in the show here, we're going to be talking about all the ways that people are using, are using that.
[2566.22 --> 2581.62]  But now if you ask me to think about what about five years out, I think what's interesting to think about here is that, how do you even stop thinking about what's edge, what's what's in the edge, what's in the cloud, what runs where, and just think about, hey, I want to solve this problem that involves machine learning.
[2581.62 --> 2599.16]  And yes, so users are on the edge, computers are in a building somewhere spread all over the world, right? So, and I think a systems, an application creator, like, I don't want to use the word developer, an application creator here should say, should be able to specify, here's what they want to do.
[2599.16 --> 2612.44]  And then the system should automatically figure out, okay, so we need this kind of models, and this model, this one should run in the edge, this one should run in the cloud, this one should might run in a cell phone base station, and automatically split what should run where, that should be done automatically.
[2612.44 --> 2622.26]  Because again, that's an optimization problem that once you define the constraints, you should be able to place the right piece of your model in the right physical place automatically.
[2622.26 --> 2629.96]  And if we nail the automation that we just talked about, from a model to the thing that runs in the hardware really well, that part is already also done, right?
[2629.96 --> 2638.98]  So now we can go and work on a higher level problem, like how do you break down your model into the pieces of what's in the edge, what's in the infrastructure, what's in the cloud, just the right way.
[2639.10 --> 2642.14]  I also think that that should be possible, right?
[2642.22 --> 2645.06]  So because, hey, we have machine learning designing chips today.
[2645.18 --> 2646.54]  That's pretty hard, right?
[2646.54 --> 2653.46]  So you have machine learning designing, you know, much better ways of doing, you know, power management in large scale data centers.
[2653.66 --> 2657.72]  These are all low level things that we used to do by hand or with heuristics, right?
[2657.76 --> 2658.98]  And we abstracted that away.
[2659.72 --> 2670.24]  As this goes up and up the stack, I'm very excited about the future of creating exciting applications without having to worry about all the design constraints that we have to worry about today.
[2670.24 --> 2671.16]  Awesome.
[2671.48 --> 2671.66]  Yeah.
[2671.84 --> 2675.06]  Well, I'm very excited about that future.
[2675.06 --> 2678.38]  And as always, it's a pleasure to talk to you, Luis.
[2678.58 --> 2682.96]  And I'm really excited by the things that you and your team at OctoML are doing.
[2683.50 --> 2690.98]  Make sure and listeners, make sure and check out the show notes for some links to some really great stuff, both for TVM and for OctoML.
[2691.34 --> 2693.38]  And yeah, thank you again for taking time, Luis.
[2693.60 --> 2694.34]  It was a pleasure.
[2694.74 --> 2695.20]  Thank you, Daniel.
[2695.30 --> 2695.82]  Thank you, Chris.
[2695.84 --> 2696.48]  Always a pleasure.
[2696.56 --> 2699.94]  And again, looking forward to coming back and talking about all the other new stuff the next year.
[2700.06 --> 2701.10]  So thank you.
[2701.36 --> 2702.10]  You guys are fun.
[2702.10 --> 2702.54]  Bye.
[2703.42 --> 2703.62]  Bye.
[2705.06 --> 2706.06]  Bye.
[2712.38 --> 2713.22]  All right.
[2713.38 --> 2715.36]  That is Practical AI for this week.
[2715.66 --> 2723.94]  If this is your first time listening, subscribe now at PracticalAI.fm or just search for Practical AI in your favorite podcast app.
[2724.04 --> 2724.66]  We're in there.
[2724.96 --> 2728.16]  And if you're a longtime listener, please do share the show with your friends.
[2728.36 --> 2731.12]  It is the best way you can help Practical AI succeed.
[2731.12 --> 2737.48]  Thanks again to Fastly for shipping our shows super fast all around the world to Breakmaster Cylinder for the Beats.
[2737.76 --> 2738.68]  And to you for listening.
[2738.90 --> 2739.62]  We appreciate you.
[2739.96 --> 2741.06]  That's all for this week.
[2741.22 --> 2742.32]  We'll talk to you again next time.
[2742.32 --> 2744.12]  Champions of the Beats.
[2744.18 --> 2745.90]  Check.
[2746.04 --> 2746.58]  스트�ial.
[2746.58 --> 2747.26]  Enter.
[2747.36 --> 2747.88]  Stay.
[2747.96 --> 2748.82]  Stay.
[2748.88 --> 2749.38]  Stay.
[2749.44 --> 2750.06]  Stay.
[2750.66 --> 2751.10]  Stay.
[2751.18 --> 2752.04]  Stay.
[2752.04 --> 2752.82]  Stay.
[2752.92 --> 2753.56]  Stay.
[2753.94 --> 2754.48]  Stay.
[2754.48 --> 2754.70]  Stay.
[2754.92 --> 2756.94]  Stay.
[2757.64 --> 2758.02]  Stay.
[2758.12 --> 2758.74]  Stay.
[2758.82 --> 2758.94]  Stay.
[2759.00 --> 2759.02]  Stay.
[2759.18 --> 2760.18]  Stay.
[2760.30 --> 2760.96]  Stay.
[2760.96 --> 2761.32]  Stay.
[2761.64 --> 2762.92]  Stay.
[2765.02 --> 2766.94]  Stay.
[2767.30 --> 2767.70]  Stay.
[2767.70 --> 2767.94]  Stay.
[2768.00 --> 2768.22]  Stay.
[2768.28 --> 2768.32]  Stay.
[2768.46 --> 2769.02]  Stay.
[2769.02 --> 2769.54]  Stay.
[2769.54 --> 2770.02]  Stay.
[2770.02 --> 2770.44]  Stay.
[2770.44 --> 2771.04]  Stay.
