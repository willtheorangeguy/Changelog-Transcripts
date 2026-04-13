[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.04 --> 36.08]  Learn more at fly.io.
[43.04 --> 46.78]  Welcome to another episode of Practical AI.
[47.16 --> 48.66]  This is Daniel Whitenack.
[48.76 --> 51.44]  I'm a data scientist with SIL International.
[51.44 --> 57.16]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[57.16 --> 57.46]  Martin.
[57.72 --> 58.42]  How are you doing, Chris?
[58.96 --> 59.94]  I'm doing very well.
[60.00 --> 60.74]  How are you today, Daniel?
[61.28 --> 63.00]  I'm actually doing amazing.
[63.40 --> 65.16]  So I'm not in my normal location.
[65.16 --> 66.86]  I'm down in Orlando, Florida.
[67.06 --> 71.82]  So one thing is it's sunny outside and I can like be outside without suffering.
[71.82 --> 78.78]  But also, well, I'm in like in-person meetings here with some of our collaborators and partners
[78.78 --> 82.08]  and they wanted me to do a demo today.
[82.36 --> 86.34]  So I got up early this morning at like 6 a.m.
[86.48 --> 93.12]  before hotel breakfast and I threw together a quick demo and I used modal for that.
[93.66 --> 99.98]  And there's literally someone that stood up out of their like seat and clapped after
[99.98 --> 100.44]  the demo.
[100.44 --> 105.24]  So our guest today is Eric Bernardson with modal.
[105.56 --> 109.10]  And so basically, Eric is making me look good in all respects.
[109.64 --> 114.00]  And and I'm pretty excited to talk more about modal and share it with everyone today.
[114.12 --> 114.64]  Welcome, Eric.
[114.90 --> 115.24]  Hi.
[115.40 --> 115.56]  Hi.
[115.62 --> 116.44]  Thanks for having me.
[116.58 --> 119.04]  I'm excited to talk about modal or anything else.
[119.54 --> 119.76]  Yeah.
[119.90 --> 120.10]  Yeah.
[120.16 --> 122.82]  I think, Chris, do you remember like quite a while ago?
[123.00 --> 124.18]  I don't remember when this was.
[124.26 --> 125.24]  Maybe, Eric, you remember?
[125.24 --> 130.62]  I think you wrote a blog post about building data teams or something like that.
[131.04 --> 132.90]  I forget exactly what it was.
[133.04 --> 135.86]  But I remember Chris and I talking about it on the podcast.
[136.08 --> 139.54]  I'll have to see if I can find it back in your blog.
[139.84 --> 141.48]  But yeah, that was in the summer of 2021.
[142.04 --> 142.44]  Yeah.
[142.44 --> 143.04]  Yeah.
[143.04 --> 143.16]  Yeah.
[143.44 --> 143.64]  Yeah.
[143.72 --> 147.56]  So we should have had you on the show then, but I'm glad that we get to have you on the
[147.56 --> 148.00]  show now.
[148.24 --> 154.50]  So so you describe modal as an end to end stack for cloud compute.
[154.50 --> 164.38]  So I guess one big question maybe to start things out is cloud compute isn't new, but it definitely
[164.38 --> 168.34]  can be complicated depending on what you're trying to do.
[168.44 --> 173.88]  Like what got you starting to think about like the set of problems that you're addressing
[173.88 --> 174.76]  with modal?
[175.02 --> 177.80]  Like what what got you going down this path?
[178.44 --> 178.84]  Yeah.
[178.84 --> 184.84]  It's kind of a longer story maybe, but I've been working with data for 15 years or maybe
[184.84 --> 185.20]  more.
[185.50 --> 186.30]  Most of my career.
[187.20 --> 188.68]  Initially, I was at Spotify for seven years.
[188.86 --> 192.68]  I built the music recommendation system there and open source of vector database called
[192.68 --> 194.38]  annoying and workflow schedule.
[194.58 --> 199.78]  But they'd like kind of everything from like deep learning to like business intelligence
[199.78 --> 203.62]  to large scale, big data type like Hadoop stuff.
[203.62 --> 206.88]  And then I was just doing a company called better for six years.
[206.88 --> 209.08]  I managed data teams, but also managed other teams.
[209.26 --> 213.54]  And so as I was thinking about starting a company, I kept coming back to data.
[214.10 --> 217.98]  And my starting point was really just like it's hard to work with data.
[218.10 --> 220.96]  And I feel like data teams don't have the tools they need.
[221.48 --> 225.46]  And initially I was super agnostic as to like what to build.
[225.62 --> 230.44]  I kind of frankly wanted to rebuild everything, which is not particularly realistic.
[230.72 --> 231.78]  Maybe in a lifetime.
[232.08 --> 233.56]  Aspirational, megalomaniac maybe.
[233.56 --> 239.18]  But what I realized was that at least like, you know, if you want to rethink a lot of
[239.18 --> 241.98]  the data stack, a good place to start is at the bottom.
[242.42 --> 247.12]  So I almost like sometimes joke that I'm like kind of like grudgingly had to start,
[247.22 --> 249.94]  you know, it's like a spite startup.
[250.18 --> 254.48]  Like, you know, and doing this like work at now at like the most lowest level, which is
[254.48 --> 259.02]  to, you know, solve the compute problem of like I have code and I want to deploy it in
[259.02 --> 261.40]  the cloud and like why is that so hard?
[261.44 --> 261.98]  I don't know.
[262.46 --> 266.06]  But, you know, it's a big problem for many data teams is, you know, just a problem of
[266.06 --> 271.46]  like, you know, taking code and scaling it out or scheduling it or running it on GPUs
[271.46 --> 274.48]  or, you know, setting up web endpoints or whatever it is.
[274.72 --> 280.56]  And really focusing on that problem as like, you know, building this core foundational layer.
[280.56 --> 284.16]  That's very abstract and, you know, very general purpose.
[284.70 --> 287.12]  So that's also why our website, I think it's a little confusing the first time.
[287.24 --> 292.38]  But in particular, what I would say we've been focusing on the last six months is online
[292.38 --> 293.90]  inference.
[294.12 --> 299.04]  So it's a lot of machine learning, AI models focusing on that use case as a sort of initial
[299.04 --> 299.72]  starting point.
[299.92 --> 304.08]  But Modelo always, to me, had this promise of, you know, running almost anything.
[304.18 --> 305.66]  It's almost like a Kubernetes in the cloud.
[305.66 --> 306.22]  Yeah.
[306.42 --> 313.32]  And one of the interesting things to me, I think, where like maybe it took me a second
[313.32 --> 315.18]  for this to like sink in.
[315.32 --> 322.04]  But once it did, it like was a really encouraging thing for me was like I have my code locally
[322.04 --> 324.76]  and I know how to run it locally.
[325.06 --> 332.92]  But then like you have this sort of concept of like these decorators within Python code that
[332.92 --> 338.56]  kind of take your code and like you run it like Python, you know, main.py, whatever.
[339.36 --> 345.10]  But actually something like the moment I realized, OK, well, now this function is actually not
[345.10 --> 346.02]  running locally.
[346.02 --> 351.64]  Like I just did some sort of like batch inference or something with this script and didn't like,
[352.12 --> 357.08]  you know, my fans aren't going on my laptop because this is actually running somewhere else.
[357.08 --> 365.16]  Could you describe like I mean, there's a lot of ways that you could have gone about this sort
[365.16 --> 369.30]  of lower level of the problems that data teams face.
[370.20 --> 376.10]  There's a really fundamental piece of this, which is like the local to cloud or local to deployment
[376.10 --> 377.46]  like cycle.
[377.72 --> 381.16]  And with Modelo, that seems very, very quick.
[381.36 --> 385.88]  Like how did you zero in on that kind of workflow?
[385.88 --> 390.40]  We built something that architecture looks something like AWS Lambda, right?
[390.46 --> 392.10]  Like, you know, it's like function as a service.
[392.24 --> 395.54]  We take code and execute it in a serverless way in the cloud.
[396.10 --> 399.54]  The starting point, like the reason why I ended up going down this rabbit hole and doing
[399.54 --> 403.62]  that, you know, really is the whole like, you know, serverless, you know, runtime is really
[403.62 --> 406.78]  kind of thinking about like developer productivity and developer happiness.
[407.62 --> 412.82]  And my sort of philosophical observation as CTO for many years is that developers, developer
[412.82 --> 416.72]  productivity, I think, you know, is very often like well understood in terms of feedback
[416.72 --> 417.12]  loops.
[417.88 --> 421.76]  And so in particular, there's a sort of, you know, as you write code, there's like almost
[421.76 --> 422.92]  like a nested set of for loops.
[423.02 --> 426.70]  It is the innermost loop of like you write some code, then it's a syntax error, then you fix
[426.70 --> 427.62]  it and then you run it.
[427.90 --> 428.84]  Maybe you have some unit tests.
[429.32 --> 431.16]  But then like there's like these like outer loops.
[432.06 --> 435.76]  They're often like, okay, let's like deploy this to the cloud or like, you know, let's like
[435.76 --> 437.06]  run this on a massive data sets.
[437.06 --> 439.68]  And that's when the iteration speed gets like very, very slow.
[440.32 --> 444.58]  And so you look at data teams, like they're often like particularly exposed to these feedback
[444.58 --> 447.76]  loops because they have to run a large data sets or they always have to run things in
[447.76 --> 448.08]  production.
[448.08 --> 451.52]  Like you can't really run like things on like synthetic data as a data team.
[451.60 --> 455.14]  Like you have to kind of deploy it into production or like run it on a real data set.
[455.22 --> 458.00]  And so it really frustrated a lot of data teams.
[458.08 --> 460.38]  It's like that sort of like very slow iteration speed.
[460.42 --> 461.82]  It's like I write some code.
[462.08 --> 465.98]  Now I have to like, you know, create a container, push it to the cloud, then go and click on an
[465.98 --> 469.24]  interface or like, you know, merge, you know, some pull requests or whatever.
[469.58 --> 471.16]  Then like, you know, my container fails.
[471.28 --> 472.72]  Now I have to go and look at logs or whatever.
[473.18 --> 476.70]  So I started to think about like, what if we bring the infrastructure into that like innermost
[476.70 --> 481.02]  loop, like the loop of like, okay, you just write code and then you like immediately run
[481.02 --> 482.32]  it, but it actually runs in the cloud.
[483.80 --> 487.62]  And, you know, in order to do that, we realized we can't do this with Kubernetes.
[487.62 --> 489.12]  We can't do this using Lambda.
[489.12 --> 494.80]  Like we basically have to build our own infrastructure that takes code and can launch containers, maybe
[494.80 --> 497.58]  hundreds of containers in the cloud in a few seconds.
[498.30 --> 502.66]  Uh, so we went very deep, you know, down that rabbit hole and built basically our own container
[502.66 --> 505.54]  runtime, our own file system, our own container builder.
[506.46 --> 512.10]  Uh, luckily I'm not, you know, afraid to go deep and like solve like kind of tricky, you
[512.10 --> 514.92]  know, container problems and dealing with Linux and file systems.
[515.14 --> 520.02]  Um, but that's like a lot of what we had to build in the last two years is that, is that
[520.02 --> 521.68]  foundational level, like that runtime.
[521.68 --> 525.40]  But, but the benefit is like now we have this, you know, super nice developer experience.
[525.46 --> 526.74]  We can just take code locally.
[526.74 --> 530.86]  You can spawn a hundred containers in the cloud in a few seconds, like running the latest code
[530.86 --> 531.70]  in the latest container.
[532.26 --> 533.18]  It sounds fascinating.
[533.32 --> 537.62]  I'm really interested in it, but I want to ask you to step back for a second with a follow
[537.62 --> 540.16]  up and bridge a gap of understanding for me.
[540.58 --> 544.00]  You were saying like, can't do it with Kubernetes, can't do it with AWS Lambda.
[544.00 --> 546.64]  Uh, and I believe you, but I don't know why.
[546.70 --> 549.52]  And I'm imagining that maybe a few of our listeners don't know why either.
[549.64 --> 554.68]  Could you kind of tell us what it is like, cause a lot of them, their companies are in
[554.68 --> 559.50]  one of those big three providers and to kind of show them, uh, you kind of demonstrated
[559.50 --> 563.34]  with the user experience quite well a moment ago, but could you talk a little bit about
[563.34 --> 569.50]  like what was falling down in those kind of more mainstream big three kind of approach,
[569.50 --> 574.54]  Google, AWS and, uh, Azure, uh, so that we can understand that.
[574.62 --> 575.42]  Cause you made a statement.
[575.68 --> 578.02]  I'm with you on that, but just bridging it.
[578.32 --> 578.44]  Yeah.
[578.56 --> 581.76]  And first of all, like I'm, I'm like the world's biggest AWS fan, right?
[581.78 --> 585.46]  Like, you know, we run everything on AWS and like, I love it for the capabilities it
[585.46 --> 588.22]  brings me as a developer to run things at scale.
[588.60 --> 588.68]  Yeah.
[588.86 --> 592.06]  Uh, developer experience in AWS has never been particularly good.
[592.16 --> 596.34]  And so, you know, like I've been banging my head, you know, for years against like, you
[596.34 --> 597.84]  know, AWS documentation.
[597.84 --> 600.42]  And in the end, I usually figured it out, but it was a pretty hard experience.
[600.70 --> 606.18]  I think in particular, the problem with both Kubernetes and AWS, you know, or like Lambda
[606.18 --> 610.76]  or EC2, et cetera, that, that we saw like, you know, either, you know, for users to use
[610.76 --> 614.78]  it directly or, or for us to build on top of that is, it's just the iteration speed.
[614.78 --> 618.46]  Like, so if, you know, for instance, in Kubernetes, let's say you want to run something in Kubernetes
[618.46 --> 620.66]  and in production going from code locally.
[620.96 --> 622.82]  Well, now you have to first build a container.
[623.00 --> 625.96]  Then you have to do some sort of Docker push as a registry, right?
[625.96 --> 627.96]  Like then you have to kick off a Kubernetes job.
[628.36 --> 631.84]  Then, you know, you have to go and look at the logs of that Kubernetes job.
[631.88 --> 635.12]  And by the way, kicking off a Kubernetes job, like that often like entails like, you know,
[635.16 --> 639.62]  the Kubelet worker, like pulling down the Docker image.
[639.62 --> 643.38]  And so we were like looking under the hood and trying to understand how like Docker works
[643.38 --> 647.40]  and Docker, you know, it's an amazing piece of technology, like, you know, for the sort
[647.40 --> 650.72]  of, you know, the new way of thinking that it brings to the table around like, you know,
[651.34 --> 656.50]  insulated containers, but it's quite inefficient in starting containers.
[656.50 --> 662.16]  Like, you know, most containers end up having lots of data that's never actually read.
[662.16 --> 667.28]  Like there's like, you know, thousands of like time zone files of like, you know, locale
[667.28 --> 670.10]  information about, you know, time zones in Uzbekistan or whatever.
[670.24 --> 671.76]  Like you're never going to read those, right?
[671.84 --> 673.02]  Unless you're in Uzbekistan.
[673.28 --> 674.76]  Sorry, just getting that in there.
[675.10 --> 675.28]  Yeah.
[675.38 --> 679.66]  And this, you know, whatever, you know, or uninhabited islands.
[679.84 --> 683.32]  Like there's like time zone information about uninhabited islands in like, you know,
[683.34 --> 684.46]  the standard Linux distribution.
[684.64 --> 685.42]  Like, okay, like great.
[685.50 --> 687.48]  But like get them out of my Docker container.
[688.02 --> 690.30]  But the other thing is also Docker is quite inefficient.
[690.30 --> 693.22]  And like, it has this like layer thing, but like other than that, you know, it doesn't
[693.22 --> 694.50]  really deduplicate information.
[695.08 --> 699.48]  And so what we realized is that what if we like rethink how, you know, those containers
[699.48 --> 701.90]  get pushed and pulled and we end up building our own file system.
[702.02 --> 705.46]  We deduplicate the content by computing a checksum of every file.
[706.30 --> 708.22]  That's actually sort of similar to how Lambda works.
[708.74 --> 712.34]  But Lambda is also not fast enough in the sense that like if you publish a new Lambda,
[712.44 --> 715.08]  it still takes about a minute for you to be able to run it.
[715.38 --> 716.56]  Lambda also has other limitations.
[716.76 --> 717.54]  It doesn't support GPU.
[717.70 --> 719.10]  It doesn't support long running jobs, et cetera.
[720.30 --> 724.12]  So those are all the reasons like why we ended up deciding we can't build this on top of
[724.12 --> 726.20]  Kubernetes or Lambda or any existing solution.
[727.04 --> 728.06]  Also not Docker.
[728.68 --> 732.84]  We ended up using lower level primitives instead and building a lot of it ourselves.
[733.02 --> 739.84]  And are there specific things about, and I sort of like in my own experience in using
[739.84 --> 744.18]  modal have experienced this, but from your perspective, I would be interested to hear like
[744.18 --> 750.10]  you talked about kind of moving towards this use case, like the use cases around machine
[750.10 --> 755.86]  learning, around AI as being kind of like very well suited to this workflow of those types
[755.86 --> 763.72]  of workflows have any sort of like added benefits and or challenges that may be like, you know,
[763.72 --> 769.40]  running a web scraper or something like that, like some other sort of like use case, which is
[769.40 --> 775.38]  related to data, but maybe not involving sort of like serialized model files and inference
[775.38 --> 776.26]  and GPUs.
[776.26 --> 781.96]  Like what are those those things about these machine learning or AI workflows where you think
[781.96 --> 788.06]  like either there's specific challenges that people have that are solved by this kind of
[788.06 --> 793.18]  quick cycle workflow versus just kind of like other data related workflows?
[793.18 --> 797.74]  Yeah, I think we focused a lot on online inference recently.
[797.74 --> 801.68]  So basically, you know, let's say you have a model could either be some off the shelf model
[801.68 --> 805.92]  from hugging face or some fine tuned model that you have yourself and you want to deploy
[805.92 --> 806.30]  that.
[806.68 --> 811.12]  And in particular, if that model uses GPU, the set of vendors that support that is somewhat
[811.12 --> 811.48]  limited.
[811.48 --> 816.82]  And, and the other reason why it's is also cost, you know, traditionally, if you go through
[816.82 --> 821.20]  the Kubernetes or EC2 route, if you want to deploy a model inference endpoint, you have
[821.20 --> 826.06]  to spin up an instance that sits idle for most of the time, you can set up autoscaling, but
[826.06 --> 827.14]  autoscaling is pretty slow.
[827.64 --> 830.68]  So moving to serverless makes a lot of sense from a cost perspective.
[831.58 --> 835.06]  And so I think that's the other reason why we've seen a lot of, you know, it's not just
[835.06 --> 835.26]  us.
[835.38 --> 838.52]  It's been, I saw the banana was in the previous episode, for instance, like there's a couple
[838.52 --> 840.10]  of other vendors that also focused on this.
[840.46 --> 844.64]  I think cost is driving a lot of that, the demand for serverless vendors for GPU compute
[844.64 --> 845.14]  specifically.
[845.92 --> 849.82]  I also think it's something that just came up in the last few months where like a lot of people
[849.82 --> 853.56]  ended up realizing like, you know, we're very good at trading models, like building, you
[853.56 --> 854.22]  know, custom stuff.
[854.40 --> 857.28]  We don't want to deal with infrastructure and running this in production.
[858.02 --> 862.60]  And so there's been a lot of demand for vendors like modal where they can just take a model
[862.60 --> 866.92]  and publish it to modal and run it in production and not have to think about, you know, auto
[866.92 --> 872.14]  scaling policies and have to think about setting up, you know, web endpoints and dealing with
[872.14 --> 875.64]  security groups and, and all that stuff.
[875.64 --> 880.28]  That being said, I mean, modal kind of going back to its roots, like we, we did, you know,
[880.32 --> 881.56]  it's not just online inference.
[881.56 --> 885.90]  Like we, we started out focusing a lot on what I think it was like embarrassingly parallel
[885.90 --> 886.36]  problem.
[886.36 --> 890.16]  Like this idea that like you have something you want to fan out and do a lot of stuff
[890.16 --> 890.62]  in parallel.
[890.96 --> 895.92]  So besides online inference, modal also does a fair amount of batch inference or sort of
[895.92 --> 897.82]  parallelizable things.
[897.82 --> 900.46]  Like, like a lot of people actually use this for web scraping.
[900.46 --> 905.98]  Other people also use this for things like computational biotech, large scale test coding.
[906.86 --> 910.26]  You know, you can also use this for various types of simulations or back testing, that
[910.26 --> 910.54]  kind of stuff.
[910.58 --> 913.02]  So there's a pretty wide range of things that, that modal as well.
[913.22 --> 918.04]  But I think right now, like the user experience of online inference is like nine out of 10,
[918.14 --> 918.80]  I would say at modal.
[919.02 --> 923.04]  The user experience for like batch inference and large scale, like parallelism is like eight
[923.04 --> 923.48]  out of 10.
[924.30 --> 927.98]  We're working on a lot of the other stuff, like data pipelines, like building more complex
[927.98 --> 932.08]  support for scheduling and that kind of stuff where right now, like it's good, but it's,
[932.20 --> 933.98]  you know, not quite yet where we want.
[934.10 --> 935.68]  We think, you know, the long-term potential is.
[936.76 --> 941.56]  So Eric, I mentioned and full disclosure to everyone in the world.
[941.56 --> 947.68]  I'm a huge fan of modal and have been using it a lot and building things in it, including
[947.68 --> 950.00]  the side project I'm working on prediction card.
[950.00 --> 954.14]  And, um, I think I just counted, I'm in the interface now.
[954.28 --> 959.20]  I have 129 modal apps deployed right now.
[959.40 --> 959.60]  Wow.
[959.74 --> 966.94]  So I want to try to like describe from my end, like it's hard because like this is an audio
[966.94 --> 972.06]  podcast and like talking about how things work without like showing something visual
[972.06 --> 976.14]  is a little bit tough, but I want to do my best at trying to describe like how I would
[976.14 --> 981.50]  describe it and then I'd love like you to fill in the gaps or correct me if I'm wrong
[981.50 --> 982.12]  at any point.
[982.28 --> 988.10]  So if you think about running something in modal, you can write a Python script, like let's
[988.10 --> 989.76]  say app.py or whatever.
[990.36 --> 992.04]  You can have functions in that script.
[992.22 --> 998.70]  And then actually one of the things I love is like dependencies is a really annoying part
[998.70 --> 1001.34]  of particularly AI and ML workflows.
[1001.34 --> 1010.20]  So you can decorate certain functions in your code with like stub dot function and then define
[1010.20 --> 1016.40]  a modal stub in your code, which is essentially like referencing a container with certain dependencies
[1016.40 --> 1017.00]  in it.
[1017.12 --> 1022.56]  And then when you execute your code, you say Python app dot py.
[1022.80 --> 1027.68]  And when it gets to executing that function in your code, which is decorated with the stub,
[1027.68 --> 1030.12]  it actually doesn't run it locally.
[1030.12 --> 1035.32]  It spins up a container in modal and runs that in the cloud.
[1035.52 --> 1041.98]  So you can do this either by just calling that function or you can actually deploy then
[1041.98 --> 1047.18]  your app and have that function be accessible as like a serverless function or a web endpoint
[1047.18 --> 1051.50]  for your other applications or your other APIs to access.
[1052.02 --> 1055.18]  So I don't know if I did a great job at describing that, Eric.
[1055.20 --> 1056.70]  That was my initial attempt.
[1057.04 --> 1059.40]  Feel free to make that more coherent.
[1059.40 --> 1061.62]  No, I think that's exactly right.
[1061.76 --> 1067.32]  Like I are, I think you touched on a couple of points of modal, you know, where we maybe
[1067.32 --> 1072.72]  think different about infrastructure and other, in particular, this guy Swix wrote a great
[1072.72 --> 1073.48]  blog post about it.
[1073.52 --> 1074.90]  It's called the self-provisioning runtime.
[1075.14 --> 1079.66]  And I think that's like, to me, it's been kind of putting words to an idea that I always
[1079.66 --> 1083.76]  had around, like, it's sort of similar, like if you ever use like a service like Pulumi,
[1083.88 --> 1086.84]  for instance, like, you know, or like Terraform or something like that, the sort of idea that
[1086.84 --> 1088.16]  like infrastructure is code.
[1088.42 --> 1090.60]  But like modal has always gone further than that.
[1090.60 --> 1095.88]  It's also like infrastructure and the app code, like put it together in the same code and have
[1095.88 --> 1099.14]  like the app itself define the infrastructure it needs to run.
[1099.14 --> 1105.16]  And so with modal in code, you define, you know, the containers you need, including Python
[1105.16 --> 1107.36]  dependencies or any other like binary dependencies you need.
[1107.48 --> 1111.30]  You can have different functions using different containers calling each other, just like Python
[1111.30 --> 1112.10]  functions, right?
[1112.56 --> 1113.86]  And it just like provisions itself.
[1113.86 --> 1116.32]  Like you can say, you know, this function should run on a GPU.
[1116.56 --> 1118.64]  This function should have 16 CPUs available.
[1118.86 --> 1121.66]  This other function needs 128 gigabytes of RAM.
[1121.82 --> 1124.34]  Like in code is zero config in modal.
[1124.46 --> 1125.54]  There's like not a YAML file.
[1125.64 --> 1127.16]  Like there's nothing you can configure in modal.
[1127.16 --> 1128.24]  Like everything is in code.
[1128.86 --> 1132.76]  And to me, it's all, you know, goes back to this idea of like the, how do you make developers
[1132.76 --> 1137.16]  productive in having the fast feedback loop is, is I think traditionally we've had to give
[1137.16 --> 1143.14]  that up and basically make engineers run things locally in order to get the fast feedback loops
[1143.14 --> 1143.58]  they need.
[1143.88 --> 1149.02]  But then the problem is like later they need, then still need to deploy it to the cloud.
[1149.14 --> 1153.72]  And then you have a whole set of issues that then break because the cloud is running
[1153.72 --> 1154.60]  in a different environment.
[1154.60 --> 1158.66]  And so this goes back to what I said, like maybe 20 minutes ago, like what if you can
[1158.66 --> 1162.96]  take the infrastructure and bring it into the innermost loop of how you iterate, then
[1162.96 --> 1166.52]  you solve this problem of having different environments because it's always running in
[1166.52 --> 1166.90]  the cloud.
[1167.12 --> 1171.62]  And it's fast enough that like, it feels, you know, some people even say modal is faster
[1171.62 --> 1174.54]  than running things locally, even though it's running in the cloud.
[1174.62 --> 1178.36]  You never, ever have to think about these environment conflicts because it's always running in the
[1178.36 --> 1180.12]  exact same container at any time.
[1180.12 --> 1183.60]  And it's fast enough that you don't have to like this like frustrating thing where you
[1183.60 --> 1185.14]  have to build containers and push them around.
[1185.14 --> 1187.28]  And like you sort of get the best of two worlds.
[1187.38 --> 1191.68]  You get the developer productivity of running things locally, but you have, you know, the
[1191.68 --> 1196.54]  full power of the cloud, you know, and all the power of, you know, containers and GPUs
[1196.54 --> 1197.04]  and like whatever.
[1197.18 --> 1197.42]  Right.
[1198.02 --> 1198.90]  I don't know if that makes any sense.
[1199.30 --> 1199.50]  Yeah.
[1199.50 --> 1204.20]  It's so Chris and I have talked about this at like certain points in the podcast.
[1204.20 --> 1211.20]  I have always like really had this disdain for like maintaining a whole bunch of like
[1211.20 --> 1212.92]  local environments as well.
[1212.92 --> 1214.64]  Like I'm not a condo user.
[1214.64 --> 1219.10]  Like I, I have like very minimal setup locally on my machine.
[1219.10 --> 1225.46]  And I, one of the things I think I kind of grasped onto is like, oh, well I can develop
[1225.46 --> 1232.14]  now locally with modal and just like import OS and import JSON and like kind of normal-ish
[1232.14 --> 1233.60]  things and import modal.
[1233.60 --> 1241.78]  But when I need to access transformers or PyTorch or like some random other package that like
[1241.78 --> 1248.20]  normalizes index scripts or something, like I actually have like zero concern about like
[1248.20 --> 1253.94]  setting that up locally to test because I can just add that as a dependency in the modal
[1253.94 --> 1257.34]  function and that runs in the cloud in its own container.
[1257.56 --> 1260.00]  So I actually never even have to install that locally.
[1260.46 --> 1265.66]  Now I could do that maybe before like using like a local build of a Docker image or something.
[1265.66 --> 1270.48]  But that again, like you were talking about, Eric has another cycle associated with it,
[1270.52 --> 1271.88]  which is also annoying.
[1272.08 --> 1272.18]  Yeah.
[1272.26 --> 1272.46]  Yeah.
[1272.58 --> 1273.22]  It's kind of annoying.
[1273.54 --> 1277.90]  So yeah, I love that this, like I can just think through like my imports are minimal.
[1278.02 --> 1280.12]  Like I can even run like a pie test.
[1280.30 --> 1280.52]  Right.
[1280.52 --> 1284.48]  And it's just testing as it's going to run in production.
[1284.48 --> 1284.92]  Right.
[1284.96 --> 1287.86]  Because it's running in a container in the cloud already.
[1288.28 --> 1290.20]  It's running that function.
[1290.74 --> 1290.90]  Yeah.
[1291.00 --> 1294.08]  So I, that's kind of like a lot of my love.
[1294.18 --> 1296.72]  I feel like that I've, I've enjoyed about it.
[1296.72 --> 1304.30]  What are the surprising ways that you've seen people use modal that maybe like have been
[1304.30 --> 1311.28]  unlocked for users that were really either difficult for them before or like, oh, I didn't
[1311.28 --> 1313.88]  expect people to do this with modal.
[1314.10 --> 1317.00]  Have you encountered any of those things that stand out?
[1317.00 --> 1322.40]  I mean, modal inference in itself, like kind of, you know, was a little bit of a serendipitous
[1322.40 --> 1323.08]  thing for us.
[1323.16 --> 1325.26]  Like, you know, we didn't expect that people would do that in general.
[1325.36 --> 1330.02]  Like we thought of modal primarily initially as like more of like a batch workhorse, like,
[1330.06 --> 1331.64]  you know, something that helps you scale out.
[1331.76 --> 1336.54]  But, but we've seen a lot of traction on online inference and model deployments.
[1336.70 --> 1341.42]  And so for that reason, we're focusing a lot on improving startup performance right
[1341.42 --> 1344.56]  now, because when you're doing online inference, you have to spin up containers very quickly.
[1344.56 --> 1346.48]  You also have to load models very quickly.
[1346.68 --> 1350.62]  And especially when you're dealing with GPUs, there's a lot of, you know, overhead of copied
[1350.62 --> 1351.76]  models to GPUs, et cetera.
[1351.86 --> 1352.92]  So it's getting that down.
[1353.18 --> 1356.34]  It's been a big focus of ours for the last few months.
[1356.72 --> 1361.04]  I guess another thing I've been like sort of surprised by is we enable the functionality
[1361.04 --> 1363.12]  to set up web hooks pretty easily.
[1363.20 --> 1368.48]  So in modal, you can define, oh, like make this function exposed to the web and give it
[1368.48 --> 1369.18]  its own URL.
[1369.18 --> 1373.16]  And now you can call this a URL and it triggers something in modal.
[1373.16 --> 1375.12]  It triggers some Python code.
[1375.54 --> 1380.02]  People started leveraging that for like building like full blown web apps on mobile, which I
[1380.02 --> 1384.22]  was kind of surprised by like graphical UIs and all kinds of stuff and like hosting whole
[1384.22 --> 1384.74]  UIs.
[1385.26 --> 1388.16]  Because I never anticipated like that being like a use case.
[1388.24 --> 1390.90]  I always thought of like, oh, well, people are going to use like, you know, whatever,
[1391.20 --> 1394.78]  like Vercel or Heroku maybe for something like that.
[1394.86 --> 1397.54]  But that's been sort of interesting to see that a lot of people are using that.
[1397.54 --> 1399.16]  And so it's pretty promising.
[1399.30 --> 1400.70]  Like maybe there's something more to be done there.
[1400.82 --> 1405.22]  Like I tend to think like our bread and butter is like machine learning and AI and like, you
[1405.22 --> 1406.28]  know, data pipelines.
[1406.44 --> 1410.46]  So I don't want to get like all in on like sort of building more like a web hosting platform.
[1410.46 --> 1411.74]  But I think there's something interesting.
[1411.88 --> 1413.34]  It's sort of similar along the same lines.
[1414.04 --> 1418.46]  A lot of people have been using us more for sort of job queues type things.
[1418.46 --> 1421.36]  It's like, you know, more like almost like as a replacement to salary.
[1422.14 --> 1425.86]  The idea that like they can create a modal function and then they can like enqueue work
[1425.86 --> 1430.38]  for it and they never have to think about scaling or sort of deployment and productionization
[1430.38 --> 1431.96]  of salary like job queues.
[1432.44 --> 1434.40]  And that was also something we didn't really think about.
[1434.50 --> 1436.26]  But a bunch of people have been telling us to actually do.
[1436.38 --> 1436.94]  So that's kind of cool.
[1437.54 --> 1439.04]  So I got a follow up question here.
[1439.36 --> 1442.36]  And you've both sort of covered it to some degree already.
[1442.76 --> 1446.90]  But as the person who has not yet had a chance to use it, I'm really curious.
[1446.90 --> 1452.08]  And I'm imagining there are a few people listening as well that are wondering, could you take
[1452.08 --> 1455.82]  us, Eric, like through kind of a classic workflow with modal?
[1456.26 --> 1460.28]  We've done that with other technologies that you may have heard on other episodes and stuff.
[1460.68 --> 1462.60]  But I'm trying to get in my mind.
[1462.68 --> 1466.48]  Daniel is doing it all the time, but I've been left behind a little bit on this.
[1466.84 --> 1471.22]  Kind of just take us through a typical AI ML workflow on modal just verbally, like what
[1471.22 --> 1473.92]  the steps are just to kind of show us that simplicity.
[1473.92 --> 1478.06]  People probably going to be thinking about whatever they're on previously, if they're
[1478.06 --> 1479.24]  on some other platform.
[1479.68 --> 1483.80]  Just as a point of comparison about how you're doing that, I'm just kind of curious if you
[1483.80 --> 1485.36]  can, any example is fine.
[1485.84 --> 1486.06]  Yeah.
[1486.16 --> 1490.76]  I mean, we've optimized a lot for making it possible to deploy things and run things in
[1490.76 --> 1491.94]  the cloud in a few minutes.
[1492.26 --> 1493.56]  So it's actually pretty straightforward.
[1493.84 --> 1497.54]  Like in modal, you basically take any Python function.
[1497.54 --> 1502.22]  So let's say you have a Python function that maybe uses hugging face, just as an example.
[1502.44 --> 1505.48]  And it uses some off-the-shelf model for maybe stable diffusion.
[1506.34 --> 1509.38]  And so let's say you have a Python function, existing Python function that uses hugging
[1509.38 --> 1511.54]  face, and it takes a prompt and it returns an image.
[1511.92 --> 1518.44]  Now you can decorate that Python function in modal with a special decorator and then annotate
[1518.44 --> 1520.56]  it and say, use this image.
[1520.64 --> 1524.16]  And then define an image in code using a special modal syntax.
[1524.16 --> 1528.08]  You can also give us a Docker file, but it's actually, we support almost everyone just
[1528.08 --> 1529.20]  does it in Python internally.
[1530.10 --> 1535.30]  So in code, you can say, basically, you know, use Debian Slim and then install these Python
[1535.30 --> 1540.06]  packages like transformers and accelerate and diffusers and a few other things.
[1540.38 --> 1542.82]  And then annotate the function to say, use that image.
[1543.12 --> 1544.38]  And then that's pretty much it.
[1544.46 --> 1547.70]  Now you can run in the command line, you can do modal deploy or modal run.
[1548.00 --> 1552.22]  And then it just takes that code, builds the container if it doesn't exist and runs it in
[1552.22 --> 1552.56]  the cloud.
[1552.68 --> 1556.88]  And that could typically take less than, if the image is already built, it typically
[1556.88 --> 1562.64]  takes about a second to take the code locally, spot a container in the cloud running that
[1562.64 --> 1563.10]  code.
[1563.94 --> 1565.38]  It works for any Python function.
[1565.76 --> 1567.38]  I mean, that's dead simple right there.
[1567.88 --> 1568.04]  Yeah.
[1568.08 --> 1569.80]  And it works for any Python function.
[1569.94 --> 1573.44]  And you can, you know, you can run pretty much any code you want because we support like,
[1573.48 --> 1576.26]  you know, fat containers, like meaning you can install Python packages.
[1576.26 --> 1581.08]  You can, you can install FFmpeg if you want to transcode some video, like you can install,
[1581.24 --> 1582.82]  you know, whatever thing you want.
[1583.22 --> 1588.30]  And we have a lot of functionality for manipulating images and building dependencies and doing pretty
[1588.30 --> 1590.22]  advanced stuff as a part of that too.
[1590.36 --> 1594.74]  Pre-baking models into images is something people want to do sometimes to optimize cold
[1594.74 --> 1595.52]  start performance.
[1596.16 --> 1597.70]  But yeah, getting started with modal.
[1597.84 --> 1602.22]  Like we really, we really optimize for having that sort of like magic experience.
[1602.22 --> 1606.50]  The first time you try modal, like making it easy to just like, you know, install the
[1606.50 --> 1610.64]  Python package, set up a token and run code immediately in the cloud.
[1611.06 --> 1616.38]  We want that first experience to be magic and sort of set a tone for like, you know, what
[1616.38 --> 1619.56]  modal is and like, you know, the fact that modal we think is a better way to work with the
[1619.56 --> 1620.26]  infrastructure in the cloud.
[1621.12 --> 1626.74]  So one of the things I was wondering about, which I guess it was a surprise to me, like
[1626.74 --> 1629.96]  I didn't really think about it when I was first like using it.
[1629.96 --> 1635.18]  So I don't know, everybody has their different setup, but usually I've got my like code editor
[1635.18 --> 1639.32]  over here and I've got like my terminal over here on maybe another monitor or something.
[1639.44 --> 1645.96]  So I've got both up and I was like writing my, it was a web hook in modal and I had it
[1645.96 --> 1649.46]  like, you know, Python app, whatever.
[1649.86 --> 1655.84]  And when it's a web hook, then like the code runs and then modal gives you this link where
[1655.84 --> 1658.48]  you can like ping like a development web hook.
[1658.48 --> 1662.00]  And of course, like I never get my code right the first time around.
[1662.16 --> 1667.62]  So like I bring up postman or something and I like try to hit my web, like that link.
[1667.82 --> 1673.06]  And of course it like, I get whatever error and kind of without realizing, I just like
[1673.06 --> 1675.70]  went over to my code and I fixed it and I just saved the file.
[1675.84 --> 1680.36]  And I saw over here in my terminal, like it just redeployed and gave me like the link again.
[1680.36 --> 1686.24]  I think that was like a really cool, like surprise for me, I guess, is like, oh, I don't even have
[1686.24 --> 1688.92]  to like, I can just like keep this up over here in the terminal.
[1689.46 --> 1691.00]  How does that work exactly?
[1691.00 --> 1697.38]  And like, was that something that you stumbled upon or, cause I found that a really satisfying
[1697.38 --> 1700.92]  way to develop because where it's like, oh, I just keep this up.
[1700.98 --> 1703.80]  I keep modifying the file and trying it until it works.
[1703.80 --> 1709.04]  And then I can just like control C and say modal deploy and then I'm done.
[1709.28 --> 1709.42]  Right.
[1709.78 --> 1710.42]  Yeah, for sure.
[1710.86 --> 1714.12]  And I know I'm like harping on it, but like kind of think about like feedback loops and
[1714.12 --> 1719.26]  like, you know, the sort of iteration of speed as a CTO, I manage a lot of different teams.
[1719.36 --> 1721.42]  I manage data teams and front end teams and backend teams.
[1721.60 --> 1725.04]  And it's sort of interesting, like how like different disciplines of software engineering
[1725.04 --> 1729.10]  have figured out their own iteration cycles, like the ability to get feedback loops very
[1729.10 --> 1729.46]  quickly.
[1730.06 --> 1732.80]  Backend engineers tend to build a lot, write a lot of unit tests.
[1732.80 --> 1736.12]  Like that's like their way, like they write some code and then they run all the unit tests
[1736.12 --> 1738.38]  or maybe they run a specific unit test that you know is going to break.
[1738.70 --> 1740.94]  And they have that like sort of way to go to get the fast feedback loop.
[1741.26 --> 1744.26]  You go to front end engineers, they have kind of a setup like you just described.
[1744.34 --> 1747.98]  They have like one monitor with the website and then one monitor where they like write
[1747.98 --> 1748.30]  code.
[1748.36 --> 1750.72]  And when they save, it's like hot release the code.
[1751.32 --> 1755.36]  So I feel like sometimes like data and backend people don't give, you know, enough like credit
[1755.36 --> 1756.24]  to like front end engineers.
[1756.36 --> 1760.88]  Like they have really figured out a lot of stuff around like software engineering for like fast
[1760.88 --> 1761.68]  feedback loops.
[1761.68 --> 1765.14]  And actually, if you look at like the modern tool chain for front engineering, I actually
[1765.14 --> 1769.10]  think in many ways it's like more advanced than, than any other part of software engineering.
[1769.24 --> 1773.04]  And so that is the sort of feedback loop that I wanted to have with modal.
[1773.14 --> 1777.86]  And like what I think makes engineers happy is that, you know, super snappy like feedback.
[1777.98 --> 1780.42]  You just have to save code and then it's like live in the cloud.
[1780.94 --> 1781.06]  Yeah.
[1781.06 --> 1784.52]  So, so we built that specifically for the web serving part of modal.
[1784.86 --> 1789.26]  Uh, cause that's something you, you kind of want to have is that ability to, we don't,
[1789.68 --> 1793.26]  you know, it's maybe less like you sort of visual feedback, but it's like the ability to like
[1793.26 --> 1796.74]  deploy something in the cloud and then you can like, you know, hit it with postman or curl
[1796.74 --> 1797.68]  or whatever immediately.
[1798.36 --> 1798.82]  Uh, yeah.
[1798.82 --> 1802.06]  I mean, under the hood, it's, um, it's all super complex.
[1802.12 --> 1803.26]  Actually refactored yesterday.
[1803.26 --> 1803.80]  It's kind of funny.
[1804.20 --> 1805.52]  We just monitor the file system.
[1805.52 --> 1812.68]  And then when we see that any file was updated, we just reload the entire app, uh, in the sub
[1812.68 --> 1816.64]  process and, uh, live patched, uh, the app running in the cloud.
[1817.24 --> 1818.50]  Uh, so it's pretty straightforward.
[1818.68 --> 1819.88]  We had a lot of that already built.
[1820.10 --> 1825.00]  So I think the problems you've been solving for like the past two years are probably really
[1825.00 --> 1830.22]  complicated for you to like loop that into like the category of really simple problems.
[1830.22 --> 1834.26]  I think that would probably be quite complicated for many, many people.
[1834.26 --> 1835.24]  Yeah, for sure.
[1835.24 --> 1839.02]  I guess like, it's like simple in the sense that it's sort of, you know, we already built,
[1839.18 --> 1844.12]  you know, so much of the like underlying complexity to like make that easy, relatively easy to
[1844.12 --> 1845.40]  support the hot reloading.
[1845.46 --> 1849.66]  Like the fact that we already built like so much complexity around like take code and deploy
[1849.66 --> 1851.34]  to the cloud and do that very quickly.
[1851.58 --> 1856.40]  You know, that's a very nice foundation to then like sort of bread and butter.
[1856.82 --> 1857.04]  Yeah.
[1857.16 --> 1857.38]  Yeah.
[1857.38 --> 1860.96]  Like building that, you know, fast container, fast file system stuff.
[1861.44 --> 1863.40]  Uh, it's a lot of cool stuff that that unlocks.
[1863.40 --> 1869.24]  So this is a particularly interesting episode, I would argue for me and probably for quite
[1869.24 --> 1874.26]  a few of our listeners that listen regularly because we're talking about something and Eric,
[1874.34 --> 1878.42]  we have the privilege of you as the person who's created this, but we also have Daniel,
[1878.68 --> 1882.40]  uh, whom I, you know, I've been working closely with and our listeners have been listening to
[1882.40 --> 1886.32]  and hearing Daniel's passion and him building his own business on your platform.
[1886.32 --> 1888.56]  And we talked to lots of different companies.
[1889.02 --> 1895.14]  Um, and so it definitely has intrigued me in a way that not every different, uh, company
[1895.14 --> 1898.02]  owner, if you would, has, I'm kind of curious.
[1898.32 --> 1903.04]  I'm thinking about it from a slightly different perspective from Daniel, but you've really got
[1903.04 --> 1905.50]  me wondering like how to make this happen.
[1905.50 --> 1912.08]  I work at a big company, as you know, um, we have big investments in kind of the, the big cloud
[1912.08 --> 1914.28]  providers as all large companies do.
[1914.78 --> 1921.48]  What are good strategies for companies to say, okay, we have so much in these other big names
[1921.48 --> 1922.86]  and stuff that are out there.
[1922.98 --> 1925.26]  How do we start using modal effectively?
[1925.50 --> 1930.80]  What are the kinds of things you've seen your larger customers do in terms of migration over or
[1930.80 --> 1936.88]  things that you might recommend that enable something of a migration to be more seamless,
[1937.16 --> 1937.84]  less painful?
[1937.84 --> 1943.86]  Because normally when you think of large company migrations, they are almost always, uh, fraught
[1943.86 --> 1947.26]  with pain and misery and challenges for the IT crews.
[1947.26 --> 1953.06]  So how do people get to this thing that we're hearing about today and mitigate all of those
[1953.06 --> 1953.52]  problems?
[1954.16 --> 1954.24]  Yeah.
[1954.40 --> 1954.56]  Yeah.
[1954.60 --> 1958.74]  I mean, first of all, like admittedly, like we're fairly early and, you know, so a lot of
[1958.74 --> 1962.66]  our customer base is early stage companies, like starting from a clean slate who have
[1962.66 --> 1964.12]  absolutely zero infrastructure.
[1964.34 --> 1965.48]  And that makes it a little bit easier.
[1965.70 --> 1966.10]  It does.
[1966.28 --> 1969.92]  In part because there's like nothing legacy that they have to port over in part also because
[1969.92 --> 1971.12]  they're just desperate for tools.
[1971.26 --> 1973.54]  And so the sales process is a little bit easier for us.
[1974.06 --> 1977.82]  I find that like the conversation when we talk to bigger customers is obviously like quite
[1977.82 --> 1978.32]  different.
[1978.98 --> 1982.58]  First of all, there's often an existing data platform that's already built in-house.
[1982.76 --> 1985.94]  There's of course also a security compliance question.
[1985.94 --> 1990.72]  And that's something we're working on that I think long-term, uh, there's a lot of really
[1990.72 --> 1995.90]  cool stuff you can do around, uh, VPC peering and other things to enable that, you know,
[1996.06 --> 1998.76]  big companies to have the security guarantees that they need.
[1999.12 --> 2002.80]  Uh, but I also think it's a separate conversation where like, you know, a bigger company, it's
[2002.80 --> 2006.38]  like there's one person who's a decision maker who has the credit card.
[2006.44 --> 2011.94]  There's another person who built a data platform who, you know, now we're saying, oh, actually
[2011.94 --> 2012.84]  we shouldn't use that.
[2012.94 --> 2013.78]  We should use modal instead.
[2013.78 --> 2015.52]  And so, you know, it's a tougher conversation.
[2015.88 --> 2019.16]  And then there's maybe a data scientist in a third, you know, third person is a data scientist
[2019.16 --> 2020.54]  who really want to deploy models.
[2020.64 --> 2022.90]  They don't really care about the infrastructure, but they heard good things about modal.
[2023.34 --> 2029.02]  I tend to think in those conversations, it's about like finding like a niche use case that's
[2029.02 --> 2035.04]  like, you know, low risk that, you know, doesn't sit in sort of some sort of critical path
[2035.04 --> 2037.48]  of like, you know, the whole business relies on this.
[2037.48 --> 2041.74]  And, you know, so it could be some sort of greenfield, you know, something new, you know,
[2041.74 --> 2046.94]  deploying a model or a very simple pipeline, uh, something that, you know, maybe doesn't
[2046.94 --> 2050.32]  touch like super sensitive data or have like super critical like guarantee.
[2050.54 --> 2055.18]  So some like research project, like that's typically where I tend to start is, you know,
[2055.50 --> 2060.70]  and, and often trying to find people, you know, data scientists and machine learning engineers
[2060.70 --> 2063.52]  who feel like the platform team doesn't really have time for them.
[2063.52 --> 2068.10]  Like, you know, they want something that lets them iterate quickly, you know, without having
[2068.10 --> 2069.26]  to bother the ops team.
[2069.62 --> 2072.64]  Those are probably the easiest conversations to have, you know, with like the bigger companies.
[2073.08 --> 2073.68]  That's good guidance.
[2073.78 --> 2074.40]  I appreciate that.
[2074.70 --> 2080.12]  I think it's very fitting that like the platform is at least right now, and please correct me
[2080.12 --> 2085.04]  if I'm wrong, is it is very Python centric in terms of like the development workflow and,
[2085.10 --> 2086.18]  and what's supported.
[2086.50 --> 2092.28]  Do you see this being sort of like, like you said that you can support so many different types
[2092.28 --> 2095.32]  of jobs in, and apps in modal.
[2095.62 --> 2100.90]  So, you know, on one side you could say, well, this could become like very general purpose
[2100.90 --> 2108.84]  in some ways, or it could like fill a really niche, uh, gap that obviously it is starting
[2108.84 --> 2112.16]  to fill and just do that really well.
[2112.16 --> 2115.30]  And like continue to kind of go deeper there.
[2115.42 --> 2121.10]  What do you see as kind of the path forward, or maybe it's a both and with, you know, something's
[2121.10 --> 2122.24]  coming sooner than later?
[2122.50 --> 2124.60]  I think of modal as my 20 year project.
[2124.60 --> 2127.90]  Like, you know, like I'm finally building a tool I always wanted to have.
[2127.96 --> 2130.52]  And like, I want to spend, you know, rest of my career doing that.
[2130.64 --> 2135.60]  Ideally, I, I, I, so my sort of end goal is to build, you know, very general purpose
[2135.60 --> 2138.38]  set of tools that have helped data teams be more productive.
[2138.38 --> 2142.84]  That, that being said, kind of like what I said at the start of this show, like I, I
[2142.84 --> 2145.78]  sort of realized like, that's a, you know, almost like make a little maniac vision.
[2145.78 --> 2150.68]  Like I, I think it all comes down to like in practice to finding something that resonates
[2150.68 --> 2155.14]  with customers and, you know, drives growth and validates demand and then sort of sequencing
[2155.14 --> 2157.88]  and kind of layering all like sort of adjacent product over time.
[2158.40 --> 2163.34]  We tend to think right now, like we have one, one sort of use case and one sort of target
[2163.34 --> 2167.60]  persona that works really well right now, which is, you know, deploying online machine learning
[2167.60 --> 2172.62]  inference that, that I think, you know, is an area where we see enormous amounts of demand
[2172.62 --> 2173.12]  and traction.
[2173.52 --> 2176.30]  So kind of how that, you know, fits into sequencing.
[2177.06 --> 2181.26]  I think, you know, an obvious next step for us is to make fine tuning and training easier
[2181.26 --> 2186.64]  to do in modal, but also thinking about, you know, like pre-processing, you know, scheduling,
[2186.86 --> 2191.16]  retraining, so it happens on a loop on a regular basis, maybe thinking about like, you know,
[2191.16 --> 2195.60]  how do you move your data sets into modal to some extent to like hosting more like stateful
[2195.60 --> 2196.18]  applications?
[2197.44 --> 2202.28]  I think there's like a long list of sort of, you know, like layering on like step by step,
[2202.74 --> 2206.06]  more and more advanced features and gradually expand to take over.
[2206.30 --> 2210.00]  And because I think the demand is there, like, you know, no one wants to have this like 35
[2210.00 --> 2212.48]  different point solutions that they have to integrate themselves, right?
[2212.52 --> 2215.78]  And a lot of the data landscape today, I think is very fragmented.
[2216.34 --> 2220.96]  And, you know, as a result, a lot of data teams have to integrate like so many different
[2220.96 --> 2222.76]  vendors and kind of duct tape them together.
[2222.76 --> 2227.36]  Like, I think there's, you know, there's a big case to be made for either some sort of,
[2227.40 --> 2232.26]  you know, consolidation or some sort of like defragmentation of the space where fewer vendors
[2232.26 --> 2233.04]  do more.
[2233.36 --> 2236.94]  So long term, that's absolutely my vision is to, you know, we're starting with this like
[2236.94 --> 2237.46]  place right now.
[2237.60 --> 2239.10]  Similarly, in terms of languages, right?
[2239.12 --> 2241.06]  Like you mentioned, you know, Python versus other languages.
[2241.18 --> 2246.46]  We think Python right now is a great place to start because that's 90, you know, percent
[2246.46 --> 2248.34]  plus of data teams use Python.
[2248.34 --> 2252.56]  But definitely think long term, you know, a lot of the infrastructure that we built is,
[2252.66 --> 2254.32]  you know, low level and it's written in Rust.
[2254.44 --> 2256.14]  It doesn't really care about what stuff is running.
[2257.48 --> 2262.18]  We think it could be, you know, great to add support for TypeScript or R or Go or Rust
[2262.18 --> 2262.70]  or whatever.
[2263.40 --> 2266.46]  So there's many different access to this, like in terms of like how we think about sequencing
[2266.46 --> 2266.96]  and expansion.
[2267.72 --> 2269.44]  I'm just saying you saw me raise my hand.
[2269.52 --> 2270.08]  I love Rust.
[2270.20 --> 2271.68]  It's my current favorite language.
[2271.68 --> 2275.20]  Go and Rust are on the back end.
[2275.66 --> 2279.10]  But let me ask you a question that came to mind as you're going through that.
[2279.44 --> 2285.18]  As you're kind of exploring the world and you have certain areas of focus, but there's
[2285.18 --> 2289.14]  also some kind of able to stretch out depending on different parts of the strategy you have.
[2289.54 --> 2296.12]  How do you see kind of, to use a very generic open term, the edge out there, things that
[2296.12 --> 2297.44]  are not in the cloud?
[2297.44 --> 2303.12]  Do you see you doing anything in the future that would be kind of edge based or do you
[2303.12 --> 2306.70]  see yourself more as the cloud partner for things that might be out on the edge and you
[2306.70 --> 2308.88]  have APIs and such available to those?
[2309.30 --> 2313.64]  How do you conceive either working with or including the edge in your overall strategy?
[2314.14 --> 2319.56]  I think edge is primarily useful for like very, very latency sensitive applications.
[2320.28 --> 2325.18]  And that's probably a segment of the market that we just feel like that's not what model
[2325.18 --> 2325.90]  is going to be good at.
[2325.90 --> 2330.18]  Because, you know, if you do things in like Wasm or V8 isolates, like, you know, in that
[2330.18 --> 2332.26]  case, you can make it like kind of fast enough.
[2332.58 --> 2336.54]  But, you know, the way we focus on serverless right now is sort of fat traditional like
[2336.54 --> 2341.22]  Linux, you know, distributions in containers or VMs.
[2341.40 --> 2345.84]  And that just has, you know, it's always going to have some non-trivial overhead, you know,
[2345.84 --> 2348.64]  maybe a second, maybe like eventually we can get it to a few hundred milliseconds.
[2349.34 --> 2352.92]  I think to sort of edge workloads that people talk about, like, you know, that's when you
[2352.92 --> 2354.94]  really need like one millisecond, right?
[2355.02 --> 2358.96]  Like, and you're really trying to, either you're doing some like IoT type, you know,
[2359.00 --> 2365.50]  like controlling like devices for manufacturing, or you're doing high performance like CDN,
[2365.60 --> 2369.38]  like SEO type stuff, you know, where you want like your website to be absurdly fast.
[2370.02 --> 2374.30]  Those are the types of workloads I don't really think model is suited super well for.
[2374.40 --> 2377.90]  And I'm more than happy to let other vendors dominate that space.
[2377.90 --> 2381.90]  We tend to think on the time scale of like a few hundred milliseconds and up.
[2382.02 --> 2383.50]  That's where we focus right now.
[2383.82 --> 2384.70]  No, that's a great answer.
[2384.88 --> 2390.38]  And definitely, I mean, trying to address every problem, you know, out there in the larger
[2390.38 --> 2392.66]  space isn't a successful approach.
[2392.84 --> 2396.70]  So hearing when I talk to people and I hear, no, we're not going to go there.
[2397.08 --> 2400.84]  I usually take that as a very good thing in terms of focus and good strategy.
[2400.98 --> 2401.82]  So good to hear that.
[2402.28 --> 2402.44]  Cool.
[2402.68 --> 2402.86]  Yeah.
[2402.86 --> 2409.34]  But kind of as we wrap up here, I'd be curious to hear, like, obviously, you're very passionate
[2409.34 --> 2414.54]  about this project, you want to work on it for 20 years, like this is your life's work,
[2414.58 --> 2415.54]  it sounds like.
[2415.80 --> 2419.76]  What are the things that are on your mind right now in terms of the things that you're excited
[2419.76 --> 2421.60]  about seeing happen in modal?
[2421.84 --> 2428.04]  And like over the next year, what are you like most excited about seeing come to pass as
[2428.04 --> 2429.46]  you continue working on the project?
[2429.46 --> 2433.68]  The thing that I personally spend the most time on is probably figuring out the like
[2433.68 --> 2441.14]  ergonomics of the SDK itself, like in code, like how do you express programs that like
[2441.14 --> 2445.82]  execute in a distributed way in the cloud and still making it feel like intuitive and easy
[2445.82 --> 2449.74]  to the user without having to think about the fact that, you know, this function runs in
[2449.74 --> 2451.38]  a different container than this function.
[2451.86 --> 2454.18]  We've made that work reasonably well for online inference.
[2454.18 --> 2457.32]  But I think, you know, when you go to like training and start dealing with file systems,
[2457.32 --> 2460.28]  like there's certain things that are like still a little bit like gnarly and I'm working
[2460.28 --> 2461.20]  a lot on that right now.
[2461.40 --> 2466.28]  So like making that user experience good and sort of intuitive, I think it's really important.
[2466.58 --> 2470.84]  And a similar note, like modal right now is like somewhat janky when you run it inside
[2470.84 --> 2473.00]  notebooks for some particular reasons.
[2473.30 --> 2477.22]  I'm not going to get into it, but it's something I definitely want to make, you know, the user
[2477.22 --> 2482.20]  experience, like running modal inside a notebook, I think should obviously be, you know, we need
[2482.20 --> 2482.88]  to fix that too.
[2483.26 --> 2483.90]  It's fine.
[2483.90 --> 2487.54]  It's not like terrible, but, you know, I definitely don't think it's like quite yet
[2487.54 --> 2487.98]  where it is.
[2488.10 --> 2491.16]  If you run modal in the script, there's a lot of this like backend stuff.
[2491.16 --> 2495.60]  Like we definitely need to like scale this up, you know, 10 X or a hundred X to scale
[2495.60 --> 2497.70]  we are like, you know, we see a lot of demand.
[2498.10 --> 2500.70]  Modal does not have a publicly available signup right now.
[2500.72 --> 2502.40]  Like you can sign up and you go on a wait list.
[2503.12 --> 2506.46]  And part of it is that just that, like we want to have a little bit more control over the
[2506.46 --> 2506.76]  scale.
[2506.76 --> 2511.68]  Like there's a lot of work we need to do on the backend to build a foundational, you know, architecture
[2511.68 --> 2513.46]  running all of this stuff, which is a very hard problem.
[2513.46 --> 2516.52]  Like, you know, it's building, you know, it's not your own lamb, there's our own Kubernetes.
[2517.52 --> 2525.30]  There's a lot of work we need to do on GPU support and in particular cold start with
[2525.30 --> 2529.04]  GPU models and fast loading of GPU models.
[2529.04 --> 2531.52]  So those are some, there's a lot of cool work.
[2531.52 --> 2536.40]  We're spending a lot of time on there, especially when it comes to like containers and in general,
[2536.52 --> 2543.50]  like isolation and VMs, like, you know, turns out that like supporting GPUs in a secure way in a
[2543.50 --> 2545.52]  multi-tenant environment is quite hard.
[2545.52 --> 2550.28]  So we're going very deep and like, you know, I'm reading about Linux device drivers and
[2550.28 --> 2552.40]  CUDA and like trying to understand all of those things.
[2553.26 --> 2553.56]  Yeah.
[2553.58 --> 2554.98]  I mean, those are all the things we're working on.
[2555.04 --> 2560.08]  I think in a year's time, like I think modal, you know, we'll see a lot more traction, you
[2560.08 --> 2562.86]  know, modal for like other things than just online inference.
[2562.86 --> 2565.18]  Like we're going to see a lot of people using modal for training.
[2565.38 --> 2568.48]  We're going to see a lot of people using modal for like parallelization.
[2568.48 --> 2573.10]  I think we're going to have, you know, much more like sort of, you know, customers on the
[2573.10 --> 2576.62]  enterprise side right now, like we're focusing very much on the startups, but we're doing,
[2576.78 --> 2579.84]  laying a lot of the security compliance work to be able to go up market.
[2580.70 --> 2581.10]  Yeah.
[2581.26 --> 2583.92]  Those are some of the things where I'm pretty excited about.
[2584.44 --> 2584.62]  Yeah.
[2584.72 --> 2584.94]  Yeah.
[2585.02 --> 2586.48]  There's a lot to be excited about.
[2586.64 --> 2593.36]  And yeah, please pass on my personal thanks again to the modal team for making me look good
[2593.36 --> 2595.36]  today and recently.
[2595.36 --> 2598.02]  And yeah, really excited about what you're doing.
[2598.02 --> 2600.64]  And appreciate you taking time to chat with us.
[2600.78 --> 2601.30]  Yeah, of course.
[2601.42 --> 2602.68]  I'm also very excited about this.
[2602.76 --> 2604.10]  So always happy to talk about it.
[2613.14 --> 2615.54]  Thank you for listening to Practical AI.
[2616.12 --> 2619.88]  Your next step is to subscribe now, if you haven't already.
[2620.30 --> 2625.00]  And if you're a longtime listener of the show, help us reach more people by sharing Practical
[2625.00 --> 2626.34]  AI with your friends and colleagues.
[2626.34 --> 2631.74]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2632.32 --> 2636.10]  Check out what they're up to at Fastly.com and Fly.io.
[2636.40 --> 2641.10]  And to our Beat Freakin' Residence, Breakmaster Cylinder, for continuously cranking out the best
[2641.10 --> 2641.82]  beats in the biz.
[2642.10 --> 2643.00]  That's all for now.
[2643.00 --> 2644.44]  We'll talk to you again next time.
[2644.44 --> 2644.48]  We'll talk to you again next time.
