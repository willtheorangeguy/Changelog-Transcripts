[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.36] on Linde servers. Head to linode.com slash changelog. This episode is brought to you by
[17.36 → 23.72] DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 → 29.18] Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 → 34.74] their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 → 42.68] R, Jupyter Notebook, TensorFlow, Sci kit, and PyTorch. Use our special link to get a $100 credit for
[42.68 → 51.30] DigitalOcean and try it today for free. Head to do.co slash changelog. Once again, do.co slash changelog.
[59.18 → 68.60] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 → 74.52] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 → 78.66] and data science happen. Join the community and snag with us around various topics of the show
[78.66 → 84.48] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 → 92.50] Well, welcome to Practical AI. Hey, Chris, how's it going, man?
[92.62 → 93.80] Pretty good. How are you doing, Daniel?
[94.16 → 99.24] Doing perfect. I'm really happy today with the conversation that we're going to have because
[99.24 → 107.48] we're going to be talking to my old colleague and still great friend, Joe Doline, or as I call him,
[107.54 → 108.80] JD. Welcome, Joe.
[109.28 → 112.78] Hey, Dan. It's great to be here. And hey, Chris, it's great to meet you on your show.
[113.00 → 113.84] Great to meet you too.
[114.20 → 116.94] Yeah. Thank you so much for joining us.
[116.94 → 118.14] Thank you for having me.
[118.38 → 122.74] Yeah. Why don't you give us a little bit of background about what you're currently involved
[122.74 → 124.34] with and how you got there?
[124.66 → 131.84] Yeah, absolutely. So as you said, I'm Joe Doline. Everyone calls me JD. I am the CEO and founder of
[131.84 → 137.38] Picketer, which is a company that builds data science tools that we'll be talking about today.
[137.94 → 143.84] Before that, I've worked at a number of startups. Probably the most relevant one to this conversation
[143.84 → 149.16] is that I also worked at Airbnb as a data infrastructure engineer, basically just
[149.16 → 155.26] managing their AI and data infrastructure for the company. And so I have a lot of experience
[155.26 → 161.50] on the infrastructure side of data science, less so as an actual practitioner. And so that's most of
[161.50 → 162.76] what we're going to be talking about today.
[163.14 → 168.90] Awesome. Yeah, that's a perfect setup. I think that we've done a lot of talking about AI,
[168.90 → 173.06] but we really haven't got into a ton of infrastructure stuff yet, I don't think. Have we,
[173.18 → 173.60] have we, Chris?
[173.86 → 180.52] Not really. And it's, I think this is an episode long overdue. And it's just to note to the listeners,
[180.66 → 186.24] I know you had said that you had previously worked with JD at Pack Durham. I have not
[186.24 → 190.50] familiar with Pack Durham as a newbie. So it'll be an interesting conversation for me
[190.50 → 194.84] having a couple of experts on here. And I'm going to, I'm going to, I'm going to ask all the stupid
[194.84 → 202.56] questions. Okay. Well, I, you know, he's not my inside man. Dan might be, but Chris definitely isn't.
[203.58 → 208.92] Yeah. Yeah. Full disclosure. I might be a little bit biased, but only I don't officially work for
[208.92 → 214.32] Pack Durham anymore. Although I am a huge fan, I am actually using Pack Durham on my current project.
[214.32 → 220.00] So I'm a huge fan and have that bias, but I'm, I'm excited to dive into the details and,
[220.08 → 222.40] and have you learn a little bit more too, Chris.
[222.40 → 226.24] Yep. Absolutely. Over the time that we've known each other since we first met and,
[226.28 → 229.80] and you've been talking about it, I've adopted it. I have a long way to go to catch up to where
[229.80 → 233.44] you guys are in terms of using it as a tool, but as a beginner, it's definitely something I'm
[233.44 → 237.48] interested in. So I can't wait to hear more from JD. Definitely. Yeah. So with that, JD,
[237.58 → 243.50] why don't you give us just kind of high level overview of what Pack Durham is and kind of the
[243.66 → 249.94] the needs that it's fulfilling or, or what it's trying to do for data scientists and people working in
[249.94 → 255.92] machine learning and AI? Yeah, absolutely. So Pack Durham is basically designed to be all,
[256.14 → 260.76] everything that you need to do high level production data infrastructure in a box.
[260.76 → 265.74] And so what that means, if you're used to, you know, doing AI workloads in, you know,
[265.88 → 270.30] Jupyter notebooks on your laptop, or maybe just in Python directly using something like TensorFlow,
[270.80 → 274.58] something like that. Pack Durham is not in any way saying that you should stop doing that.
[274.58 → 281.24] Pack Durham is just giving you a way to take that code and deploy it on the cloud in a distributed
[281.24 → 285.56] fashion so that you know, it's going to run every single night or, you know, hook it up with its
[285.56 → 290.26] processing steps so that you can have everything sort of going in a pipeline end to end. And this
[290.26 → 295.94] is what companies turn to when they sort of need to make that leap from a model that's on somebody's
[295.94 → 299.94] laptop to something that's like a core part of their business that's going to run every single
[299.94 → 305.98] night. This sort of all came out of my experiences at Airbnb, where I was basically trying to make a
[305.98 → 311.74] platform that did that for our data scientists. And while I was working there, I had a couple of
[311.74 → 317.06] sort of novel ideas for what I thought that the world of data infrastructure was missing, and what
[317.06 → 322.98] I wanted to bring to it. So the first unique thing that we did with Pack Durham is, you know,
[322.98 → 327.28] we needed a way to store data. So we have a distributed file system, it's called the Pack Durham
[327.28 → 331.60] file system. If you're familiar with the Hadoop ecosystem, this is probably something pretty
[331.60 → 337.20] similar to HDFS or Tachyon or something like that. What's different about our file system is that
[337.20 → 343.38] it's capable of version controlling large data sets in addition to storing them. And so you can have,
[343.44 → 348.62] you know, your training data set, it can be terabytes of data, and this data is constantly coming in from
[348.62 → 354.16] your users on a website from satellite imagery or something like that. And the Pack Durham file system
[354.16 → 358.68] will actually give you discrete commits like in Git, where you can see, okay, this is what my
[358.68 → 362.78] training data set looked like a week ago, this is what it looked like a month ago, and things like
[362.78 → 369.06] that. And what's really important for AI, that is not only do we keep these different versions,
[369.38 → 375.22] but we actually link them to their outputs using a system that we call provenance. And so at any time
[375.22 → 380.52] when you've trained a model in Pack Durham, you can ask the system, what is the provenance for this
[380.52 → 385.06] model? And it'll trace you back to all the different pieces of training data that went in
[385.06 → 389.08] it into it, and all the different pieces of code that went into training this model so that
[389.08 → 393.36] you can basically see where it came from, and you can reproduce your results. Does that make
[393.36 → 398.46] sense to you guys? It does. I'm going to dive in since I'm the newbie on this and ask. Please do.
[398.84 → 405.06] So kind of, and I'm asking this on behalf of the listeners and partly for myself. First,
[405.06 → 411.60] quick question. Is it a proprietary system? Is it open source? This is all open source. We do have
[411.60 → 416.70] an enterprise system that goes on top of it. And I'll talk to you later about what features
[416.70 → 420.48] are limited to the enterprise system. But nothing that I've talked about up until this point is in
[420.48 → 425.48] that this is all open source, so you can download it yourself. Okay, and to kind of wrap our heads
[425.48 → 430.02] around it a little bit, you kind of mentioned the file system and versioning and this what sounds
[430.02 → 433.72] like a kind of feature called Providence where you can go back and do that. Could you kind of
[433.72 → 440.14] describe for someone who has never heard of Pachyderm kind of what the feature set is and what kind of
[440.14 → 445.16] a typical use case might be so that in their own shop where they're doing data science, they can kind
[445.16 → 449.88] of figure out how it fits in with what they're already doing? Yeah, yeah, absolutely. So I think
[449.88 → 455.98] it's I think it's easiest to sort of focus in on a use case here. So one that I can talk about very
[455.98 → 462.50] publicly because it was a public competition was the Department of Defence was until recently running a
[462.50 → 468.96] competition, where they were basically having people write image detection algorithms for
[468.96 → 474.54] satellite imagery that they had, right? So they had a bunch of satellite images that they had taken,
[474.74 → 479.50] and they wanted people to write models that would detect this is a hospital right here, this is a
[479.50 → 486.08] school, this is a bus, things like that. Interesting AI problem, also an interesting architecture problem
[486.08 → 490.76] for them, right? Because they have people just basically throwing code at them through this web
[490.76 → 495.32] interface. And they need to take that and run it through their pipeline and get results out the
[495.32 → 500.38] other end and give those to the users. So the way that they set that up in Pachyderm is first, they
[500.38 → 506.86] spun up an instance of it, and they deployed it on AWS, they used as the backing store, they use S3. So
[506.86 → 511.24] ultimately, all of this was stored in object storage, which made it very, very easy for them to manage.
[511.50 → 516.12] And then they loaded all the satellite images into the Pachyderm file system. And so that's,
[516.28 → 519.70] you know, you can get stuff in there in a number of ways, you can get it in there directly from
[519.70 → 525.08] object storage, you can push it over HTTP. I'm not sure exactly which one they used. But from there,
[525.08 → 529.32] they now had a system where all the data was just sitting there in different versions, they could
[529.32 → 534.64] update it and have a new version. And then anytime that a user's code came in, they just deployed a
[534.64 → 539.40] new pipeline on Pachyderm. And that would then slurp up all of those images and process them in
[539.40 → 543.62] parallel. And out the other end, after some processing would come just a score report that they
[543.62 → 548.42] could report back to the user. And that might include your code failed on these five images,
[548.42 → 552.90] so you don't get a score, or it might be your code succeeded on these five images. And here's
[552.90 → 556.38] how accurate you were. And it would get them full reports about like, here's what you did well on,
[556.44 → 559.64] here's what you didn't do well on, things like that. Does that answer your question? Or do you
[559.64 → 562.30] want to know more about sort of specific features within Pachyderm?
[562.74 → 567.62] No, that that does help a little bit, I guess, I guess, as a follow-up, you talked about file system
[567.62 → 572.20] and its ability of versioning. Are there any other kind of high level, like key things that you want to
[572.20 → 576.02] name that you really can't use Pachyderm without considering those features?
[576.02 → 582.80] So in terms of the file system, that really basically covers it. It does basically all the
[582.80 → 587.62] standard things that you'd expect from a distributed file system, plus the versioning
[587.62 → 592.30] and provenance component. And that's really the only quirk to it. Now, on the processing side,
[592.46 → 599.10] things also start to get interesting. And here is where we need to start introducing maybe a few
[599.10 → 605.34] jargon words that I will explain. So one of the sort of key things that we use in Pachyderm is
[605.34 → 609.92] containers. And I'm sure most listeners at this point have heard of the company Docker,
[610.14 → 613.88] which has been a very successful Silicon Valley company. And they make this thing called a container,
[614.36 → 619.84] which is basically just a standard way to ship around code, right? Think of the problem that
[619.84 → 626.00] you've had where, you know, you write some script in Python that trains a model, then you send it over
[626.00 → 629.48] to your friend, and they've got the wrong version of Python, or they've got the wrong version of
[629.48 → 632.42] TensorFlow installed or something like that. And it's all incompatible.
[632.42 → 638.16] A Docker container is a way to ship code that's going to work anywhere, regardless of what the
[638.16 → 642.54] user has got installed on their machine, or regardless of within the cluster. Pachyderm's
[642.54 → 648.06] processing is all built on Docker containers. And so what that means is that you as a data scientist,
[648.60 → 653.80] when you want to productionize your code and take it off of your laptop and into the cluster,
[654.32 → 658.14] then all you need to do is package it up into a Docker container, which means that there's
[658.14 → 663.04] a little bit of a learning curve there to understand the tooling of Docker. But once you've got that,
[663.26 → 668.16] you as a data scientist are now completely in control of the environment that your code runs in,
[668.18 → 672.66] and all the dependencies and everything like that. And so once people grok this, it's actually
[672.66 → 678.04] very, very liberating. And the reason that I wanted to build this on top of containers was because
[678.04 → 683.14] when I was at Airbnb, we would have these problems all the time when a data scientist would come to
[683.14 → 687.92] me, and they'd written some new piece of processing that they wanted to be in the company's pipeline,
[688.44 → 691.58] could be a machine learning model, or could just be something as simple as data cleaning,
[692.00 → 695.48] or something like that. And they would send me the Python script. And then I would realize,
[695.62 → 699.64] oh, this isn't quite compatible with what I've got on the cluster. And we didn't have Docker
[699.64 → 705.12] containers there. We just had one big monolithic cluster. And so if we didn't have the right versions
[705.12 → 710.18] of Python installed, I actually would have to either redeploy the entire cluster just to run that one
[710.18 → 716.36] user's code, which was very untenable, or I would have to have them change their code to use different
[716.36 → 720.08] versions, things like that. And so it was this constant back and forth where the data scientists
[720.08 → 723.66] couldn't quite use the tools they wanted. Our infrastructure people couldn't quite like
[723.66 → 728.50] maintain a cluster with a consistent set of tools. And so I had this aha moment when I realized if
[728.50 → 733.30] these guys could just use Docker containers, then this impedance mismatch would totally go away.
[733.44 → 736.28] And we could both do our jobs a lot more easily. Does that make sense, Chris?
[736.28 → 741.08] I was just going to say it like following up on that. So it's kind of like whether you're
[741.08 → 748.76] using Python or R or, you know, Java or whatever the different tool you're using is or the language
[748.76 → 754.82] you're using, essentially, these containers unify the way that you treat each processing step.
[754.88 → 757.30] Would that be an accurate way to see or to say it?
[757.54 → 762.66] Absolutely. Yeah. So it allows us to basically handle the infrastructure the same way,
[762.66 → 766.08] no matter what code it's written in. And so we have a lot of companies where
[766.08 → 770.70] one of the things that's really appealing about Packard is that they all of their data scientists
[770.70 → 776.40] just know different languages. And they're looking for some sane way to have everybody writing code in
[776.40 → 780.92] their own language and pull it, tie it all together into a system that they can understand.
[781.36 → 784.74] And Packard allows them to do that. Now, the key thing about this, of course,
[784.74 → 789.72] is that because we have the provenance tracking, like you can still see the fact that like, oh,
[789.72 → 793.24] this data came followed through all of these steps and came out the other end,
[793.24 → 797.76] even though like one step was Python, one step was Ruby, one step was Java, one step was C++.
[798.38 → 802.80] And you didn't have to write any special tooling within those languages to track the data.
[803.16 → 808.64] Yeah, that's awesome. So I'm going to kind of pose a problem. I want to see if you would kind of go
[808.64 → 813.80] about things the same way as I would, JD. So let's say that we have a, you know, we have a Jupiter
[813.80 → 817.64] notebook. And I like how you kind of brought that up before, because that's where a lot of data
[817.64 → 822.68] scientists kind of start out. So let's say that Chris and I have been working on this Jupiter
[822.68 → 830.00] notebook that has some pre-processing for images. And then we train a particular model, let's say,
[830.16 → 836.26] in TensorFlow, and then we output results and then maybe do some post-processing. And to test it out,
[836.32 → 841.94] we've just kind of downloaded like a sample data set of images locally. And then we've kind of
[841.94 → 847.34] proven that, yeah, this is like a good way that we think we should do this kind of in this Jupiter
[847.34 → 854.00] notebook. So in order for us to kind of get that scenario off of our, you know, off of our laptops
[854.00 → 860.30] and into Packager, what would be the things that we would need? What would be the steps that we
[860.30 → 866.88] should do both on the data and the processing side? That is a great question. And I think we'll be a
[866.88 → 871.44] really illustrative answer. I'm going to sort of try to answer this with rather than jumping
[871.44 → 875.84] straight to the like, so here's the nth state of this, where I think it's like you're using all of
[875.84 → 880.82] the Packager features. I'm sort of going to like to build it up piece by piece, which is how we recommend
[880.82 → 886.00] data scientists to do it. So the first kind of problem that you need to solve when you want to
[886.00 → 891.44] put a Jupiter notebook into Packager is the fact that Jupiter notebooks are meant to be interactive,
[891.92 → 896.00] right? They're meant to have a user like opening up the browser and actually like clicking the run
[896.00 → 900.20] button and stuff like that. And so the first thing that you can do is you can actually run sort of
[900.20 → 904.52] Jupiter inside a Packager service, and you can just run Jupiter notebooks all by themselves,
[904.52 → 909.94] but they can't just turn into a pipeline that runs without any human intervention, right? Because
[909.94 → 913.70] Jupiter isn't designed that way. And so like in an automated and triggered sort of way.
[914.14 → 920.02] Right, right. So the first step to take is just to extract the code from Jupiter. I'm pretty sure
[920.02 → 924.96] Jupiter makes it very easy to export as a Python script at this point. And so you would do that and
[924.96 → 930.24] then you would put that in a Python container with whatever dependencies you need. And to start,
[930.38 → 934.66] I wouldn't even tease apart these different steps, the pre-processing, the model training,
[934.66 → 939.96] and the post-processing. You could just do all of those in one container, and you wouldn't even
[939.96 → 944.34] necessarily need to parallelize the data because if it was running on your laptop, it could probably run
[944.34 → 950.94] on a beefy EC2 node as well. And so that process I think would take you, you know, if you had
[950.94 → 955.50] packet or set up to begin with, you could probably do that in 20 minutes. And then you would have gone
[955.50 → 961.40] from a system that you can run manually on your laptop and edit to a system that now runs every
[961.40 → 965.90] single time a new image comes into the repository, or you change the code or something like that.
[966.04 → 971.20] And so, and also of course, now it's deployed on the cloud. So you can easily throw a GPU in there
[971.20 → 976.22] if you want. You can easily throw more memory at it and stuff like that. And so, so now you have sort of
[976.22 → 981.56] the first step of a productionized pipeline. Now, the next step is figuring out which of these steps
[981.56 → 986.32] does it make sense to tease apart so that maybe their outputs can be used by other steps. You know,
[986.36 → 990.32] in the future, you might want to do the same pre-processing and then trade multiple different
[990.32 → 995.50] models and then do the same post-processing on them or something like that. And so I would separate
[995.50 → 1002.34] out the pre-processing step, the training step, and the post-processing step into their own
[1002.34 → 1007.12] individual pipelines. And so now I've got a chain of like three steps and each of these is doing
[1007.12 → 1013.00] something different. And now I get the opportunity to sort of optimize each of these steps individually.
[1013.56 → 1019.26] Right. So the pre-processing step, for the most part, the pre-processing steps that I've seen
[1019.26 → 1025.20] can be done completely in parallel. Right. You're doing things like cleaning up the images. You don't need
[1025.20 → 1030.84] to see all the other images to clean up one image. Parallel as far as like in the sense of
[1030.84 → 1035.86] distributed processing, like processing things in isolation. Exactly. Yeah, exactly. So that's
[1035.86 → 1041.62] another of the like sort of important, important things that we get from a container is that it's
[1041.62 → 1047.36] very, very easy for us to scale that up. Right. So you can say, I need to process all of these
[1047.36 → 1052.30] images. Here's a container that does it, but don't just spin up one copy of this container. Give me a
[1052.30 → 1056.68] thousand. And so you're now cranking through a thousand images at the same time rather than one.
[1056.86 → 1059.96] And so you'll get done much, much faster, and you can handle much, much bigger loads.
[1059.96 → 1067.20] So I would do that with that step. The training step, making training happen in parallel is
[1067.20 → 1071.40] definitely a much more complicated question than making something like pre-processing happen in
[1071.40 → 1077.58] parallel. So normally we would still keep that as a non-parallel thing because your code needs to see
[1077.58 → 1082.32] all the data to train on it. If that is not true, if you really want to start paralyzing that,
[1082.44 → 1087.58] that is when you want to start looking at things like Below, which we integrate with, as you know,
[1087.58 → 1092.36] Dan, although we're still working on making that integration better. And then the last step,
[1092.42 → 1098.16] the post-processing step, that one could sort of stay as is unless you were anticipating having a
[1098.16 → 1102.72] lot of things that you wanted to post-process in parallel. So for example, when the DoD did their
[1102.72 → 1109.66] pipelines, theirs is all designed around the fact of we have one data set, but we have thousands of
[1109.66 → 1113.94] different people submitting models that they want to get tested. And so actually the post-processing step
[1113.94 → 1117.42] could be pretty expensive because they were just doing it for so many different entries.
[1117.58 → 1122.00] And so that was happening in parallel as well. From an infrastructure perspective, that's basically
[1122.00 → 1126.08] the idea of these pipelines is that when you segment these steps off into little pipelines,
[1126.32 → 1130.74] you then get complete control over the infrastructure on a pipeline by pipeline basis.
[1130.98 → 1135.62] So you get the ability to say like, this one needs to run in parallel with a thousand copies of the
[1135.62 → 1140.42] container up and each of those containers needs to have a GPU accessible to it and this much memory and
[1140.42 → 1145.48] stuff like that. And this one over here is not doing it really much at all. So like it just needs
[1145.48 → 1149.76] one container, and we'll fit that in somewhere. And the system sort of automagically figures out how
[1149.76 → 1152.16] to make all of this work with the resources that it has.
[1152.74 → 1157.56] Okay. Hey, JD, that was a great explanation. As a beginner, I have a few questions I'd like to follow
[1157.56 → 1163.96] up with. First, you mentioned Below. So I take it that Kubernetes is part of the architecture
[1163.96 → 1165.46] that you're deploying onto?
[1165.46 → 1171.18] Yes. I guess I jumped the gun on that one mentioning Below before Kubernetes. But yes,
[1171.28 → 1176.08] this is I think now when we need to bring in one more jargon word, and this will probably be our
[1176.08 → 1181.14] last infrastructure jargon word, which is Kubernetes. If you've heard of Docker, you've
[1181.14 → 1185.18] probably heard of Kubernetes as well. Actually, at this point, I think if you install Docker,
[1185.30 → 1190.18] it just has Kubernetes built into it. You should think of Kubernetes as kind of the puppet master
[1190.18 → 1195.62] for your containers, right? So a container is a really, perfect way to deploy a single piece
[1195.62 → 1200.82] of code, like a program. It's literally just a process inside a box. To deploy complicated
[1200.82 → 1205.50] distributed applications, you need to deploy a bunch of programs on different machines and make
[1205.50 → 1208.78] sure that they can all talk to each other and that they have the right resources and everything like
[1208.78 → 1214.28] that. And that's the piece that Kubernetes handles. So Kubernetes allows you to speak in very
[1214.28 → 1218.64] high level terms. That were a lot of the terms I was talking about, Packet are speaking in of
[1218.64 → 1223.94] basically being able to say, I want you to make sure that there is a copy of this container running
[1223.94 → 1229.28] somewhere. You have a thousand machines, you have the code to run, just make sure that this is always
[1229.28 → 1233.84] up somewhere. And I can talk to it consistently when I hit like this IP address or something like that.
[1234.24 → 1238.66] And Kubernetes will figure all of that out in the background for you. And it can be instead of
[1238.66 → 1242.78] one copy, it can be a thousand copies, and they can have specific infrastructure requirements like
[1242.78 → 1246.86] GPUs and stuff like that. And Kubernetes just solves all of that and deploys all of these
[1246.86 → 1251.08] containers. And so that's how we accomplish that with Picketers is we basically just take
[1251.08 → 1256.42] these Kubernetes semantics and then augment them with knowledge of the data that needs to be
[1256.42 → 1260.94] processed and capture how that data gets processed and where it goes.
[1261.32 → 1264.76] Gotcha. So just to kind of catch up a little bit and make sure I'm on the right track,
[1264.76 → 1269.88] you have Kubernetes deployed for infrastructure, and you're deploying Picketers on top of that.
[1270.24 → 1274.64] And you have the file system that it brings with the versioning and your capability for
[1274.64 → 1278.72] Providence tracking. And you've talked about the pipelines and stuff. I take just to ensure that
[1278.72 → 1282.94] I'm on the right track. I assume that the data is in the containers that you're deploying specifically.
[1283.54 → 1288.56] Yeah. So that's where it starts to get interesting. The data is in the containers,
[1288.88 → 1294.02] but it's kind of ephemerally in the containers because containers themselves are kind of ephemeral.
[1294.36 → 1299.06] Part of the point of a system like Kubernetes and the reason that you give it a thousand nodes to
[1299.06 → 1305.28] operate on is that any of those nodes could die at any time. Right. And this is the sort of thing
[1305.28 → 1309.84] where like, this is technically always true. You know, even when you're just running your code on
[1309.84 → 1315.42] your laptop, your laptop can die at any time. It's a physical machine, but this isn't such a concern
[1315.42 → 1320.10] when you have one computer, but when you're running on a thousand, it's almost guaranteed to happen
[1320.10 → 1326.76] once a day, just because you've got so many machines there. And so we put the data into your
[1326.76 → 1332.78] container for you to process. And then when you finish processing it, we write it back out to
[1332.78 → 1337.62] object storage. And that's where once it's in object storage, that's when it's actually persisted
[1337.62 → 1341.64] within our architecture because nothing that's stored on a disk in a container,
[1341.92 → 1345.24] any of that stuff could disappear at any moment is basically how we operate.
[1345.72 → 1350.60] This is also a great opportunity for me to talk to you about what the actual interface that your code
[1350.60 → 1356.58] gets to the packet arm data is. We really, really wanted to build a system that was going to be
[1356.58 → 1361.80] language agnostic. One of the things that really bugged me about the Hadoop ecosystem was that you
[1361.80 → 1366.44] sort of had to write in Java to really get the most comfortable semantics. Like you could kind of use
[1366.44 → 1372.44] Python, but it was always a little bit kludge. And so when your code that you've put in a container
[1372.44 → 1378.22] boots up and because Packet Arm wants it to process some data, you will just find your data sitting on
[1378.22 → 1383.72] the local file system under a directory called PFS. And these are just totally normal files.
[1383.72 → 1389.12] You can open them with a system call open, and you can read from them and write to them and stuff
[1389.12 → 1394.18] like that. And so this we thought was just the most natural interface that your code could possibly
[1394.18 → 1399.72] have. And users often have the experience when they've just written a Jupyter notebook to process
[1399.72 → 1404.78] some stuff on their laptop. Normally, they're just getting net data from local disk too. And so they
[1404.78 → 1408.30] have the experience when they're getting onto Packet Arm and like, okay, I'm going to need to learn the
[1408.30 → 1412.12] Packet Arm API. I'm going to need to import Packet Arm into my Python code or something like that.
[1412.12 → 1416.58] Like, no, you can just, you know, just use your normal OS system calls to open data and write
[1416.58 → 1419.62] data out. And that's, that's the entire system. That's all you need to do.
[1419.90 → 1425.08] Yeah. So I have a follow up there and, and maybe there have been some, some updates that I'm not
[1425.08 → 1431.36] aware of, but I think one of the common kind of maybe struggles that I've seen people ask about
[1431.36 → 1437.06] is, you know, this is definitely fundamentally different from something like Hadoop or Spark,
[1437.06 → 1442.48] where you have like some concept of, of data locality here. You're kind of like putting
[1442.48 → 1448.36] data into the container and then taking it out, but it actually lives somewhere else. Are there
[1448.36 → 1453.28] concerns with that? Are there like, like trade-offs? What, what is, what are the sort of trade-offs that
[1453.28 → 1458.14] you're, you're playing with there, especially as you get into kind of larger data sets and that sort of
[1458.14 → 1464.80] thing? Yeah. So there's absolutely trade-offs, right? Because each time that means that the data needs to be
[1464.80 → 1471.32] downloaded from S3 written, written to local disk, which is normally faster than S3. So that doesn't
[1471.32 → 1476.14] really incur a penalty. And then it needs to be pushed back into S3. And so basically what you're
[1476.14 → 1481.24] trading off here is that this system could be more performance, performant if it was entirely using
[1481.24 → 1488.12] hard drives, but it would be basically harder to, for, for admins to maintain, right? Because the
[1488.14 → 1492.14] the thing that people like about object storage is that it's just really dumb and simple. You've just
[1492.14 → 1496.82] got a bucket sitting there with all the data in it. There's no like, which hard drive is this on?
[1496.92 → 1500.12] Like, do we have all the hard drives? Are they linked up to the right things and stuff like that?
[1500.88 → 1505.94] The reason that we chose this architecture as, as sort of our initial architecture is that this
[1505.94 → 1510.58] was a lot of the direction that we saw. We saw people basically making this same trade-off in Hadoop,
[1510.58 → 1515.88] even though that they, they didn't have to. So by far the most common Hadoop cluster that we see
[1515.88 → 1521.44] today, and this applies to Spark as well, is basically everything stored in object storage,
[1521.56 → 1526.76] almost always S3, and then Map Reduce on top of that. And a lot of people are just bypassing actual
[1526.76 → 1532.62] HDFS at this point. We have been making, over the last release, and we're going to do a lot more of
[1532.62 → 1539.62] this in the upcoming 1.9 release, a lot of progress toward using hard drives to cache stuff.
[1539.62 → 1544.36] And so we're sort of going the other way that Hadoop went, where they were first a hard drive
[1544.36 → 1549.02] only solution. And then they started having like S3 as a way to like, checkpoint stuff out to long
[1549.02 → 1552.92] term storage. And then eventually that started becoming the only way that people ran stuff.
[1553.16 → 1557.20] We're always going to have object storage as like the long term place that we checkpoint stuff out
[1557.20 → 1561.20] to. And then we're going to use hard drives on top as like a cache. And that'll also allow us to
[1561.20 → 1566.52] use boatloads of memory as a cache too similar to Tachyon if people want like really, really low latency
[1566.52 → 1572.68] stuff. Cool. Yeah. The times that I've interacted with Spark, I kind of like, I always defaulted to
[1572.68 → 1577.42] that S3 option anyway, because it was hard for me to figure out other things. I don't know if that's
[1577.42 → 1584.30] just my own, you know, my own ignorance or whatever it is. But I definitely hear you on that front.
[1584.66 → 1588.24] But yeah, it's kind of like, there's always trade-offs, right? You don't get anything for
[1588.24 → 1591.76] free, but it's really kind of what you want. What do you want to optimize for?
[1592.24 → 1596.50] Yeah, it's always trade-offs. And actually, one of the things that we do a lot of,
[1596.52 → 1603.12] is trying to counsel people to not worry as much about like performance on the margins
[1603.12 → 1610.48] in the early days. Because we've seen a lot of like infrastructure deployments and like data
[1610.48 → 1614.98] science projects that just get really bogged down and thinking like, well, there's going to be this
[1614.98 → 1619.60] extra cost of data getting copied from S3 and getting back and stuff like that. And we always try
[1619.60 → 1624.26] to tell people like, worry about these things if it's truly going to make it impossible for you to
[1624.26 → 1628.24] accomplish your goals. Like if this absolutely needs to be a low latency system, because you're
[1628.24 → 1633.70] doing like algorithmic trading or something like that. But in a lot of cases, we feel like people
[1633.70 → 1639.18] get better results by just focusing on getting something that works. And that's, you know, I think
[1639.18 → 1643.52] exactly the trade-off that you were making when you were setting up Spark is that like, yeah, if you
[1643.52 → 1649.04] really bang your head against the wall, like you can figure out how to set up S3 on like solid state
[1649.04 → 1653.30] drives on AWS. And it's going to be faster than what you're doing, what you're doing with S3.
[1653.30 → 1657.86] But if you consider the amount of time that you spent setting that up as like performance time
[1657.86 → 1661.16] until you actually get your results, you might actually get them much, much slower.
[1661.48 → 1664.66] So there's a huge amount of value in just having infrastructure that you understand top to
[1664.66 → 1669.12] bottom and that is simple. So I wanted to ask about that. We've kind of talked about a lot of
[1669.12 → 1675.16] different technologies, you know, in these potential use cases. And I know that kind of getting back to
[1675.16 → 1679.96] teams and individual skills, blood teams where the skills were, you know, varied fairly widely.
[1679.96 → 1685.40] Some people like myself came from software engineering into the AI world and machine
[1685.40 → 1690.00] learning world and others came straight out of school and, you know, with data science degrees
[1690.00 → 1696.30] and had not done some of those. Do you ever find that there is any challenge or intimidation where
[1696.30 → 1700.48] people come out, and they may know their data science, but, you know, they may not have even
[1700.48 → 1705.16] heard of Kubernetes or not be familiar with containerization? I kind of wanted to call that
[1705.16 → 1710.26] out because like, you know, me and you and Daniel are all incredibly familiar with containerization
[1710.26 → 1714.22] and Kubernetes and such, but not everybody is kind of, how do you speak to that? Do you,
[1714.28 → 1718.50] do you recommend a data engineer or infrastructure engineer get involved, or what have you run into
[1718.50 → 1718.94] in real life?
[1719.32 → 1725.06] Yeah. So that's definitely a challenge for us, and we really see the full gamut, and it's just very,
[1725.16 → 1729.00] very interesting. You see some people who like build themselves as like, look, I'm a
[1729.06 → 1733.02] I'm a data science person. Like I'm, I've never really done any serious software engineering.
[1733.02 → 1736.86] Like I don't really keep up on this stuff. And then you sort of just sit them down and explain
[1736.86 → 1740.14] like, all right, well, here's what Docker is like, here's how you install and stuff. And they're like,
[1740.20 → 1744.68] oh, this basically seems to make sense. Like I can get by here. And then there's some people for
[1744.68 → 1749.76] whom we, we do like education sessions and basically just try to teach people the basics of containers
[1749.76 → 1756.08] so that they can work with it. I would say that actually when we really have challenges, it has,
[1756.08 → 1762.44] it's less about software engineering expertise and probably more about DevOps expertise,
[1762.44 → 1768.16] be honest. Like a lot of the, the types of issues that we hit are just like the permission on
[1768.16 → 1774.10] the Kubernetes cluster is wrong. And so when you go to deploy, like your code, everything works until
[1774.10 → 1779.32] it starts trying to like talk to S3 and then like the network just doesn't work or something. Cause
[1779.32 → 1783.66] like the bucket is rejecting it or something like that. And like, there's just a lot of DevOps
[1783.66 → 1789.56] complication in there. And so, you know, we always, we always sort of try to like to keep our feet on the
[1789.56 → 1793.88] ground a little bit on this stuff because you know, our whole goal with Picketer was when I was
[1793.88 → 1798.88] at Airbnb is like, well, this data infrastructure is really hard. And my team is 25 people just
[1798.88 → 1803.42] keeping this darn thing running. And so what are all the companies that don't have a team of 25
[1803.42 → 1807.86] people to keep their data infrastructure running doing? And so we wanted to make something where
[1807.86 → 1812.04] you didn't need that team. Like a data scientist could just do it by themselves. And I think we're
[1812.04 → 1815.78] closer, but you know, then when we go into companies and talk to them, we're like, well, we've got like
[1815.78 → 1819.52] one person working on this full-time, and you know, they're feeling like they have to do a lot of DevOps
[1819.52 → 1824.10] to keep the Picketers cluster up and running. I sort of realized like, okay, you know, we haven't,
[1824.20 → 1827.66] we've made an improvement here. We haven't just magically eliminated this. You know, we haven't
[1827.66 → 1833.80] gone from, you need 25 DevOps people to keep big infrastructure running to you need zero DevOps people
[1833.80 → 1838.36] to do it. And so we're trying to make that better in every release. We're trying to make that as easy
[1838.36 → 1842.96] as possible. And one of the big steps forward on that will be having our own hosted solutions. So people
[1842.96 → 1847.92] don't have to deploy everything on their own cloud just to try it out. Short answer is, is that's
[1847.92 → 1852.92] definitely a challenge is that there's a bit of an infrastructure leap that needs to be made, which can
[1852.92 → 1857.22] be uncomfortable for a lot of people that I think could ultimately benefit from the feature set of
[1857.22 → 1859.82] Picketers. It's just, they can't quite get the activation energy.
[1860.42 → 1865.04] So I was wondering, is, is there anything else, you know, and another question that you commonly find
[1865.04 → 1871.02] is people have existing infrastructure in place. They might be a Hadoop shop, a Spark shop, or one of
[1871.02 → 1875.18] several other technologies, you know, they might have big databases like Cassandra. What are you
[1875.18 → 1879.50] trying to replace? And how are you trying to fit in? I know we talked about the data locality issue,
[1879.64 → 1885.52] but are there any other big considerations that you would say is, is, you know, why you should go
[1885.52 → 1887.68] Picketers versus what they already have in house?
[1888.06 → 1894.96] Yeah, I mean, I would say the things we're trying to replace are sort of HDFS, and then the computation
[1894.96 → 1900.90] layers on top of that. So like Map Reduce is a common one, but like Hive and Spark, and stuff like that,
[1900.90 → 1905.46] we're also trying to speak to. Those are the main things that we're trying to replace. We constantly
[1905.46 → 1911.52] have the challenge of with people who have existing data infrastructure and want us to sort of fit
[1911.52 → 1918.08] into that well. And that's always a bit of a back and forth, because some things can work really well
[1918.08 → 1922.50] in Picketers, because you can just, you have the flexibility of a container. And so you can put
[1922.50 → 1928.26] whatever you want in there. So, you know, people will have containers that include code so that they
[1928.26 → 1934.40] can go and talk to Base somewhere else in the cluster, right? And so then you have sort of a
[1934.40 → 1939.82] natural like shim to put between your existing infrastructure and Picketers, which is the
[1939.82 → 1944.42] container code, which is totally flexible. It doesn't work beautifully for everything, right?
[1944.48 → 1949.38] Like what you wind up doing with like Spark, or something is you wind up having like, here's your
[1949.38 → 1954.20] data, it's stored in Picketers. Now you boot up a job and you want to talk to Spark. So now I need to
[1954.20 → 1958.66] push all this data into Spark or somewhere where it can access it or something like that. So we're
[1958.66 → 1964.00] sort of constantly trying to figure out how to make these integrations better. But the users that
[1964.00 → 1968.70] always excite us the most are the people who basically come in and say, like, we don't want
[1968.70 → 1974.12] to go down the Hadoop route. Like we know that there is a lot of just pain required to get a working
[1974.12 → 1978.34] Hadoop cluster and to get stuff functional on it. And so we want to try something different and just
[1978.34 → 1983.90] build from on Picketers from scratch. And so long term for our company, we're focused
[1983.90 → 1988.60] on how can we make things perfect for people who just see the Picketers vision and commit to it
[1988.60 → 1993.92] from scratch. Because those are, you know, if we're successful in 10 years, then those are going
[1993.92 → 1997.60] to be the people that have really made the company successful. And the sort of the integrations will
[1997.60 → 2002.04] help us along the way to onboard more people, but it's really going to depend on that core use case.
[2002.52 → 2006.62] Yeah. So the team that I'm working on now, the organization is pretty big, but it's kind of
[2006.62 → 2013.08] on this project that I'm working on, it's like myself who has some type of data science background,
[2013.08 → 2020.20] and then another guy who is somewhat technical, but he's a linguist. And so our ability to spin up a
[2020.30 → 2027.64] like a working Hadoop infrastructure is probably like less than 0% probability. And so, I mean,
[2027.64 → 2033.90] even just like, if there's one thing I could say to, to listeners, like, even if you just get to like,
[2033.90 → 2040.18] where you can use containers themselves is like a huge benefit also to like reproducibility in the
[2040.18 → 2045.72] in the space of machine learning and AI, which is, is awesome. So I kind of wanted to follow up.
[2045.86 → 2051.18] You've already mentioned JD that Picketers, at least what we've talked about up to this point is,
[2051.26 → 2057.26] is free, but I also know like you're a company, right? And I should give you some congratulations
[2057.26 → 2060.08] because you just kind of hit a big accomplishment. Isn't that right?
[2060.08 → 2065.96] Yeah. And, and thank you for the congratulations. We just raised a series a which means that we have
[2065.96 → 2071.14] a ton more funding to basically pursue our vision for data science infrastructure. And it also means
[2071.14 → 2075.44] that you can commit to Picketers as your infrastructure with a lot more peace of mind
[2075.44 → 2080.70] now, because you know, the company is going to be around for quite a ways to come. That also sort of
[2080.70 → 2085.96] leads, as you said, we are, we are a company, which means that we need a way to make money. And that
[2085.96 → 2090.56] for that, we have an enterprise product. So let me just sort of tell you what's in that,
[2090.62 → 2095.56] that you won't find in the enterprise. We try to really make it so that our open source product
[2095.56 → 2101.30] contains everything that's going to be really useful to sort of individuals and people who,
[2101.42 → 2104.90] you know, just want to get some, some data science done, but they're not running within
[2104.90 → 2109.68] a gigantic organization where they have all of those concerns. So the types of things that go into
[2109.68 → 2114.94] that enterprise product are the permission system. And so that's, you know, the ability to say like
[2114.94 → 2120.44] this data right here is owned by Dan, this data right here is owned by JD, this data right here
[2120.44 → 2126.18] is owned by Steve, things like that, and make sure that nobody is getting data that they don't have
[2126.18 → 2131.84] access to. And what's cool, and what we think is a very crucial feature for these types of system is
[2131.84 → 2137.24] that it's informed by our provenance model, right? This is a big problem that you'll run into
[2137.24 → 2143.72] in big data organizations, is that it's very easy to have some data that nobody's allowed to see
[2143.72 → 2147.80] that then gets turned into a model or some sort of aggregation or something like that,
[2148.18 → 2152.04] that everyone's allowed to see that is accidentally leaking the data that went into it.
[2152.20 → 2156.48] And so we have our provenance tracking system at form, the permission system. So if you don't have
[2156.48 → 2160.94] access to the provenance of data, then by default, you don't have access to the data itself,
[2160.94 → 2165.00] because it might contain that information that you're not allowed to see. Other things that go into
[2165.00 → 2170.58] the enterprise product are like a sort of wizard UI builder for building new pipelines and things like
[2170.58 → 2176.16] that and visualizing how they're working and the ability to sort of track and really optimize your
[2176.16 → 2181.48] pipelines, see where they're spending all of their time and squeeze every last little bit of performance
[2181.48 → 2187.18] out of your hardware. The other main thing that we sell is basically just support and our time.
[2187.30 → 2191.54] And the ability to talk to us and have us prioritize features and stuff like that, which is
[2191.54 → 2193.30] every open source project does that.
[2193.30 → 2198.78] Yeah, it's fascinating. I always love to hear different people's perspectives on their
[2198.78 → 2203.66] open source models as well. I was just talking to someone the other day, a friend who's starting
[2203.66 → 2208.82] a new business and considering how they should approach open source, but yet also be a company
[2208.82 → 2214.12] and survive. So I think there is definitely people out there that are interested in that question.
[2214.28 → 2215.36] So I appreciate you sharing that.
[2215.74 → 2222.64] Yeah, absolutely. And it's tricky, and it's very imperfect, because I really think that this is a system that
[2222.64 → 2228.78] really should exist. There's a lot of need for a system like this. It basically has to be open
[2228.78 → 2234.40] source for it to actually fill that need. In my mind, I just couldn't see a proprietary system
[2234.40 → 2239.46] becoming like the standard data infrastructure layer. But it's very, very hard to get the funding
[2239.46 → 2245.50] to work when you're open source. It's this huge asset because people can so easily try your product and
[2245.50 → 2250.94] you get so much adoption and stuff like that. But it really anchors people of just like an unwillingness
[2250.94 → 2256.52] to pay for software when it's open source. And so you always sort of need to cross that threshold.
[2256.66 → 2262.28] And one of the things that we're looking to do in the future, now that we've raised more money,
[2262.38 → 2267.32] is basically built the hosted version of our software. Because that just sort of totally,
[2267.42 → 2271.42] it totally changes the value proposition. But it also, I think, has some sort of psychological
[2271.42 → 2276.74] effects on people wherein like nobody would ever pay for Git. But the idea that you're going to pay
[2276.74 → 2281.40] seven bucks a month to have like private repos on GitHub or something like that is just totally
[2281.40 → 2282.56] palatable to people.
[2282.56 → 2288.26] I think that's a fantastic idea. I love the hosted idea. I know that when Daniel first introduced me
[2288.26 → 2292.84] to Pachyderm a while back, and I was kind of initially learning the fact that coming from
[2292.84 → 2298.28] the software engineering world, that it was built on containerization and Kubernetes was a huge plus for
[2298.28 → 2302.80] me. If I recall correctly, a lot of it's in Go, which I thought was pretty amazing,
[2302.80 → 2307.46] as is Docker and Kubernetes. I guess if you're just hearing about it, and you've kind of come
[2307.46 → 2312.36] away from this episode today, and you want to learn more about it, and maybe want to dive in,
[2312.44 → 2316.50] get your hands dirty and figure out if it's right for your organization, how do people get started
[2316.50 → 2316.76] with that?
[2317.18 → 2322.38] Yeah, so we've got a bunch of tutorials and like quick start guides online. And so you know,
[2322.42 → 2326.76] if you want to just sit down with a guide and start hacking away, then that's the way to do it.
[2326.84 → 2332.70] We also have a very active user Slack channel, where all of our engineers and everyone on the team
[2332.70 → 2336.76] is just always hanging out and ready to ask questions. And you know, those questions range
[2336.76 → 2341.18] from like, I hit this error, what do I do? And you know, we just give you a simple response,
[2341.18 → 2346.82] if it's simple, hopefully it's simple. And to people also asking us, you know, I'm looking at
[2346.82 → 2351.92] Pachyderm for a new project, talk to me about the feature set, you know, talk to me about how you think
[2351.92 → 2356.36] this could be helpful here and just like talking to us. And so I think that's, that's really the best
[2356.36 → 2361.28] way if you want someone to talk about, to talk to about stuff is just stopped by the Slack channel.
[2361.28 → 2367.44] Awesome. Well, thank you so much for taking time to talk with us, JD. Of course, we'll put the links
[2367.44 → 2371.62] to like the tutorials and the docs and the Slack channel and all of that in our show notes. So,
[2372.02 → 2377.32] so go check those out. But it's been awesome to hear from you and really excited to hear about the
[2377.32 → 2379.66] progress with Pachyderm and all the good things you're doing.
[2380.00 → 2382.92] Yeah, thanks so much for having me, man. I love appearing on podcasts.
[2383.46 → 2387.32] All right, well, look forward to seeing great things from Pachyderm. Thanks again.
[2387.32 → 2388.50] Thanks for coming on the show.
[2388.54 → 2388.78] Thanks, guys.
[2391.28 → 2395.30] All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this
[2395.30 → 2399.82] show, do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it.
[2399.94 → 2403.38] If you are on Twitter or social network, share a link with a friend, whatever you got to do,
[2403.62 → 2408.04] share the show with a friend if you enjoyed it. And bandwidth for changelog is provided by Vastly.
[2408.16 → 2412.42] Learn more at fastly.com. And we catch our errors before our users do here at changelog because
[2412.42 → 2417.74] of Rollbar. Check them out at rollbar.com slash changelog. And we're hosted on Linde cloud
[2417.74 → 2423.54] servers. Head to leno.com slash changelog. Check them out. Support this show. This episode is hosted
[2423.54 → 2429.18] by Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith. The music is by Break master
[2429.18 → 2434.72] Cylinder. And you can find more shows just like this at changelog.com. When you go there, pop in
[2434.72 → 2439.34] your email address, get our weekly email, keeping you up to date with the news and podcasts for
[2439.34 → 2444.00] developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2447.74 → 2456.50] I'm Nick Needed. This is K-Ball. And I'm Rachel White. We're panellists on JS Party, a community
[2456.50 → 2461.06] celebration of JavaScript and the web. Every Thursday at noon central, a few of us get together
[2461.06 → 2465.38] and chat about JavaScript, Node, and topics ranging from practical accessibility to weird
[2465.38 → 2471.94] web APIs. You could just evil the text that you're given and then, and that's basically what
[2471.94 → 2478.56] it's doing. What could go wrong? Yeah, exactly. This is not legal advice to evil text as it comes
[2478.56 → 2483.46] in. Join us live on Thursdays at noon central. Listen and Slack with us in real time or wait
[2483.46 → 2488.54] for the recording to hit. New episodes come out each Friday. Find the show at changelog.com
[2488.54 → 2491.90] slash JS Party or wherever you listen to podcasts.
