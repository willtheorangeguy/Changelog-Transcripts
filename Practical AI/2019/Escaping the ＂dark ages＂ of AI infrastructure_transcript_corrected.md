[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.36 → 18.18] This episode is brought to you by DigitalOcean.
[18.58 → 19.22] Guess what?
[19.42 → 24.22] DigitalOcean recently added MySQL and Regis to their list of managed databases.
[24.42 → 29.12] Their full managed databases lineup now includes the three most popular databases out there for developers.
[29.12 → 31.82] Postgres, MySQL, and Regis.
[32.26 → 36.76] Eliminate the complexity involved in managing, scaling, and securing your database infrastructure.
[37.20 → 40.60] And instead, get back to focusing on building value for your users.
[41.20 → 45.70] Learn more and get started for free with a $50 credit at do.co slash Changelog.
[45.84 → 47.98] Again, do.co slash Changelog.
[59.12 → 66.20] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[66.72 → 71.08] This is where conversations around AI, machine learning, and data science happen.
[71.58 → 75.84] Join the community and slack with us around various topics of the show at changelog.com slash community.
[76.18 → 77.02] Follow us on Twitter.
[77.12 → 78.60] We're at Practical AI FM.
[78.86 → 79.92] And now onto the show.
[79.92 → 87.60] Welcome to another episode of the Practical AI Podcast.
[87.96 → 88.96] My name is Chris Benson.
[89.14 → 91.62] I'm a principal AI strategist at Lockheed Martin.
[91.88 → 97.58] And with me, as always, is my co-host, Daniel Whiten ack, who is a data scientist with SIL International.
[97.76 → 98.54] How's it going today, Daniel?
[99.20 → 100.96] It's going perfect.
[101.06 → 106.04] It's Thanksgiving week here in the States for those that are listening from the States.
[106.04 → 107.86] So a little bit shorter week.
[107.98 → 109.46] I'm working through Wednesday.
[109.78 → 113.82] So it's a good week and I feel like I've been reasonably productive.
[114.16 → 115.00] So what about you?
[115.38 → 116.32] Same for me.
[116.40 → 121.68] I'm working through Wednesday, but I'm looking forward to having a long weekend ahead.
[121.78 → 123.30] Do you have any special plans for Thanksgiving?
[124.08 → 126.34] Well, just Thanksgiving dinner.
[126.46 → 130.28] But then I'm going to help out my wife, who has a candle business.
[130.74 → 134.42] And Cyber Monday weekend is pretty insane for them.
[134.42 → 137.38] It's a company called Antique Candle Co.
[137.52 → 140.68] And they're going to ship out a kind of insane number of orders.
[140.80 → 144.40] So I'll probably be packing boxes with candles, which will be a nice, you know,
[144.58 → 148.04] break from staring at a screen and something completely different.
[148.56 → 150.36] So no AI in that one.
[151.18 → 152.32] Not yet.
[152.40 → 156.48] Although, I mean, so I help them with some like marketing and Facebook ad stuff.
[156.54 → 161.44] And obviously in advertising, it is interesting to kind of come from the AI perspective
[161.44 → 165.96] because you see certain things like in Facebook ads where it's talking about, you know,
[166.02 → 167.80] optimization and learning.
[167.90 → 172.52] As you kind of kick off the ad, there's like a learning phase where it's kind of figuring
[172.52 → 178.30] out how to optimize the placement, the placements and the and the cost and all that.
[178.40 → 181.76] And so it's interesting to think about it from that perspective, for sure.
[182.20 → 182.58] Fantastic.
[182.58 → 186.64] Well, you know, we need to include a link to your wife's business in the show notes.
[187.10 → 188.28] And I certainly will.
[188.44 → 189.24] Shameless plug.
[189.50 → 189.92] There you go.
[190.00 → 192.86] In case there are any AI people who want to jump into candles.
[193.06 → 195.68] So I guess for me, I'm just taking a breather next week.
[195.80 → 199.38] I'm at Carnegie Mellon University for an AI conference to do a panel.
[199.78 → 200.58] And yeah, that sounds great.
[200.66 → 200.86] Yeah.
[200.88 → 203.72] And then finishing up the week with two things in a row.
[203.72 → 210.54] I'll be in Philadelphia doing an AI and ethics talk as a keynote at an ethics conference.
[210.54 → 216.38] And then I'm finishing Friday night in Austin where the final Alpha Pilot, which we've had
[216.38 → 219.72] an episode on the world championship race will be there.
[220.06 → 223.70] And at the end of that race that evening, we're going to hand out a $1 million check to
[223.70 → 224.02] the winner.
[224.68 → 225.36] Exciting stuff.
[225.36 → 225.56] Yeah.
[225.82 → 226.58] Pretty big deal.
[226.64 → 231.12] If anyone's interested in hearing more about that, we have an Alpha Pilot episode from not
[231.12 → 233.86] long ago, and you're welcome to tune into that.
[234.26 → 238.80] But turning to today, we have a fantastic guest.
[239.04 → 244.54] We have Evan Sparks, who is the co-founder and CEO at Determined AI.
[245.32 → 246.54] Evan, welcome to the show.
[247.26 → 248.22] Thanks so much for having me, guys.
[248.26 → 249.76] It's a pleasure to be speaking with you today.
[250.54 → 251.70] Pleasure to have you on the show.
[251.70 → 255.82] If you could just kind of start us off giving us a little bit of background about yourself,
[256.06 → 260.12] kind of how you got to where you're at this point before we dive into Determined AI.
[260.12 → 261.34] Yeah, absolutely.
[261.58 → 266.76] So as it pertains to my sort of career around machine learning and AI, I really kind of got
[266.76 → 271.08] my start in that space, kind of fresh out of college in quantitative finance.
[271.18 → 272.32] So this is the mid-2000s.
[272.58 → 276.96] I was working for an asset manager based in Boston, where we were doing applied machine
[276.96 → 280.80] learning to the stock market to pick stocks and trade client portfolios.
[280.80 → 284.42] When I was in, I did my PhD in physics.
[284.72 → 287.88] And this was like before the sort of data science hype.
[288.04 → 292.88] But the rumour I always heard for like people that got out of academia was there was like,
[293.48 → 296.82] oh, you can go do all this cool math stuff and finance.
[297.36 → 299.38] But I never quite figured out how to do that.
[300.08 → 303.40] Yeah, I mean, there definitely was a very common career path.
[303.44 → 307.58] And it's funny, you know, probably a few years later, everybody then went into ad tech or something
[307.58 → 308.22] like that.
[308.36 → 311.56] And, you know, now it's probably autonomous vehicles or something.
[311.90 → 315.70] There's always an interesting corner in a hot area to be doing this stuff, which is one of
[315.70 → 317.76] the things that I find super fascinating.
[318.14 → 321.98] So in a few years of that client finance thing, I found that other people really, you know,
[322.24 → 324.20] liked looking at PE ratios all day.
[324.24 → 324.98] And that wasn't for me.
[325.04 → 327.78] I was much more interested in sort of the technology problems we were solving.
[328.24 → 332.32] Ended up going to work for a startup in the NLP space called Recorded Future.
[332.32 → 338.30] So we were, you know, building, taking the web and throwing it through this massive NLP
[338.30 → 342.60] engine and building kind of structured data products based on it and trying to figure out
[342.60 → 347.04] how we sell that kind of structured data to places like trading firms, but also like the
[347.04 → 348.76] federal government and so on.
[348.82 → 353.26] And ultimately, that company sort of found a good niche in threat intelligence, basically
[353.26 → 358.68] trying to build predictive indicators of where cyberattacks are going to happen and so on.
[358.68 → 362.52] But again, with the same kind of data driven sort of machine learning technology.
[363.12 → 369.40] And so, you know, in many ways, the roles were pretty similar, one being kind of in financial
[369.40 → 374.08] services, but the other being in this kind of totally different startup kind of environment.
[374.62 → 379.24] But, you know, always building models and kind of driving kind of forward data products.
[379.42 → 383.34] And in both cases, though, I found I was spending much more time building and maintaining my
[383.34 → 387.26] own infrastructure than I was kind of worrying about the modelling problems.
[387.26 → 391.28] And so, you know, and it was really the case in those days, this is kind of like,
[391.48 → 397.38] figure around 2010, 2012, as Hadoop was kind of becoming popular, and so on, where as soon as
[397.38 → 401.48] I was tasked with analyzing a data set that didn't fit in memory on my laptop,
[401.84 → 403.64] my world just like collapsed, right?
[403.70 → 407.38] And you were forced to like, figure out how to write and reproduce jobs and so on.
[407.88 → 414.82] And I took that as kind of good signal to go back and invent the world that I wanted to live in,
[414.82 → 420.36] in grad school. So I had the good fortune to join the AMP lab at UC Berkeley, right around the time
[420.36 → 426.48] that Apache Spark was born. And my co-founder at determined AI, Amit Tal Walker, and I got to work
[426.48 → 431.48] kind of right away building out kind of the machine learning ecosystem to Spark. So we were among
[431.48 → 436.66] the designers and initial contributors to ML Lib, which is the standard library for machine learning
[436.66 → 442.06] in that ecosystem. And the rest of my PhD was really kind of focused on how do we build sort of,
[442.06 → 446.72] how do we give people tools to build end to end machine learning applications and optimize them
[446.72 → 449.38] in, you know, a large scale and sort of distributed fashion?
[450.16 → 457.46] So this is a slightly less formal question, but it must have been a perfect fit in terms of,
[457.46 → 461.28] of working on Spark and being named Sparks. I'm assuming it,
[461.98 → 464.24] Spark was not named for Evan Spark.
[464.24 → 471.90] No, absolutely not. I, you know, it was funny. I sat next to Mate Bavaria, who was the creator of
[471.90 → 479.02] Spark in the lab, sort of Spark was around 0.3 when, when I, when I landed in the lab. And the first
[479.02 → 484.22] like few days we sat next to each other, there were this kind of like long, weird stares going on back
[484.22 → 489.38] and forth until finally we kind of broke the ice and made it, made a joke about it. But yeah, it was kind
[489.38 → 494.46] of fortunate coincidence from, from my perspective, I guess you know, there was a long-running joke
[494.46 → 501.26] that my real name was Evan Apache Sparks, but not so much. So yeah, it was a it was good timing.
[501.26 → 506.08] And honestly, the amp lab was a great place to be for what I wanted to study, which is really
[506.08 → 511.64] thinking about where does this intersection of huge volumes of data and machine learning really get
[511.64 → 517.64] real and how do we build our kind of supporting systems to enable this. And so also while at Berkeley,
[517.64 → 523.96] I met my other co-founder at Determined AI, Neil Conway, who's more kind of from the pure
[523.96 → 529.76] distributed systems kind of part of the world. So he'd been a Postgres committer, he was working at
[529.76 → 534.44] kind of quarter patching mess for a while around kind of distributed resource management. Meanwhile,
[534.58 → 540.08] me on the other hand is more kind of dyed in the wool theoretical ML student. And he's now a professor
[540.08 → 544.58] at CMU in the machine learning department. In some ways, you think of me as the person who takes the
[544.58 → 549.14] what those guys do individually, figures out how to mash them together, and then hopefully can figure
[549.14 → 553.82] out how to build interesting applications on top of kind of that intersection of system and machine
[553.82 → 559.58] learning. So while at Berkeley, and I promise this is getting into what we do here at Determined,
[559.74 → 564.28] while at Berkeley, one of the big things that we saw, the big megatrends that was happening within
[564.28 → 569.88] academia first was this shift to deep learning as a primary way that people wanted to be doing
[569.88 → 574.30] machine learning, particularly in industrial settings. And so it started with computer vision
[574.30 → 580.48] and speech. And obviously, more recently, we've seen amazing advances in things like NLP and text.
[581.02 → 587.18] And this meant people retooling, you know, learning how to use tools like TensorFlow, buying GPUs on mass,
[587.52 → 592.68] figuring out how to take this what had been like a tiny corner of academic machine learning,
[592.68 → 599.56] and really kind of make it into an industrially viable technology, and stubbing their toe on a lot
[599.56 → 604.12] of serious problems along the way, right? So you go from, you know, logistic regression that trains on
[604.12 → 610.26] my Spark cluster in a couple of minutes, to like, you know, big week long training runs for large scale
[610.26 → 616.96] image classifiers on a, you know, massive cluster of GPUs, for example, you start to have a lot of design
[616.96 → 621.34] decision baked into your modelling choices that you didn't have before. Things like, you know,
[621.34 → 625.72] just how many layers should this architecture have? How does the model capacity relate to my training
[625.72 → 630.66] data set, and so on, and in ways that are sort of not really intuitive, and end up being really
[630.66 → 636.40] highly empirical. So we saw that. And we also saw that the frameworks, the TensorFlow and the PyTorch,
[636.46 → 642.58] and so on of the world, are perfect at sort of their individual tasks, their tasks with, which is
[642.58 → 648.34] helping you describe what your model is, and get it training on, say, a single or maybe several GPUs on a
[648.34 → 655.74] machine, but terrible at helping model developers through the rest of the workflow associated with
[655.74 → 660.80] getting one of these applications into production. Stuff that you guys have covered on your show
[660.80 → 665.88] before around data labelling, and so on. We don't do any of that at Determined AI. But there are other
[665.88 → 671.32] pieces of the workflow around hyperparameter optimization, architecture search, getting your
[671.32 → 677.22] models to train really fast across a wide variety of different hardware platforms, dynamically managing
[677.22 → 683.46] resources in the cloud, say, so that you can, you know, pay for the GPUs only while you're really
[683.46 → 689.62] using them. All of that stuff is sort of handled right now on a manual basis, honestly, with
[689.62 → 694.68] bash scripts and duct tape in many cases. And people don't really have a good way to support their more
[694.68 → 700.32] general workflows as they're in this model development process. And so at Determined AI, that's really the
[700.32 → 706.20] the gap that we serve to fill. How do we enable you to do the rest of the pieces of your
[706.20 → 710.18] workflow, while still using the tools that you know, and love your TensorFlow, your PyTorch, your
[710.18 → 715.56] Keras, etc, but make you much more productive as kind of individual engineer, but more importantly,
[715.56 → 720.12] as a team of engineers, how do you share your results in a reproducible fashion? And how do you make
[720.12 → 725.48] sure that I can get the same model out of my infrastructure as you do? And so, you know,
[725.60 → 727.44] at Determined AI, that's really what our mission is.
[727.44 → 734.34] Yeah, so I'm curious to dive into to a few pieces of that. But you mentioned in one of the blog posts
[734.34 → 740.32] on Determined AI about, you know, people still kind of living in the dark age of AI infrastructure,
[740.32 → 747.22] where certain larger companies have built sophisticated AI native infrastructure for their
[747.22 → 753.88] own use, but everybody else's is kind of struggling. I'm curious if that sort of dark age that you're
[753.88 → 759.64] seeing is due to the fact that, like you say, that there's all these other pieces of the AI workflow
[759.64 → 767.66] that might be data pre-processing, model deployment, model optimization, all of these other things,
[767.76 → 773.78] data labelling, like you mentioned, is it that the tools for those other pieces of the workflow are not,
[774.48 → 781.68] there aren't good tools for those? Or is it that, like, they don't play well together in a sort of
[781.68 → 787.00] all-in-one workflow? Or just that, you know, like people haven't developed, had enough time to
[787.00 → 791.40] develop standardized methodologies around these things? What do you see as kind of the main
[791.40 → 792.30] contributor there?
[792.76 → 798.42] Yeah, I think it's a little bit of both. So I think that, you know, you hit the nail on the head with
[798.42 → 805.42] the in many cases, there are individual tools and point solutions to some of the problems that you
[805.42 → 811.02] mentioned. So there are toolkits for model compression. There, you know, are services and open source
[811.02 → 815.88] libraries for just hyperparameter optimization and so on. Even sometimes full companies built around
[815.88 → 822.88] these things. But in our view, you know, what ends up being a result of that is that you get these tools
[822.88 → 828.72] that are isolated and don't, aren't designed to work well with one another. And more importantly,
[828.72 → 834.64] you then miss sort of broader opportunities that might exist around optimizing sort of the entire
[834.64 → 839.08] workflow. If you can kind of step back and look at that, rather than, you know, individually,
[839.08 → 844.44] like, how do I make this particular piece of the puzzle go absolutely as fast as possible?
[844.92 → 850.44] Sure, you eliminate that bottleneck, but you might still be completely bottlenecked on ETL or data
[850.44 → 856.00] collection or training time, for example. And so you have to be careful as an organization about where
[856.00 → 860.96] you're investing your time and your resources in terms of making those things better. We think that
[860.96 → 865.58] a more holistic design, that is one where the pieces are kind of designed and know about each other,
[865.58 → 873.64] opens the door for certain types of optimizations. So to give you an example, we have our resource manager
[873.64 → 880.88] that is built into our product at Determined AI is totally AI aware, it's aware of the fact that what you're
[880.88 → 889.34] doing with running your jobs on our system, all the jobs are somehow related to training or running inference
[889.34 → 896.34] models. And you can start to make a bunch of interesting assumptions about the workload that
[896.34 → 901.28] you couldn't if this was just general purpose compute. For example, the idea that these things are iterative,
[901.54 → 907.48] and that they have intermediate state like model weights and state of the optimizer that can be used
[907.48 → 912.70] to sort of checkpoint and understand where the computation was and then reschedule it, say, to run on
[912.70 → 918.82] another device. Now, we have that kind of design in the resource management section. But then
[918.82 → 923.48] when we're designing our hyperparameter tuning algorithms, for example, and implementing them,
[923.64 → 928.90] we can take full advantage of knowing what that internal scheduling layer looks like, and use
[928.90 → 933.46] properties of that scheduling layer that we couldn't if we were just running this as like a black box job
[933.46 → 939.92] on top of something like Spark or, or Kubernetes or whatever. And that power of sort of these components
[939.92 → 944.80] being designed with one another in mind allows us to do this job much more efficiently in a much more
[944.80 → 950.56] fault-tolerant and resource aware kind of way than we would be able to otherwise. If you're spending 90% of your
[950.56 → 956.72] time kind of starting up the cluster and getting it done, that's a lot of wasted cycles for your GPUs that your
[956.72 → 960.92] data scientists really want to be putting to work, you know, finding good models and solving your problems.
[961.62 → 968.40] So I'm curious, you mentioned kind of a more holistic view of AI infrastructure. And I know that
[968.40 → 974.16] something that can happen, because there are so many pieces to this, that you can end up in with
[974.16 → 980.14] scenarios and companies where you have a data engineering team or something that's in charge
[980.14 → 985.12] of all of this, like pre-processing and getting data sets ready. And then you have like, the modelling
[985.12 → 992.50] group, and then you have like, deployment and app, people app integration group people,
[992.50 → 1001.26] do you see that trend disappearing as things are kind of tighter, more tightly and better integrated
[1001.26 → 1007.82] together? Or do you think it's reasonable that, you know, a data scientist could take something all
[1007.82 → 1012.96] the way through that whole cycle, I guess, could and should, should they be doing that?
[1013.34 → 1019.78] I think it depends on the company and kind of the the the scale of the application that's under
[1019.78 → 1025.06] development. For example, if you're building a self-driving car, that's probably not a job for
[1025.06 → 1029.62] a single data scientist, I would really hope, right? You know, that's an it's sort of call it a
[1029.62 → 1033.60] generational moonshot, if you will. And there, it makes perfect sense that you're going to have
[1033.60 → 1040.54] massive team of people just worrying about data labelling and data ingest and ETL, another set of
[1040.54 → 1045.52] people just working on kind of the perception pieces of the job, another set of people just working
[1045.52 → 1050.38] on maybe a different component around path planning, and so on. And so there, you know, in those
[1050.38 → 1055.76] scenarios, you really want to think about, okay, what are the various teams? And what are the personas
[1055.76 → 1061.18] of the users of a broader machine learning platform? What do they care about? And how do we facilitate
[1061.18 → 1066.66] coordination and communication between those teams? In other cases, companies have done a perfect
[1066.66 → 1073.04] job of cleaning up their data, putting it into, you know, massive data warehouses, and making it,
[1073.04 → 1078.14] you know, even making their feature catalogue, say, self serve, and the kind of thing where a data
[1078.14 → 1085.90] scientist who says, hey, I'm looking for a fraud model for mobile purchases in Southeast Asia. That's,
[1086.06 → 1090.74] you know, we've decided we're losing enough money on that particular area that a specialized model on
[1090.74 → 1095.76] this particular part of the world makes sense. In those cases, I do think that proper infrastructure
[1095.76 → 1101.76] can enable a data scientist to go from, you know, start to finish all the way. And ideally, you want to get
[1101.76 → 1107.22] that person to the point where they don't have to work directly with a data engineer to get,
[1107.60 → 1112.34] you know, the features flowing through the system and so on. And in my view, almost more importantly,
[1112.62 → 1117.04] or places that we see people get tripped up is around sort of deployment and monitoring of those
[1117.04 → 1122.86] models. We see people often taking models that are, you know, building PyTorch or TensorFlow or
[1122.86 → 1129.10] whatever, and like completely rewriting these things in C++ or Scala or whatever, because that's what
[1129.10 → 1134.02] fits into the production serving environment. That side of things, you know, we see these
[1134.02 → 1138.84] deployment engineers, that's a job I would love to see go away in the common case, if the
[1138.84 → 1144.62] infrastructure gets better. You want data scientists to be able to sort of get to the point where
[1144.62 → 1149.10] they're confident that it works well enough on test sets, and maybe even start to A-B test it,
[1149.10 → 1154.72] and then, you know, hit a button and deploy it more broadly to the fleet. Reducing that friction
[1154.72 → 1160.18] in that time is definitely kind of a central thing I think we need as an industry in order to make
[1160.18 → 1162.70] these technologies more viable and successful.
[1162.70 → 1181.98] If you like this show, I bet you'd enjoy listening to Go Time. Not working with Go? Don't hit that
[1181.98 → 1186.46] fast-forward button quite yet. Go Time covers a wide range of topics, including cloud infrastructure,
[1186.82 → 1192.38] distributed systems, microservices, Kubernetes, and Docker. Not only that, but they have a ton of
[1192.38 → 1195.96] fun doing it. Listen to this clip from a recent episode on security.
[1197.34 → 1201.58] I'm very excited about this. Before we start, I'd like to just try an experiment. This is a
[1201.58 → 1207.90] security podcast. I just want to try something. Bear with me. Hey Siri, play Never Going to Give You
[1207.90 → 1213.24] Up by Rick Astley. Okay, Google, play Never Going to Give You Up by Rick Astley. Alexa, play Never Gonna
[1213.24 → 1220.02] Give You Up by Rick Astley. So I just want to see if that does hack anyone's home devices. And please
[1220.02 → 1225.82] let me know in the Slack channel or on Twitter if it does. Do you just hack yourself? I just hacked
[1225.82 → 1234.40] myself. It's not hacking if you hack yourself, is it? Go Time is a riot. Check it out at changelog.com
[1234.40 → 1240.18] slash Go Time or subscribe to our master feed at changelog.com slash master and let your podcast
[1240.18 → 1244.16] client download all the shows that we produce. Then you can pick and choose the ones you're interested
[1244.16 → 1248.26] in the most and skip the rest. What have you got to lose? All right, back to the show.
[1248.26 → 1270.40] So Evan, I'd like to ask, what are some of the unique challenges that are related to team
[1270.40 → 1277.28] interactions that you're seeing in terms of sharing data, sharing GPUs, and other aspects
[1277.28 → 1282.04] of jointly utilizing AI infrastructure? Could you speak to some of those challenges for us?
[1282.44 → 1288.72] Yeah, I think from our perspective, so the data piece is one that every organization faces,
[1288.92 → 1294.56] particularly organizations who are dealing with sensitive data. And that is something that we've
[1294.56 → 1301.88] seen users kind of figure out on their own. They have a versioned role-based access control system
[1301.88 → 1307.74] on their primary stores of data, at least the interesting data, oftentimes the data that contains
[1307.74 → 1313.36] PII and that sort of thing. They really tightly regulate who gets access to those resources and
[1313.36 → 1318.64] the data resources and when, as they should. From our perspective, it's really about integrating with
[1318.64 → 1324.84] those various kinds of authentication mechanisms and supporting security on those data stores. So we do
[1324.84 → 1330.12] that out of the box. The second and third pieces, I think, that are harder for organizations that most
[1330.12 → 1336.24] people don't really have an answer for. Our first sort of resource sharing. So the rude awakening that
[1336.24 → 1343.12] many people get into with GPUs in general is they're really expensive. And you're talking about spending
[1343.12 → 1351.06] upwards of $150K on, say, a DGX1, which is one of NVIDIA's latest servers filled with V100s. And
[1351.06 → 1357.76] one of those might be good for two data scientists. But in order to enable your team to really be productive,
[1357.76 → 1364.34] you need several of those kinds of servers. And we see people doing really immature things with
[1364.34 → 1370.42] these systems. We see people managing them with either like static allocation, meaning Joe gets
[1370.42 → 1378.06] GPUs one through four on this box and Kyle gets five through eight, you know, kind of forevermore,
[1378.20 → 1382.94] or they've got like some kind of Google Calendar system set up. And this is some really sophisticated
[1382.94 → 1387.06] organizations that we run into where that's the way they're managing this expensive resource.
[1387.06 → 1392.56] Do you think that's just because of like the mixed background of people working on this sort of
[1392.56 → 1399.14] technology that a lot of people are coming from, you know, science or maybe non computer science
[1399.14 → 1402.18] or non software engineering background? Or do you think it's more than that?
[1402.32 → 1407.38] Yeah, totally. I think that is a big so that's a big piece of it. And honestly, people who are really
[1407.38 → 1413.04] good at thinking about convex holes and the right shape of your loss function, and so on,
[1413.04 → 1418.86] probably shouldn't be wasting their time, honestly, thinking about like the right way to do resource
[1418.86 → 1423.58] management, that problem has been solved in a bunch of different domains. And we, you know,
[1423.62 → 1427.68] that should be a layer of abstraction. And that's one that we provide to folks. There are other
[1427.68 → 1431.48] solutions to this problem as well, that some of the cluster resource managers that I mentioned earlier,
[1431.48 → 1436.80] like Kubernetes, or we see people using, you know, queuing systems like Slum from the HPC world,
[1436.80 → 1441.10] those things all have their drawbacks. But you know, in general, this is like, this is a problem
[1441.10 → 1445.24] that modellers don't want to be thinking about. And more generally, I think we need better, you know,
[1445.40 → 1446.48] abstractions for these folks.
[1446.98 → 1452.72] So that's certainly a challenge. I mean, I've been at two large organizations, one that I'm still at,
[1452.78 → 1460.92] Lockheed Martin, where we have many DGX systems within the enterprise. And we are from a kind of AI
[1460.92 → 1466.60] oriented high performance computing context, trying to make these resources as broadly available,
[1466.60 → 1471.36] as possible, kind of conceptually, how do you think about that? Obviously, you will see
[1471.36 → 1476.50] organizations that start off doing this, you know, you get a GPU, and you get a GPU and all that,
[1476.50 → 1480.54] but that's not that doesn't scale against the workloads that, you know, certain teams,
[1480.54 → 1484.72] they only need one GPU at a time, and it may not take very long. And others might need dozens
[1484.72 → 1490.84] for a much longer period of time and everything in between. Conceptually speaking, how do you approach
[1490.84 → 1496.22] differentiating between users and the various differentiated workloads that they're having to
[1496.22 → 1497.02] contend with?
[1497.38 → 1502.72] We love to see people that try and plan for this sort of thing, right? They try and get a sense of,
[1503.24 → 1508.10] okay, I know I have this data volume coming in next year. I know, roughly speaking, it's going to
[1508.10 → 1513.14] take me this long on this many GPUs to train my models. Let's set aside budget and bring those
[1513.14 → 1518.32] resources on-prem or secure them, you know, with long-term leases on one of the cloud providers
[1518.32 → 1523.94] for the most part. Now, that does a good job at kind of helping you plan for your base load,
[1524.02 → 1528.96] right? But then, as always, there's going to be things that come up, like towards the end of the
[1528.96 → 1533.18] quarter, or a new model family comes out, or a new project takes really high priority that you've
[1533.18 → 1539.90] just got to ship. In which case, we see, you know, real benefits to bursting onto cloud resources.
[1540.46 → 1546.00] And so, within the context of our system, that's a core feature that we offer. We call it elastic AI
[1546.00 → 1551.04] infrastructure. And the basic idea is that if the system is configured and there's budget within the
[1551.04 → 1557.24] organization and so on, you can do that dynamic sort of provisioning of those cloud resources,
[1557.40 → 1562.18] spilling work over onto them. We handle sort of the data transfer and other aspects of that planning
[1562.18 → 1567.42] for you. And then, you know, as the workload goes down, those resources are released and the
[1567.42 → 1572.10] organization can save money. So, we think it's a combination of, you know, having good planning,
[1572.10 → 1576.92] but also maintaining some flexibility in your systems and your processes are required to
[1576.92 → 1582.82] really help AI scale within the enterprise. I know one of the things that I've talked to people
[1582.82 → 1588.70] about as they've talked about this particular problem is the fact that the data transfer,
[1588.70 → 1594.36] as you're trying to scale new, like GPU nodes in the cloud or something, if you have to, you know,
[1594.42 → 1602.08] transfer 200 gigabytes of data very frequently, that could be a downside. Are there ways around
[1602.08 → 1607.50] the sort of, you know, data management piece while still keeping things elastic?
[1608.26 → 1613.50] Yeah. So, when we see people kind of in sort of hybrid cloud and on-premise environments,
[1613.90 → 1620.92] we like to take a look at what their infrastructure is for replicating that data. And we'd like to see
[1620.92 → 1625.32] it is sort of continuous where the copy of the data that lives on the cloud and the copy of the data
[1625.32 → 1629.82] that lives on-premise are maintained in a way that they're not exactly identical necessarily,
[1629.82 → 1635.40] but very, very close, or there is a path for them to become identical very quickly. So,
[1635.46 → 1638.98] that sort of incremental process ends up being important. The other side of things I'd say is,
[1639.08 → 1644.06] you know, with all this discussion about just how big the data sets have gotten and how much data you
[1644.06 → 1650.58] need to fuel deep learning and so on, we are mostly looking at customers where like the upper bound on
[1650.58 → 1656.42] the size of the training set they're dealing with is like order of terabytes. And that is a lot
[1656.42 → 1661.08] easier to manage and transfer and move around. It's still hard. You don't want to do it a hundred
[1661.08 → 1666.26] times a day or whatever, but it's easier than, than say moving petabytes, which is, you know,
[1666.30 → 1671.94] the scales that, you know, a lot of people are in the Hadoop space and so on, we'll talk about.
[1671.94 → 1677.94] And so, that gives you a little bit more flexibility and makes the data transfer being the big bottleneck
[1677.94 → 1680.76] in our experience is often the exception, not the rule.
[1681.38 → 1687.86] Yeah. So, it's good to hear that terabytes is small data now. It's only big data when we get to
[1687.86 → 1693.34] petabytes, I guess. I'm just kind of curious. I'm pretty fascinated with kind of, as you've taken us
[1693.34 → 1699.98] through the approach, I'm curious as you're looking out kind of at the competitive landscape,
[1699.98 → 1706.08] as you see different organizations tooling up, you know, everything from the giant companies like
[1706.08 → 1712.38] Google and Microsoft and Amazon and such to smaller startups in the space like you. How do you think
[1712.38 → 1716.98] about yourself in a competitive advantage mode? Like, what do you really think differentiates
[1716.98 → 1720.14] yourself from those out there? How do you think about that in your head?
[1720.44 → 1724.94] I think there are a couple of key things. One, we've got some pretty unique expertise on the team
[1724.94 → 1730.18] kind of in this space. These are problems we've been thinking about really deeply, both in an academic,
[1730.38 → 1736.06] but also professional setting for collectively the team dozens of years, right? And we've got
[1736.06 → 1741.28] a track record of delivering some really popular and influential technology in this space.
[1741.74 → 1747.00] The other thing I'd say is, I think the cloud vendors are there to build their platforms to
[1747.00 → 1751.86] help monetize their hardware, you know, the GPUs that they've invested in, they want to get people
[1751.86 → 1759.32] using and so on. And so, all of it is, you know, Google pushing Google's cloud or Amazon pushing their
[1759.32 → 1765.60] cloud and so on. Where we differentiate ourselves is by being really neutral to the vendor. We will give
[1765.60 → 1771.24] people access to the best, cheapest, you know, correct technology for their particular workloads.
[1771.82 → 1779.22] And you're already seeing signs of vendors getting kind of custom hardware for these particular tasks.
[1779.70 → 1783.84] So, Google has TPUs now. Microsoft just announced a partnership with Graph core.
[1784.24 → 1790.74] There are sort of, and you can bet that Amazon is working on AI-specific hardware. There are going to be
[1790.74 → 1796.56] a bigger menu of hardware choices to be available to help you solve these problems down the road.
[1796.66 → 1801.38] And we think that developers, in the same way they don't want to be worrying about, like,
[1801.46 → 1805.78] the resource management and the calendar system, they definitely don't want to be worrying about
[1805.78 → 1812.40] reprogramming their applications and figuring out which chip is best for this version of my language
[1812.40 → 1817.56] model and so on. And we think that layer of abstraction from a systems level can offer that kind of
[1817.56 → 1822.16] flexibility. So, you submit your job to us. We figure out what the best hardware to run it on is.
[1822.22 → 1826.58] We go acquire that for you. Your job gets built and run. And then those resources are released.
[1826.74 → 1831.28] That basic idea, I think, is something that we can do, and we'll be able to do better than
[1831.28 → 1835.50] the larger cloud vendors because we won't have these exclusive ties to one or the other.
[1836.18 → 1839.28] So, that kind of leads me a little bit into a next question,
[1839.28 → 1846.12] which is around automation and, I guess, more specifically around AutoML methods. So,
[1846.30 → 1852.42] I see AutoML mentioned quite a few times on the site. And also, I mean, there's been kind of a
[1852.42 → 1860.14] general trend of sort of AutoML platforms being released like Google Cloud AutoML or H2O driverless AI.
[1860.50 → 1865.28] And there seems to be a lot of focus in this area. I was wondering, you know, it probably makes sense
[1865.28 → 1871.82] to people like one problem that AI people are going to have is managing their like GPU infrastructure.
[1871.82 → 1877.82] But maybe people think that the like hyperparameter tuning and the modelling side of things is kind of
[1877.82 → 1883.52] their baby, and they don't want to mess with things like that. What do you see as some of the major
[1883.52 → 1889.32] advantages of automating some of that piece of things and utilizing some of these AutoML methods to
[1889.32 → 1894.86] kind of automatically figure out architectures, automatically figure out the right hyperparameters,
[1894.86 → 1900.48] or automatically do other things? What role do you see that playing in the sort of future of AI
[1900.48 → 1901.04] infrastructure?
[1901.82 → 1908.56] Yeah, so I think the way we think about it right now is that you've got these experts who are highly
[1908.56 → 1915.18] trained in their particular fields, you know, maybe they're really great at understanding the physics
[1915.18 → 1923.34] of solar flares or, you know, understanding how robotics works or whatever it is. And yet,
[1923.34 → 1929.16] they're spending a lot of their time doing highly tedious tasks. So manually, you know,
[1929.22 → 1933.48] hit it, looking, telling the end of the log files, figuring out what the loss looked like,
[1933.84 → 1938.52] deciding, is this an area I want to keep investing in? Or should I try radically different model
[1938.52 → 1943.42] architecture, that sort of thing. And then writing the same, you know, 50 nested before loops to
[1943.42 → 1949.16] tune over my parameters and over and over again. And when there are better algorithms out there for
[1949.16 → 1953.42] this stuff, either they don't know about them, or they don't have time or interest in implementing
[1953.42 → 1959.92] them. And they don't quite realize it's easy and narrow to miss the fact that much of this work
[1959.92 → 1964.94] could be, you know, totally automated away, or at least partially automated away. And so our view is
[1964.94 → 1970.62] really, we want to give these practitioners power tools, right? Instead of saying, like, we're going to
[1970.62 → 1976.62] build a robot that builds a house for you. Let's take a carpenter and equip him with power hammer and the
[1976.62 → 1982.10] circular saw and so on. That's kind of the phase where we think that we're in with when it comes
[1982.10 → 1987.82] to AI development. And so if you can equip experts with tools, again, new layers of abstraction that
[1987.82 → 1992.54] they can reason about, say, move from, you know, fiddling with the knobs individually to reasoning
[1992.54 → 1997.92] about search spaces and budgets around how many, say, GPU hours you want to put into solving a
[1997.92 → 2002.84] particular problem, and then letting the system pick the right algorithm for, say, hyperparameter
[2002.84 → 2008.08] optimization or the right way to approach that problem, we see really terrific gains. We've had
[2008.08 → 2012.74] customers tell us that they were able to replicate what had been, you know, a two-month process of
[2012.74 → 2017.74] manually tuning hyperparameters and selecting model architectures in a single overnight run of our
[2017.74 → 2022.82] system. And that's, you know, leveraging kind of best of breed algorithms from active learning,
[2023.12 → 2027.54] developed primarily by my co-founder, Amit Al Walker, around hyperparameter optimization and
[2027.54 → 2033.06] architecture search. And that to me is sure, if you could do that, you know, 50 times a year,
[2033.32 → 2037.76] I'd be printing money right now. But even if you can save somebody a couple of months, a few times a
[2037.76 → 2042.78] year, that ends up being really powerful in the way that they get their work done and how quickly they
[2042.78 → 2047.28] shift their applications. And again, they start thinking about the data problems and the modelling
[2047.28 → 2051.98] problems that they have, and not so much how do I, you know, write out this infrastructure and that
[2051.98 → 2058.20] sort of thing. So I know one of the things that, that determined AI is working on has been, you know,
[2058.22 → 2063.60] a lot about making AI work reproducible and being able to track experiments. And, you know, within
[2063.60 → 2069.62] the larger body of literature and AI, we're always hearing about explainability and transparency and
[2069.62 → 2075.52] such as that in AI. So I guess what I'm asking is, you know, why do you think that this is important
[2075.52 → 2081.90] to have this reproducibility built into AI infrastructure going forward? What kind of benefits do you see at
[2081.90 → 2087.88] offering? And what do you think might be missing in terms of the things that we are tracking or parts
[2087.88 → 2093.14] of the conversation that haven't really been addressed yet? Yeah, I mean, I think that if you
[2093.14 → 2098.68] told a software engineer that their code wasn't going to be tracked, and that, you know, even if
[2098.68 → 2103.60] their code was tracked, they were going to check it out from GitHub and try and build the system. And,
[2103.78 → 2107.98] you know, there was only like a 2% chance that they were going to get the same artifact out at the end of
[2107.98 → 2113.86] the day, as their peer who downloaded the same repo that afternoon, they would look at you like
[2113.86 → 2120.06] you were completely crazy, right? But that is very much the state of reality and the world with when
[2120.06 → 2124.64] it comes to machine learning practice. And it's because we have all this stuff under the hood that
[2124.64 → 2128.76] we need to track and get just right in order to get our algorithms to converge to the same level.
[2129.12 → 2133.12] It doesn't help that the optimization problems we're solving these days are non-convex. And so
[2133.12 → 2139.62] there's a bunch of stochastic embedded in them and so on. But the idea that I need to collect and
[2139.62 → 2144.46] understand every random seed that lives anywhere in my system, I need to understand what are the
[2144.46 → 2150.24] right hyperparameters for this particular run? What are the settings of the optimizer and so on
[2150.24 → 2155.74] in order to, and how is my model even initialized in the first place? Those are all necessary ingredients.
[2155.88 → 2162.10] I also have to keep track of what my data is. Now, once you have built a solution or a system for
[2162.10 → 2167.32] ensuring reproducibility across runs of different machine learning models, and this gets to your
[2167.32 → 2171.86] point of why it's important. Now you have the kernel of something that can be used to enable
[2171.86 → 2179.22] very direct and repeated collaboration among data scientists. You can say, hey, download my
[2179.22 → 2185.38] version of the model, and you can reproduce it exactly. Okay, great. Reproducible, done. That's
[2185.38 → 2190.82] cool. Reproducible, built. But now I can also use that to say, hey, why don't you extend my model?
[2190.82 → 2196.28] Try turning it on a different data set. Try running it on 64 GPUs and make sure that it
[2196.28 → 2202.38] converges in the same way. And I can begin to sort of riff with my colleagues on the next great idea.
[2202.50 → 2206.28] And I think that's sort of the dream. It's one thing for a single developer to be able to continue
[2206.28 → 2211.42] to innovate. But once somebody has a good idea, and now you can broadcast that idea to the entire
[2211.42 → 2216.90] rest of the organization, and everybody incorporates that into their solutions. Now you've got a flywheel
[2216.90 → 2222.26] going that can really help an organization accelerate. And again, we see these kinds of
[2222.26 → 2227.60] best practices and properties emerging at places that are really sophisticated in their AI infrastructure,
[2227.78 → 2233.46] the bigger companies, the Googles of the world, and so on. But that hasn't yet hit the mainstream yet
[2233.46 → 2238.28] because our tools don't have support for that. And so that's one of the main things that we try to
[2238.28 → 2239.44] drive at Determined AI.
[2239.44 → 2246.24] All right, Evan, I'd like to kind of switch gears a little bit here. So we've been talking a lot about
[2246.24 → 2252.42] practical things around infrastructure, which I think is great because this is practical AI after
[2252.42 → 2258.00] all, and those things are super important. But I was also curious to hear some of your thoughts on
[2258.00 → 2264.72] another subject. I saw that you wrote a recent blog post about AI leadership and positive impacts on
[2264.72 → 2270.18] things like the economy on human labour, and other things. I was wondering if you could share a little
[2270.18 → 2275.56] bit about the motivation behind that article and why you thought some optimism needed to be brought
[2275.56 → 2276.54] into that conversation.
[2277.46 → 2283.80] Yeah, I mean, it's funny, the company is headquartered in San Francisco. And as I get outside the San
[2283.80 → 2288.22] Francisco kind of AI bubble, or whatever you want to call it, you know, at dinner parties with friends,
[2288.58 → 2294.64] outside this world, a common theme that comes up is, isn't AI all about automating jobs
[2294.64 → 2300.28] away? Isn't it all about taking away kind of my livelihood? And, you know, it's scary as we move
[2300.28 → 2306.68] into for people who are even in skilled jobs, they're looking at, hey, is your algorithm that
[2306.68 → 2311.92] is perfect at tech summarization, going to replace the need for, you know, the training programs
[2311.92 → 2317.16] in my law firm of, you know, an army of freshly admitted attorneys doing discovery work and that
[2317.16 → 2323.06] sort of thing, right? And, you know, the answer is, is right, it's like, it's maybe, but when I think
[2323.06 → 2328.76] about technology, I like to look back on kind of what has technology done for the economy over time?
[2328.76 → 2335.90] And how has this story played out previously? So on the blog posts, I use an example of how Japan
[2335.90 → 2341.32] recognized that their population demographics were going to shift in the 80s, and started plowing a
[2341.32 → 2346.22] lot of money into robotics. And of course, now they're a world leader in robotics. But it was in
[2346.22 → 2351.30] service of kind of planning for a world where the majority of the population was going to be over 65,
[2351.30 → 2357.26] right? And building out infrastructure to support that. So I think that a similar kind of view needs
[2357.26 → 2362.26] to be taken of AI here, we look at the industrial revolution, we've been automating things for like
[2362.26 → 2366.14] a century and a half at this point, and probably longer than that, depending on how you want to
[2366.14 → 2372.12] think about it, it always does lead to sort of short term job displacement. But in the long run,
[2372.52 → 2379.72] quality of life and standard of living across the globe has risen dramatically. And so I think we kind
[2379.72 → 2385.30] of need to take that view on technology as a whole, in that we have to be careful about what it does in
[2385.30 → 2390.06] the short term to people, and making sure that we've got social policies in place to help folks out.
[2390.38 → 2396.56] But it's good to be optimistic, these technologies can be really, they can enable things that felt like
[2396.56 → 2401.34] science fiction 10 years ago to be real, like the self-driving cars we see off the streets and so on.
[2401.34 → 2407.44] But they can also really help, you know, in a bunch of ways that are otherwise unexpected,
[2407.44 → 2411.92] around helping environmental health, we've got a customer in kind of the waste management space,
[2412.00 → 2417.96] that specifically uses AI to help, you know, do recycling much more sort of effectively.
[2418.52 → 2423.76] We've also got, we're working with folks in pharmaceutical drug discovery that are using AI to
[2423.76 → 2430.42] cure new diseases. So there are ways that these technologies can be used broadly for the
[2430.42 → 2434.06] social good. And that was really the motivation behind this piece that I put together.
[2434.66 → 2439.00] Yeah, that it's really great to hear that. Actually, I know, just because it's a brief tangent,
[2439.32 → 2443.76] Daniel and I are both very focused on using AI for good. And we talk a lot about it during various
[2443.76 → 2449.20] episodes. And Daniel is focusing on bringing, making language availability with an AI, you know,
[2449.20 → 2452.76] more broadly available, because there are so many languages out there in the world that are
[2452.76 → 2459.38] not getting attention from technology. And I focus on animal welfare issues, and such. And so I love your
[2459.38 → 2466.66] optimism in this space. So I guess turning to the next thing is obviously with the potential for AI
[2466.66 → 2473.50] to continue to increase productivity at large, despite some of the bumps in the road, obviously,
[2473.50 → 2478.96] for society that you already addressed. And given the fact that there is a tremendous concern right now
[2478.96 → 2484.34] about privacy issues, how do you look at that dynamic tension between productivity and privacy?
[2484.34 → 2489.98] Are the two, are they always at odds with each other? Are they mutually exclusive in the context
[2489.98 → 2496.14] of AI? Or do you see a more optimistic path where you can be productive and yield privacy at the
[2496.14 → 2500.96] same time? It's a fascinating question on a broad area. And with my kind of recovering
[2500.96 → 2507.24] academic hat on, I think it's a fascinating question from fundamental research where we can set
[2507.24 → 2514.14] up this, what you're calling perhaps we can formally study whether there is fundamentally a privacy or
[2514.14 → 2519.30] product and productivity trade off. And first, we try and answer that question. And then if there is
[2519.30 → 2526.12] indeed this trade off, maybe there are ways that we can come up with that will give us precise control
[2526.12 → 2531.30] over that trade off as we make it. So an example I like to talk about is federated learning,
[2531.30 → 2538.32] where users could potentially remain completely in control over their data, and it stays, you know,
[2538.36 → 2545.00] on their edge devices. And yet the collective wisdom of all the users through AI and things like
[2545.00 → 2551.70] homomorphic encryption and, and, and so on, could be used to in a differentially kind of private way,
[2552.06 → 2558.34] help update models that globally make use of lots of users data without leaking individually
[2558.34 → 2563.32] private sensitive pieces of information. I don't think this stuff has been completely figured out,
[2563.40 → 2569.82] which is why I think it's still a fascinating research area. But I'm hopeful that as consumers demand
[2569.82 → 2576.12] that their data be kept private and so on, which I think we're seeing a lot of and look no further than
[2576.12 → 2583.28] GDPR and in the European Union, as evidence of this, that we will start to have to get clever with how we
[2583.28 → 2588.18] navigate that trade off space. And I'm really excited. You know, I watched the research
[2588.18 → 2592.16] coming out in the field pretty closely, because I think there's some really exciting stuff happening.
[2592.92 → 2598.34] Yeah, I know that in the most recent versions of TensorFlow and a bunch of other projects,
[2598.46 → 2602.34] there were very certain things around privacy. And of course, you have things like
[2602.34 → 2608.26] federated learning, like you're talking about, I was wondering, kind of as we get near to the
[2608.26 → 2615.52] end of our conversation here, in terms of practicalities for AI practitioners, whether that be
[2615.52 → 2621.80] someone that's, you know, working on some of their first AI projects, maybe as part of a startup or
[2621.80 → 2629.64] something or a larger company, what are some of the best things that, you know, we could implement to
[2629.64 → 2634.42] help our workflow? What's the biggest bang for the buck that we can do? Maybe that's looking into
[2634.42 → 2640.10] things like AutoML, or maybe that's implementing experiment tracking, where do you think people
[2640.10 → 2644.72] should start changing their workflows first to make the biggest impact?
[2645.14 → 2651.44] So I think if you're is you're kind of in the early days of your projects, and just kind of getting
[2651.44 → 2657.50] your feet well with the technologies, my advice would not be to go try an AutoML solution off the
[2657.50 → 2662.50] shelf. It might work for you, but you're going to be in a position very quickly where you don't
[2662.50 → 2669.30] understand what's going on one layer of the stack beneath you. And as data problems come up,
[2669.30 → 2673.96] or the next model needs a new tweak to it or something like that, you might be at a loss and
[2673.96 → 2682.12] might be at a place where you're stuck. Instead, what I tell people is invested heavily in your data
[2682.12 → 2688.92] production, tracking, versioning, to make sure that you're in a spot where you can go back and replay
[2688.92 → 2693.72] the past as it was exactly at that point in the past and build your models in that particular way.
[2693.72 → 2700.12] And begin to invest in tracking and understanding your workflows from a code and data and kind of
[2700.12 → 2705.42] models perspective. So that is some level of experiment tracking. The other thing I'd say is
[2705.42 → 2710.48] start simple. So start with the simplest model that could possibly work and solve your problem.
[2710.92 → 2716.16] And that will do two things. It will both one, maybe your problem is really simple. And you don't
[2716.16 → 2722.14] need, you know, a fancy 50 layer convolutional neural network with an LSDM bolted on the side to solve it,
[2722.14 → 2726.66] which is a good thing to learn. But at the very least, it gives you a baseline for okay,
[2726.80 → 2732.48] this is the know, baseline sort of no signal-to-noise ratio kind of place I need to be I need
[2732.48 → 2737.18] to make sure my models are at least as good as this. And it gets you in the habit of targeting
[2737.18 → 2742.60] a metric that you can use to evaluate whether your model is good enough. And I think that's
[2742.60 → 2744.46] a really important lesson for people getting started.
[2744.46 → 2750.60] Yeah, and I think those are amazing tips. In terms of like the experiment tracking one,
[2750.66 → 2755.40] I think you're right on the money. That's a huge benefit that people can have for people that are
[2755.40 → 2760.02] maybe not coming from a software engineering background. In your experience, maybe they're
[2760.02 → 2766.16] not quite to where they're ready to invest in the full determined AI solution. But what would be some
[2766.16 → 2771.30] like practical ways for them to track certain experiments, you know, initially just a matter of
[2771.30 → 2777.58] sort of metadata and naming things correctly or getting into good version control habits with
[2777.58 → 2783.72] with GitHub? Or where do you see people struggling the most? Or what are some simple ways that maybe
[2783.72 → 2785.46] they can benefit themselves?
[2785.98 → 2791.62] Yeah, so I, you know, I would say that for sure, get used to using software version control tools
[2791.62 → 2797.74] for your code and versions of the models that you got. For data, things like S3,
[2797.74 → 2802.00] for example, on Amazon, they offer a version data store, you can turn it on your bucket,
[2802.48 → 2807.72] and start using the version numbers as you're pulling data off of it. And then for the last
[2807.72 → 2815.32] piece, honestly, or a big piece is around metrics. And so that in the early days, can be recorded
[2815.32 → 2821.20] through either some pretty ad hoc processes. So structured log files, where you write down what
[2821.20 → 2827.64] you think are the key parameters of a particular experiment or run. So think of it as maybe a
[2827.64 → 2832.84] JSON blob that records, you know, the keys and values that you care about, and store that
[2832.84 → 2837.32] somewhere where you're sure you can get access to it. And so on. There are also projects,
[2837.40 → 2842.02] open source projects out there like ml flow tracking, which can help facilitate this
[2842.02 → 2846.14] and give you dashboards around this as well. And so that might be another place that I'd recommend
[2846.14 → 2850.92] people check out if they're interested in another open source option in this area.
[2850.92 → 2856.84] Awesome. Yeah, that's great. I should also mention, Joel Ruse was on the podcast, and
[2856.84 → 2862.52] we'll link his episode in the show notes as well. He talked a good deal about responsible AI
[2862.52 → 2867.92] development practices, bringing some of that expertise from software engineering into the
[2867.92 → 2872.74] the AI research and AI development workflow. So we'll definitely link that.
[2872.74 → 2879.80] And I guess to close out for listeners who might not necessarily have all the skills and
[2879.80 → 2883.92] infrastructure and back end engineering, and they're wanting to kind of level up and they maybe
[2883.92 → 2888.04] they're even a little bit intimidated by kind of diving into this new area. Do you have any other
[2888.04 → 2893.02] any other ideas that you to close out with on how they can level up those infrastructure skills?
[2893.66 → 2898.34] There are a number of greats, you know, online resources. It's funny, I've never really like
[2898.34 → 2903.64] thought about that side of things needed to be levelled up. In fact, that's kind of why we
[2903.64 → 2908.36] provide the software platform that we do to try and keep people from worrying about that.
[2908.50 → 2909.32] That's fair enough.
[2909.72 → 2915.40] But yeah, you know, I think that the various cloud providers do a good job of providing education
[2915.40 → 2920.56] around things like Kubernetes and so on that can be helpful as you're thinking about what's the
[2920.56 → 2925.14] modern way of building out this infrastructure. But I don't have specific resource recommendations in
[2925.14 → 2925.72] mind right now.
[2925.72 → 2931.50] No worries. Well, Evan, thank you so much for coming on to the show and telling us all about
[2931.50 → 2935.46] determined AI and infrastructure, and it was a fantastic conversation.
[2935.72 → 2938.60] Sure thing. Great, great speaking with you guys. Thanks so much for having me.
[2940.86 → 2945.04] All right, thank you for tuning into this episode of Practical AI. If you enjoyed the show,
[2945.10 → 2950.02] do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are on
[2950.02 → 2953.80] Twitter or social network, share a link with a friend, whatever you got to do, share the show with a
[2953.80 → 2958.28] friend if you enjoyed it. And bandwidth for Changelog is provided by Vastly. Learn more at
[2958.28 → 2963.20] fastly.com. And we catch our errors before our users do here at Changelog because of Rollbar. Check them
[2963.20 → 2969.10] out at rollbar.com slash Changelog. And we're hosted on Linde cloud servers. Head to linode.com
[2969.10 → 2974.58] slash Changelog. Check them out. Support this show. This episode is hosted by Daniel Whiten ack and Chris
[2974.58 → 2980.16] Benson. The music is by Break master Cylinder. And you can find more shows just like this at
[2980.16 → 2985.52] ChangeLog.com. When you go there, pop in your email address, get our weekly email, keeping you up to date
[2985.52 → 2990.94] with the news and podcasts for developers in your inbox every single week. Thanks for tuning in.
[2990.94 → 2991.84] We'll see you next week.
