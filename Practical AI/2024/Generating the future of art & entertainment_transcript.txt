[0.00 --> 8.66]  Welcome to Practical AI.
[9.34 --> 19.54]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 32.36]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.62 --> 46.12]  Welcome to another episode of the Practical AI podcast.
[46.54 --> 48.64]  I am your co-host, Chris Benson.
[49.16 --> 52.98]  Usually I have our other co-host, Daniel Whitenack, with us.
[53.04 --> 54.38]  He is not able to join today.
[54.38 --> 56.54]  But we have a great show in store.
[56.74 --> 59.64]  We have with us a super interesting guest.
[60.04 --> 66.24]  You may very well, if you follow AI, have heard about this guest and this company doing some super cool stuff.
[66.46 --> 75.86]  So I'd like to introduce Anastasis, sorry, I'm mispronouncing, Germanidis, who is the co-founder and CTO at Runway.
[76.34 --> 78.18]  Sorry I screwed up your name there.
[78.48 --> 80.20]  Did I get it anywhere close to right there?
[80.66 --> 81.68]  Yeah, all good.
[82.12 --> 83.32]  Thanks so much for having me.
[83.32 --> 85.70]  No, sorry for the stutter there.
[85.84 --> 87.34]  Thanks for joining us on the show.
[87.52 --> 90.64]  You guys are doing some really cool stuff at Runway.
[90.98 --> 95.92]  Wanted you to actually, before we dive fully in, kind of tell us a little bit about your own background.
[95.92 --> 107.32]  And then we'll kind of dive into kind of the environment that you find yourself in and the industry and what kinds of problems out there are interesting as we dive in.
[107.48 --> 110.94]  So first of all, you know, CTO of a hot AI company.
[110.94 --> 111.78]  How did you get there?
[111.86 --> 113.54]  How did you get to where you're at right now?
[113.54 --> 118.20]  Well, the first thing I would say is that I did not get here by planning for it.
[118.20 --> 123.04]  I think in some ways is planning against being where I am today.
[123.04 --> 124.56]  So just to give you the background.
[125.18 --> 128.98]  So my background is kind of a hybrid of engineering and art.
[129.14 --> 138.06]  So I was for the past decade or so, I've been kind of in different startups working as an engineer at the same time having my own art practice.
[138.06 --> 143.38]  And so doing kind of a variety of work and kind of media arts and interactive arts.
[143.88 --> 148.46]  Runway was the first time where those two kind of different worlds have converged for me.
[148.64 --> 151.08]  But Runway started in art school.
[151.28 --> 156.24]  So this is not really where companies, AI companies get started usually.
[157.00 --> 167.66]  So my motivation for going to art school was actually to take a break from technology to really explore like the more creative and like in some ways.
[168.06 --> 175.92]  Open and exploration of those technologies without any concern about like making something that would make a commercial sense at some point.
[176.40 --> 182.30]  But it just so happened that, you know, I met my co-founders there and we started kind of making those small tools.
[182.64 --> 184.54]  And like one thing led to another.
[184.84 --> 191.54]  And we realized that this was kind of a really useful thing to build out and kind of spend our focus time on.
[191.54 --> 197.98]  It sounds like it was a bit of a passion project, you know, without that commercial intent up front, you know, in the beginning.
[198.06 --> 200.48]  And you kind of fell into it because it was what you love.
[200.84 --> 200.92]  Yeah.
[201.02 --> 204.74]  And I think that's how the best things get started very usually.
[204.96 --> 212.50]  It's just like and that's been a general pattern, I would say, not just at the start, but just throughout the way we rebuild the company.
[212.90 --> 219.06]  There is this book that we really give to every employee that's called Why Greatness Cannot Be Planned.
[219.06 --> 227.52]  And it just talks about this idea that like when you have very, very concrete goals in mind, it's actually very often you end up not meeting them.
[227.70 --> 235.20]  And sometimes going for like the next stepping stone is the right approach to actually get to very interesting findings or novel insights.
[235.20 --> 240.86]  And so that's been part of how Runway started and that's been part of how Runway had continued to grow.
[241.48 --> 253.88]  But yeah, initially, I would say our main goal was like these machinery models are super difficult to understand, super difficult to use, especially when we started like around five years ago.
[254.22 --> 260.50]  But they're super interesting for artists and they can make really compelling things with it once they get to the point where they can actually use them.
[260.50 --> 271.20]  At that point, generative models, kind of AI was a bit at an earlier stage in terms of both how many people cared about it and also the results of those models.
[271.74 --> 278.22]  But it was still, even at that point, really useful for artists the moment we gave the right tools for them to use it.
[278.32 --> 281.12]  And so that was kind of the inception of Runway.
[281.20 --> 288.96]  I'm curious, recognizing that there wasn't the master plan that you were implementing, there was a bit of serendipity to how you arrived there.
[288.96 --> 295.12]  I am kind of curious, you mentioned that you would kind of set aside technology before you were going back into art right there.
[295.30 --> 306.36]  And I'm kind of curious, did the technologies you were in prior to art school play into where you've come out here with, you know, in terms of Runway being that end result?
[306.60 --> 312.76]  Or did you, you know, is there any connection there or were they just, you happened to be in a different area and were finding AI?
[312.98 --> 315.80]  Were you active in AI prior to going back into art school?
[315.80 --> 320.22]  My interest in AI kind of goes back into like at least high school and before.
[320.80 --> 327.48]  So I've been, before Runway, I was working as a machine learning engineer, as a kind of distributed systems engineer at different companies.
[327.66 --> 331.70]  So definitely had a background in this area, was very interested in AI.
[332.34 --> 338.12]  My interest was specifically in neural networks, which, you know, when I was kind of decades ago,
[338.20 --> 342.22]  they had become kind of like ignored area of machine learning.
[342.22 --> 348.94]  Like they were kind of seen as a dead end, that like they wouldn't be able to, like at that point, like support vector machines around there.
[349.38 --> 350.74]  And the models were more popular.
[351.24 --> 360.98]  But there was still something very compelling about neural networks that made me actually get, kind of start working with them from kind of high school with some initial projects.
[360.98 --> 363.86]  So I've been very interested in AI kind of throughout.
[364.34 --> 370.18]  The motivation for going to art school was, and just to kind of keep more context on the kinds of art school,
[370.38 --> 375.50]  it was, it's a program at NYU that was kind of exploring the intersection of art technology.
[376.20 --> 383.92]  Technology was still part of it, but it was less kind of technology for the sake of technology or for just like novelty for the sake of novelty.
[383.92 --> 392.00]  I think more understanding, like how the technology could be used in creative ways or in ways that are maybe unconventional.
[392.70 --> 398.74]  As you were coming into art school and you have this background as a machine learning engineer and the passion for art,
[399.42 --> 402.98]  what has been, you know, your initial vision for that industry?
[403.18 --> 407.74]  Like within entertainment, human creativity, which are things that you currently are targeting,
[407.74 --> 414.72]  how did you see them and how did you expect to be able to impact the industries with AI going into the process?
[414.84 --> 418.48]  So like things are moving so fast and we're seeing these amazing technologies,
[418.48 --> 421.16]  which we're going to be talking about in the minutes to come.
[421.16 --> 429.48]  But I'm really curious what your perspective was about where this was going for art and entertainment prior to actually arriving there.
[429.48 --> 437.68]  The perspective for us has always been that those models, those techniques are never going to be a source of ideas.
[437.78 --> 441.84]  They're going to be an acceleration and expression of like creators' ideas.
[442.40 --> 446.18]  This is the kind of mindset that we started building those tools around.
[446.66 --> 455.30]  And that's why from the beginning, we started working very closely with filmmakers or with designers or with artists in making those tools and getting their feedback on how to make them.
[455.30 --> 464.10]  The other aspect to, in terms of how we were kind of seeing the trajectory of those models was when we look back at like 2017 or 2018,
[464.38 --> 473.96]  when we just started kind of working on this, the results of those models were, you know, pixelated, low resolution, very experimental, you know, the composition was off.
[474.54 --> 478.72]  But you could see the trend very clearly that, you know, every year the resolution was doubling,
[478.86 --> 481.62]  the fidelity was improving at a fairly predictable way.
[481.62 --> 486.10]  And so it was not a matter of if, it was a matter of when this would arrive.
[486.64 --> 488.34]  Timing those things is always really difficult.
[488.54 --> 497.06]  So we didn't really know like exactly when we're going to get to this like breakthrough where those models really started becoming actually useful.
[497.26 --> 500.80]  But it was, we knew that it was going to happen at some point in the next years.
[501.62 --> 504.20]  Most people who were machine learning engineers,
[504.20 --> 510.04]  and I work with university students a lot and people at the company I'm at now and previous companies.
[510.32 --> 512.40]  And that's kind of their dream job.
[512.40 --> 515.06]  And I find it, it's really interesting to me that you said,
[515.12 --> 519.18]  I'm going to set that aside for a little bit and go and do art school.
[519.54 --> 521.94]  What was the driving factor for you?
[521.98 --> 524.32]  Because obviously that turned out for your story,
[524.32 --> 526.06]  that turned out to be crucial,
[526.20 --> 529.90]  that juxtaposition, if you will, of those different factors.
[529.90 --> 531.94]  I'm just curious, what made you say,
[532.28 --> 536.46]  I think I'm going to put down machine learning engineering for a while and go back to art school.
[536.56 --> 537.84]  I was just curious what that was,
[537.88 --> 542.08]  because obviously that seemed to create a perfect environment for you to spring from.
[542.56 --> 549.58]  I would say mainly just the motivation and the need to explore the possibilities of something
[549.58 --> 559.06]  without a very clear expectation that it needed to result in a tool that was kind of necessarily useful
[559.06 --> 564.98]  or just the being in an environment where it can kind of have this open and exploration
[564.98 --> 567.00]  of the possibilities of this technology.
[567.50 --> 571.26]  It was less that, you know, I wasn't interested in machine learning or I wanted to get away from it.
[571.56 --> 576.72]  It was more, I wanted to explore it in a context where there was no kind of expectation that,
[576.72 --> 581.36]  you know, I needed to build something that was, you know, commercially valuable or like super useful.
[581.36 --> 588.56]  So, of course, that took a turn and I ended up like that was a way to get to something that ended up being very,
[588.86 --> 590.12]  a very good fit for a company.
[590.62 --> 597.96]  But I would say initially it was like, I was very interested in, at some point, I think in 2015, 2016,
[597.96 --> 602.92]  they were just starting to emerge this kind of new movement around making art with AI.
[602.92 --> 607.48]  And there were some initial explorations, a lot of them in kind of the open source world.
[607.90 --> 615.84]  And I just started contributing to making kind of small projects around making kind of tools to make art with AI.
[616.40 --> 622.10]  And so really just wanted to spend more time building those things and less kind of in the,
[622.36 --> 625.04]  kind of purely in the industry, working with machine learning.
[625.14 --> 629.92]  Because I think those, those two things, you're working with the same underlying models and the same technologies,
[629.92 --> 634.30]  but the actual results are very different that you're creating with them.
[634.88 --> 637.92]  And just one more kind of story from Art School to illustrate.
[638.72 --> 642.74]  We, like one of the first projects that we built with my co-founder, Chris,
[643.32 --> 649.18]  was this drawing tool essentially where there was this model that NVIDIA released
[649.18 --> 652.42]  that was meant for kind of self-driving car research.
[653.04 --> 658.50]  And the main idea of this model was you could give a kind of a layout of essentially a street view.
[658.50 --> 664.48]  So like kind of indications of where pedestrians are or like the road is or other cars are,
[664.84 --> 667.50]  and then generate an image using that layout.
[667.68 --> 673.22]  It doesn't sound like the most kind of creative model or like creative use case for a tool.
[673.60 --> 678.86]  The context of that model is very much for like as part of like self-driving kind of car research
[678.86 --> 681.92]  and just kind of creating synthetic data for that and so on.
[681.92 --> 687.40]  But we decided to build this drawing tool around it where you could define kind of the layout of a scene
[687.40 --> 691.14]  and then generate kind of street views based on that layout.
[691.38 --> 696.90]  We saw that the moment we gave it to Artis, the kinds of scenes that we were creating were super different
[696.90 --> 699.46]  than like what the regular opposite of the model was.
[699.58 --> 704.94]  So they would create like giant pedestrians or like street signs flying from the sky.
[704.94 --> 710.54]  So there's the same insight there that, you know, you're working with the same types of models,
[711.06 --> 714.76]  the same types of technologies, but seeing them with a fresh set of eyes
[714.76 --> 717.66]  and a different perspective makes all the difference.
[718.14 --> 723.54]  And so this is what I came to art school to do is to see the same underlying kind of
[723.54 --> 727.92]  ML AI technologies with a new kind of set of eyes, exploring new possibilities.
[727.92 --> 731.14]  And this is what we hope to do also with the tool itself.
[744.02 --> 745.06]  What's up, friends?
[745.22 --> 749.10]  Is your code getting dragged down by joins and long query times?
[749.54 --> 751.70]  The problem might be your database.
[752.10 --> 754.72]  Try simplifying the complex with graphs.
[754.72 --> 758.78]  A graph database lets you model data the way it looks in the real world
[758.78 --> 761.42]  instead of forcing it into rows and columns.
[761.84 --> 765.28]  Stop asking relational databases to do more than what they were made for.
[765.80 --> 769.84]  Graphs work well for use cases with lots of data connections like supply chain,
[770.14 --> 773.42]  fraud detection, real-time analytics, and generative AI.
[773.96 --> 778.18]  With Neo4j, you can code in your favorite programming language and against any driver.
[778.42 --> 781.02]  Plus, it's easy to integrate into your tech stack.
[781.30 --> 783.68]  People are solving some of the world's biggest problems with graphs.
[783.68 --> 784.78]  And now it's your turn.
[785.06 --> 788.14]  Visit neo4j.com slash developer to get started.
[788.52 --> 792.00]  Again, neo4j.com slash developer.
[792.32 --> 796.84]  That's n-e-o-4-j dot com slash developer.
[796.84 --> 820.78]  So, you arrived at art school for that purpose of seeing all this through a new set of eyes.
[820.78 --> 822.56]  And you met your co-founder, Chris.
[823.02 --> 827.04]  And you guys had that spark of an idea, which would become Runway.
[827.24 --> 831.56]  Can you talk a little bit about the insight that you had there that created Runways?
[831.80 --> 837.66]  Before we dive fully into what Runway has done since, I'm really curious what the moment where you and Chris,
[838.02 --> 839.88]  you know, kind of said, we have something here.
[839.98 --> 841.36]  This is something we're going to go do.
[841.80 --> 842.88]  Was there a distinct moment?
[842.98 --> 844.80]  Did you just kind of gradually arrive there?
[844.80 --> 849.68]  What was that moment like where you decided it's time to go be an entrepreneur in this context?
[850.48 --> 854.00]  So, I wouldn't say it was one moment that kind of was the turning point.
[854.20 --> 859.54]  So, we were working on a lot of different projects with Chris and Alejandro, the other co-founder.
[859.54 --> 872.52]  And each of those projects was kind of a standalone tool around kind of helping for, let's say, a specific art project for an artist or for a specific kind of medium or specific kind of context.
[872.96 --> 877.70]  Over time, we realized that there was a lot of the same things that we had to do for each new project.
[877.70 --> 885.56]  And at that point, setting up, like being able to run models was even more like difficult than it is today.
[885.74 --> 897.40]  Even like kind of running a Google call-up notebook was like too much to ask sometimes for like artists without any technical kind of background or know-how about how those models work.
[897.84 --> 902.98]  So, the initial idea was, let's start from what's already out there in the open source world.
[902.98 --> 909.98]  Like there is already kind of a wealth of different models that perform different tasks, but let's make kind of a creative tool around them.
[910.08 --> 922.66]  So, let's bring the kind of interface and the kind of experience that artists are familiar with from other creative tools, but use those new models that were coming out that have all these interesting possibilities kind of on the backend.
[922.96 --> 925.98]  That was like the main idea of Runway initially.
[925.98 --> 945.44]  And also, as I mentioned before, there was kind of that vision was there from the start that as these models were becoming better and better, more the applicability of those models will go increasingly more from, you know, the more experimental use cases to something that's like actually driving production.
[945.44 --> 948.98]  And it's like really, really useful for a variety of creative workflows.
[949.26 --> 952.18]  And we saw that happen kind of very quickly after starting Runway.
[952.18 --> 971.86]  You mentioned along the way there that the difficulty of implementing some of the models and even today with a number of different choices out there, it's still something that many companies are contending with is, you know, how to address models, how to train them, where they're going to train them, what the deployment, you know, how it fits into products.
[971.86 --> 974.06]  There's a gazillion questions out there.
[974.06 --> 979.92]  You were doing this at a moment where that wasn't even as sorted as it is now.
[980.18 --> 981.98]  And it's still in development at this point.
[982.38 --> 984.00]  How did you manage that?
[984.30 --> 993.28]  Because that's when I've talked to other people, that's often been one of the biggest challenges is just getting the resources in place, especially at that time when it was still an early development.
[993.28 --> 1006.64]  What was that like to try to bring that, bring your vision out when obviously the environment that we were doing AI in was still fairly exclusive in a lot of ways in the sense of access to expertise, resources.
[1007.10 --> 1011.34]  You're in an art school that's designed to help you do that, but that couldn't have been easy.
[1011.82 --> 1011.92]  Yeah.
[1012.02 --> 1017.46]  So we essentially had to figure out a lot of things from scratch as we were building this.
[1017.46 --> 1038.60]  So as I mentioned, initially Runway was based around providing access to existing open source models, but we quickly actually realized that we needed to build a new house research team in order to really get those models from something that makes a good demo or a good prototype to something that's really useful.
[1039.18 --> 1044.90]  So that was actually from the first few months of Runway, it became very clear that we needed to do this.
[1044.90 --> 1048.48]  Of course, none of us three had built a research team before.
[1048.78 --> 1061.32]  That was like, I had engineering and research in some kind of ML and research background, but the experience of how to build the team, like what skills is to bring in was like nobody on the team had it.
[1061.46 --> 1064.46]  And so a lot of the things we just had to do and figure out from scratch.
[1064.86 --> 1069.28]  One nice thing I would say is that because we started so early, we had years to figure this out.
[1069.28 --> 1080.76]  So if you're just coming into like AI and like as part of kind of building a new company today, the time horizon, you need to figure those things out in much more accelerated fashion.
[1081.36 --> 1088.46]  So for us, like we spent the first years figuring out like, what does it mean to actually build a research organization within a startup?
[1088.46 --> 1097.34]  And what does it mean to build like a robust kind of deployment pipeline so that you can not only kind of serve those models, but also serve them interactively?
[1097.44 --> 1102.02]  Because a big part of the way we build tools at Runway is like the interactions.
[1102.36 --> 1106.04]  It's a very key aspect of really making those models useful.
[1106.04 --> 1119.82]  I think when I've talked to other entrepreneurs about this, you know, they have a tough time as you're kind of getting to the place where you're at now in terms of being able to, you know, have the research, you're doing amazing research.
[1119.94 --> 1125.18]  But you had to kind of get from A to B in the meantime and kind of keep the company alive.
[1125.18 --> 1131.68]  How did you approach from a funding customers, things like that, while you were kind of figuring all these things out?
[1131.78 --> 1139.14]  Because that strikes me as a pretty hard problem to tackle in, you know, as you're moving along, but you still have to pay the bills, if you will.
[1139.26 --> 1148.06]  How did you tackle those kind of issues in terms of creating an AI startup that couldn't instantly be everything, you know, that it is today from day one?
[1148.06 --> 1155.38]  I would say the main insight is to, we wanted to make sure that Runway was useful at each stage of its evolution.
[1155.76 --> 1167.30]  So even though, you know, the generative models were not quite as powerful back when we started as they are today, they weren't as big a part of the initial kind of tool offering.
[1167.30 --> 1171.28]  And we wanted to make the tool as useful from like the very beginning as possible.
[1171.28 --> 1181.52]  So the product of Runway went through many evolutions that really track how the kind of AI models evolved and at which stage they were useful for which things.
[1182.04 --> 1194.00]  A big part of early Runway was building out a video editor that was a really combined some of the more traditional video editing techniques with AI-based techniques to speed up the process of a lot of video editing workflows.
[1194.00 --> 1207.98]  And that wasn't necessarily something that had generative models powering it, but it was a really useful tool that really gave us a lot of insight about how to build tools that are really useful for creative workflows and how to really solve like real pain points of video editors.
[1208.48 --> 1221.68]  But at the same time, while we're building those tools, we're also at this kind of research that was ongoing, that was still remaining at a kind of more academic level of just like really demonstrating how we can improve the results of generative models.
[1221.68 --> 1227.32]  And at some point, there was that kind of intersection point where we started bringing those generative models production.
[1227.98 --> 1234.38]  So the overall strategy was we knew that generative models would be like really powerful given enough time.
[1234.46 --> 1242.20]  And if we invest the resource on the research side, at the same time, we knew that at the beginning, not everything is to be powered by generative models.
[1242.20 --> 1261.64]  So we're building a lot of AI-based tools that incorporated, that were really useful from the beginning, and that they were used by VFX artists, by video editors to speed up a lot of their workflow, even far before we released things like Gen 1 or Gen 2 for kind of text-to-video functionality.
[1261.64 --> 1265.58]  You know, you're saying generative, but it was definitely the early days of generative.
[1265.92 --> 1268.78]  And you certainly, like right now, it's all the rage.
[1268.92 --> 1271.42]  You know, everyone's talking generative in every context.
[1271.66 --> 1274.22]  But you had some insights into that.
[1274.32 --> 1279.22]  You know, you talked about the fact that you guys knew that that was going to be the case going forward.
[1279.58 --> 1282.50]  But to your credit, not everybody did.
[1283.24 --> 1287.24]  You know, there's been a lot of people went, aha, much later than you went, aha.
[1287.24 --> 1295.30]  And I'm kind of curious, is there anything that stands out as what drove the insights that you guys had and why?
[1295.40 --> 1301.30]  Because, I mean, you were really one of the very first to get these kinds of functionalities, you know, to product.
[1301.56 --> 1302.72]  That's very notable.
[1302.94 --> 1308.28]  And, you know, you might say the rest of the world didn't, you know, not that many.
[1308.38 --> 1316.32]  And so what were some of the things that gave you that confidence to say, this is clearly going to be critical to our future.
[1316.32 --> 1319.50]  This is going to drive the industry at an early stage.
[1319.62 --> 1321.84]  You were pioneering that thought process.
[1322.20 --> 1322.92]  How did you get there?
[1323.36 --> 1327.70]  From the very beginning, a big part of running was working directly with artists and building those tools.
[1327.94 --> 1337.70]  And so when we gave them even early versions of generative models, we could already see that they, like, there was really compelling aspects of working with them.
[1337.88 --> 1341.72]  Even if the results were low resolution or, like, not as high fidelity.
[1341.72 --> 1350.90]  So, like, early forms of things like prompt engineering or, like, figuring out how to kind of traverse the latent space of those models were still there at the beginning of runway.
[1351.32 --> 1360.06]  And we saw how artists were engaging with them, like how they were kind of, they were finding them to be really compelling and really useful.
[1360.06 --> 1370.94]  And so really part of it has been just having this early view into how artists would kind of more early adopters, I would say, were engaging with those models.
[1371.12 --> 1376.24]  And just extrapolating that once those models improve, other people will equally find them as compelling.
[1376.24 --> 1385.90]  So working with artists, I think, has been a really important part of just really understanding kind of the future of those models and extrapolating of how they would be used.
[1385.90 --> 1400.22]  And also just looking at the kind of history of art and how toolmaking was always part of, like, how new tools always allowed kind of new, created new kind of art movements or allowed new kinds of kind of genres to emerge.
[1400.64 --> 1405.34]  And just assuming and kind of predicting that the same would happen with those generative models.
[1405.34 --> 1418.10]  Along the way, as you were going down this path, what stumbles did you have, you know, as part of putting, because it's quite remarkable, because you clearly could see the future, you know, before you got there.
[1418.10 --> 1431.46]  And with more clarity than others that might be in a similar position, as you did that, what kinds of things did you were either unexpected or challenges that were bigger than you thought?
[1431.46 --> 1438.38]  You know, the things were maybe at a moment in time, you were grinding your teeth and going, or this is not exactly how I had it planned.
[1438.46 --> 1441.46]  Do you have any stories to that effect during this process?
[1441.94 --> 1445.52]  Many stories and many learnings along the way, for sure.
[1445.52 --> 1458.64]  I think the biggest requiring insight that we've had around how to build for those tools, and the thing that I think is still not fully appreciated today, is how important control is in terms of interacting with those models.
[1458.64 --> 1473.12]  And so every time we invested into adding more ways in which you can really control the outputs of the models that people were using inside Runway, we saw a whole new set of possibilities and whole new kinds of usage.
[1473.12 --> 1476.12]  So that has been a really consistent theme.
[1476.12 --> 1487.20]  And even at the beginning, we just saw that those models had a lot of flows that they might, you know, not always, like if you have a very simple ways of controlling them, they might not really give you what you want.
[1487.20 --> 1495.60]  And you might have to like, do a lot of like tries with the same model can generate a lot of outputs to get to kind of where you want your desired result.
[1495.60 --> 1504.14]  And so that's really what we saw with the kind of early, like when we first released Gen 2, you could only kind of control things with a text prompt.
[1504.78 --> 1513.74]  And we saw very quickly that that led to people just kind of generating like tens or hundreds of outputs in order to get to the result that they wanted.
[1514.16 --> 1523.54]  And so we invested kind of continuous more and more, adding more and more ways in which you can like manipulate things essentially as a film director would think about creating a scene.
[1523.54 --> 1534.56]  So a film director would have a vision, not just of like, you know, description, high level description of what the scene is, but how the camera moves in a scene or like how do the characters interact with each other.
[1535.00 --> 1547.92]  So having ways in which you can control really the kind of camera motion or like the motion, the object motion, like the motion of the characters in a scene, like all those things that like make total sense from a curious point of view.
[1547.92 --> 1553.34]  But they're not necessarily how like maybe ML researchers would necessarily think about those models.
[1553.78 --> 1561.82]  I think that has been always the insight that, you know, we never, we never saw negative effects from adding more and more ways of controlling those models.
[1577.92 --> 1582.54]  This is a changelog news break.
[1583.24 --> 1585.42]  Pewter is the internet OS.
[1585.92 --> 1595.10]  Pewter is an advanced open source desktop environment in the browser designed to be feature rich, exceptionally fast and highly extensible.
[1595.50 --> 1604.92]  It can be used to build remote desktop environments or serve as an interface for cloud storage services, remote servers, web hosting platforms and more.
[1604.92 --> 1610.90]  I've been around long enough to see a bunch of these desktop OS and a browser window demos and toys.
[1610.90 --> 1616.56]  But this is the first time I've been impressed by one enough to keep the tab open longer than 30 seconds.
[1617.14 --> 1627.34]  From the URL structure to the cloud storage integration to the developer portal, Pewter strikes me as an actually viable internet based operating system with potentially real world use cases.
[1627.66 --> 1628.50]  And that's saying a lot.
[1628.86 --> 1632.96]  Oh, and it's also entirely built with vanilla JavaScript and jQuery.
[1632.96 --> 1637.36]  So you know the devs haven't cargo culted together something they can't grow and maintain.
[1637.74 --> 1639.16]  On that note, they say,
[1639.68 --> 1643.14]  For performance reasons, Pewter is built with vanilla JavaScript and jQuery.
[1643.40 --> 1650.04]  Additionally, we'd like to avoid complex abstractions and to remain in control of the entire stack as much as possible.
[1650.28 --> 1654.72]  Also partly inspired by some of our favorite projects that are not built with frameworks.
[1655.14 --> 1657.98]  VS Code, PhotoP, and OnlyOffice.
[1657.98 --> 1663.54]  You just heard one of our five top stories from Monday's Changelog News.
[1663.92 --> 1676.32]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1676.76 --> 1680.20]  Once again, that's changelog.com slash news.
[1680.20 --> 1688.26]  So before the break, you brought up Gen 2.
[1688.46 --> 1692.76]  And I'd like we've had a little bit of a history on the development, which is fascinating.
[1692.90 --> 1694.26]  It's an incredible story you have.
[1694.84 --> 1697.20]  Tell us all about Runway today.
[1697.56 --> 1698.64]  You've arrived here.
[1699.08 --> 1699.90]  You have Gen 2.
[1700.30 --> 1704.40]  Just talk a little bit about how you're impacting industry today.
[1704.40 --> 1710.02]  And for listeners who haven't been to your website, you talk about advancing creativity with artificial intelligence.
[1710.02 --> 1716.16]  And you specifically note that you're an applied AI research company shaping the next era of art, entertainment, and human creativity.
[1716.74 --> 1720.52]  What does that mean in 2024 as you're out there in the space?
[1720.84 --> 1723.00]  Can you talk a little bit about the company as it is now?
[1723.50 --> 1723.62]  Yeah.
[1723.76 --> 1728.50]  To give some context, Gen 2 is a text-to-video and image-to-video generation model.
[1728.50 --> 1733.34]  So essentially, it takes a description of a scene and generates a video output from that scene.
[1733.34 --> 1738.50]  And it's one of the many models that we have at Runway, the most well-known one.
[1739.00 --> 1743.36]  The broad vision of the company has remained the same over the last five years.
[1743.50 --> 1747.42]  And it's understanding and creating the new generation of creative tools.
[1747.90 --> 1753.20]  And then working with artists directly to figure out, to help them shape those tools as much as possible.
[1753.76 --> 1760.32]  And so I think where we are today is, I would say we're still at the very early stages of where those models can go.
[1760.32 --> 1765.74]  I think video generation, this is really the year where video generation gets really good.
[1765.74 --> 1777.04]  And so we're really excited to be part of building out those technologies and figuring out how to work with artists to make them as useful as possible.
[1777.44 --> 1785.60]  We've seen over the past years, and we're with Gen 2, film studios, streaming companies, ad agencies adopting Runway.
[1785.60 --> 1794.16]  And that adoption is not just from kind of individual creators, but it's really we see companies starting to use those models and incorporating in the workflows.
[1794.76 --> 1805.00]  And I think it's not going to be a binary shift where you go from not using Gen 3 models at all as part of kind of making video or making art to using it everywhere.
[1805.26 --> 1806.60]  It's a more gradual transition.
[1806.60 --> 1814.62]  And for us, the big goal is kind of teaching folks how to use those models, supporting all the creators that are making interesting things with those models.
[1815.06 --> 1822.06]  So we have an AI film festival that we showcase kind of films that use AI in different ways.
[1822.50 --> 1832.56]  So I would say for us, the goal is very much kind of holistic of like we do the research, we create the research and development in building out the next generation of those models.
[1832.56 --> 1840.38]  We build useful tools around those models, and we also work with artists and with companies that want to adopt those models in their creative workflows.
[1841.18 --> 1852.74]  As you have been working into this for years, for most of the rest of the world, the past few months have been a big eye-opener, particularly with big cloud companies, you know, producing their models and stuff and competing in that.
[1853.14 --> 1857.74]  There's the obvious aspect of you have the industries that you're playing in and that you're strung in.
[1857.74 --> 1870.82]  But what concerns do you have from a competitive standpoint against other companies, you know, especially these big all-encompassing cloud companies that are in sort of the AI arms race to produce the ever-larger, more capable model?
[1871.22 --> 1874.42]  At no point in this conversation have you expressed any concern.
[1874.86 --> 1877.14]  Have you raised that or anything, which is quite notable.
[1877.34 --> 1880.16]  Usually people are a little bit worried about that.
[1880.40 --> 1882.36]  And you seem very strong in your space.
[1882.96 --> 1885.92]  How do you see those other big players that are out there?
[1885.92 --> 1887.70]  Do you see them as competitors even?
[1887.92 --> 1890.36]  Or are they far enough from you that that's not a big deal?
[1890.56 --> 1897.44]  Or are you so tightly into the industries that you're serving specifically that you have a huge competitive advantage?
[1897.48 --> 1898.30]  How do you see all that?
[1898.72 --> 1903.50]  For us, we've always kind of had the perspective and mindset of running a wrong race.
[1903.72 --> 1915.78]  And so we try not to kind of be too distracted by, especially at these days, like there is so much kind of noise and discourse around AI that it's easy to kind of get stuck in like following the latest.
[1915.92 --> 1916.48]  Development.
[1916.48 --> 1919.16]  So I think that's kind of the number one aspect.
[1919.36 --> 1929.72]  When we first released Gen 2 last year, one of our positions that was not as popular, I would say, last year was that video generation models were going to be the kinds.
[1929.92 --> 1937.06]  Like video was the modality that kind of encapsulated as much world knowledge and usefulness as possible.
[1937.06 --> 1939.74]  And last year, a lot of the focus was on language.
[1940.22 --> 1952.04]  And for us, it was a bit kind of unorthodox to kind of maybe pay so much attention to video specifically and claim that video generation models were like really the way to build really broadly useful AI systems.
[1952.04 --> 1957.56]  And over the past months, we've seen more companies kind of entering the space of video generation models.
[1958.02 --> 1959.76]  And so it was nothing unexpected.
[1960.08 --> 1964.32]  Like we know that those models are going to be really useful for a wide variety of use cases.
[1964.78 --> 1968.84]  They're going to be useful beyond creating creative tools, which is really our focus.
[1968.84 --> 1989.08]  And so for us, it's really important to maintain that focus of really like not just building those models and like making kind of cool demos around that, but really figuring out like bridging that gap between, you know, those demos and really deploying them to products and really getting kind of people to use them and getting kind of making them controllable.
[1989.08 --> 1998.06]  So there is still that gap, I would say, from doing just the research and developing the model to actually making those models controllable and deploying useful tools.
[1998.62 --> 2001.32]  And for us always, it has been the focus to bridge that gap.
[2001.78 --> 2003.82]  And so that's kind of continues to be our focus.
[2004.56 --> 2013.56]  So again, like video generation models are still very early and like we haven't kind of seen anything yet about what they'd be ultimately capable of.
[2013.56 --> 2020.08]  You can imagine, you know, a year from now, two years from now, every company is going to have like a photorealistic video generation model.
[2020.52 --> 2025.06]  And that's an assumption that we're making that the competitive advantages shift over time.
[2025.56 --> 2029.32]  And at that point, like what's the differentiation of runway for us?
[2029.46 --> 2038.54]  It's always been working very closely with artists, building really useful tools and bridging and bringing, making those models really controllable and useful.
[2038.54 --> 2047.16]  It's fascinating to me because I talk to so many people in different companies and they're busy trying to just AI everything.
[2047.42 --> 2048.98]  And they're kind of all about the AI.
[2049.36 --> 2063.82]  You guys are doing the AI, but it sounds like competitively having been so embedded into the artistic ecosystem with your tooling is really, you know, kind of something that keeps you right there.
[2063.82 --> 2070.18]  While everybody goes through the kind of the AI model wars, you know, in terms of trying to produce so much.
[2070.72 --> 2074.62]  Do you think that long heritage of the tool making is probably key to your future in that sense?
[2074.70 --> 2076.26]  Is that kind of how you're thinking about it?
[2076.68 --> 2079.26]  I think it's the most important aspect of how we're operating.
[2079.26 --> 2092.06]  Otherwise, again, it's too easy to get lost in a short-term race of just having kind of a marginally better model for a few weeks versus kind of really having the mindset of building the most useful tool long term.
[2092.06 --> 2096.66]  And then obviously updating the model, making sure, you know, you get state-of-the-art results with it.
[2096.94 --> 2098.10]  But it's not the goal.
[2098.22 --> 2100.36]  It's not the focus to have the best model.
[2100.80 --> 2106.74]  The focus is to get artists to make, you know, the coolest things or the most compelling things with those models.
[2106.74 --> 2112.18]  And if that remains the goal, then that also informs how we build those models.
[2112.48 --> 2128.18]  And so, like, another aspect of Runway is just, like, we have a research team and then we also have a creative team in-house that works with the research team on a daily basis and, like, tries out the latest models, informs how we do the research, like, what kind of controls we need to have the models.
[2128.18 --> 2140.14]  And having that perspective is really, like, when I talk to researchers that work in, you know, academic labs or kind of large industry labs, they might publish papers about the potential creative applications of those models.
[2140.38 --> 2142.30]  But they don't interact with artists daily.
[2142.42 --> 2147.70]  They don't often know, like, is this actually useful or is it just a hypothesis that I'm making?
[2148.12 --> 2152.52]  And Runway, as a researcher, you get that feedback on a daily basis.
[2153.02 --> 2156.46]  And I think that really changes how you approach building those models.
[2156.46 --> 2161.48]  For listeners, you and I can see each other, though this is an audio-only podcast.
[2162.16 --> 2168.94]  But you had this glint in your eye a moment ago when you were talking about kind of where you expected these video models to be going.
[2169.42 --> 2172.98]  For just a minute there, you reminded me of kind of the kid in the candy store.
[2173.16 --> 2176.12]  You could see your passion really flying out of your eyes there.
[2176.32 --> 2178.24]  And obviously, I'm the only one that could see that.
[2178.80 --> 2180.72]  Talk a little bit about where you think this is going.
[2180.72 --> 2182.18]  That's what everybody is wondering.
[2182.42 --> 2194.94]  There's so many questions, you know, that people have in terms of, you know, how video fits in their life, what life becomes like when you have generative capabilities that essentially, you know, simulate life in so many ways.
[2195.20 --> 2198.50]  What are you expecting over the next year or so?
[2198.50 --> 2206.04]  And like, I'm not holding you to it, obviously, but just what do you anticipate might happen in the video space generatively?
[2206.36 --> 2212.76]  And then how would you see it several years out, you know, when it's kind of exponentially had time to grow a bit?
[2213.04 --> 2214.14]  What does that look like to you?
[2214.14 --> 2222.36]  The way we like to think about those generative model models is we have this term of their general world models.
[2222.84 --> 2235.74]  Essentially, they simulate different aspects of the world because in order to kind of similar to how, you know, you have large language models that have been trained with a very simple task to just predict the next token in a sentence.
[2235.74 --> 2247.58]  In order to predict that the next token and perform the task really well, they have to gain all this understanding about kind of different aspects of human knowledge, different aspects of the world just to solve this task well.
[2248.04 --> 2256.58]  Because they need to, you know, complete sentences that might, you know, come from an encyclopedia or like a forum post or it's like a wide variety of cases that we need to have.
[2256.58 --> 2261.60]  So we think very similarly of how those video generation models operate.
[2262.02 --> 2269.16]  In order to predict the next frame, you need to gain kind of not the understanding of basic kind of rules of motion or like physics.
[2269.58 --> 2274.36]  You really need to gain a kind of more comprehensive, like broader understanding of the world.
[2274.82 --> 2278.88]  And so like if I think, you know, a year from now, where did those models go?
[2278.88 --> 2291.70]  Essentially becoming more and more higher fidelity simulations of the world, giving you the ability to really imagine all sorts of different kind of scenarios, like build out, tell all kinds of different kind of narratives and stories.
[2291.70 --> 2305.36]  And I think that the applications of that are kind of really, there is kind of wide ranging kind of application that goes beyond the kind of content creation use cases, which I think for us are kind of still remain the focus.
[2305.86 --> 2314.88]  But just building models that can, you know, perceive the visual world, like, of course, like can be used in all kinds of other ways as well.
[2315.38 --> 2316.76]  Thank you for sharing your story.
[2316.76 --> 2330.70]  As we finish up here, we have a lot of young listeners on the show and there is, I guarantee that there are quite a few young artists that are technically inclined out there, you know, high school, maybe early college age.
[2330.98 --> 2335.14]  And they're listening to this and they're going, that guy just lived the life that I'm wishing I could live.
[2335.26 --> 2337.24]  You know, that's the kind of thing that I want to do.
[2337.54 --> 2345.00]  What would you, whether they identify themselves kind of as a young artist who's technically inclined or technologist who loves art, however they see themselves.
[2345.00 --> 2360.50]  Do you have any guidance on how they might step into the future and kind of get to that sweet spot for them, given the fact that clearly the technology was specifically with AI and the artistic world will continue to merge and develop together for years to come?
[2360.60 --> 2361.74]  How, where should they go?
[2361.82 --> 2362.46]  What should they do?
[2362.54 --> 2362.98]  Any thoughts?
[2363.36 --> 2367.96]  I would say the number one thing is following your curiosity and team training as much as possible.
[2367.96 --> 2373.32]  So there is a lot of ways in which you can, you can start kind of like building those models yourself.
[2373.32 --> 2374.82]  You can start kind of running them.
[2375.14 --> 2378.46]  You can start to get kind of an understanding of what you can do with them.
[2378.52 --> 2381.12]  And that's available to really kind of anyone.
[2381.80 --> 2390.14]  And so really like you can start getting involved today in building projects, kind of exploring AI or making creative projects with AI.
[2390.46 --> 2391.82]  That would be the number one thing.
[2391.82 --> 2398.20]  It's also, I would say for me, planning, trying to plan ahead too much has never quite worked.
[2398.60 --> 2409.00]  Really focusing on like what I can build today, like where kind of curiosity and interestingness will drive me next has always been kind of the guiding principle.
[2409.00 --> 2422.70]  And so that would generally be my, my recommendation is not trying to think of, you know, what, where technology will be five years from now, because really nobody can fully plan ahead, but rather trying to really build interesting things today.
[2422.70 --> 2433.48]  It's actually surprisingly, I would say easy to like, if you started making, you know, projects open source and just showing them to others, it can be quite fast that you can get noticed for those projects.
[2433.48 --> 2439.80]  And you can like start to, you know, build a community around them, work with other people and collaborate on your projects.
[2440.32 --> 2447.32]  And kind of with those collaborations kind of one by one, you can kind of get to a point where you can kind of start kind of doing this work full time.
[2447.76 --> 2453.50]  So like really focusing on the next project, I think for me has been really the way to go.
[2454.04 --> 2455.52]  Well, Anastasios, thank you so much.
[2455.58 --> 2456.90]  That was fantastic guidance.
[2457.12 --> 2458.88]  Appreciate your, your perspective.
[2459.18 --> 2461.24]  Fascinating story leading into this.
[2461.24 --> 2465.02]  And especially in all the early insight that you guys had.
[2465.20 --> 2470.30]  Thanks for coming on and talking about runway and the world in which you guys are trying to make a bit better.
[2470.56 --> 2470.94]  Appreciate it.
[2471.22 --> 2471.76]  Thank you, Chris.
[2479.12 --> 2480.16]  All right.
[2480.42 --> 2482.82]  That is Practical AI for this week.
[2483.62 --> 2484.66]  Subscribe now.
[2484.66 --> 2489.82]  If you haven't already, head to practicalai.fm for all the ways.
[2489.82 --> 2496.22]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[2496.78 --> 2501.44]  Sign up today at practicalai.fm slash community.
[2502.04 --> 2508.96]  Thanks again to our partners at fly.io, to our Beat Freaking Residence, Breakmaster Cylinder, and to you for listening.
[2509.32 --> 2511.08]  We appreciate you spending time with us.
[2511.44 --> 2512.62]  That's all for now.
[2512.86 --> 2514.54]  We'll talk to you again next time.
[2514.54 --> 2544.52]  We'll talk to you again next time.
