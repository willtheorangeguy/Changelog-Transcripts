[0.00 --> 8.58]  Welcome to Practical AI.
[9.14 --> 15.90]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.90 --> 18.72]  are changing the world, this is the show for you.
[19.14 --> 24.32]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.32 --> 24.62]  listen.
[24.90 --> 26.72]  Check them out at Fastly.com.
[26.72 --> 31.96]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.38 --> 33.66]  No ops required.
[33.98 --> 36.02]  Learn more at fly.io.
[42.88 --> 47.70]  Welcome to another fully connected episode of the Practical AI podcast.
[48.16 --> 54.06]  In these episodes, Chris and I keep you fully connected with a bunch of different things
[54.06 --> 57.48]  that are happening in the AI and machine learning community.
[58.06 --> 61.98]  And we talk through some things to help you level up your machine learning game.
[62.52 --> 63.98]  My name is Daniel Whitenack.
[64.12 --> 69.88]  I am a founder at Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[70.36 --> 72.40]  who is a tech strategist at Lockheed Martin.
[72.88 --> 73.54]  How are you doing, Chris?
[73.72 --> 75.22]  I'm doing great today, Daniel.
[75.26 --> 75.70]  How's it going?
[76.20 --> 77.08]  It's going good.
[77.08 --> 82.32]  You know, this week I was, well, it's been an interesting couple of weeks for me in that
[82.32 --> 90.26]  I was at the Intel Innovation Conference out in San Jose the week before last.
[90.50 --> 96.66]  And then this week I was at the Go Programming Language Conference called GopherCon and taught
[96.66 --> 97.52]  a workshop there.
[97.90 --> 99.66]  And so that was really enjoyable.
[99.66 --> 104.92]  So two weeks in sunny California or mostly sunny California, I guess.
[105.12 --> 106.22]  That was really cool.
[106.42 --> 112.52]  So maybe even just highlighting a couple of cool things that are happening in those communities
[112.52 --> 113.50]  at Intel.
[113.72 --> 118.56]  There were a couple of things that were highlighted that might be of interest.
[118.70 --> 128.76]  One is it seems like Intel is really diving into the idea of AI-enabled applications on your
[128.76 --> 134.20]  local machine, which I know is something we might talk about a little bit in this show
[134.20 --> 134.88]  in particular.
[135.10 --> 141.06]  That is like, hey, if I want to build a desktop application that people actually run on their
[141.06 --> 149.82]  laptop and I want that to run stable diffusion as part of the application and not, you know,
[149.86 --> 153.60]  reach out over the network to some API, how would I build that?
[153.60 --> 159.96]  And what would those sort of like AI PCs is, I think, what they're calling them.
[160.20 --> 161.84]  What would those have to look like?
[161.88 --> 166.14]  And they're thinking about that with some of their processors, which is interesting.
[166.36 --> 171.64]  And then on the data center side, they had a bunch of things, including announcing the
[171.64 --> 179.62]  Intel Developer Cloud, which is cool because you can go on there similar to other cloud environments
[179.62 --> 186.76]  and spin up either a VM or actually connect to a bare metal instance that has their latest
[186.76 --> 193.06]  generation of processors, including these Gaudi 2 processors, which are from Habana Labs.
[193.22 --> 195.36]  They were acquired by Intel.
[195.64 --> 197.62]  I forget when, but they have.
[197.80 --> 200.62]  So they would be sort of on the data center side.
[200.72 --> 203.10]  You're running accelerated workloads on these.
[203.10 --> 208.78]  And we're actually running some of our prediction guard stuff on these Gaudi processors and seeing
[208.78 --> 210.08]  really great performance.
[210.28 --> 213.34]  So those are a couple of things highlighted from there.
[213.76 --> 214.84]  And yeah, I don't know.
[214.98 --> 219.80]  Have you heard those themes in your conversation as well in terms of either new processors,
[220.66 --> 227.46]  advances in data center technology or this kind of local inference side of things?
[227.46 --> 229.38]  I have quite a bit actually.
[230.02 --> 235.26]  And I'm certainly not an expert on microelectronics by any stretch, but I have friends who are and
[235.26 --> 236.92]  listen to them closely when they talk.
[237.20 --> 242.06]  There's a bit of an ongoing revolution on the microprocessor side.
[242.60 --> 248.34]  And so many of us that have been in the AI world for a long time, there have been, for
[248.34 --> 251.64]  instance, GPUs from NVIDIA have been kind of a core to that.
[251.64 --> 256.68]  But there's a lot of chip types that have been coming out by a number of different vendors
[256.68 --> 258.38]  to compete with that.
[258.92 --> 264.34]  Famously, Google was probably the first one well known with their TPUs, tensor processing
[264.34 --> 264.78]  units.
[265.02 --> 270.88]  But there's all sorts of specialized chips and chiplets that are coming out that are enabling
[270.88 --> 271.90]  these types of things.
[272.02 --> 275.00]  So I think Intel is definitely one of the global leaders in that.
[275.62 --> 281.34]  And looking forward to having, it'll be nice when everyone's laptops and phones and everything
[281.34 --> 283.82]  are all completely equipped with everything they need.
[284.54 --> 285.00]  Yeah, yeah.
[285.22 --> 290.92]  It's super interesting, especially for use cases where it's like your personal assistant,
[291.28 --> 296.84]  AI enabled personal assistant that really is tied to you personally.
[297.50 --> 302.70]  Applications like that, I think you'd want to run a lot of those things locally and not
[302.70 --> 304.96]  be sending a lot of that data all around.
[305.18 --> 306.64]  So that's kind of interesting.
[306.64 --> 315.26]  They also talked a lot about confidential computing, which is an interesting topic that I think maybe
[315.26 --> 321.56]  some of our audience at least wouldn't be familiar with as much from what we talk on this show
[321.56 --> 322.06]  about.
[322.24 --> 328.80]  But it is very connected to the AI world in the sense that if you are running kind of secure
[328.80 --> 335.00]  workloads through AI models, whether you're doing that on NVIDIA chips or other chips like
[335.00 --> 344.74]  we've talked about, there are ways and toolkits to enable you to actually secure the environments
[344.74 --> 352.24]  that you are running those models in and actually provide attestation to know that nothing has
[352.24 --> 356.12]  been tampered with inside of those kind of secure environments.
[356.50 --> 357.54]  So I'm going to surprise you.
[357.66 --> 359.14]  I actually know quite a lot about that.
[359.22 --> 361.20]  Those are trusted execution environments.
[361.42 --> 363.38]  Let's just say I've touched on those quite a lot.
[363.38 --> 366.96]  I think Intel's version is like TDX trusted.
[367.42 --> 368.14]  Yeah, it's something.
[368.50 --> 369.78]  They have a couple of different versions.
[369.90 --> 372.10]  That's the one that's out in the marketplace right now.
[372.20 --> 377.32]  But yeah, it's the idea of ensuring that when you normally, if you're running a program
[377.32 --> 382.08]  for audience, if you're running a program and it has to transit, obviously, from system
[382.08 --> 385.70]  to system, every system has a processor it's processing on.
[385.94 --> 389.72]  And even if you're running encryption at the application layer, you have to unwrap that
[389.72 --> 393.00]  encryption for the processing to happen in the chip.
[393.00 --> 400.08]  An adversary, you know, if it's on the order of a major nation state, has the ability to
[400.08 --> 406.08]  steal unencrypted information that had been encrypted in transit straight out of the processor
[406.08 --> 406.58]  memory.
[406.58 --> 413.68]  And Intel and other vendors are starting to push trusted execution environments and products
[413.68 --> 419.58]  and services around that, which protects and guarantees the safety of that data inside
[419.58 --> 420.20]  the processor.
[420.42 --> 422.24]  Something I've spent some time on, actually.
[422.86 --> 423.98]  Yeah, it's super interesting.
[423.98 --> 431.18]  And I think even the CTO and his talk had like a T-shirt that sort of had a Venn diagram
[431.18 --> 434.44]  kind of thing between like security and AI.
[434.82 --> 440.24]  And at the intersection of that is a lot of, you know, what he talked about, this sort of
[440.24 --> 446.52]  idea that, hey, whatever hardware you're running on, if you can combine AI workloads with
[446.52 --> 451.82]  these sort of trusted or confidential computing ideas, that can be very powerful and take care
[451.82 --> 458.96]  of at least some of the security and privacy concerns that people have with AI workloads
[458.96 --> 461.36]  in general, which is cool.
[461.92 --> 466.14]  So yeah, the two are converging in a big way because while trusted execution environments,
[466.14 --> 472.24]  which are referred to as TEEs, have been around for years in processors, now that we are having
[472.24 --> 479.06]  large federated workflows, which is really classic on cloud-based AI jobs, where you're distributing
[479.06 --> 485.48]  an AI inference or training across many, many systems with very, very important data that
[485.48 --> 488.00]  you would not want to get into an adversary's hands.
[488.50 --> 494.90]  That federation is really kind of pushing AI and, you know, chip providers together in that
[494.90 --> 495.96]  way to guarantee that.
[496.10 --> 500.70]  We didn't see lots of workloads that would be falling in that category until we hit the
[500.70 --> 502.56]  AI space and it's chock full of them.
[502.56 --> 507.60]  So I keep remembering things that happened over the past couple of weeks while I've been
[507.60 --> 513.00]  traveling and people have mentioned, but one maybe other noteworthy thing for people to
[513.00 --> 519.56]  be aware of on the more of the infrastructure side, which I think we will talk a little bit
[519.56 --> 524.76]  more about in this episode is that Cloudflare announced their workers' AI.
[525.18 --> 530.90]  And I think this is the latest in this sort of series of serverless GPU solutions.
[530.90 --> 540.40]  So these worker AIs are Cloudflare's version of the serverless GPU type environment that we've
[540.40 --> 545.84]  talked about with things like modal or base 10 or banana.
[546.30 --> 551.74]  There's a lot of these coming out, but I think it's worth noting that a very large player like
[551.74 --> 557.88]  Cloudflare is now kind of dipping into this serverless GPU space, which I think also signals
[557.88 --> 565.24]  that we'll be kind of seeing in the cloud side more and more push towards serverless GPU
[565.24 --> 569.24]  workloads and environments that support that.
[569.72 --> 569.84]  Interesting.
[570.10 --> 570.86]  Very interesting.
[571.40 --> 579.14]  Well, that's a bunch of infrastructure and confidential infrastructure and computing and security
[579.14 --> 582.54]  stuff that has crossed our paths in the past couple of weeks.
[582.54 --> 590.14]  But one of the questions that you asked me leading up to this recording was about things
[590.14 --> 591.40]  are moving so fast.
[591.40 --> 600.88]  And I think deploying and managing an AI workload may look different now than it even looked six
[600.88 --> 601.62]  months ago.
[601.62 --> 610.36]  And it's been a while since we talked through the kind of developer or technical team perspective
[610.36 --> 617.18]  on how you might, if you want to use one of these models that's coming out all the time.
[617.40 --> 620.10]  So Mistral AI's model just came out.
[620.10 --> 625.72]  The ones that received huge, amazing amount of funding just earlier in June, and now they
[625.72 --> 626.96]  have their first model out.
[626.96 --> 629.78]  It's released Apache 2, so you can download it.
[629.92 --> 633.54]  So the question is, let's say you want to use one of these great models that's coming
[633.54 --> 639.12]  out these days and you want to host it in your company's infrastructure or even just play
[639.12 --> 640.72]  around with it as a developer.
[641.14 --> 643.40]  What does that look like currently?
[643.72 --> 648.00]  Because there's also, along with these models that are coming out, new tooling that's coming
[648.00 --> 649.14]  out all the time.
[649.14 --> 651.80]  So what does that look like these days?
[651.98 --> 657.84]  And what are the various options and things to consider as you're interacting with these
[657.84 --> 663.18]  models and considering even hosting them yourself or integrating them in your own infrastructure?
[663.58 --> 668.10]  That's a fair question because it's been a while since we talked through some of the
[668.10 --> 669.34]  infrastructure, I think, Chris.
[669.88 --> 670.32]  It has.
[670.50 --> 674.74]  And for what it's worth, I'm going to brag on you for a second since I know that you would
[674.74 --> 675.66]  not do that to yourself.
[675.66 --> 682.86]  With Daniel being the founder of Prediction Guard, this is a topic that he is a global
[682.86 --> 685.08]  expert in, really, really knows what he's doing.
[685.56 --> 690.00]  And as we were talking about, I've had so many people asking me these questions that Daniel
[690.00 --> 691.36]  was just talking about lately.
[691.70 --> 695.30]  And I was like, well, one of my best friends is a real pro at this.
[695.62 --> 696.50]  So thank you.
[696.68 --> 698.58]  If you can kind of start walking us through.
[698.72 --> 701.32]  And this is a moving topic, as you just pointed out.
[701.36 --> 702.76]  It's changed in the last few months.
[702.76 --> 705.22]  And we'll continue to evolve over time.
[705.70 --> 709.86]  But yeah, if you can start walking us through what that looks like today.
[710.02 --> 712.56]  You know, we're in the beginning of the fall of 2023.
[713.22 --> 716.50]  Something that might help the rest of us for at least the next few months.
[717.04 --> 721.62]  And maybe one note on this is I'm also getting these questions all the time.
[721.68 --> 724.80]  And like you say, I'm deploying models all the time with Prediction Guard.
[724.80 --> 732.36]  I think a lot of people, if you're a developer or an infrastructure person, you just have
[732.36 --> 733.68]  that natural desire.
[733.94 --> 739.64]  Even if you end up using a model that's behind some API that's hosted by someone else, it
[739.64 --> 746.70]  can be useful and instructive in building your own intuition even to just try deploying one
[746.70 --> 747.32]  of these models.
[747.50 --> 748.96]  See what's involved.
[749.14 --> 750.76]  See how they run.
[750.84 --> 751.70]  That sort of thing.
[751.70 --> 759.80]  It's also kind of worthwhile from my perspective to experiment with different models before
[759.80 --> 764.84]  you say, you know, lock yourself into a certain model family or something.
[765.08 --> 769.76]  It's relatively easy now with the tooling to get somewhat of a sense of how these different
[769.76 --> 773.10]  models perform and build up that intuition for yourself.
[773.10 --> 775.84]  Even if you end up using a model that's behind an API.
[775.84 --> 780.10]  I mentioned I was at GopherCon this week, and that was some of the questions that came
[780.10 --> 782.88]  up to taught a workshop on generative AI.
[783.70 --> 788.56]  And that was a good long discussion in there that people had a lot of questions about was,
[788.98 --> 791.44]  hey, let's say I didn't want to use one of these APIs.
[791.90 --> 794.16]  How do I pull down a model and use it?
[794.54 --> 795.70]  So yeah, let's jump in.
[795.78 --> 802.58]  Let's first maybe talk about something that I know that we've touched on before.
[802.58 --> 807.16]  But just to emphasize here, where can you get models?
[807.50 --> 814.28]  And let's say that we're putting aside for a second the kind of closed proprietary chunk
[814.28 --> 814.92]  of models.
[814.92 --> 819.66]  These would be ones from like OpenAI, Anthropic, Cohere, etc.
[820.42 --> 821.70]  They have their own APIs.
[821.86 --> 822.78]  They host those models.
[822.92 --> 829.32]  Let's say that we're interested in either an open access model, but it could be either an
[829.32 --> 835.60]  open and somewhat restricted model or an open and somewhat permissively licensed model.
[835.70 --> 837.88]  And we've talked about that on the show, too.
[838.44 --> 844.88]  For example, there's models that come out that are licensed for commercial use or non-commercial
[844.88 --> 846.84]  use or research purposes only.
[846.98 --> 850.26]  But let's say you want to use one of these open access models.
[850.74 --> 854.36]  The first question that might come up is, where do I find these models?
[854.36 --> 859.08]  The best place that you can find these models is on Hugging Face.
[859.54 --> 866.70]  So if you go to the Hugging Face website, just huggingface.co, and you click on models,
[866.86 --> 873.48]  you'll see that there's, at the time of this recording, around 345,000 models on Hugging Face.
[873.64 --> 874.64]  A few to choose from.
[875.00 --> 875.46]  Yeah, yeah.
[875.58 --> 876.70]  A lot to choose from.
[876.90 --> 880.82]  And think about this, those of you that are familiar with GitHub, right?
[880.86 --> 882.86]  How many GitHub repositories are there?
[882.86 --> 890.58]  There's a lot of GitHub repositories that are someone like tried something in an afternoon
[890.58 --> 892.86]  and uploaded something to their GitHub repo, right?
[892.90 --> 899.34]  It doesn't mean that's the most useful thing for you to use in your workflows, although you
[899.34 --> 900.90]  could kind of learn from it, maybe.
[901.16 --> 902.56]  It's similar on Hugging Face.
[902.66 --> 908.42]  There's a lot of people that might like, oh, I tried fine-tuning this model, and now I uploaded
[908.42 --> 911.12]  it to my repo on Hugging Face.
[911.12 --> 917.70]  And similar to GitHub, one of the things that you want to look at just as a practitioner
[917.70 --> 920.46]  is look at how many people are downloading the model.
[920.62 --> 924.90]  Look at how many people are hearting the model or, you know, liking the model.
[925.30 --> 928.60]  And you can filter by those things.
[928.60 --> 935.60]  So if I click on model, I can then click on a filter like the task that I'm interested
[935.60 --> 939.74]  in, a computer vision task or an NLP task or an audio task.
[939.74 --> 946.52]  And then I can look at both the trending models and how many models were downloaded, filtered
[946.52 --> 948.78]  by things like licenses and languages.
[948.78 --> 955.78]  So, yeah, I think the first thing to be aware of is just the landscape of models and where
[955.78 --> 956.64]  you find them.
[957.00 --> 962.80]  And the best place for that currently, although there are other repositories, is by and far
[962.80 --> 967.42]  Hugging Face and go there and treat it similarly to GitHub.
[967.68 --> 971.12]  And that there's going to be a lot of there that might not be of interest to you, but there's
[971.12 --> 973.90]  going to be some really great things there as well.
[982.34 --> 983.10]  What's up, friends?
[983.14 --> 985.80]  There's so much going on in the data and machine learning space.
[986.28 --> 987.58]  It's just hard to keep up.
[987.58 --> 991.66]  Did you know the graph technology lets you connect the dots across your data and ground
[991.66 --> 993.62]  your LLM in actual knowledge?
[994.00 --> 999.14]  To learn about this new approach, don't miss Nodes on October 26th at this free online conference
[999.14 --> 1003.50]  developers and data scientists from around the world will share how they use graph technology
[1003.50 --> 1008.60]  for everything from building intelligent apps and APIs to enhancing machine learning and
[1008.60 --> 1010.00]  improving data visualizations.
[1010.64 --> 1013.26]  There are 90 inspiring talks over 24 hours.
[1013.40 --> 1016.50]  So no matter where you're at in the world, you can attend live sessions.
[1016.50 --> 1020.76]  To register for this free conference, visit neo4j.com slash nodes.
[1020.94 --> 1026.36]  That's N-E-O, the number 4, J.com slash nodes.
[1029.14 --> 1038.20]  Okay, Chris, I'm on Hugging Face and I see a bunch of different models that are potentially
[1038.20 --> 1039.52]  available to me.
[1039.86 --> 1049.08]  And I can click on, for example, object detection and see that the trending model that I'm looking
[1049.08 --> 1053.64]  at is from Facebook, D-E-T-R ResNet 50.
[1053.64 --> 1057.68]  Seems like people have used ResNet quite a bit.
[1058.70 --> 1060.60]  603,000 downloads.
[1061.16 --> 1064.96]  And so maybe that's a good place I want to start if I'm looking at object detection.
[1065.32 --> 1073.96]  If I go to, let's say, automatic speech recognition, up at the top would be OpenAI's Whisper model,
[1074.22 --> 1080.08]  which is a great choice and released openly that you can use for speech transcription.
[1080.08 --> 1086.72]  If I go to, for example, text generation, which a lot of people care about these days,
[1087.20 --> 1092.40]  the trending one right now is this new Mistral 7 billion model that we mentioned earlier was
[1092.40 --> 1093.10]  just released.
[1093.74 --> 1096.46]  So let's take those as our kind of example.
[1096.60 --> 1102.92]  Let's say I want to run something like OpenAI Whisper, or I want to run text generation with
[1102.92 --> 1104.26]  Mistral 7 billion.
[1104.26 --> 1108.96]  Or there's even a range of sizes of models, right?
[1109.04 --> 1114.08]  The 7 billion model from Mistral Falcon, 180 billion was released recently.
[1114.44 --> 1123.36]  So one question that I think people have is, how do I know which model might serve my task well?
[1123.96 --> 1128.48]  And one thing I'd like to recommend to people is even before you try to download the model
[1128.48 --> 1132.68]  yourself and run it, you can go in and click on these models.
[1132.68 --> 1141.12]  Like if I click on Mistral 7 billion version 0.1, if you notice on the right hand side of
[1141.12 --> 1149.46]  the Hugging Face model card for that model, a lot of these models already have a hosted
[1149.46 --> 1156.76]  interactive interface that you can just click the compute button and see the output of the
[1156.76 --> 1157.60]  model.
[1157.70 --> 1161.68]  So it's kind of like a playground that you can see a bit of the output of.
[1161.76 --> 1167.16]  You can do the same thing with a lot of, you know, computer vision models or audio models.
[1167.36 --> 1175.04]  And then below that, you'll see a little thing called spaces using Mistral 7 billion, or if
[1175.04 --> 1177.62]  you're on Whisper spaces using Whisper.
[1177.62 --> 1185.88]  These are little demo apps that are actually hosted within Hugging Face's infrastructure where
[1185.88 --> 1189.58]  people have actually integrated Mistral 7 billion.
[1189.58 --> 1194.30]  And a lot of these are kind of just a simple input output interface.
[1195.08 --> 1200.14]  And so even without downloading the model, if you're just trying to get a sense for what
[1200.14 --> 1206.20]  these models do, you can click through some of these spaces that are using them or just
[1206.20 --> 1211.14]  look at that kind of interactive playground feature and just try, you know, upload some of
[1211.14 --> 1216.16]  your own prompts or upload some of your own audio or whatever that is to see how the model
[1216.16 --> 1216.98]  operates.
[1217.06 --> 1220.56]  I think a lot of people might miss this if they're just scrolling through.
[1221.06 --> 1222.04]  Let me ask you a quick question.
[1222.48 --> 1226.62]  When, if you're looking and you're trying to narrow down, you know, which model you want
[1226.62 --> 1226.98]  to pick.
[1227.18 --> 1231.72]  We've talked on previous episodes about some of the concerns that go with different sizes
[1231.72 --> 1232.44]  and such.
[1232.44 --> 1239.44]  So are there some models that, unless I have a very large infrastructure available to me,
[1239.76 --> 1243.54]  many, many GPUs, for instance, that I should probably disregard?
[1243.94 --> 1250.18]  Is there like a minimum and maximum practical threshold that would say that I have some hardware,
[1250.36 --> 1253.82]  but not everything that I would dream about that I might want to go for?
[1254.46 --> 1258.18]  So there's kind of an answer to this and then a follow up.
[1258.18 --> 1267.16]  One is for this sort of transformer language models, oftentimes if you go much beyond 7 billion
[1267.16 --> 1273.06]  parameters, maybe pushing it up to kind of 13 to 15 billion parameters, you're not going
[1273.06 --> 1278.84]  to be able to run it very well just by default by downloading it and running it with the kind
[1278.84 --> 1285.02]  of standard tooling on anything but a single accelerated processor like a GPU.
[1285.02 --> 1289.84]  And even then, most of the time, not on a consumer GPU.
[1290.58 --> 1298.66]  However, the follow up to that is that a lot of people have created open source tooling around
[1298.66 --> 1306.34]  model optimization that may allow you to run these models on consumer hardware or even on CPUs.
[1306.46 --> 1311.96]  And I'd like to talk about that here in a bit that a lot of times you may want to consider this
[1311.96 --> 1318.28]  sort of model optimization piece of your pipeline when you're considering how to run the model,
[1318.42 --> 1323.58]  because sometimes the sort of default size and default precision of the model might not
[1323.58 --> 1329.54]  be best for you, both in terms of your needs, in terms of performance or in terms of the hardware
[1329.54 --> 1330.84]  that's available to you.
[1330.84 --> 1337.92]  But I would say in this phase of like what model is going to be good for me, go ahead and
[1337.92 --> 1342.78]  put that sort of hardware concern, although it's important, put it a little bit to the
[1342.78 --> 1349.60]  side and focus on which model is giving me the output behavior that I want, right?
[1349.84 --> 1352.80]  Because you have a certain task in mind, right?
[1352.80 --> 1359.34]  And if you could figure out, hey, this model kind of does what I want, and it seems like
[1359.34 --> 1361.08]  it's giving pretty reasonable output.
[1361.40 --> 1366.94]  And then you find out, oh, well, I can't run it on the GPU that I have, or I need to figure
[1366.94 --> 1368.14]  out how to run this on a CPU.
[1368.38 --> 1373.86]  Then that kind of narrows down the type of tooling that you're going to have to use for
[1373.86 --> 1376.78]  optimization, or you might not need to optimize at all.
[1376.90 --> 1382.16]  So kind of start with the smaller models and build up to something that fulfills the behavior
[1382.16 --> 1387.04]  requirements that you have by just using some of these demos, using some of these spaces,
[1387.04 --> 1393.14]  and then think about, okay, I've now figured out I need Falcon 180 billion.
[1393.58 --> 1397.38]  So what does that look like for me to run that in my own infrastructure?
[1397.38 --> 1401.84]  Then there's kind of a follow-up series of things that we can talk about related to that.
[1402.48 --> 1402.60]  Gotcha.
[1402.84 --> 1403.14]  Thanks.
[1403.22 --> 1407.56]  So I was kind of getting ahead of myself then a little bit in terms of worrying too much
[1407.56 --> 1408.42]  about hardware first.
[1408.78 --> 1409.50]  Yeah, yeah.
[1409.50 --> 1414.78]  I think the question, well, maybe it's because I come from a data science background, right?
[1415.24 --> 1422.06]  My data science experience always tells me, start with the smaller models and work your
[1422.06 --> 1428.68]  way up to the bigger ones until you find something that behaves in a way that will work for you.
[1428.68 --> 1434.28]  And then figure out the kind of infrastructure requirements around that.
[1434.72 --> 1442.02]  Because if you start smaller and work to bigger, it's going to be easier to work with that smaller
[1442.02 --> 1445.14]  model infrastructure-wise and latency-wise and all of that.
[1445.14 --> 1451.26]  But some people do have really complicated sets of problems where they need a really big,
[1451.34 --> 1457.36]  like let's say, you know, I want to produce really, really, really, really good synthesized
[1457.36 --> 1461.24]  speech or really, really good transcriptions from audio.
[1461.44 --> 1467.06]  I'm going to need maybe a bigger model than a really, really small OpenAI Whisper model.
[1467.06 --> 1473.32]  So it has to do with the requirements of your use case as well, I would say.
[1473.90 --> 1474.14]  Okay.
[1474.40 --> 1479.16]  So let's say you identify a model and you've kind of picked what you want to do.
[1479.22 --> 1480.00]  Where do you go from there?
[1480.30 --> 1480.52]  Yeah.
[1480.52 --> 1487.62]  So let's say that you've picked a model and let's take the first case where it's a model
[1487.62 --> 1496.44]  that could reasonably or you think it could reasonably fit on a single processor, a single
[1496.44 --> 1504.58]  accelerator, or by your own sort of infrastructure constraints, you need it to operate on a single
[1504.58 --> 1505.58]  accelerator.
[1505.58 --> 1513.00]  And even if you don't have those infrastructure constraints, I think one recommendation I often
[1513.00 --> 1519.30]  give is it's just way easier to run something on a single accelerator or a single CPU.
[1519.98 --> 1526.26]  So I personally recommend to people, even if it's a bit larger of a model, convince yourself that you
[1526.26 --> 1533.26]  can't run it on a single accelerator or a single CPU before you make the jump to spin up a GPU
[1533.26 --> 1535.04]  cluster or something like that.
[1535.04 --> 1539.76]  It's just a lot harder to deal with, even with good tooling, some good tooling around
[1539.76 --> 1541.18]  that side, which we can talk about.
[1541.54 --> 1543.44]  So yeah, let's say that you found a model.
[1543.68 --> 1544.02]  I don't know.
[1544.08 --> 1546.58]  Let's say it's our Mistral 7 billion model.
[1547.06 --> 1552.62]  You should be able to run that on a single instance with an accelerator or a GPU.
[1553.30 --> 1556.28]  I would then look at that model.
[1556.28 --> 1564.50]  And depending on the type of the model, oftentimes in the model card on Hugging Face, hopefully,
[1564.50 --> 1572.18]  if it's a nicely maintained model in Hugging Face, then it will likely, just like a readme
[1572.18 --> 1577.12]  and GitHub, it will likely have a little code snippet that says, hey, here's an example of
[1577.12 --> 1577.96]  how to run this.
[1577.96 --> 1585.68]  What I usually do in that case is I just spin up a Google Colab notebook because I want to
[1585.68 --> 1588.86]  see how this thing runs and how many resources it's going to consume.
[1589.08 --> 1591.26]  So I'll spin up a Google Colab notebook.
[1591.62 --> 1598.12]  If people aren't familiar, Google Colab is just a hosted version of Jupyter notebooks with
[1598.12 --> 1604.12]  a few extra features, like you can have certain free access to GPU resources.
[1604.48 --> 1610.26]  There's similar things from like Kaggle and Paper Space and Deep Note and a bunch of others.
[1610.26 --> 1615.40]  So spin up one of these hosted notebooks and just copy paste that example code in that notebook
[1615.40 --> 1617.92]  and try a single inference.
[1618.12 --> 1623.72]  And oftentimes what you can do in these environments is if you look up at the top right corner of
[1623.72 --> 1626.84]  Google Colab, there's a little resources thing.
[1626.84 --> 1633.36]  And once you load your model in, you can actually look at, oh, how much GPU memory am I taking
[1633.36 --> 1634.16]  up, right?
[1634.22 --> 1636.60]  How much CPU memory am I taking up?
[1636.68 --> 1640.40]  And that gives you a good sense of, hey, I loaded this model in.
[1640.54 --> 1641.66]  I performed an inference.
[1641.88 --> 1649.64]  If I just do nothing else, like the most naive thing I can do, then I'm consuming 12 gigabytes
[1649.64 --> 1652.16]  of GPU memory or something like that.
[1652.36 --> 1656.76]  And that kind of tells you if you don't do any optimization, then.
[1656.84 --> 1662.86]  You're going to need a GPU card that at least has 12 gigabytes of memory.
[1663.22 --> 1668.36]  And so maybe you use like a A10G or you could use an A100.
[1668.36 --> 1671.10]  That might be a little bit overkill in this case.
[1671.10 --> 1676.16]  But one of these with maybe 24 gigabytes of memory, you have a little bit of headroom there
[1676.16 --> 1681.54]  and you can say now you've narrowed down not only the model, but potentially the hardware,
[1681.76 --> 1688.34]  assuming you don't do any optimization, potentially the hardware that you could use to deploy it.
[1688.38 --> 1691.10]  So as of yet, I haven't spun up really any infrastructure.
[1691.74 --> 1696.18]  This is kind of my standard thing where I'm like, hey, what's the deal with this model?
[1696.18 --> 1698.18]  How do I perform a single inference?
[1698.34 --> 1700.22]  And what kind of resources am I going to need?
[1700.40 --> 1705.62]  It's a nice little cheat code equivalent of finding out what you're getting into, it sounds like.
[1706.04 --> 1707.38]  Yeah, yeah, for sure.
[1707.64 --> 1712.32]  And if you happen to have the other way I've done this in the past is if you happen to have
[1712.32 --> 1718.94]  a VM or maybe it's just your own like personal workstation and you have a consumer GPU card.
[1718.94 --> 1726.74]  If you have Docker running on that system, you could pull down a pre-built, you know,
[1726.88 --> 1733.36]  transformers, hugging face transformers Docker image and just run it interactively.
[1733.52 --> 1739.38]  Open a bash shell into that Docker container and run an inference, just like I said,
[1739.42 --> 1742.28]  or spin up the model, load it into memory in Python.
[1742.28 --> 1747.62]  And then in another tab or another terminal, just run Docker stats and it'll tell you,
[1747.62 --> 1754.40]  you know, how much memory you're consuming and that sort of thing or run NVIDIA SMI or
[1754.40 --> 1760.58]  the similar for other systems or other processors that would tell you how much GPU memory you're
[1760.58 --> 1760.76]  running.
[1760.88 --> 1763.26]  So this is kind of a next phase that I do.
[1763.40 --> 1766.32]  The first is like maybe what kind of model do I want?
[1766.38 --> 1768.88]  The second is how do I run an inference with this model?
[1770.00 --> 1776.86]  Then kind of is a whole branching series of funness, which is either you go down the path
[1776.86 --> 1783.30]  of saying, I want to optimize my model in some way to run it either faster or on fewer resources,
[1783.30 --> 1788.40]  or I want to go down the path of saying, nope, this is fine.
[1788.88 --> 1793.08]  I can run it with the resources that I figured out it needs.
[1793.08 --> 1799.00]  And then you kind of move on to the deployment side of things.
[1799.00 --> 1826.16]  Okay, Chris, let's say that we want to follow the path on our choose your own adventure,
[1826.16 --> 1830.64]  that you want to do some model optimization on your model.
[1830.64 --> 1831.12]  Okay.
[1831.34 --> 1836.58]  The reason you would want to do this is one of two reasons.
[1836.80 --> 1846.60]  One is, hey, it turns out I crashed my Google CoLab trying to run Falcon 180 billion because I ran
[1846.60 --> 1847.70]  out of GPU memory.
[1848.22 --> 1852.34]  And turns out you need more GPU memory for that or multiple GPUs.
[1852.34 --> 1856.96]  And I don't either have access to that or don't want to pay a bunch of money to spin up a GPU
[1856.96 --> 1859.70]  cluster and run the model in a distributed way.
[1860.22 --> 1868.50]  Or it's maybe even a smaller model and you want to run it either faster or on standard non-accelerated
[1868.50 --> 1868.94]  hardware.
[1869.56 --> 1875.56]  Like I heard a talk at GopherCon about a workflow where people were running a model at the edge
[1875.56 --> 1880.54]  in a lab to process imagery coming off of a microscope.
[1881.04 --> 1883.42]  And it was all disconnected from the public internet.
[1883.72 --> 1886.26]  So in that case, you just have a CPU.
[1886.74 --> 1888.40]  Maybe you need to optimize on the CPU.
[1888.94 --> 1894.14]  So there's gradually more and more options that are out there to do this.
[1894.66 --> 1901.76]  Some people might have seen things like Lama CPP, which is sort of a implementation of the
[1901.76 --> 1908.78]  Lama architecture that's very efficient and allows you to run Lama language models on like
[1908.78 --> 1913.98]  your laptop or on like an, I think a lot of people were running them on MacBooks with M1
[1913.98 --> 1915.12]  or M2 processors.
[1915.60 --> 1925.26]  If you want to kind of scroll through this set of optimization stuff, if you go to the Intel
[1925.26 --> 1930.58]  Analytics Big DL repo, that's Big DL, like Big Deep Learning.
[1931.40 --> 1937.78]  First of all, the Big DL library does a lot of this sort of optimization or helps you run
[1937.78 --> 1939.68]  these sorts of models in an optimized way.
[1939.96 --> 1945.18]  But they also have this little note at the top, which is actually a very, I found it to
[1945.18 --> 1947.94]  be a very helpful little index as well.
[1947.94 --> 1956.42]  They say this is built on top of the excellent work of Lama CPP, GPTQ, GGML, Lama CPP Python,
[1956.58 --> 1959.42]  Bits and Bytes, QLaura, et cetera, et cetera, et cetera.
[1959.62 --> 1967.06]  These are all things that people have done to run big models in a smaller way, I guess
[1967.06 --> 1968.48]  would be the right way to put it.
[1968.58 --> 1971.20]  So Bits and Bytes is a good example of this.
[1971.54 --> 1977.48]  Hugging Face has a bunch of blog posts about this where they've run, you know, the big
[1977.48 --> 1985.08]  bloom model in a Google Colab notebook by loading it not in the full precision, but in a quantized
[1985.08 --> 1985.44]  way.
[1985.58 --> 1988.34]  But there's a lot of different ways to do this.
[1988.34 --> 1992.72]  And that's a kind of a good reference to see a bunch of those different ways.
[1993.14 --> 1996.38]  At some point for a future show, we should come back and revisit that.
[1996.46 --> 1997.34]  That sounds really cool.
[1997.66 --> 1998.26]  Yeah, yeah.
[1998.36 --> 2002.16]  And I think it probably deserves a show in and of itself.
[2002.16 --> 2009.32]  People might refer back to an episode that we had with Neural Magic on the podcast where
[2009.32 --> 2017.68]  they talked about the various strategies for optimizing a model to run on commodity hardware
[2017.68 --> 2018.92]  like CPUs.
[2019.04 --> 2023.64]  But there's a ton of different projects in this space, both from companies and open source
[2023.64 --> 2029.08]  projects like OpenVINO and Optimum and Bits and Bytes and all of these.
[2029.08 --> 2035.66]  So if you are needing to take this big model and make it either make it smaller or run it
[2035.66 --> 2041.30]  more optimized on certain hardware, then you might want to go through this model optimization
[2041.30 --> 2042.86]  phase.
[2043.20 --> 2047.98]  Assuming you did that or you didn't need to optimize your model, then we get to deployment.
[2048.82 --> 2055.36]  Now, Chris, what's in your mind when you think of these days, where might people want to
[2055.36 --> 2057.08]  deploy models?
[2057.08 --> 2058.68]  Yeah, I think so.
[2058.92 --> 2065.08]  It's one of those situations where a lot of people I'm talking to are trying to decide
[2065.08 --> 2067.06]  between cloud environments.
[2067.16 --> 2071.98]  And we're seeing some people that had dived into cloud pulling back and investing in their
[2071.98 --> 2076.02]  own and as well as starting to explore some of the other chip offerings.
[2076.26 --> 2082.24]  So people are kind of reconsidering that go cloud when it's too big for you now and looking
[2082.24 --> 2086.52]  at these open models in their own hardware and trying to figure out, okay, I don't really
[2086.52 --> 2087.96]  know how to do that at this point.
[2088.12 --> 2094.50]  So that's where I'm really curious is let's say that we go ahead and buy a reasonable GPU
[2094.50 --> 2097.86]  capability in-house, but it's not too big.
[2097.94 --> 2099.06]  What can I make of that?
[2099.06 --> 2103.98]  If I'm willing to do a little bit of investment, but we're not talking millions and millions of
[2103.98 --> 2104.66]  dollars kind of thing.
[2104.66 --> 2105.80]  Yeah, yeah.
[2106.00 --> 2114.40]  So it might be good for people to kind of categorize the ways that you might want to deploy an AI
[2114.40 --> 2116.52]  model for your own application.
[2116.52 --> 2123.68]  And even before I give those categories, I think I also normally recommend to people that I think
[2123.68 --> 2130.00]  still the best way to think about deploying one of these models, if you're deploying it to support
[2130.00 --> 2135.64]  some type of application in your business or for your own personal project or whatever it is,
[2135.64 --> 2136.60]  any type of scale.
[2136.60 --> 2143.22]  I think you're going to save yourself a lot of time by thinking about the deployment of the model
[2143.22 --> 2151.88]  as a REST API and then your application code connecting to that model or a REST API or a GRPC
[2151.88 --> 2153.58]  API or whatever type of API you want.
[2153.68 --> 2157.06]  But the purpose of the model server is to serve the model.
[2157.62 --> 2160.64]  And then you have your application code that connects to that.
[2160.76 --> 2166.30]  Now, that could be running on the same machine or the same VM as your application code,
[2166.30 --> 2167.90]  or it could be running on a different one.
[2168.40 --> 2173.40]  But as soon as you make that separation a little bit, I don't really promote people
[2173.40 --> 2175.04]  microservice everything.
[2175.30 --> 2179.68]  But I think in terms of model serving, it's useful because you can take care of the concerns
[2179.68 --> 2185.22]  of that model, maybe the specialized hardware it's running on, and then take care of the concerns
[2185.22 --> 2186.66]  of your application separately.
[2187.38 --> 2195.10]  And if your application is a front-end web app or is something written, an API written in Go or
[2195.10 --> 2200.32]  Rust or whatever it is, then you don't have to worry about like, oh, how do I run this in a
[2200.32 --> 2202.18]  different language or that sort of thing?
[2202.26 --> 2204.58]  You just handle that through the API contract.
[2204.92 --> 2206.60]  So that's maybe one.
[2207.16 --> 2211.48]  Kind of classical separation of concerns that any developer would be doing.
[2211.82 --> 2212.02]  Yep.
[2212.16 --> 2212.40]  Yep.
[2212.48 --> 2212.86]  Exactly.
[2212.96 --> 2215.94]  And then you can test each separately, all of that good stuff.
[2216.04 --> 2216.22]  Sure.
[2216.22 --> 2223.68]  But if we think about the categories of how you might deploy these things, there's the
[2223.68 --> 2229.68]  case where you would want to run this in a serverless way.
[2230.04 --> 2234.54]  Like we already talked about what Cloudflare just released, but there's a whole bunch of
[2234.54 --> 2240.80]  these options like Cloudflare and Banana and Base 10 and Modal and a bunch of different
[2240.80 --> 2246.60]  places where you can spin up a GPU when you need it, and then it shuts down our scales
[2246.60 --> 2247.84]  to zero afterwards.
[2248.82 --> 2254.40]  And there are, so depending on the size of your model and how you implement it, the sort
[2254.40 --> 2259.10]  of cold start time or the time it takes to spin up that model and have it ready for you
[2259.10 --> 2262.28]  to use might be somewhat annoying for you.
[2262.36 --> 2264.60]  But the advantage is you're not going to pay a lot.
[2264.76 --> 2266.82]  So you could at least try that first.
[2266.82 --> 2272.68]  There's kind of this more and more offerings in that space, but a lot of them have like,
[2272.76 --> 2278.92]  you know, Base 10, the Cloudflare thing, whatever it is, you're going to be running it in someone
[2278.92 --> 2280.20]  else's infrastructure.
[2280.52 --> 2285.46]  So if you have like your own on-prem thing or something like that, maybe a little bit
[2285.46 --> 2292.68]  harder to deploy that sort of serverless infrastructure because they've optimized those systems for
[2292.68 --> 2293.18]  what they are.
[2293.18 --> 2297.94]  So likely in that scenario, you're signing up for an account on one of these platforms
[2297.94 --> 2302.18]  and you're deploying your model there, and then you can interact with it when you want.
[2302.64 --> 2309.98]  A second kind of way you could do this is like a containerized model server that's running
[2309.98 --> 2316.96]  either on a VM or a bare metal server that has an accelerator on it, one or more accelerators
[2316.96 --> 2317.60]  on it.
[2317.60 --> 2317.96]  Right.
[2318.44 --> 2324.56]  And so you could spin up an EC2 instance with a with a GPU or, you know, you could even
[2324.56 --> 2329.50]  run this as part of an auto scaling cluster that's like a Kubernetes cluster or something
[2329.50 --> 2329.92]  like that.
[2329.98 --> 2334.62]  But these would be VMs that have a GPU attached or something like that.
[2334.62 --> 2341.22]  And they would be probably up either all the time or they would have uptime that's different
[2341.22 --> 2343.58]  from the serverless offerings.
[2343.58 --> 2344.00]  Sure.
[2344.18 --> 2346.44]  And so you'd just be paying for that all the time.
[2346.44 --> 2353.86]  And in those cases, like maybe you could use a model packaging system like Base 10's Trust
[2353.86 --> 2355.14]  is one that I use.
[2355.32 --> 2361.64]  But there's other ones as well, Selden and others that will actually create a model package
[2361.64 --> 2366.10]  in a dockerized way that allows you to deploy your system.
[2366.68 --> 2369.72]  Is there any standardization yet in that space?
[2369.72 --> 2372.10]  Or does each vendor have its own approach?
[2372.10 --> 2374.26]  I think each vendor has its own approach.
[2374.48 --> 2382.18]  Like if you look at Hugging Face, they have the TGI or text generation inference project,
[2382.32 --> 2385.64]  which I think is what they use a lot to serve some of their models.
[2385.94 --> 2391.36]  And that kind of is set up differently than Base 10's Trust, which is set up differently than
[2391.36 --> 2392.84]  Selden's system.
[2393.20 --> 2401.46]  There are some standardization in that, like if you have a general like Onyx model or something
[2401.46 --> 2405.48]  like that, there's various servers that take in that format.
[2405.98 --> 2411.98]  But the way in which you set up your REST API might be different in different frameworks.
[2412.18 --> 2415.36]  So this is a very framework dependent thing, I would say.
[2416.00 --> 2416.12]  Gotcha.
[2416.38 --> 2416.54]  Yeah.
[2416.74 --> 2422.30]  And there's also an additional layer of choice here, not only in terms of what framework you
[2422.30 --> 2425.78]  use, but also in terms of optimizations around that.
[2425.78 --> 2432.24]  So there's certain optimizations like VLLM, which is an open source project that not all
[2432.24 --> 2432.42]  it.
[2432.48 --> 2438.34]  So this doesn't modify the model, but it modifies the inference code that allows the model to
[2438.34 --> 2440.10]  run more efficiently for inference.
[2440.30 --> 2446.40]  So this is not the sort of model optimization that we talked about earlier, which is actually
[2446.40 --> 2449.50]  changing the model in terms of precision or in other ways.
[2449.50 --> 2456.78]  But this is actually a layer of optimization of how the model is called that helps it run
[2456.78 --> 2457.50]  faster.
[2458.06 --> 2463.18]  So yeah, there's a lot of choices there as well.
[2463.74 --> 2469.78]  And I think once you get to that point and you've chosen, like let's say you're using
[2469.78 --> 2476.26]  Base10's trust system and you've deployed your model, you know, either on a VM or in a serverless
[2476.26 --> 2483.22]  environment or you're using whatever system you're using, I think then kind of gets to
[2483.22 --> 2489.18]  these additional operational concerns about like, how do I plug all this together in an
[2489.18 --> 2490.00]  automated way?
[2490.10 --> 2497.10]  So if I push my model to Hugging Face or if I update my inference code, how does that trigger
[2497.10 --> 2502.06]  a rebuild of my server and then redeploy that on my infrastructure?
[2502.06 --> 2509.70]  And that gets closer then into what is more traditionally DevOps-y infrastructure automation
[2509.70 --> 2515.64]  type of things, which is its own whole land of frameworks and options and that sort of
[2515.64 --> 2515.84]  thing.
[2515.94 --> 2520.50]  But it's more of a standardized thing that software engineers are familiar with.
[2520.90 --> 2521.02]  Right.
[2521.46 --> 2528.92]  That's kind of, from my perspective, that's if we were to just summarize, you kind of go from
[2528.92 --> 2534.80]  model selection and experimentation, which I would say, don't spin up your own infrastructure
[2534.80 --> 2536.16]  necessarily for that.
[2536.60 --> 2541.80]  And once you figure out a behavior of a model that works well for you, then decide if you
[2541.80 --> 2544.62]  need to optimize it to run it in the environment you need to.
[2544.92 --> 2546.36]  If so, optimize it.
[2546.36 --> 2555.86]  And then once you're ready to deploy it, think about a model server, which is geared to specifically
[2555.86 --> 2558.26]  inferencing of your model.
[2558.58 --> 2560.26]  And that's the separation of concerns.
[2560.96 --> 2565.72]  And either you can use a framework like one of these we've talked about, or you could build
[2565.72 --> 2571.46]  your own, you know, fast API service around it or whatever API service you like and deploy
[2571.46 --> 2579.92]  it in a way that is ideally automated so that you can do all the nice DevOps-y things around
[2579.92 --> 2580.06]  it.
[2580.06 --> 2581.42]  That sounds really good.
[2581.78 --> 2586.44]  So you've done a fantastic job of laying everything out.
[2586.80 --> 2591.82]  I think I've talked to you hoarse at the moment, trying to cover everything.
[2592.00 --> 2593.44]  Be careful what you ask for, Chris.
[2593.44 --> 2602.08]  So as we are winding up for this episode, what are some of the kind of open source go-to tools
[2602.08 --> 2608.02]  that pop top of mind for you that you tend to find yourself going to over and over again,
[2608.12 --> 2609.38]  you know, for folks to explore?
[2610.00 --> 2617.44]  Yeah, I think on the pulling a model down and running it for inference, just that sort of
[2617.44 --> 2618.26]  series of things.
[2618.26 --> 2625.68]  There's really nothing, in my opinion, that beats the Hugging Face Transformers library.
[2626.14 --> 2628.48]  And this is not for people that aren't familiar.
[2628.64 --> 2632.78]  This is not just for language models and that sort of transformers.
[2633.10 --> 2640.28]  But this is general purpose functionality that you can use also for speech models and computer
[2640.28 --> 2646.56]  vision models and all sorts of models, both in terms of data sets and pulling down models
[2646.56 --> 2649.20]  and extra convenience on top of that.
[2649.32 --> 2653.34]  There's not really anything I think that is more comprehensive than that.
[2653.50 --> 2659.20]  And Hugging Face has a great Hugging Face course where you can online, if you just search for
[2659.20 --> 2661.72]  Hugging Face course, it'll walk you through some of that.
[2662.24 --> 2670.38]  In terms of the model optimization side of things, I would recommend checking on a few different
[2670.38 --> 2670.88]  packages.
[2671.18 --> 2673.32]  One of those is called Optimum.
[2673.32 --> 2682.34]  It's collaboration between a bunch of different parties, but it allows you to load models with
[2682.34 --> 2684.06]  the Hugging Face API.
[2684.54 --> 2689.72]  So similar to how you would load them with Hugging Face, but then optimize them on the fly for
[2689.72 --> 2695.30]  various architectures like CPUs or Gaudi processors or special processors.
[2695.30 --> 2717.48]  In terms of quantization and model optimization of the actual model, like the model parameters, you could look up bits and bytes by Hugging Face, OpenVINO by Intel, this big DL library from Intel, which I mentioned that readme and that GitHub also links to other things that people have done.
[2717.48 --> 2720.48]  So it's nice that you can explore that as well.
[2720.48 --> 2729.58]  And there are other projects like Apache TVM and others that have been around for some time and do model optimization.
[2730.00 --> 2730.12]  Yep.
[2730.28 --> 2731.66]  And we've talked about that one before.
[2732.14 --> 2732.28]  Yeah.
[2732.34 --> 2737.68]  And then on the deployment side, there's an increasing number.
[2737.68 --> 2744.84]  The one that I've used quite a bit is called Truss from Base 10, T-R-U-S-S, like Bridge Truss.
[2745.18 --> 2749.22]  And that allows kind of packaging and deployment of models.
[2749.32 --> 2751.74]  You don't have to use their cloud environment.
[2751.78 --> 2757.60]  You can deploy to their cloud environment if you want, or you could just run it as a Docker container, but it's really this packaging.
[2757.60 --> 2768.42]  But there's other ones I mentioned too, like the TGI from Hugging Face or VLLM if you're interested in LLMs.
[2769.06 --> 2770.94]  So yeah, there's kind of a range there.
[2771.04 --> 2780.48]  And of course, each cloud provider has their option to deploy models as well, like SageMaker in AWS, which a lot of people use also.
[2780.94 --> 2784.82]  So I think you've given us plenty of homework to go out there and explore a bit.
[2785.18 --> 2785.88]  Yeah, yeah.
[2785.88 --> 2787.84]  There's no shortage of things to try.
[2788.24 --> 2798.54]  It can be a little bit overwhelming to navigate the landscape, but I would just encourage people, you know, that first step of figuring out what model you need to use doesn't require you to deploy a bunch of stuff.
[2798.62 --> 2799.86]  Just try it in a notebook.
[2799.86 --> 2809.90]  And once you figure that out, then find a way, even just search for like, oh, you found out you want to use Llama to 7 billion.
[2809.90 --> 2816.78]  Just search for the great thing now is you can search and say like running Llama 7 billion on a CPU.
[2817.42 --> 2822.68]  And there'll be a few different blog posts that you can follow to figure out how people have done that.
[2822.68 --> 2827.54]  And so just follow that path and kind of follow some of the examples that are out there.
[2827.68 --> 2832.16]  It's not like any of us that are doing this day to day don't do the exact same thing.
[2832.16 --> 2848.04]  Like when we deployed recently on the Gaudi processors and Intel developer cloud, I just went to the Hibana Labs repo where they talk about Gaudi and they have like, you know, text generation dot pi example or whatever it was called.
[2848.04 --> 2851.26]  And, you know, there's a lot of copy and pasting that happens.
[2851.44 --> 2852.18]  So that's OK.
[2852.30 --> 2853.52]  And that's how development works.
[2853.82 --> 2854.54]  So fantastic.
[2854.84 --> 2858.38]  Well, thank you for letting me pick your brain on this topic for a while.
[2858.60 --> 2858.92]  Sure.
[2859.70 --> 2863.42]  And like I said, I think you're almost hoarse after this one.
[2863.82 --> 2866.88]  But that was a really, really good instructional episode.
[2866.88 --> 2869.56]  So I'll actually personally be going back over it.
[2869.94 --> 2870.12]  Cool.
[2870.24 --> 2871.14]  Well, it's fun, Chris.
[2871.26 --> 2873.30]  Thanks for letting me ramble on.
[2873.52 --> 2876.98]  And I'm sure we'll have some follow ups on similar topics as well.
[2877.56 --> 2878.00]  Absolutely.
[2878.28 --> 2878.72]  All right.
[2878.82 --> 2880.44]  Well, that'll be it for this episode.
[2880.66 --> 2885.20]  Thank you very much, Daniel, for for filling both the host and the guest seat this week.
[2886.02 --> 2887.44]  Another fully connected episode.
[2887.56 --> 2888.38]  I'll talk to you next week.
[2888.58 --> 2888.78]  All right.
[2888.84 --> 2889.42]  Talk to you soon.
[2897.42 --> 2900.24]  Thank you for listening to Practical AI.
[2900.76 --> 2904.56]  Your next step is to subscribe now if you haven't already.
[2905.00 --> 2911.04]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2911.54 --> 2916.42]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2917.00 --> 2920.80]  Check out what they're up to at Fastly.com and Fly.io.
[2920.80 --> 2926.52]  And to our beat freaking residents, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2926.80 --> 2927.70]  That's all for now.
[2927.96 --> 2929.12]  We'll talk to you again next time.
[2929.12 --> 2929.54]  But.
[2934.92 --> 2935.22]  Thank you.
[2941.22 --> 2941.42]  Thank you.
[2941.64 --> 2945.80]  Thank you.
