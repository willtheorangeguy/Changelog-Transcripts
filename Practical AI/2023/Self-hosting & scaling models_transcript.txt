[0.00 --> 8.58]  Welcome to Practical AI.
[9.14 --> 15.90]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.90 --> 18.72]  are changing the world, this is the show for you.
[19.14 --> 24.32]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.32 --> 24.62]  listen.
[24.90 --> 26.72]  Check them out at Fastly.com.
[26.72 --> 31.98]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.38 --> 33.66]  No ops required.
[33.98 --> 36.02]  Learn more at fly.io.
[43.20 --> 46.24]  Welcome to another episode of Practical AI.
[46.62 --> 48.20]  This is Daniel Whitenack.
[48.32 --> 54.56]  I am the founder and CEO at Prediction Guard, and I'm joined as always by my co-host, Chris
[54.56 --> 57.54]  Benson, who is a tech strategist at Lockheed Martin.
[57.84 --> 58.50]  How are you doing, Chris?
[58.82 --> 60.00]  Doing very well today, Daniel.
[60.04 --> 60.48]  How's it going?
[60.88 --> 61.60]  Oh, it's going great.
[61.72 --> 67.58]  I spent the afternoon in sort of a brainstorming session with a couple of our team members
[67.58 --> 70.10]  here at Prediction Guard, and it was a ton of fun.
[70.36 --> 76.46]  So talking about a lot of prompt engineering things and how different models perform and
[76.46 --> 77.34]  that sort of thing.
[77.40 --> 78.46]  So it was a good time.
[78.88 --> 80.52]  I'm glad you're doing that because you know what?
[80.52 --> 83.26]  I just want things that just work, you know?
[83.38 --> 84.50]  I don't want to have to think about it.
[84.54 --> 85.78]  I'm glad you're thinking about it.
[86.40 --> 90.10]  I think we might have someone else to talk to who knows how to make things that just work.
[90.80 --> 91.32]  Yeah, yeah.
[91.42 --> 97.44]  Well, a lot of the models that we're running sort of just work for us in terms of inference
[97.44 --> 104.30]  because we're hosting some of our models in Base 10, and we've got Tuan joining us from
[104.30 --> 105.08]  Base 10 today.
[105.18 --> 105.84]  How are you doing, Tuan?
[106.18 --> 106.70]  Hi, Dan.
[106.84 --> 107.22]  Hi, Chris.
[107.30 --> 108.74]  Nice to see you guys again.
[108.74 --> 110.58]  Back to the kind words, Dan.
[110.86 --> 112.44]  Yeah, yeah, for sure.
[112.62 --> 118.74]  Well, it's exciting to have you actually back on the show because it was, I believe, I looked
[118.74 --> 125.74]  it up, it was like May, June 2021 when we recorded and released the last episode with
[125.74 --> 126.02]  you.
[126.48 --> 127.80]  So how are you doing?
[128.04 --> 129.44]  What's new?
[129.60 --> 130.62]  And how is Base 10?
[130.70 --> 131.66]  How's the ride been?
[132.72 --> 134.06]  Yeah, it's been crazy.
[134.06 --> 138.06]  I feel like the last, I think it was like May 2021.
[138.96 --> 140.78]  That's like a millennium in AI time, you know.
[140.96 --> 141.62]  Oh my God.
[141.80 --> 144.82]  If it actually does feel like it was a different job ago.
[145.26 --> 145.66]  Yes.
[145.90 --> 147.90]  It feels like the job before the last job.
[148.56 --> 148.76]  Oh no.
[150.06 --> 151.02]  If that makes sense.
[151.14 --> 156.08]  No, I think, being crazy, I think the last two years for everyone here have probably been
[156.08 --> 156.80]  a bit of a whirlwind.
[157.16 --> 161.26]  You guys are pretty on top of current things and machine learning and AI.
[161.52 --> 168.14]  And I think, I imagine, just like for you guys, it's hard to keep up at times with what's
[168.14 --> 168.36]  going on.
[168.46 --> 168.94]  I think, you know.
[169.10 --> 172.98]  We only do one show a week and, you know, it's getting, we almost need a daily show.
[173.10 --> 174.38]  There's so much content now.
[174.58 --> 175.42]  It's not enough.
[175.62 --> 175.76]  Yeah.
[175.76 --> 181.74]  Don't give our listeners ideas because I don't know if I can do a daily show, but it
[181.74 --> 182.30]  is a lot.
[182.50 --> 188.42]  And I think, so I'm looking back previous at our episode and last time we talked about
[188.42 --> 192.06]  sort of the easiest way to create ML apps.
[192.28 --> 195.26]  That was kind of part of how the conversation was framed.
[195.48 --> 202.76]  And I know just from working with you and talking with you as friends that a lot has
[202.76 --> 209.36]  changed and you've seen some things within how people are deploying machine learning,
[209.52 --> 213.64]  AI systems that now Base 10 is really focused on.
[213.74 --> 220.34]  Could you give us kind of like the high level view of Base 10 and the type of problem, the
[220.34 --> 221.64]  type of solution that you're offering?
[221.98 --> 222.50]  Yeah, yeah, yeah.
[222.62 --> 226.32]  I think, I think it's just worth probably like pointing out, you know, before I go into
[226.32 --> 230.70]  Base 10 specific things, like one of the, like the key things that changed since we last
[230.70 --> 231.60]  talked, I think, you know.
[231.76 --> 232.04]  Sure.
[232.04 --> 236.96]  If you think of like the year of like 2012 to 2020, you know, data scientists were the
[236.96 --> 238.12]  ones doing a lot of machine learning.
[238.28 --> 240.88]  I think, you know, that's changed for a number of reasons.
[241.56 --> 245.52]  I have a lot of thoughts on that, but probably the bigger changes are, you know, the emergence
[245.52 --> 246.86]  of good open source models.
[247.40 --> 251.28]  And I know you do a lot of work with that and, you know, like we've seen Hugging Face
[251.28 --> 256.04]  as a community evolve into like really, really vibrant place where if you want to get a sense
[256.04 --> 260.72]  of how fast things are moving, it doesn't take long to, you know, take screenshots of
[260.72 --> 264.70]  Hugging Face every Monday morning and see how the trending is changing.
[264.70 --> 267.52]  And you'll see that things are pretty different every week.
[267.52 --> 271.50]  I don't know if it was Daniel that said this or another friend of mine, but the analogy
[271.50 --> 276.40]  was that, you know, Hugging Face has become to AI kind of what GitHub has always been for
[276.40 --> 278.30]  software developers over the last decade or so.
[278.82 --> 281.44]  It's just, you know, it's the place to go to find it.
[281.50 --> 282.58]  Anyway, I didn't mean to interrupt you there.
[282.58 --> 282.98]  Yeah.
[283.32 --> 286.16]  And the good about it, but also the confusing too.
[286.34 --> 295.04]  It's like, you know, you have like random person clones model or copies model and uploads
[295.04 --> 299.44]  random version of that model that like maybe works.
[300.34 --> 300.64]  Yeah.
[300.88 --> 301.36]  I understand.
[301.50 --> 304.64]  I feel like the game you have to play with Hugging Face is like, but does it run?
[305.02 --> 306.10]  You know, does the model run?
[306.28 --> 307.28]  But does the model run?
[307.28 --> 313.02]  But, you know, I think open source emerged and I think like stuff like Whisper showing
[313.02 --> 319.66]  up and, you know, some of these OCR type replacement models showing up, you know, they're probably
[319.66 --> 324.60]  the more interesting ones to me, not because what they do, but because they end up just solving
[324.60 --> 326.32]  a lot of open problems.
[326.46 --> 332.50]  You know, if you think about transcription as a problem, think about nuance and like how
[332.50 --> 333.50]  long they were working for that.
[333.50 --> 333.66]  Yeah.
[333.72 --> 338.34]  Like literally 20 or 30 years of work, just kind of, all right, that's a solved problem
[338.34 --> 338.54]  now.
[338.62 --> 339.24]  Let's move on.
[339.86 --> 343.06]  Oh, we've actually solved multi-language with the same model too.
[343.18 --> 344.74]  Business models come and go, don't they?
[344.94 --> 345.20]  Yeah.
[345.30 --> 345.50]  Yeah.
[345.66 --> 346.20]  It's wild.
[346.32 --> 352.46]  And I think like the last piece is just around, you know, like the chat GPT moment for AI
[352.46 --> 354.72]  interesting for a number of reasons.
[354.82 --> 360.28]  I personally think it's someone who built infrastructure that it's most interesting because if you want
[360.28 --> 364.42]  to call that the iPhone moment of AI, I think it's a bit different to that because it's
[364.42 --> 365.62]  so early in the journey.
[366.10 --> 371.04]  It's like if the iPhone showed up and we were all using 5110 from Nokia, the world would
[371.04 --> 372.14]  be very, very different.
[372.28 --> 378.32]  And I think because consumers and developers, their first taste of machine learning and AI
[378.32 --> 381.06]  was through chat GPT and GPT APIs.
[381.06 --> 385.28]  Otherwise, the stakes are just, you know, it's just harder to build something good.
[385.46 --> 389.58]  Like, you know, people don't want to use a model that takes 12 seconds to run.
[389.94 --> 395.24]  You know, like high speed production inference is, you know, taken for granted when you're
[395.24 --> 396.70]  using this model.
[396.78 --> 400.86]  And then when you kind of combine that with, okay, open source models need to be run somewhere.
[401.20 --> 401.76]  All right.
[401.86 --> 404.92]  We personally think that's like, okay, well, there's a massive infrastructure opportunity
[404.92 --> 411.06]  that, well, maybe not even opportunity that just say a fact that a whole new stack will
[411.06 --> 416.80]  be built to support models to be able to power these end user experiences.
[416.80 --> 422.48]  And I think like that's kind of the core insight kind of going into base 10 and talking a bit
[422.48 --> 428.04]  about base 10 around like what's changed is that, you know, we kind of two years ago when
[428.04 --> 430.46]  we were talking about data scientists, we weren't talking about engineers.
[430.46 --> 435.70]  I think that's pretty key to our story, which is that I think we came to the realization
[435.70 --> 440.50]  that every engineer needs to grapple with machine learning now, as opposed to maybe a
[440.50 --> 442.08]  smaller market of data scientists.
[442.42 --> 448.94]  I think going from smaller models that run in memory to larger models is another big, you
[448.94 --> 450.04]  know, focus change we've had.
[450.16 --> 454.72]  I think there's a bunch of language stuff and NLTK stuff and, you know, you were doing
[454.72 --> 455.50]  all that work, Daniel.
[455.92 --> 460.16]  But for the most part, everyone was using, you know, scikit-learn and scikit-learn models for
[460.16 --> 461.18]  the most part run in memory.
[461.62 --> 462.58]  On CPUs.
[462.86 --> 463.62]  On CPUs.
[463.96 --> 464.20]  Yeah.
[464.56 --> 469.50]  If you think just in that time period, the amount of maturation, you know, that's occurred
[469.50 --> 473.56]  in this industry, it still bought you something a second ago, which kind of hit me.
[473.96 --> 478.24]  And that is most people out there in the general public, you know, are really just getting into
[478.24 --> 479.86]  this, you know, with chat GPT and stuff.
[480.06 --> 481.82]  And we've come a long road already.
[482.08 --> 486.16]  I just, I'm listening to you and it's amazing how far we've come in such a short time.
[486.16 --> 486.60]  Yeah.
[486.60 --> 486.88]  Yeah.
[486.92 --> 487.40]  It's insane.
[487.76 --> 488.40]  A hundred percent.
[488.50 --> 492.28]  And I think that, you know, going from small models to large models as well, it's just
[492.28 --> 494.92]  like that change kind of happened pretty quickly.
[495.18 --> 495.58]  Yeah.
[495.68 --> 497.50]  I saw one who did a bunch of work with small models.
[497.50 --> 500.40]  Like they have their time in place, but they're just not that fun anymore.
[502.10 --> 506.92]  Like something that runs in memory just doesn't give you the same feeling as, and then I think
[506.92 --> 511.44]  the last one is just so much of the stuff that was happening with machine learning outside
[511.44 --> 516.94]  of Fang, I'd say was like Fang had some production use cases around like ad serving and search
[516.94 --> 517.82]  and whatnot.
[518.08 --> 521.30]  But outside of that, it was mostly just internal workflows.
[521.72 --> 525.16]  You'd go and work on fraud and content moderation and recommendation systems.
[525.16 --> 529.76]  And I think, you know, going from, hey, every product is going to have some sort of machine
[529.76 --> 530.30]  learning in it.
[531.24 --> 537.14]  Every existing product will definitely, and 90% of new products will be built with a new
[537.14 --> 541.92]  pillar that is machine learning and AI, which wasn't the case, I think, two years ago, which
[541.92 --> 543.06]  is just crazy to think about.
[543.34 --> 543.42]  Yeah.
[543.60 --> 545.40]  It's completely changed in that time.
[545.72 --> 551.70]  I think one thing that was brought into focus for me while you were talking was that as soon
[551.70 --> 561.22]  as you make this leap to kind of larger models and you make the leap from some closed API
[561.22 --> 566.48]  that's very fast to maybe running your own model, there's two things that become like immediately
[566.48 --> 567.24]  clear.
[567.24 --> 572.70]  One is the infrastructure challenge around that, which I think is the workflow around
[572.70 --> 576.48]  that and the model hosting, you know, base 10, of course, is an expert in that.
[576.60 --> 583.36]  And the other side of that is like the product sort of concerns around running these things,
[583.36 --> 587.28]  which I feel like, you know, we always have great conversations too.
[587.34 --> 591.58]  And because like you're on the one side of that and I'm probably on the other side because
[591.58 --> 597.58]  yeah, like when you're using chat GPT or even the open AI API, they have layers of, you know,
[597.66 --> 602.94]  protections on the prompts and like on the output, they have, you know, filters to make
[602.94 --> 605.02]  sure they're not responding in certain ways.
[605.02 --> 607.68]  And there's all these product concerns that people don't think about.
[607.68 --> 611.26]  And then they take like a llama to model or something, they run it.
[611.34 --> 614.50]  And then there's like, oh, this doesn't respond.
[614.50 --> 616.40]  Like this is not a product, right?
[616.50 --> 619.30]  And so like the infrastructure is a piece of that.
[619.58 --> 625.44]  The ability to iterate very quickly with models of a variety of types, I think is part of that
[625.44 --> 626.42]  infrastructure challenge.
[626.52 --> 630.02]  How do you see that infrastructure piece of this kind of playing out?
[630.46 --> 630.58]  Yeah.
[630.72 --> 634.48]  Maybe just before I say, go into that, when you were saying that, it reminded me of like,
[634.72 --> 638.56]  I bought a drone in 2014 and I was so excited.
[638.78 --> 639.98]  It was a DJI Phantom 3.
[639.98 --> 644.94]  I was so pumped and, you know, I flew it around a bit and then I basically had autopilot mode
[644.94 --> 645.92]  where you didn't have to do anything.
[646.50 --> 647.98]  Like it kind of just stabilizes itself.
[648.48 --> 652.26]  And then there was this button that said manual mode and it has like all sorts of warnings.
[652.42 --> 655.48]  And I remember saying, like being like, oh, how hard can it be?
[655.76 --> 655.92]  Oh, right.
[656.26 --> 656.58]  Oh.
[657.18 --> 658.20]  I'm really like joking.
[658.36 --> 663.10]  Like I was in a safe space, but I put it into manual mode while I was up in the air
[663.10 --> 666.06]  and it just fell to the ground very, very fast.
[666.72 --> 668.42]  I don't know, Chris, do you have some experience with this?
[668.42 --> 673.00]  Well, I'm in aerospace professionally, so I know a little bit about that.
[673.14 --> 673.50]  And yes.
[673.82 --> 680.06]  Chris, weren't you like the TV host of the drone racing competition or something like this?
[680.06 --> 680.18]  I was.
[680.18 --> 680.38]  Yeah.
[680.38 --> 680.70]  Yeah.
[680.70 --> 680.82]  Yeah.
[680.82 --> 680.90]  Yeah.
[680.90 --> 681.42]  Yeah.
[681.42 --> 682.54]  A few years ago.
[682.76 --> 683.24]  Yeah.
[683.26 --> 687.78]  I was one of the hosts of the first drone racing league.
[687.92 --> 692.72]  They had a championship series and they were using, instead of you as a human, they were
[692.72 --> 695.16]  navigating obstacle courses and stuff like that.
[695.16 --> 701.48]  And what I learned through that experience is when you have how much autonomy is required
[701.48 --> 703.80]  to make even small things fly well.
[704.08 --> 704.22]  Yeah.
[704.30 --> 704.72]  And yeah.
[704.76 --> 707.66]  So I, I sympathize with you for going on manual there.
[707.76 --> 708.72]  Oh no, don't do it.
[708.78 --> 709.36]  Don't do it.
[709.62 --> 714.08]  And the analogy I think holds here, it's like the closed, the closed API, it seems so great.
[714.08 --> 717.42]  And then you, you see something like a llama too or a mistrawl and you're like, okay, I'll
[717.42 --> 718.40]  just rip and replace this.
[718.46 --> 721.66]  And it's like, nope, that's not going to work for a number of reasons.
[721.66 --> 724.14]  And I think that's kind of how we see about it.
[724.14 --> 728.70]  Like think about infrastructure based sandwich is that running models in production is very,
[728.78 --> 729.20]  very difficult.
[729.38 --> 731.04]  It's difficult for a number of reasons.
[731.04 --> 736.22]  So I can decide, but like from like a user requirements perspective, like latency and
[736.22 --> 740.50]  throughput paramount costs are something you want to optimize.
[740.50 --> 743.88]  Data privacy is, you know, a whole nother beast.
[744.84 --> 748.90]  Security comes into play that orchestrating this across a bunch of different hardware,
[749.54 --> 752.38]  orchestrating this across clouds becomes a problem.
[753.00 --> 754.28]  Benchmarking these things isn't easy.
[754.60 --> 759.12]  And that's even before you go into all the evals and the, you know, the kind of like the
[759.12 --> 761.42]  guardrails you want to put around this thing to get it running.
[761.58 --> 764.52]  And I know some of the stuff that you think a lot about, Dan.
[764.68 --> 768.28]  So just as an extension of what you're saying, and Daniel, you mentioned it at first, but
[768.28 --> 772.66]  if you could also talk a little bit about what the difference is about just hosting, like,
[772.66 --> 777.44]  like just having the model hosted and kind of the idea around what you have to put around
[777.44 --> 779.00]  it as a, to make it a product.
[779.00 --> 782.74]  Cause I don't think most people talk about, I don't hear a lot of conversations about that.
[782.84 --> 787.22]  And it's a big set of gotchas on what to do, you know, and kind of what's involved in
[787.22 --> 787.48]  that.
[787.66 --> 790.52]  What's your thinking around that when, when people are looking at doing that?
[790.90 --> 793.50]  I can talk well about the first one and I have thoughts about the second.
[793.88 --> 797.70]  Dan's going to be the expert around a lot of piece of that, but to get a model running
[797.70 --> 800.72]  production, there's actually a ton of work you need to do from an infrastructure perspective.
[801.28 --> 805.02]  And this is before we talk about the workflow stuff, you know, you need to figure out how
[805.02 --> 807.00]  to containerize this thing and get this image running.
[807.16 --> 811.74]  Like, you know, as we alluded to earlier, like just taking a model of hugging face and expecting
[811.74 --> 813.40]  it to run is not a thing.
[813.86 --> 816.44]  You know, there's a bunch of requirements that these models have.
[816.72 --> 819.22]  There's quantization inside the code.
[819.56 --> 825.82]  There is different base images that they might need based on Torch and PyTorch and Python
[825.82 --> 826.30]  versions.
[826.98 --> 831.32]  And then, you know, you can really find yourself in a bit of a pickle, just trying to dockerize
[831.32 --> 831.74]  a model.
[831.86 --> 834.98]  So the first thing is you need to figure out how to get this in some sort of containerized
[834.98 --> 836.50]  form so you can run it elsewhere.
[837.32 --> 840.96]  Once you have that, the truth is that you need to spit up some sort of service that can
[840.96 --> 842.14]  deal with variable traffic.
[842.56 --> 845.84]  And the reason why that is, is that traffic, you know, these things tend to be expensive.
[846.26 --> 848.30]  They tend to be bound by compute.
[848.78 --> 853.22]  So if you get smashed with a bunch of requests, it's not like you can just have one model
[853.22 --> 856.30]  and it will queue out, they will time out, the whole thing will slow down, your product
[856.30 --> 856.68]  won't work.
[856.74 --> 859.82]  So you need to figure out how to scale up and down with traffic.
[859.94 --> 863.36]  And then you need to figure out all the security concerns that come with all that.
[863.66 --> 865.12]  That's just on the serving layer.
[865.56 --> 867.92]  Now you need to start thinking about the workflow layer that sits on top of that.
[868.00 --> 870.86]  And I think, you know, version management is a non-existent for them.
[870.98 --> 876.32]  So hooking it up into CICD, to really treat this like a service or a microservice that
[876.32 --> 879.98]  has putting your model in an API, you need observability and logging.
[879.98 --> 882.44]  Another whole set of features.
[883.04 --> 888.50]  And what you realize is that taking a model and getting it working in production behind
[888.50 --> 894.98]  a reliable, secure, performant API and maybe cost efficient, as someone who's done this
[894.98 --> 900.88]  myself, as someone who's built a company to try to abstract this way, it is easily for
[900.88 --> 905.12]  one model, a couple of people have had counts work for a couple of quarters, if you're lucky,
[905.58 --> 906.14]  at scale.
[906.14 --> 913.60]  And I think that is the most efficient organizations that can hire people with Kubernetes experience
[913.60 --> 914.46]  to be able to do this.
[914.56 --> 919.90]  So that's the type of things that we try to abstract away from our users, where it's like,
[919.96 --> 922.98]  you know, you figure out the Python code, we'll figure out everything else.
[923.34 --> 928.12]  And we'll give this model this first class treatment so that you can version around, that
[928.12 --> 931.34]  you can log around it, that you can observe it and you can call it.
[931.52 --> 933.40]  But you don't need to think so much about that.
[933.40 --> 933.78]  You get that.
[934.38 --> 939.68]  That's now to the point where you have something behind an API and ready to consume.
[940.02 --> 944.22]  Now, there's a bunch of stuff that needs to happen to make sure that, you know, it doesn't
[944.22 --> 946.76]  start saying random stuff that you protect against hallucinations.
[946.92 --> 950.48]  It's not just ingesting PII all the time.
[950.76 --> 952.84]  Dan can probably talk really quickly about that as well.
[953.24 --> 953.54]  I'm sure.
[953.54 --> 959.66]  Yeah, I think part of the reason why I'm always excited to talk to Tuen and his team at Base
[959.66 --> 961.78]  10 is because they are experts in this.
[962.20 --> 964.68]  All of those layers that we just talked about.
[964.84 --> 972.30]  I was actually on a call with someone the other day and we were talking about like spinning
[972.30 --> 974.22]  up some microservices or something.
[974.30 --> 978.22]  And I think my comment was like, I just really don't want to care about Kubernetes because
[978.22 --> 983.24]  I don't want to like wake up lying in a ditch crying in the fetal position.
[983.74 --> 985.68]  Like that's how I view that like whole world.
[985.84 --> 989.82]  So props to you and your team for dealing with that side of things.
[989.94 --> 995.40]  I think that's what's allowed us then on like the prediction guard side in a lot of ways to
[995.40 --> 1002.48]  like bring up a model quickly and then have the time to think about some of these other
[1002.48 --> 1004.14]  things too.
[1004.24 --> 1011.24]  And I don't know if you can comment on like, I have my own perspective from trying to run
[1011.24 --> 1018.24]  models for, for my company, but it would be interesting to hear the perspective of different
[1018.24 --> 1021.00]  personas that are coming into Base 10.
[1021.00 --> 1030.66]  Like, are they people that are sort of application developers that are, you know, not infrastructure
[1030.66 --> 1031.18]  people?
[1031.42 --> 1032.78]  Are they like data scientists?
[1032.78 --> 1036.42]  Like what are the, what are the types of people that are coming to Base 10?
[1036.60 --> 1044.56]  And I, maybe along with that, like, as you mentioned, closed APIs are getting used a lot,
[1044.56 --> 1049.04]  but still people are coming over to think about like hosting their own models.
[1049.04 --> 1053.04]  One question would be like, why, like, who are these people and why?
[1053.70 --> 1053.90]  Totally.
[1054.26 --> 1055.84]  I'll answer the second one first.
[1056.40 --> 1061.10]  No, I think I'll add them together is that it is more and more just engineers.
[1061.60 --> 1067.42]  I'd say like, I don't know if there's any, there's any distinction now between like, I'd
[1067.42 --> 1070.38]  say it's less and less data scientists, your traditional data scientists.
[1070.52 --> 1075.16]  It's more and more people with some ML exposure, product engineers, infrastructure engineers who've
[1075.16 --> 1078.24]  tried to build it themselves and have really felt the pain.
[1078.24 --> 1083.70]  And I think from a product engineering perspective, like why want people want to use open source
[1083.70 --> 1088.40]  APIs, I think cost is one big thing is that open AI tends to stack up over time.
[1088.40 --> 1094.52]  I think, or Anthropic, I think the other one is data privacy and security is that you don't
[1094.52 --> 1098.12]  want to just be piping over all your data to open AI today.
[1098.12 --> 1101.44]  And especially when you start to talk about B2B use cases and enterprises.
[1102.10 --> 1105.38]  And I think there's like, probably the more interesting one is that there are just like
[1105.38 --> 1108.20]  a long tail of people working on weird models.
[1108.74 --> 1110.00]  People are fine tuning models.
[1110.44 --> 1112.96]  Fine tuning open AI models is not great.
[1113.44 --> 1118.56]  You get a bit more control with that manual mode with open source models.
[1118.56 --> 1123.32]  And so it's kind of like the long tail of use cases, I'd say, are coming more and more.
[1123.44 --> 1126.00]  And these can be engineers, they can be machine learning engineers.
[1126.62 --> 1130.82]  It can be honestly like a lot of audio models, like different modalities that there's not
[1130.82 --> 1134.90]  that much exposure to with closed APIs and a lot of custom stuff as well.
[1135.42 --> 1138.02]  You mentioned, you know, like shipping data over to open AI.
[1138.02 --> 1143.58]  And I have talked to gazillions of people who have that as a constraint in their businesses,
[1143.98 --> 1147.86]  you know, because the attorneys for the business are like, nope, you don't want to send,
[1147.98 --> 1151.12]  you know, your proprietary information and stuff over that.
[1151.52 --> 1155.40]  I guess you would not have that issue at all with base 10, would you?
[1155.48 --> 1159.06]  I mean, that kind of goes away altogether when you're hosting in that way, right?
[1159.82 --> 1159.94]  Yeah.
[1160.32 --> 1161.78]  You have ownership of your data.
[1161.86 --> 1163.04]  We don't log any of that data.
[1163.36 --> 1167.72]  You're treating the model as just like a map of input, the output and nothing else.
[1167.72 --> 1168.08]  Yeah.
[1168.16 --> 1172.16]  That would really solve a lot of people's problems by taking an approach like that.
[1172.50 --> 1172.64]  Yeah.
[1172.68 --> 1175.66]  And I think the second piece there is that once you adopt the base 10 approach, you can
[1175.66 --> 1179.04]  then start to think about like self-hosting, deploying it within your own VPC.
[1179.20 --> 1185.62]  So, you know, we have customers that deploy base 10 within their own AWS account and data
[1185.62 --> 1189.40]  never leaves kind of their boundaries or their accepted boundaries.
[1190.40 --> 1190.46]  Yeah.
[1190.46 --> 1197.12]  And we've kind of, I think you've framed the concerns that you're looking at with base 10
[1197.12 --> 1202.62]  very well, these sort of infrastructure scaling concerns of hosting your own model.
[1202.62 --> 1209.86]  Could you maybe take a step back and just describe like, if I go into base 10, like how have you
[1209.86 --> 1213.82]  architected the approach like to, I'm an application developer.
[1214.20 --> 1220.78]  I want to run, you know, some random fine tune of Llama 2 that I've created somehow.
[1220.78 --> 1220.90]  Wow.
[1221.22 --> 1222.50]  What is it like for me?
[1222.66 --> 1226.50]  What does that look like with the way that you've structured this?
[1226.66 --> 1231.30]  And what's some of the thinking behind that in terms of the workflow and how you want it
[1231.30 --> 1238.12]  to be for people so that they can treat, I guess, that model as a first class thing that
[1238.12 --> 1242.32]  is a first class asset in terms of what they're monitoring and logging, that sort of thing?
[1242.76 --> 1243.40]  Yeah, for sure.
[1243.70 --> 1248.94]  Our goal is just to make it easy and, you know, try to take away as much of the complexity,
[1249.14 --> 1253.36]  but, you know, maybe more importantly, it's still that you'd have a bit of control.
[1253.96 --> 1256.74]  You know, I think base 10 data is like a one line to deploy your models.
[1256.84 --> 1258.00]  Like, you know, we don't believe that anymore.
[1258.46 --> 1262.22]  You know, either we think that, you know, actually having a little bit of structure around it
[1262.22 --> 1266.46]  gives you actually a bit of structure up front, gives you a lot more flexibility.
[1266.84 --> 1267.88]  I'm a bit down the line.
[1267.88 --> 1273.36]  And so we have an open source library called Trust, which is basically a, it's an abstraction
[1273.36 --> 1276.46]  that if you write your model in, you get kind of everything free.
[1276.64 --> 1279.12]  And so basically you need to write two things.
[1279.46 --> 1283.24]  You need to write one Python class with a load function and a predict function.
[1283.36 --> 1284.68]  And this is vanilla Python code.
[1284.90 --> 1287.08]  It can sit within your monorepo.
[1287.68 --> 1289.50]  You can specify requirements as you want.
[1289.90 --> 1291.78]  There's nothing base 10 about these files.
[1292.32 --> 1294.16]  You know, you could run them outside of base 10.
[1294.22 --> 1295.04]  I think that's very important.
[1295.04 --> 1298.72]  Well, but once you write that load and predict function, it does two things.
[1298.82 --> 1301.14]  One, it tells us, hey, what are you trying to do here?
[1301.20 --> 1302.38]  And, you know, we can load that up.
[1302.62 --> 1304.74]  And when we deploy a model, we load that function.
[1304.86 --> 1307.80]  When we infer, we run the predict function.
[1308.46 --> 1311.96]  But more importantly, within those functions, we allow you to compile stuff down.
[1312.04 --> 1316.58]  We allow you to kind of do the tricks that you need to do so that, you know, you still
[1316.58 --> 1317.38]  have that control.
[1317.84 --> 1321.20]  And, you know, within that, you can write preprocessing and post-processing functions
[1321.20 --> 1326.74]  that allow you to, you know, maybe, like, strip out some data, log something, monitor something.
[1327.16 --> 1330.72]  But really, it's still giving that control at the product and application level while
[1330.72 --> 1332.90]  still abstracting out the thing we want with trust.
[1333.32 --> 1338.72]  Once you have a trust developed, and you can go to trust.base10.co and check out a bunch
[1338.72 --> 1340.84]  of these, it's a pretty simple abstraction.
[1340.84 --> 1342.62]  And you can just push that up.
[1343.06 --> 1346.82]  And we kind of give you all the work on version management around that deploy trust.
[1347.46 --> 1347.90]  Yeah.
[1348.14 --> 1355.30]  Could you speak then to, like, that's, like, the prep, kind of, that goes into, oh, I've
[1355.30 --> 1356.30]  got my weird model.
[1356.60 --> 1358.26]  I'm writing this Python class.
[1358.40 --> 1361.24]  I'm going to deploy it on somewhere.
[1361.88 --> 1366.12]  And I know that, like, one thing that I think is really cool how you've made base10
[1366.12 --> 1368.54]  trust is, like you mentioned, it is open source.
[1368.54 --> 1374.24]  And so you can run, trust things, and deploy in a variety of ways.
[1374.34 --> 1379.18]  One of those being, like, base10's hosted infrastructure, which is, of course, easy.
[1379.30 --> 1384.72]  But it's also, like, generally a great, great sort of framework to package your models.
[1385.14 --> 1388.54]  But let's say that you do kind of go the base10 route.
[1388.72 --> 1393.52]  You deploy this through the base10 client to base10.
[1394.14 --> 1398.52]  Could you kind of compare and contrast, like, let's say I just tried to run a base10 client.
[1398.54 --> 1408.34]  Run my model in a fast API API in a EC2 instance or ECS or, like, whatever that is in my cloud.
[1408.96 --> 1414.92]  What is going to be different about what I look at when I kind of look at my model in base10
[1414.92 --> 1417.90]  versus running this API somewhere else?
[1418.06 --> 1420.12]  And how does that make a meaningful difference?
[1420.46 --> 1425.06]  Or what are you trying to do in terms of making a meaningful difference for the day-to-day for
[1425.06 --> 1425.36]  people?
[1425.86 --> 1426.18]  Yeah.
[1426.36 --> 1429.96]  Well, I think what you're doing is that, so besides, you know, you can run that model
[1429.96 --> 1430.54]  in fast API.
[1431.06 --> 1431.38]  Great.
[1431.58 --> 1432.32]  You got this model.
[1432.86 --> 1433.50]  You give it an input.
[1433.60 --> 1434.16]  It gives you an output.
[1434.46 --> 1434.78]  Fantastic.
[1434.96 --> 1435.58]  Let's carry on.
[1435.70 --> 1439.22]  But it's, like, the depth of features and the creation of workflow, which are really
[1439.22 --> 1439.86]  important here.
[1439.96 --> 1443.88]  And so, like, the depth of features is that, hey, if you can do that with fast API, great.
[1443.96 --> 1445.10]  You're still going to have to set up auto-scaling.
[1445.62 --> 1446.96]  You're still going to have to set up observability.
[1447.42 --> 1449.36]  You're going to have to set up logging and whatnot.
[1449.92 --> 1450.60]  Hardware management.
[1450.60 --> 1455.52]  But I think the workflow is probably more important, to be honest, because we're creating
[1455.52 --> 1458.80]  a defined way for you to publish new versions of this.
[1459.26 --> 1462.64]  If you want to A-B test two models, you can have two models running at the same time.
[1463.18 --> 1468.76]  You know, it's really that the removal of boilerplate and the addition of some workflow
[1468.76 --> 1472.72]  so that, you know, when you are deploying this in production and you need to roll back
[1472.72 --> 1477.22]  a version, you don't need to go and scramble to find that fast API file that you were using
[1477.22 --> 1478.60]  before and we've all been there before.
[1478.60 --> 1484.32]  And so, that creation of workflow is probably, I think, what a lot of our customers probably
[1484.32 --> 1485.14]  use us for.
[1485.68 --> 1491.64]  Besides, you know, I think the production grade inference is a given, but a lot of the
[1491.64 --> 1493.18]  differentiation comes from that workflow.
[1494.06 --> 1497.84]  Just to totally boil it down, you're saving them a lot of work right there.
[1498.02 --> 1498.90]  Yeah, 100%.
[1498.90 --> 1499.10]  Yeah.
[1499.26 --> 1501.38]  There's a lot of kind of grunge work.
[1501.64 --> 1506.46]  It reminds me of Dan liking to do his data massaging that I'm always teasing him about.
[1506.46 --> 1511.68]  But joking aside, you're basically saving us all sorts of work so we can get into production
[1511.68 --> 1516.94]  faster, get it up and running, and know that it's production grade all the way through with
[1516.94 --> 1519.42]  a minimal amount of effort and know that it's just there.
[1519.76 --> 1520.28]  100%.
[1520.28 --> 1522.20]  Like, we're working with this customer right now.
[1522.34 --> 1526.68]  This is a pretty late stage startup.
[1526.68 --> 1530.20]  It's hundreds of millions of dollars, AI-native product.
[1530.52 --> 1536.40]  They've got a team of four AI info people to manage this, and they've been working on this
[1536.40 --> 1537.20]  for about two years.
[1537.78 --> 1541.42]  You know, we're able to replicate and get a more performant API up and running in two
[1541.42 --> 1541.68]  days.
[1542.22 --> 1542.46]  Wow.
[1542.46 --> 1546.26]  I think that is kind of what we are trying to...
[1546.26 --> 1549.76]  It's the performance, the workload, it's the maintainability, but it's also just the
[1549.76 --> 1550.48]  speed to prod.
[1550.90 --> 1558.28]  I don't know how many of your users do this, but the fact that this might be sort of revealing
[1558.28 --> 1563.12]  about me as a person and also reveal some utility of Base 10.
[1563.12 --> 1565.28]  But I can literally...
[1565.28 --> 1569.84]  Like, last night, I'm sitting on my couch, and I can log in to Base 10 on my phone, and
[1569.84 --> 1577.80]  that just changed the auto-scaling from two replicas to five max replicas and the timeout
[1577.80 --> 1585.56]  and all those things of the auto-scaling of my Llama 2 fine-tune from my couch in between
[1585.56 --> 1586.68]  Halo games.
[1587.24 --> 1588.42]  So that was...
[1588.42 --> 1588.88]  That's terrifying.
[1588.88 --> 1595.96]  I don't know what that reveals about me as a person, but certainly that ease of use,
[1596.04 --> 1597.26]  I think, is really interesting.
[1597.58 --> 1604.06]  It's like that proverb when you try to solve a problem, and then you're like, I'll solve
[1604.06 --> 1608.08]  this with regex, and then you just have another problem to solve.
[1608.40 --> 1609.30]  It's kind of like that.
[1609.44 --> 1614.40]  It's like you want to deploy your model, and then you want to deploy it with Kubernetes,
[1614.40 --> 1620.16]  and then you have a whole other problem to solve and solve the auto-scaling stuff and
[1620.16 --> 1621.08]  all that.
[1621.72 --> 1625.32]  And then I think on top of that, it's just all the SRE work that you have to do for that
[1625.32 --> 1625.62]  service.
[1625.94 --> 1627.20]  Like, what happens when it goes down?
[1627.80 --> 1630.36]  What happens when you need to migrate something over?
[1630.78 --> 1633.04]  What happens when there's a new GPU you want to use?
[1633.04 --> 1635.44]  Because there's just so much...
[1635.44 --> 1640.30]  I feel like we've really turned the corners, and I think stuff like AI and ML, that really
[1640.30 --> 1642.92]  has helped here because people want to move fast.
[1643.14 --> 1647.20]  It's like, I feel like we've put the build versus buy debate a little bit to rest for
[1647.20 --> 1649.72]  a bit, where we just don't hear it as much.
[1649.80 --> 1651.66]  It's like, hey, we want to build it ourselves.
[1651.84 --> 1654.74]  Like, people are just like, we want managed solutions.
[1655.42 --> 1655.56]  Yeah.
[1655.72 --> 1659.42]  You got to go fast these days, because if you don't, somebody else is going to get there
[1659.42 --> 1661.52]  first, and you're not going to have a business.
[1661.52 --> 1664.34]  And the market is remarkably talent-constrained.
[1664.60 --> 1668.34]  Like, again, Dan, you're saying this, and this makes me happy because, like, so, you
[1668.34 --> 1673.82]  know, Dan's background is in data platform and dealing with all of these things.
[1673.92 --> 1674.78]  You know, like, it is...
[1674.78 --> 1676.18]  I've cried myself to sleep.
[1676.34 --> 1677.20]  In fetal position.
[1679.74 --> 1681.58]  And so, really, it's just that ease of use.
[1681.70 --> 1684.80]  And, like, it's ease of use and the ability to scale with you.
[1685.10 --> 1689.10]  And that's probably, like, the two things which we try to bring to our customers.
[1689.10 --> 1693.44]  But then, I think, just even outside of Base 10, it's probably the biggest opportunity,
[1693.44 --> 1698.52]  I'd say, in machine learning infrastructure right now is, think of all the user stories
[1698.52 --> 1701.56]  that are important now that weren't important 12 months ago.
[1701.88 --> 1707.54]  And maybe just take a slightly longer-term view than, what can I build around OpenAI APIs,
[1707.66 --> 1709.04]  which has, like, stopped a lot of attention.
[1709.50 --> 1711.80]  These are all places where Base 10 is thinking about going.
[1712.00 --> 1714.34]  Or, like, you know, we will partner with people who are doing it.
[1714.34 --> 1717.82]  If you think about people at the emails layer, think about people at the fine-tuning layer,
[1717.90 --> 1721.82]  you think of people at the training layer, at the observability layer, the logging layer.
[1721.96 --> 1724.64]  It's, like, there's an entire new stack here to be built.
[1724.74 --> 1725.92]  And that's a massive opportunity.
[1726.52 --> 1728.78]  And those eggs are a really interesting company to look at, to be honest,
[1728.84 --> 1730.28]  because, you know, they were training their models.
[1730.72 --> 1731.62]  They were helping people train them.
[1731.70 --> 1732.74]  They were remarkably early.
[1733.22 --> 1738.32]  But, like, the value is very, very clear to a pretty sophisticated buyer in Databricks.
[1738.32 --> 1743.08]  And so, to any folks building tools around here, like, so much value to be added.
[1743.74 --> 1744.38]  It's a green field.
[1745.30 --> 1751.76]  I have another question to ask you, because you are living in kind of that world of model deployments
[1751.76 --> 1754.38]  and the various ways that people are doing this.
[1754.58 --> 1759.08]  People are fine-tuning their own models or just using open models.
[1759.40 --> 1763.10]  I'm wondering how you see the trends going.
[1763.10 --> 1768.98]  So, you've already talked a little bit about open models being available, small to big models,
[1769.12 --> 1771.12]  and how people are hosting them.
[1771.40 --> 1780.34]  There's tons of people that are also exploring this area around running models kind of at the edge
[1780.34 --> 1782.52]  or in various environments or on laptops.
[1783.06 --> 1787.34]  And also people that are exploring kind of, you already mentioned quantization
[1787.34 --> 1792.60]  and running models on CPUs, potentially instead of GPUs.
[1792.60 --> 1801.96]  I'm curious, as someone who hosts a lot of models in the world, what are you seeing in terms of this trend?
[1802.16 --> 1806.02]  Because you hear about these topics, but I don't really have a good sense of...
[1807.04 --> 1814.54]  Obviously, people are exploring those things, but are those people just extra loud on the internet?
[1815.14 --> 1817.24]  Or certainly there's use cases.
[1817.48 --> 1820.96]  Chris knows them well for running certain things at the edge.
[1820.96 --> 1826.26]  But for many people out there that are maybe building a SaaS platform or something,
[1826.80 --> 1828.76]  that's less relevant.
[1828.94 --> 1830.58]  Although maybe the costing...
[1830.58 --> 1834.38]  You mentioned cost optimization as well around that sort of thing.
[1834.58 --> 1835.00]  So, yeah.
[1835.06 --> 1836.34]  How are you seeing as someone...
[1836.34 --> 1840.44]  I guess my question is, as someone who hosts a lot of models for a lot of people,
[1840.94 --> 1843.48]  what are you seeing as people's concerns,
[1843.48 --> 1850.88]  both in terms of that costing, optimizing models, and deployment targets, I guess?
[1851.42 --> 1851.68]  Totally.
[1852.00 --> 1855.46]  I think what we're seeing is it's remarkably early, to be honest.
[1855.64 --> 1856.34]  There are opportunities...
[1856.34 --> 1861.42]  People are deploying stuff on edge, but I think there's not enough of them today.
[1861.58 --> 1864.40]  Just kind of think about a generalized opportunity there.
[1864.40 --> 1869.82]  And so I think there's a company called OctoML that started with edge deployment,
[1870.00 --> 1871.70]  and then things were just like, let's move this out.
[1872.22 --> 1874.12]  Because that's where the opportunity today is.
[1874.42 --> 1879.24]  I think all the stuff that's happening around running these models on less and less hardware,
[1879.50 --> 1881.20]  or optimizing them in X-way or Y-way,
[1881.62 --> 1883.46]  it's remarkably intriguing, right?
[1883.46 --> 1888.88]  It's pretty crazy that we can get a model that we can barely run on the biggest GPU we can find,
[1889.36 --> 1891.38]  and some person figured out how to compile it down,
[1891.76 --> 1895.88]  or re-run it with C++ kernels, and all of a sudden it runs anywhere.
[1896.30 --> 1897.10]  That's pretty fantastic.
[1897.36 --> 1900.38]  But I do think that we're still in the research phase there.
[1900.86 --> 1902.94]  We're in the experimental research phase,
[1903.06 --> 1905.96]  and we've seen a lot of people deploy those models.
[1906.68 --> 1909.14]  Yes, we've seen a lot of people play with those models.
[1909.26 --> 1910.40]  We've seen a lot of interest in those models.
[1910.40 --> 1913.14]  But I can't really think of too many examples of people running those models.
[1913.46 --> 1915.24]  in production just yet.
[1915.34 --> 1918.04]  But it seems inevitable that over time...
[1918.04 --> 1918.72]  Oh, it will happen.
[1918.86 --> 1920.22]  ...that is the arc that we are on.
[1920.32 --> 1920.56]  Yeah.
[1920.70 --> 1922.04]  These models are getting smaller and smaller.
[1922.30 --> 1922.58]  Yeah.
[1922.74 --> 1927.04]  When I'm not on the podcast, I'm in a world where it's all about things moving around in time and space.
[1927.48 --> 1933.20]  And a lot of those things will have AI capability on board going forward.
[1933.34 --> 1934.32]  So that's...
[1934.32 --> 1934.96]  I agree with you.
[1935.02 --> 1937.50]  There's a lot of research going on, and no one...
[1937.50 --> 1939.84]  It's not a solved problem in one...
[1939.84 --> 1942.48]  There's not a set of best practices yet, if you will.
[1942.48 --> 1945.46]  But it's an area that is majorly ripe.
[1945.96 --> 1956.96]  I'll be really curious to see if you guys or another company is able to leverage all the expertise you've built up and experience you've built up in the cloud and kind of move out into those areas.
[1957.26 --> 1958.22]  Bring your own device, yeah.
[1958.42 --> 1958.66]  Yeah.
[1958.66 --> 1961.38]  There's millions of devices out there just waiting for you.
[1961.58 --> 1961.86]  Yeah.
[1962.06 --> 1966.48]  I'd say the challenge there is just around how...
[1966.48 --> 1969.46]  I'm guessing Lockheed's devices are a bit of a snowflake.
[1969.64 --> 1976.68]  And you can't build for one type of device and just go and apply that to the next device there.
[1976.68 --> 1982.40]  And I feel like there's probably some generalization that needs to happen at the OS layer before we can do that.
[1982.44 --> 1985.88]  But I am also completely uneducated on Edge stuff.
[1986.00 --> 1987.94]  So you probably have a lot more to say that than I do.
[1987.94 --> 1989.96]  Well, and it's interesting too.
[1990.10 --> 1997.54]  I sort of ask this in a leading way because one of the people that we're talking to kind of genericized this.
[1997.54 --> 2006.94]  But they run some equipment at the Edge in manufacturing and they have like a hub at the Edge, which is air-gapped, which doesn't talk to the internet.
[2007.12 --> 2014.00]  But their whole like next generation of things is going to be internet connected.
[2014.00 --> 2033.92]  And when I was talking to them about like doing some things with large language models in that environment, you know, essentially where we got was, hey, well, it's going to be more hassle for you to figure out some of these like model optimization things and all of that than to just like set up an API in base 10 or something like that.
[2033.92 --> 2037.10]  And just connect it out if that's where you're headed anyway.
[2037.56 --> 2042.58]  And it's not like a military security concern like one of these situations.
[2042.58 --> 2046.32]  So, yeah, I think we're probably see both and.
[2046.52 --> 2058.22]  But for a lot of people, it's like kind of how I've categorized these things in my mind is, yeah, some people will want to run Kubernetes in their own infrastructure and they have the expertise to do that.
[2058.74 --> 2060.62]  And if that's you, then like, great.
[2060.70 --> 2062.72]  You're one of maybe a few people on the planet.
[2062.94 --> 2063.30]  I don't know.
[2063.56 --> 2063.94]  Good on you.
[2064.22 --> 2065.18]  Good on you.
[2066.08 --> 2072.08]  And similarly, like with Chris, if you're running a lot of models on the Edge, which I know certain people are.
[2072.08 --> 2073.82]  And in certain industries, it's really important.
[2074.42 --> 2075.08]  That's great.
[2075.16 --> 2076.38]  And that expertise will be there.
[2076.50 --> 2088.46]  But I think for the I don't know, my sense is that for a lot of majority of people, like separating out that infrastructure concern of model hosting is really, really a useful way to think about things.
[2088.46 --> 2089.14]  So, I don't know.
[2089.22 --> 2089.56]  We'll see.
[2089.80 --> 2091.80]  I'm always bad at predicting the future.
[2092.14 --> 2093.76]  We talked to this one customer.
[2094.44 --> 2101.62]  He was saying that for some reason, the CEO bought a bunch of GPUs and they literally have machines in the office.
[2101.62 --> 2110.94]  They're like, oh, well, we're going to do the I think Amazon has like the Kubernetes anywhere or something where you can basically like a hybrid sort of thing.
[2111.18 --> 2111.32]  Yeah.
[2111.32 --> 2111.54]  Yeah.
[2111.88 --> 2114.88]  You know, we ran away from that opportunity.
[2115.28 --> 2116.46]  It's suffice to say.
[2116.98 --> 2120.04]  But, you know, there are I think these people are thinking about these problems.
[2120.14 --> 2124.26]  I don't know if there is a a solution here just yet.
[2124.26 --> 2124.68]  Yeah.
[2125.30 --> 2141.76]  Well, as you kind of think about so obviously and I know just from our discussions, like you're helping a lot of people and really significant use cases in the space with already with what you're doing with the infrastructure side of model hosting.
[2141.76 --> 2150.62]  But as you look to kind of the next I can't even say like the next years because things move so quickly.
[2150.62 --> 2165.24]  But as you look towards the future and like what is not yet solved on the infrastructure side with model hosting and what are like you and base 10 really excited to dig into what comes to mind and what are you thinking about?
[2165.72 --> 2169.74]  Yeah, I think within the containers like that layer is gets very interesting.
[2169.74 --> 2176.96]  I think, you know, BLM, which I'm sure you've played around with TGI, which, you know, they're both great.
[2177.10 --> 2181.12]  I still I think they're still far from ready for prime time just yet.
[2181.52 --> 2186.98]  BLM, TGI and TRCLM that NVIDIA just put out.
[2187.26 --> 2194.06]  I think there's going to be more and more of these frameworks and supporting these frameworks, I think, is going to be very, very key for us and what we're really excited about.
[2194.06 --> 2201.06]  So we're going deeper at that layer so you can kind of bring your own framework on your container and really benefit from that.
[2201.14 --> 2205.36]  So, you know, we're going to have first class support or TRTLM pretty soon.
[2205.36 --> 2207.38]  And we already do for TGI and BLM.
[2207.48 --> 2209.22]  And I think that side is pretty interesting.
[2209.42 --> 2211.68]  I think, you know, we have a big launch coming up.
[2211.94 --> 2215.60]  I'm happy to talk about it right now, actually, but around multi-cluster.
[2215.60 --> 2222.08]  So that's basically being able to, one, use your own compute to bring your compute to base 10.
[2222.58 --> 2231.54]  So the control plane sits on base 10 and the workload plane, considered GCP, Azure, AWS, or some combination of the three.
[2231.80 --> 2234.06]  And then we'll keep adding clouds to that.
[2234.42 --> 2239.68]  And so I think that's very, very exciting, especially in the enterprise that because, you know, people want self-hosted.
[2240.06 --> 2240.54]  That's huge.
[2240.92 --> 2241.40]  It is.
[2241.54 --> 2242.44]  It's really nice.
[2242.90 --> 2243.50]  That's going to be big.
[2243.50 --> 2245.94]  And then kind of just beyond serving.
[2246.26 --> 2250.86]  And I think with really science, you know, we've already had one foray and we learned a lot.
[2250.98 --> 2254.64]  And, you know, we ended up retiring, but we're going to get into fine tuning at some point.
[2254.76 --> 2263.10]  I think like that's, we keep seeing, like, just like I said about kind of like the edge device stuff and the compilation stuff is that fine tuning is still an art.
[2263.40 --> 2266.88]  I'm a little bearish on like APIs that say, give me your data, I'll give you a model.
[2266.98 --> 2268.94]  Like, I think you need more controls.
[2268.94 --> 2273.76]  As someone who built an API that said, give us your data, we'll give you a model with Blueprint.
[2274.36 --> 2275.72]  You know, I think you need more control.
[2276.04 --> 2277.54]  You need control over your base models.
[2277.66 --> 2282.66]  You need more control over even the fine tuning scripts to customize that model.
[2282.76 --> 2285.10]  We'll start to think about that very soon.
[2285.22 --> 2289.14]  You know, we're already doing a bunch of work with customers to make sure that we're marching in the right direction.
[2289.14 --> 2295.74]  So I'm very excited about that, which is that, you know, over time, base 10 becomes this place where you can run your models great.
[2296.20 --> 2298.86]  But then you can also start to collect data sets around your model.
[2299.42 --> 2306.76]  Just imagine if you could just give your model to base 10 and then, you know, you either opt in and we basically write all your input and output data to S3.
[2307.50 --> 2308.00]  That's beautiful.
[2308.36 --> 2308.52]  Yeah.
[2308.58 --> 2313.04]  Like essentially a level of caching for model inputs, outputs.
[2313.26 --> 2313.32]  Yeah.
[2313.42 --> 2313.72]  Exactly.
[2313.72 --> 2314.04]  Yeah.
[2314.22 --> 2325.34]  The multi-cloud thing really will be big for enterprise, by the way, just to that point, because I think most enterprises across many industries are recognizing that their future is a multi-cloud world.
[2325.46 --> 2327.14]  It's no longer tied to one.
[2327.70 --> 2342.04]  And if you have base 10 able to do that hosting and run a control plane and you can deploy into any of the cloud clusters that you happen to be in, maybe different parts of the company emphasize one or the other, then that takes a lot of challenge that they're currently facing out of that.
[2342.14 --> 2342.94]  So it's pretty sweet.
[2342.94 --> 2344.86]  I mean, also just open up opportunities, right?
[2344.92 --> 2346.32]  Especially in the GPU-contained world.
[2346.88 --> 2348.22]  You can get them from wherever you want.
[2348.50 --> 2355.10]  And then, you know, I think once you have data sets as well, then fine-tuning just becomes obvious, which is like, okay, now can I fine-tune this?
[2355.28 --> 2361.08]  And, you know, maybe it's even like, hey, hook up your open AI endpoint using base 10 so we can collect that data set.
[2361.18 --> 2366.38]  And then we can create that fine-tuned minstrel or llama to keep you the model you want.
[2366.42 --> 2369.06]  So I think there's a lot of interesting things along that whole stuff.
[2369.06 --> 2374.54]  And as I said to you guys earlier, there's so much opportunity here for people building in the tooling layer.
[2375.18 --> 2376.66]  Friend AI and ML.
[2376.92 --> 2377.90]  It's very exciting overall.
[2377.90 --> 2378.54]  Yeah.
[2378.78 --> 2386.38]  Well, we appreciate you taking time out of doing great work in that layer to talk to us and share with our listeners.
[2386.88 --> 2388.74]  This is a great conversation.
[2389.24 --> 2395.54]  And hopefully we have you on the show in less than three years from now.
[2395.54 --> 2399.72]  But if not, at least three years from now, hopefully sooner.
[2400.26 --> 2404.46]  So thank you for joining us again and giving us an update and some insights around this.
[2404.72 --> 2408.82]  And really appreciate what you all are doing and appreciate you taking time.
[2409.30 --> 2409.54]  Of course.
[2409.66 --> 2410.26]  Thank you.
[2410.50 --> 2412.90]  Thank you so much for spending time on the show.
[2413.02 --> 2413.74]  I thought it was fun to be on it.
[2413.74 --> 2424.84]  Thank you for listening to Practical AI.
[2425.34 --> 2429.18]  Your next step is to subscribe now, if you haven't already.
[2429.62 --> 2435.64]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2436.10 --> 2441.04]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2441.04 --> 2445.42]  Check out what they're up to at Fastly.com and Fly.io.
[2445.82 --> 2451.12]  And to our Beat Freakin' Residence Breakmaster Cylinder for continuously cranking out the best beats in the biz.
[2451.40 --> 2452.30]  That's all for now.
[2452.60 --> 2453.72]  We'll talk to you again next time.
