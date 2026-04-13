[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.18 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.94 → 111.32] Welcome to another fully connected episode of Practical AI,
[111.62 → 116.42] where we keep you fully connected with everything that's happening in the AI community.
[116.64 → 123.34] We're going to take some time to discuss some things related to the recent topics in AI news,
[123.34 → 129.70] and we'll dig into a few learning resources that are related to those to help you level up your machine learning game.
[130.06 → 133.78] So I'm Daniel Whiten ack, data scientist with SIL International,
[133.78 → 142.44] and I'm joined by my co-host, Chris Benson, who is a chief AI strategist with Lockheed Martin RMS APA Innovations.
[142.74 → 143.40] How are you doing, Chris?
[143.58 → 144.02] Doing great.
[144.08 → 144.70] How's it going, Daniel?
[144.94 → 145.92] It's going really well.
[145.92 → 151.86] I'm sitting in a newly remodelled home office, so I'm pretty happy.
[151.98 → 157.52] We got some final painting done and set up my monitor and new desk and everything,
[157.76 → 158.62] so I'm feeling pretty good.
[159.08 → 159.68] What about you?
[159.94 → 161.06] I'm relieved to be home.
[161.42 → 165.98] I've been travelling the last couple of weeks and hit Washington, D.C., New York,
[165.98 → 173.46] and I was just in Silicon Valley as we recorded this for NVIDIA GPU Technology Conference,
[173.66 → 176.18] and so back, recorded a couple of things there.
[176.44 → 182.16] I know last week we had a guest from there, and there's going to be some more down the road,
[182.30 → 184.72] so I'm really looking forward to today.
[185.04 → 192.58] Yeah, me too, and I think it's kind of ideal that I just went through all of my personal setup
[192.58 → 197.98] here in my home office this week because you had suggested that we talk about a certain topic
[197.98 → 203.86] that I know is really on a lot of people's minds as they get into this field and as they kind of
[203.86 → 208.54] try to figure out what to focus on as they're learning things and how to build a team.
[208.90 → 211.08] So you want to intro what we're going to be talking about today?
[211.46 → 211.62] Sure.
[211.82 → 216.82] So today we're going to be talking about a fairly broad topic that we're labelling AI infrastructure,
[217.10 → 221.90] which encompasses a lot of stuff, and the reason that I had suggested it was
[221.90 → 227.60] I have so many conversations with people who are trying to kind of get their own AI operations
[227.60 → 233.04] set up, both at a personal level, just like you and me as data scientists working on stuff,
[233.14 → 237.10] but also at an organizational level trying to figure out how their company needs to get
[237.10 → 239.86] everything stood up that they need there to do what they're doing.
[239.98 → 242.56] So we're going to talk about kind of a lot of the ideas.
[243.08 → 246.90] It's a huge topic, so there's only so much we'll be able to cover, but hopefully we can bind
[246.90 → 249.02] of dive into some of that stuff today and have fun with it.
[249.44 → 250.02] Yeah, for sure.
[250.02 → 255.60] I know that there's a lot of when I do trainings and other things, I always get a lot of questions
[255.60 → 258.24] about, oh, how should I do my personal setup?
[258.38 → 263.60] What do I need to buy to actually be an AI practitioner on that side of things?
[263.60 → 265.24] So the personal infrastructure side.
[265.36 → 272.00] But then also there's like so many choices of things out there as far as how you set up
[272.00 → 273.34] your workflow and all of that.
[273.80 → 279.10] So just a disclaimer as we kind of go into this conversation, we'll probably be primarily
[279.10 → 282.58] focusing on a lot of the things that we have personally interacted with.
[282.68 → 288.00] But we would love to hear some of the infrastructure or the frameworks or the setup that our listeners
[288.00 → 291.92] have or maybe that we're missing or definitely if we misrepresent anything.
[292.52 → 293.78] So definitely do that.
[293.94 → 295.10] Join our Slack community.
[295.30 → 299.84] You can do that at changelog.com slash community or on our LinkedIn page.
[299.84 → 305.14] And let us know what we're missing or what your personal setup looks like.
[305.42 → 310.58] But we'll try to, you know, as we go to conferences and like I said, as we do trainings and other
[310.58 → 314.46] things like that, I think we've seen a lot of what people are doing out there.
[314.56 → 319.54] So hopefully we can convey some of that today and give kind of a landscape of infrastructure.
[319.54 → 320.14] Absolutely.
[321.04 → 326.26] I think and there's just a there are so many different ways to put together infrastructure.
[326.42 → 327.48] There's so much choice.
[327.62 → 330.60] This field has just absolutely exploded in the last couple of years.
[330.72 → 335.64] When we were first talking about machine learning back in the know, when we first got to
[335.64 → 339.70] know each other and stuff, there just weren't the plethora of options that we have at this
[339.70 → 339.92] point.
[339.96 → 341.90] So we'll try to sort through some of that today.
[342.16 → 342.36] Yeah.
[342.36 → 348.56] So let's kind of jump in maybe with a general question and think about like, as AI practitioners,
[348.56 → 357.06] how much time do we spend kind of doing development, you know, on our local setup or our local machine
[357.06 → 363.14] or laptop versus in a cloud or hosted environment or kind of specialized on prem hardware?
[363.26 → 364.88] So what's your experience with that, Chris?
[364.88 → 371.36] So I know different people who do different ways, but I really focus on using cloud or hosted
[371.36 → 372.88] environments most of the time.
[373.32 → 378.22] I have friends and colleagues that have bought their own home equipment, you know, in terms
[378.22 → 383.06] of the different types of GPUs that are available and, you know, they can plug in graphics cards
[383.06 → 383.74] and that kind of thing.
[384.02 → 387.70] But from where I'm coming from, I don't tend to be the guy who's always out buying the latest
[387.70 → 388.86] new thing constantly.
[389.20 → 395.04] And this field is moving so fast that I have kind of chosen to opt out of buying my own equipment
[395.04 → 399.28] since I would constantly be replacing it because the new shiny thing would be out there.
[399.28 → 404.14] So if it's a trivial toy little thing like, you know, for demos or for teaching people,
[404.14 → 408.14] then I might do something on my MacBook just using the CPU.
[408.14 → 411.72] But it has to be, you know, truly a tiny thing for that to be the case.
[412.06 → 415.36] Almost any other time, I'm either going to a hosted environment or a cloud environment.
[415.36 → 421.36] Yeah, I think that kind of how it splits up for me, or at least has, you know, in the past
[421.36 → 429.12] couple of years is I do a lot of kinds of the initial work to test my code and ensure that
[429.12 → 430.38] it actually runs.
[430.90 → 435.36] So, you know, deal with a lot of those issues, maybe deal with some like data formatting or
[435.36 → 441.16] data pre-processing or kind of looking at example data, making some example API calls,
[441.16 → 445.70] figuring out how to deal with that data in a Jupyter notebook, all of those sorts of like
[445.70 → 447.14] kind of initial things.
[447.26 → 449.28] A lot of those I still do locally.
[449.92 → 450.64] Actually, I do as well.
[450.70 → 453.16] I was only thinking in terms of training when I said that.
[453.22 → 454.14] So I should have been more clear.
[454.36 → 454.58] Yeah.
[454.72 → 459.44] So then, of course, like you said, you know, at a certain point, you know, you're limited
[459.44 → 462.10] locally, but also you need to scale things up.
[462.10 → 467.26] And, you know, we've said a lot of times here that AI doesn't really do you any good.
[467.26 → 471.36] You know if it just stays on your laptop, it has to get out there and be practical.
[471.66 → 473.60] So I like to make that jump.
[473.76 → 479.20] I think, you know, maybe a good way to put it is to make that jump to a production like
[479.20 → 483.08] environment, whatever that's going to be, whether that's going to be somewhere in the
[483.08 → 487.76] cloud or on on-premise hardware or whatever, make that jump as soon as you reasonably can
[487.76 → 490.26] without, you know, wasting much time.
[490.40 → 491.86] That's kind of my viewpoint on that.
[492.04 → 493.06] Yeah, I would agree with that.
[493.10 → 496.94] I mean, there's some, as you pointed out in my brain, as I answered that last question,
[496.94 → 501.14] I was kind of jumping straight into training on a GPU or TPU.
[501.54 → 505.48] And in that case, I move it off my Mac pretty quick.
[505.58 → 510.28] But for the vast majority of the data prep, which is the most of the work, getting everything,
[510.38 → 514.20] you know, ready for training and, you know, pulling data in and massaging it and doing
[514.20 → 516.74] all the things you have to do so that it is ready for that.
[517.12 → 522.20] Most of that I do on my Mac unless we're talking about, in some cases, the data sets are simply
[522.20 → 527.22] too big, and then I'll offload it to a server, not necessarily a GPU or a specialty, you know,
[527.22 → 531.52] something like a DGX, but to some other server just to crank away while I do other stuff.
[532.00 → 532.14] Yeah.
[532.26 → 536.94] And a lot of the stuff, you know, if you're going to be running a training for a model
[536.94 → 543.42] for, you know, five hours or 12 hours or whatever it ends up being, it just simply not
[543.42 → 544.76] practical to do that locally.
[544.76 → 551.32] But like you said, that's actually probably the proportionality wise, the smaller amount
[551.32 → 554.10] of things that an AI practitioner would do.
[554.24 → 559.12] The majority of things are, you know, figuring out what data to use and figuring out what
[559.12 → 563.64] format it's in and then getting it, you know, engineering some features or trying out some
[563.64 → 569.48] certain things, making sure your code runs before you, you know, spend up for GPU time
[569.48 → 570.94] in the cloud or something like that.
[571.46 → 571.58] Agree.
[571.58 → 575.96] It's funny that, you know, we like to think of ourselves as AI practitioners and yet the
[575.96 → 581.26] training piece of that, even though training itself may last quite a while as you're doing
[581.26 → 585.32] that in the scheme of a project, it's a very small amount of time that you spend.
[585.68 → 585.84] Yep.
[586.12 → 591.04] So let's think about with that in mind, I guess, you know, one of the questions that I get
[591.04 → 595.94] a lot when I'm going around doing trainings and other things is, hey, do I need to invest
[595.94 → 601.56] in some sort of GPU workstation for my home office or a really expensive laptop with
[601.56 → 605.84] a GPU or something that can be there in my office?
[606.44 → 609.62] Obviously, I think neither one of us have that situation.
[609.78 → 610.96] So maybe that's the answer.
[611.30 → 615.54] But I think if there's people out there that are wondering, that's not really necessary
[615.54 → 617.28] at this point.
[617.28 → 622.92] So I think you can use a little bit cheaper hardware to do your local development as long
[622.92 → 629.54] as you're able to connect to the APIs and the UIs and, you know, open up a terminal and
[629.54 → 631.82] connect to the instances that you're running elsewhere.
[632.18 → 633.88] Yeah, I have a rule of thumb on that.
[634.00 → 635.18] And the way I do it.
[635.26 → 639.52] So I have both initially, you know, we've talked a little bit about this in previous episodes,
[639.52 → 643.54] things that we do at a personal level that we're interested in personally, separate from
[643.54 → 643.82] work.
[643.82 → 645.00] And then I have the work things.
[645.18 → 649.64] And because I work for Lockheed and have previously worked for other large companies since I've
[649.64 → 653.98] been in the AI space, I have resources there where they are dedicated equipment.
[654.30 → 660.06] In general, people say, hey, should I be buying a DGX workstation, or should I buy some graphics
[660.06 → 660.38] cards?
[660.56 → 665.58] I really say there's a crossover point where it depends on how much you're training.
[665.76 → 671.84] If you have enough going in your operation to where you are really needing training cycles
[671.84 → 675.88] kind of around the clock, then, you know, and that's more than just personal projects,
[675.92 → 678.00] obviously, that's at work or a team of people.
[678.22 → 679.72] Yeah, that's going to be in a corporate setting.
[680.06 → 680.38] Yeah, right.
[680.70 → 684.82] Then it can make sense to buy your own equipment because, you know, there's a big investment
[684.82 → 688.70] that you're making, but then you're utilizing that equipment constantly.
[689.24 → 690.98] And so that it makes sense.
[691.06 → 696.12] But for most of us who are not doing that kind of around the clock operation, I think,
[696.20 → 700.18] you know, going with cloud providers is probably the way to go because you can just use
[700.18 → 703.28] what you need, pay for that bit and then move on without continuing to.
[703.86 → 708.00] So but if you were training around the clock, then there's a crossover point where cloud
[708.00 → 712.46] providers can become more expensive than actually making that investment yourself.
[712.58 → 713.02] Yeah.
[713.24 → 717.78] And I mean, if you're especially if you're looking for a job in AI or if you're getting
[717.78 → 723.50] into AI or even once you have a job in AI, most of the time, any of that specialized
[723.50 → 725.22] hardware would be purchased.
[725.32 → 728.64] It would be purchased by your company to enable things for your team.
[728.82 → 729.02] Correct.
[729.02 → 731.38] You're never going to have to invest personally.
[732.08 → 733.18] At least you don't have to.
[733.30 → 737.48] I mean, you could if you really want to work on some crazy personal projects, but you don't
[737.48 → 738.28] have to do that.
[739.00 → 745.52] And so just to kind of be transparent, you know, as a data scientist, my personal infrastructure
[745.52 → 751.46] basically looks like and by personal infrastructure, I mean, my local setup just looks like a MacBook,
[751.86 → 755.14] you know, without the goofy touch bar thing, because that's, that's weird.
[755.60 → 757.30] I have to have an escape key.
[757.30 → 757.68] I'm sorry.
[757.84 → 758.24] There you go.
[758.24 → 760.26] You know, an external monitor.
[760.88 → 761.82] I get a nice keyboard.
[762.32 → 766.86] That's essential for me that that mechanical keyboard makes typing a joy.
[767.30 → 771.04] But then I don't really have a ton of stuff even installed locally.
[771.24 → 774.70] So I have the native Python or brew installed Python.
[774.70 → 779.72] So I don't use like Anaconda or any of this kind of loaded sort of package managers.
[779.72 → 781.56] Those can be really nice for a lot of people.
[781.66 → 784.76] I just don't find it as nice for me personally.
[785.22 → 787.00] But there is some advantage to that.
[787.26 → 788.36] I use a really simple.
[788.52 → 793.06] I just use a VAM ID and I have Jupiter and Docker installed locally.
[793.06 → 800.46] I use things like Postman for testing API calls and Go occasionally, you know, and Slack and
[800.46 → 803.06] Zoom and all the web conference stuff because I work remotely.
[803.32 → 804.86] So that's kind of what I prefer.
[805.06 → 806.78] Again, all of those are personal preferences.
[807.00 → 812.76] I know a lot of people that find a lot of value in kind of these environment managers like
[812.76 → 815.20] Anaconda or maybe other ways of doing things.
[815.28 → 816.42] That's just not what I do.
[816.42 → 819.40] What does your personal setup look like, Chris?
[819.72 → 821.42] Sadly, it's much like yours.
[821.52 → 823.08] So I won't go through everything.
[823.34 → 824.38] But yeah, I'm on a MacBook.
[824.66 → 828.06] Like you, I also like Ubuntu separately if I'm on a server.
[828.54 → 832.34] Standard kind of MacBook setup with an external monitor, keyboard, trackpad.
[832.44 → 834.02] Nothing fancy for me.
[834.46 → 837.00] I also brew install Python as well.
[837.38 → 842.04] I've had trouble with Anaconda when I tried to change use cases around, and it somehow would
[842.04 → 843.36] start throwing errors.
[843.50 → 844.82] So I found that to be simplest.
[844.82 → 849.40] For deep learning, I'm always starting in a Jupyter notebook and hoping that it's successful
[849.40 → 854.20] enough to migrate later down the road out of that Jupyter notebook into code as a library.
[854.96 → 855.52] Docker a lot.
[855.62 → 862.20] I mean, Docker is, I'm so glad Docker came along before the AI explosion happened because
[862.20 → 867.30] utilizing it with containers has made the world of AI training and deployment so much
[867.30 → 867.62] easier.
[867.96 → 871.72] And then I know like you, anyone who's listened to us knows we both love Go.
[871.90 → 873.72] I use Go as my default Go-to language.
[873.72 → 877.38] I use Python for the data science things that tend to be Python specific.
[877.82 → 879.14] And I don't have a GPU.
[879.78 → 884.78] I actually, I have like a TX2 that I play around with, and I'm about to get a NATO from NVIDIA.
[884.90 → 887.60] But you know, those are mainly for my toy projects and stuff.
[887.74 → 893.88] For any training, I am going to typically, if either whatever my company has to offer and
[893.88 → 896.94] we have stuff within Lockheed Martin that I can use for work.
[896.94 → 901.36] If it's on my own, I'm going to like AWS SageMaker and Google Cola.
[901.56 → 903.20] And so that gives you a sense.
[903.26 → 907.02] And we can talk in both about some of the those in more detail as we go forward here.
[907.60 → 907.72] Yeah.
[907.90 → 912.62] So I think moral of the story, I mean, you don't need a fancy computer, even a MacBook.
[912.98 → 913.58] We have those.
[913.58 → 917.56] But if you just have a cheaper notebook, that's fine as well.
[917.56 → 921.20] Because, you know, a lot of the things that you'll probably be doing are hosted.
[921.36 → 924.12] There's no need for that specialized hardware.
[924.60 → 926.70] There's probably is a lower limit to that.
[927.10 → 934.48] One time my wife borrowed my MacBook for a week and I tried to go for a week on a Chromebook.
[934.58 → 935.86] And there was a lot of pain there.
[935.90 → 937.42] Although I think that's getting better too.
[937.42 → 941.40] I think, you know, people like Kelsey Hightower and others, you know, develop on a Chromebook.
[941.60 → 941.94] Yeah, I know.
[942.02 → 942.58] He loves it.
[942.64 → 944.34] I know from his Twitter feed.
[944.44 → 950.50] But I remember when you did that, because as an aside, we tried to record an episode at that point.
[950.62 → 952.88] I know you were having some technical struggles with that.
[953.18 → 954.32] And I've also struggled.
[954.46 → 957.78] But that I remember very distinctly you're trying to work through that.
[957.98 → 958.16] Yeah.
[958.28 → 960.82] And again, you know, these are personal preferences.
[960.82 → 964.64] So we'd love to hear what your guys' setup is and what value you find from things.
[964.64 → 974.42] But I'm kind of moving on from our personal local setup and talking about, okay, from our local setup, that's pretty, maybe pretty light.
[974.60 → 977.24] At least a lot of people's local setup is kind of light.
[977.54 → 981.04] You know, what are the things that we're connecting to that are hosted or in the cloud?
[981.40 → 987.70] What enables our AI workflows, the things that we use that don't run on our book?
[987.70 → 1001.46] And to kind of switch to that topic, I think probably there's something we need to talk about first, which is there's an infinite number of ways that we could enable AI workflows in the cloud or on-prem.
[1001.82 → 1007.68] And a lot of that's going to be driven by the organization that you're working for and what their concerns are.
[1008.10 → 1012.06] So the first of those may be being kind of governance issues.
[1012.06 → 1017.36] So I know probably with you working for Lockheed, Chris, there are a lot of things related to that.
[1017.44 → 1021.02] But I think anywhere now there's going to be a lot of governance related issues.
[1021.44 → 1021.52] Yeah.
[1021.64 → 1032.08] You know if it's just you, you know, as we're talking about ourselves individually, you just kind of plug in whatever tools you like, and you create your workflow out of that, which is available.
[1032.08 → 1033.44] And there are different ways of doing that.
[1033.48 → 1036.54] And it's pretty simple because it's really based on your personal preference.
[1036.54 → 1045.44] But as soon as you get to even a small team level and certainly as you get to multiple teams across an organization, it gets pretty complicated quick.
[1045.56 → 1064.30] And you have to start thinking about all the issues that go into making something that will work not only technically for you as a data scientist doing the work, but also accommodate the various laws, regulations, you know, things like GDPR in Europe that have to be accounted for.
[1064.30 → 1072.08] And how you do different types of workflows and testing and some of those topics that, you know, just off the cuff.
[1072.16 → 1075.54] And we can dive into a few of them or things like data discovery.
[1075.92 → 1080.92] How are you going to know what's available to you beyond, you know, just things that your own team might be producing?
[1081.36 → 1085.12] What are some of the trust and certification issues out there?
[1085.12 → 1095.64] Provenance and lineage, you know, and I know that when you were in your previous position at Pachyderm, I know prominence is one of the features that you had there and maybe talk a little bit toward that.
[1095.72 → 1097.98] But data management, who owns data?
[1098.10 → 1099.26] What's the sovereignty of the data?
[1099.70 → 1103.14] How do you access the data and the different tools in the workflow?
[1103.66 → 1108.24] And what kinds of data science processes do you build around that?
[1108.24 → 1110.14] So that's a lot to think about.
[1110.36 → 1111.82] You know what about you, Daniel?
[1112.04 → 1115.44] You know if you want to dive into a couple of the things that are of interest to you there.
[1115.98 → 1116.18] Yeah.
[1116.30 → 1131.66] I mean, I think the big one, maybe a big one to emphasize is just, you know, all the problems in this area in my mind and all the major blockers that I've hit as a practitioner are mostly having to do with the data side of things.
[1131.66 → 1135.86] Not whether I had the compute power to train a specific model or something.
[1136.38 → 1147.54] So, for example, there's always issues, you know, if you're using someone else's data, there's privacy issues depending on if it's personally identifiable, identifying data.
[1147.54 → 1159.36] Of course, if you're working in health care, there are issues about, you know, even where you're allowed to store certain data and whether that is on prem at a facility in the cloud.
[1159.52 → 1161.00] There are a lot of issues there.
[1161.00 → 1177.96] And so I think the main issues are that you're being some of those data sources that you might like to use might force you into using certain infrastructure, might force you into staying on premise in your own company's infrastructure, or it might allow you to be in the cloud.
[1177.96 → 1191.96] And even if you are in the cloud, you might still have to maintain certain audit trails and that sort of thing for the data that you're using, especially if you're using data that's been generated by EU citizens and all of that sort of thing with GDPR.
[1192.86 → 1192.96] Yeah.
[1193.14 → 1196.74] So I think all of this, that's really, in my mind, the major factor.
[1196.74 → 1198.10] Yeah, I would agree with that.
[1198.22 → 1207.12] And that was a great point you made in that just the laws and the way laws will affect your own organization's strategy in terms of where you're housing data.
[1207.12 → 1218.16] And I've actually seen over the last couple of years, you know, as people were prepping for GDR, and then it came into being, I've had conversations with people where they chose where to keep data from a nationality standpoint.
[1218.16 → 1228.18] And so they might literally relocate their operations from a in terms of the training and the data storage and stuff into a completely different country to accommodate those laws.
[1228.18 → 1234.64] And also to figure out with different countries having different laws, how are they going to approach that from a strategy standpoint?
[1235.20 → 1236.68] You know where should those operations be?
[1236.78 → 1242.10] So it can, it can increase your cost on having enough equipment to go to different places and to have to think through that.
[1242.10 → 1244.44] So there are multiple rabbit holes here.
[1244.44 → 1248.58] And I know we're just kind of skimming over the top of some of these issues on this episode.
[1248.58 → 1253.82] And we can certainly do episodes and actually have done some in the past where we kind of do some deep dives.
[1254.06 → 1258.80] I'll kind of leave it there and let us kind of proceed on down the infrastructure route.
[1259.10 → 1267.82] Yeah, I think the main takeaway is before you decide on a specific, oh, I'm going to run in GCP, or I'm going to run in AWS, or I'm going to run on-prem.
[1267.82 → 1282.16] You need to have a process in place that will help you decide what are the data concerns related to where I am allowed to store data, how much data I can share, even within your own organization.
[1282.16 → 1297.02] The Data Engineering Podcast is a weekly deep dive on modern data management with the engineers and entrepreneurs who are shaping the industry.
[1297.30 → 1305.60] Go behind the scenes on the tools, techniques, and difficulties of data engineering so you can learn and keep up with the knowledge to make you and your business successful.
[1305.60 → 1313.48] Can you give a bit of an outline about the motivation for choosing Jupyter Notebooks in particular as the core interface for your data teams?
[1313.86 → 1318.16] Yeah, and actually, when I first joined Netflix, it was sort of tossed at me.
[1318.34 → 1319.94] And I was definitely like, well, are we crazy?
[1320.16 → 1321.84] And the answer was like, we might be a little crazy.
[1322.34 → 1328.66] Go to dataengineeringpodcast.com to listen, subscribe, and share it with your friends and colleagues.
[1335.60 → 1351.46] So we've kind of been through so far talking about, you know, our personal setup, what an AI practitioner might need locally,
[1351.46 → 1362.66] and then what organizational concerns might go into choices around whether your AI workflow runs in the cloud or where you store your data and that sort of thing.
[1362.66 → 1372.26] But let's go ahead and, you know, jump into how AI practitioners are running their AI workflows in the cloud or on-prem.
[1372.36 → 1380.88] What are the sorts of frameworks and infrastructure and tools that they're using to actually enable those AI workflows?
[1381.22 → 1387.76] And so, again, this is from our personal experience and, you know, what we've seen other people doing and what we've done ourselves.
[1387.76 → 1394.26] But, you know, maybe we can start with what sorts of resources do we need in terms of compute and storage?
[1394.42 → 1399.82] So what sorts of resources do you need to run your AI workflows, Chris?
[1400.14 → 1406.54] Well, kind of going back to a little while ago, I'm very focused on Docker just because it makes it a lot easier.
[1406.76 → 1409.94] Having said that, I do keep TensorFlow installed locally.
[1409.94 → 1414.72] But since I'm not running on a local GPU, I'm not sure that I necessarily need to do that.
[1415.06 → 1418.40] I think for any real workflow I do, I kind of, I have a Docker container.
[1418.58 → 1425.28] And I know for, especially at work, we have a specific production containers that we use for our workflows there.
[1425.52 → 1427.02] And so we'll pull down one of those.
[1427.22 → 1428.88] There are a lot of options on that.
[1429.04 → 1436.56] I know NVIDIA, for instance, has a bunch of production workload containers that you can use as a base for your company.
[1436.56 → 1441.52] And this is assuming that you are running on NVIDIA equipment in that case that are already optimized for that.
[1441.64 → 1452.66] And so for me, it's really easy to grab one of those production containers and then do the customization I need, add my model into it, figure out how I'm going to get the data into that for training.
[1452.90 → 1457.20] I've done that a couple of different ways over time, depending on what the resources available to me are.
[1457.38 → 1462.52] But when I'm serious about doing work, and I'm not just playing around, I'm starting Docker from the get-go.
[1462.52 → 1467.82] Yeah, and what I kind of often, so I love using Docker as well.
[1468.02 → 1474.98] How I kind of think about the layers that I need to deploy to enable my AI workflow.
[1475.46 → 1477.64] A lot of times what I'm running will be in Docker.
[1478.04 → 1485.38] But then under the hood or layer down, I like to think of kind of two primary types of resources that I need.
[1485.54 → 1487.54] And those being computed and storage.
[1487.54 → 1493.88] So if you just have computed, you might be able to run your Docker container, but then you're going to have where you're going to put your data.
[1494.04 → 1498.08] It's not so great to put 200 terabytes of data in a Docker container.
[1498.24 → 1500.20] I don't know that anyone's actually done that.
[1500.30 → 1504.40] Although some people have put, you know, like to put data in containers.
[1504.40 → 1511.24] So I like to think of kind of under the hood or a layer down, we need kind of two sets of resources.
[1511.24 → 1514.00] Those being computed and storage.
[1514.32 → 1520.42] Now with compute, of course, you have some choices as far as whether that's going to be in the cloud or on-prem.
[1520.60 → 1524.64] Similar to basically any engineering workflow that any company does.
[1524.64 → 1533.08] And then storage wise, I think, you know, mostly what I've interacted with is pretty agnostic to my AI workflow.
[1533.22 → 1536.32] Sometimes a lot of times you don't have the choice of where your data is stored.
[1536.46 → 1542.08] You might be working with a production, you know, MySQL database or Postgres.
[1542.14 → 1548.22] Or you might be working with data that's just dumped to an object store like S3 or something like that.
[1548.22 → 1555.06] So typically the storage options in my cases are oftentimes driven by things already existing within a company.
[1555.20 → 1557.06] So you might not have a lot of say in that.
[1557.28 → 1561.62] But then compute wise, maybe you do have a little bit more say in that.
[1561.88 → 1568.04] So when you're running those Docker containers and that sort of thing, you mentioned that, Chris, sometimes you run on like NVIDIA hardware.
[1568.32 → 1574.46] So when you're saying that, I think what you're meaning is kind of like on-premise NVIDIA workstation.
[1574.46 → 1579.84] So how is that different from running on a GPU like in the cloud?
[1579.98 → 1581.30] Could you kind of go into that a little bit?
[1581.70 → 1586.56] Sure. So, I mean, it really comes down to the constraints, as you said, that you have.
[1586.62 → 1593.48] If you're in, I don't have a particular preference, but let's say AWS and you're using SageMaker, and you're pulling your data out of S3.
[1594.00 → 1596.90] You know, it is what it is in terms of that's the service they're offering.
[1596.98 → 1598.20] It's a great way of doing it.
[1598.20 → 1603.88] But to contrast against that, we have a lot of DGX equipment at Lockheed.
[1604.00 → 1605.94] And my previous employer had DGXs too.
[1606.30 → 1611.06] And that means that you're running, you're kind of into a data centre where you have the DGX set up.
[1611.08 → 1616.84] And then you have a set of equipment with storage and such around that to enable your operation.
[1617.08 → 1620.48] So, you know, it's great if you have a DGX2 that you're operating on,
[1620.48 → 1624.52] but you're going to need the storage around that to pull from and to push out to.
[1624.70 → 1626.58] There may be some processing around there.
[1626.68 → 1633.50] So you end up essentially creating a whole build around your DGX to enable those operations.
[1633.80 → 1637.32] And so it's not so different really from the cloud environment.
[1637.52 → 1640.22] You know, either way you have storage, you're pulling data from it,
[1640.26 → 1644.16] you're running it through assuming that it's been pre-processed and is ready for training.
[1644.42 → 1645.90] And then you got the output somewhere.
[1646.18 → 1650.36] And so, and then you have to have access to all of that from wherever you're coming in.
[1650.48 → 1656.32] So the AWS or Google or Azure world each has their own ways of doing all those pieces.
[1656.50 → 1659.28] If you're running your own data centre, then it really depends on the company.
[1659.68 → 1664.32] Whereas I've worked for two companies with DGX equipment that I was able to use,
[1664.42 → 1670.68] that piece of it was the same, but how they built around the DGXs was different in both companies.
[1670.76 → 1675.54] So just because you have the luxury of buying an AI supercomputer like that
[1675.54 → 1678.14] doesn't mean that your setup is going to be the same.
[1678.14 → 1681.42] It's very distinct on how your organization wants to configure it.
[1681.70 → 1686.92] Yeah, I think your experiences are almost on a total different side of the spectrum from mine,
[1687.02 → 1692.04] probably only because, you know, right now I'm working with a nonprofit.
[1692.32 → 1694.76] So I think this is a good, a good contrast.
[1694.92 → 1700.38] So obviously the companies that you've worked for and do have, you know, embedded AI research teams,
[1700.38 → 1703.02] maybe they invest in some of this NVIDIA hardware.
[1703.66 → 1710.32] But for me, doing sort of machine learning and AI data related work with a nonprofit,
[1710.64 → 1718.42] I would basically be left out of every room I was in if I tried to get anyone to buy a 200 grand NVIDIA box.
[1718.62 → 1723.16] So I've pretty much relied on everything in the cloud when I've needed it.
[1723.16 → 1728.82] And I think that wherever you fall on that spectrum for your AI team, there is a route forward.
[1729.02 → 1736.30] So it's great if you're able to afford that kind of dedicated hardware, and you have that commitment level within your organization.
[1736.30 → 1741.46] But maybe you're not at that point yet, or you're just, you know, you're a startup trying to get into this space
[1741.46 → 1744.60] or another organization that doesn't have a huge AI team.
[1744.60 → 1748.12] You can do very similar things in the cloud.
[1748.28 → 1753.04] So every cloud provider has instances that are available with specialized hardware.
[1753.18 → 1760.98] They also have a lot of services that are, you know, that will allow you to spin up clusters to do distributed computing,
[1761.22 → 1762.62] you know, like Kubernetes clusters.
[1763.02 → 1765.46] And there are frameworks on top of that we can talk about in a bit.
[1765.54 → 1769.02] So I think wherever you fall in that spectrum, there's a route forward.
[1769.02 → 1778.46] But in either case, you're going to have some number of compute nodes on premise or in the cloud that maybe some have just regular CPUs,
[1778.52 → 1779.82] maybe some have GPUs.
[1779.90 → 1785.62] And then you're going to have some storage that is storing the data that you're working with for your training data sets and that sort of thing.
[1786.04 → 1789.42] So now thinking about like, let's say that's the base.
[1789.42 → 1796.32] So you figured out whether you're going to be in the cloud or on premise, whether you have dedicated hardware using the cloud stuff.
[1796.32 → 1802.76] What do AI people actually run on top of this compute and storage infrastructure?
[1803.16 → 1810.68] So maybe let's first think about what do people run on this for kind of model development and experimentation?
[1811.24 → 1813.36] So what's your experience there, Chris?
[1813.52 → 1818.32] What are some of the maybe you mentioned like notebook environments like Jupyter?
[1818.56 → 1820.48] Do you run those off of your laptop?
[1820.66 → 1825.66] Do you have experience hosting those within your infrastructure for model development, or how does that work for you?
[1825.66 → 1828.00] So often I will start locally.
[1828.38 → 1835.12] So it kind of depends on how at this point with me being more Docker focused, I found that it's easier to go ahead.
[1835.28 → 1841.32] And in the beginning, I used to open up a Jupyter notebook locally, but then I had to package it up and go put it into the Docker.
[1841.46 → 1849.20] And I've gotten to where I just start off with a Docker container these days because there's a little bit more to do in that slightly than just opening up a notebook.
[1849.20 → 1853.30] But that way I don't have to package it all up later.
[1853.46 → 1857.72] It's easier because once I get into my workflow, I can start just building.
[1857.96 → 1861.48] And then when it makes time, I can run the container on the infrastructure.
[1861.82 → 1865.00] And so for me, that is personally, that's an easier way to go.
[1865.32 → 1867.52] There's also how do you set up the resources?
[1867.74 → 1868.82] What do you want to select?
[1868.82 → 1878.32] I've used Domino Data Labs and that is enabling you, kind of gives you a very nice front end when you have different types of equipment out there.
[1878.46 → 1879.68] It's something obviously you don't need.
[1879.78 → 1887.78] If you're in a cloud environment, then you have those interfaces that you're going to be used to from that provider, whichever one you want to choose to do that.
[1887.78 → 1892.66] But Domino kind of gives me that on the front end if I have our own infrastructure back end.
[1893.14 → 1897.84] And then at that point, it's just moving it, scheduling it and moving it over there.
[1898.08 → 1901.54] And again, there's a lot of variability on how you want to do that.
[1901.84 → 1904.04] Yeah, I think you're right, Chris.
[1904.14 → 1907.76] I think that variability also falls onto a spectrum.
[1907.98 → 1917.06] So we talked about the spectrum of the hardware that you might use that all this is running on in terms of specialized hardware versus things available in the cloud.
[1917.06 → 1918.72] But I think there's a spectrum here, too.
[1919.16 → 1921.02] There's a lot on one side of the spectrum.
[1921.02 → 1936.86] There's a lot of open source free tooling that will allow you to do kind of interactive model development and run it on pretty much any hardware like in the cloud, on Kubernetes, in Docker, on-prem, things like Jupyter Lab.
[1936.86 → 1939.60] It's like Jupyter, but multi-user Jupyter.
[1939.78 → 1944.44] So you can have multiple Jupyter kernels and all of this stuff and run a lot of different notebooks.
[1944.70 → 1946.50] But there's also other free options.
[1946.50 → 1956.64] There's Google's Collaborator or Cola, which has a bunch of kind of free GPU resources and other things and notebooks that you can manage.
[1957.44 → 1963.18] There are things like Binder that will spin up Jupyter notebooks from a GitHub repo.
[1963.36 → 1968.42] So that's kind of one side of the spectrum where you're using a lot of these free kind of environments.
[1968.42 → 1977.56] On the other side of the spectrum, there's kind of data science platforms like you were talking about, Chris, which are things like Domino and Data Robot and Databricks, H2O.
[1977.88 → 1979.48] Some of these are not free.
[1979.82 → 1981.56] In fact, some of them are not very cheap.
[1981.90 → 1989.16] Some of them are a little bit more moderately priced depending on how many users you have and what workloads you're running.
[1989.16 → 1997.12] But a lot of this kind of give you, like you were saying, a really nice interface maybe to track your data, track different experiments that you're doing.
[1997.24 → 2004.94] My experience is that a lot of them are centred around the idea of experiments and running experiments and iterating on those experiments.
[2004.94 → 2013.22] They're not necessarily meant for running production AI services, but very much for model development and experimentation.
[2013.80 → 2013.86] Yeah.
[2014.00 → 2029.24] You know, by the way, as an aside, while we're talking about some of these different providers, I've noted over the past year in particular that there's a real battle between the cloud providers to draw in entry level students in this AI world in terms of doing your initial training.
[2029.24 → 2033.68] Because any course you may select is going to have a cloud provider that you get used to.
[2033.68 → 2047.46] So, for instance, deeplearning.ai, which uses Coursera, is right now they have the Coursera for the classroom stuff, but they're also using Google Cola in the current set of courses.
[2047.84 → 2049.68] And that way you kind of get used to that environment.
[2049.90 → 2051.68] So you get a little bit of buy-in.
[2052.14 → 2058.28] If you're taking an NVIDIA Deep Learning Institute course, they're using their own NVIDIA GPU Cloud.
[2058.72 → 2059.98] You know, we tend not to talk about that.
[2059.98 → 2066.44] We tend to talk about Microsoft, Google, and AWS in general, but NVIDIA has theirs and there are other providers out there as well.
[2066.60 → 2075.08] So as we're talking about what you're buying into, that very well may be impacted by how you were trained and what your comfort level is.
[2075.44 → 2076.04] Yeah, for sure.
[2076.58 → 2083.10] Yeah, I know that I'm very comfortable with certain things that other people just don't like and laugh at me for using.
[2083.10 → 2088.18] So I think that, you know, you have to experiment as well and find where you're comfortable.
[2088.82 → 2089.24] So, okay.
[2089.30 → 2092.60] So we have, you know, the base of compute and storage.
[2092.84 → 2103.78] On top of that compute, we are running certain things for experimentation and model development, like somewhere on that spectrum of, you know, open source sort of notebook things like JupyterLab.
[2103.78 → 2110.68] And then, or maybe less open source or not open source things like Domino for data science platforms.
[2110.68 → 2122.92] So the next thing that we might want to run on top of the compute and storage is some way to kind of automate model training and the pre-processing and post-processing of data.
[2123.14 → 2134.82] So automatically, you know, when new data is brought in, you might want to update a training data set, retrain your model, export a serialized version of that model, and then export that into some serving framework.
[2135.16 → 2138.60] So this is typically called like pipelining and automation.
[2138.60 → 2140.66] There's a lot of tools for this.
[2140.86 → 2144.98] I'm a Packet Arm user, and I work for them full-time for a while.
[2145.08 → 2147.54] So I'm definitely biased in that way.
[2147.98 → 2149.20] And I love Packet Arm.
[2149.56 → 2151.82] But that's certainly not the only thing you can use.
[2151.94 → 2155.94] There are things like Luigi and Airflow that are commonly used for this.
[2156.46 → 2160.52] I don't see quite as much as Hadoop and Spark stuff going on these days.
[2160.66 → 2161.18] But I don't know.
[2161.26 → 2166.24] What is your impression of the landscape and, you know, where things are headed with this side of things?
[2166.24 → 2173.04] Well, you still in the enterprise, you're still seeing a lot of Hadoop, especially Spark more so in the enterprise environments.
[2173.36 → 2178.32] And I don't really, even though I'm in big companies now, I really come from smaller companies.
[2178.50 → 2181.08] And so it has been interesting.
[2181.28 → 2184.68] I almost bypassed those particular technologies along the way.
[2184.80 → 2186.04] And then I've kind of come back.
[2186.04 → 2191.12] So as you're in a large organization, you do have to accommodate those in those data flows.
[2191.44 → 2198.24] Given the choice, I mean, and this is, I'm probably heavily influenced by you in terms of liking Packet Arm for that.
[2198.72 → 2202.96] Obviously, I think you mentioned Below is another tool that is used.
[2203.20 → 2204.46] And that one's good.
[2205.14 → 2209.22] Kind of everything, Kubernetes, everything from my perspective, because it kind of won.
[2209.32 → 2212.60] I don't have to think about that too much anymore and just say, let's go that route.
[2212.72 → 2215.36] I know Packet Arm is built on top of Kubernetes as well.
[2215.36 → 2216.06] How about you?
[2216.44 → 2216.64] Yeah.
[2216.80 → 2218.38] So, I mean, I think you're right.
[2218.56 → 2221.74] Obviously, people have invested a lot in Hadoop over time.
[2221.88 → 2224.08] And so you have to deal with that in certain cases.
[2224.08 → 2228.66] And this is another one of those concerns that we were talking about that might drive your infrastructure choice.
[2228.66 → 2238.36] If you have to write on top of HDFS and have a ton of stuff written in, you know, Hive queries and all of that, you might be stuck with using that for whatever reason.
[2238.68 → 2242.98] You know, thankfully, I kind of have some flexibility in my projects.
[2242.98 → 2245.90] So I like to do things a little bit differently.
[2246.08 → 2247.60] But there are a lot of choices out there.
[2247.68 → 2253.74] But I think in general, kind of circling back to kind of how I have this architecture laid out in my head.
[2254.18 → 2256.28] You've got the compute and storage.
[2256.28 → 2260.96] You've got those experimentation pieces on top of that, maybe like JupyterLab or something.
[2261.18 → 2276.26] Then you have some type of automated, like non-interactive tool that will allow you to automate the retraining of your models or updating of data sets or updating of databases that drive certain services or that sort of thing.
[2276.26 → 2280.46] And that if it involves large data sets, it might involve distributed processing.
[2280.80 → 2285.24] If it involves model training, it might involve, you know, specialized hardware.
[2286.10 → 2297.66] But, you know, having a pipelining tool, something like Airflow or Picketers, Cube flow, Spark, these sorts of things will allow you to update those large data sets over time.
[2297.92 → 2299.74] But that's definitely not the end of the story.
[2299.74 → 2302.16] So let's say that we're updating our model over time.
[2302.54 → 2306.54] How are we going to then serve that model on top of?
[2306.72 → 2308.12] So maybe we've trained it.
[2308.24 → 2313.50] Now we want to use that serialized trained model to run many, many inferences.
[2314.06 → 2315.42] How are people doing that?
[2315.92 → 2318.48] So it's kind of funny leading into that.
[2318.62 → 2323.62] That's the part that most people don't think their way through all the way is how do you get to deployment?
[2323.74 → 2329.64] How do you make this thing that you've created actually work in real life with the rest of your software and hardware?
[2329.74 → 2330.20] Out there.
[2330.60 → 2337.26] And so some of the things that need to be thought about there are what technologies are going to use.
[2337.32 → 2338.36] I use Tensor RT.
[2338.86 → 2341.30] And, you know, you have to be thinking about how you're serving.
[2341.44 → 2351.16] And there are different approaches to that, as well as something that's often forgotten in this space is CI to CD, which is continuous integration, continuous deployment.
[2351.16 → 2354.78] We're so used to, in the software world, thinking about that.
[2355.20 → 2361.20] But the kind of the data science world and the thinking that dominates the AI space often forgets that altogether.
[2361.20 → 2366.12] Or in some cases, you'll find data scientists who aren't really familiar with it at all.
[2366.22 → 2373.60] And they're so used to doing things that are going to stay on a server, you know, or website or something that's internal to an organization.
[2373.60 → 2383.70] That now that we are getting to where you have AI models being pushed out for inference on the edge all over the place and eventually may far outnumber things even in the servers as we move forward over the years.
[2384.34 → 2385.50] That's going to be really critical.
[2385.50 → 2396.26] So, you know, things like thinking your way through things like TensorFlow serving, you know, Tensor RT and different things like Monet has an approach to doing that as well.
[2396.38 → 2397.10] What about yourself?
[2397.44 → 2404.54] Yeah, I mean, I think what you want to be thinking about is you have that period of experimentation and model development.
[2404.54 → 2406.50] And that may be local, that may be in the cloud.
[2406.50 → 2423.50] But ultimately, you're going to want to run an automated non-interactive pipeline that takes in some amount of training data, trains your model using some framework, maybe TensorFlow or PyTorch on a workstation or on a cluster like a Kubernetes cluster.
[2423.50 → 2431.82] And then outputs a serialized version of that to some resource like maybe an object store like S3 or something like that.
[2431.82 → 2452.00] And then you may have a this may be plugged into CCD in some way where, you know, maybe I push new model training code to GitHub and a CCD tool like Jenkins is listening on that GitHub repo, knows that my code has changed, automatically runs my pipeline to retrain my model.
[2452.00 → 2466.92] That model is retrained. As soon as it's retrained, then there's a call made to update the model that's being used in maybe TensorFlow serving or another serving framework like Monet or Selden or something like that.
[2467.08 → 2474.50] Or maybe your own custom service that's using that model, something that other software engineers have written or something like that.
[2474.54 → 2479.74] Or it could even be a JavaScript app or a mobile app that is updated based on that.
[2479.74 → 2489.12] I think the more pieces of that you can automate, the better in my experience, assuming that you're going to be wanting to update those things fairly regularly.
[2489.50 → 2505.50] Yeah, I think to kind of package the last couple of minutes up, the takeaway there is if you're a data scientist, and you may be very comfortably starting off in your Jupyter notebook world where you're creating a model that has to go be trained, but at some point it has to come back to software.
[2505.50 → 2535.48] At some point it has to come back to software.
[2535.50 → 2555.44] If you're a server that is supporting your business operations or whether it be in the billions of IoT devices that we're going to have out there or whether it be on your phone or future mobile devices that we haven't gotten to yet, that's where it's going to live and that's where it's going to be doing the thing that you're creating it for.
[2555.44 → 2561.58] And so thinking of that end right early in the process is really crucial.
[2561.80 → 2562.80] It only matters.
[2562.92 → 2567.54] This thing you're working on only matters if it's usable in the real world out there as a piece of software.
[2567.96 → 2570.90] I think that's a great way to close things out.
[2570.90 → 2576.74] Obviously, there are a ton of things that we did not have time to talk about.
[2577.18 → 2581.16] So please join our Slack channel at changelog.com slash community.
[2581.34 → 2587.18] We'd love to chat with you about this sort of infrastructure related things and practical things about your setup.
[2587.18 → 2592.10] Before we leave, I just wanted to share a couple of relevant learning resources.
[2592.62 → 2599.20] We always like to give some learning resources for people that are wanting to level up in the areas that we're talking about.
[2599.62 → 2602.26] So we've mentioned Google's Cola a couple of times.
[2602.26 → 2616.66] I would highly recommend if you're just wanting to experiment with TensorFlow or PyTorch on GPUs and on TPUs or these sorts of specialized types of hardware, you can do that for absolutely free on Google's Cola.
[2616.94 → 2618.20] There's a ton of examples.
[2618.42 → 2620.12] There's a great intro video to that.
[2620.54 → 2623.14] Also, there's Intel's AI Dev Cloud.
[2623.58 → 2625.74] I've played around on there a good bit.
[2625.98 → 2631.64] That's a great place to experiment with hardware other than GPUs like Intel's Leon processors.
[2631.64 → 2639.22] They have optimized really fast versions of like TensorFlow and PyTorch that you can use there and without a lot of commitment.
[2639.46 → 2642.26] So just jump in, try some examples.
[2642.60 → 2651.86] A lot of these frameworks and tools that we've mentioned have great examples that you can try out with relatively low cost or no cost in some cloud environment.
[2652.20 → 2656.46] So try some things out, get your hands dirty and let us know what you build.
[2656.80 → 2657.40] Well, sounds good.
[2657.50 → 2660.38] Thanks for hopping on this episode, Daniel.
[2660.38 → 2661.68] This was a perfect conversation.
[2661.90 → 2669.62] And I think actually we'll probably have some spinoff episodes of deep diving in some of the topics that we've hit today that we just didn't have time for.
[2669.88 → 2670.16] For sure.
[2670.38 → 2670.54] Yeah.
[2670.60 → 2671.46] See you next week, Chris.
[2671.66 → 2672.04] Take care.
[2672.34 → 2672.64] Bye-bye.
[2672.64 → 2675.38] All right.
[2675.42 → 2678.06] Thank you for tuning into this episode of Practical AI.
[2678.32 → 2683.42] If you enjoyed this show, do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it.
[2683.52 → 2687.00] If you are on Twitter or social network, share a link with a friend, whatever you got to do.
[2687.22 → 2688.68] Share the show with a friend if you enjoyed it.
[2688.98 → 2691.62] And bandwidth for changelog is provided by Vastly.
[2691.74 → 2693.18] Learn more at fastly.com.
[2693.36 → 2696.58] And we catch our errors before our users do here at changelog because of Rollbar.
[2696.58 → 2699.20] Check them out at robot.com slash changelog.
[2699.28 → 2702.00] And we're hosted on Linde cloud servers.
[2702.36 → 2703.98] Head to linode.com slash changelog.
[2704.06 → 2704.52] Check them out.
[2704.60 → 2705.42] Support this show.
[2705.76 → 2709.00] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2709.44 → 2711.52] The music is by Break master Cylinder.
[2711.90 → 2715.36] And you can find more shows just like this at changelog.com.
[2715.56 → 2717.48] When you go there, pop in your email address.
[2717.78 → 2723.80] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2724.20 → 2724.98] Thanks for tuning in.
[2724.98 → 2725.90] We'll see you next week.
[2726.58 → 2756.56] We'll see you next week.
[2756.56 → 2763.76] Explore the inner workings of the human brain to understand behaviour change, habit formation, mental health, and the complexities of the human condition.
[2764.14 → 2769.98] It's hosted by myself, Adam Stachowiak, and my good friend, Muriel Reese, a doctor in clinical psychology.
[2770.52 → 2776.24] It's about brain science applied, not just how the brain works, but how we apply what we know about the brain to better our lives.
[2776.82 → 2777.18] Here we go.
[2777.18 → 2781.02] So where do we begin to understand the mind?
[2781.02 → 2784.28] Humans have brains with all this neural activity.
[2784.92 → 2787.36] And I'm just thinking about what I know about my brain.
[2787.46 → 2789.94] I understand that it's up there, what it is.
[2790.02 → 2791.66] I understand it's very important to me.
[2791.78 → 2793.58] And without it, I couldn't function.
[2794.22 → 2797.44] But, you know, my mind isn't my brain's activity.
[2797.44 → 2804.06] How can we begin to break down the brain and the mind to really understand the operations behind our mind?
[2804.06 → 2812.52] Well, one of the things that is really important when we're looking at the brain and the mind is actually the words that we use to describe different things.
[2812.62 → 2816.24] And so I think it's really important to be as clear as possible.
[2816.48 → 2820.48] And so I think we want to differentiate the brain from the mind.
[2820.76 → 2823.12] And so the brain is made up of different structures.
[2823.12 → 2830.90] And then the mind is sort of the inner workings of the physical structures, which is not observable.
[2831.14 → 2837.70] But when we're looking at the brain, there are some primary structures that are fundamental to being human.
[2837.70 → 2840.58] And that involves sort of three different brains.
[2840.78 → 2844.96] Well, we have the brain stem, the limbic brain, and the prefrontal cortex.
[2845.14 → 2852.26] I know I might get a little petty in talking about some of these things, but I think it's helpful when we can have a visual.
[2852.26 → 2857.88] So if you put your right hand up in the air like you're being sworn in with all five fingers next to each other.
[2857.88 → 2858.20] I got my hand up.
[2858.20 → 2866.00] Go ahead and fold your thumb across the palm of your hand and then close your four fingers over the top of your thumb.
[2866.10 → 2867.18] Okay, I got that.
[2867.38 → 2876.40] And so in order to correlate these with different structures, your wrist would be synonymous with your brain stem, which is the reptile brain.
[2876.40 → 2883.08] Then your thumb is the limbic brain or mammalian brain, which means all mammals have that part of the brain.
[2883.34 → 2889.50] And then your four fingers are what we refer to as the frontal lobe or part of the prefrontal cortex.
[2890.02 → 2899.38] Okay, so we sort of have three brains in one and all do different things in our brain to help us be able to live and move and be safe.
[2899.38 → 2904.12] So if we have three brains in one, they all have their different roles.
[2904.28 → 2909.32] It sounds like, you know, the reptilian seems, I don't know, like it can't think very well.
[2909.46 → 2918.80] When it comes to the reptilian brain, I'm assuming it's just sort of like, you know, gut reactions in a very, very quick thinking, you know, almost subconscious kind of stuff potentially.
[2918.90 → 2919.30] Is that right?
[2919.92 → 2920.78] Yeah, you're spot on.
[2921.00 → 2925.86] Sometimes I think, again, it's helpful to parallel things with what we do know and do understand.
[2925.86 → 2929.64] So thinking of different animals, reptiles, right?
[2929.92 → 2931.00] Lizards, turtles.
[2931.52 → 2937.42] So the brain stem is really only responsible for these key functions within the body.
[2937.56 → 2941.48] So breathing, heart rate, the essentials and fight or flight.
[2941.86 → 2948.38] If a lizard is afraid, right, it needs to figure out what it needs to do to survive.
[2948.50 → 2951.68] So the brain stem is just preoccupied with the function of survival.
[2952.02 → 2952.94] How do I not die?
[2952.94 → 2960.02] And then if we move up to that mammal brain, right, we can think about, you know, cats or dogs, bats.
[2960.44 → 2965.56] And that mammal brain or limbic brain is really the feeling centre of our brain.
[2965.66 → 2967.92] There's two key brain structures as part of that.
[2968.02 → 2974.16] And that is involving the amygdala and the hippocampus, which is responsible for memory.
[2974.76 → 2980.54] The one thing I think is super fascinating about the mammal brain is really the way in which we bank memories.
[2980.54 → 2988.98] Whenever things have the most emotion associated with it, we're more likely to remember that.
[2989.38 → 2989.52] Okay.
[2989.54 → 2991.60] So it doesn't matter whether it's positive or negative.
[2991.60 → 2996.70] So be it a wedding, birth of a child, you know, or something super traumatic.
[2996.70 → 2999.38] Our brain goes, oh, that's so important to remember.
[2999.72 → 3002.80] It vacuums seals it so that we hold on to that.
[3002.80 → 3010.28] And so this is why, too, our lives have different meaning and being able to feel is a fundamental part of being human.
[3010.82 → 3013.48] The mammal brain is really the feeling centre.
[3013.62 → 3022.10] So as opposed to more of the fight or flight from the reptile brain, our mammal brains, they're still more unconscious, subconscious things.
[3022.24 → 3029.20] But imagine that the Dewey Decimal System of your brain sorts things according to feelings when we're mammals.
[3029.20 → 3033.38] That's a preview of Brain Science.
[3033.38 → 3041.04] If you love where we're going with this, email us to get on the list to be notified the very moment this show gets released.
[3041.36 → 3044.50] Email us at editors at changelaw.com.
[3044.60 → 3050.04] In the subject line put in all caps, BRAIN SCIENCE with a couple bangs if you're really excited.
[3050.54 → 3054.80] You can also subscribe to our master feed to get all of our shows in one single feed.
[3054.80 → 3060.72] Head to changelaw.com slash master or search in your podcast app for Change Law Master.
[3060.86 → 3061.46] You'll find it.
[3061.72 → 3065.88] Subscribe, get all of our shows and even those that only hit the master feed.
[3066.12 → 3068.04] Again, changelaw.com slash master.
[3068.04 → 3090.70] I want to be remembered for my gourmet line of frozen seafood dinners.
[3090.70 → 3091.30] Beep.
[3091.46 → 3092.46] Peace.
[3100.46 → 3100.70] Peace.
[3100.74 → 3101.28] Peace.
[3101.28 → 3101.42] Peace.
[3101.42 → 3101.70] Peace.
[3101.72 → 3103.28] Peace.
[3103.28 → 3105.74] Peace.
[3105.74 → 3106.28] Peace.
[3106.46 → 3106.86] Peace.
[3106.86 → 3107.48] Peace.
[3107.50 → 3108.34] Peace.
[3108.34 → 3108.40] Peace.
[3108.40 → 3108.60] Peace.
[3108.60 → 3108.70] Peace.
[3108.70 → 3109.30] Peace.
[3109.30 → 3112.78].
