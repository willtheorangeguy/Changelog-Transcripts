[0.00 → 3.26] These noisier sources of supervision can be much more scalable,
[3.60 → 6.70] much faster to execute, easier to version control and iterate on
[6.70 → 7.84] than individual labels are.
[7.96 → 10.00] And if you can layer a number of these on top of each other
[10.00 → 12.76] and basically then let their votes be aggregated by an algorithm,
[13.02 → 14.12] one that we developed at Stanford,
[14.28 → 16.70] you now have the ability to get maybe not 100 perfect labels,
[16.80 → 18.28] but 100,000 pretty good labels.
[18.62 → 19.94] And it takes about the same amount of time.
[20.00 → 22.36] And as we've seen time and time again in recent years,
[22.36 → 24.98] the size of the data set seems to keep winning the day
[24.98 → 26.88] when it comes to getting high performance with these models.
[26.88 → 31.70] Obama for Changelog is provided by Vastly.
[32.00 → 33.88] Learn more at Fastly.com.
[34.12 → 36.42] Our feature flags are powered by Launch Darkly.
[36.68 → 38.48] Check them out at LaunchDarkly.com.
[38.72 → 40.58] And we're hosted on Leno cloud servers.
[40.98 → 44.50] Get $100 in hosting credit at Leno.com slash Changelog.
[45.00 → 47.64] This episode is brought to you by DigitalOcean,
[47.94 → 51.12] Droplets, Managed Kubernetes, Managed Databases,
[51.38 → 54.64] Spaces, Object Storage, Volume Block Storage,
[54.64 → 58.40] Advanced Networking like Virtual Private Clouds and Cloud Firewalls,
[58.56 → 61.82] Developer tooling like the Robust, API, and CLI
[61.82 → 64.84] to make sure you can interact with your infrastructure the way you want to.
[65.26 → 68.76] DigitalOcean is designed for developers and built for businesses.
[69.44 → 73.32] Join over 150,000 businesses that develop, manage,
[73.46 → 75.82] and scale their applications with DigitalOcean.
[76.16 → 79.60] Head to do.co slash Changelog to get started with a $100 credit.
[79.92 → 82.06] Again, do.co slash Changelog.
[82.06 → 106.38] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[106.70 → 108.46] productive, and accessible to everyone.
[108.46 → 112.88] This is where conversations around AI, machine learning, and data science happen.
[113.30 → 117.34] Join the community and Slack with us around various topics of the show at ChangeLog.com
[117.34 → 119.22] slash community and follow us on Twitter.
[119.36 → 120.98] We're at Practical AI FM.
[127.38 → 130.12] Welcome to another episode of the Practical AI podcast.
[130.44 → 131.50] My name is Chris Benson.
[131.74 → 135.20] I'm a principal emerging technology strategist with Lockheed Martin.
[135.20 → 141.06] And unfortunately, Daniel was not able to join us today, but I have a guest that I'm excited
[141.06 → 141.92] to talk to today.
[142.08 → 147.26] I have Brayden Hancock, who is the co-founder and head of technology at Snorkel AI.
[147.86 → 149.02] Welcome to the show, Brayden.
[149.08 → 149.70] How's it going today?
[150.10 → 150.28] Thanks.
[150.38 → 150.92] Glad to be here.
[151.16 → 151.60] Doing well.
[152.04 → 156.34] Well, I was wondering if you would start off telling us a bit about your own background
[156.34 → 158.76] and let us understand how you got to where you're at.
[158.84 → 161.18] And then I'm looking forward to asking you more about Snorkel AI.
[161.78 → 162.38] Yeah, absolutely.
[162.38 → 167.20] So yeah, as you mentioned, I'm currently a co-founder and head of technology at Snorkel
[167.20 → 167.44] AI.
[168.06 → 171.98] The company's been around for about a year and a half now, maybe coming on too.
[172.54 → 173.74] And it's been a blast.
[174.36 → 179.54] Before that, I was a Stanford PhD student, along with all the rest of my co-founders.
[179.60 → 182.02] That's actually the origin story of our company.
[182.64 → 185.50] And then that's what brought me to the Bay Area in the first place.
[185.68 → 187.80] It was actually not in computer science originally.
[187.80 → 193.72] I came from mechanical engineering and just found myself consistently being drawn to machine
[193.72 → 194.02] learning.
[194.56 → 197.38] And then finally, you know, saw the writing on the wall and made the jump myself going
[197.38 → 197.94] into grad school.
[198.36 → 203.10] So I'm just curious because we hear that kind of story a lot where people are coming in
[203.10 → 205.92] from an industry that you may or may not expect that to happen.
[206.02 → 209.90] When you're still doing mechanical engineering, what was the draw into machine learning for
[209.90 → 210.50] you at that point?
[210.56 → 214.16] I'm just curious what it was that started that process of sliding over.
[214.58 → 216.14] Yeah, no, I completely agree with you.
[216.14 → 218.00] I think we see a lot of people make that shift.
[218.14 → 221.78] And it's perhaps not too surprising, just given how rapidly the field is growing, that
[221.78 → 223.34] the people have to come from somewhere.
[223.88 → 229.54] But for me, I think part of it's just how much faster science is in computer science.
[229.56 → 232.14] The fact that you can iterate so much more quickly.
[232.30 → 237.08] An experiment can be run in seconds or minutes, you know, certainly set up and run in a day
[237.08 → 242.20] often, you know, for certain experiments compared to when you've got a mechanical rig and there
[242.20 → 246.66] are parts and, you know, one bad transistor and the whole thing's kind of suspect.
[247.02 → 251.30] And there's just so many more failure modes in such longer timeframes that I kept coming
[251.30 → 251.84] back to.
[251.98 → 256.30] I want to be able to answer questions quickly, and could do that so much faster in CS.
[256.74 → 260.58] And do you think that's going to be a situation that we see over and over again with people
[260.58 → 262.12] in various industries pulling in?
[262.26 → 263.52] We've seen a certain amount of that.
[263.60 → 264.70] I tease Daniel a lot.
[264.70 → 269.28] We end up talking to people that come from physics a lot and one way or another, they
[269.28 → 270.22] found their way over.
[270.48 → 274.40] So do you think that's going to be very typical with mechanical engineers constantly finding
[274.40 → 279.08] the need to use machine learning to get their jobs done and whether they jump over
[279.08 → 280.52] to the dark side or not?
[280.76 → 285.26] I'm sure we'll continue to see plenty of people jump in from over there, you know, for different
[285.26 → 286.16] reasons, probably, right?
[286.22 → 290.22] I think for a lot of people, you end up finding that the best way to do your job is to use machine
[290.22 → 290.44] learning.
[290.46 → 293.24] And then you realize, hey, this is actually a really cool tool.
[293.24 → 295.50] I think I'd like it to be more than just a tool for me.
[295.60 → 299.50] And then you really lean in and start, you know, diving in a more permanent way rather
[299.50 → 301.54] than just in sort of applied sense.
[301.80 → 302.00] Gotcha.
[302.16 → 306.82] So I'm just curious, what was your first experience as you started getting into machine learning
[306.82 → 308.44] before you made the full jump?
[308.50 → 311.06] What was that thing that was drawing you in?
[311.10 → 312.44] What kind of models were you doing?
[312.78 → 317.10] What was your tooling that made you think it might be time to make a shift?
[317.30 → 320.82] You know, this baby just shows how thick I am that it actually goes all the way back
[320.82 → 325.30] to high school that I was that I my first dabbling in machine learning and loved it and just
[325.30 → 329.72] didn't even don't realize then that I should have just embraced it full wholeheartedly from
[329.72 → 330.10] the get go.
[330.20 → 332.14] But there was a lucky break for me.
[332.18 → 336.78] There's an internship program for high school students near Wright Patterson Air Force Base
[336.78 → 338.22] in Ohio, where I grew up.
[338.22 → 344.14] And so I was on a project using MATLAB, of course, the lingua franca of mechanical engineers,
[344.40 → 346.84] not the Python of machine learning engineers.
[347.12 → 352.72] But yeah, so I was the task that I was assigned to was using genetic algorithms to design better
[352.72 → 353.30] airfoils.
[353.30 → 356.08] So some non-gradient based optimization.
[356.08 → 361.30] And I thought it was so cool that even after I lost my MATLAB license, you know, during the
[361.30 → 362.56] school year, I had to go back to high school.
[362.56 → 367.84] So this was after my junior year, I used Excel and, you know, I had a separate tab for each
[367.84 → 371.70] generation of the genetic algorithm and like tried to recreate it there because I was still,
[371.84 → 374.36] of course, a lousy programmer, but just thought the ideas were so neat.
[374.84 → 375.14] Very cool.
[375.34 → 381.00] So is it genetic algorithms were what actually pulled you in and going from that and thinking
[381.00 → 386.76] all the way to now as a co-founder at Snorkel AI, what was the crossover right there that got
[386.76 → 387.90] you to Snorkel AI?
[388.36 → 392.50] Yeah, I'd say, you know, from the very beginning, one of the ideas that drew me in was there's
[392.50 → 397.28] should be this different interface for getting things done for transferring information
[397.28 → 401.04] from an expert into a program that can now do work for you.
[401.08 → 406.22] And I think historically, that's very imperative code very much like describe exactly what you
[406.22 → 407.30] want done step by step.
[407.50 → 412.50] And that was less interesting to me felt a little bit more like your jobs just to translate,
[412.66 → 414.08] you know, from one language to another.
[414.30 → 418.02] But the cool thing about machine learning or AI in general, I think is that you get more of
[418.02 → 422.72] a sense in the right setup of if you can tell me what's good, then I can find it.
[422.80 → 428.38] There's this better synergy between the human and the computer where now I can show you what
[428.38 → 430.10] I want, even if I don't know how to get there.
[430.20 → 433.24] And you can get there, you know, where you here are the computer, of course.
[433.58 → 437.24] So I think that's the broader idea that was really appealing to me all along the way that
[437.24 → 438.70] had me coming to machine learning.
[438.70 → 443.60] And then throughout my PhD, I kind of dove into that problem much more deeply of what
[443.60 → 447.34] really is the best interface for getting domain knowledge from an expert into a model.
[447.88 → 451.60] And that's, you know, those are themes that I explored for multiple years that along with
[451.60 → 456.02] my co-founders ended up, you know, being what led us to snorkel and then snorkel AI.
[456.26 → 460.96] Now, just to dive in there a little bit, was there a particular itch that you were scratching
[460.96 → 463.90] in that context that actually led to snorkel AI?
[463.90 → 468.44] Was there something you can relate where it was like, well, guys, we got to solve this
[468.44 → 469.30] particular issue.
[469.46 → 473.82] This is something that we need to dive into that might have been the specific genesis or?
[474.86 → 475.06] Yeah.
[475.26 → 480.22] So I'd say one thing that my PhD advisor was fantastic about was Chris Ray at Stanford.
[480.40 → 485.84] And he, I think, is very good at making sure that the problems you're solving actually will
[485.84 → 487.78] matter to people, actually solve real problems.
[487.90 → 491.92] And part of the way that you do that is by, you know, on most papers, we would try and have
[491.92 → 497.02] real world collaborators work with another company or research organization or government
[497.02 → 500.94] entity or something where we could make sure that like this actually solves your problem.
[501.34 → 502.42] So people are more likely to care.
[502.50 → 505.88] This is likely going to stick and, you know, and have a potential to make real impact.
[506.56 → 512.82] And so very early on in my degree is we were looking at what is the effective bottleneck for
[512.82 → 514.38] new machine learning applications?
[514.52 → 517.50] What is it that stops people from solving their problems quickly, as quickly as they'd like
[517.50 → 517.72] to?
[518.14 → 521.76] The realization came that that bottleneck is almost always the training data.
[521.92 → 524.08] You know, we saw kind of the writing on the wall.
[524.18 → 526.34] Deep learning was blossoming right about then.
[526.50 → 530.54] We saw these super powerful models, feature engineering's becoming a lot less necessary.
[530.88 → 532.28] A lot of that can be learned now.
[532.42 → 539.14] But with the one caveat of you can do all this if you have just mountains of, you know, perfectly
[539.14 → 542.00] labelled clean training data ready to go for your specific task.
[542.10 → 544.34] And that in reality never exists, of course.
[544.34 → 550.48] And so that I'd say was the real impetus for this line of work was, you know, this is what
[550.48 → 551.22] stops people.
[551.38 → 554.98] In academia, it's download the data set and then do something cool with it.
[555.10 → 556.28] But in industry, it's...
[556.28 → 556.64] Get the data.
[556.68 → 559.78] I mean, steps like one through nine is where am I going to get my data and do I have enough
[559.78 → 560.74] of it and is it clean enough?
[560.82 → 563.14] And these annotators are doing the exact wrong thing.
[563.20 → 564.26] I can clarify the instructions.
[564.40 → 565.08] Is this good now?
[565.52 → 566.32] It's iterating.
[566.58 → 568.66] And 80% of the work is making that training set.
[568.78 → 572.38] After that, like pulling off some state-of-the-art model in the open source and running that, that's
[572.38 → 573.00] the easy part.
[573.48 → 573.94] Yeah, it's funny.
[574.16 → 577.02] You would think of AI as...
[577.02 → 582.44] I think people outside our industry look at this and think we're doing this, you know,
[582.50 → 584.80] dark magic of AI and producing the model.
[585.06 → 589.18] But every time we talk to somebody, it's always trying to get set up to do that.
[589.28 → 594.06] It's getting to that, getting to the starting line of doing the actual modelling itself that
[594.06 → 595.02] people are struggling with.
[595.02 → 596.88] So tell us a bit about Snorkel AI.
[597.24 → 602.36] You know, how did that blossom out of this experience that as a co-founder you were having?
[602.38 → 605.80] And as well as what, you know, what the others were driven to do as well.
[605.92 → 609.62] And can you tell us a little bit about your co-founders and just kind of how the whole
[609.62 → 610.34] thing got started?
[610.74 → 610.92] Yeah.
[611.08 → 615.58] So we feel very lucky at Snorkel AI to have the founding team that we do.
[615.68 → 617.20] It's a little bit larger than you typically have.
[617.26 → 618.02] There are five of us.
[618.60 → 623.76] It's Chris Ray, who I mentioned was my PhD advisor, myself, and then three other previous
[623.76 → 624.20] students.
[624.20 → 625.54] We were all sorts of in the same cohort.
[625.80 → 628.34] Alex Rather, Aroma Karma, and Henry Ehrenberg.
[629.12 → 634.00] And all of us, you know, began at about the same time, our grad school experience and picking
[634.00 → 634.78] up different projects.
[635.36 → 639.40] And all of us were just drawn to these ideas and ended up collaborating in almost every
[639.40 → 642.82] combination you can think of between the four of us on different papers through those
[642.82 → 643.08] years.
[643.82 → 647.50] And, you know, it was going to be in the beginning, like, this is an interesting idea.
[647.58 → 651.28] Let's run a quick experiment, pull up a Jupyter notebook, test some of these ideas.
[651.76 → 652.80] And then it really seemed to work.
[652.80 → 656.52] And so then it became a workshop paper and then a full paper and eventually the best of
[656.52 → 661.28] paper and an open source project and then an open source ecosystem and other derivative
[661.28 → 663.24] projects and lots of collaborations.
[663.62 → 669.30] And we helped a few different organizations make sort of industry scale versions of this
[669.30 → 672.90] internally to really prove out the concept of paper with Google, for example, that we
[672.90 → 673.50] were able to publish.
[673.80 → 677.92] And by the time that we were at the end of our degrees, it was clear that there was just
[677.92 → 679.58] such a dramatic pull for this.
[679.58 → 684.56] The ideas were very well validated at that point over, you know, probably 35 different
[684.56 → 689.24] peer-reviewed publications, but maybe more importantly, a bunch of different organizations
[689.24 → 694.40] that independently had seen success with these approaches, almost always from working with
[694.40 → 696.08] us to kind of help lead them through the process.
[696.64 → 700.90] And so we just learned so much through that time about what you would really need to take
[700.90 → 705.72] this proof of concept and make it something that could be repeatable and with a relatively
[705.72 → 709.56] low barrier to entry that doesn't require a room full of Stanford PhDs to make it
[709.58 → 710.06] successful.
[710.40 → 714.14] And that's part of what motivated the company is, you know, the chance to now make this
[714.14 → 719.10] a, you know, fully supported enterprise ready and, you know, able to be shared with a whole
[719.10 → 722.40] bunch of different industries and company sizes and in different work areas.
[722.40 → 729.18] Before you dive into the specifics of the product and service offerings, could you talk about
[729.18 → 730.62] a little bit about what you did learn?
[730.62 → 736.50] Because with that opportunity to be doing the academic work and to progress through that over
[736.50 → 743.78] time and kind of have that insight before you ever actually start the new company, can you talk about
[743.78 → 748.00] what that learning process was like, and what were some of the things that had a big impact
[748.00 → 749.78] specifically, conceptually?
[749.98 → 754.78] And then from there, I'd like to kind of go one into how that was realized in the company itself.
[754.78 → 756.00] Yeah, absolutely.
[756.24 → 757.22] And I completely agree.
[757.30 → 762.34] I think it was a huge, huge advantage for us to have that, I mean, really much larger
[762.34 → 765.78] period of time than you would ever get as a startup to do the learning phase, right?
[765.82 → 770.98] We were able to succeed and fail and try different variations and really push the boundaries and
[770.98 → 772.96] like intentionally try to find where does this fail?
[773.12 → 776.24] Because as an academic, that's, I mean, that's the hat you wear is like, let's really sums out.
[776.30 → 777.76] Let's do every ablation we can think of.
[777.82 → 779.52] Let's figure out, does this work for text?
[779.56 → 780.32] Does this work for video?
[780.32 → 783.50] Does it work for, you know, very dependent and correlated data?
[783.60 → 788.00] Does it work for, you know, the whole variety of the space that you can imagine, we were
[788.00 → 788.60] able to test.
[788.70 → 792.90] And so it meant that by the time that we were building now the, you know, the air quotes
[792.90 → 796.92] final version, like the enterprise version, we were able to bring all these different
[796.92 → 798.60] learnings to bear as part of that design.
[798.94 → 805.36] So if I was trying to structure categorically the lessons that we learned, I think one of the
[805.36 → 807.04] big ones was interfaces.
[807.04 → 811.22] I think as a, as a grad student supported open source project, you don't have a lot of time
[811.22 → 812.68] to polish up a front end for people.
[812.68 → 812.90] Right.
[812.92 → 815.82] So it's, uh, it's in the form of like a Python package.
[815.82 → 819.46] And if there are unit tests, you're lucky because that's, you know, of course we cared
[819.46 → 821.54] about that, but it's not necessarily in your incentive.
[821.66 → 823.54] Unit tests don't lead to papers, right?
[823.56 → 826.04] It just means you have some more stable development as you work.
[826.04 → 827.54] So it was fine and it worked well.
[827.64 → 829.40] And we, you know, of course did support it as much as we could.
[829.50 → 833.86] But I think one thing we did realize is, you know, we were writing a lot of the same code
[833.86 → 834.70] over and over again.
[834.70 → 837.16] And there were certain templates for labelling functions.
[837.28 → 840.78] I think we'll talk more about those later, but, you know, third party integrations or
[840.78 → 844.90] like just sort of patterns of sequences of steps that people would try that get lost if
[844.90 → 847.00] it'd be in like the forest of scripts and notebooks.
[847.58 → 853.02] Whereas if you can set up a properly structured interface and GUI as well as other access points,
[853.02 → 855.56] you can really dramatically improve the likelihood of success.
[855.84 → 858.04] So that's one category, the interfaces, I'd say.
[858.72 → 859.98] What else did you learn along the way?
[860.04 → 864.48] Was interfaces the primary driver there or any other key lessons there?
[864.82 → 866.54] Yeah, no, I mean, interfaces was a big one.
[866.66 → 870.72] I'd say if I was grouping it into other areas, I'd say there was also infrastructure.
[871.12 → 874.54] There was like intuitions that we gained and baking those in.
[874.92 → 879.24] And then sort of like user profiles or like interaction points.
[879.38 → 881.48] So I can say a word about each of those.
[882.22 → 885.36] On the infrastructure side, I think that one's fairly self-explanatory.
[885.36 → 888.64] If you're going to have your, as a company, if you're going to depend on a piece of software,
[888.64 → 893.94] you need it to have certain things like, I mean, basic security and logging, encryption
[893.94 → 899.20] and compatibility with the data formats that you care about and dependency management and
[899.20 → 900.04] parallelization.
[900.18 → 904.12] All these things that, of course, of course you want in software you're going to depend on,
[904.26 → 907.60] but that again, just aren't necessarily a part of research code.
[907.64 → 909.24] That's meant to be more of a proof of concept.
[909.24 → 909.64] Sure.
[910.26 → 915.28] Kind of making it real comes down to really kind of classical software development things
[915.28 → 918.02] that you need in place to deploy remote software.
[918.22 → 921.92] And I think that comes back to a point that we run into a lot on the show.
[922.00 → 926.42] And that is the fact that you can't really separate the AI from the software the AI is
[926.42 → 927.20] running in.
[927.30 → 931.46] And it sounds like you all had a realization about that even before you got the organization
[931.46 → 931.96] launched.
[931.96 → 933.46] Yeah, no, absolutely.
[934.32 → 939.30] I mean, I'd say another big piece of this is, again, as an academic, you often test these
[939.30 → 940.08] ablations.
[940.18 → 943.30] You'll test a very specific problem, and can the model learn what I need it to?
[943.40 → 948.00] But in the wild, you often have actually just a problem you need to solve, and you don't
[948.00 → 949.34] necessarily care how that's solved.
[949.44 → 951.16] You just, you know, you want a high quality system.
[951.52 → 956.30] And so you typically, you know, you don't just have this one model that's ready to go with
[956.30 → 959.54] the data that you care about that has an output that is exactly what you care about.
[959.86 → 961.70] There's always, it's a pipeline, right?
[961.70 → 963.50] You've got pre-processing steps.
[963.60 → 964.84] You've got business logic.
[965.00 → 968.04] You're chaining together multiple models or multiple operators.
[968.22 → 970.06] Some are heuristic and some are machine learning based.
[970.64 → 975.14] And so this actually gets at one of the big differences, I'd say, in terms of, you know,
[975.18 → 980.18] fundamental value out of the Snorkel open source versus Snorkel flow, the business product
[980.18 → 986.28] now is that the latter is much more focused on building AI applications, like an application
[986.28 → 991.44] that solves your problem from end to end rather than just a point solution for a part of a
[991.44 → 994.40] pipeline that is making a training set or training a single model.
[994.74 → 994.94] Gotcha.
[994.94 → 1020.28] So Braden, just a moment ago, you were talking about Snorkel open source and Snorkel flow.
[1020.28 → 1025.40] And could you now define what each of those are and describe what the differences in the
[1025.40 → 1025.72] two are?
[1026.44 → 1026.96] Yeah, absolutely.
[1027.22 → 1033.28] So if you go to snorkel.org, that's the website for the open source project that again, you
[1033.28 → 1038.96] know, began almost four years ago at Stanford and served as sort of our testing ground and
[1038.96 → 1044.16] proof of concept area for a lot of these ideas around, can we basically change the interface
[1044.16 → 1048.34] to machine learning to be around, you know, programmatically creating and managing and
[1048.34 → 1049.68] iterating on training sets.
[1050.42 → 1051.36] And so that's what that is.
[1051.40 → 1052.24] It's pip installable.
[1052.34 → 1053.18] You can pull it down now.
[1053.28 → 1057.10] It's, you know, got 4,000 something stars, and it's used in a bunch of different projects.
[1058.12 → 1063.18] Snorkel flow is the offering now the primary product of Snorkel AI.
[1063.18 → 1067.70] And that is based on and powered by that Snorkel open source technology.
[1068.34 → 1071.30] But then it's just sort of expands to much more.
[1071.50 → 1074.10] It is now a platform, not a library.
[1074.24 → 1078.56] It comes with some of those infrastructure improvements that I mentioned before.
[1078.80 → 1084.10] It also bakes in a lot of the intuitions that we gained from the years of using the
[1084.10 → 1084.62] open source.
[1084.78 → 1091.30] There are certain ways that you can guide the process systematically to creating, you
[1091.30 → 1095.50] know, these programmatic training sets or improving them systematically, really completing the loop
[1095.50 → 1100.82] so that at every stage of the way, you have some sort of hint at what should I focus on
[1100.82 → 1103.72] next to improve the quality of my model or of my application.
[1104.36 → 1109.04] So that application, you know, the Snorkel flow is, as I mentioned, or sorry, that platform
[1109.04 → 1114.72] is meant to be this much broader solution for supporting end to end pipelines, not just the
[1114.72 → 1118.80] data labelling part, baking in a bunch of these, you know, best practices, tips and tricks
[1118.80 → 1123.00] that we learned over the years of essentially writing the textbook on this new interface
[1123.00 → 1123.78] to machine learning.
[1124.04 → 1127.56] And then includes also, you know, some of those interfaces like an integrated notebook
[1127.56 → 1131.44] environment for when you do want to do very low level, you know, custom one off stuff,
[1131.56 → 1135.76] but also some much higher level interfaces like those templates I mentioned for labelling
[1135.76 → 1136.20] functions.
[1136.40 → 1141.94] There are a number of ways where it can be a truly no code or very low code environment for
[1141.94 → 1147.18] subject-matter experts who don't necessarily know how to, you know, whip out the Python
[1147.18 → 1151.32] and solve a problem, but do have a lot of knowledge that's relevant to solving a problem.
[1151.84 → 1151.94] Gotcha.
[1152.30 → 1156.04] Actually, to dive a little bit deeper into both sides of that, let's start with the open
[1156.04 → 1157.74] source and build on that.
[1158.06 → 1163.66] What would be a typical use case where somebody would go to snorkel.org and do the pip install,
[1163.82 → 1164.40] read the docs?
[1164.56 → 1167.64] And what are you offering with that and through those libraries?
[1168.00 → 1168.66] What's available?
[1169.12 → 1173.14] And then in a minute, I'll obviously ask you the other side about taking it to that next level.
[1173.14 → 1178.84] But if you could kind of give us a sense of what the open source side experience is like,
[1178.92 → 1181.72] what the benefit of the libraries are, that'd be fantastic.
[1182.20 → 1182.30] Yeah.
[1182.50 → 1187.58] So if you go actually to snorkel.org, there's a section that is tutorials.
[1187.92 → 1190.92] And we walk through a number of different, fairly simple, right?
[1191.08 → 1195.14] But meant to be sort of instructive tutorials for different ways you could use the library.
[1195.50 → 1200.70] So often one of the most intuitive places to start with that is on text-based problems.
[1200.70 → 1204.78] There also are a couple of demonstrations there for how to apply it to images.
[1205.30 → 1207.00] And then we've got research papers as well.
[1207.06 → 1211.02] We can point people to for working with time series or video or things like that.
[1211.12 → 1215.42] But one very simple example, one that we actually rely on in our primary tutorial,
[1215.54 → 1219.82] just because it's very interpretable and almost everyone has the domain expertise necessary for it,
[1220.26 → 1223.32] is training a document classifier.
[1223.42 → 1226.28] And in this case, we could say the document will be emails.
[1226.56 → 1228.80] And you want to classify these as spam or not spam.
[1228.80 → 1232.58] You know, one way you could do this in a sort of traditional machine learning setting is
[1232.58 → 1236.38] get a bunch of emails that, you know, are sort of raw and unlabelled.
[1236.64 → 1242.10] Look at them one by one and label them as this one's spam, this one's not spam, that one's spam.
[1242.66 → 1246.52] And eventually you'll have the thousands or tens of thousands or hundreds of thousands of emails
[1246.52 → 1250.82] that you need to train some very powerful deep learning model to do a great job, right?
[1250.82 → 1256.28] But when you do this process, if you've ever tried to label a data set, you do find that very quickly,
[1256.78 → 1263.96] there start to be certain things that you rely on to be efficient or that are like basically the signs to you
[1263.96 → 1265.54] for why you should label things a certain way.
[1266.14 → 1270.92] So, you know, an easy example here might be lots of spam emails try and sell you prescription drugs, right?
[1271.32 → 1276.22] So you may see, you know, the word Vicodin in an email and that's pretty clear to you.
[1276.22 → 1278.36] This is not a valid business email.
[1278.54 → 1279.76] This is spam, and you can mark it as such.
[1281.00 → 1285.86] And you might eventually label over 100 emails that have the word Vicodin and all of them are spam
[1285.86 → 1288.40] for approximately that same reason, among other things.
[1288.40 → 1290.90] There's other content in the email, but that's what tipped you off.
[1291.62 → 1296.54] And so if you could instead just, you know, one time say, and if you see the word Vicodin in the email,
[1296.76 → 1301.68] good chance that this is a little, you know, more likely to be spam rather than we'll call it ham or not spam.
[1302.08 → 1302.20] Right.
[1302.20 → 1306.88] You could write that, apply that to hundreds of thousands of unlabelled data points and get,
[1307.26 → 1310.42] in one fell swoop, hundreds of labelled examples.
[1310.74 → 1312.28] And those labels may not be perfect.
[1312.38 → 1314.10] There may actually be a couple examples in there.
[1314.38 → 1317.10] You know, some small portion where it actually was valid.
[1317.20 → 1321.30] Someone was asking, you know, did you see where my Vicodin was put?
[1321.36 → 1321.94] I'm not sure.
[1322.18 → 1322.30] Yeah.
[1322.42 → 1323.46] I won't guess.
[1324.34 → 1329.48] But basically, you know, these noisier sources of supervision can be then, you know, much,
[1329.48 → 1334.12] much more scalable and, you know, much faster to execute, easier to version control and iterate on
[1334.12 → 1335.28] than individual labels are.
[1335.60 → 1339.32] And if you can layer a number of these on top of each other and basically then let them,
[1339.86 → 1345.04] you know, let their votes be aggregated by an algorithm, you know, one that we developed at Stanford,
[1345.62 → 1348.52] you now have the ability to get, you know, maybe not 100 perfect labels,
[1348.62 → 1350.10] but 100,000 pretty good labels.
[1350.10 → 1351.74] And it takes about the same amount of time.
[1351.82 → 1355.26] And as we've seen time and time again in recent years, you know,
[1355.30 → 1359.58] the size of the data set seems to keep winning the day when it comes to getting high performance with these models.
[1360.30 → 1360.38] Yeah.
[1360.48 → 1367.68] So essentially that open source library is helping you scale out your labelling so that you get to the meaningful thing,
[1367.76 → 1370.94] meaning that you're actually starting to create models faster.
[1371.36 → 1372.80] So a way to overcome that.
[1372.94 → 1373.36] That's right.
[1373.50 → 1373.68] Yeah.
[1373.68 → 1379.10] You can think of it as, you know, yeah, essentially as a way of building and managing training sets,
[1379.34 → 1384.68] you know, very, very quickly, often at a much higher sort of rate of production,
[1384.68 → 1386.98] as well as just much larger magnitude.
[1387.40 → 1392.40] So at what point, if you've been doing this for a while, and you found that utility in the libraries and such,
[1392.72 → 1397.64] what is a typical scenario that you're finding with customers where they do need to level up?
[1397.68 → 1399.72] Maybe they've used the open source software for a while.
[1399.72 → 1403.52] Maybe they had already been doing it even prior to you creating the company.
[1403.68 → 1404.74] But now it's time.
[1404.84 → 1406.38] You mentioned platform specifically.
[1406.98 → 1413.32] What is it that they are now facing that it's a clear step up, and they need the enterprise approach at this point?
[1413.78 → 1413.90] Yeah.
[1414.06 → 1417.60] So I'd say there are a number of different reasons for this.
[1417.96 → 1419.54] And it's a little bit different, you know,
[1419.56 → 1422.14] which elements of the grab bag are most important for different customers.
[1422.32 → 1423.52] But I can list a few of those.
[1423.96 → 1427.34] So, you know, one of the big ones is just the guidance.
[1427.34 → 1431.98] I think with the proof of concept, you know, library, the open source, over the years of using it,
[1431.98 → 1433.44] we knew sort of what to look for.
[1433.64 → 1436.16] How accurate is accurate enough for a labelling function?
[1436.28 → 1437.76] How many do I need?
[1437.96 → 1442.56] What, you know, how should I come up with ideas for what a valid labelling function could be?
[1443.04 → 1447.98] How could I integrate external resources that I may have, like a legacy model that I want to improve on?
[1448.04 → 1452.22] Or maybe an ontology that belongs to the business that has information in it?
[1452.22 → 1453.22] And how should I integrate that?
[1453.22 → 1460.36] So there's a lot of, you know, what would otherwise be folk knowledge if you're using the open source that you just only get through experience
[1460.36 → 1465.66] that we've been able to really bake in and support in a native first class guided way in the platform.
[1465.86 → 1467.86] And that's a big difference maker for a lot of people.
[1468.44 → 1468.54] Gotcha.
[1468.74 → 1473.44] As we're talking here, I'm looking through your website and I went into the platform
[1473.44 → 1483.16] and I noticed that you're kind of segregating out the different processes with label and build, integrate and manage, train and deploy, analyze and monitor.
[1483.44 → 1484.88] Why that particular segregation?
[1485.30 → 1488.50] What is it that the platform brings to each of those capabilities?
[1489.04 → 1491.20] How are you guys envisioning this process?
[1491.50 → 1495.92] And if you have any insight, what is separating that from other options that you may see in the marketplace?
[1495.92 → 1503.02] Yeah, so I'd say that that label and build is probably the piece of that pipeline that overlaps most with the open source
[1503.02 → 1510.92] in the sense that that's the area where you're going to write labelling functions and then, you know, likely aggregate these right into effectively training labels,
[1511.48 → 1515.26] confidence weighted labels for these unlabelled examples that you can now train on.
[1516.06 → 1523.32] That, you know, manage and version piece up next, that speaks to, you know, when you have not just a one-off project,
[1523.32 → 1528.86] when your goal is not just to fill a table in a paper, but really to, you know, to build something that you have confidence in,
[1528.90 → 1533.78] that you can come back to, that you can, you know, point to in the case of an audit or whatnot.
[1534.16 → 1536.74] There's extra value in managing all these different artifacts.
[1537.44 → 1545.36] You've got often many applications that you care about, many teams working on it, many different, again, just, you know, artifacts that you create,
[1545.44 → 1547.72] whether that's models or training sets or sets of labelling functions.
[1547.72 → 1553.10] So there is an element here that's as well just the data management side of things and tracking, you know,
[1553.14 → 1556.38] and in versioning and supporting sort of all of those types of workflows.
[1557.06 → 1562.70] On the modelling side, that is entirely, you know, unique to the platform with respect to the open source
[1562.70 → 1569.22] that we have a bunch of sorts of industry standard modelling libraries integrated with the platform.
[1569.40 → 1573.00] So if you do want to, you know, train a scikit-learn model, sure,
[1573.00 → 1578.34] or some of the hugging face transformers right there, Flare is another one, XGBoost.
[1578.82 → 1581.76] So a lot of these libraries we've kind of unified behind a simple interface
[1581.76 → 1587.88] so that it can be a sort of push-button experience to try out a number of different things,
[1587.94 → 1588.92] a hyperparameter tune and whatnot.
[1589.46 → 1592.84] But with the goal really being of, you'll find most of the time,
[1593.22 → 1598.04] you'll get the biggest lift by actually improving the training set rather than the model.
[1598.28 → 1601.42] And so I guess that actually moves us on to the fourth part, which is analysis.
[1601.42 → 1604.30] We have a whole separate page with a bunch of different components
[1604.30 → 1607.62] that effectively take a look at how your model is currently performing
[1607.62 → 1610.48] and where it's making mistakes and why it might be making those mistakes,
[1610.70 → 1613.38] and then makes concrete recommendations for what to do next.
[1613.50 → 1617.90] And so in some cases, it's, you know, yes, actually, your training set looks pretty good.
[1617.96 → 1621.90] The learned labels that we're coming up with actually line up pretty well with ground truth.
[1622.02 → 1625.74] And so if you're making mistakes here, it's probably because, you know, it's your model now.
[1625.74 → 1630.00] So you need to try a more powerful model or, you know, hyperparameter tune a little bit differently.
[1630.00 → 1632.46] And I think that's where a lot of machine learning practitioners
[1632.46 → 1636.32] naturally go immediately to the model and hyperparameter tuning.
[1636.50 → 1639.78] When in reality, almost always the far larger air bucket is
[1639.78 → 1645.06] there are whole swaths of your evaluation set that have no training set examples that look at all like them.
[1645.22 → 1647.96] There are like basically just blind spots that your model has.
[1648.42 → 1651.38] And, you know, now in the platform, you can go ahead and click on that air bucket.
[1651.62 → 1654.94] Go look at those, you know, 20 or 100 or however many examples
[1654.94 → 1657.68] where none of your labelling functions are applying.
[1657.68 → 1661.82] So this is not reflected at all in your training set and write some new supervision
[1661.82 → 1665.26] that will add effectively examples of that type to your training set
[1665.26 → 1669.18] so that the next model you train will know something about those types of examples
[1669.18 → 1670.80] and can improve upon them.
[1671.14 → 1671.48] Sounds good.
[1671.56 → 1674.02] I'm also looking at some of the different solutions that you have
[1674.02 → 1679.18] that are listed from document classification, named entity recognition, information extraction.
[1679.18 → 1686.46] I'm kind of curious since as you're looking at this and you guys clearly found a gap in the marketplace
[1686.46 → 1691.72] from the perspective you were coming from, what makes your approach to each of these problems?
[1691.72 → 1695.92] Because these are fairly classical problems, sentiment analysis and anomaly detection.
[1696.26 → 1700.84] What are some of the ways that you think you're adding value that you weren't finding out there?
[1700.84 → 1707.06] What is that special sauce to some degree that you guys were really looking to introduce into the marketplace
[1707.06 → 1708.24] with this platform?
[1708.24 → 1714.12] Yeah, I think what really moves the needle is the fact that with this approach and with this platform,
[1714.64 → 1719.78] machine learning becomes just more practical, more systematic, more iterative.
[1720.42 → 1723.78] And so all of these different problem types you mentioned, different ones,
[1724.00 → 1727.08] I think on the website right now we mostly focus on the text-based ones.
[1727.16 → 1730.94] But again, we've seen these used successfully, and we'll continue to build out the areas
[1730.94 → 1733.20] for applying this to other modalities as well.
[1733.20 → 1738.52] But this paradigm is really agnostic to the data modality and most problem types, right?
[1738.66 → 1743.16] It's at its heart, it is a machine learning problem where you have a training set, and you have a model.
[1743.70 → 1748.94] And when your model is making mistakes, it's often due to what is or isn't reflected,
[1749.16 → 1750.88] you know, clearly enough in your training set.
[1751.42 → 1755.06] And so for any of these problems, you know, there are different types of labelling functions that you write
[1755.06 → 1758.16] for a classification problem versus an extraction problem or whatnot.
[1758.16 → 1763.30] But fundamentally, once you scrape off that top layer, it looks very similar.
[1763.90 → 1768.40] And so, you know, this platform really is meant to solve a wide variety of problem types
[1768.40 → 1772.74] and work in a bunch of different industries, you know, in verticals and whatnot.
[1772.88 → 1778.36] Because, you know, again, it's sort of under the hood, they're all relying on the same basic
[1778.36 → 1781.08] fundamental principles about how machine learning works.
[1781.72 → 1783.70] And then it was with that in mind that we built the platform.
[1788.16 → 1818.14] Thank you.
[1818.16 → 1822.92] Once again, that's changelog.com slash plus.
[1823.92 → 1846.10] So that was a good introduction.
[1846.10 → 1852.04] I am curious, though, earlier in the conversation, you talked about some of the third party integrations.
[1852.66 → 1855.42] And along with that, I'm kind of thinking from a workflow standpoint.
[1855.88 → 1861.44] So, you know, could you describe a little bit about how you might integrate in with other tools that are, you know,
[1861.52 → 1863.10] widely used within this industry?
[1863.60 → 1867.36] What kind of integrations you have and how that kind of really helps the practitioner
[1867.36 → 1870.66] get through the process of modelling that they're trying to do?
[1870.66 → 1871.10] Yep.
[1871.28 → 1876.12] One of the things that we learned from the open source project, it was the importance of having, you know,
[1876.16 → 1880.24] intuitive, natural modular interfaces to different parts of this pipeline.
[1880.44 → 1883.70] The labels, certainly the labelling functions as well, the models, all that.
[1884.10 → 1888.16] And so we kept that design principle very much in mind as we designed the platform.
[1888.16 → 1895.30] And we've made sure that every step of the pipeline can be done either in the GUI or via an SDK that we provide.
[1895.84 → 1901.32] And so that means that you can, you know, write labelling functions via these, you know, nice GUI, you know,
[1901.38 → 1902.22] builders that we've got.
[1902.22 → 1908.96] Or you can define, you know, completely arbitrary black box labelling functions via, you know, code in the notebook,
[1909.24 → 1911.36] push those up, and then they're treated the same way in the platform.
[1911.72 → 1912.94] Same thing with the training sets.
[1912.98 → 1917.52] You can create a training set and then go to the models page and identify the model that you want,
[1917.60 → 1919.42] set a few hyperparameters and train it there with a button.
[1919.88 → 1925.16] Or you can use the SDK to export your training set, train your own model, and then just re-register the predictions,
[1925.44 → 1929.80] you know, push them back up, just some, you know, very lightweight, assign certain UIDs, certain labels,
[1929.80 → 1932.32] and then use the analysis page to still guide you.
[1932.74 → 1936.48] And so it means that we're able to interact with a lot of different, you know,
[1936.54 → 1940.60] customer types and workflows that have different requirements for, you know,
[1940.60 → 1943.90] some people know we really just need to use our proprietary model.
[1944.02 → 1946.42] We know that nothing works as well as this does.
[1946.78 → 1947.68] That's totally fine.
[1947.78 → 1952.10] At that point, you can pull things down from the platform and then push up the results when you're done.
[1952.38 → 1955.92] For other people, it's actually, we've got a lot of, you know,
[1956.00 → 1958.70] training labels already available from crowd workers,
[1958.70 → 1961.76] or it's just as a natural part of our product, we're always getting feedback that we can use.
[1962.06 → 1965.40] But we'd really like to be able to be systematic about how we, you know,
[1965.52 → 1967.02] patch up failure modes that we have.
[1967.06 → 1969.86] And so we want to use the platform, you know, the analysis tooling especially,
[1970.02 → 1970.96] but maybe also the models.
[1971.16 → 1973.76] And so for them, they're able to start, you know, in that way.
[1973.76 → 1977.36] So really, it's that, you know, any piece of this can be, you know,
[1977.42 → 1979.32] that's the sort of the test we use for ourselves is,
[1979.64 → 1983.36] can I complete an application in Snorkel flow without ever opening up, you know,
[1983.40 → 1984.70] that tab of my browser?
[1984.70 → 1987.94] Or, you know, and the answer is yes, which makes it just sort of, you know,
[1988.06 → 1989.92] ultimately flexible, I guess, you know,
[1989.94 → 1991.86] platform for integrating with other workflows you may have.
[1992.52 → 1992.62] Gotcha.
[1992.98 → 1998.06] So, you know, you guys are, even though you're several years given the work ahead of time
[1998.06 → 2000.46] getting into the company, you mentioned that you're about a year and a half
[2000.46 → 2002.14] into the company's existence,
[2002.14 → 2005.24] which is pretty early in the lifetime of an organization.
[2006.08 → 2008.88] Recognizing that it takes time to get things out the door and stuff,
[2008.88 → 2013.68] what other gaps are you seeing in the industry that is, you know,
[2013.68 → 2015.32] more of that itching that you want to scratch,
[2015.32 → 2017.42] whether it be short-term or longer-term,
[2017.76 → 2020.80] what are you envisioning Snorkel flow evolving into?
[2021.26 → 2024.44] And what kinds of problems that you're not addressing today necessarily
[2024.44 → 2027.24] are you thinking about addressing for the future?
[2027.54 → 2031.26] When you guys are getting together and hanging out and talking about what-ifs,
[2031.38 → 2033.24] what are some of those what-ifs that you're willing to share?
[2033.72 → 2033.88] Yeah.
[2034.08 → 2036.26] So, yeah, a few different things come to mind.
[2036.26 → 2039.44] One of them is that, as I mentioned, I guess, a couple of times,
[2039.62 → 2041.08] there are different modalities to consider.
[2041.28 → 2043.60] And the way that you write labelling functions over images
[2043.60 → 2047.04] is fundamentally different from the way that you write labelling functions for text.
[2047.16 → 2049.36] And so just given where the market pull was initially,
[2049.36 → 2050.62] we've started focusing on text,
[2050.70 → 2054.16] but we absolutely plan to bring in some of that other research we've done
[2054.16 → 2056.66] as time goes on over the coming months and years.
[2057.20 → 2061.34] I'd say, in addition, another area that's fascinating to us
[2061.34 → 2063.54] where we would have this sort of unique leg up
[2063.54 → 2065.18] based on the approach that we're taking
[2065.18 → 2067.30] is the monitoring side of things.
[2067.46 → 2071.24] When you acknowledge that most applications are going to go deploy,
[2071.74 → 2076.24] it's not, great, I've got my model now, deploy it and set it and forget it.
[2077.00 → 2078.58] Like, test distributions change.
[2078.68 → 2079.52] The world shifts.
[2079.62 → 2080.74] People talk about different topics.
[2080.88 → 2081.96] Different words get different meanings.
[2082.42 → 2084.80] COVID was not a part of the discussion a year ago,
[2084.86 → 2089.54] and now it's a huge part of the societal fabric of what gets talked about on social media.
[2089.54 → 2094.82] So the fact that you do very frequently need to iterate on your models,
[2095.08 → 2097.00] improve them, as well as just sort of,
[2097.18 → 2100.68] you'd like to know preferably more than just a single number of,
[2100.92 → 2102.36] you know, the accuracy of my model.
[2102.42 → 2103.16] Is that going up or down?
[2103.52 → 2107.40] It's fascinating to see what types of examples
[2107.40 → 2109.38] am I starting to get more right or more wrong?
[2109.38 → 2111.22] What subsets of my data are, you know,
[2111.26 → 2114.56] are diverging basically from what they were when I was trained?
[2114.66 → 2118.02] And so what's fascinating is after you've written these labelling functions,
[2118.58 → 2122.24] they're essentially a bunch of different, like, hooks into your data set.
[2122.34 → 2126.48] They each observe different slices of your data that have different common properties,
[2126.72 → 2129.76] and these could effectively become monitoring tools for you
[2129.76 → 2135.38] because you can now observe how those labelling functions increase or decrease in coverage over time
[2135.38 → 2139.10] when applied on sort of the new data that's streaming through your application
[2139.10 → 2142.76] and inform you when you can basically set up automated alerts
[2142.76 → 2145.80] showing you now's the time to go and update things
[2145.80 → 2150.56] or here's some suspicious activity going on based not just on did the number go up or down,
[2150.62 → 2153.16] but, like, we're seeing movement in different parts of the space
[2153.16 → 2154.28] where your model's operating.
[2155.02 → 2155.72] Take a look.
[2156.16 → 2160.22] So that maybe appeals more to the technical, you know, nerdy side of things,
[2160.34 → 2162.02] but I think it's a fascinating problem,
[2162.10 → 2164.06] one where you've got that information, right?
[2164.06 → 2169.40] You have already identified for you these very interesting angles on your problem,
[2169.56 → 2174.22] and so why not use those to help guide the sort of post-deployment life of a model?
[2174.66 → 2176.94] I guess at this point, as you were answering that,
[2177.14 → 2179.78] I want to ask within the limits, obviously, of what you can share,
[2180.32 → 2183.08] customers that you have, what are some of the fascinating things
[2183.08 → 2184.90] that you've seen customers doing with this
[2184.90 → 2189.30] that may be particularly things that were outside what you might have expected?
[2189.78 → 2191.70] The kinds of things, you know, we all have problems.
[2191.70 → 2195.46] Everybody in this industry has areas of focus that we're addressing.
[2195.92 → 2198.52] What are some of the things that made you surprised?
[2198.72 → 2202.26] And, you know, people went, oh, okay, hadn't expected that to see that,
[2202.32 → 2203.24] or just for plain cool.
[2203.44 → 2205.38] Just something that someone's doing that's just like, wow,
[2205.50 → 2208.26] I love having our platform involved in that.
[2208.64 → 2208.84] Yeah.
[2209.04 → 2211.92] You know, two things that I've found personally very cool.
[2212.16 → 2216.52] One of them is the privacy preservation aspect of this approach.
[2216.52 → 2220.62] That was not necessarily a, you know, top priority or top of mind
[2220.62 → 2222.96] when we were developing these techniques at Stanford.
[2223.06 → 2225.26] It was often, you know, on problems where it's just,
[2225.36 → 2226.24] I'm trying to get a good result.
[2226.30 → 2227.00] I want a high quality.
[2227.06 → 2227.90] How can I get high quality?
[2228.22 → 2230.10] But it's been really cool to see different companies
[2230.10 → 2233.58] that have the very desirable goal of,
[2234.04 → 2237.04] you know, we'd like to have our data being seen by fewer humans.
[2237.04 → 2239.02] We'd like to have fewer people reading your emails,
[2239.20 → 2241.98] fewer people seeing your medical or financial records.
[2241.98 → 2244.76] And how can we do that while not sacrificing the quality
[2244.76 → 2245.80] of our machine learning models?
[2246.28 → 2247.92] And so it's been fascinating to see them,
[2248.30 → 2250.68] you know, in working with them, coming up with these setups
[2250.68 → 2254.20] where now they can take a very small approved subset of the data
[2254.20 → 2256.54] to give them ideas for how to write labelling functions
[2256.54 → 2259.26] or to label like a test set to give them a sense of overall how it's quality.
[2259.74 → 2263.24] But then the vast majority of their data never gets seen by a human now.
[2263.24 → 2267.66] They can take these programs they've developed to go label those automatically,
[2267.82 → 2268.88] use them to train a model,
[2269.10 → 2271.88] and then get back just sort of the final weights of the model.
[2272.40 → 2274.16] And it's really, you know, neat to see.
[2274.22 → 2276.14] And I'd love to see that sort of thread continue
[2276.14 → 2278.98] because, I mean, not just for the privacy preservation standpoint,
[2279.10 → 2281.40] but also, you know, we keep seeing, you know,
[2281.40 → 2284.42] articles about the PTSD almost that you get, you know,
[2284.42 → 2286.84] as an annotator over these awful domains.
[2286.94 → 2288.46] I mean, you hear about some for social media.
[2288.66 → 2289.88] Yeah, there are some horrendous ones.
[2289.88 → 2291.90] I mean, actually, even during the Stanford days,
[2291.94 → 2294.26] we worked with DARPA on a project for human trafficking.
[2294.48 → 2296.06] In their case, it was more out of, I think,
[2296.12 → 2299.28] necessity of keeping up with a very rapidly moving environment
[2299.28 → 2301.30] where it's these adversarial settings.
[2301.30 → 2303.76] And so your training set's always losing its value
[2303.76 → 2304.80] because things are always changing.
[2304.90 → 2307.60] And so they needed to be able to create training sets very quickly.
[2307.60 → 2309.10] And they did with Snorkel, which was cool.
[2309.26 → 2312.14] But also conveniently now, there are that many fewer people
[2312.14 → 2315.12] who need to spend a day sitting in front of these awful,
[2315.22 → 2316.38] you know, human trafficking ads.
[2316.38 → 2319.70] So I think the privacy standpoint is very cool.
[2320.12 → 2323.24] I think another interesting application we've seen was there.
[2323.30 → 2326.60] We had one customer who, and I'll try to appropriately obfuscate here,
[2326.68 → 2330.74] but they had an application that was affected, we'll say, by COVID.
[2331.14 → 2334.60] When you suddenly have the stock market, you know, plummeting,
[2334.72 → 2337.42] and there are certain risks associated with that for different businesses.
[2337.42 → 2341.00] And we were in the middle of a POV engagement with them,
[2341.08 → 2343.84] sort of their test running the product to see how it worked for them.
[2344.40 → 2346.22] And they came to us and said, okay, here's actually,
[2346.44 → 2348.68] this was not part of our scoped, you know, work,
[2348.80 → 2351.20] but this suddenly matters a lot to us.
[2351.24 → 2352.98] And our typical process would take about a month.
[2353.38 → 2354.46] Do you think you could help us?
[2354.56 → 2357.34] Could we try and use Snorkel to get some result faster?
[2357.88 → 2359.30] And so since it was very early on,
[2359.34 → 2361.76] and we hadn't necessarily had a lot of time to train them yet using the platform,
[2361.76 → 2363.70] we said, sure, we've got some ideas.
[2363.70 → 2366.92] You know, give us a sec, threw three of us in a war room for the day,
[2367.06 → 2369.32] ordered some burritos, you know, and hacked away.
[2369.70 → 2372.80] And by the end of the day, we were able to extract the terms that they needed
[2372.80 → 2376.00] with over 99% accuracy on their application.
[2376.00 → 2379.34] And that was achievable with a model that was trained on,
[2379.44 → 2383.30] you know, tens of thousands of examples, which we didn't need to label.
[2383.42 → 2384.70] We were able to quickly come up with,
[2385.04 → 2387.34] what are the generalizable, you know, rules and principles here
[2387.34 → 2390.22] that we could use to create a training set to train a model that now,
[2390.30 → 2392.76] you know, can handle edge cases and things much better than these rules,
[2392.76 → 2394.68] and then get the high quality that they needed.
[2394.68 → 2399.50] So that sort of, you know, live action, the nerds save the day, right?
[2399.72 → 2400.54] Kind of moment.
[2400.64 → 2401.42] No, it's a good story.
[2401.50 → 2402.22] Super cool to see.
[2402.52 → 2404.22] You've raised several interesting points there.
[2404.38 → 2406.90] You know, one of which is the fact that in real life,
[2406.92 → 2408.50] as this technology is more pervasive,
[2408.92 → 2413.82] that these dynamic ever-changing data sets are a reality we have to contend with.
[2414.12 → 2417.94] I mean, are you seeing the industry getting more flexible at large?
[2417.96 → 2419.92] In addition, you know, obviously you guys are,
[2419.92 → 2424.04] you know, in terms of thinking about the fact that that's something that has to be accommodated.
[2424.14 → 2428.50] But I would expect that that is something that has to be addressed more and more.
[2428.58 → 2430.64] Do you have any insight into kind of,
[2430.90 → 2435.92] or any thoughts into where we're going in terms of us moving along this curve
[2435.92 → 2440.82] from these, you know, static label data sets that we were talking about historically
[2440.82 → 2443.78] at the beginning of the conversation to this dynamic, you know,
[2443.80 → 2447.62] especially since COVID has struck, the ever-changing world on a day-to-day basis.
[2447.62 → 2450.08] You know, what's that trajectory look like?
[2450.12 → 2451.82] And how are you guys preparing for that?
[2452.24 → 2452.44] Yeah.
[2452.62 → 2457.70] So I think we're definitely seeing an increased awareness of some of these issues.
[2457.92 → 2461.98] I think a lot of companies are still trying to figure out how to address it in the right way.
[2462.26 → 2466.46] We see companies realizing that, you know, schema lock-in is becoming this problem for us
[2466.46 → 2468.86] because real problems, you know, change.
[2468.98 → 2469.82] Our objectives change.
[2469.88 → 2470.92] We learn more about the problem.
[2470.92 → 2475.70] What we thought was a positive or negative classification problem is actually positive,
[2475.82 → 2476.44] negative, or neutral.
[2476.66 → 2479.68] And then all of our old labels are garbage now because we don't know where the neutrals are
[2479.68 → 2480.50] and the positives and negatives.
[2480.86 → 2484.28] So people are being burnt by some of these problems.
[2484.42 → 2488.44] And so I think that's part of the reason why we've had such early success with sort of inbound
[2488.44 → 2492.82] interest more than we could even handle at first, because people are aware now of some
[2492.82 → 2494.10] of the costs that come with machine learning.
[2494.38 → 2497.72] The promise of machine learning is very much being broadcast and how it's, you know,
[2497.72 → 2501.56] the future and solves a lot of problems, but there do end up being these very practical,
[2502.08 → 2506.90] I won't say necessarily limitations, but, you know, gotchas or, you know, costs really,
[2507.00 → 2508.64] right, that you need to be aware of.
[2508.94 → 2513.08] So I see this reflected a little bit in the way that companies are starting to prioritize
[2513.08 → 2517.90] more the ability to see the like, where did my model learn this?
[2517.98 → 2519.42] Like that auditability kind of.
[2519.60 → 2519.86] Yes.
[2520.24 → 2522.36] We're kind of touching on kind of AI ethical issues.
[2522.36 → 2524.68] You've talked about auditability and privacy and such.
[2524.94 → 2525.02] Yeah.
[2525.02 → 2529.34] Totally, totally see that as you're kind of maturing your way through the process here.
[2529.80 → 2530.14] Exactly.
[2530.66 → 2530.88] So, yeah.
[2530.94 → 2533.50] So, I mean, they realize that that's important in a way that they maybe didn't before.
[2533.76 → 2537.48] I think they're also realizing just from an economic standpoint that there's this, that
[2537.48 → 2540.56] the training data is not a one-time cost.
[2540.72 → 2542.50] This is a capital expenditure.
[2542.66 → 2544.28] This is an asset that loses value.
[2544.38 → 2546.20] There is a half-life to these things.
[2546.20 → 2551.14] And so you start seeing these, you know, ongoing, regular cyclical budgets to get the training
[2551.14 → 2553.56] data, even just for a single application.
[2553.76 → 2557.86] Not, we need more data to train more models for more applications, but to keep this application
[2557.86 → 2558.68] fresh and alive.
[2558.82 → 2560.02] That's a great insight right there.
[2560.42 → 2560.62] Yeah.
[2560.70 → 2561.64] Well, it's fascinating.
[2561.86 → 2567.44] And it changes the way that you account for the cost of different applications you might
[2567.44 → 2567.86] use, right?
[2567.86 → 2572.18] Because there's a certain way that you maintain imperative, we'll call it software 1.0.
[2572.18 → 2577.08] And there's a different way that you maintain this machine learning-based software 2.0, you
[2577.08 → 2578.10] know, way of solving a problem.
[2578.28 → 2579.38] It's something people are learning.
[2579.52 → 2582.44] And I think that's part of all interesting part of the conversations that we're having
[2582.44 → 2586.22] with different customers as they realize how this can maybe change the way that they
[2586.22 → 2588.10] approach their machine learning stack in general.
[2588.62 → 2588.70] Okay.
[2588.88 → 2594.00] So, I guess as we wind up here, I'm finally getting to ask what is always my favourite question
[2594.00 → 2596.72] anytime we're getting to talk to someone such as yourself.
[2596.82 → 2599.12] And that is, you know, blank sheet of paper.
[2599.12 → 2604.14] What are you excited about right now in the space of machine learning and AI?
[2604.66 → 2608.90] You know, what is the thing that has captured your imagination, whether it's work-related
[2608.90 → 2611.40] or whether it's not work-related and just something cool out there?
[2611.50 → 2612.46] What's got you going?
[2612.92 → 2617.22] That's the thing I'm really interested in tracking either on my own or through the company
[2617.22 → 2617.64] or whatever.
[2617.80 → 2618.20] What's cool?
[2618.64 → 2619.78] That's a very good question.
[2619.96 → 2621.04] There's a lot, I know.
[2622.86 → 2624.12] So many things.
[2624.54 → 2628.94] I'd say there are a number of areas that are super important, super hard.
[2628.94 → 2629.88] But super important.
[2630.22 → 2633.78] And I'm glad to see that they're getting the attention that they deserve, at least that
[2633.78 → 2634.78] we're training in the right direction.
[2635.76 → 2640.78] And that stems around, I mean, the privacy, the fairness, the bias.
[2641.32 → 2643.70] A lot of that, I think it's just super hard.
[2643.76 → 2646.88] If anyone says that they've got a solution to that problem, I'd be very dubious.
[2647.62 → 2650.60] But I think we are, you know, marching toward progress there.
[2650.78 → 2654.10] And that's something that I'm certainly going to watch with great interest and hope that we
[2654.10 → 2655.60] can be a part of the solution there.
[2655.84 → 2656.64] That's one piece.
[2656.64 → 2663.14] But when I think maybe a little closer to my personal research agenda and history, a
[2663.14 → 2668.40] lot of that's centred around how you get signal from a person into a machine, right?
[2668.78 → 2673.70] And so a lot of my research through the years has been seeing kind of how high up the stack
[2673.70 → 2674.18] can we go?
[2674.66 → 2679.28] Like there's this figure in my dissertation that compares basically the computer programming
[2679.28 → 2680.76] stack to like the machine learning stack.
[2680.76 → 2684.88] So, you know, computer programming, computers run on these ones and zeros, right?
[2684.94 → 2688.88] They run on individual bytes and bits, but nobody writes ones and zeros code.
[2689.10 → 2694.24] You write in higher level interfaces like a C or even like a SQL or something that compile
[2694.24 → 2698.52] down sometimes multiple times into this low level code that you're then going to actually
[2698.52 → 2698.98] run on.
[2699.40 → 2703.06] And I'd say similarly, machine learning runs on individual labelled examples.
[2703.26 → 2704.06] That's how we train it.
[2704.08 → 2706.30] That's how we express information to it.
[2706.30 → 2712.08] But it feels fairly naive, actually, to one by one write these ones and zeros, write these
[2712.08 → 2713.72] trues and false son our individual examples.
[2713.92 → 2717.92] And so I think that there are a lot of fascinating things that can be done around
[2717.92 → 2723.72] higher level interfaces of expressing expertise that then, you know, in various automated or
[2723.72 → 2728.26] just sort of assisted ways can eventually result in the training sets that have the properties
[2728.26 → 2730.82] you need to actually communicate with your model.
[2730.94 → 2732.74] You know, use the compiler, right?
[2732.74 → 2736.18] Essentially, the optimization algorithm that's in place to transfer that information.
[2736.44 → 2738.60] So that's a fairly high level description.
[2738.68 → 2741.30] But I think there are interesting things yet to be done there.
[2741.66 → 2742.66] Well, thank you for sharing that.
[2742.74 → 2743.34] I appreciate it.
[2743.36 → 2746.24] Brayden, thank you so much for coming on to Practical AI.
[2746.50 → 2749.94] It was a great conversation and looking forward to our next one.
[2750.02 → 2751.48] Looking forward to having you back sometime soon.
[2751.82 → 2752.16] Absolutely.
[2752.38 → 2753.00] Thanks for having me.
[2753.30 → 2753.68] Thank you.
[2756.88 → 2759.80] This is our final episode of 2020.
[2759.80 → 2765.14] We're taking a couple of weeks off to relax, re-energize and gear up for the new year.
[2765.76 → 2770.68] If you want more Practical AI goodness during the break, I personally recommend the Waymo
[2770.68 → 2775.28] episode with Drag Anglo, the one where Peter Wang drops a bunch of history and knowledge
[2775.28 → 2779.20] on the guys, and the human compatible AI episode with Stuart Russell.
[2779.52 → 2781.60] I'll link those three up in the show notes for you.
[2782.58 → 2785.72] Practical AI is hosted by Chris Benson and Daniel Whiten ack.
[2785.72 → 2789.64] It's produced by me, Jared Santo, and our music is brought to you by the Beat Freak,
[2789.76 → 2790.54] Break master Cylinder.
[2790.98 → 2792.78] We have awesome sponsors who get it.
[2793.00 → 2795.72] Thanks to Vastly, Linde, and Launch Darkly for their support.
[2796.26 → 2797.02] That's our show.
[2797.32 → 2798.48] We'll talk to you again next year.
[2798.48 → 2828.46] We'll be right back.
