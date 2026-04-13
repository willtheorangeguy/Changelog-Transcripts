[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.42] This is where conversations around AI, machine learning, and data science happen.
[93.42 → 98.20] Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.44 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.48 → 102.28] And now onto the show.
[107.16 → 111.02] Welcome to another episode of Practical AI.
[111.36 → 112.84] This is Daniel Whiten ack.
[112.96 → 115.98] I'm a data scientist with SIL International,
[115.98 → 119.84] and I'm joined, as always, by my co-host, Chris Benson,
[120.26 → 123.24] who is a principal AI strategist at Lockheed Martin.
[123.66 → 124.30] How are you doing, Chris?
[124.44 → 125.32] Doing great, Daniel.
[125.36 → 125.94] How's it going today?
[126.44 → 127.46] It's going good.
[127.56 → 131.06] It is a snowy day here in the Midwest.
[131.46 → 134.68] Last night, we lost our power at our house,
[135.04 → 135.94] but it's back now,
[136.08 → 138.86] so spent the night putting logs on the fire,
[139.04 → 140.26] which wasn't so bad.
[140.56 → 141.04] Oh, boy.
[141.16 → 142.30] At least you got your power back.
[142.36 → 144.18] You're not podcasting on the generator, huh?
[144.18 → 144.62] Exactly.
[145.36 → 146.98] Not podcasting on the generator.
[147.26 → 148.76] Internet is back for work,
[148.84 → 150.52] and all things are good there.
[150.68 → 153.32] So I'm guessing it's not quite the same in Georgia,
[153.50 → 154.82] but by Georgia standards,
[154.92 → 156.20] it's quite cold here, actually.
[156.48 → 158.42] So, yeah, definitely we're going,
[158.50 → 159.06] what happened?
[160.34 → 161.88] Since it's cool outside,
[162.06 → 163.96] it's a good day to stay inside.
[164.40 → 165.90] We got a cool topic, don't we?
[166.14 → 166.84] Yeah, yeah.
[167.24 → 168.28] That was a good one.
[168.82 → 171.94] And learn about some cool new stuff
[171.94 → 174.14] that's happening in the AI world
[174.14 → 176.68] and particularly around machine learning
[176.68 → 179.00] and AI tooling and apps.
[179.74 → 181.88] And today we have with us Adrian Troy,
[182.10 → 184.68] whose co-founder and CEO at Streamlet.
[184.82 → 185.42] Welcome, Adrian.
[185.68 → 187.20] Hey, thanks so much for having me.
[187.24 → 188.10] I'm thrilled to be here.
[188.96 → 191.38] Yeah, so maybe before we jump into
[191.38 → 193.84] machine learning and AI apps
[193.84 → 196.70] and all that goes along with that,
[196.78 → 198.94] could you just give us a little bit of an idea
[198.94 → 199.84] about your background
[199.84 → 201.84] and how you ended up where you're at now?
[202.30 → 202.86] Sure.
[203.08 → 204.58] I started off my professional career
[204.58 → 206.94] as a professor at Carnegie Mellon,
[207.14 → 210.36] and I was working on large-scale simulations
[210.36 → 211.82] of smoke and water.
[212.54 → 215.34] And so got to see really the complexities
[215.34 → 219.54] of running these really long-running computations,
[219.66 → 221.32] and it's very similar to AI in that way.
[221.32 → 224.72] And was that for environmental sort of applications
[224.72 → 227.96] or just for better understanding
[227.96 → 229.38] how to model those things?
[229.66 → 230.10] Yes.
[230.58 → 234.06] So our application domain was computer graphics, actually.
[234.32 → 236.98] So basically making realistic virtual worlds
[236.98 → 238.54] indistinguishable from reality.
[238.78 → 239.06] Gotcha.
[239.46 → 240.86] And the work that we did, though,
[240.88 → 242.08] was actually quite fundamental.
[242.08 → 244.40] So it was really about how do you model
[244.40 → 247.46] the fluid equations, for example, on a computer
[247.46 → 248.80] and what sort of efficiencies
[248.80 → 251.14] are made possible by the physics.
[251.92 → 252.14] Awesome.
[252.32 → 253.28] Yeah, that's fascinating.
[253.68 → 255.54] Did that kind of lead you naturally
[255.54 → 258.62] into the whole machine learning and AI world,
[258.88 → 260.62] or was that something you developed
[260.62 → 261.46] an interest in later?
[261.66 → 262.78] Yeah, no, it was.
[263.22 → 266.56] We were actually pioneering AI-like techniques
[266.56 → 269.12] in the space of fluid simulation
[269.12 → 270.64] and cloth simulation.
[271.32 → 273.82] And so we did a lot of so-called
[273.82 → 275.20] data-driven simulation,
[275.38 → 277.34] which means you capture a huge amount of data
[277.34 → 279.12] about how some phenomenon works,
[279.12 → 281.18] and then you can build an efficient model.
[281.28 → 282.86] So it really is a form of machine learning.
[283.54 → 285.60] So yeah, worked on that.
[285.74 → 288.56] And then also built some pretty large communities.
[288.56 → 291.00] So I was the founder of Fold it,
[291.24 → 293.88] which was a protein folding video game,
[294.30 → 295.58] and then Eternal,
[295.68 → 298.06] which was an RNA folding video game
[298.06 → 299.24] in collaboration with Stanford.
[299.24 → 301.76] So I had a sort of weird career,
[301.88 → 304.08] which was a mixture of doing
[304.08 → 306.08] really large-scale computing on the one hand,
[306.12 → 308.28] and then also building these online communities
[308.28 → 309.22] on the other.
[309.70 → 312.22] And so those came together in Streamlet.
[312.74 → 314.96] Yeah, so the communities that you're talking about,
[315.06 → 315.62] this is where,
[315.76 → 318.38] and I think I've read about this before,
[318.74 → 320.58] is the idea with those things,
[320.64 → 321.22] it was like,
[321.38 → 322.98] we've got this really complicated problem,
[322.98 → 325.58] and we want people to play this game
[325.58 → 329.60] to explore the solution space in some ways.
[329.76 → 330.66] That's exactly right.
[331.08 → 334.56] Yeah, so these were non-technical people
[334.56 → 337.30] interacting with your application
[337.30 → 340.08] that had some sort of scientific
[340.08 → 341.88] or technical implications.
[341.88 → 343.28] And actually, could you provide
[343.28 → 344.72] just kind of example of that,
[344.78 → 345.44] just to make it real?
[345.84 → 349.92] Yeah, so an example is in the game Eternal,
[350.18 → 352.78] which I recommend everyone just go and check out.
[353.14 → 354.20] EternaGame.org.
[354.60 → 355.52] Super fun and interesting.
[356.14 → 360.22] So what we were doing was designing RNA's
[360.22 → 362.86] that, because these are tiny molecules in the body
[362.86 → 363.82] that can, for example,
[364.32 → 365.94] switch between two shapes
[365.94 → 367.52] under certain circumstances.
[368.16 → 370.06] And so this is actually the mechanism
[370.06 → 372.02] by which a lot of so-called,
[372.16 → 374.38] quote-unquote, computation happens in the cell.
[374.82 → 376.20] And so being able to master this
[376.20 → 379.28] is really a sort of fundamental building block
[379.28 → 381.38] of like building next-generation therapeutics.
[381.38 → 383.92] And it turns out that players playing this game,
[384.30 → 385.76] some of them have really developed
[385.76 → 387.70] like an amazing sort of technique and intuition
[387.70 → 389.52] about how to design molecules like this.
[389.78 → 391.22] So it's actually, it's really remarkable.
[391.44 → 392.76] And, you know, we've published papers
[392.76 → 394.38] in sort of top journals
[394.38 → 395.96] based on discoveries by players.
[396.10 → 397.38] So it's really sort of remarkable.
[397.76 → 400.24] You can join, and anyone can join
[400.24 → 402.16] and do the tutorials and learn how to do this.
[402.16 → 408.30] And in a way, I do see these crazy scientific computing games
[408.30 → 410.02] as precursors to Streamlet
[410.02 → 413.48] because what we did was sort of translate
[413.48 → 416.98] one world into another, you know, computing, basically.
[417.20 → 419.10] And so in Fold it and Stereo,
[419.18 → 422.38] we were sort of translating the world of molecules
[422.38 → 424.84] and, you know, biomolecules into a game.
[425.38 → 427.92] And in Streamlet, which we just released,
[427.92 → 431.06] we're essentially translating the world of app development
[431.06 → 433.82] into a sort of the language of machine learning.
[434.48 → 436.66] And I think in all of these cases,
[437.08 → 438.58] you know, as soon as we released it,
[438.84 → 441.86] community kind of lit up and just was so excited.
[442.42 → 444.16] And I remember before the podcast,
[444.26 → 444.92] you were just saying,
[445.36 → 446.70] half your tweets are about Streamlet.
[447.10 → 448.50] And I think it's because it's cool
[448.50 → 451.00] to give people new powers they didn't have before
[451.00 → 452.92] and to sort of act as an intermediary
[452.92 → 454.06] between two different worlds.
[454.06 → 457.82] Yeah, it's like I've always had a desire personally
[457.82 → 462.52] to get my hands dirty with like front-end engineering.
[462.98 → 464.26] But at the same time,
[464.48 → 466.74] I've always been so busy with other things
[466.74 → 469.90] that I'm like, oh, well, you know, my stuff is cool.
[470.08 → 471.64] But like in a lot of ways,
[471.64 → 475.28] what you're doing on the back end is totally transparent
[475.28 → 479.22] or actually should in many ways be transparent to users.
[479.22 → 484.84] But always like having a desire to create cool app things.
[485.84 → 488.84] I've never really got much into that world
[488.84 → 495.78] other than like random HTML or CSS sort of like task.
[496.14 → 498.52] So yeah, I definitely could see like it is kind of
[498.52 → 502.14] a new superpower that people probably wish that they had.
[502.34 → 504.42] But there are a lot of barriers there, I guess.
[504.86 → 506.86] You know, it's been such a kind of weak point
[506.86 → 510.24] as people really try to get into this space
[510.24 → 512.06] in terms of AI technologies
[512.06 → 514.54] and make them meaningful in what they're doing
[514.54 → 515.84] for work or their life or whatever.
[516.26 → 517.76] And being able to connect that in with,
[517.88 → 518.82] you know, through apps and stuff.
[518.98 → 521.46] It's been a huge area that needed attention.
[521.46 → 522.86] And it sounds like Streamlet
[522.86 → 524.28] is very much focusing on that.
[524.84 → 524.98] Yeah.
[525.16 → 527.24] And maybe for the benefit of your listeners
[527.24 → 528.44] who haven't heard of it,
[528.46 → 530.80] I'm happy to also give a really brief description
[530.80 → 532.02] of what it is.
[532.82 → 533.92] Do you mystify it?
[534.02 → 534.70] Yeah, please do.
[534.76 → 536.12] I think this would be a great time for that.
[536.12 → 536.30] Yeah.
[536.48 → 539.32] So basically, Streamlet is an app framework
[539.32 → 542.04] for machine learning engineers and data scientists.
[542.72 → 545.78] And we were, you know, machine learning engineers.
[546.38 → 549.26] And so we took the starting point of, you know,
[549.28 → 551.76] what we saw as the machine learning engineering workflow.
[552.42 → 554.10] And we asked,
[554.24 → 557.26] how can we make a sort of machine learning script
[557.26 → 561.26] into an app as simply as possible
[561.26 → 563.88] so that it basically feels like a scripting exercise?
[563.88 → 565.66] And so what Streamlet is,
[565.66 → 567.84] is just a package that you can install
[567.84 → 569.94] that gives you a bunch of,
[570.22 → 570.60] through pip,
[571.04 → 572.50] and it gives you a bunch of functions.
[573.18 → 574.14] And those functions,
[574.34 → 577.76] you can just interleave an existing ML code
[577.76 → 578.88] with these functions.
[578.88 → 581.22] And they essentially make things parametrizable.
[581.58 → 583.04] They do a little bit of layout.
[583.04 → 586.04] And they turn your code into a beautiful app.
[586.70 → 587.96] And it's really true.
[588.50 → 589.66] And as you pointed out,
[589.72 → 591.66] there's a lot of interesting tech
[591.66 → 593.24] just below the surface
[593.24 → 594.82] that makes that possible.
[595.02 → 597.22] We have a multithreaded server
[597.22 → 598.30] that starts in the background.
[598.60 → 599.46] There's WebSockets
[599.46 → 602.06] shuttling information back and forth to the browser.
[602.28 → 603.72] There's a whole browser app
[603.72 → 604.94] that's interpreting this
[604.94 → 606.32] and creating what you see on the screen.
[606.32 → 608.92] But all of that kind of goes away
[608.92 → 610.04] from the user's perspective.
[610.04 → 612.16] And you just get a really,
[612.36 → 615.00] a couple dozen magical Python commands
[615.00 → 619.26] that transform a machine learning script
[619.26 → 620.18] or a data science script
[620.18 → 623.56] into an app that you can use
[623.56 → 624.40] and share with others.
[624.94 → 626.94] Yeah, that's really great context.
[627.22 → 628.12] And as you mentioned,
[628.22 → 630.02] there's a lot to dig into there.
[630.18 → 633.76] Maybe next we could kind of just set the stage.
[633.76 → 637.30] You've talked about like the RNA stuff that you did.
[637.42 → 639.70] And we've talked about what Streamlet is.
[640.26 → 645.22] Maybe we could dive into why creating apps
[645.22 → 647.30] or these tools or interfaces
[647.30 → 650.72] is something that is relevant
[650.72 → 654.38] to particularly machine learning and AI practitioners.
[654.76 → 657.60] So why isn't it just the case that,
[657.88 → 659.50] oh, like machine learning and AI people
[659.50 → 662.38] should just write their code in Python scripts
[662.38 → 663.74] and then pass things off to the machine
[663.76 → 666.26] to front end engineers to make something pretty?
[666.36 → 670.52] Why is there this need to have like data scientists
[670.52 → 673.30] or AI practitioners create apps themselves?
[674.12 → 675.76] Yeah, that's a great question.
[675.92 → 678.34] So the first sort of implicit observation
[678.34 → 680.78] is that they do need to create apps.
[681.16 → 682.60] And this is something that I've seen,
[682.70 → 683.66] you know, after Carnegie Mellon,
[683.72 → 684.66] I went to Google X
[684.66 → 686.40] and then I went to Zoo
[686.40 → 688.00] and built self-driving cars.
[688.00 → 690.86] And every single ML team I've seen,
[691.40 → 692.90] you end up creating apps.
[693.04 → 694.88] And so I'll give you some examples
[694.88 → 696.58] from the self-driving car space.
[696.92 → 699.96] We had an app that allowed engineers to run simulations.
[700.50 → 701.58] We had an app that allowed them
[701.58 → 703.12] to search all of our simulations
[703.12 → 704.74] and compare two different simulations
[704.74 → 705.60] with different parameters.
[706.10 → 708.50] We had API endpoints that you could go to
[708.50 → 710.66] and see subsets of all the data that we collected
[710.66 → 711.44] and look at images.
[711.44 → 715.08] And so there was actually really this constellation,
[715.28 → 717.24] this sort of application layer that was built
[717.24 → 719.16] that was sort of a focal point.
[719.56 → 721.34] It was like the bonfire of the team.
[721.42 → 722.52] It's where we all got together
[722.52 → 724.00] and communicated and chatted.
[724.30 → 727.40] So that is actually a really crucial part
[727.40 → 728.36] of the ML workflow
[728.36 → 729.92] is building these internal apps,
[730.04 → 731.58] especially in a non-trivial project.
[732.28 → 734.74] And similarly, an important thing
[734.74 → 736.36] for machine learning and data scientists
[736.36 → 738.82] is to build apps for external consumption.
[738.82 → 742.22] So often other teams need to consume models
[742.22 → 743.46] in various ways
[743.46 → 745.54] and they need sort of an application layer to do that.
[745.92 → 747.64] We're in talks with a very big company
[747.64 → 749.32] to use Streamlet in production
[749.32 → 751.64] to allow their huge sales force
[751.64 → 753.72] to make interesting recommendation decisions.
[754.28 → 757.06] So it's really both for internal and external users.
[757.26 → 757.96] And then the question is,
[758.02 → 760.94] well, why don't you want ML engineers
[760.94 → 763.20] writing in Flask, for example,
[763.42 → 765.58] or using an app team?
[765.86 → 767.88] And the answer is that those things
[767.88 → 769.74] really, really slow down the cycle.
[770.16 → 771.16] So, you know, for example,
[771.34 → 773.78] a tool that we used all the time at Zoo
[773.78 → 775.42] was the scenario replay tool,
[775.54 → 777.78] which was if the car did something unexpected,
[778.00 → 779.06] we would want to be able to go back
[779.06 → 780.66] and see every single sensor reading
[780.66 → 782.94] and everything all in one web page
[782.94 → 784.22] and scrub through it, for example.
[784.74 → 787.70] And that tool required new features
[787.70 → 788.52] like every week.
[789.28 → 791.26] You know, we'd be developing a new sensor
[791.26 → 792.30] that had to be displayed
[792.30 → 794.84] and we had a different data set for vision
[794.84 → 796.64] and we had to be able to switch between them, etc.
[796.64 → 801.06] So these tools require constant new features.
[801.70 → 803.94] And so it's really empowering
[803.94 → 805.86] to be able to create them yourself
[805.86 → 807.04] easily and beautifully
[807.04 → 809.82] and then, you know, directly iterate on them
[809.82 → 811.70] and directly serve them to your users,
[811.80 → 813.16] be they other members of your team
[813.16 → 814.38] or other people in the company.
[814.86 → 816.50] So that's really the power
[816.50 → 819.02] of being able to write apps quickly and easily
[819.02 → 821.04] and in a flow that you might expect.
[821.34 → 822.54] And I think that's why the community
[822.54 → 824.06] has been so receptive.
[824.06 → 826.08] So I guess one of the questions
[826.08 → 827.60] I wanted to ask up front was,
[828.00 → 829.80] you know, as you're doing these GUI things,
[829.92 → 831.72] you know why not just use Jupyter
[831.72 → 833.84] given the fact that if you're a user out there,
[834.10 → 836.76] given the fact that it is so broadly deployed,
[836.94 → 838.54] it's kind of become the standard way
[838.54 → 840.20] that people are starting out.
[840.44 → 842.62] And, you know, other than the fact
[842.62 → 844.32] that you might want to show things
[844.32 → 845.38] to non-technical people,
[845.48 → 846.76] recognizing that not everyone
[846.76 → 847.86] looks at Jupyter Notebook,
[847.98 → 849.36] what are some of the advantages
[849.36 → 850.60] of doing it this way?
[851.10 → 852.78] Could you kind of talk about that a little bit
[852.78 → 853.76] about using it internally?
[854.24 → 854.48] Totally.
[854.88 → 857.02] So I would say that Jupyter,
[857.20 → 859.00] first, we ourselves use Jupyter
[859.00 → 860.18] alongside with Streamlet
[860.18 → 862.48] so that they don't exclude one another at all.
[863.08 → 865.38] Jupyter, we feel, is centred
[865.38 → 867.44] on the EDA workflow,
[867.64 → 870.74] the exploratory data analysis workflow.
[871.30 → 873.12] And it's a fantastic tool for that.
[873.12 → 874.60] And then it sort of branched out
[874.60 → 877.22] into making apps a little bit more,
[877.46 → 879.14] being, you know, an expository tool
[879.14 → 879.98] of various kinds.
[880.12 → 882.22] And those are all great adjacent use cases.
[883.02 → 884.34] Streamlet was really founded
[884.34 → 886.44] on the idea of building
[886.44 → 888.12] interactive apps really easily.
[888.38 → 892.16] And so we have a different workflow.
[892.78 → 894.56] It's, I think, very, very simple.
[894.74 → 895.46] It's very lightweight.
[895.66 → 896.82] It's super easy to understand.
[897.22 → 898.78] And it's slightly difficult to describe.
[898.96 → 899.82] You just have to try it.
[900.04 → 900.78] You know, in essence,
[900.78 → 901.88] we allow you to sprinkle
[901.88 → 903.56] these interactive widgets
[903.56 → 904.40] throughout your code,
[904.54 → 905.64] and then we sort of organize it
[905.64 → 906.88] into an app very easily.
[907.46 → 909.00] And I think it's that simplicity
[909.00 → 910.88] that community has really responded to.
[912.22 → 919.30] What is up, Practically AI listeners?
[919.50 → 920.68] We're working with Infinite Red
[920.68 → 922.82] to promote their free AI mini course.
[923.06 → 924.50] It's called AI Demystified.
[924.84 → 925.72] Learn more and enrol
[925.72 → 928.06] at learn ai.infinite.red.
[928.20 → 929.88] This free five-day mini course
[929.88 → 931.32] is a great introduction
[931.32 → 932.90] to the most important concepts,
[933.02 → 934.72] types, and business applications
[934.72 → 936.34] for AI and machine learning.
[936.66 → 937.70] Each day of the course
[937.70 → 939.06] includes a lesson,
[939.06 → 940.10] a quiz,
[940.34 → 940.92] and an assignment
[940.92 → 942.02] to submit your learning.
[942.50 → 943.96] And after you've completed the course,
[944.08 → 945.60] you'll also get a certificate
[945.60 → 946.38] of completion
[946.38 → 947.70] for your LinkedIn profile
[947.70 → 948.70] or for your portfolio.
[949.46 → 950.60] If you've been feeling lost
[950.60 → 951.30] in the world of AI
[951.30 → 952.66] and hearing lots of buzzwords,
[952.92 → 954.26] then by the end of this mini course,
[954.30 → 955.78] you'll be able to speak intelligently
[955.78 → 957.70] about AI and machine learning
[957.70 → 958.60] and their practical
[958.60 → 959.58] business applications.
[960.22 → 961.02] Again, this course
[961.02 → 962.16] is completely free.
[962.54 → 963.50] Learn more and enrol
[963.50 → 965.60] at learn ai.infinite.red.
[965.88 → 968.68] Again, learn ai.infinite.red.
[981.28 → 982.84] So, Adrian,
[982.96 → 984.16] you mentioned that
[984.16 → 985.08] kind of getting more
[985.08 → 987.04] into Streamlet itself.
[987.56 → 989.04] You mentioned that Streamlet
[989.04 → 991.12] is an app framework
[991.12 → 992.44] for machine learning
[992.44 → 993.64] and data science teams.
[993.98 → 994.26] I was wondering
[994.26 → 996.46] if you could unpack that a bit
[996.46 → 997.86] for people that maybe
[997.86 → 999.70] are not familiar
[999.70 → 1001.60] with front-end engineering
[1001.60 → 1003.22] and creating apps.
[1003.44 → 1004.54] When we're talking about
[1004.54 → 1005.84] an app framework here,
[1006.18 → 1006.76] for example,
[1006.86 → 1008.08] are we talking about
[1008.08 → 1009.26] just something
[1009.26 → 1010.76] that's going to be like a UI
[1010.76 → 1012.28] that's running in your browser?
[1012.58 → 1013.56] Is this having anything
[1013.56 → 1014.48] to do with mobile?
[1015.02 → 1015.74] Is this like,
[1015.86 → 1017.36] what is the app
[1017.36 → 1018.48] that we're talking about?
[1018.48 → 1019.72] And what does it mean
[1019.72 → 1021.48] that it's an app framework?
[1021.62 → 1022.12] I think you mentioned
[1022.12 → 1023.42] some things about components
[1023.42 → 1024.72] and stuff like that.
[1025.36 → 1025.48] Yeah.
[1025.90 → 1027.42] So, what it means
[1027.42 → 1029.80] is that you can write
[1029.80 → 1031.14] a Python script
[1031.14 → 1033.22] with any kind of code
[1033.22 → 1033.76] that you want.
[1033.88 → 1035.14] NumPy, SciPy,
[1035.30 → 1036.78] PyTorch, TensorFlow.
[1037.46 → 1039.64] And then you can add
[1039.64 → 1041.80] these magical Streamlet commands.
[1042.46 → 1043.86] Like, St. Write
[1043.86 → 1044.88] lets you write anything
[1044.88 → 1045.62] to the screen.
[1046.30 → 1047.66] St. Slider lets you
[1047.66 → 1049.04] put a slider on the screen.
[1049.62 → 1051.86] And you sprinkle these commands
[1051.86 → 1053.28] in your Python code.
[1053.90 → 1055.28] And what you have
[1055.28 → 1056.72] is a Python file
[1056.72 → 1058.42] that instead of saying
[1058.42 → 1059.44] Python that file,
[1059.60 → 1061.28] you say Streamlet run that file.
[1061.80 → 1063.50] And that command
[1063.50 → 1064.76] sets up a server,
[1065.50 → 1066.38] opens up a browser,
[1066.80 → 1068.52] and connects the two.
[1068.94 → 1071.12] That app is now running
[1071.12 → 1072.40] locally on your laptop
[1072.40 → 1073.60] or wherever you're running it.
[1073.64 → 1075.22] It could be on EC2 instance.
[1076.02 → 1077.72] And it's actually an app
[1077.72 → 1078.36] that you can run.
[1078.50 → 1079.50] You can look at it on mobile
[1079.50 → 1080.56] if you go to that URL
[1080.56 → 1081.90] and it looks nice on mobile too.
[1082.00 → 1083.18] So, it's both web
[1083.18 → 1084.14] and mobile in that sense.
[1084.60 → 1085.04] And it's something
[1085.04 → 1085.60] that you can share
[1085.60 → 1087.16] with others in your company
[1087.16 → 1088.12] and give them
[1088.12 → 1088.94] an interactive view
[1088.94 → 1089.84] into whatever it was
[1089.84 → 1090.56] you were working on.
[1090.76 → 1091.82] So, it could be as simple
[1091.82 → 1093.44] as here is a model.
[1093.68 → 1094.64] You know, play with the inputs
[1094.64 → 1095.52] and look at the outputs.
[1095.92 → 1097.06] I just created this app
[1097.06 → 1098.10] in five minutes
[1098.10 → 1098.80] just to show you.
[1099.28 → 1100.08] Or it could be something
[1100.08 → 1100.68] really sophisticated
[1100.68 → 1101.82] like let's build an app
[1101.82 → 1104.58] to organize all of our data
[1104.58 → 1105.66] and all of our models
[1105.66 → 1106.96] and allow us to run,
[1107.10 → 1107.38] you know,
[1107.72 → 1108.80] the latter on the former
[1108.80 → 1110.06] and arbitrary subsets
[1110.06 → 1111.06] and search engines
[1111.06 → 1111.70] and all this stuff.
[1112.02 → 1112.76] And so, you can go
[1112.76 → 1113.64] really crazy with it.
[1113.96 → 1114.98] So, that's what an app is.
[1115.20 → 1115.82] And fundamentally,
[1116.02 → 1116.86] it's basically just
[1116.86 → 1117.90] a Python program
[1117.90 → 1119.74] running on a server somewhere.
[1120.70 → 1122.44] So, kind of wondering
[1122.44 → 1123.20] in terms of,
[1123.24 → 1123.76] I'm trying to think
[1123.76 → 1125.00] about workflow and stuff.
[1125.08 → 1125.32] Mm-hmm.
[1125.92 → 1126.96] Is Streamlet
[1126.96 → 1128.20] mostly for prototyping
[1128.20 → 1129.72] or how far can you take it?
[1129.78 → 1130.14] And I guess,
[1130.24 → 1131.04] as part of that,
[1131.50 → 1132.38] couple of things,
[1132.50 → 1133.82] how would you integrate it
[1133.82 → 1135.34] into a small team environment
[1135.34 → 1137.24] and then conversely,
[1137.46 → 1137.74] you know,
[1137.76 → 1138.20] on the other side,
[1138.22 → 1138.82] you also mentioned
[1138.82 → 1139.54] you had been working
[1139.54 → 1140.48] with a larger client.
[1140.86 → 1141.48] How does it work
[1141.48 → 1141.92] in production
[1141.92 → 1143.42] for a larger team
[1143.42 → 1144.64] in an enterprise environment?
[1145.22 → 1146.58] And would it replace
[1146.58 → 1148.60] maybe in that kind of context
[1148.60 → 1149.74] some front-end engineering
[1149.74 → 1150.56] that you might otherwise
[1150.56 → 1151.28] have in that enterprise?
[1152.22 → 1153.22] Yeah, that's exactly right.
[1153.38 → 1154.56] So, really in a small
[1154.56 → 1155.80] or a large organization,
[1156.40 → 1157.26] the first step
[1157.26 → 1158.14] is just pip install
[1158.14 → 1158.58] Streamlet.
[1158.80 → 1160.18] It's an open-source project
[1160.18 → 1161.98] with a very permissive license.
[1162.32 → 1163.04] So, really,
[1163.34 → 1164.72] I don't think any organization
[1164.72 → 1165.68] would object to that.
[1166.06 → 1166.98] And you can play with it
[1166.98 → 1167.76] locally on your laptop
[1167.76 → 1169.34] and just see how it feels.
[1169.74 → 1170.52] And I encourage people
[1170.52 → 1170.90] to do that.
[1170.94 → 1171.94] It's actually really fun
[1171.94 → 1173.66] and extremely simple
[1173.66 → 1174.28] to learn.
[1174.60 → 1175.04] And then,
[1175.14 → 1176.24] once you get to something,
[1176.42 → 1176.54] you know,
[1176.54 → 1177.34] the next step might be
[1177.34 → 1178.22] look over my shoulder,
[1178.44 → 1179.22] show someone else
[1179.22 → 1180.04] in the organization,
[1180.54 → 1181.56] look at this thing I created.
[1181.98 → 1182.54] The next step
[1182.54 → 1183.78] is deploying it.
[1184.08 → 1184.82] Right now,
[1185.18 → 1186.50] there's a bunch of
[1186.50 → 1188.16] articles in Medium.
[1188.16 → 1189.48] You can just Google for them,
[1189.52 → 1190.66] which explain how to deploy
[1190.66 → 1191.80] Streamlet on EC2,
[1192.06 → 1192.68] on Heroku.
[1193.14 → 1194.58] It's a little bit of a process,
[1194.82 → 1195.30] to be honest,
[1195.68 → 1196.56] but you can set up
[1196.56 → 1197.46] a little server somewhere
[1197.46 → 1198.42] and then tell other people
[1198.42 → 1199.26] to point to it.
[1199.50 → 1200.24] And lo and behold,
[1200.38 → 1201.14] you now have an app
[1201.14 → 1201.82] that can be used
[1201.82 → 1202.50] in the organization.
[1202.50 → 1204.56] So that's the existing workflow.
[1205.14 → 1206.28] What we are working on
[1206.28 → 1207.32] with both large
[1207.32 → 1208.20] and small clients
[1208.20 → 1209.28] is something called
[1209.28 → 1210.06] Streamlet for Teams.
[1210.54 → 1211.42] And what that does
[1211.42 → 1212.86] is basically made the deployment
[1212.86 → 1214.04] completely painless.
[1214.32 → 1214.66] That's sort of
[1214.66 → 1215.58] the enterprise version.
[1216.10 → 1216.92] And it also adds
[1216.92 → 1217.54] a bunch of
[1217.54 → 1218.42] fascinating
[1218.42 → 1219.48] enterprise features.
[1219.84 → 1221.14] So load balancing,
[1221.48 → 1222.40] greater scalability,
[1223.26 → 1223.82] authentication,
[1224.38 → 1224.78] logging,
[1225.20 → 1225.98] those kinds of things.
[1226.50 → 1227.06] So,
[1227.34 → 1228.32] I wanted to follow up
[1228.32 → 1229.32] real quick on deployment
[1229.32 → 1230.16] just while you're there.
[1230.58 → 1231.92] What does the mobile picture
[1231.92 → 1232.44] look like?
[1232.58 → 1233.40] Or is there one
[1233.40 → 1234.02] at this point?
[1234.14 → 1234.82] Or is that something
[1234.82 → 1235.60] you're still working on?
[1235.94 → 1236.12] Yeah.
[1236.26 → 1237.10] So the mobile picture
[1237.10 → 1240.20] is that you deploy an app
[1240.20 → 1241.48] in one way or another.
[1241.66 → 1243.22] And so you would have to have
[1243.22 → 1244.78] either a VPN
[1244.78 → 1246.18] or a public IP address.
[1246.50 → 1247.52] And then if you point
[1247.52 → 1249.06] someone to that app,
[1249.40 → 1250.26] they will see it
[1250.26 → 1251.26] either rendered
[1251.26 → 1252.50] correctly on a browser
[1252.50 → 1253.38] or rendered correctly
[1253.38 → 1254.34] on a mobile device.
[1254.96 → 1255.60] And so an example
[1255.60 → 1256.58] of such an app
[1256.58 → 1258.02] that one of our users created
[1258.02 → 1259.98] is called Awesome Streamlet.
[1260.50 → 1261.58] And it's basically
[1261.58 → 1263.10] a collection of cool scripts
[1263.10 → 1264.02] and tricks that people
[1264.02 → 1265.10] have figured out in Streamlet.
[1265.26 → 1266.10] It's another sort of
[1266.10 → 1267.26] separate open source project.
[1267.66 → 1268.58] You can do pull requests
[1268.58 → 1269.38] against it and stuff.
[1269.66 → 1270.42] And it's an app
[1270.42 → 1271.48] that just runs on the internet
[1271.48 → 1272.58] and anyone can go to it.
[1272.80 → 1274.16] And so if you want to see
[1274.16 → 1275.14] the mobile experience
[1275.14 → 1275.70] of Streamlet,
[1275.86 → 1277.26] just Google Awesome Streamlet
[1277.26 → 1278.26] and play with it
[1278.26 → 1279.26] on a mobile device
[1279.26 → 1280.30] or on a sort of
[1280.30 → 1281.16] standard web browser.
[1281.74 → 1282.66] So that's the mobile story
[1282.66 → 1282.96] right now.
[1283.02 → 1283.72] We don't have any way
[1283.72 → 1284.36] of like packaging
[1284.36 → 1285.12] a Streamlet app
[1285.12 → 1286.76] into an iPhone app
[1286.76 → 1287.82] or something like that yet.
[1288.16 → 1289.20] That's a really cool idea though.
[1290.08 → 1290.84] Maybe we should do that.
[1290.84 → 1292.04] Yeah, cool.
[1292.20 → 1292.46] Thanks.
[1293.10 → 1294.54] So I'm kind of wondering,
[1294.76 → 1295.30] we've had people
[1295.30 → 1296.14] on the podcast
[1296.14 → 1296.96] in the past
[1296.96 → 1297.66] and I know there's
[1297.66 → 1298.24] probably people
[1298.24 → 1298.78] that are listening
[1298.78 → 1299.58] that are familiar
[1299.58 → 1301.28] with the R world
[1301.28 → 1302.34] and Shiny.
[1302.42 → 1303.04] Yep, totally.
[1303.44 → 1305.16] And I always felt like,
[1305.28 → 1305.68] oh, there was
[1305.68 → 1307.42] this Shiny thing
[1307.42 → 1308.32] with R
[1308.32 → 1310.28] that seemed cool
[1310.28 → 1311.22] and similar
[1311.22 → 1312.32] in some ways
[1312.32 → 1313.06] at least maybe.
[1313.44 → 1314.12] And there wasn't
[1314.12 → 1314.70] a parallel
[1314.70 → 1316.04] that at least
[1316.04 → 1316.56] I knew of
[1316.56 → 1317.28] for Python.
[1317.28 → 1318.74] if people aren't aware,
[1319.12 → 1319.96] Shiny kind of
[1319.96 → 1321.38] has this ability
[1321.38 → 1322.82] to help you build apps
[1322.82 → 1323.86] around your R scripts
[1323.86 → 1324.68] and that sort of thing.
[1325.10 → 1325.56] So I was wondering
[1325.56 → 1326.72] if there are
[1326.72 → 1328.26] actually some parallels there
[1328.26 → 1329.52] or if the end goals
[1329.52 → 1330.44] of Streamlet
[1330.44 → 1332.06] are slightly different
[1332.06 → 1333.68] than Shiny
[1333.68 → 1334.94] and if so,
[1335.02 → 1336.32] how you see all that.
[1336.88 → 1337.36] Yeah, so
[1337.36 → 1338.44] actually Shiny
[1338.44 → 1339.88] was a big inspiration
[1339.88 → 1340.72] for what we're doing
[1340.72 → 1341.38] and indeed
[1341.38 → 1342.30] when we were sort of
[1342.30 → 1343.66] building the first iterations
[1343.66 → 1344.22] of Streamlet,
[1344.22 → 1345.00] one thing that we heard
[1345.00 → 1345.96] over and over again
[1345.96 → 1346.98] was why is there
[1346.98 → 1348.04] no Shiny for Python?
[1348.66 → 1349.20] And so
[1349.20 → 1350.26] that was really
[1350.26 → 1351.20] kind of like
[1351.20 → 1352.00] a guiding light
[1352.00 → 1352.86] as we were developing
[1352.86 → 1353.30] Streamlet.
[1353.74 → 1354.64] I would say that
[1354.64 → 1356.38] there is a fairly
[1356.38 → 1357.38] significant
[1357.38 → 1358.62] technical difference
[1358.62 → 1359.28] in the implementation
[1359.28 → 1360.80] in that Shiny
[1360.80 → 1362.12] is sort of based
[1362.12 → 1363.18] on wiring
[1363.18 → 1364.06] these callbacks
[1364.06 → 1365.08] and Streamlet
[1365.08 → 1365.86] is actually based
[1365.86 → 1366.54] on a more sort of
[1366.54 → 1367.72] declarative data flow model.
[1368.58 → 1369.26] So I think that
[1369.26 → 1370.76] the user experience
[1370.76 → 1371.88] of building apps
[1371.88 → 1372.46] in each
[1372.46 → 1374.46] is quite different
[1374.46 → 1375.42] but certainly
[1375.42 → 1376.34] the sort of
[1376.34 → 1378.04] space that they fill
[1378.04 → 1378.98] in the ecosystem
[1378.98 → 1379.76] I think there are
[1379.76 → 1380.40] huge parallels
[1380.40 → 1381.96] and we would be
[1381.96 → 1382.82] really honoured
[1382.82 → 1384.00] to be considered
[1384.00 → 1385.02] the Shiny of Python.
[1385.20 → 1386.10] So, you know,
[1386.18 → 1386.82] one of the things
[1386.82 → 1387.58] we mentioned earlier
[1387.58 → 1388.84] was seeing Streamlet
[1388.84 → 1389.68] in our Twitter feed
[1389.68 → 1390.26] so much
[1390.26 → 1391.20] in recent weeks
[1391.20 → 1392.14] and I guess
[1392.14 → 1393.32] it really seems like
[1393.32 → 1393.72] Streamlet
[1393.72 → 1394.66] kind of burst onto
[1394.66 → 1395.12] the scene
[1395.12 → 1396.10] with tons of
[1396.10 → 1397.06] existing support,
[1397.42 → 1398.24] a lot of attention
[1398.24 → 1399.68] and you had mentioned
[1399.68 → 1400.74] that there are
[1400.74 → 1401.28] organizations
[1401.28 → 1403.18] like Stitch Fix,
[1403.42 → 1403.74] Uber,
[1404.00 → 1404.34] Twitter
[1404.34 → 1405.60] that are using
[1405.60 → 1406.18] Streamlet.
[1406.46 → 1407.40] How did that happen
[1407.40 → 1408.50] at least I guess
[1408.50 → 1409.08] from our perspective
[1409.08 → 1410.02] so early on
[1410.02 → 1411.14] as people became
[1411.14 → 1411.68] aware of it
[1411.68 → 1412.48] you already had
[1412.48 → 1412.92] you know
[1412.92 → 1413.74] major uptake
[1413.74 → 1414.74] on the platform?
[1415.06 → 1415.16] Yeah,
[1415.54 → 1416.64] so basically
[1416.64 → 1417.76] what happened was
[1417.76 → 1418.64] a year ago
[1418.64 → 1419.80] Streamlet was
[1419.80 → 1420.76] more or less
[1420.76 → 1421.22] a solo
[1421.22 → 1422.12] programming project
[1422.12 → 1422.64] of mine
[1422.64 → 1424.04] and my mom
[1424.04 → 1424.52] was like
[1424.52 → 1425.18] you should
[1425.18 → 1425.88] try to
[1425.88 → 1426.34] you know
[1426.34 → 1426.96] make a business
[1426.96 → 1427.36] around this
[1427.36 → 1427.62] if you're going
[1427.62 → 1427.94] to spend
[1427.94 → 1428.48] so much time
[1428.48 → 1428.74] on this.
[1428.82 → 1429.16] I actually was
[1429.16 → 1429.96] unemployed at the time
[1429.96 → 1431.28] and she was like
[1431.28 → 1431.86] anyway
[1431.86 → 1432.26] I was like
[1432.26 → 1432.84] it's impossible
[1432.84 → 1433.60] you can't do it
[1433.60 → 1434.02] and
[1434.02 → 1434.78] That's a good mom.
[1434.96 → 1435.32] I know
[1435.32 → 1435.82] I know
[1435.82 → 1437.30] she encourages
[1437.30 → 1437.78] her kids
[1437.78 → 1438.22] to follow
[1438.22 → 1438.68] you know
[1438.68 → 1439.14] their dreams
[1439.14 → 1439.36] or
[1439.36 → 1440.86] I guess
[1440.86 → 1441.20] she could have
[1441.20 → 1441.44] said
[1441.44 → 1441.66] you know
[1441.66 → 1441.92] you should
[1441.92 → 1442.42] get a job
[1442.42 → 1443.24] so anyway
[1443.24 → 1445.20] You made your job
[1445.20 → 1445.44] there.
[1445.60 → 1445.78] Yeah.
[1445.88 → 1446.30] There you go.
[1446.42 → 1446.94] Yeah, yeah, yeah.
[1447.30 → 1447.96] I started to realize
[1447.96 → 1448.70] that there might be
[1448.70 → 1449.32] a business model
[1449.32 → 1449.92] around this
[1449.92 → 1450.76] that made sense
[1450.76 → 1451.70] but even in those
[1451.70 → 1452.22] early days
[1452.22 → 1452.98] before there was
[1452.98 → 1453.62] a business model
[1453.62 → 1454.36] I was showing it
[1454.36 → 1454.90] to my friends
[1454.90 → 1456.02] and people
[1456.02 → 1456.50] were excited
[1456.50 → 1456.94] about it
[1456.94 → 1458.14] and I was a professor
[1458.14 → 1458.94] at Carnegie Mellon
[1458.94 → 1459.80] and at Google X
[1459.80 → 1460.12] and stuff
[1460.12 → 1460.56] so I
[1460.56 → 1460.86] you know
[1460.86 → 1461.36] I'm pretty
[1461.36 → 1462.54] like I have a social network
[1462.54 → 1463.76] that sort of stretches
[1463.76 → 1466.02] into the ML teams
[1466.02 → 1467.08] at all the big
[1467.08 → 1468.18] Silicon Valley companies
[1468.18 → 1469.50] and so you know
[1469.50 → 1470.22] just by virtue
[1470.22 → 1471.12] of showing it to people
[1471.12 → 1471.88] and in some cases
[1471.88 → 1472.58] them showing it
[1472.58 → 1473.18] to their friends
[1473.18 → 1473.78] we built a little
[1473.78 → 1474.52] community of people
[1474.52 → 1475.32] who were using it
[1475.32 → 1476.32] and at these
[1476.32 → 1476.62] you know
[1476.62 → 1477.42] sort of
[1477.42 → 1478.56] very well-known companies
[1478.56 → 1480.18] and so you know
[1480.18 → 1480.96] they were a little leery
[1480.96 → 1481.34] they were like
[1481.34 → 1482.06] what's this thing
[1482.06 → 1482.98] is it open source
[1482.98 → 1483.40] and what
[1483.40 → 1484.88] are we allowed to use
[1484.88 → 1485.48] this isn't our company
[1485.48 → 1486.42] but they were also
[1486.42 → 1487.14] excited about it
[1487.14 → 1487.60] and so that's
[1487.60 → 1488.14] that's kind of
[1488.14 → 1489.02] that was really
[1489.02 → 1489.42] the thread
[1489.42 → 1490.16] that carried us
[1490.16 → 1491.56] into you know
[1491.56 → 1492.78] through the initial
[1492.78 → 1493.92] seed raise
[1493.92 → 1495.04] and I think
[1495.04 → 1495.60] the investors
[1495.60 → 1496.38] sort of sensed
[1496.38 → 1497.02] our excitement
[1497.02 → 1498.12] and our users' excitement
[1498.12 → 1499.36] and then over the past year
[1499.36 → 1500.76] we've just been
[1500.76 → 1501.70] more or less
[1501.70 → 1502.56] listening to them
[1502.56 → 1503.50] and building features
[1503.50 → 1504.72] and we waited
[1504.72 → 1505.28] a little bit
[1505.28 → 1505.88] until we thought
[1505.88 → 1506.52] it was cool
[1506.52 → 1507.56] and then we released it
[1507.56 → 1509.16] as you were kind of
[1509.16 → 1510.30] taking what was
[1510.30 → 1510.96] then your just
[1510.96 → 1511.76] kind of personal
[1511.76 → 1512.64] project around
[1512.64 → 1513.86] and showing it to people
[1513.86 → 1515.16] and talking about it
[1515.16 → 1515.88] and talking about
[1515.88 → 1516.74] the need there
[1516.74 → 1517.72] and I guess
[1517.72 → 1518.68] sense kind of
[1518.68 → 1519.96] the features
[1519.96 → 1520.84] that the community
[1520.84 → 1521.70] has been asking for
[1521.70 → 1522.20] and other things
[1522.20 → 1523.64] has anything surprised you
[1523.64 → 1524.44] in terms of
[1524.44 → 1525.46] what people
[1525.46 → 1526.62] really want
[1526.62 → 1527.50] a lot
[1527.50 → 1527.92] versus
[1527.92 → 1529.16] things maybe
[1529.16 → 1529.84] that you thought
[1529.84 → 1530.78] would be important
[1530.78 → 1532.14] but weren't as important
[1532.14 → 1533.26] has anything surprised you
[1533.26 → 1533.92] in that way?
[1534.18 → 1534.50] Totally
[1534.50 → 1535.76] the big one
[1535.76 → 1536.88] actually is really
[1536.88 → 1538.30] this shiny for Python thing
[1538.30 → 1539.34] the original version
[1539.34 → 1539.78] of Streamlet
[1539.78 → 1540.70] was way more
[1540.70 → 1541.28] focused
[1541.28 → 1543.36] on just visualizing code
[1543.36 → 1544.36] actually
[1544.36 → 1545.44] and so
[1545.44 → 1545.98] to the extent
[1545.98 → 1546.74] that there was interaction
[1546.74 → 1547.24] it was
[1547.24 → 1548.30] we had this really cool
[1548.30 → 1549.46] hot reloading feature
[1549.46 → 1550.16] and so you could
[1550.16 → 1551.08] to the extent
[1551.08 → 1551.84] that there was interaction
[1551.84 → 1552.44] it was because
[1552.44 → 1553.60] you were editing the code
[1553.60 → 1554.44] and you could see things
[1554.44 → 1555.40] interactively changing
[1555.40 → 1556.06] on this screen
[1556.06 → 1556.66] which was actually
[1556.66 → 1557.26] super cool
[1557.26 → 1558.26] and very much
[1558.26 → 1558.82] at the core
[1558.82 → 1559.40] of I think
[1559.40 → 1560.60] the fun of Streamlet
[1560.60 → 1562.62] but people basically said
[1562.62 → 1563.72] we want apps
[1563.72 → 1565.88] and I resisted it
[1565.88 → 1566.24] actually
[1566.24 → 1567.16] I said this is a different
[1567.16 → 1567.98] product definition
[1567.98 → 1569.06] we don't know
[1569.06 → 1569.94] how to do this right
[1569.94 → 1571.14] and finally
[1571.14 → 1573.28] the community
[1573.28 → 1574.28] overpowered us
[1574.28 → 1574.68] basically
[1574.68 → 1576.12] and we sat down
[1576.12 → 1577.76] and really thought
[1577.76 → 1578.56] deeply about how
[1578.56 → 1579.22] this would work
[1579.22 → 1579.94] and in fact
[1579.94 → 1582.20] looked at every
[1582.20 → 1583.20] other app framework
[1583.20 → 1584.38] we would get our hands on
[1584.38 → 1585.44] and created this
[1585.44 → 1587.26] giant 70-slide deck
[1587.26 → 1588.58] of how they all worked
[1588.58 → 1589.74] shiny and
[1589.74 → 1590.72] Plot Dash
[1590.72 → 1591.36] and all these other
[1591.36 → 1591.94] kinds of things
[1591.94 → 1592.68] then we built
[1592.68 → 1593.22] what we thought
[1593.22 → 1594.06] it should look like
[1594.06 → 1596.06] and it was
[1596.06 → 1597.04] kind of leap
[1597.04 → 1597.84] into the unknown
[1597.84 → 1598.90] because I really
[1598.90 → 1599.62] wasn't sure
[1599.62 → 1601.04] it was going to
[1601.04 → 1603.32] be the kind of
[1603.32 → 1604.88] magical experience
[1604.88 → 1606.56] that I thought
[1606.56 → 1607.68] Streamlet needed
[1607.68 → 1608.26] to be
[1608.26 → 1611.04] and we just
[1611.04 → 1611.62] did it
[1611.62 → 1613.52] and we showed
[1613.52 → 1614.06] it to people
[1614.06 → 1615.40] and they were
[1615.40 → 1615.82] thrilled
[1615.82 → 1617.22] and actually
[1617.22 → 1617.44] you know
[1617.44 → 1618.20] we actually
[1618.20 → 1619.22] we're huge users
[1619.22 → 1619.70] of Streamlet
[1619.70 → 1620.50] so we build
[1620.50 → 1621.34] all of our dashboards
[1621.34 → 1622.30] and all this
[1622.30 → 1623.02] internal stuff
[1623.02 → 1623.64] in Streamlet
[1623.64 → 1624.52] and I remember
[1624.52 → 1625.12] one of the engineers
[1625.12 → 1625.54] being like
[1625.54 → 1627.18] Streamlet is really fun
[1627.18 → 1629.34] and I was like
[1629.34 → 1630.04] I know
[1630.04 → 1631.28] isn't that weird
[1631.28 → 1632.40] it's really fun
[1632.40 → 1632.96] like it's
[1632.96 → 1634.04] almost like
[1634.04 → 1634.60] we discovered
[1634.60 → 1635.28] this thing
[1635.28 → 1636.24] rather than
[1636.24 → 1636.60] you know
[1636.60 → 1637.14] built it
[1637.14 → 1637.98] and then we were like
[1637.98 → 1639.10] this thing is awesome
[1639.10 → 1640.20] so that
[1640.20 → 1640.62] you know
[1640.62 → 1641.56] that increased
[1641.56 → 1642.44] our sort of
[1642.44 → 1643.36] excitement
[1643.36 → 1643.98] basically
[1643.98 → 1644.70] and then
[1644.70 → 1644.96] you know
[1644.96 → 1645.38] it was being
[1645.38 → 1645.98] well received
[1645.98 → 1647.14] by the user groups
[1647.14 → 1647.78] so we really
[1647.78 → 1648.68] did have a nice
[1648.68 → 1650.44] user community
[1650.44 → 1651.42] by the time
[1651.42 → 1651.90] we launched
[1651.90 → 1652.72] and we also felt
[1652.72 → 1653.44] like we had
[1653.44 → 1653.94] you know
[1653.94 → 1654.36] confidence
[1654.36 → 1655.50] that there's a lot
[1655.50 → 1656.36] of things
[1656.36 → 1656.88] that we want
[1656.88 → 1657.38] to improve
[1657.38 → 1657.72] a lot
[1657.72 → 1658.10] but we had
[1658.10 → 1658.44] confidence
[1658.44 → 1659.26] that people
[1659.26 → 1659.70] could really
[1659.70 → 1660.12] use it
[1660.12 → 1661.56] I love that story
[1661.56 → 1663.04] being able to
[1663.04 → 1663.40] you know
[1663.40 → 1663.92] you start off
[1663.92 → 1664.40] by scratching
[1664.40 → 1665.10] your own itch
[1665.10 → 1665.88] and then
[1665.88 → 1666.54] you are building
[1666.54 → 1666.96] something
[1666.96 → 1668.00] that you
[1668.00 → 1668.64] and the people
[1668.64 → 1669.34] you're interacting
[1669.34 → 1670.42] with find fun
[1670.42 → 1670.98] and useful
[1670.98 → 1671.66] and exciting
[1671.66 → 1672.32] and getting
[1672.32 → 1672.92] on top of that
[1672.92 → 1673.64] and then
[1673.64 → 1674.52] on top of that
[1674.52 → 1674.90] you know
[1674.90 → 1675.76] Daniel and I
[1675.76 → 1676.54] both come from
[1676.54 → 1677.48] software development
[1677.48 → 1677.88] and we
[1677.88 → 1678.10] you know
[1678.10 → 1678.80] big
[1678.80 → 1679.26] open source
[1679.26 → 1679.66] advocates
[1679.66 → 1681.10] we love the fact
[1681.10 → 1681.90] that Streamlet
[1681.90 → 1682.58] is open source
[1682.58 → 1683.42] and wanted to
[1683.42 → 1684.22] kind of understand
[1684.22 → 1684.78] what was the
[1684.78 → 1685.90] economic model
[1685.90 → 1687.18] behind Streamlet
[1687.18 → 1687.82] and you know
[1687.82 → 1688.88] who is supporting
[1688.88 → 1689.50] it in that
[1689.50 → 1690.00] open source
[1690.00 → 1690.42] context
[1690.42 → 1691.50] and who's
[1691.50 → 1691.98] kind of
[1691.98 → 1692.96] developing on it
[1692.96 → 1693.98] you know
[1693.98 → 1694.56] and contributing
[1694.56 → 1695.14] to it at this
[1695.14 → 1695.38] point
[1695.38 → 1695.66] you know
[1695.66 → 1696.24] what does that
[1696.24 → 1696.84] open source
[1696.84 → 1698.02] side of the
[1698.02 → 1698.66] business look like
[1698.66 → 1698.98] for you
[1698.98 → 1699.42] yeah
[1699.42 → 1700.52] there's a sort
[1700.52 → 1701.30] of a guiding
[1701.30 → 1701.90] principle
[1701.90 → 1702.62] that we have
[1702.62 → 1703.54] borne in mind
[1703.54 → 1704.70] which is that
[1704.70 → 1705.88] so let me first
[1705.88 → 1706.28] say that
[1706.28 → 1707.24] Streamlet
[1707.24 → 1707.88] the way it works
[1707.88 → 1708.34] is that
[1708.34 → 1709.42] the library
[1709.42 → 1710.26] that you download
[1710.26 → 1711.00] is completely
[1711.00 → 1711.68] free and open
[1711.68 → 1711.98] source
[1711.98 → 1712.54] can be used
[1712.54 → 1713.24] for any reason
[1713.24 → 1713.78] whatsoever
[1713.78 → 1714.50] forked
[1714.50 → 1715.00] modified
[1715.00 → 1715.40] etc
[1715.40 → 1717.52] we are also
[1717.52 → 1718.00] building an
[1718.00 → 1718.74] enterprise product
[1718.74 → 1719.28] called Streamlet
[1719.28 → 1719.76] for teams
[1719.76 → 1721.34] and that's
[1721.34 → 1721.80] something that
[1721.80 → 1722.12] we are going
[1722.12 → 1722.48] to charge
[1722.48 → 1723.12] customers for
[1723.12 → 1724.00] so basically
[1724.00 → 1724.56] there's this
[1724.56 → 1725.18] dual model
[1725.18 → 1725.50] and it's
[1725.50 → 1725.88] actually a
[1725.88 → 1726.08] very
[1726.08 → 1727.08] it's becoming
[1727.08 → 1727.64] sort of the
[1727.64 → 1728.34] dominant open
[1728.34 → 1729.28] source business
[1729.28 → 1729.62] model
[1729.62 → 1731.14] and the guiding
[1731.14 → 1732.10] principle basically
[1732.10 → 1732.96] is that anything
[1732.96 → 1733.78] that's tech
[1733.78 → 1735.08] all the
[1735.08 → 1736.06] crazy web socket
[1736.06 → 1736.56] stuff
[1736.56 → 1737.44] the caching
[1737.44 → 1738.10] the hashing
[1738.10 → 1738.62] the queues
[1738.62 → 1739.18] all the stuff
[1739.18 → 1740.00] underneath Streamlet
[1740.00 → 1741.10] that's all free
[1741.10 → 1741.68] and open source
[1741.68 → 1742.62] and we have
[1742.62 → 1743.42] lots of plans
[1743.42 → 1743.96] to improve
[1743.96 → 1744.32] Streamlet
[1744.32 → 1744.98] in really
[1744.98 → 1745.74] fundamental ways
[1745.74 → 1746.02] we're just
[1746.02 → 1746.64] super excited
[1746.64 → 1746.98] about that
[1746.98 → 1747.52] so there's a lot
[1747.52 → 1747.96] more tech
[1747.96 → 1748.42] coming down
[1748.42 → 1748.84] the line
[1748.84 → 1749.72] and it's just
[1749.72 → 1750.10] going to make
[1750.10 → 1750.52] it is cooler
[1750.52 → 1751.24] and more magical
[1751.24 → 1752.30] than on the
[1752.30 → 1752.84] other hand
[1752.84 → 1753.50] there's all the
[1753.50 → 1754.18] features that
[1754.18 → 1754.96] are useful
[1754.96 → 1755.56] in a business
[1755.56 → 1756.00] context
[1756.00 → 1756.86] so that's
[1756.86 → 1757.52] increased
[1757.52 → 1758.26] scalability
[1758.26 → 1759.50] load balancing
[1759.50 → 1760.80] security
[1760.80 → 1761.80] logging
[1761.80 → 1762.52] authentication
[1762.52 → 1763.06] etc
[1763.06 → 1764.34] management
[1764.34 → 1765.26] of apps
[1765.26 → 1766.34] and so
[1766.34 → 1767.48] those features
[1767.48 → 1767.94] are going to be
[1767.94 → 1768.52] part of Streamlet
[1768.52 → 1768.92] for teams
[1768.92 → 1769.60] and so
[1769.60 → 1770.08] right now
[1770.08 → 1770.54] we're in the
[1770.54 → 1771.28] process of
[1771.28 → 1772.14] talking with
[1772.14 → 1772.52] customers
[1772.52 → 1773.24] and understanding
[1773.24 → 1774.20] how we can
[1774.20 → 1774.64] sort of
[1774.64 → 1775.68] nail the value
[1775.68 → 1776.26] prop there
[1776.26 → 1777.02] for different
[1777.02 → 1777.60] use cases
[1777.60 → 1778.42] so
[1778.42 → 1779.58] you know
[1779.58 → 1780.76] it looks
[1780.76 → 1781.36] perfect
[1781.36 → 1782.18] corporations
[1782.18 → 1782.94] are excited
[1782.94 → 1783.46] about Streamlet
[1783.46 → 1783.96] for teams
[1783.96 → 1784.98] we have an
[1784.98 → 1785.78] incredibly long
[1785.78 → 1786.40] list of people
[1786.40 → 1786.90] who are
[1786.90 → 1787.74] basically telling
[1787.74 → 1788.30] us they'd like
[1788.30 → 1788.64] to pay
[1788.64 → 1789.18] when it comes
[1789.18 → 1789.42] out
[1789.42 → 1790.48] and that means
[1790.48 → 1790.86] that we can
[1790.86 → 1791.34] support the
[1791.34 → 1791.80] open source
[1791.80 → 1792.16] project
[1792.16 → 1792.80] and that's
[1792.80 → 1793.38] just like
[1793.38 → 1794.08] super thrilling
[1794.08 → 1794.66] because
[1794.66 → 1795.92] it's just so
[1795.92 → 1796.48] fun to build
[1796.48 → 1796.94] open source
[1796.94 → 1797.34] software
[1797.34 → 1811.38] this episode
[1811.38 → 1811.94] is brought
[1811.94 → 1812.50] to you by
[1812.50 → 1813.18] Brave
[1813.18 → 1814.10] big news
[1814.10 → 1814.44] from the
[1814.44 → 1815.02] Brave team
[1815.02 → 1816.28] version 1.0
[1816.28 → 1817.00] is official
[1817.00 → 1817.86] that means
[1817.86 → 1818.40] our favourite
[1818.40 → 1819.10] open source
[1819.10 → 1820.12] privacy focused
[1820.12 → 1821.06] blazing fast
[1821.06 → 1821.98] browser is ready
[1821.98 → 1822.62] for prime-time
[1822.62 → 1823.70] their brand new
[1823.70 → 1824.56] iOS app
[1824.56 → 1825.46] landed just in
[1825.46 → 1825.90] time for the
[1825.90 → 1826.28] announcement
[1826.28 → 1826.86] and the
[1826.86 → 1827.32] Brave team
[1827.32 → 1827.98] is celebrating
[1827.98 → 1828.62] by granting
[1828.62 → 1829.54] 8 million
[1829.54 → 1830.40] basic attention
[1830.40 → 1831.12] tokens to the
[1831.12 → 1831.48] community
[1831.48 → 1832.28] that means
[1832.28 → 1832.56] when you
[1832.56 → 1833.12] download the
[1833.12 → 1833.76] iOS app
[1833.76 → 1834.12] you get
[1834.12 → 1834.82] 20 bat
[1834.82 → 1835.42] absolutely
[1835.42 → 1835.94] free
[1835.94 → 1837.02] put it to
[1837.02 → 1837.52] good use
[1837.52 → 1837.94] by heading
[1837.94 → 1839.26] to changelog.com
[1839.26 → 1839.72] hitting the
[1839.72 → 1840.38] triangle icon
[1840.38 → 1840.98] in the upper
[1840.98 → 1841.40] right hand
[1841.40 → 1841.72] corner
[1841.72 → 1842.66] and flipping
[1842.66 → 1843.20] us a tip
[1857.32 → 1858.28] so as we
[1858.28 → 1858.32] can't
[1858.32 → 1858.34] so as we've
[1858.34 → 1858.66] been having
[1858.66 → 1859.42] this conversation
[1859.42 → 1859.88] I've been
[1859.88 → 1860.26] kind of
[1860.26 → 1861.12] thinking about
[1861.12 → 1861.94] like my
[1861.94 → 1862.38] own use
[1862.38 → 1862.80] cases
[1862.80 → 1863.50] my own
[1863.50 → 1864.06] workflows
[1864.06 → 1864.66] and where
[1864.66 → 1865.24] this comes
[1865.24 → 1865.54] in
[1865.54 → 1866.30] and it
[1866.30 → 1867.10] seems like
[1867.10 → 1868.16] you know
[1868.16 → 1869.04] streamlet
[1869.04 → 1869.72] itself
[1869.72 → 1871.00] is kind of
[1871.00 → 1871.84] in one of
[1871.84 → 1872.46] those situations
[1872.46 → 1873.20] where it's like
[1873.20 → 1874.02] it's a tool
[1874.02 → 1875.14] and if you ask
[1875.14 → 1875.66] like oh what
[1875.66 → 1876.18] could you do
[1876.18 → 1876.86] with streamlet
[1876.86 → 1877.38] you could do
[1877.38 → 1878.60] like sort of
[1878.60 → 1879.12] an infinite
[1879.12 → 1880.58] combination of
[1880.58 → 1881.42] things with it
[1881.42 → 1882.00] which makes it
[1882.00 → 1882.86] kind of hard to
[1882.86 → 1883.98] like nail down
[1883.98 → 1884.66] some starting
[1884.66 → 1885.26] points and so
[1885.26 → 1885.64] I'm thinking
[1885.64 → 1886.30] like oh well
[1886.30 → 1887.28] I could you
[1887.28 → 1887.56] know if I
[1887.56 → 1887.94] wanted to
[1887.94 → 1888.68] create a UI
[1888.68 → 1890.10] where I
[1890.10 → 1890.84] didn't have to
[1890.84 → 1891.80] jump into my
[1891.80 → 1892.62] code and adjust
[1892.62 → 1893.04] a bunch of
[1893.04 → 1893.82] hyperparameters
[1893.82 → 1894.92] to you know
[1894.92 → 1895.90] retrain my
[1895.90 → 1896.64] model I could
[1896.64 → 1897.50] create a nice
[1897.50 → 1898.40] little UI to do
[1898.40 → 1899.24] that or if I
[1899.24 → 1900.22] just wanted to
[1900.22 → 1901.56] like push
[1901.56 → 1902.86] images through
[1902.86 → 1904.46] a model and
[1904.46 → 1905.20] do some inference
[1905.20 → 1906.20] and draw bounding
[1906.20 → 1907.20] boxes around them
[1907.20 → 1908.56] to review those
[1908.56 → 1909.28] things I could do
[1909.28 → 1910.84] that as you
[1910.84 → 1911.30] think about
[1911.30 → 1912.00] people's AI
[1912.00 → 1913.22] workflows going
[1913.22 → 1914.16] from like data
[1914.16 → 1914.94] prep to
[1914.94 → 1915.94] training to
[1915.94 → 1917.26] inference to
[1917.26 → 1918.52] like maybe
[1918.52 → 1919.78] feedback and
[1919.78 → 1921.06] data labelling
[1921.06 → 1921.84] what do you
[1921.84 → 1922.60] think maybe is
[1922.60 → 1923.24] like a good
[1923.24 → 1923.96] place for people
[1923.96 → 1924.92] to start thinking
[1924.92 → 1925.68] about where
[1925.68 → 1926.74] streamlet could
[1926.74 → 1927.60] provide the
[1927.60 → 1928.76] most value
[1928.76 → 1929.90] quickest is it
[1929.90 → 1930.46] whenever you want
[1930.46 → 1931.06] to like show
[1931.06 → 1931.98] someone else
[1931.98 → 1932.84] something or
[1932.84 → 1933.88] you know could
[1933.88 → 1934.34] it is other
[1934.34 → 1935.40] places yeah
[1935.40 → 1936.26] curious about
[1936.26 → 1937.68] that yeah so
[1937.68 → 1938.30] it really runs
[1938.30 → 1939.00] the gamut as
[1939.00 → 1939.72] you pointed out
[1939.72 → 1940.38] it's sort of as
[1940.38 → 1941.24] broad as machine
[1941.24 → 1941.94] learning and data
[1941.94 → 1942.74] science itself
[1942.74 → 1943.90] we've seen a
[1943.90 → 1944.84] lot of cool
[1944.84 → 1945.90] different use
[1945.90 → 1946.68] cases so
[1946.68 → 1947.38] people are
[1947.38 → 1948.24] creating interactive
[1948.24 → 1949.06] resumes in
[1949.06 → 1949.86] streamlet so
[1949.86 → 1950.82] you can actually
[1950.82 → 1951.80] see the different
[1951.80 → 1952.54] models they've
[1952.54 → 1953.30] built people are
[1953.30 → 1953.74] also building
[1953.74 → 1954.38] like explainer
[1954.38 → 1955.12] demos so we've
[1955.12 → 1956.00] seen you know
[1956.00 → 1957.34] now increasing
[1957.34 → 1958.14] number of GitHub
[1958.14 → 1959.12] repos that say
[1959.12 → 1959.90] if you want to
[1959.90 → 1960.58] test out this
[1960.58 → 1961.64] model or my
[1961.64 → 1962.74] code just
[1962.74 → 1963.52] streamlet run
[1963.52 → 1964.38] this demo
[1964.38 → 1966.04] and that's super
[1966.04 → 1966.96] fun and really
[1966.96 → 1967.94] powerful actually for
[1967.94 → 1968.46] the people who are
[1968.46 → 1969.46] testing out different
[1969.46 → 1970.02] open source
[1970.02 → 1971.40] projects we're
[1971.40 → 1972.30] seeing people build
[1972.30 → 1974.04] dashboards for
[1974.04 → 1975.12] often for like
[1975.12 → 1975.98] external consumption
[1975.98 → 1976.90] so a dashboard for
[1976.90 → 1977.78] the marketing team
[1977.78 → 1979.18] recommendation engine
[1979.18 → 1979.96] that kind of thing
[1979.96 → 1981.14] similarly we're
[1981.14 → 1981.98] seeing like tools
[1981.98 → 1982.40] for like an
[1982.40 → 1983.32] external operations
[1983.32 → 1984.10] team of some
[1984.10 → 1984.68] kind so for
[1984.68 → 1985.88] example the ops
[1985.88 → 1986.98] team can see data
[1986.98 → 1987.72] from the self-driving
[1987.72 → 1988.70] car as it's being
[1988.70 → 1989.18] downloaded
[1989.18 → 1990.54] annotation tools
[1990.54 → 1991.48] people are doing
[1991.48 → 1992.22] that in streamlet
[1992.22 → 1993.10] we have some
[1993.10 → 1994.04] friends at Google
[1994.04 → 1995.26] who are doing a
[1995.26 → 1996.16] real-time monitoring
[1996.16 → 1997.08] of some pretty
[1997.08 → 1998.38] advanced and secret
[1998.38 → 1999.76] hardware they just
[1999.76 → 2000.48] put streamlet on a
[2000.48 → 2001.34] Raspberry Pi and
[2001.34 → 2001.80] then they built
[2001.80 → 2002.24] these like a
[2002.24 → 2003.08] real-time dashboards
[2003.08 → 2004.64] and yeah just
[2004.64 → 2006.08] managing data one
[2006.08 → 2006.44] way of thinking
[2006.44 → 2007.08] about it is like
[2007.08 → 2007.86] every time you
[2007.86 → 2008.50] might write a
[2008.50 → 2009.40] command line tool
[2009.40 → 2010.74] a little just one
[2010.74 → 2011.56] for yourself you
[2011.56 → 2012.38] know that I want
[2012.38 → 2013.42] to list all the
[2013.42 → 2014.38] data sets in this
[2014.38 → 2015.72] directory and compute
[2015.72 → 2016.60] some statistics about
[2016.60 → 2017.78] them you could
[2017.78 → 2018.66] imagine just instead
[2018.66 → 2019.22] of writing a command
[2019.22 → 2019.96] line tool write a
[2019.96 → 2020.64] little streamlet app
[2020.64 → 2022.54] and suddenly it's
[2022.54 → 2023.60] really much easier
[2023.60 → 2024.46] to see and prettier
[2024.46 → 2026.00] it's more easily
[2026.00 → 2027.06] shareable with others
[2027.06 → 2028.52] and understandable you
[2028.52 → 2029.04] know all the
[2029.04 → 2030.06] parameters can be sort
[2030.06 → 2031.06] of encoded as like
[2031.06 → 2031.82] interactive widgets
[2031.82 → 2032.90] and it's not much
[2032.90 → 2033.52] more complicated
[2033.52 → 2034.80] that's a great
[2034.80 → 2035.64] example right there
[2035.64 → 2036.56] because I do that
[2036.56 → 2037.60] I'll create little
[2037.60 → 2038.70] command line interfaces
[2038.70 → 2039.82] on a regular basis
[2039.82 → 2040.96] just to scratch my
[2040.96 → 2041.60] own itch on stuff
[2041.60 → 2042.64] so I'm glad you
[2042.64 → 2043.24] brought that out as
[2043.24 → 2044.34] an example as I
[2044.34 → 2046.10] look around on the
[2046.10 → 2047.14] streamlet website I'm
[2047.14 → 2047.50] going through the
[2047.50 → 2048.26] documentation while
[2048.26 → 2049.48] we're talking one of
[2049.48 → 2050.46] the things that I'm
[2050.46 → 2051.62] seeing is different
[2051.62 → 2052.58] terminology that you
[2052.58 → 2053.64] have associated with
[2053.64 → 2054.54] streamlet and
[2054.54 → 2055.60] recognizing that we
[2055.60 → 2057.20] are audio only that
[2057.20 → 2057.84] we're doing a podcast
[2057.84 → 2059.24] here and don't have
[2059.24 → 2060.04] the visuals that I'm
[2060.04 → 2061.20] diagrams wanted to
[2061.20 → 2062.08] talk about whether
[2062.08 → 2062.94] or not you could
[2062.94 → 2064.12] just kind of briefly
[2064.12 → 2065.62] say what a couple of
[2065.62 → 2066.58] things mean to you
[2066.58 → 2067.94] I'll throw out four or
[2067.94 → 2069.00] five terms and just
[2069.00 → 2070.08] kind of tell us what
[2070.08 → 2070.92] they are in the
[2070.92 → 2071.88] streamlet context if
[2071.88 → 2073.18] you would yeah I'll
[2073.18 → 2073.90] just I'll name them
[2073.90 → 2074.78] all, and I'll prompt
[2074.78 → 2075.58] you later if you
[2075.58 → 2077.06] forget data flow
[2077.06 → 2079.64] caching widgets
[2079.64 → 2081.96] sidebar and app model
[2081.96 → 2083.02] is a few could you
[2083.02 → 2083.88] kind of talk to what
[2083.88 → 2084.60] each of those is to
[2084.60 → 2086.46] you so when we say
[2086.46 → 2088.56] that streamlet has a
[2088.56 → 2090.04] data flow model what
[2090.04 → 2091.88] that means is that it
[2091.88 → 2093.04] really is you could
[2093.04 → 2093.70] you could actually just
[2093.70 → 2094.96] say it's a scripting
[2094.96 → 2096.72] model which is to say
[2096.72 → 2098.44] the script executes from
[2098.44 → 2099.80] top to bottom and you
[2099.80 → 2101.38] can define variables and
[2101.38 → 2102.52] those variables you know
[2102.52 → 2103.48] transform things and
[2103.48 → 2104.98] it's really the machine
[2104.98 → 2107.58] learning workflow and so
[2107.58 → 2109.16] what we add to that
[2109.16 → 2111.44] workflow is a couple of
[2111.44 → 2114.52] cool superpowers so one
[2114.52 → 2116.76] of them is widgets which
[2116.76 → 2118.26] is you can basically
[2118.26 → 2119.50] anywhere in the flow of
[2119.50 → 2121.82] your program insert if
[2121.82 → 2122.86] you want to say x equals
[2122.86 → 2124.12] five instead of saying x
[2124.12 → 2125.00] equals five you can say
[2125.00 → 2127.12] x equals St slider and
[2127.12 → 2128.74] now a slider sort of
[2128.74 → 2129.74] magically appears on the
[2129.74 → 2131.16] screen and x will be
[2131.16 → 2132.30] whatever you set the
[2132.30 → 2134.08] slider to another thing
[2134.08 → 2135.12] that magical thing that
[2135.12 → 2136.58] we add is the sidebar
[2136.58 → 2137.98] super simple but it
[2137.98 → 2139.22] basically gives you an
[2139.22 → 2141.18] area on the left usually
[2141.18 → 2142.16] to put some widgets and
[2142.16 → 2143.34] stuff, and it's a very
[2143.34 → 2144.82] very simple layout model
[2144.82 → 2145.80] that actually leads to
[2145.80 → 2146.54] like gorgeous
[2146.54 → 2147.94] looking apps with almost
[2147.94 → 2149.36] no work at all another
[2149.36 → 2150.58] superpower that we give
[2150.58 → 2152.72] you are caching and what
[2152.72 → 2154.08] that means is that you
[2154.08 → 2155.12] can decorate your
[2155.12 → 2157.22] function with this magic
[2157.22 → 2159.38] called St cache and we
[2159.38 → 2161.64] will memorize the
[2161.64 → 2162.82] function i.e. we'll
[2162.82 → 2164.72] remember how it behaves
[2164.72 → 2166.64] and that's useful because
[2166.64 → 2168.12] it lets you speed up your
[2168.12 → 2169.24] apps and so when people
[2169.24 → 2171.28] slide the sliders or type
[2171.28 → 2172.18] in text in the text
[2172.18 → 2173.92] inputs it'll just be
[2173.92 → 2175.84] faster and those things
[2175.84 → 2176.92] together so the data
[2176.92 → 2178.18] flow from top to bottom
[2178.18 → 2179.92] the layout both in the
[2179.92 → 2180.94] main area and in the
[2180.94 → 2182.84] sidebar the ability to
[2182.84 → 2184.86] do widgets and have
[2184.86 → 2186.40] inputs and then caching
[2186.40 → 2187.78] to speed things up are
[2187.78 → 2189.32] together what we call the
[2189.32 → 2190.74] streamlet app model and
[2190.74 → 2193.24] so it's actually quite
[2193.24 → 2194.64] unique because it's
[2194.64 → 2196.16] really focused on
[2196.16 → 2196.74] let's make this
[2196.74 → 2197.70] understandable for
[2197.70 → 2198.64] machine learning engineers
[2198.64 → 2199.66] and data scientists and
[2199.66 → 2200.50] let's let's give them the
[2200.50 → 2201.90] ability to create apps
[2201.90 → 2202.96] that otherwise would be
[2202.96 → 2204.52] very complicated to
[2204.52 → 2206.16] create quite frankly
[2206.16 → 2208.02] so i yeah I mean it
[2208.02 → 2209.72] sounds like as I'm
[2209.72 → 2210.48] kind of thinking through
[2210.48 → 2211.62] some of my scripts it's
[2211.62 → 2212.66] like whenever I'm going
[2212.66 → 2215.00] through and I like have
[2215.00 → 2217.02] the desire to put in like
[2217.02 → 2218.38] a command line argument or
[2218.38 → 2220.18] something like that i
[2220.18 → 2221.20] want to modify all the
[2221.20 → 2223.30] time maybe a way to think
[2223.30 → 2225.20] about it would just be to
[2225.20 → 2226.74] think about instead of
[2226.74 → 2228.28] having that command line in
[2228.28 → 2230.50] my mind I could have an UI
[2230.50 → 2231.44] in my mind where I'm
[2231.44 → 2232.60] thinking oh well what if
[2232.60 → 2233.76] this was an UI and I could
[2233.76 → 2234.76] just get that parameter
[2234.76 → 2236.38] in that way or I could
[2236.38 → 2237.54] change this thing in that
[2237.54 → 2239.38] way or create you know
[2239.38 → 2241.54] the display this graph or
[2241.54 → 2243.16] display this image in this
[2243.16 → 2245.32] way so kind of is that a
[2245.32 → 2246.24] good way to think about it
[2246.24 → 2247.98] as I'm going through
[2247.98 → 2249.02] my script and I know I'm
[2249.02 → 2250.04] going to be modifying this
[2250.04 → 2251.32] all the time or I know I'm
[2251.32 → 2253.28] gonna when I give this to
[2253.28 → 2254.98] someone else then I'm
[2254.98 → 2255.78] going to have to tell them
[2255.78 → 2257.04] all of these things to
[2257.04 → 2258.74] modify is that a good way
[2258.74 → 2259.38] to think about that's a
[2259.38 → 2260.18] great way to think about
[2260.18 → 2262.02] it and that's um that's
[2262.02 → 2263.20] really you know I use it
[2263.20 → 2265.30] that way all the time so
[2265.30 → 2266.26] like a script that I want
[2266.26 → 2268.22] to write right now is when
[2268.22 → 2269.92] we do new feature releases
[2269.92 → 2271.30] we just released a new
[2271.30 → 2272.64] stream like two days ago and
[2272.64 → 2273.66] we do it about every week
[2273.66 → 2275.08] or two we want to make
[2275.08 → 2276.68] sure that everyone who
[2276.68 → 2278.58] requested a feature on the
[2278.58 → 2279.98] forums is basically
[2279.98 → 2281.38] notified by us that
[2281.38 → 2281.98] their feature was
[2281.98 → 2283.68] implemented and so what
[2283.68 → 2285.12] that amounts to is a
[2285.12 → 2286.98] little tiny script that
[2286.98 → 2288.40] runs some git commands
[2288.40 → 2289.22] and then does some
[2289.22 → 2290.90] GitHub stuff in order to
[2290.90 → 2291.98] assemble a list of pull
[2291.98 → 2293.76] requests and then parse
[2293.76 → 2295.12] those out, and so we can
[2295.12 → 2296.12] we can sort of keep track
[2296.12 → 2297.20] of what happened easily
[2297.20 → 2299.06] and automatically and so
[2299.06 → 2300.52] you just imagine that
[2300.52 → 2301.38] would be a very simple
[2301.38 → 2302.62] well it'd be an intricate
[2302.62 → 2304.12] little python script to
[2304.12 → 2304.82] get that done on the
[2304.82 → 2306.42] command line and instead
[2306.42 → 2308.14] we can just use streamlet
[2308.14 → 2309.06] to make it a little
[2309.06 → 2310.74] interactive app and so the
[2310.74 → 2311.72] first step is just yeah
[2311.72 → 2312.82] create that app and
[2312.82 → 2314.02] suddenly it's just
[2314.02 → 2315.22] prettier it's easier to
[2315.22 → 2316.20] understand it's easier to
[2316.20 → 2317.78] use it's just as
[2317.78 → 2319.00] shareable and then the
[2319.00 → 2320.50] next step is you know
[2320.50 → 2321.50] this is really cool this
[2321.50 → 2322.32] should be running all the
[2322.32 → 2323.86] time everyone should have
[2323.86 → 2325.00] access to this without you
[2325.00 → 2326.12] know checking out my code
[2326.12 → 2327.92] so let's deploy it and I
[2327.92 → 2329.00] think that just that
[2329.00 → 2331.22] attitude which is your know
[2331.22 → 2331.90] this is just a little
[2331.90 → 2332.90] script let me write it up
[2332.90 → 2334.22] is the starting point for
[2334.22 → 2335.56] creating lots and lots of
[2335.56 → 2336.90] extremely cool and useful
[2336.90 → 2339.48] streamlet apps so it sounds
[2339.48 → 2340.78] really great I'm pretty
[2340.78 → 2342.26] excited about jumping
[2342.26 → 2343.28] into it after we stop
[2343.28 → 2344.86] recording this yeah totally
[2344.86 → 2346.44] and I'm thinking through
[2346.44 → 2347.54] my own use cases in my
[2347.54 → 2348.34] head while we're talking
[2348.34 → 2350.76] if I get to a point where
[2350.76 → 2352.64] I don't have exactly you
[2352.64 → 2354.00] know in the tool the thing
[2354.00 → 2355.00] that I want, and I'm
[2355.00 → 2355.90] starting to think about
[2355.90 → 2357.62] extending what's possible
[2357.62 → 2358.54] how do you go about doing
[2358.54 → 2359.68] that how easy is it to
[2359.68 → 2361.36] extend streamlet and kind
[2361.36 → 2362.56] of create custom UIs and
[2362.56 → 2363.46] components that aren't
[2363.46 → 2365.02] necessarily the things
[2365.02 → 2365.70] that you're showing in the
[2365.70 → 2366.82] examples or the docs or
[2366.82 → 2367.68] stuff what is that
[2367.68 → 2370.00] extension chance look
[2370.00 → 2371.34] like totally the first
[2371.34 → 2372.86] thing I'd say is write
[2372.86 → 2375.52] your extension down in
[2375.52 → 2377.46] the forums we have a
[2377.46 → 2378.34] super active user
[2378.34 → 2380.12] community we really try
[2380.12 → 2382.28] to also have as many
[2382.28 → 2383.12] streamlet devs as
[2383.12 → 2384.80] possible involved and so
[2384.80 → 2385.70] you know questions get
[2385.70 → 2386.72] answered quickly and
[2386.72 → 2388.30] knowledgeably so ask your
[2388.30 → 2388.96] question in the forums
[2388.96 → 2390.80] one thing that I think a
[2390.80 → 2391.34] lot of people are
[2391.34 → 2392.28] surprised about is they
[2392.28 → 2393.42] say oh streamlet can't do
[2393.42 → 2394.68] this, and actually it can
[2394.68 → 2396.60] there's you know we wrap
[2396.60 → 2398.20] a lot of all the basic
[2398.20 → 2399.28] visualization libraries
[2399.28 → 2400.90] map plot lib Altair plot
[2400.90 → 2402.74] etc deck GL and we
[2402.74 → 2404.06] there are a lot of ways to
[2404.06 → 2405.40] combine the basic elements
[2405.40 → 2406.56] in streamlet to do really
[2406.56 → 2408.36] really cool things and so
[2408.36 → 2409.40] often people are surprised
[2409.40 → 2410.44] when we say oh no there is
[2410.44 → 2411.22] a way of doing that so
[2411.22 → 2413.18] that's step one step two
[2413.18 → 2415.12] is if it's impossible to do
[2415.12 → 2416.70] in streamlet you're welcome
[2416.70 → 2418.54] to check out and fork the
[2418.54 → 2419.44] repo, and we have
[2419.44 → 2420.34] instructions on how to do
[2420.34 → 2421.24] that, and you can go in
[2421.24 → 2422.06] there and look at how we
[2422.06 → 2423.16] did something and make a
[2423.16 → 2424.52] change and in fact we're
[2424.52 → 2425.92] also welcome and have
[2425.92 → 2427.24] started seeing a bunch of
[2427.24 → 2428.52] community improvements to
[2428.52 → 2429.60] streamlet and so we
[2429.60 → 2431.12] welcome those PRS number
[2431.12 → 2432.98] three is that's a pretty
[2432.98 → 2433.98] heavyweight thing to check
[2433.98 → 2435.36] out streamlet and modify
[2435.36 → 2437.18] it we're working on
[2437.18 → 2439.36] plugin architecture and by
[2439.36 → 2440.28] working on I should I
[2440.28 → 2441.12] should caveat by saying
[2441.12 → 2443.06] we have designs on paper
[2443.06 → 2444.04] we haven't started coding
[2444.04 → 2445.32] it up yet so I think this
[2445.32 → 2446.14] will sometimes be released
[2446.14 → 2448.52] 2020, but the designs are
[2448.52 → 2450.60] very, very cool and I think
[2450.60 → 2451.56] it's just going to breathe
[2451.56 → 2453.38] new life into streamlet in
[2453.38 → 2454.62] terms of possibilities and
[2454.62 → 2455.90] so we're really excited to
[2455.90 → 2457.10] do that and let people
[2457.10 → 2458.36] build essentially arbitrary
[2458.36 → 2460.32] front ends in streamlet and
[2460.32 → 2461.58] then power them through
[2461.58 → 2464.62] python awesome well just to
[2464.62 → 2466.42] kind of wrap up and give
[2466.42 → 2469.12] people a place to go get
[2469.12 → 2470.24] hands-on right away with
[2470.24 → 2471.16] streamlet because I know a
[2471.16 → 2472.68] lot of people will want to
[2472.68 → 2474.82] where's the best place for
[2474.82 → 2476.86] people to go first is that
[2476.86 → 2478.12] your website or maybe
[2478.12 → 2478.96] describe a little bit of
[2478.96 → 2481.22] the tutorials and how people
[2481.22 → 2482.52] can can get started you
[2482.52 → 2483.32] mentioned you can pip
[2483.32 → 2485.10] install it but what's the
[2485.10 → 2486.64] the best way to get up and up
[2486.64 → 2487.78] and running I guess totally
[2487.78 → 2489.42] yeah the simplest starting
[2489.42 → 2491.64] point is just our web page
[2491.64 → 2495.84] streamlet s-t-r-e-a-m-l-i-t
[2495.84 → 2498.18] dot i-o, or you can go to
[2498.18 → 2500.64] our GitHub page GitHub slash
[2500.64 → 2502.24] dream let slash dream let and
[2502.24 → 2503.60] then once you get there we're
[2503.60 → 2504.58] going to give you the
[2504.58 → 2505.52] instructions which are pretty
[2505.52 → 2506.78] simple so pip install
[2506.78 → 2510.16] streamlet, and then you get a
[2510.16 → 2511.58] this command called streamlet and
[2511.58 → 2512.86] you can test it up by typing
[2512.86 → 2515.58] streamlet hello, so pip install
[2515.58 → 2517.08] streamlet hello and
[2517.08 → 2518.34] then once you're in any one of
[2518.34 → 2520.30] those points you kind of have
[2520.30 → 2522.12] touchpoints to get to all the
[2522.12 → 2523.32] other parts of the community and
[2523.32 → 2525.16] really the main hubs of the
[2525.16 → 2527.92] community are the wiki the
[2527.92 → 2530.78] documentation the forums and
[2530.78 → 2532.64] GitHub and in all of those
[2532.64 → 2535.32] places you'll find people
[2535.32 → 2537.72] chatting discussing coming up with
[2537.72 → 2539.22] cool solutions sharing
[2539.22 → 2541.18] information so yeah it's pretty
[2541.18 → 2544.72] great awesome uh well i I know
[2544.72 → 2545.60] there'll be a lot of people
[2545.60 → 2547.26] checking that out I would love to
[2547.26 → 2549.38] see what people build with
[2549.38 → 2550.92] streamlet so if you want to share
[2550.92 → 2552.36] that with us, you can of course
[2552.36 → 2553.88] share that in streamlets community
[2553.88 → 2556.68] but also on the practical AI slack
[2556.68 → 2558.02] channel which you can find at
[2558.02 → 2560.36] changelog.com slash community or
[2560.36 → 2561.92] share it with us on our LinkedIn
[2561.92 → 2564.66] page or on Twitter, and we would love
[2564.66 → 2566.74] to see what you build with
[2566.74 → 2569.00] streamlet I'm really excited to
[2569.00 → 2570.56] see where the project goes and
[2570.56 → 2572.48] really appreciate you taking time
[2572.48 → 2574.14] to talk to us about it today Adrian
[2574.14 → 2576.32] yeah it was a delight and I'm
[2576.32 → 2577.80] really excited to see what your
[2577.80 → 2579.34] audience does too so yeah let us
[2579.34 → 2581.16] know post in the forums post on
[2581.16 → 2583.16] twitter uh we're trying to keep up
[2583.16 → 2584.96] on all that stuff so we're we'd
[2584.96 → 2585.74] love to see what you're doing
[2585.74 → 2587.54] excellent well thank you so much i
[2587.54 → 2589.24] hope we can meet in person at a
[2589.24 → 2590.70] conference or something, but we'll
[2590.70 → 2592.36] look forward to seeing all the great
[2592.36 → 2593.52] things online cool thanks for
[2593.52 → 2594.86] joining us yep thank you so much
[2594.86 → 2598.50] all right thank you for tuning into
[2598.50 → 2600.80] this episode of practical AI if you
[2600.80 → 2602.40] enjoyed this show do us a favour go on
[2602.40 → 2604.14] iTunes give us a rating go in your
[2604.14 → 2606.18] podcast app and favourite it if you are
[2606.18 → 2607.90] on Twitter or social network share a
[2607.90 → 2609.04] link with a friend whatever you got to
[2609.04 → 2610.42] do share the show with a friend if you
[2610.42 → 2612.72] enjoyed it and bandwidth for changelog is
[2612.72 → 2614.60] provided by fast learn more at
[2614.60 → 2616.60] fastly.com, and we catch our errors
[2616.60 → 2618.04] before our users do here at changelog
[2618.04 → 2619.96] because of Rollbar check them out at
[2619.96 → 2622.24] rollbar.com slash changelog, and we're
[2622.24 → 2624.68] hosted on Linde cloud servers head
[2624.68 → 2626.48] to linode.com slash changelog check
[2626.48 → 2628.28] them out support this show this
[2628.28 → 2630.56] episode is hosted by Daniel whiten ack
[2630.56 → 2632.76] and Chris Benson the music is by
[2632.76 → 2634.78] break master cylinder, and you can find
[2634.78 → 2636.46] more shows just like this at
[2636.46 → 2638.88] changelog.com when you go there pop in
[2638.88 → 2640.98] your email address get our weekly email
[2640.98 → 2642.58] keeping you up to date with the news
[2642.58 → 2644.60] and podcasts for developers in your
[2644.60 → 2646.82] inbox every single week thanks for
[2646.82 → 2648.16] tuning in we'll see you next week
[2648.16 → 2655.94] we'll find out
[2655.94 → 2656.38] what's next should be
[2656.38 → 2657.58] a response to those
[2657.58 → 2658.12] ину by
[2658.12 → 2659.28] ATT Facilitator
[2659.28 → 2660.06] is a great miss
[2660.06 → 2660.92] was a great miss
[2660.92 → 2662.08] of you
[2662.08 → 2662.54] the one day
[2662.54 → 2662.96] 15
[2662.96 → 2663.68] the twelve
[2663.68 → 2664.28] the
[2664.28 → 2664.68] the
[2664.68 → 2665.36] the
[2665.36 → 2666.34] the
[2666.34 → 2667.34] the
[2667.34 → 2668.48] the
[2668.48 → 2669.86] the
[2669.96 → 2670.78] the
[2670.78 → 2672.60] the
[2672.60 → 2674.42] the
[2674.42 → 2674.58] the
[2674.58 → 2674.70] the
[2674.70 → 2676.70] the
