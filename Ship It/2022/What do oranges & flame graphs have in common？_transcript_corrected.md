[0.12 → 5.12] Welcome to Ship It, a podcast about Ops, Oranges, and Flame Graphs.
[5.42 → 10.64] Today, we are talking with Frederik Branch, founder of Polar Signals and Prometheus Maintainer.
[10.90 → 15.82] Some of you may remember Frederik from episode 33, when we introduced parka.dev.
[16.28 → 23.04] In today's episode, we talk about a database built for observability, Frost DB, formerly
[23.04 → 24.58] known as Arctic DB.
[24.58 → 30.16] EPF generates a lot of high cardinality data, which requires a new approach to writing,
[30.48 → 32.44] persisting, and then reading back this state.
[32.88 → 37.64] My TLDR is that Frost DB is sub-zero cool and well worthy of its name.
[38.10 → 39.40] Do you know what else is cool?
[40.02 → 44.00] Vastly, for serving our content with minimal latency right from their edge.
[44.50 → 46.16] Learn more at fastly.com.
[46.16 → 58.00] This episode is brought to you by MongoDB, the makers of MongoDB Atlas, the multi-cloud
[58.00 → 59.80] application data platform.
[60.32 → 65.70] Atlas provides an integrated suite of data services centred around a cloud database designed
[65.70 → 67.78] for scale, speed, and simplicity.
[68.28 → 72.68] You can ditch the columns and the rows once and for all and switch to a database loved by
[72.68 → 75.20] millions for its flexible schema and query API.
[75.20 → 79.18] When you're ready to launch, Atlas layers on production-grade resilience, performance,
[79.48 → 82.40] and security so you can confidently scale your project from zero to one.
[82.76 → 85.12] Atlas is a truly multi-cloud database.
[85.44 → 90.90] Deploy your data across multiple regions simultaneously on AWS, Azure, and Google Cloud.
[91.30 → 92.42] Yes, you heard that right.
[92.50 → 95.74] Distribute your data across multiple cloud providers at the same time.
[96.00 → 97.82] The next step is to try Atlas Free today.
[98.16 → 99.18] They have a free forever tier.
[99.48 → 102.72] Prove yourself and your team that the platform has everything you need.
[102.72 → 105.26] Head to MongoDB.com slash changelog.
[105.38 → 109.08] Again, MongoDB.com slash changelog.
[114.36 → 115.74] We are going to shift.
[115.92 → 118.42] Three, two, one.
[118.42 → 133.08] Hi, Frederick.
[133.42 → 134.76] Welcome back to Ship It.
[134.88 → 136.58] Just in time for summer.
[137.06 → 138.14] Thanks for having me back.
[138.14 → 140.28] So we last met in episode 33.
[141.12 → 142.16] Merry Shipman.
[142.56 → 143.22] It was Christmas.
[143.36 → 143.96] Can you believe it?
[143.98 → 144.74] And it's almost summer.
[144.86 → 145.80] So six months ago.
[146.06 → 148.98] And we had a great time talking about trying out Parka.
[149.10 → 150.40] And I enjoy trying it out.
[151.04 → 151.94] Yeah, same for us.
[151.94 → 153.26] Michal Jurassic.
[153.42 → 157.38] Thank you for figuring out what we're doing wrong with Erlang Perf Maps.
[157.62 → 160.00] That was Parka agent issue 145.
[160.32 → 162.58] So thank you, Michal, for helping us figure it out.
[163.12 → 165.10] And this happened very recently.
[165.62 → 166.34] Thank you, David.
[166.42 → 168.84] David An sari for writing that amazing blog post.
[169.10 → 174.78] How to use Prof with and how to do flame grass with RabbitMQ and mentioning Parka.
[174.88 → 177.40] I'm really excited to see what happens next.
[177.52 → 178.48] That was very nice to see.
[178.48 → 180.14] We'll drop a link in the show notes.
[181.06 → 188.20] And Kamal, he wrote two blog posts on various topics, which there's like lots of things happening in this space.
[188.42 → 190.86] So do you want to tell us more about it, Frederick?
[191.08 → 193.34] Because it's like the tip of the iceberg, literally.
[193.86 → 195.78] The tip of the Polar Signals iceberg.
[195.98 → 198.02] There's been so many things happening in the background.
[198.44 → 200.64] Yeah, I mean, where to start, right?
[200.98 → 206.96] I think one of the most exciting things that have nothing to do with software for us at Polar Signals
[206.96 → 209.72] is that we grew the team a ton since we last talked.
[210.00 → 213.68] I think we doubled the team since you and I talked last.
[213.68 → 218.68] So we're now 11 people, which is extremely exciting to see organizationally.
[219.72 → 228.60] But then, of course, the software that we're building is becoming ever better, ever more features and more stable and everything.
[228.60 → 235.36] Yeah, I think it's cool that you started with the Erlang bit because that's kind of where we left off last.
[235.54 → 246.24] And it's entirely random that just yesterday, that RabbitMQ blog post was to no control of you or me was published, right?
[246.32 → 250.84] Showing that what we were trying to do last time is properly supported by Erlang.
[250.84 → 253.46] You know, when things are meant to happen, they just happen.
[253.82 → 255.38] Just sit back and just let them happen.
[255.48 → 256.32] Just going with the flow.
[256.42 → 257.28] Big fan of that.
[257.60 → 261.50] And seeing things come together this way, we're definitely on the right track with this.
[262.00 → 266.10] So I know that Kamal Akron, he was with you back in December.
[266.66 → 270.10] He wrote two blog posts, amazing blog posts on this topic.
[270.82 → 274.20] Fantastic symbols and where to find them, part one and two.
[274.50 → 275.66] We'll drop them in the show notes.
[275.66 → 282.10] And they explain a lot more of the issues that we're seeing, and the issues were specifically symbolizing stack traces.
[282.66 → 285.54] Kamal did an amazing job explaining it in great detail.
[286.12 → 287.32] There are some screenshots there.
[287.76 → 290.92] David covers a lot of this in his blog post, the recent blog post.
[291.08 → 293.90] So it's a really deep dive into this topic.
[293.90 → 307.96] And I really enjoy these like fantastic people spending a lot of time just to explain in very detailed terms what the problem is, why it's important, how it works.
[308.08 → 309.18] Big fan of that too.
[309.52 → 314.40] So in these six months, what changed with Parka, parka.dev?
[314.70 → 319.20] So I think almost everything has changed at least a little bit.
[319.20 → 329.62] Since you mentioned the work that Kamal has been doing and all the blog posts that he's been writing, the blog posts are kind of the result of all of his work, right?
[329.66 → 334.90] Like basically they're the blog posts that he wished he had had when he was working on this.
[334.90 → 338.92] Because there's so much archaic information out there.
[339.12 → 343.54] Or like basically like Linux has grown over the last 30 years.
[343.68 → 344.24] My gosh.
[344.24 → 350.12] And like even before that, like elf binaries, like they've been around for a very long time.
[350.32 → 353.88] And yeah, there are just a lot of intricate things that can happen.
[353.98 → 358.18] And then there are random things that compilers do to binaries to optimize them.
[358.26 → 364.92] And that kind of just all makes our life really miserable, but also kind of interesting in profiling world.
[364.92 → 381.72] And yeah, so Kamal has kind of like one of the really important things that kind of came out of all of this work that Kamal was doing and what ultimately resulted in those blog posts as well is something called position independent executables support for these.
[381.72 → 390.18] And the reason why this is really important is basically all binaries or all like shared objects, shared libraries.
[390.52 → 395.82] So think of LBC is kind of the one that basically everything dynamically links to, right?
[396.22 → 405.36] But anything you can think of that is like a shared object, shared library and Linux, those are position independent executables.
[405.36 → 414.92] And that the term comes from that they can essentially be mapped into memory, into random places in the process, basically.
[414.92 → 428.26] And even if they are mapped in those random places, we can still kind of translate those memory addresses back to something that is understandable uniquely for that shared library.
[428.70 → 437.92] So even if there are two different binaries that do completely different things with these libraries, the shared object is the same one, and we can treat it as the same one.
[437.92 → 461.06] So that was really important so that we can do analysis of like an entire infrastructure where, as I said, lots of binaries linked to the same libraries, and we can then link all of this information and say, hey, there are like hundreds of binaries using this function in LBC that is super unoptimized or something like that, right?
[461.18 → 462.62] Not that that's really the case.
[462.70 → 466.56] LBC is a very well optimized library, but you get the idea.
[466.56 → 471.04] It's basically a superpower in order to get like whole system visibility.
[471.68 → 471.74] Yeah.
[471.86 → 473.00] So that's exciting.
[473.18 → 478.58] And kind of as a bonus, every Rust binary out there is a position independent executable.
[478.84 → 485.02] So that means that just by doing all this work, we now support Rust even better than we did before.
[485.42 → 486.10] That's amazing.
[486.38 → 487.02] That's amazing.
[487.48 → 495.98] The one thing, so thank you for slowing me down because you're right, this is important, like to talk about those two blog posts, the fantastic symbols and where to find them.
[495.98 → 504.88] The first one, the ELF, the Linux executable walkthrough, that picture, I think it's worth a thousand words in this case.
[505.12 → 512.84] It explains so well how this breaks down, how the ELF binary breaks down, what it is, sorry, the ELF format.
[513.10 → 515.00] And there's so much to that.
[515.00 → 522.28] And then in part two, where we talk about JIT and Node is given as an example, how does it actually work in practice?
[522.48 → 528.92] It's really nice to see that and to basically connect those dots because there's, as you mentioned, the problem space is huge.
[529.40 → 535.72] And if you're missing those fundamentals, it's very difficult to understand how the pieces fit together and what are you even looking at.
[535.72 → 537.64] Why is this important?
[537.94 → 541.50] David, he wrote it in the Improving RabbitMQ Performance blog post.
[541.68 → 552.72] He showed the importance of understanding what is happening at a very low level when it comes to reasoning about performance, when it comes to improving performance in whatever you're running.
[553.20 → 554.60] So where is the time spent?
[554.74 → 556.74] What is the least efficient?
[556.74 → 562.38] And because these things are so complicated, can we have a universal language, please understand what is happening?
[562.78 → 569.64] And I think to a great extent, EPF allows us to do things that were not possible before or were very, very hard before.
[569.78 → 574.78] And only a handful of people were able to pull this one-off and even then spend a lot of time.
[574.92 → 577.62] Brendan Gregg came to mind, this comes to mind.
[578.02 → 584.60] He did so much for the flame graph, understanding, CPU sampling, CPU profiling, all that.
[584.60 → 585.52] Yeah, absolutely.
[585.52 → 597.94] And I think kind of our mission with the Parker project is to take all of this information from all of these communities and kind of bundle it into one, right?
[598.00 → 607.54] Like you said, Brendan Gregg has done phenomenal work showing us how to profile Java applications, but also native binaries.
[607.54 → 612.06] And then there are like completely on the other side of the spectrum, right?
[612.52 → 615.74] There are really amazing Python and Ruby profilers.
[616.34 → 623.26] Like one that I'm really excited about is Ruby Spy that was originally created by Julia Evans.
[623.26 → 632.20] And it basically outlines how we're going to have support for CPU profiling for Ruby processes as well.
[632.64 → 634.70] And that's what I'm kind of trying to say, right?
[634.76 → 637.20] Like we learned also about Erlang, right?
[637.28 → 641.78] That's kind of something that actually came out of this podcast, which I think is really exciting.
[641.78 → 652.94] Just kind of getting all of these pieces together so that we can have actual whole system profiling so that we can look at our entire infrastructure as one, right?
[653.02 → 654.98] Regardless of what language we're talking about.
[654.98 → 658.06] And as we can see based on this podcast, right?
[658.40 → 662.78] That's a long road to go, but it's one word going.
[662.98 → 666.60] I really like how simple you make this.
[666.76 → 669.30] I think that's one of my favourite aspects of parka.
[669.82 → 671.92] How something that's very complex.
[672.02 → 675.36] And if you have to do this by hand, just go and look through all the instructions.
[676.24 → 679.78] And if you haven't done this, you realize like by step number five or six, you go, you know what?
[679.84 → 680.84] Do I really want to do this?
[680.90 → 683.58] Like you're questioning whether you really want to do that.
[683.58 → 685.68] That's just how involved it is.
[686.74 → 691.54] And having an open source project that does this, that makes this really, really easy.
[691.66 → 692.96] That's what just got me excited.
[692.96 → 697.00] The first time I heard about parka because I knew how difficult it is to get it right.
[697.68 → 704.44] And I think everyone that spent a bit of time with PROF and which is the other one, DBG, no GDB.
[704.86 → 706.02] Oh my goodness me.
[706.18 → 706.60] Oh wow.
[706.62 → 709.16] That's like another tool, which is so difficult to use.
[709.32 → 711.40] And I had like to spend a bit of time there.
[711.40 → 713.62] And I almost always forgot like my steps.
[713.74 → 714.54] There's like so many.
[714.96 → 718.90] So unless you do this all day, every day, it's really hard stuff.
[719.44 → 720.84] And parka makes it simple.
[720.98 → 722.18] And I love that story.
[722.18 → 726.58] It's funny that you phrase it in that way, because I was talking a couple of weeks ago,
[726.64 → 729.22] I was talking to like a high frequency trading company.
[729.22 → 739.02] And as I think everybody can imagine, shaving off a single CPU cycle is a competitive advantage to them.
[739.02 → 739.30] Right.
[739.74 → 749.06] And even in those kinds of environments, they were telling us that like they love how we're going the extra mile and doing continuous profiling.
[749.06 → 754.66] But they would already be happy with profiling products that just made it easier to do profiling.
[754.78 → 754.92] Right.
[755.02 → 757.60] So we're kind of doing multiple things there.
[757.70 → 757.86] Right.
[757.90 → 760.40] Like we're doing exactly that, like you already said.
[760.58 → 769.14] And then we're also going that extra step of actually giving them performance data of all time and not just a single point in time.
[769.14 → 769.54] Yeah.
[770.08 → 776.12] And just as we've shown in episode 33, there's even like a pull request that goes with it.
[776.80 → 778.04] It's anyone can take this.
[778.14 → 779.76] If you have Kubernetes, it's super simple.
[780.10 → 781.80] One command, and you have it.
[782.16 → 783.12] That's all it takes.
[783.40 → 784.84] And it's open source.
[785.30 → 795.02] You're free to, you know, do like look at it, contribute to it, you know, make it your own, whatever you want to do with it, because it's such an important piece of technology, I think.
[795.02 → 801.18] So speaking of which, I've noticed straight off the bat, your website.
[801.60 → 801.78] Yeah.
[801.96 → 804.66] And I think like, wow, like parka.dev.
[805.26 → 807.26] I really like the new website.
[807.42 → 816.84] Like tell us a little bit about that, because I haven't seen such a big change, such a positive change happen, like in just like within a couple of months.
[817.14 → 818.48] What's the story behind it?
[818.48 → 826.76] Honestly, that has very little to do with our team and has all to do with the really incredible team at Pixel Point.
[827.26 → 835.22] So they're like a web consultancy, but I had known them through, like I got to know them through some other open source projects.
[835.54 → 838.54] So they did the website for the K6 project.
[838.72 → 841.08] They did the website for drone.
[841.66 → 842.10] Cilium.
[842.48 → 843.22] Yes, Cilium.
[843.22 → 855.02] I think even maybe even the EPF website, I'm not 100% sure, but basically they've become kind of the web consultancy for open source projects and like deep tech projects.
[855.78 → 867.60] And so I was really excited to kind of just reach out to them and see if they're interested in a project like this and working with us, because we felt like, you know, we needed a makeover for the parka.dev website.
[867.60 → 871.56] And they are just absolutely mind-blowing amazing.
[871.92 → 879.56] Like they, they really tried to understand what parka does and they themselves got really excited about it.
[879.64 → 879.80] Right.
[879.96 → 891.68] That of course is a bonus, but because they tried so hard to actually understand what parka does, they were able to tell the story really amazingly.
[891.68 → 894.46] And then they're also just brilliant designers, you know?
[894.46 → 894.90] Yeah.
[895.26 → 904.16] I want to give a huge shout-out to Pixel Point because I rarely see a website that I think captures something as well as parka.parka.dev does.
[904.40 → 905.78] I really like the story.
[905.90 → 913.60] I mean, I knew parka, but it just basically opened it up like in ways which I was like, surprisingly, they were surprising to me.
[914.16 → 916.88] And even like the screenshots, they got them spot on.
[917.36 → 921.84] Like how it works, why it's important, all that good stuff.
[922.28 → 923.04] Good job, Pixel Point.
[923.24 → 923.92] Good job.
[923.92 → 926.44] Actually, it's a funny, funny thing.
[926.98 → 935.38] One of the things that actually kind of went the other way was we did the screenshots, and they were like, can we edit the screenshots to look prettier?
[935.54 → 935.70] Right.
[935.74 → 940.12] And we were like, I don't think that's being genuine to our users or potential users.
[940.28 → 940.46] Right.
[940.68 → 950.54] And so what happened was they made the edits to the screenshots, and then we actually implemented those changes in parka so that it would actually look that way.
[950.58 → 950.74] Right.
[950.74 → 953.42] And then it kind of, then we did real screenshots again.
[953.66 → 954.20] Oh, wow.
[954.20 → 961.06] And so that was a cool collaboration that I think, you know, unless you ask about it, you don't really find out.
[961.18 → 967.28] But like aside from the website, they actually also influenced the way that parka looks today.
[967.28 → 976.08] So I'm really glad you mentioned that because when I looked at the new websites, and I've seen the flame graphs, my first thought was, hang on, they didn't look like this.
[976.28 → 978.32] Like they are like, is this real?
[978.42 → 979.50] Like, has this actually happened?
[980.16 → 982.98] Ran the update, check the new flame graphs.
[982.98 → 984.26] And they're exactly the same.
[984.44 → 987.66] And I remember that we talked about this around episode 33.
[987.66 → 994.14] And I was thinking, hmm, that's one thing which could do with some improving because it's a bit difficult to understand certain things.
[994.84 → 999.20] Still, you know, huge improvement over what we had before, but, you know, not as easy as it could be.
[999.54 → 1000.76] And it was great to see.
[1000.82 → 1002.56] That's one of the first things which I've noticed.
[1002.98 → 1006.58] The other thing which I noticed is your favourite Easter egg.
[1007.08 → 1008.98] Can you tell us a bit about it?
[1009.46 → 1010.82] Yeah, yeah, this is awesome.
[1010.82 → 1013.40] I mean, it's kind of a design gimmick, right?
[1013.50 → 1019.48] But I think it's really cool that like we talked already about parka and the relationship to EPF.
[1019.88 → 1023.42] And like EPF has this bee as a logo, right?
[1023.52 → 1032.72] And as you scroll through the website, the bee kind of flies through the picture and like out of the website, which I think is, I love that detail.
[1033.20 → 1036.50] I'm disappointed if a website doesn't have an Easter egg.
[1036.50 → 1041.46] I think Chain Guard spoiled it for us with like the hair on various people.
[1041.94 → 1043.42] I mean, now I'm looking for Easter eggs.
[1043.78 → 1046.14] And I think changelog.com needs an Easter egg too.
[1046.60 → 1048.98] If Jared is listening to this, that's okay.
[1049.10 → 1050.92] And if not, I'll mention it in our next Kaiden.
[1051.12 → 1052.86] But Easter eggs are so important.
[1053.00 → 1060.40] They just, you know, like play and, you know, having a bit of fun is so important because our day to day, it's hard enough as it is.
[1060.54 → 1061.62] Let's be honest about it.
[1061.62 → 1065.04] So every little opportunity to have a bit of fun, I think we should seize it.
[1065.58 → 1067.68] And, you know, that's how I think of Easter eggs.
[1067.68 → 1082.94] This episode is brought to you by our friends at Fire Hydrant.
[1083.14 → 1086.00] Fire Hydrant is the reliability platform for every developer.
[1086.42 → 1089.68] Incidents, they impact everyone, not just Sees.
[1089.68 → 1098.08] They give teams the tools to maintain service catalogues, respond to incidents, communicate through status pages, and learn with retrospectives.
[1098.46 → 1107.38] What would normally be manual error-prone tasks across the entire spectrum of responding to an incident, they can all be automated in every way with Fire Hydrant.
[1107.38 → 1112.70] They have incident tooling to manage incidents of any type with any severity with consistency.
[1113.24 → 1116.36] Declare and mitigate incidents all from inside Slack.
[1116.76 → 1123.08] Service catalogues allow service owners to improve operational maturity and document all your deployments in your service catalogue.
[1123.68 → 1131.04] Incident analytics allow you to extract meaningful insights about your reliability over any facet of your incident or the people who respond to them.
[1131.04 → 1140.82] And at the heart of it all, incident run books, they let you create custom automation rules, convert manual tasks into automated, reliable, repeatable sequences that run when you want.
[1141.20 → 1145.20] You can create Slack channels, Jira tickets, Zoom bridges instantly after declaring an incident.
[1145.72 → 1148.26] Now your processes can be consistent and automatic.
[1148.74 → 1150.40] The next step is to try it free.
[1150.54 → 1154.92] Small teams, up to 10 people, can get started for free with all Fire Hydrant features included.
[1155.24 → 1156.66] No credit card is required.
[1157.10 → 1159.28] Get started at firehydrant.io.
[1159.28 → 1161.58] Again, firehydrant.io.
[1172.98 → 1179.08] So I think that you can almost anticipate this question because I think I asked it last time.
[1179.34 → 1182.36] Do you use Parka, profileparka.dev?
[1182.60 → 1183.54] All the time.
[1184.18 → 1184.60] Nice.
[1184.60 → 1185.40] All the time, yes.
[1185.92 → 1188.50] So specifically our demo cluster.
[1188.50 → 1196.64] So if you go to demo.parka.dev, that's Parka profiling itself, but also the Parka agent profiling itself.
[1196.76 → 1197.90] So it's all super meta.
[1198.54 → 1203.14] And actually we have like a Prometheus setup that is monitoring it as well.
[1203.72 → 1213.02] And so all of this we're kind of using to do improvements all the time and to figure out whether the improvements that we're doing actually make sense and have the desired effect.
[1213.02 → 1214.02] I think that's important.
[1214.02 → 1214.28] I think that's so important.
[1214.52 → 1219.96] Gooding your own product and the thing that you're working on in this case, like your open source.
[1220.28 → 1221.22] Would you call it a product?
[1221.36 → 1223.58] Would you say Parka is a product or a project?
[1223.62 → 1224.62] Parka is the project.
[1225.16 → 1227.04] And then Polar Signal Cloud is the product.
[1227.04 → 1227.40] Right.
[1227.60 → 1234.32] So Parka, the open source project, using it and seeing the improvements and like even for itself, it's so important.
[1234.72 → 1239.78] But I have noticed this blog post about profiling Next.js apps with Parka.
[1239.98 → 1244.36] And that made me think, oh, hang on, you know, there must be something more to it.
[1244.44 → 1250.00] And I know that parka.dev runs on Tercel, which is the Next.js company.
[1250.00 → 1255.20] And in that case, I was thinking you must be doing something with the website as well.
[1255.36 → 1256.94] I haven't seen that in the demo.
[1257.24 → 1258.44] Maybe I wasn't paying enough attention.
[1258.72 → 1262.88] But the fact that it's the live, is it for the website itself as well?
[1263.06 → 1263.20] Okay.
[1263.32 → 1268.74] So parka.dev itself is a 100% aesthetic website that's hosted on Tercel.
[1269.16 → 1272.08] So that we're not profiling, though.
[1272.40 → 1277.84] Maybe we can partner with Tercel one day and profile all the applications there.
[1277.84 → 1280.08] That's not something that we're doing today.
[1280.40 → 1284.08] But actually, Polar Signals Cloud is Next.js.
[1284.48 → 1287.04] And that we're profiling with Parka.
[1287.30 → 1288.60] And is that what the demo does?
[1288.84 → 1292.98] No, that's just our like internal Polar Signals Cloud project.
[1293.10 → 1294.92] I've noticed that it runs on K3S.
[1295.28 → 1296.52] Is it Vivo by any chance?
[1296.82 → 1297.56] It's Vivo, yeah.
[1297.96 → 1298.42] Nice.
[1298.54 → 1298.80] Okay.
[1298.92 → 1299.84] I can see it.
[1300.02 → 1300.64] I can see it.
[1301.16 → 1301.98] That was really nice.
[1301.98 → 1303.14] Click on the demo.
[1303.14 → 1310.34] And I was like, I was wanting to know more about it, where it runs, how it's set up, what is being profiled.
[1310.76 → 1315.50] And I'm glad that you mentioned all those things, because now it just makes a lot more sense in my head.
[1315.78 → 1320.32] So the other thing, which I'm just reading around and, you know, doing a bit of research,
[1320.72 → 1328.72] I've seen you mention that Matthias recently fixed some things in the Polar Signals IO pipeline, the continuous delivery pipeline.
[1328.72 → 1332.26] So six minutes from PR to dry run.
[1333.16 → 1333.78] Yeah, yeah.
[1333.78 → 1334.90] This is pretty exciting.
[1334.90 → 1335.40] In the K2S cluster.
[1335.76 → 1337.24] How does this relate to Parka?
[1337.34 → 1339.32] I don't think this is parka.dev, right?
[1339.36 → 1341.92] This is just for the agent, for the server.
[1342.22 → 1344.78] This is the like Polar Signals Cloud product.
[1345.08 → 1350.42] So basically, like we have a mono repo that runs, that kind of contains all of Polar Signals Cloud.
[1350.42 → 1361.14] And within that repo, we now have from like opening the PR to doing a dry run apply to our Kubernetes cluster within six minutes.
[1361.14 → 1369.38] So that includes like building all the container images, running like previews of the UI, all of these things, everything in six minutes.
[1369.54 → 1374.74] So in six minutes, you can basically try out your change in a like staging like environment.
[1374.74 → 1382.60] And it will tell you when you merge this pull request, this is the changes that we're going to be applying to the production Kubernetes cluster.
[1382.96 → 1383.18] Okay.
[1383.44 → 1383.74] Okay.
[1384.34 → 1390.70] So I'm just trying like in my head to imagine how do you view if the changes are positive or negative?
[1391.00 → 1393.28] So do you look at the profiles?
[1393.88 → 1396.36] Do you have some, how does that work?
[1396.80 → 1399.58] To see if the change that you're rolling out is a good one.
[1399.58 → 1405.74] So in this case, it was just that we did much more aggressive caching in our like builds.
[1406.00 → 1411.80] So here it was really just seeing whether the total runtime was less than what we had before.
[1411.98 → 1417.48] But that was like, that was very noticeable because before it was like 26 minutes.
[1417.48 → 1417.78] Okay.
[1417.78 → 1422.42] And after doing some very aggressive caching, we got down to six minutes.
[1422.78 → 1423.06] Okay.
[1423.34 → 1425.26] So yeah, what runs the CI CD?
[1425.46 → 1426.36] Is it GitHub Actions?
[1426.74 → 1427.56] And what is the caching?
[1428.14 → 1428.40] Okay.
[1428.40 → 1445.92] We just do like, so previously we did, we did most of our caching through like Docker layers, but we ran into a couple of issues with that where I wasn't, I don't remember exactly anymore what the problem was, but there were some permission issues, and we couldn't figure out why that was happening.
[1445.92 → 1453.96] And the saving and the saving and the saving and the saving and the saving and the saving and loading of Docker caches was actually taking longer than running the builds.
[1454.52 → 1459.14] And so we decided we're not going to do the actual build within the Docker files anymore.
[1459.32 → 1465.00] We're going to do like, because we have a hundred percent static, statically linked go binaries.
[1465.00 → 1468.50] That's all that fuller signals cloud is made up of.
[1468.72 → 1476.10] So we're building the statically linked binaries before, and then we just put those into a container, into containers.
[1476.68 → 1482.40] And so basically all we're doing is we're using the go caching from GitHub Actions now.
[1482.92 → 1483.26] I see.
[1483.46 → 1483.82] I see.
[1483.92 → 1484.08] Okay.
[1484.18 → 1487.26] So it's, I think you're thinking about the build kit caching.
[1487.26 → 1493.78] So the build kit caching integration with the GitHub Actions cache is slower than actually running the commands.
[1494.48 → 1498.62] And I have seen this before, and there's like a great story for another time behind that.
[1499.28 → 1503.72] And Eric is someone that I work with, and he's one of the build kit core maintainers.
[1504.04 → 1507.22] And, you know, he's well aware of this, and he's, he's working towards a solution.
[1507.66 → 1509.56] But I know what you mean.
[1509.82 → 1516.58] I know that sometimes using the layer caching, the build kit layer caching with GitHub Actions can be slower for sure.
[1516.58 → 1516.98] Okay.
[1517.64 → 1518.34] That makes sense.
[1518.80 → 1523.18] So where do you build those binaries that go, the statically linked go binaries?
[1523.42 → 1526.02] Those we build just through normal GitHub Actions.
[1526.04 → 1526.26] Okay.
[1526.42 → 1534.68] And like beforehand, we load the go mod cache from previous runs, and then we save the cache if it changes.
[1535.02 → 1535.36] Okay.
[1535.56 → 1536.38] Yeah, that makes sense.
[1536.48 → 1536.70] Okay.
[1536.88 → 1537.46] I can see that.
[1537.96 → 1542.44] So in six minutes, you get your change out in the staging cluster.
[1542.44 → 1543.84] And then what happens afterwards?
[1544.20 → 1545.74] I mean, then people review it.
[1545.74 → 1550.26] The cool thing is because we also run like previews on Tercel.
[1550.54 → 1554.98] Basically, you can try out the entire pull request after six minutes, right?
[1555.04 → 1564.42] Like we've got like the UIs that can either be pointed at different versions of the API or even the like production API.
[1564.42 → 1568.86] Because, you know, most of the time, it's either or, right?
[1568.88 → 1572.74] Like a pull request that only does change to the front end.
[1573.34 → 1578.14] And in that case, it's actually nicer if you can just use production data immediately.
[1578.78 → 1579.56] So yeah.
[1579.56 → 1579.60] Yeah.
[1579.90 → 1584.64] And then if it's approved and merged, then within the next six minutes, it's going to be deployed.
[1584.90 → 1585.12] Nice.
[1585.48 → 1587.08] How many deploys do you do per day?
[1587.14 → 1588.62] Because this sounds very efficient.
[1589.00 → 1589.84] You must be doing a lot.
[1590.12 → 1590.28] Yeah.
[1590.34 → 1593.04] I mean, it depends on what people are working on.
[1593.12 → 1596.46] But like we can easily do tens of deploys if we want to.
[1596.46 → 1597.50] So that's very nice.
[1597.62 → 1598.96] That makes a huge difference.
[1599.14 → 1608.80] Being able to make small changes, try them out in the final place where they will run, gaining that confidence and then just, you know, saying, yep, this looks good to me.
[1608.80 → 1613.32] And then, you know, a few minutes later, in this case, several minutes later, you have it.
[1613.58 → 1613.78] Nice.
[1614.22 → 1617.86] Have you ever found yourself in a situation where you have to roll back?
[1618.28 → 1622.92] A change had unexpected consequences in production that were not visible in staging?
[1623.46 → 1623.80] Absolutely.
[1623.80 → 1627.46] That's where kind of another really cool piece comes into play.
[1627.88 → 1639.92] So one of my colleagues, I think you mentioned Matthias already, he built a really cool tool called IRA, which is for planning, but also maintaining and kind of tracking Los.
[1640.26 → 1644.18] And all of our APIs have Los through IRA.
[1644.18 → 1652.78] And so when we have a genuine user impact through a merge, then we get notified within, you know, a couple of minutes.
[1653.18 → 1655.38] And then we can easily roll back the change.
[1655.58 → 1664.72] And at worst, we have the time that it took to alert us, which is usually somewhere between five and 10 minutes if, you know, there's a really drastic problem.
[1664.72 → 1666.16] And then we roll back.
[1666.28 → 1673.28] So turn around 16 to 20 minutes until we would have rolled back a severe change.
[1673.28 → 1675.28] That sounds like a very nice setup.
[1675.90 → 1676.88] Very, very nice.
[1677.06 → 1685.30] I bet it must be so nice working with all this tooling that's like you mostly built, and you understand how everything fits together.
[1685.30 → 1689.10] And you have like a very nice and efficient system of getting changes out.
[1689.10 → 1695.96] And if something, I don't want to say breaks, if something, you know, behaves unexpectedly, you can go back, and you can see when that happens.
[1696.46 → 1699.96] So I know that you mentioned IRA last time that we talked.
[1700.10 → 1704.16] I don't remember how much of it made it in the final conversation in the episode.
[1704.98 → 1707.26] But can you tell us a bit more about it?
[1707.58 → 1709.50] And how is it coming along since we last?
[1709.60 → 1711.10] Because I remember you mentioning it.
[1711.16 → 1714.36] I was excited about it, but I didn't have time to follow up on that.
[1714.36 → 1723.44] So I highly recommend actually that you do an episode with Matthias because he's much more qualified to talk about it than I am because I'm just a user.
[1723.90 → 1728.14] Matthias is the creator, and he just does everything around that project.
[1728.52 → 1731.28] And really, it's not anything that we do at Polar Signals.
[1731.32 → 1733.66] It's just something he's also passionate about.
[1734.12 → 1737.22] And so, you know, it made its way into Polar Signals infrastructure.
[1738.00 → 1739.30] And it's an amazing tool.
[1739.30 → 1745.30] Like, I find myself not going to, like, Prometheus Alert Manager or even Prometheus.
[1745.64 → 1759.12] When I get a page, my first thing, the first thing I do is I hop into IRA and see, like, what my, like, error rate, error budget burn rate is and how severe this change is actually affecting my users.
[1759.78 → 1768.40] So IRA itself is, like I said, a tool to manage Los essentially, specifically for Prometheus setups.
[1768.40 → 1770.42] It doesn't integrate into anything else.
[1770.86 → 1773.58] And that's just because that's the only tool that we use.
[1774.24 → 1781.50] But with IRA, you can kind of say, I have this GRPC API that I have metrics for in Prometheus.
[1781.90 → 1786.26] And I have this goal of, like, three nines, right?
[1786.30 → 1788.66] Like 99.9 or 99.95.
[1788.66 → 1794.30] And then IRA will automatically generate multi-window error burn rates.
[1794.62 → 1796.38] So this is a very long term.
[1796.94 → 1808.54] And there's a lot of theory behind this why these alerts are better than, like, a normal threshold of, like, 1% or 0.1% error rate is happening right now.
[1808.54 → 1816.02] Because we don't really care if that error rate happens once and just spikes for a very brief second, right?
[1816.14 → 1825.80] We actually care about are we going to fulfill our promise to our users over the next 30 days or within the last 30 days, right?
[1825.80 → 1835.98] And so we really only want to get paged if we are in danger of violating that kind of contract that we have with our users, right?
[1835.98 → 1843.58] And so multi-error burn rates essentially calculate how quickly are we burning our error budget.
[1844.36 → 1849.06] And if we continue at this rate, are we going to run out of error budget?
[1849.40 → 1856.82] So essentially, when are we going to get to that point where we are violating that contract we have with our users?
[1856.82 → 1869.18] So that's essentially, IRA allows you to efficiently manage those, but also is just much smarter than I am, for example, to generate those Prometheus alerts.
[1869.38 → 1875.72] Because there's a lot of math behind this that you really need to understand pretty deeply to do useful alerts.
[1876.06 → 1883.38] And Matthias has spent countless hours studying this and really implementing something unique with IRA.
[1883.38 → 1886.50] All right. That's a conversation that I'm really looking forward to.
[1886.82 → 1888.30] Thank you for mentioning it.
[1888.44 → 1893.28] I remember last time when, again, we just briefly talked about it, but the focus was something else.
[1893.52 → 1900.78] Now that you mention it again, this comes up and there's a demo.IRA, P-Y-R-R-A.dev.
[1901.18 → 1904.58] That's fascinating. It's pira.dev on GitHub.
[1905.32 → 1909.62] This is something that, you know, like we have like those projects that people get like ideas.
[1910.02 → 1915.78] They are very excited about for a few months, and then they stop being as excited and then, you know, becomes like abandonedware.
[1915.78 → 1917.54] This doesn't seem to be that.
[1918.00 → 1923.32] And I really like that, you know, like a lot of interest is on this.
[1923.48 → 1928.20] Like you're using it, you're seeing the benefits of its longer term, more than a few months.
[1928.44 → 1930.38] And I'm very curious to see where this goes.
[1930.56 → 1932.46] I think this has some great potential.
[1932.76 → 1935.30] And I like how Matthias is thinking about it for sure.
[1935.88 → 1937.34] So that one's coming up.
[1937.42 → 1939.20] Thank you, Frederick, mentioning that.
[1939.30 → 1943.00] Yeah, I'm sure he'll be happy to do an episode with you.
[1943.00 → 1943.44] Amazing.
[1944.44 → 1947.02] So I'd like us to take this like a half point.
[1947.16 → 1949.26] So I'd like us to do like a conversation cleanser.
[1949.46 → 1951.84] But I would like to talk about the orange farm.
[1952.60 → 1956.30] So I'd like us to tell us more about that orange farm, Frederick.
[1957.68 → 1959.52] What is this orange farm?
[1960.52 → 1966.76] So just before Rubicon EU, we as Polar Signals did our very first in-person offsite.
[1966.76 → 1971.18] So for those who don't know, Polar Signals was founded end of 2020.
[1971.64 → 1974.80] So COVID pandemic was in full swing.
[1975.26 → 1975.62] Oh, yes.
[1975.70 → 1976.42] Full swing, yeah.
[1977.20 → 1980.46] And so we were a fully remote company.
[1980.78 → 1989.56] And up until that point, I, even as the founder, hadn't seen a lot of the people who we ended up hiring at Polar Signals in person.
[1989.56 → 1998.44] And so we spent kind of the entire week before Rubicon together, kind of partly working, doing like hackathons and doing some strategic planning.
[1998.66 → 2002.78] But also, you know, just spending time, some quality time together.
[2003.40 → 2009.22] And yeah, one of the kind of team events that we did was we went to an orange farm in Valencia.
[2009.66 → 2012.02] Because like Rubicon EU was in Valencia.
[2012.28 → 2015.82] And Valencia is famous for their like orange farms.
[2016.40 → 2018.08] And I love orange juice.
[2018.08 → 2020.12] Okay, I can see where this is going.
[2020.32 → 2021.36] I can see where it's going.
[2021.84 → 2025.64] And we went to this really lovely orange farm just outside of Valencia.
[2026.00 → 2035.74] We booked kind of like a private tour on the farm where they kind of taught us through like the history of how like modern day oranges were even developed.
[2036.22 → 2039.94] And like personal history of their family and the orange farm and so on.
[2039.94 → 2044.56] And yeah, we got to like pick oranges right off of the tree.
[2044.88 → 2050.48] And they told us how to actually eat oranges, which apparently I've been doing wrong all my life.
[2050.72 → 2051.46] So how do you do it?
[2051.50 → 2051.88] No, hang on.
[2051.92 → 2052.56] This is important.
[2052.82 → 2054.16] How should you eat oranges?
[2054.16 → 2057.36] So yeah, I didn't know this.
[2057.44 → 2062.18] But essentially, you take the orange with the like stem upwards, right?
[2062.22 → 2063.66] Like the green part upwards.
[2064.04 → 2066.40] And you just kind of bite into it.
[2066.62 → 2070.58] And you kind of bite out the top part of the orange.
[2070.58 → 2073.22] And then you kind of throw that part away.
[2073.46 → 2078.84] And then you can kind of squeeze the orange juice into your mouth and kind of drink it.
[2079.16 → 2084.60] And then once you've squeezed kind of most of it, you kind of just break it open, and then you eat the flesh.
[2085.18 → 2087.78] And you can actually do that without making a mess.
[2088.06 → 2089.00] Like it's mind glowing.
[2089.78 → 2090.22] Okay.
[2090.54 → 2090.90] Wow.
[2091.02 → 2092.68] That sounds like great tips.
[2092.82 → 2093.74] Thank you very much for that.
[2094.20 → 2095.98] And that sounds like a great team activity.
[2095.98 → 2104.54] I know it's really hard to adjust like to the new reality because we always thought like that's like short term, you know, things will come back to normal.
[2104.72 → 2105.86] We'll be back in offices.
[2106.16 → 2107.24] But that hasn't happened.
[2107.64 → 2108.54] I'm not seeing it.
[2109.00 → 2114.04] I think the world has moved on to a new model where most of us are remote.
[2114.48 → 2115.40] There's no office.
[2115.64 → 2119.48] I mean, who would have thought that this will become the norm, especially in the startups.
[2120.10 → 2121.86] And that has so many benefits.
[2121.86 → 2130.34] One of the drawbacks is that you don't get to spend in-person time, quality time with the people that you work with because it makes a huge difference.
[2130.50 → 2135.24] And activities like this just create those bonds, which are so important to a good, healthy team.
[2135.60 → 2139.32] And I'm glad that you're taking every opportunity you can to do that.
[2139.42 → 2142.64] It's so important to build a healthy team and a healthy company.
[2142.82 → 2143.00] Yeah.
[2143.38 → 2144.02] Couldn't agree more.
[2144.36 → 2144.68] Okay.
[2144.68 → 2144.74] Okay.
[2151.86 → 2163.10] This episode is brought to you by Sentry.
[2163.26 → 2164.98] Build better software faster.
[2165.46 → 2169.12] Diagnose, fix, and optimize the performance of your code.
[2169.12 → 2176.24] More than a million developers in 68,000 organizations already use Sentry, and that includes us.
[2176.54 → 2178.04] Here's the easiest way to try Sentry.
[2178.46 → 2181.52] Head to sentry.io slash demo slash sandbox.
[2181.86 → 2185.66] That is a fully functional version of Sentry that you can poke at.
[2186.04 → 2188.80] And best of all, our listeners get the team plan for free for three months.
[2189.10 → 2191.98] Head to sentry.io and use the code changelog when you sign up.
[2192.16 → 2195.50] Again, sentry.io and use the code changelog.
[2195.68 → 2204.84] And by Chromosphere, when it comes to observability, teams need a reliable, scalable, and efficient solution so they can know about issues well before their customers do.
[2205.10 → 2208.44] They need a solution that helps them move faster than the competition.
[2208.44 → 2217.68] And companies born in the cloud-native era often start with Prometheus for monitoring, which is obviously an amazing piece of software, but they quickly push it to its limits and often outgrow it.
[2217.94 → 2226.62] They run into issues with siloed data, missing long-term storage, and wasted engineering time firefighting the monitoring system versus delivering their application with confidence.
[2226.62 → 2234.86] They describe the system as a house of cards where a single developer's seemingly benign change can overload the whole monitoring system.
[2235.12 → 2239.18] Or they say they're flying blind because they pride themselves on making data-driven decisions.
[2239.64 → 2242.86] But losing visibility means they lose this competitive edge.
[2242.86 → 2246.78] Ryan Skol, VP of Engineering at DoorDash, has this to say about Chromosphere.
[2247.18 → 2247.40] Quote,
[2247.76 → 2256.08] The visibility and control that Chromosphere's platform gives us to manage our observability data and costs are a game-changer, especially with our unprecedented growth.
[2256.38 → 2256.72] End quote.
[2257.10 → 2261.44] Chromosphere is the observability platform for cloud-native teams operating at scale.
[2261.86 → 2264.52] Learn more and get a demo at Chronosphere.io.
[2264.86 → 2267.12] Again, Chronosphere.io.
[2267.12 → 2271.12] Chronosphere.io
[2271.12 → 2271.76] Chronosphere.io
[2271.76 → 2272.20] Chronosphere.io
[2272.20 → 2272.24] Chronosphere.io
[2272.24 → 2272.84] Chronosphere.io
[2272.86 → 2278.86] Chronosphere.io
[2278.86 → 2284.92] So, there's another huge thing that happened just before Rubicon, just before Rubicon EU.
[2285.24 → 2290.44] You introduced Arctic DB, and that's what I would like us to talk about next.
[2291.12 → 2297.04] So, what is Arctic DB, and why does the world need something like Arctic DB?
[2297.04 → 2302.62] Yeah, this is something that I've been excited about building for a really long time.
[2302.62 → 2305.54] and I've kind of been thinking about this problem space
[2305.54 → 2306.74] for a really long time.
[2307.26 → 2311.22] So kind of in the name, it's a new database, right?
[2311.40 → 2313.86] It's an embedded database written in Go.
[2314.26 → 2318.82] So maybe listeners are familiar to like Badger DB
[2318.82 → 2323.86] or Level DB or even kind of like Rocks DB
[2323.86 → 2329.48] where you're using it as a library in your application
[2329.48 → 2331.82] to build something around, right?
[2331.82 → 2336.16] I guess S2 Lite is the most classic example of this.
[2336.66 → 2339.46] And Arctic DB is a columnar database.
[2339.78 → 2343.70] So as opposed to many, many other databases
[2343.70 → 2347.16] where let's say in S2 Lite, for example,
[2347.84 → 2350.52] typically the data is stored in rows, right?
[2350.58 → 2353.76] If you insert a new row into your S2 Lite database,
[2354.34 → 2358.38] physically on disk, all the data that belongs to the same row
[2358.38 → 2359.78] are physically co-located.
[2359.78 → 2362.20] That's a row-based database.
[2362.86 → 2364.38] And then a columnar database,
[2364.74 → 2370.42] we store all the values of an entire column co-located.
[2370.88 → 2374.78] And that's really useful when you want to do analytics of the data.
[2375.12 → 2377.92] So if you want to scan an entire column,
[2378.12 → 2380.96] and let's say you want to aggregate it,
[2381.00 → 2382.72] you want to sum all the values in there,
[2382.72 → 2387.32] or you want to do comparisons of strings or something like that.
[2387.32 → 2391.34] It just turns out that the way that computers work,
[2391.56 → 2393.14] that's much more efficient to do
[2393.14 → 2396.12] than doing kind of random access on disk
[2396.12 → 2400.10] and loading individual pieces off of this to do those things.
[2400.10 → 2406.26] And so that's why we, for ARCA, needed a columnar database.
[2406.72 → 2408.94] We kind of realized that pretty early on.
[2409.14 → 2412.82] And I have some kind of prior experience with the Prometheus TSDB,
[2412.98 → 2417.40] which if you squint a lot, is also a columnar database,
[2417.78 → 2421.76] but like highly, highly optimized for the Prometheus use case.
[2421.76 → 2427.28] The one thing that is additionally kind of different in Arctic DB,
[2427.56 → 2430.06] that really there's no other database out there
[2430.06 → 2432.40] that allows you to do something like this,
[2432.82 → 2436.60] which does we have kind of semi-flexible schemas.
[2436.90 → 2440.10] So you can define a schema, and you can say,
[2440.50 → 2444.60] these columns must always be there if you insert a new row.
[2445.02 → 2448.84] But then we also have something that we call dynamic columns.
[2448.84 → 2454.14] And this is specifically useful for kind of label style data,
[2454.28 → 2456.02] similar to what Prometheus has, right?
[2456.12 → 2461.12] We want to be able to attach labels to specific data points
[2461.12 → 2463.36] so that we can then slice and dice data
[2463.36 → 2466.56] by random infrastructure labels, right?
[2466.64 → 2469.52] Like it can be the region of our data centre.
[2469.68 → 2471.38] It can be the name of our data centre.
[2471.48 → 2473.94] It can be our namespace in our Kubernetes cluster.
[2474.08 → 2474.86] It can be our pod.
[2475.06 → 2475.88] It can be our container.
[2476.08 → 2478.50] It can be our process ID, right?
[2478.50 → 2481.66] Like we as Polar Signals don't want to dictate
[2481.66 → 2484.08] how you organize your infrastructure.
[2484.36 → 2486.10] And so we want to give you that flexibility
[2486.10 → 2489.30] to choose the labelling however you like it.
[2489.46 → 2492.12] That philosophy came from Prometheus, right?
[2492.14 → 2493.94] And we felt like that was one of the things
[2493.94 → 2495.64] that made Prometheus really successful.
[2496.26 → 2499.34] And so it's something that we felt like we had to replicate.
[2499.34 → 2506.74] But the nature of profiling data means that we have unique sets of labels
[2506.74 → 2508.74] much more often than Prometheus.
[2509.20 → 2511.98] And this is kind of the classic cardinality problem
[2511.98 → 2514.54] that people run into with Prometheus.
[2514.64 → 2518.48] And there's nothing wrong with Prometheus' design for that, with that, right?
[2518.84 → 2523.64] Prometheus is like not meant for the like undefined,
[2523.80 → 2525.94] unbound cardinality use cases.
[2525.94 → 2528.68] It can actually handle them surprisingly well,
[2529.20 → 2532.38] but it wasn't designed in that way, right?
[2532.54 → 2533.94] Again, nothing wrong with that,
[2534.30 → 2536.82] but continuous profiling needed something different
[2536.82 → 2541.10] because we don't know what stack traces will occur,
[2541.28 → 2543.36] how often they will occur, right?
[2543.48 → 2544.42] That's completely random.
[2544.54 → 2547.10] It depends on what the process is actually executing.
[2547.10 → 2551.62] And so we needed a storage that actually internalizes that
[2551.62 → 2556.14] and where we don't pay a penalty for cardinality.
[2556.76 → 2559.96] And so essentially the way it's done in Arctic DB
[2559.96 → 2563.36] is that every time we see a new label key,
[2563.74 → 2567.86] we dynamically create a new column that is then inserted into
[2567.86 → 2571.66] and everything else just is treated as this column
[2571.66 → 2575.00] is just null basically for all other rows.
[2575.00 → 2577.66] So I'm really glad that you mentioned this
[2577.66 → 2580.16] because cardinality used to keep come up.
[2580.30 → 2582.98] I mean, I'm sure it still does in the context of Prometheus.
[2583.32 → 2586.84] And I know that that had memory implications
[2586.84 → 2589.88] as well as disk implications.
[2590.36 → 2591.80] It would basically use up more memory,
[2592.12 → 2593.64] more disk space to store the data.
[2594.14 → 2597.58] Does it affect Arctic DB in the same way
[2597.58 → 2600.78] when it comes to memory size and disk size?
[2600.88 → 2604.16] Does Arctic DB use more memory and more disk?
[2604.16 → 2605.38] If there are more labels?
[2605.86 → 2609.44] So there's at least one fundamental point here
[2609.44 → 2611.66] that I think I need to point out,
[2611.76 → 2613.88] which is if you have more data,
[2614.12 → 2617.14] then you need to pay for it in some way, right?
[2617.18 → 2620.34] Like there's no such thing as storing data for free, right?
[2620.38 → 2621.72] Like if we're able to do that,
[2621.76 → 2625.46] then I think like the fundamentals of computing change.
[2625.46 → 2625.74] Yeah.
[2626.18 → 2626.54] Okay.
[2627.42 → 2631.62] But the characteristics of paying for cardinality
[2631.62 → 2633.72] are dramatically different.
[2633.92 → 2637.68] In Prometheus, we want to keep series of data alive
[2637.68 → 2638.84] for as long as possible
[2638.84 → 2641.58] because that improves compression.
[2642.20 → 2643.64] And that's ultimately what,
[2644.14 → 2646.14] or one of the pieces that make Prometheus
[2646.14 → 2647.52] as efficient as it is.
[2647.68 → 2649.98] Again, that's why I keep going back to,
[2649.98 → 2652.54] this is a good design for Prometheus
[2652.54 → 2654.68] because it allows Prometheus to exploit
[2654.68 → 2657.34] several pieces of that equation
[2657.34 → 2659.78] to be able to serve things
[2659.78 → 2663.26] like the super low latency queries like Prometheus does.
[2663.26 → 2667.72] In Arctic DB, we're not paying per series.
[2668.20 → 2670.90] We're basically paying per row that we're inserting.
[2670.90 → 2672.72] And the point is,
[2672.96 → 2678.64] we're kind of bringing the cost of inserting a row down so much
[2678.64 → 2680.14] that we don't care anymore
[2680.14 → 2683.76] how many columns we have in that row.
[2684.26 → 2687.20] So it's where basically our penalty is,
[2687.44 → 2689.54] or our cost is at the row level
[2689.54 → 2692.00] as opposed to the cardinality level.
[2692.44 → 2693.10] I see, I see.
[2693.54 → 2694.44] Okay, that makes sense
[2694.44 → 2697.52] because when we used to have lots and lots of labels
[2697.52 → 2699.78] on metrics in Prometheus,
[2699.78 → 2701.86] what used to happen when you would query them,
[2702.40 → 2703.62] you would use a lot of memory.
[2704.42 → 2706.74] So things would take a lot longer.
[2707.16 → 2708.98] And if you wanted to have them optimized,
[2709.48 → 2711.32] you would use, I think, more disk space,
[2711.42 → 2713.10] if I remember correctly, and memory.
[2713.40 → 2716.22] So I'm wondering, like those ad hoc queries,
[2716.42 → 2719.92] which you don't know what labels you'll be querying for.
[2720.04 → 2721.12] So then you just add up.
[2721.70 → 2723.70] I mean, you don't have to declare what the labels are
[2723.70 → 2725.00] because I think it will also like create
[2725.00 → 2726.86] different time series, if I remember correctly.
[2726.90 → 2727.84] This is like all coming back.
[2727.84 → 2730.14] I haven't used it like in maybe, I don't know,
[2730.16 → 2732.20] a year now, give or take six months,
[2732.28 → 2732.90] something like that.
[2733.66 → 2736.34] And the more labels you would have,
[2736.42 → 2738.00] like the more time series you would get.
[2738.46 → 2739.02] Is that right?
[2739.38 → 2739.72] That's right.
[2739.80 → 2742.46] Every unique combination of labels
[2742.46 → 2745.28] identifies a time series in Prometheus.
[2745.56 → 2745.96] That's it.
[2746.16 → 2748.18] And then that is what was resulting
[2748.18 → 2750.22] in that excessive storage
[2750.22 → 2751.80] and excessive memory usage,
[2751.80 → 2753.26] like disk space and memory.
[2753.26 → 2755.22] And if ARCA doesn't do that,
[2755.28 → 2756.72] that's amazing because that means
[2756.72 → 2759.18] like the cost of a label is much,
[2759.28 → 2760.88] much lower than it is in Prometheus.
[2761.28 → 2763.22] As you say, two different systems
[2763.22 → 2765.16] designed for specific use cases,
[2765.42 → 2768.26] but Arctic DB seems to have solved
[2768.26 → 2770.18] this cardinality tackled,
[2770.18 → 2772.26] tackled head on the problem of cardinality,
[2772.40 → 2773.76] which makes a huge difference.
[2773.94 → 2776.72] So does that mean that you can store
[2776.72 → 2779.80] the samples or the profiles that you get
[2779.80 → 2784.40] with arbitrary labels like customer names
[2784.40 → 2786.42] or service names or things like that,
[2786.46 → 2788.06] because that opens up the world
[2788.06 → 2790.78] to a host of new possibilities if you do that.
[2791.10 → 2792.36] Yeah, that's absolutely right.
[2792.44 → 2794.16] And like one of the first things
[2794.16 → 2795.40] that we started implementing
[2795.40 → 2797.32] once we had Arctic DB,
[2797.86 → 2799.04] we haven't released this yet,
[2799.14 → 2800.44] but it's something that I've talked about
[2800.44 → 2801.46] a couple of times already,
[2801.46 → 2805.34] is that we attach a trace ID to a stack trace.
[2805.34 → 2807.36] So that way, what we can do
[2807.36 → 2809.52] is we can pull up all the CPU time
[2809.52 → 2812.56] that was created by a single request,
[2812.74 → 2814.66] right, across services, right?
[2814.78 → 2816.48] Because we have a single trace ID
[2816.48 → 2818.70] that is piped through all of our services.
[2819.02 → 2820.52] Now, this only does work
[2820.52 → 2823.30] if you actually have like
[2823.30 → 2824.98] application level instrumentation
[2824.98 → 2826.28] for profiling as well,
[2826.44 → 2829.02] because the profiler needs to know
[2829.02 → 2831.38] about that trace ID somehow.
[2831.80 → 2833.56] But if you put in that work
[2833.56 → 2834.84] and it's not a lot of work,
[2835.12 → 2835.92] as a matter of fact,
[2835.92 → 2837.10] this can actually be done
[2837.10 → 2839.08] as kind of open telemetry wrapper.
[2839.54 → 2840.00] So you can,
[2840.60 → 2842.74] you only need to kind of install a library
[2842.74 → 2843.46] and then you have
[2843.46 → 2845.04] all of that information automatically.
[2845.48 → 2847.12] And then you can jump from
[2847.12 → 2849.22] like a distributed trace
[2849.22 → 2850.90] to all the profiling data
[2850.90 → 2853.80] associated with that request
[2853.80 → 2854.56] or, you know,
[2854.60 → 2856.12] whatever your trace ID represents.
[2856.62 → 2858.08] So because you mentioned
[2858.08 → 2860.72] how Prometheus is being used for,
[2861.22 → 2862.78] like not as it was designed
[2862.78 → 2863.80] and people abuse it,
[2864.04 → 2864.92] here's a crazy idea.
[2864.92 → 2866.24] And you tell me Arctic DB
[2866.24 → 2867.28] would be abused
[2867.28 → 2868.82] if it was used for this purpose.
[2869.16 → 2869.94] What would happen
[2869.94 → 2871.54] if Arctic DB would be used
[2871.54 → 2872.56] to store events
[2872.56 → 2875.34] with arbitrary labels?
[2875.72 → 2876.42] Would it work?
[2876.80 → 2877.98] That's exactly the use case
[2877.98 → 2878.74] that it's built for.
[2879.12 → 2880.64] Okay, nice.
[2880.76 → 2880.92] Yeah.
[2881.00 → 2881.78] You could absolutely
[2881.78 → 2883.72] use Arctic DB
[2883.72 → 2884.70] to store
[2884.70 → 2886.14] distributed tracing data
[2886.14 → 2887.12] or log data.
[2887.44 → 2887.92] It's not something
[2887.92 → 2888.62] that we're focusing
[2888.62 → 2890.38] on ourselves right now,
[2890.48 → 2891.74] just because, you know,
[2891.74 → 2892.92] it's important for us
[2892.92 → 2894.06] to stay focused on
[2894.06 → 2895.54] continuous profiling.
[2896.18 → 2898.24] But I think the possibilities
[2898.24 → 2899.54] are exciting.
[2900.08 → 2901.46] And like one of the first comments
[2901.46 → 2902.14] that we got
[2902.14 → 2904.00] when we open sourced Arctic DB
[2904.00 → 2905.06] was,
[2905.42 → 2906.28] can we use this
[2906.28 → 2907.14] instead of like
[2907.14 → 2908.54] Prometheus TSDB, right?
[2908.74 → 2909.46] To like solve
[2909.46 → 2911.54] some of the cardinality issues.
[2911.76 → 2912.56] And definitely,
[2912.68 → 2913.58] this is a possibility,
[2913.58 → 2915.16] but also like,
[2915.44 → 2916.50] we need to take it
[2916.50 → 2917.90] with a grain of salt, right?
[2917.96 → 2918.82] Like Arctic DB,
[2918.82 → 2919.74] we open sourced
[2919.74 → 2920.50] at the moment
[2920.50 → 2921.58] it started working.
[2922.18 → 2923.30] And like Prometheus TSDB
[2923.30 → 2925.30] has had seven years
[2925.30 → 2927.12] of performance optimizations,
[2927.90 → 2928.08] right?
[2928.14 → 2929.14] Like I think
[2929.14 → 2929.96] there is
[2929.96 → 2931.12] a possibility
[2931.12 → 2931.94] in the future
[2931.94 → 2932.84] to explore
[2932.84 → 2934.52] that path
[2934.52 → 2935.12] further,
[2935.36 → 2936.14] but it's definitely
[2936.14 → 2937.14] going to take a while
[2937.14 → 2939.12] to get any sort of
[2939.12 → 2940.12] similar performance
[2940.12 → 2940.88] characteristics.
[2941.06 → 2941.62] And like I said,
[2941.98 → 2943.14] Prometheus was specifically
[2943.14 → 2944.14] designed for those
[2944.14 → 2945.28] like super low latency
[2945.28 → 2945.74] queries.
[2946.54 → 2948.16] So the fundamental
[2948.16 → 2949.48] setup
[2949.48 → 2950.66] does mean that
[2950.66 → 2951.56] Prometheus should
[2951.56 → 2953.28] always outperform
[2953.28 → 2953.88] Arctic DB.
[2954.54 → 2955.24] But Arctic DB,
[2955.48 → 2955.94] I think,
[2956.12 → 2956.60] can get
[2956.60 → 2958.26] pretty close
[2958.26 → 2959.16] because of
[2959.16 → 2960.00] a couple of tricks
[2960.00 → 2961.52] that we're doing
[2961.52 → 2962.60] with the data.
[2963.24 → 2964.90] So let me see
[2964.90 → 2965.74] if I got this right.
[2966.22 → 2966.76] Prometheus
[2966.76 → 2967.92] was optimized
[2967.92 → 2968.74] for metrics.
[2969.42 → 2969.96] Arctic DB
[2969.96 → 2971.72] is optimized
[2971.72 → 2972.38] and built
[2972.38 → 2973.40] for events.
[2973.82 → 2974.18] I don't know
[2974.18 → 2974.76] if I would even
[2974.76 → 2975.50] call it events.
[2975.60 → 2976.32] It's really just
[2976.32 → 2977.80] tagged data,
[2977.80 → 2979.52] whatever that
[2979.52 → 2980.26] means to you.
[2980.64 → 2981.60] I wrote
[2981.60 → 2982.02] with a couple
[2982.02 → 2982.42] of people
[2982.42 → 2983.60] who want
[2983.60 → 2984.06] to store
[2984.06 → 2984.94] super high
[2984.94 → 2985.62] cardinality
[2985.62 → 2986.60] data that
[2986.60 → 2987.18] they're grabbing
[2987.18 → 2988.22] from EPF
[2988.22 → 2988.96] and this is
[2988.96 → 2990.00] totally possible
[2990.00 → 2990.34] and there's
[2990.34 → 2992.34] no existing
[2992.34 → 2993.78] type of data
[2993.78 → 2994.92] that could be
[2994.92 → 2996.36] used to describe
[2996.36 → 2996.76] this.
[2996.84 → 2997.40] It's just
[2997.40 → 2998.34] super high
[2998.34 → 2998.96] cardinality
[2998.96 → 3000.18] data that
[3000.18 → 3001.14] you want to
[3001.14 → 3001.92] search by
[3001.92 → 3003.10] a label-based
[3003.10 → 3003.54] system.
[3003.54 → 3004.48] One last
[3004.48 → 3004.82] question
[3004.82 → 3005.38] before we
[3005.38 → 3005.80] move from
[3005.80 → 3006.34] the Arctic
[3006.34 → 3007.08] DB topic.
[3007.38 → 3007.48] Well,
[3007.64 → 3008.08] kind of.
[3009.28 → 3009.66] Is there
[3009.66 → 3010.22] a single
[3010.22 → 3010.94] process of
[3010.94 → 3011.58] Arctic DB?
[3012.00 → 3012.16] I mean,
[3012.26 → 3012.40] okay,
[3012.46 → 3013.06] so first
[3013.06 → 3013.50] of all,
[3013.72 → 3014.58] it is
[3014.58 → 3015.36] embedded.
[3015.98 → 3016.24] That's
[3016.24 → 3016.58] something that
[3016.58 → 3016.98] you mentioned
[3016.98 → 3017.40] and that is
[3017.40 → 3017.70] important.
[3018.38 → 3018.92] Does it
[3018.92 → 3019.90] have any
[3019.90 → 3020.40] primitives
[3020.40 → 3020.68] when it
[3020.68 → 3021.02] comes to
[3021.02 → 3021.46] clustering?
[3021.72 → 3022.00] Does it
[3022.00 → 3022.36] understand
[3022.36 → 3023.12] a cluster
[3023.12 → 3023.94] of processes
[3023.94 → 3024.44] that have
[3024.44 → 3025.12] Arctic DB
[3025.12 → 3025.86] embedded?
[3025.86 → 3027.12] So that's
[3027.12 → 3027.50] something that
[3027.50 → 3028.48] we're building
[3028.48 → 3030.14] for Polar
[3030.14 → 3030.70] Signals Cloud
[3030.70 → 3031.20] right now.
[3031.66 → 3031.90] And it's
[3031.90 → 3032.50] possible that
[3032.50 → 3033.04] we'll open
[3033.04 → 3034.22] sources in
[3034.22 → 3034.62] the future.
[3035.36 → 3036.22] The reality
[3036.22 → 3036.82] is just
[3036.82 → 3037.42] we're a
[3037.42 → 3037.70] business.
[3037.84 → 3038.12] We need to
[3038.12 → 3038.40] at some
[3038.40 → 3038.84] point start
[3038.84 → 3039.36] making some
[3039.36 → 3039.86] money, right?
[3040.42 → 3041.08] So it's just
[3041.08 → 3041.60] something that
[3041.60 → 3042.26] we haven't
[3042.26 → 3042.66] spent too
[3042.66 → 3043.12] much time
[3043.12 → 3043.36] on.
[3043.58 → 3043.82] But it's
[3043.82 → 3045.64] definitely a
[3045.64 → 3046.26] path that
[3046.26 → 3046.64] we want to
[3046.64 → 3047.16] keep open.
[3047.60 → 3048.54] And I think
[3048.54 → 3049.42] it's inevitable
[3049.42 → 3049.94] that we'll
[3049.94 → 3050.56] probably do
[3050.56 → 3051.28] this eventually.
[3051.72 → 3052.12] Like I said,
[3052.20 → 3052.50] it's just
[3052.50 → 3052.96] something that
[3052.96 → 3053.92] we purely
[3053.92 → 3054.68] need in
[3054.68 → 3055.22] order to run
[3055.22 → 3055.54] Polar
[3055.54 → 3056.16] Signals Cloud
[3056.16 → 3056.94] today.
[3057.08 → 3057.38] So that's
[3057.38 → 3057.68] why we're
[3057.68 → 3058.20] building it.
[3058.30 → 3058.58] And then
[3058.58 → 3059.02] we'll see
[3059.02 → 3059.44] what we'll
[3059.44 → 3060.04] do with it
[3060.04 → 3061.10] potentially in
[3061.10 → 3061.76] the open
[3061.76 → 3063.00] source community.
[3063.62 → 3064.08] Before we
[3064.08 → 3065.16] talk about
[3065.16 → 3065.84] the Polar
[3065.84 → 3066.50] Signals Cloud,
[3066.90 → 3067.84] I would like
[3067.84 → 3069.52] to cover
[3069.52 → 3069.96] some of the
[3069.96 → 3070.44] shoutouts
[3070.44 → 3071.04] for Arctic
[3071.04 → 3071.38] DB.
[3071.58 → 3072.08] Because I've
[3072.08 → 3072.40] seen that
[3072.40 → 3072.56] you've
[3072.56 → 3072.90] collaborated
[3072.90 → 3073.40] with a
[3073.40 → 3073.74] lot of
[3073.74 → 3074.22] people on
[3074.22 → 3074.50] this.
[3075.06 → 3075.62] So it's
[3075.62 → 3075.98] not just
[3075.98 → 3076.72] you coming
[3076.72 → 3077.20] up with a
[3077.20 → 3077.90] crazy idea
[3077.90 → 3078.84] and seeing
[3078.84 → 3079.24] how it
[3079.24 → 3079.36] works.
[3079.36 → 3081.06] So you
[3081.06 → 3081.44] mentioned
[3081.44 → 3082.08] some amazing
[3082.08 → 3082.54] people.
[3083.04 → 3083.42] The one
[3083.42 → 3083.80] which I would
[3083.80 → 3084.04] like to
[3084.04 → 3084.46] start with
[3084.46 → 3084.96] is
[3084.96 → 3085.54] Tyler
[3085.54 → 3085.94] Neely.
[3086.10 → 3086.32] I didn't
[3086.32 → 3086.88] even know
[3086.88 → 3087.68] about him
[3087.68 → 3088.14] until you
[3088.14 → 3088.42] mentioned
[3088.42 → 3088.66] him.
[3089.02 → 3089.48] He's been
[3089.48 → 3089.86] building
[3089.86 → 3090.82] Rust databases
[3090.82 → 3092.40] since 2014.
[3093.14 → 3093.72] SLED and
[3093.72 → 3094.06] Rio.
[3094.62 → 3095.42] So he has a
[3095.42 → 3095.80] lot of
[3095.80 → 3096.30] experience.
[3096.30 → 3096.56] I was
[3096.56 → 3097.38] watching one
[3097.38 → 3097.64] of his
[3097.64 → 3098.34] Foster talks
[3098.34 → 3099.02] from 2020.
[3100.02 → 3100.70] He's smart.
[3100.70 → 3103.70] genius smart.
[3103.70 → 3105.44] So tell us
[3105.44 → 3105.86] more about
[3105.86 → 3106.24] the people
[3106.24 → 3106.60] that you
[3106.60 → 3107.22] collaborated
[3107.22 → 3108.24] on Arctic
[3108.24 → 3108.52] DB.
[3108.72 → 3108.90] At least
[3108.90 → 3109.50] the ideas.
[3109.98 → 3110.84] Let's start
[3110.84 → 3111.26] with Tyler
[3111.26 → 3111.70] actually.
[3112.20 → 3112.96] I've known
[3112.96 → 3113.98] Tyler for
[3113.98 → 3115.36] six years,
[3115.48 → 3115.98] seven years
[3115.98 → 3116.30] almost.
[3116.76 → 3117.42] He actually
[3117.42 → 3118.34] rented a
[3118.34 → 3118.88] desk from
[3118.88 → 3119.30] us at
[3119.30 → 3119.74] CoreOS
[3119.74 → 3120.38] Times in
[3120.38 → 3120.56] the
[3120.56 → 3121.90] Berlin office.
[3122.74 → 3124.54] He has
[3124.54 → 3125.06] some history
[3125.06 → 3126.14] at Mesosphere
[3126.14 → 3126.76] building,
[3126.96 → 3127.52] working on
[3127.52 → 3128.34] Zookeeper as
[3128.34 → 3128.66] well.
[3128.66 → 3130.86] Any
[3130.86 → 3131.58] crazy
[3131.58 → 3132.86] distributed
[3132.86 → 3133.78] system or
[3133.78 → 3135.32] high-performance
[3135.32 → 3136.52] databases that
[3136.52 → 3137.02] you can think
[3137.02 → 3137.60] of, he's
[3137.60 → 3138.52] had his
[3138.52 → 3139.24] hands on
[3139.24 → 3139.90] somehow.
[3140.90 → 3141.56] I'm just
[3141.56 → 3142.20] also friends
[3142.20 → 3142.90] with Tyler.
[3143.02 → 3143.48] I like to
[3143.48 → 3144.14] go for a
[3144.14 → 3144.58] coffee with
[3144.58 → 3144.90] him or
[3144.90 → 3145.24] something.
[3146.00 → 3146.62] We just
[3146.62 → 3147.10] have common
[3147.10 → 3147.54] interests.
[3147.92 → 3148.36] I was
[3148.36 → 3149.58] talking to
[3149.58 → 3149.98] him that
[3149.98 → 3150.68] we're
[3150.68 → 3151.24] thinking about
[3151.24 → 3151.74] building this
[3151.74 → 3153.18] new database
[3153.18 → 3154.26] with these
[3154.26 → 3154.90] characteristics.
[3155.46 → 3156.28] I'm not
[3156.28 → 3157.14] sure about
[3157.14 → 3158.20] our model
[3158.20 → 3159.18] for transactions.
[3159.50 → 3160.06] We just
[3160.06 → 3161.54] spent several
[3161.54 → 3163.06] hours together
[3163.06 → 3163.80] discussing
[3163.80 → 3164.86] various
[3164.86 → 3166.38] isolation and
[3166.38 → 3167.30] consistency
[3167.30 → 3167.88] mechanisms.
[3168.68 → 3169.24] Ultimately,
[3169.48 → 3169.70] what we
[3169.70 → 3170.04] ended up
[3170.04 → 3170.46] implementing
[3170.46 → 3171.40] is 100%
[3171.40 → 3172.44] his idea.
[3173.00 → 3173.66] Like I
[3173.66 → 3173.84] said,
[3174.04 → 3175.22] sure, we
[3175.22 → 3175.56] might have
[3175.56 → 3176.00] written the
[3176.00 → 3176.78] code, but
[3176.78 → 3177.96] Tyler was
[3177.96 → 3178.46] the person
[3178.46 → 3178.84] who came
[3178.84 → 3179.24] up with
[3179.24 → 3179.90] the mechanism.
[3180.84 → 3182.00] Huge shout
[3182.00 → 3183.00] out to him
[3183.00 → 3183.52] for that.
[3184.02 → 3184.54] I guess the
[3184.54 → 3185.34] next one we
[3185.34 → 3185.62] definitely
[3185.62 → 3186.26] need to
[3186.26 → 3187.14] mention
[3187.14 → 3188.72] are Paul
[3188.72 → 3189.80] Dix and
[3189.80 → 3190.26] Andrew
[3190.26 → 3191.00] Lam from
[3191.00 → 3192.38] InfluxDB.
[3192.88 → 3193.46] Basically,
[3193.66 → 3194.30] they're building
[3194.30 → 3195.02] something very
[3195.02 → 3195.82] similar in
[3195.82 → 3196.14] Rust.
[3196.40 → 3196.68] Actually,
[3196.76 → 3197.08] they've been
[3197.08 → 3197.50] building it
[3197.50 → 3197.84] for much
[3197.84 → 3198.32] longer than
[3198.32 → 3198.82] we have.
[3200.04 → 3202.00] They were
[3202.00 → 3204.24] vital and
[3204.24 → 3205.04] they were
[3205.04 → 3205.72] very generous
[3205.72 → 3206.26] in sharing
[3206.26 → 3207.16] their experience
[3207.16 → 3207.98] of what
[3207.98 → 3208.20] they're
[3208.20 → 3208.54] building,
[3208.70 → 3209.02] which is
[3209.02 → 3210.00] InfluxDB
[3210.00 → 3210.58] Box.
[3210.70 → 3211.28] It's their
[3211.28 → 3212.32] next generation
[3212.32 → 3213.74] columnar database
[3213.74 → 3214.74] that's going
[3214.74 → 3216.20] back all
[3216.20 → 3216.58] of the
[3216.58 → 3217.02] Influx
[3217.02 → 3217.62] cloud
[3217.62 → 3218.08] product.
[3218.48 → 3218.78] They
[3218.78 → 3219.42] have
[3219.42 → 3219.72] something
[3219.72 → 3220.38] similar
[3220.38 → 3220.80] with the
[3220.80 → 3221.18] dynamic
[3221.18 → 3221.78] columns.
[3222.10 → 3222.26] They're
[3222.26 → 3222.94] building
[3222.94 → 3223.52] on top
[3223.52 → 3224.14] of Apache
[3224.14 → 3224.80] Arrow and
[3224.80 → 3225.14] Apache
[3225.14 → 3225.60] Parquet.
[3226.06 → 3226.60] A lot
[3226.60 → 3226.92] of the
[3226.92 → 3227.46] foundational
[3227.46 → 3228.26] pieces are
[3228.26 → 3228.74] extremely
[3228.74 → 3229.18] similar.
[3229.76 → 3230.20] Like I
[3230.20 → 3230.36] said,
[3230.44 → 3230.68] they were
[3230.68 → 3230.98] super
[3230.98 → 3231.38] generous
[3231.38 → 3231.72] in
[3231.72 → 3232.32] sharing
[3232.32 → 3232.54] their
[3232.54 → 3232.98] experience
[3232.98 → 3233.30] because
[3233.30 → 3233.66] we
[3233.66 → 3234.06] definitely
[3234.06 → 3234.36] would
[3234.36 → 3234.56] not
[3234.56 → 3234.76] be
[3234.76 → 3235.00] here
[3235.00 → 3235.32] this
[3235.32 → 3236.06] soon
[3236.06 → 3236.72] quickly
[3236.72 → 3237.32] in
[3237.32 → 3237.46] this
[3237.46 → 3237.64] kind
[3237.64 → 3237.76] of
[3237.76 → 3238.12] quality
[3238.12 → 3238.34] if
[3238.34 → 3238.88] they
[3238.88 → 3239.16] hadn't
[3239.16 → 3239.48] shared
[3239.48 → 3239.98] all
[3239.98 → 3240.18] of that
[3240.18 → 3240.78] experience.
[3241.04 → 3241.92] This is
[3241.92 → 3242.08] it.
[3242.22 → 3243.02] This is
[3243.02 → 3244.22] the secret
[3244.22 → 3245.10] to great
[3245.10 → 3245.70] teams and
[3245.70 → 3245.92] great
[3245.92 → 3246.90] products and
[3246.90 → 3247.24] great
[3247.24 → 3247.72] open source
[3247.72 → 3248.32] projects.
[3248.82 → 3249.48] Great people
[3249.48 → 3250.22] coming together
[3250.22 → 3251.22] over coffee
[3251.22 → 3253.02] or a meal
[3253.02 → 3254.52] sharing ideas
[3254.52 → 3255.32] and then
[3255.32 → 3256.10] the best
[3256.10 → 3257.26] ones win
[3257.26 → 3258.02] always
[3258.02 → 3258.70] and the
[3258.70 → 3259.22] bad ones
[3259.22 → 3259.62] eventually
[3259.62 → 3260.24] go away.
[3260.74 → 3261.24] There's
[3261.24 → 3261.92] lots and
[3261.92 → 3262.26] lots of
[3262.26 → 3262.92] bad ideas
[3262.92 → 3263.34] and there's
[3263.34 → 3263.84] a lot of
[3263.84 → 3264.14] fun to
[3264.14 → 3264.68] be had
[3264.68 → 3265.88] so they
[3265.88 → 3266.52] are important
[3266.52 → 3267.86] but it's
[3267.86 → 3268.50] always like
[3268.50 → 3269.42] amazing people
[3269.42 → 3270.04] coming together
[3270.04 → 3270.90] and creating
[3270.90 → 3271.58] something amazing
[3271.58 → 3272.18] and then
[3272.18 → 3272.62] putting it
[3272.62 → 3273.02] out there
[3273.02 → 3273.82] and see
[3273.82 → 3274.34] what happens.
[3274.66 → 3275.00] I love
[3275.00 → 3275.26] that.
[3275.54 → 3275.84] He also
[3275.84 → 3276.26] mentioned
[3276.26 → 3276.84] Ackley
[3276.84 → 3277.66] Ackley
[3277.66 → 3278.28] Roussel
[3278.28 → 3278.52] from
[3278.52 → 3278.94] Segment
[3278.94 → 3279.86] and that
[3279.86 → 3280.12] was a
[3280.12 → 3280.82] shout out
[3280.82 → 3281.64] and Julian
[3281.64 → 3282.06] Pivot to
[3282.06 → 3282.54] from the
[3282.54 → 3283.22] Prometheus
[3283.22 → 3283.50] team.
[3283.74 → 3284.04] Yeah so
[3284.04 → 3284.84] I've never
[3284.84 → 3285.58] actually spoken
[3285.58 → 3286.00] to him
[3286.00 → 3286.78] in person
[3286.78 → 3287.84] but I
[3287.84 → 3288.44] spoken to
[3288.44 → 3289.16] other people
[3289.16 → 3289.66] at Segment
[3289.66 → 3290.48] I think
[3290.48 → 3291.10] it's
[3291.10 → 3291.44] pronounced
[3291.44 → 3291.92] Shill
[3291.92 → 3293.34] so Shill
[3293.34 → 3294.36] is an
[3294.36 → 3294.98] incredible
[3294.98 → 3295.52] engineer.
[3296.22 → 3296.98] He's put
[3296.98 → 3297.74] together most
[3297.74 → 3298.78] of the
[3298.78 → 3299.48] Parquet Go
[3299.48 → 3300.12] library that
[3300.12 → 3301.16] we're using
[3301.16 → 3301.64] under the
[3301.64 → 3302.48] hood and
[3302.48 → 3302.82] it was
[3302.82 → 3303.06] kind of
[3303.06 → 3303.20] a
[3303.20 → 3303.74] collaboration
[3303.74 → 3304.62] like in
[3304.62 → 3305.74] January I
[3305.74 → 3306.08] was doing
[3306.08 → 3306.86] research of
[3306.86 → 3307.66] which Parquet
[3307.66 → 3308.58] libraries are
[3308.58 → 3309.18] out there
[3309.18 → 3309.98] and I
[3309.98 → 3310.34] want to say
[3310.34 → 3310.72] I might have
[3310.72 → 3311.32] tweeted it
[3311.32 → 3311.70] or something
[3311.70 → 3312.12] like that
[3312.12 → 3313.26] and Shill
[3313.26 → 3313.70] was like
[3313.70 → 3314.04] I've got
[3314.04 → 3314.60] something for
[3314.60 → 3315.48] you and
[3315.48 → 3315.88] at that
[3315.88 → 3316.48] point the
[3316.48 → 3317.20] library was
[3317.20 → 3317.82] actually still
[3317.82 → 3318.56] closed source
[3318.56 → 3319.44] like just
[3319.44 → 3320.02] Segment was
[3320.02 → 3320.48] working on
[3320.48 → 3321.12] it by
[3321.12 → 3321.96] themselves and
[3321.96 → 3322.52] then they
[3322.52 → 3322.80] kind of
[3322.80 → 3323.40] open sourced
[3323.40 → 3324.14] it, and we've
[3324.14 → 3324.94] had a super
[3324.94 → 3325.88] tight collaboration
[3325.88 → 3326.68] I want to say
[3326.68 → 3327.74] I've done 20
[3327.74 → 3328.28] pull requests
[3328.28 → 3329.48] myself against
[3329.48 → 3330.22] this library by
[3330.22 → 3331.10] now and
[3331.10 → 3331.60] they're just
[3331.60 → 3332.92] like it's a
[3332.92 → 3334.26] very, very fine
[3334.26 → 3334.72] piece of
[3334.72 → 3336.00] engineering huge
[3336.00 → 3336.92] shout out it's
[3336.92 → 3338.08] the APIs are
[3338.08 → 3339.18] just super
[3339.18 → 3339.86] thought through
[3339.86 → 3340.98] the performance
[3340.98 → 3341.98] is just
[3341.98 → 3343.14] incredible like
[3343.14 → 3343.92] Arctic DB would
[3343.92 → 3344.76] be nowhere if it
[3344.76 → 3345.40] wasn't for that
[3345.40 → 3346.44] work yeah if
[3346.44 → 3347.86] listeners don't
[3347.86 → 3348.82] take away anything
[3348.82 → 3349.38] else from this
[3349.38 → 3350.04] conversation it's
[3350.04 → 3350.78] check out that
[3350.78 → 3352.04] library I'm a
[3352.04 → 3352.54] huge fan
[3352.54 → 3353.58] right we'll put
[3353.58 → 3354.02] it in the show
[3354.02 → 3354.78] notes because that
[3354.78 → 3355.60] sounds like a very
[3355.60 → 3356.72] important one okay
[3356.72 → 3358.56] okay yeah so for
[3358.56 → 3359.18] those that stuck
[3359.18 → 3360.20] with us to this
[3360.20 → 3361.70] point we need to
[3361.70 → 3362.58] talk about the
[3362.58 → 3363.22] Polar Signals
[3363.22 → 3364.34] Cloud because I'm
[3364.34 → 3365.02] sure that you want
[3365.02 → 3366.02] to hear about it so
[3366.02 → 3368.32] what is the Polar
[3368.32 → 3369.12] Signals Cloud tell
[3369.12 → 3370.92] us about it so in
[3370.92 → 3372.00] essence Polar Signals
[3372.00 → 3373.60] Cloud is hosted
[3373.60 → 3376.22] parka so basically
[3376.22 → 3377.52] it's kind of the
[3377.52 → 3378.44] classic SAS model
[3378.44 → 3380.20] right like you want
[3380.20 → 3381.18] to reap all the
[3381.18 → 3382.24] benefits of continuous
[3382.24 → 3383.44] profiling you
[3383.44 → 3384.30] understand that it's
[3384.30 → 3385.80] useful but you
[3385.80 → 3386.36] don't want to have
[3386.36 → 3387.42] to like maintain
[3387.42 → 3388.76] the backend system
[3388.76 → 3390.46] the APIs up
[3390.46 → 3392.22] times like storage
[3392.22 → 3393.78] efficiency and all
[3393.78 → 3395.24] of that right running
[3395.24 → 3395.92] a distributed
[3395.92 → 3398.86] database all of
[3398.86 → 3399.98] those things so
[3399.98 → 3401.16] basically the entire
[3401.16 → 3402.08] experience of Polar
[3402.08 → 3403.12] Signals Cloud as you
[3403.12 → 3404.34] just deploy the
[3404.34 → 3406.16] parka agent on your
[3406.16 → 3407.70] Kubernetes cluster you
[3407.70 → 3408.54] pointed at Polar
[3408.54 → 3409.60] Signals Cloud and
[3409.60 → 3410.98] you're automatically
[3410.98 → 3412.16] profiling your entire
[3412.16 → 3413.58] infrastructure just like
[3413.58 → 3414.46] that like there's
[3414.46 → 3415.28] nothing else that you
[3415.28 → 3416.66] need to do so yeah
[3416.66 → 3417.30] that's that's the
[3417.30 → 3417.96] product that we're
[3417.96 → 3419.52] currently that we're
[3419.52 → 3421.16] working on it's not
[3421.16 → 3422.90] generally available yet
[3422.90 → 3424.12] we're trialling it with
[3424.12 → 3425.32] a couple of early
[3425.32 → 3427.50] beta customers but
[3427.50 → 3428.50] yeah I mean if there
[3428.50 → 3430.12] are any listeners
[3430.12 → 3431.58] that think that they'd
[3431.58 → 3433.52] be a particularly good
[3433.52 → 3435.18] like case study for us
[3435.18 → 3436.70] please reach out you
[3436.70 → 3437.88] can kind of sign up on
[3437.88 → 3439.22] our website we'll get
[3439.22 → 3441.22] a get an email that
[3441.22 → 3442.00] you've signed up and
[3442.00 → 3444.04] we can kind of chat and
[3444.04 → 3445.46] figure out if it makes
[3445.46 → 3447.68] sense yeah I really
[3447.68 → 3450.56] like that simplicity of
[3450.56 → 3451.26] just setting up the
[3451.26 → 3452.58] agent, and you have it
[3452.58 → 3454.42] all I remember from
[3454.42 → 3455.64] when I used to set up
[3455.64 → 3456.90] Prometheus and
[3456.90 → 3457.86] Carvana on
[3457.86 → 3460.00] Kubernetes and managing
[3460.00 → 3461.32] them the upgrades and
[3461.32 → 3462.62] all that it's not
[3462.62 → 3463.92] difficult, but it's an
[3463.92 → 3464.80] extra thing that you
[3464.80 → 3465.74] have to do and
[3465.74 → 3467.70] sometimes there's higher
[3467.70 → 3468.52] value things that you
[3468.52 → 3469.78] may want to do instead
[3469.78 → 3470.98] different use cases
[3470.98 → 3471.82] different
[3471.82 → 3474.06] setups I remember when
[3474.06 → 3475.28] we made the switch and
[3475.28 → 3476.32] what a big difference
[3476.32 → 3477.82] that made I remember
[3477.82 → 3478.64] when we set up the
[3478.64 → 3479.72] honeycomb agent because
[3479.72 → 3480.76] you can't install
[3480.76 → 3482.72] honeycomb the UI and
[3482.72 → 3484.14] the server just use it
[3484.14 → 3486.94] as a service and I
[3486.94 → 3487.66] really enjoy that
[3487.66 → 3488.92] experience I have to
[3488.92 → 3490.70] say ARCA I remember
[3490.70 → 3491.42] when I set everything
[3491.42 → 3492.72] up, and I was thinking
[3492.72 → 3493.86] I wish there was just
[3493.86 → 3495.70] the agent episode 33
[3495.70 → 3497.22] right to remember and
[3497.22 → 3498.12] we had like the server
[3498.12 → 3498.96] and the UI we talked
[3498.96 → 3499.72] about memory we
[3499.72 → 3500.48] talked about a bunch
[3500.48 → 3502.08] of things and now
[3502.08 → 3503.00] you have it six months
[3503.00 → 3504.12] later like you're
[3504.12 → 3505.46] trialling it and you
[3505.46 → 3506.10] know I mean it's
[3506.10 → 3507.16] amazing to see that
[3507.16 → 3508.68] my most important
[3508.68 → 3509.82] takeaway from our
[3509.82 → 3510.86] conversations Frederick
[3510.86 → 3512.08] I usually ask the
[3512.08 → 3513.12] guests but this time
[3513.12 → 3514.28] I'll go first because
[3514.28 → 3514.92] I think it's so
[3514.92 → 3515.72] important to mention
[3515.72 → 3518.00] this is how much I
[3518.00 → 3519.22] enjoy our interactions
[3519.22 → 3520.50] as like a very basic
[3520.50 → 3521.60] level person to
[3521.60 → 3523.58] person I really enjoy
[3523.58 → 3524.48] seeing the journey
[3524.48 → 3525.40] that you're on
[3525.40 → 3526.78] yourself with the
[3526.78 → 3527.54] company with the
[3527.54 → 3528.42] people that you know
[3528.42 → 3529.64] like work with you
[3529.64 → 3530.78] and get excited about
[3530.78 → 3531.82] your ideas and they
[3531.82 → 3532.66] see things the way
[3532.66 → 3534.50] you see things and
[3534.50 → 3536.06] it's been amazing to
[3536.06 → 3537.32] watch that you know
[3537.32 → 3539.08] as a bystander and
[3539.08 → 3540.26] every six months or
[3540.26 → 3540.98] every few months
[3540.98 → 3541.52] actually it hasn't
[3541.52 → 3542.32] been that long when
[3542.32 → 3543.28] I check in there's
[3543.28 → 3544.30] always something new
[3544.30 → 3546.00] and exciting that you
[3546.00 → 3546.60] have out there
[3546.60 → 3548.80] shipping Arctic DB was
[3548.80 → 3549.46] such a huge
[3549.46 → 3550.98] achievement seeing you
[3550.98 → 3552.08] at Rubicon EU the
[3552.08 → 3553.36] stand the excitement
[3553.36 → 3554.68] that was generated it
[3554.68 → 3555.80] was great to see and
[3555.80 → 3556.70] you're still like such
[3556.70 → 3558.52] a small team so that
[3558.52 → 3560.04] story from a human
[3560.04 → 3561.88] like one-to-one to a
[3561.88 → 3563.44] team to a product to
[3563.44 → 3564.40] a company it's been
[3564.40 → 3566.24] great to watch and
[3566.24 → 3567.56] great people do great
[3567.56 → 3568.92] things I don't know I
[3568.92 → 3569.84] mean it may sound a bit
[3569.84 → 3571.68] cliché, but it is what
[3571.68 → 3573.58] it is you know there's
[3573.58 → 3574.78] no secret you know if
[3574.78 → 3575.90] you truly believe if you
[3575.90 → 3576.78] have like if you're
[3576.78 → 3578.34] aligned and everything
[3578.34 → 3579.48] like what you say and
[3579.48 → 3580.54] what you do and what you
[3580.54 → 3581.54] think they're all the
[3581.54 → 3582.84] same the sky's the
[3582.84 → 3584.50] limit it's been great
[3584.50 → 3585.28] you know seeing that
[3585.28 → 3586.44] come together and
[3586.44 → 3587.78] polar signals cloud I'm
[3587.78 → 3588.58] really looking forward to
[3588.58 → 3590.02] trying it out because
[3590.02 → 3591.92] I've seen like what the
[3591.92 → 3592.92] world looked like before
[3592.92 → 3594.24] and I want to see what it
[3594.24 → 3595.18] looks like after and I
[3595.18 → 3596.10] have a good feeling about
[3596.10 → 3597.60] this so lets's see how
[3597.60 → 3598.52] well it works in practice
[3598.52 → 3600.52] I have no doubts but I
[3600.52 → 3601.32] still want to see it
[3601.32 → 3604.34] yeah so what about your
[3604.34 → 3605.44] key takeaway for the
[3605.44 → 3606.22] audience you mentioned
[3606.22 → 3607.14] about the people a little
[3607.14 → 3609.26] bit about Arctic DB and
[3609.26 → 3610.54] we can take the key
[3610.54 → 3611.64] takeaway but maybe first
[3611.64 → 3612.28] like what are you
[3612.28 → 3613.20] thinking in the next six
[3613.20 → 3614.70] months when are you
[3614.70 → 3615.76] going with the polar
[3615.76 → 3616.84] signals cloud what do
[3616.84 → 3617.50] you expect to happen
[3617.50 → 3619.54] next just a few things
[3619.54 → 3620.24] that you can share
[3620.24 → 3622.74] yeah I mean we want to
[3622.74 → 3625.02] GA the product right we
[3625.02 → 3626.12] want to make it as
[3626.12 → 3628.12] accessible to anyone who
[3628.12 → 3630.02] wants to as much as we
[3630.02 → 3631.48] can like you said right
[3631.48 → 3633.82] like it'll really only take
[3633.82 → 3634.94] deploying the agent and
[3634.94 → 3635.94] you're automatically
[3635.94 → 3637.58] profiling your entire
[3637.58 → 3639.16] infrastructure that said
[3639.16 → 3640.20] we want to make sure
[3640.20 → 3641.62] because profiling is one of
[3641.62 → 3642.90] those it's kind of like
[3642.90 → 3644.68] with any other data
[3644.68 → 3646.54] problem if people don't
[3646.54 → 3648.82] trust the data that's a
[3648.82 → 3650.84] huge problem right and
[3650.84 → 3652.38] you like people lose
[3652.38 → 3653.38] confidence in a product
[3653.38 → 3655.00] very quickly when that
[3655.00 → 3656.48] happens and so it's
[3656.48 → 3657.70] something we want to be
[3657.70 → 3659.56] careful that when we do
[3659.56 → 3660.90] make the product
[3660.90 → 3662.12] generally available that
[3662.12 → 3663.42] it is very solid and that
[3663.42 → 3665.90] people can rely depend on
[3666.50 → 3668.26] it and trust it most
[3668.26 → 3669.90] most importantly right so
[3669.90 → 3672.68] so yeah that's kind of our
[3672.68 → 3675.04] mission for the for all of
[3675.04 → 3676.50] this year lets's say and
[3676.50 → 3678.46] then after that we'll see
[3678.46 → 3679.36] right like there's definitely
[3679.36 → 3681.08] a lot of there's so much
[3681.08 → 3682.84] opportunity to build things
[3682.84 → 3683.74] on top of continuous
[3683.74 → 3685.32] profiling there are very
[3685.32 → 3686.66] exciting things that you
[3686.66 → 3688.24] can do with this data that
[3688.24 → 3689.76] isn't just as a human
[3689.76 → 3691.68] analyzing this data right
[3691.68 → 3693.20] but yeah just kind of going
[3693.20 → 3693.94] back to what you were
[3693.94 → 3695.54] saying I think I don't think
[3695.54 → 3697.08] I realized it as much
[3697.08 → 3698.92] before going into this
[3698.92 → 3700.72] call but because you and
[3700.72 → 3701.46] I have been kind of
[3701.46 → 3702.86] checking in every six
[3702.86 → 3705.30] months or so it's just
[3705.30 → 3708.18] mind-blowing to kind of
[3708.18 → 3711.20] check in on the growth of
[3711.20 → 3712.56] the company of the people
[3712.56 → 3714.56] of the project because you
[3714.56 → 3716.10] know I'm very close to all
[3716.10 → 3716.92] of it, so I don't
[3716.92 → 3719.64] necessarily see like I see
[3719.64 → 3721.50] small changes right but I
[3721.50 → 3723.38] if I then look back six
[3723.38 → 3725.42] months and think about
[3725.42 → 3726.34] all the things that we
[3726.34 → 3728.68] achieved I'm just like I'm
[3728.68 → 3730.64] blown away yeah I couldn't
[3730.64 → 3731.88] decide whether that is my
[3731.88 → 3733.60] top thing or you know
[3733.60 → 3734.70] something that we kept on
[3734.70 → 3735.82] bringing up about Arctic
[3735.82 → 3737.24] DB is kind of how
[3737.24 → 3738.74] important community is and
[3738.74 → 3740.28] how important leveraging
[3740.28 → 3742.68] your network but also I
[3742.68 → 3743.72] think whenever I talk
[3743.72 → 3744.84] about that I also have to
[3744.84 → 3746.20] talk about sharing your
[3746.20 → 3748.22] network right like that's
[3748.22 → 3749.62] the most powerful thing you
[3749.62 → 3750.90] can possibly do to someone
[3750.90 → 3752.66] else right like give people
[3752.66 → 3754.00] access to your network
[3754.00 → 3756.44] it'll like to put their
[3756.44 → 3758.04] careers or their projects
[3758.04 → 3759.56] or whatever it is on like
[3759.56 → 3761.82] hyperspeed right I think
[3761.82 → 3763.72] that's something I
[3763.72 → 3765.20] learned early on in my
[3765.20 → 3766.98] career and like in both
[3766.98 → 3768.40] directions like it's helped
[3768.40 → 3770.94] me tremendously but I also
[3770.94 → 3772.52] try to give it onwards as
[3772.52 → 3774.00] much as I can, that's a
[3774.00 → 3775.52] good one that's a good one
[3775.52 → 3777.38] well Frederick I will
[3777.38 → 3778.72] definitely check in again in
[3778.72 → 3780.36] six months time but what I
[3780.36 → 3781.96] would like to do is keep
[3781.96 → 3783.40] like in closer
[3783.40 → 3784.84] contact because I'm seeing
[3784.84 → 3785.80] some of the amazing things
[3785.80 → 3786.74] that you're building and
[3786.74 → 3788.40] six months it's almost it's
[3788.40 → 3789.24] almost like we're not in
[3789.24 → 3791.16] justice to all the amazing
[3791.16 → 3792.48] things that you know come out
[3792.48 → 3794.14] of polar signals the
[3794.14 → 3795.74] connections that you make the
[3795.74 → 3797.78] ideas that you generate and
[3797.78 → 3798.96] I think I would like
[3798.96 → 3800.58] to share a bit more of that
[3800.58 → 3801.74] because there's a lot of
[3801.74 → 3804.64] amazing stuff going on and I
[3804.64 → 3806.12] think time that's the only
[3806.12 → 3808.06] limit you know time it like
[3808.06 → 3809.26] there's only so many hours
[3809.26 → 3810.32] in the day and there's only
[3810.32 → 3811.70] like your attention and
[3811.70 → 3813.40] your mind share is limited
[3813.40 → 3815.58] but definitely worth it so
[3815.58 → 3816.54] thank you for joining me
[3816.54 → 3817.62] here today thank you for
[3817.62 → 3818.46] sharing all the wonderful
[3818.46 → 3819.48] things, and I'm looking
[3819.48 → 3820.82] forward to what you do
[3820.82 → 3822.10] next it'll be great I'm
[3822.10 → 3822.96] sure of it thank you
[3822.96 → 3824.08] Frederick thank you for
[3824.08 → 3824.88] having me again
[3824.88 → 3830.68] thank you for tuning into
[3830.68 → 3831.96] another episode of ship it
[3831.96 → 3833.18] check out our other
[3833.18 → 3834.56] podcasts for developers
[3834.56 → 3837.50] changelog.com slash master
[3837.50 → 3838.90] you can connect with
[3838.90 → 3840.38] like-minded developers by
[3840.38 → 3842.88] changelog.com slash community
[3842.88 → 3844.38] thank you quickly for the
[3844.38 → 3845.52] worldwide low latency
[3845.52 → 3847.68] changelog.com our listeners
[3847.68 → 3850.38] love those blazing fast MBS
[3850.38 → 3852.56] your beats are awesome
[3852.56 → 3854.54] break master cylinder that's it
[3854.54 → 3855.64] for this week see you all
[3855.64 → 3857.68] next week my last thought for
[3857.68 → 3859.48] today is the takeaways from
[3859.48 → 3861.34] the first year of ship it I've
[3861.34 → 3862.34] been reviewing all the
[3862.34 → 3864.06] transcripts for the first 30
[3864.06 → 3865.88] episodes and there are a lot
[3865.88 → 3867.00] of incredible insights in
[3867.00 → 3869.30] them I'm thinking blog posts
[3869.30 → 3870.70] and slides what do you
[3870.70 → 3870.94] think
