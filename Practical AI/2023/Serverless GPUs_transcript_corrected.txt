[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[42.66 → 45.72] Welcome to another episode of Practical AI.
[46.06 → 47.42] This is Daniel Whiten ack.
[47.52 → 53.20] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[53.20 → 56.18] Benson, who is a tech strategist at Lockheed Martin.
[56.18 → 57.14] How are you doing, Chris?
[57.68 → 58.62] I'm doing fine.
[58.70 → 63.24] It's been interesting times, though it's not what we're going to be talking about today.
[63.72 → 72.58] Been watching the showdown between Google and Microsoft over ChatGPT and Bard, and things
[72.58 → 74.86] are happening as we're recording this.
[75.28 → 79.18] I thought maybe you would have been too distracted with the new Harry Potter game.
[79.18 → 80.90] Well, there is that.
[81.54 → 87.08] Yes, we all have our secret little things that we do to keep entertained.
[87.62 → 88.30] Yeah, yeah.
[88.50 → 95.06] Well, I forget one of our recent guests brought up that quote of like, you don't need to do
[95.06 → 96.42] machine learning like Google.
[96.58 → 99.92] And you're talking about like Google and Bard and all of these things.
[99.92 → 105.12] And when you think about those things, you think about like, oh, these like data centres
[105.12 → 110.10] full of GPUs and these huge supercomputers that they've got at their disposal to do things,
[110.10 → 116.36] which isn't the type of GPU infrastructure that most practitioners have access to.
[117.02 → 122.96] And that happens to be maybe the topic of what we'll get into today a little bit.
[123.10 → 123.74] Excellent.
[123.74 → 128.26] With Eric Underman, founder of Banana, serverless GPUs.
[128.30 → 128.82] Welcome, Eric.
[129.26 → 129.70] Thank you.
[129.80 → 131.00] That was a beautiful lead in.
[131.60 → 136.18] Definitely want to help people get that Google level infrastructure without that level of
[136.18 → 136.46] effort.
[136.72 → 137.66] So glad to be here.
[138.00 → 138.34] Awesome.
[138.82 → 141.14] Yeah, well, we're really excited to have you.
[141.22 → 146.22] I have to say I did spin up a model in Banana leading up to this conversation.
[146.22 → 149.16] So I'm pretty excited to talk about it.
[149.16 → 153.62] But before we get into the specifics of all the cool things that you're doing,
[153.74 → 159.12] I know that our listeners, like I say, they're probably very familiar with GPUs and like
[159.12 → 163.94] why they're important to AI, machine learning, modelling.
[164.38 → 170.22] But maybe they've just heard of serverless as like this cloud thing that is like a thing
[170.22 → 171.74] that people do in the cloud.
[171.86 → 173.20] They do serverless things.
[173.42 → 176.64] And they've never thought about like serverless GPUs.
[176.64 → 182.22] Could you just like step back for a second and describe like, first off, like for people
[182.22 → 187.24] that might need just a very brief intro, what do you mean when you say serverless?
[187.50 → 190.92] And then kind of take us into like serverless GPUs.
[190.96 → 191.82] Is that a new thing?
[191.90 → 193.76] Has that existed before?
[194.14 → 196.32] I'm curious to hear your perspective.
[197.06 → 198.92] So I love your specific phrasing.
[199.04 → 201.28] What do you mean when you say serverless?
[201.28 → 206.60] Because serverless is one of those terms that nobody has really pinned down exactly what
[206.60 → 207.20] it defines.
[208.08 → 216.42] Our working definition is this idea that when you need capacity, when you need servers to
[216.42 → 221.54] handle your requests, when you're in periods of spikes, in surges of use, you have more
[221.54 → 221.90] servers.
[222.10 → 224.52] When you have less use, you have fewer servers.
[224.68 → 226.70] And when you have no use, you have zero servers.
[226.70 → 231.84] And the idea of this is to make it so that you as an engineering team and as a product
[231.84 → 234.52] don't need to think about your compute as a fixed cost.
[234.72 → 238.24] It allows you to essentially view it as pretty much per request phase.
[238.40 → 243.20] You go, funny enough, serverless really does mean servers running under the hood.
[243.42 → 246.14] But the less is that you just don't need to think about it.
[246.18 → 247.08] You think about it less.
[247.50 → 251.98] I'm happy to dive into what the details of that mean in regard to GPUs.
[251.98 → 256.78] But serverless has been around for about 10, 15 years.
[257.28 → 263.38] I don't know my exact timelines, but it's been a concept within CPU-based compute, serving
[263.38 → 265.10] things like websites, backends.
[265.74 → 270.96] And people have been wanting this to exist for GPUs for a long time, and nobody's really
[270.96 → 271.54] cracked it.
[272.04 → 274.10] And that's the challenge we've been working on.
[274.10 → 280.62] I know that you talked about websites, about backends, that sort of thing.
[281.06 → 287.10] Just in general, when we're talking about serverless GPUs, in your mind, is the use case that you
[287.10 → 295.66] have mostly on the inference side or on the training side of what practitioners are doing?
[295.90 → 297.14] Or is there a little bit of both?
[297.32 → 300.76] The vast majority, at least from what we've seen, is on inference.
[300.76 → 304.28] And I think inference is where the value of serverless comes in the most.
[304.78 → 309.20] There are other tools for training where it's not as latency constrained, where you could
[309.20 → 311.78] use other infrastructure orchestration tools.
[312.64 → 318.74] But for specifically inference, serverless is one of the keys to the kingdom, if you could
[318.74 → 320.04] really do serverless well.
[320.50 → 324.84] So we just as a team have chosen to focus mainly on inference, real-time inference.
[324.84 → 330.76] So if there's a user at the other end waiting for a response, we're the ones responsible
[330.76 → 332.30] for making that response happen quickly.
[332.92 → 333.02] Gotcha.
[333.26 → 339.74] And why has it taken so long to get to serverless GPUs versus serverless CPUs?
[340.28 → 345.04] One of the biggest problems in serverless is what's called the cold boot time.
[345.72 → 348.58] Cold boot, as in you don't have servers running.
[348.82 → 349.90] A request comes in.
[349.90 → 355.60] That request coming in triggers a server scale up going from zero to one and then one to many.
[356.52 → 362.82] And the time it takes in order to get resources provisioned and ready to handle requests in
[362.82 → 368.48] CPUs can take a couple seconds on a platform like AWS Lambda.
[368.78 → 371.18] It could take multiple seconds, maybe 10 seconds for a cold boot.
[371.18 → 377.50] And that's just simply spinning up the environment, spinning up a container or a micro VM, whatever
[377.50 → 383.94] they're running, and getting an HTTP server ready to handle that particular call or set of calls
[383.94 → 386.46] for the user before then shutting down.
[386.82 → 392.46] So cold boot has been a big blocker, and it's primarily the initialization time of the application
[392.46 → 394.20] before handling jobs.
[394.72 → 398.80] On GPUs and machine learning, exponentially harder.
[398.80 → 401.68] Reason being, we're running 20 gigabyte models.
[402.14 → 408.20] Those models can't be taking up RAM before a call comes in because that is not serverless.
[408.28 → 410.30] Then you're just running and always on replica.
[411.12 → 416.64] So the cold boot problem is deeply exaggerated when you get to GPUs because not only do you
[416.64 → 422.20] need to provision the GPUs and the environment or the container, you need to load that model
[422.20 → 425.42] from disk onto CPU, onto GPU.
[425.42 → 427.92] That process could take 10 minutes for some models.
[428.64 → 432.70] And it's just been a pretty huge blocker for most GPU use cases.
[433.26 → 436.86] So for that reason, this product hasn't existed before.
[437.30 → 440.28] Definitely not trying to delve into the secret sauce, if you will.
[440.68 → 445.38] But can you kind of lay the landscape of how you even start to think about that problem?
[445.74 → 451.70] Like what are some of the different ways that you might address and maybe different orgs,
[451.70 → 455.50] you know, as you develop competition over time, probably different people will take different
[455.50 → 455.84] approaches.
[455.96 → 458.22] Like how do you even think about that landscape?
[458.22 → 460.62] Because that seems like a daunting task.
[460.62 → 465.08] You know, when you talk about 10 minutes to get it moved over and stuff, that's huge.
[465.08 → 467.88] Like how do you even start to approach the problem?
[467.88 → 473.58] So this is definitely one of our most prized pieces of IP, our cold boot tech.
[473.70 → 475.84] So can't dive too deep into the details.
[476.06 → 476.54] No worries.
[476.74 → 477.44] Whatever works.
[477.60 → 478.74] What is publicly known?
[479.30 → 482.86] You got to think about getting, well, firstly, constraint.
[483.34 → 485.58] Constraint, you cannot take up GPU RAM.
[485.58 → 491.82] If you have a 40 gigabyte A100 machine, if you put a model into that RAM, that portion
[491.82 → 497.44] of the RAM or like that machine entirely, if you're not virtualizing it, it's just like
[497.44 → 498.54] it's taken.
[498.94 → 500.00] You are paying for it.
[500.08 → 500.76] It is dead space.
[500.90 → 506.00] If you're not using it, that's massive GPU burn without any utilization.
[507.12 → 510.28] So constraint model can't sit in RAM.
[510.42 → 510.84] Okay.
[510.98 → 512.02] At least GPU RAM.
[512.02 → 516.92] Um, so when we go about the cold boot problem, what we're really thinking about is how do
[516.92 → 521.28] we get the model specifically the weights as close to RAM as possible without actually
[521.28 → 527.98] occupying resources or, you know, more precious compute resources like 40 gigs of limited RAM.
[528.24 → 528.94] That's hard.
[529.40 → 534.52] But if you have a terabyte of storage on the machine, uh, you could at least have local
[534.52 → 535.74] caching the model.
[535.84 → 541.90] So like you could take that up passively between calls without incurring, you know, sacrificing
[541.90 → 545.64] that piece of hardware because you could fit so many more models onto the disc.
[545.76 → 546.12] Gotcha.
[546.18 → 548.84] And then you could start thinking about like, you know, how do you start pre-caching this
[548.84 → 549.46] on the CPU?
[549.62 → 555.00] If the CPU has enough RAM, um, not saying that's something we do, but these are like the framework
[555.00 → 558.94] in which you would start thinking about it is how do we get that RAM is, or that model
[558.94 → 561.78] is close to GPU RAM without actually taking up GPU RAM.
[561.78 → 566.00] Because in the end, GPU RAM is, that's where the cost goes.
[566.30 → 569.56] Because once you use that, that machine is tied up, and it's not usable for anything else.
[570.34 → 575.56] In your experience, I mean, I know you've been likely talking to tons of different clients,
[575.70 → 581.58] different use cases, like that are really kind of thinking about how, how their workflows
[581.58 → 583.40] could adapt to the serverless workflow.
[583.56 → 585.16] I'm just thinking about my own workflows.
[585.16 → 591.32] Like we're running a lot of models, but none of our models on my team are like receiving
[591.32 → 596.16] thousands of inferences per second or something like that.
[596.22 → 602.34] Like it is very much like in this zone where we kind of get a burst of activity and then
[602.34 → 606.72] we're kind of down, you know, for a bit, not getting that much.
[606.72 → 609.98] And then maybe another burst, uh, that we need to process.
[609.98 → 616.98] Um, so in that case, like I would probably be willing in my own use cases to put up with
[616.98 → 624.38] somewhat like longer of a cold start, like response for the model when it comes up and
[624.38 → 627.78] then subsequent ones during that burst being much faster.
[628.08 → 630.04] What have you noticed with clients?
[630.04 → 631.86] Like what is the tolerance there?
[631.94 → 638.04] Like where are you trying to get, and where do you think is like reasonable for most workflows?
[638.04 → 644.70] I guess I don't have a perfect answer for you on this in that ideally cold boots are zero.
[645.34 → 646.66] Yes, that, that, that's true.
[646.72 → 651.68] I guess, um, I'm banana on a serverless platform in general.
[652.08 → 655.92] Unfortunately, you do have to start thinking about the servers because you want to avoid
[655.92 → 659.48] cold boots when avoidable in the case of banana.
[659.74 → 662.78] If you have a model, uh, it's undergone a cold boot.
[663.10 → 664.60] It's handled the first call.
[664.66 → 665.32] It's ready to go.
[665.32 → 670.60] We have it configured to hang around for 10 seconds, just in case more calls come in.
[671.22 → 674.40] And that 10 seconds is completely configurable by the user.
[675.02 → 677.44] So if no calls come in, we consider it.
[677.60 → 677.74] Okay.
[677.74 → 678.78] We've gone through the surge.
[678.86 → 682.18] We could scale down that particular replica scales itself down.
[682.58 → 685.72] If calls start coming in again, cold boots are incurred again.
[686.38 → 691.44] Um, only if the existing replication you have can't handle that throughput and start scaling
[691.44 → 691.82] up more.
[691.82 → 699.40] So because we give users the ability to like fine tune their autoscale in a sense or fine
[699.40 → 700.76] tune, maybe configure.
[701.40 → 701.88] Yeah.
[701.96 → 704.08] Configure you can configure the autoscale.
[704.24 → 709.34] Um, so we have some users who choose to run always on replicas with a minimum replica
[709.34 → 709.66] count.
[709.66 → 715.64] So at any given time, maybe you have a baseline of two GPUs running, but you can surge to 20
[715.64 → 716.72] if you need.
[717.38 → 718.88] Um, so we have some users doing that.
[718.96 → 723.72] We have some users who have gone away from the default 10 seconds, uh, idle time to go
[723.72 → 724.08] longer.
[724.08 → 729.80] Because they know like they would rather pay you for those GPUs to be up and handle any traffic
[729.80 → 730.52] that may come in.
[730.52 → 733.26] Then have more frequent cold boots.
[733.82 → 737.06] Reason I give that context about bananas.
[737.06 → 744.48] I've been really surprised by how few users increase their idle time right now, or at least
[744.48 → 748.56] the majority of the customers we're serving are more price sensitive than latency sensitive.
[748.72 → 753.60] At least given the general trade-off we give them, um, in that they could configure the idle
[753.60 → 757.42] timeout and through that tune, how much they pay versus how much they wait.
[757.92 → 762.82] But most users would rather have machines shut down and then incur that cold start time.
[763.04 → 768.20] And that's a great thing for us because that allows us to chip away at this cold start problem
[768.20 → 773.96] and give users an exclusively better experience of the faster your cold starts are, the more
[773.96 → 778.46] willing users are to take those cold starts because it's less impactful on their inferences.
[778.46 → 784.66] Um, and the less idle time you could run on your GPUs following calls before they start
[784.66 → 785.24] shutting down.
[785.24 → 786.80] Because it's not as risky, you know?
[804.62 → 805.70] Hello friends.
[805.70 → 811.12] This is Jared here to tell you about changelog plus over the years.
[811.12 → 817.10] Many of our most diehard listeners have asked us for ways they can support our work here at
[817.10 → 817.54] changelog.
[817.68 → 823.68] We didn't have an answer for them for a long time, but finally we created changelog plus
[823.68 → 824.66] a membership.
[824.66 → 828.76] You can join to directly support our work as a thank-you.
[828.88 → 835.62] We save you some time with an ad free feed, sprinkle in bonuses like extended episodes and
[835.62 → 838.58] give you first access to the new stuff we dream up.
[839.04 → 842.46] Learn all about it at changelog.com slash plus.
[842.66 → 845.98] You'll also find the link in your chapter data and show notes.
[846.40 → 849.64] Once again, that's changelog.com slash plus.
[849.82 → 850.48] Check it out.
[850.84 → 851.88] We'd love to have you with us.
[851.88 → 866.28] So as you were kind of describing that, that was really, it's a very interesting mesh of
[866.28 → 866.72] skills.
[866.72 → 868.68] It seems to do what you're doing there.
[868.68 → 874.00] Because you obviously have to have a pretty good understanding of deep learning in general
[874.00 → 878.34] and kind of the AI space and the performance characteristics around that.
[878.34 → 885.80] But you also have to go very, very deep in terms of network engineering and architectural
[885.80 → 888.34] considerations and such like that.
[888.34 → 891.74] It also kind of brings different cultures together.
[891.74 → 899.68] For instance, in terms of like the choices of languages and stuff distinctly, like do you tend
[899.68 → 904.32] to go with one language for everything for simplicity’s sake?
[904.42 → 909.04] Or do you tend to go with different languages that are catered towards specific use cases?
[909.38 → 916.08] By way of example, like Python for deep learning specific things and like Rust, you know,
[916.12 → 918.90] or something C plus for infrastructure thing.
[918.90 → 921.96] How do you, or do you stick with one like Python for everything?
[921.96 → 924.24] Because that way you have a simpler setup to govern.
[924.38 → 925.96] How do you take that strategy wise?
[926.40 → 931.04] So the obvious language for hosting ML model inference is Python.
[931.22 → 934.60] It's almost a requisite as in all of our users are running in it.
[935.08 → 940.20] So the framework that we give users to build on, which is essentially boilerplate
[940.20 → 942.90] for a server that's written in Python.
[943.32 → 945.72] We don't need to maintain that too much.
[945.80 → 947.70] It's an extremely simple HTTP wrapper.
[947.70 → 953.22] And the vast majority of our work on the pipeline infrastructure side is all done in Go.
[953.56 → 956.50] So we're probably 95% Go.
[956.86 → 960.96] We have some TypeScript for our web app, some Next.js that we're running.
[961.74 → 968.90] And then when you get deep into like the runtime, we work on C plus and CUBA as well.
[969.34 → 973.02] But that's a small subset of our engineering team works at that level.
[973.16 → 976.92] The majority of us write pipelines and networks within Go.
[976.92 → 978.98] I got to say, it's kind of funny that you bring that up.
[979.04 → 980.00] Daniel and I love Go.
[980.18 → 983.42] We actually met in the Go community because we're both GoPro.
[983.56 → 987.54] We were like at the time kind of the two AI oriented people in the Go community.
[987.72 → 990.98] So it's just a little bit ironic to hear that.
[991.50 → 991.92] That's awesome.
[991.92 → 995.54] I've been so disappointed in Python.
[995.72 → 997.16] I mean, Python's amazing language.
[997.46 → 1001.58] It's where I learned my first bit of serious general purpose programming was Python.
[1002.62 → 1013.10] But I'm saddened to know that the language we chose for GPU programming, basically, is a language that like has a global interpreter lock.
[1013.10 → 1017.28] It does not have great multiprocessing built in.
[1017.84 → 1019.26] I wish Go were the choice there.
[1020.14 → 1022.38] It doesn't seem like it's going to happen, but I'm a huge fan of Go.
[1022.56 → 1024.18] I think it's a great language to write in.
[1024.90 → 1027.30] And I could go on for a long time about this.
[1027.40 → 1032.28] In fact, one of the reasons I learned about the changelog network was listening to the Go Time podcast.
[1033.00 → 1034.12] Yeah, for sure.
[1034.28 → 1034.74] Shout out.
[1036.04 → 1037.52] Shout out to that other podcast.
[1037.70 → 1038.54] Yeah, definitely.
[1038.54 → 1038.66] Definitely.
[1039.70 → 1047.82] It's cool to hear about, I guess, the setup of how you thought about this problem and how you even structured the team and that sort of thing.
[1047.94 → 1060.56] I'm wondering at this point if you could kind of just give us a sense for like if I'm a data scientist or even just a software engineer trying to integrate a model into my stack,
[1060.96 → 1065.74] what does the workflow as of now look like for me with Banana?
[1065.74 → 1069.10] What do I do to get a model up and going?
[1069.64 → 1073.02] And maybe just a couple examples of that to give people a sense.
[1073.12 → 1077.28] It's a bit hard on an audio podcast, but I'm sure you've done similar things in the past.
[1077.70 → 1078.12] Yeah.
[1078.40 → 1084.02] Well, I'd love to give a visual demo, but going through audio-wise, generally the process looks like this.
[1084.02 → 1087.66] A lot of people are building off of standard models.
[1088.24 → 1096.24] So say a Stable Diffusion or a whisper, at least for like this current, this hype wave of all these new, exciting open source models coming out.
[1096.78 → 1097.44] Until next week.
[1097.72 → 1098.42] Yeah, until next week.
[1098.44 → 1099.60] And then the next one comes out.
[1100.00 → 1104.40] Thankfully, we have these one-click templates that you could use on Banana.
[1104.40 → 1113.54] So in a single click, you could go from an open source model that somebody has published on Banana and bring that into your own account and start using it yourself.
[1113.74 → 1119.36] So within a few seconds, you could have a functioning endpoint for popular models that have been put up by the community.
[1119.36 → 1127.28] And then we see naturally the step beyond that, moving from you effectively have an API, you don't really know what's running behind the scenes.
[1128.40 → 1134.52] You could fork that code, you start working on it yourself and customizing it for your own use case.
[1135.12 → 1146.22] So if you're doing some fine-tuning, if quite honestly, you want to go away from the standard or like the big model templates and roll it yourself, just have whatever deep net that you've built.
[1146.22 → 1151.28] That's where you start getting into sort of the local dev iteration cycle.
[1151.60 → 1155.86] And this is where I shout out a previous guest, Bred Nader over there at Bred.
[1156.92 → 1168.54] We recommend users go and have an interactive GPU environment so that you could load your model, test it against some inference payload, shut it down, iterate.
[1168.54 → 1175.16] If you're doing something like a Stable Diffusion, you want to make sure that the image transformations server side are happening correctly.
[1175.16 → 1176.16] That's where you iterate.
[1176.16 → 1177.16] That's where you iterate.
[1177.16 → 1180.16] You're doing all of this within the banana framework.
[1180.16 → 1182.16] We have an HTTP framework.
[1182.16 → 1184.16] You could find open source online.
[1184.16 → 1187.16] That's generally the building point for most users.
[1187.16 → 1189.16] So you're modifying a function within that.
[1189.16 → 1194.16] That is the inference function, takes in some JSON, runs the model, returns some JSON.
[1194.16 → 1201.16] Do that iteratively until you have your customized model that works to the API you're hoping for.
[1201.16 → 1203.16] And then you push that to GitHub.
[1203.16 → 1205.16] And then from there, you could go into banana.
[1205.16 → 1209.16] You could select that repo, and we have a CI pipeline built in.
[1209.16 → 1213.16] So when you select that repo, we build the model, we deploy it.
[1213.16 → 1216.16] Every time you push to main, we rebuild and redeploy.
[1216.16 → 1226.16] So we generally recommend users to, if they're shipping new fine-tuned versions, it's usually them updating, say, a link to an S3.
[1226.16 → 1232.16] Then in the build pipeline, we bundle that model into the container itself and get that deployed to the GPUs.
[1232.16 → 1237.16] So kind of curious, and this is sort of a follow-up, largely because of the medium we're in.
[1237.16 → 1243.16] Since we're audio only, and we don't have the ability to show the process that you're describing.
[1243.16 → 1252.16] Just for clarity, like your typical customer slash user, what skills would they typically have to productively use banana?
[1252.16 → 1260.16] You know, what are those necessary minimum skills for them to be able to really engage productively and move through things?
[1260.16 → 1268.16] A lot of our users are quite surprisingly full stack engineers and not deep experience data people and ML people.
[1268.16 → 1280.16] So as long as you can wrap your head around using frameworks or abstractions like hugging face, for example, if you could use a pipeline like that, pull it locally, that's something you could deploy into banana.
[1280.16 → 1285.16] So some Python expertise in order to write the code in the first place, it's an HTTP server.
[1285.16 → 1289.16] So you write that you wrap it around, say, a hugging face model.
[1289.16 → 1290.16] You don't need to fine tune it.
[1290.16 → 1293.16] You could use the standard models and then learn fine-tuning later.
[1293.16 → 1296.16] And ideally, you do have some knowledge of Docker.
[1296.16 → 1299.16] Ultimately, what is deployed to banana is a Docker file.
[1299.16 → 1305.16] If you build within our template, generally, you don't need to do things that are too custom unless you choose to.
[1305.16 → 1307.16] But a little bit of knowledge of Docker helps.
[1307.16 → 1314.16] So Python, hugging face Docker, that's effectively all you need in order to get something deployed onto banana.
[1314.16 → 1320.16] I'm just on the site now and kind of looking through some of your community templates, which are pretty cool.
[1320.16 → 1331.16] I mean, you have all sorts of things, Cohen, T5, Santa Coder, all sorts of things with a sort of one click deploy button to get them up and going.
[1331.16 → 1343.16] One question I had, just like when I deploy, because it looks like based on your docs, I can call it with like the model ID from Python, for example.
[1343.16 → 1346.16] So I could like to integrate this directly in a Python app.
[1346.16 → 1351.16] Can I also call it sort of like as a REST endpoint or something like that?
[1351.16 → 1354.16] Or is the primary use case a client integration?
[1354.16 → 1357.16] We do have public documentation for the REST endpoint.
[1357.16 → 1358.16] So awesome.
[1358.16 → 1360.16] It's not officially supported.
[1360.16 → 1368.16] We try to encourage people to go through our official SDKs, which at this point are Python TypeScript go in Rust.
[1368.16 → 1374.16] That said, anyone who wants to go directly into the REST endpoint, there's documentation to do so.
[1374.16 → 1385.16] We like being able to boil it down to a simple banana. Run function where you just give a model key, you give whatever JSON in you want your server to process, and then you receive the JSON out from that.
[1385.16 → 1391.16] But our goal is to be able to give people access to the levels of extraction that they choose to run in.
[1391.16 → 1399.16] For example, because we have a public REST endpoint, people have integrated banana into their Swift applications or into their Ruby applications.
[1399.16 → 1402.16] So it's an HTTP call in the end.
[1402.16 → 1406.16] People could unwrap our APIs and go at it directly.
[1406.16 → 1407.16] Feel free.
[1407.16 → 1419.16] Yeah, I guess that leads right into my next question, which is, does anything stand out in terms of like how people are using this serverless workflow that maybe surprised you based on what you're seeing?
[1419.16 → 1423.16] I've been amazed at the quantity of fine-tunes that are deployed through banana.
[1423.16 → 1433.16] If you look at the analytics of people deploying from our one click templates versus people deploying from custom repos, 80% are custom repos.
[1433.16 → 1447.16] And that means that people are coming to serverless because they have a unique API that they need to run somewhere and that they can't simply run with a standard API provider or even an API provider with fine-tuning features.
[1447.16 → 1456.16] Like they want to go to own the API themselves, own the application logic themselves, the fine tune themselves, and just Voucherize that up and send it on to banana.
[1456.16 → 1463.16] So the vast majority of our users are doing custom workloads, which to me was surprisingly little banana lore.
[1463.16 → 1470.16] We previously started as an ML as an API company, the idea of showing up, click the model you want, and you get an API for that.
[1470.16 → 1474.16] And there's a lot of pull there, especially right now with the hype.
[1474.16 → 1480.16] There's so many people who want to integrate AI into their applications without touching the AI at all.
[1480.16 → 1485.16] So it has been surprising for us seeing how many people are running custom code on us.
[1485.16 → 1490.16] And it's been validating of the idea that the platform approach versus the API approach has been the way to go.
[1490.16 → 1504.60] Could you kind of walk us through what a typical one might look like, you know, where someone's doing that kind of custom thing, just to give us a sense of what it is that you're seeing, whether it's, you know, fictional, but realistic, or a real case example, whatever works for you.
[1504.60 → 1520.60] So one thing users are doing just as a very basic example of if latency is an extremely sensitive thing for them and cold boots are particularly painful, what they'll do is they'll engineer a conditional, like a Boolean in the JSON that they send in.
[1520.60 → 1521.60] That's called the warm-up.
[1521.60 → 1527.60] So they'll do like warm-up equals true and make it so that server side, they actually don't perform any heavy computation.
[1527.60 → 1529.60] It's just intended as a warm-up call.
[1529.60 → 1540.60] So if architecturally they need servers running, like fully warmed up by the time the actual inference starts running, they engineer this into their endpoint.
[1540.60 → 1552.60] Another thing as well, if people want to run fine-tunes or run multiple models side by side and start doing some model changing, we see people building that into banana as well.
[1552.60 → 1566.60] And then lastly are just basically state-of-the-art moves so fast right now that the second stable to fusion launch, for example, suddenly there's in painting and in painting is the next thing that came out a week later.
[1566.60 → 1570.60] And that's some random code people found in a GitHub, and they integrated themselves.
[1570.60 → 1579.60] So customization on that sense allows users to stay as far ahead as they possibly can if it's necessary for their use case.
[1579.60 → 1591.60] Could you highlight something you have in your mind as maybe as a workflow that would not be appropriate for the sort of serverless GPU infrastructure?
[1591.60 → 1598.60] So I think this like, like you say, fine tune models inferencing, like, you know, using these state-of-the-art templates.
[1598.60 → 1606.60] Is there something where you would say, hey, like maybe that's not fitting for the serverless use case?
[1606.60 → 1620.60] Yeah. So in inference land, if you have completely steady traffic all the time, don't use serverless, you'll get unnecessary cold boots, and it just slows down your inference, and you're paying effectively the same.
[1620.60 → 1624.60] So that's the inference side. Training side.
[1624.60 → 1628.60] We'd like to think that you could currently train on banana, though.
[1628.60 → 1634.60] I often find that training is a more interactive experience or at least in like the initial prototyping phase.
[1634.60 → 1649.60] Once you have pipelines built in to say automatically collect data and batch train, that actually does work on banana because you could just fire that data as the payload, train the model server side, upload it to S3, return the call and then the replica shuts down.
[1649.60 → 1665.60] But most training jobs or most like exploratory training jobs, I would not recommend doing on serverless in part just due to the like the observability that you need to see the tracing setting up things like this is outdated tech, but tensor board.
[1665.60 → 1670.60] There's more visualization tools. Also, keep in mind, I'm not a training expert.
[1670.60 → 1678.60] So perhaps there's space in the training that people would see value in serverless, but generally I'd recommend avoiding serverless.
[1678.60 → 1687.60] And then lastly, if you have any jobs that are batched, as in, you know exactly when they're going to happen.
[1687.60 → 1692.60] It's a bit easier to automate your own infrastructure and build it yourself to do that.
[1692.60 → 1695.60] Ideally, we make serverless so good that you don't need to think about that.
[1695.60 → 1706.60] But I think in the current state of serverless, a lot of batch processing jobs, if you're say running an indexer across an internal database, and you don't need to have it running all the time.
[1706.60 → 1713.60] That's where running a serverless may be a bit too much lift in order to port it into serverless versus just doing it yourself.
[1713.60 → 1727.60] I was looking, I'm also looking through your website while we're talking, and I'm in the docs and I kind of hit the SDK area, which you kind of talked about a little bit ago with the different SDKs and Python, Node, Go, REST.
[1727.60 → 1733.28] Did you mention Rust earlier or did I mishear that as Rust? I may have misheard something.
[1733.86 → 1738.50] I did mention Rust. I actually don't know if we have it documented. We launched it two days ago, if I recall.
[1738.86 → 1745.88] Gotcha. So the thing that got me thinking here, that's very leading edge. It's very like out there.
[1745.88 → 1754.94] I'm kind of getting the sense that your customers are adopting more forward-leaning languages in general for what they're doing.
[1755.76 → 1761.22] And that's why they're leaning forward into this new concept of serverless GPUs.
[1761.72 → 1764.42] Is that consistent with what you're seeing?
[1764.42 → 1781.84] Are you really kind of targeting the types of software developers that are kind of early adopters, paving the way versus somebody that's maybe in some of the older, more enterprise-y languages, maybe not quite as risk-taking and such?
[1782.42 → 1784.36] That's very much in line with what we've been seeing.
[1784.76 → 1789.36] We find that a lot of our users are adamant for cell users, as an example.
[1789.36 → 1795.16] So they're in Next.js. They've chosen a relatively modern framework to build their front-end apps in.
[1795.88 → 1798.06] And they make the same decisions for their back-end.
[1798.28 → 1799.54] They're often TypeScript forward.
[1800.04 → 1802.46] If they want to do systems level, they'll do Rust or Go.
[1803.10 → 1807.22] For these reasons, we've chosen to offer these official SDKs.
[1807.80 → 1809.24] Yeah, that's fascinating.
[1810.34 → 1815.08] One of my questions in kind of thinking about this is like the different use cases that you could have,
[1815.08 → 1820.58] the different industries that are rapidly adopting AI, integrating it in their software stacks.
[1820.76 → 1822.72] Like everybody's adopting AI, right?
[1823.10 → 1826.78] But like it's certainly making a lot of strides in certain areas.
[1827.02 → 1844.14] And certain industries like, you know, let's say healthcare or something like that have unique constraints around even like their own inference data leaving to go like to some hosted model somewhere that's not in their own infrastructure.
[1844.14 → 1852.10] But in other words, when I go to Banana, I see like all I have to care about is like deploying a model.
[1852.48 → 1854.30] There's my model ID, right?
[1854.36 → 1856.94] I can think about like the timeout and all of that.
[1857.06 → 1858.48] It's all very functional, right?
[1858.52 → 1862.02] And I don't even have to like to give a thought for where that's running.
[1862.24 → 1867.94] I could see like the opposite end of that is like certain industries would probably be a little bit uncomfortable with that.
[1867.94 → 1878.80] But there's a lot of developers that are just wanting to like, you know, bootstrap these like amazing AI powered things like very rapidly.
[1878.80 → 1881.52] There are so many things coming to market like that.
[1882.00 → 1884.78] So I guess that would be fitting in that way.
[1884.86 → 1896.84] Do you have any plans in the future for like Banana serverless, but like connect my AWS infrastructure or something like that to run in the Banana way or something like that?
[1896.84 → 1898.68] Short answer, yes.
[1899.42 → 1900.10] Long answer.
[1900.46 → 1901.08] It's complicated.
[1901.20 → 1902.20] It's going to be a long time.
[1902.42 → 1903.80] Yeah, it's very complicated.
[1904.18 → 1919.88] And one of the things that we see with serverless is the fact that we have economies of scale sharing everyone as tenants within our cloud, because that allows us to do more efficient bin packing and make it so that when you're not using a server, like when the server container is shut down, you're not charged.
[1919.88 → 1923.28] If you're running on your own cloud, you still need to have the underlying resources running.
[1924.30 → 1925.42] We're a venture skilled business.
[1926.24 → 1933.00] We want to hit that million dollar annual revenue, ideally, or sorry, not a million dollar, a hundred million dollar annual revenue, ideally more.
[1934.14 → 1939.68] And I think getting into that, we're eventually going to have to start thinking about how do more traditional enterprises integrate this.
[1939.68 → 1952.02] Though choosing our niche right now, we see significant pull that could get us to one $10 million annual just from these new teams who aren't bound by such constraints of needing to run in their own cloud.
[1952.28 → 1954.68] So long answer, restated.
[1954.90 → 1956.04] We'll get to it eventually.
[1956.78 → 1961.98] And I'm sure it's like it will be a necessary part of the product, but it loses out on a lot of the magic that we're currently providing.
[1962.32 → 1966.96] So we'd rather just focus on these new and upcoming startups that are running on us.
[1966.96 → 1969.40] Yeah, that makes a lot of sense, I think.
[1970.22 → 1977.26] It does make me wonder, like, because you are creating so much magic for the users.
[1977.72 → 1983.14] And a lot of that, like you're saying, like thinking about like what GPUs are you spinning up?
[1983.28 → 1985.18] Like, how are you bidding on these?
[1985.28 → 1987.96] Like, where are you like, how are you allocating them?
[1988.36 → 1994.42] Have you learned any sort of like general like you can get GPUs from a lot of places.
[1994.42 → 1997.58] There's a lot of different kinds of scales of pricing.
[1998.34 → 2002.00] There are a lot of different ways to run GPUs in the cloud.
[2002.64 → 2017.18] Have you found any just sort of like good practices or things that you found to be useful just generally in terms of thinking about like using GPUs in the cloud that you'd love to pass on to listeners?
[2017.18 → 2021.32] So we use this phrase called skate ahead of the puck.
[2022.00 → 2025.74] It's a phrase from hockey where don't go to where the puck is, go to where it's going.
[2026.76 → 2028.98] So applying that to auto-scaling.
[2029.28 → 2032.62] Auto scaling really has two components.
[2033.02 → 2037.18] You're auto-scaling the underlying nodes, the hardware that's running the GPUs.
[2037.18 → 2041.90] Like that's running the Kubernetes cluster, whatever your deployment target is.
[2042.64 → 2053.20] And then secondly, you're auto-scaling the deployments themselves going from replication of zero to one to many within the confines of whatever nodes you have set up.
[2053.44 → 2058.32] So you're effectively auto-scaling two things, Kubernetes pods and the nodes themselves.
[2058.32 → 2069.32] So my recommendation are if people are building things like this in-house, what they should absolutely do is use a platform that has an automation API for the underlying VMs.
[2069.32 → 2072.58] Right now, GPU cloud is sort of the wild west.
[2072.70 → 2079.50] There are a lot of new players, traditional hyperscaler clouds like Google Cloud, AWS, Azure.
[2079.96 → 2085.78] They have the automation, but the GPU prices are not as competitive as you could get on some of these newer clouds.
[2085.78 → 2103.34] So my biggest recommendation for people building mature systems would be to choose a provider that you get ideally guaranteed access to GPUs, which allows you to scale your GPUs up ahead of the demand of whatever workloads you're running within your cluster.
[2103.98 → 2107.26] And then it doesn't have to be homogenous, the workloads deployed.
[2107.86 → 2112.86] Just as long as you maintain GPU capacity to handle those, you should be good.
[2112.86 → 2122.28] But because you're auto-scaling, like the applications within Kubernetes, it allows you to have a little more lead time for like super slow scale ups on the GPUs.
[2122.52 → 2125.50] This has been a super instructive conversation.
[2125.70 → 2126.82] I'm learning a lot.
[2127.02 → 2135.58] I want to extend your analogy one question further because you're talking about skating ahead of the puck, not skating to the puck, but where it's going to go.
[2135.58 → 2138.58] So you are pioneering this field.
[2138.76 → 2140.24] You are out there on the front.
[2140.46 → 2146.68] You are leaning forward, and you are supporting other people in other organizations that are trying to lean forward as well.
[2146.88 → 2149.90] So I'm going to ask you, where is the puck going?
[2150.12 → 2152.80] You know, short term, middle, middle, long term.
[2152.96 → 2159.24] How do you see the future for those who are not in your industry but are going to be supported by you?
[2159.62 → 2160.66] Tell us the vision.
[2160.80 → 2161.52] What's it going to?
[2162.22 → 2163.52] Fine-tunes are going to be huge.
[2163.52 → 2167.14] I think there are two camps for where AI is going to be going.
[2167.42 → 2173.16] There's the one model to rule them all camp, which is there's going to be some mega model that does everything.
[2173.70 → 2183.20] And then there's the other camp, which is what we're leaning into, which is the best model for you as a user is a model that's trained on data from you, specifically you.
[2183.56 → 2189.42] And we see customers deploying fine-tunes on us, not just for their use case, but for their end user.
[2189.42 → 2193.52] Imagine you are building a writing assistant app.
[2193.88 → 2200.96] How do you fine tune for every single one of your end users and deploy that and make it so that that user has a unique model?
[2201.16 → 2204.68] It's essentially a companion, almost a clone of them.
[2204.68 → 2213.10] And where the puck is going is where we, every human on Earth, just like they have a phone in their pocket, they're going to have a fleet of models fine-tuned just on them.
[2213.92 → 2218.98] And that's one thing we're excited about with serverless is in order to do that viably, you got to have serverless.
[2219.46 → 2220.54] Can't have it running all the time.
[2220.66 → 2222.38] So very excited in this sense.
[2222.38 → 2232.82] If you're not looking into user level fine-tunes, I think it's a very interesting space to be in because it gets you so much further than any application level stuff you could do to make the experience better.
[2233.56 → 2233.96] That's awesome.
[2234.18 → 2237.58] Yeah, I think that's a super exciting way to close out the conversation.
[2238.32 → 2249.38] This is a really exciting time to be in this space, both in terms of what's possible with fine-tuning and those sorts of technologies, but also like new infrastructure coming up, like what you're building.
[2249.38 → 2253.28] So thanks much for taking time to chat with us, Eric.
[2253.34 → 2254.24] It's been a real pleasure.
[2255.08 → 2255.66] This is awesome.
[2255.98 → 2256.64] Appreciate it, guys.
[2265.64 → 2268.14] Thank you for listening to Practical AI.
[2268.64 → 2272.48] Your next step is to subscribe now, if you haven't already.
[2272.92 → 2278.94] And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2279.38 → 2284.34] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2284.92 → 2288.70] Check out what they're up to at Fastly.com and Fly.io.
[2289.10 → 2294.42] And to our Beat Freakin' Residence, Break master Cylinder, for continuously cranking out the best beats in the biz.
[2294.72 → 2295.60] That's all for now.
[2295.92 → 2297.02] We'll talk to you again next time.
[2297.02 → 2298.02] Bye.
[2298.02 → 2298.52] Bye.
[2298.52 → 2299.02] Bye.
[2299.02 → 2299.52] Bye.
[2299.52 → 2300.02] Bye.
[2300.02 → 2300.08] Bye.
[2300.08 → 2300.52] Bye.
[2300.52 → 2301.08] Bye.
[2301.08 → 2301.52] Bye.
[2301.52 → 2301.58] Bye.
[2301.58 → 2301.64] Bye.
[2301.64 → 2301.70] Bye.
[2301.70 → 2302.14] Bye.
[2302.14 → 2302.64] Bye.
[2302.64 → 2303.64] Bye.
[2303.64 → 2303.70] Bye.
[2309.38 → 2309.94] Bye.
[2310.68 → 2311.02] Bye.
[2335.42 → 2337.02] Bye.
[2337.02 → 2337.58] Bye.
[2337.58 → 2337.64] Bye.
[2337.64 → 2338.22] Bye.
