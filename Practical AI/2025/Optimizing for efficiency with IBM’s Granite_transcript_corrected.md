[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.46 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[26.32 → 28.36] Thanks to our partners at Fly.io.
[28.36 → 31.10] Launch your AI apps in five minutes or less.
[31.40 → 33.38] Learn how at Fly.io.
[44.02 → 47.48] Welcome to another episode of the Practical AI podcast.
[47.84 → 48.74] This is Chris Benson.
[48.94 → 50.06] I am your co-host.
[50.48 → 55.46] Normally, Daniel Whiten ack is joining me as the other co-host, but he's not able to today.
[55.46 → 59.12] I am a Principal AI Research Engineer at Lockheed Martin.
[59.38 → 63.02] Daniel is the CEO of Prediction Guard.
[63.44 → 70.62] And with us today, we have Kate Soule, who is Director of Technical Product Management at
[70.62 → 71.90] Granite for IBM.
[72.30 → 73.38] Welcome to the show, Kate.
[73.66 → 74.14] Hey, Chris.
[74.20 → 74.84] Thanks for having me.
[74.84 → 81.62] So, I know we're going to dive shortly into what Granite is, and some of our listeners
[81.62 → 83.40] are probably already familiar with it.
[83.56 → 84.56] Some may not be.
[85.08 → 90.34] But before we dive into that, wondering, we're talking about AI models.
[90.48 → 95.92] That's what Granite is, and the world of LLMs, generative AI.
[96.48 → 101.66] Wondering if you could start off talking a little bit about your own background, how you arrived
[101.66 → 107.38] at this, and we'll get into a little bit about, you know, what IBM is doing and why it's interested
[107.38 → 111.44] in and how it fits into the landscape here for those who are not already familiar with
[111.44 → 111.54] it.
[111.90 → 112.14] Perfect.
[112.34 → 112.48] Yeah.
[112.54 → 112.94] Thanks, Chris.
[113.02 → 118.78] So, I lead the technical product management for Granite, which is IBM's large family of
[118.78 → 122.18] large language models that is produced by IBM Research.
[122.18 → 128.86] And so, I actually joined IBM and IBM Research a number of years ago before large language
[128.86 → 131.28] models really became popular.
[131.50 → 135.76] You know, they had a bit of a Netscape moment, right, back in November 2022.
[136.14 → 138.68] So, I've been working at the lab for a little while.
[139.06 → 144.26] I am a little bit of an odd duck, so to speak, in that I don't have a research background.
[144.44 → 145.32] I don't have a PhD.
[145.84 → 147.30] I come from a business background.
[147.30 → 152.72] I worked in consulting for a number of years, went to business school, and joined IBM Research
[152.72 → 157.96] and the AI lab here in order to get more involved in technology.
[158.22 → 161.32] You know, I've always kind of had one foot in the tech space.
[161.56 → 166.74] I was a data scientist for most of my tenure as a consultant and always, you know, thought
[166.74 → 169.14] that there were a lot of exciting things going on in AI.
[169.38 → 175.32] And so, I joined the lab and basically got to work with a lot of generative AI researchers
[175.32 → 178.60] before large language models really kind of became big.
[179.04 → 182.76] And, you know, about two and a half years ago, a lot of the technology we were working
[182.76 → 189.16] on, all of a sudden, we started to find and see that there were tremendous business applications.
[189.76 → 193.70] You know, OpenAI really demonstrated what could happen if you took this type of technology
[193.70 → 196.46] and Porsche fed it enough compute to make it powerful.
[196.60 → 197.90] It could do some really cool things.
[197.90 → 205.34] So, from there, we worked as a team really to spin up a program and offering at IBM for
[205.34 → 209.96] our own family of large language models that we could offer our customers in the broader
[209.96 → 211.10] open source ecosystem.
[211.88 → 217.00] Do you, I'm curious with, one of the things that I've, you know, we've noticed over time
[217.00 → 222.82] is different organizations kind of are positioning these large language models within their product
[222.82 → 225.48] offerings in unique ways.
[225.78 → 229.66] And we've, you know, we could go through some of your competitors and say they do this way.
[229.90 → 236.00] How do you guys see that in terms of, you know, how large language models fit into your product
[236.00 → 236.42] offering?
[236.62 → 239.48] Is there a vision that IBM has for that?
[239.96 → 240.12] Yeah.
[240.26 → 246.38] You know, I think the fundamental premise of large language models are that they are a building
[246.38 → 250.98] block that you get to build on and reuse in many different ways, right?
[251.04 → 255.14] Where one model can drive a number of different use cases.
[255.42 → 260.20] So, you know, from IBM's perspective, that value proposition resonates really clearly.
[260.20 → 266.10] We see a lot of our customers, our own internal offerings where, you know, there's a lot of effort
[266.10 → 272.82] on data curation and collection and kind of creating and training bespoke models for a specific task.
[272.82 → 277.30] And now with large language models, we get to kind of use one model and with very little
[277.30 → 280.08] labelled data, all of a sudden, you know, the world's your oyster.
[280.22 → 281.14] There's a lot you can do.
[281.94 → 288.26] And so that's a bit of the reason why we have centralized the development of our large language
[288.26 → 290.98] models within IBM research, not a specific product.
[291.52 → 297.74] It's one offering that then feeds into many of our different products and downstream applications.
[297.74 → 304.06] And it allows us to kind of create this building block that we can then also offer customers to
[304.06 → 305.76] be able to build on top of as well.
[305.88 → 310.76] And open source ecosystem developers, you know, we think there are a lot of different applications
[310.76 → 312.14] for that one offering.
[312.72 → 316.32] And so, you know, that's a little bit kind of from the organizational side, why we're,
[316.62 → 317.70] why it's kind of exciting, right?
[317.70 → 319.34] That we get to do this all within research.
[319.34 → 321.26] We don't have a P&L, so to speak.
[321.26 → 326.30] We're doing this to create ultimately a tool that can support any number of different use
[326.30 → 327.72] cases and downstream applications.
[328.30 → 328.62] Very cool.
[328.76 → 330.24] And you mentioned open source.
[330.40 → 336.68] So I want to ask you, because that's always a big topic among organizations is, if I remember
[336.68 → 340.50] correctly, Granite is under an Apache 2 license.
[340.60 → 341.56] Is that correct?
[341.94 → 342.64] That's correct.
[342.96 → 346.86] I'm just curious, because we've seen strong arguments on both sides.
[346.86 → 351.54] Why is Granite an open source license like that?
[351.66 → 355.56] What was the decision from IBM to go that direction?
[356.14 → 356.24] Yeah.
[356.38 → 361.18] Well, there was kind of two levels of decision-making that we had to make when we talked about
[361.18 → 362.00] how to license Granite.
[362.32 → 364.18] One was open or closed.
[364.68 → 369.60] So are we going to release this model, release the weights out into the world so that anyone
[369.60 → 372.44] can use it regardless if they spend a dime with IBM?
[372.44 → 378.84] And ultimately, IBM believes strongly in the power of open source ecosystems.
[379.36 → 383.42] A huge part of our business is built around Red Hat and being able to provide open source
[383.42 → 386.30] software to our customers with enterprise guarantees.
[387.14 → 393.50] And we felt that open AI was a far more responsible environment to develop and to incubate this
[393.50 → 394.44] technology as a whole.
[394.60 → 396.86] And when you say open AI, you mean open source AI.
[397.06 → 398.04] Open source AI.
[398.18 → 399.02] Just making sure.
[399.22 → 400.78] Very important clarification.
[400.78 → 402.30] Very important clarification.
[402.82 → 405.78] So that was why we released our models out into the open.
[406.20 → 408.00] And then the question was, under what license?
[408.12 → 409.90] Because there are a lot of models.
[410.18 → 411.34] There are a lot of licenses.
[412.24 → 419.66] And a bit of the moment that everyone's seeing is you have a gamma license for a gamma model.
[419.74 → 421.48] You've got a llama license for a llama model.
[421.58 → 422.96] Everyone's coming up with their own license.
[423.12 → 425.70] And in some ways, it makes sense.
[425.96 → 429.14] Models are a bit of a weird artifact.
[429.42 → 430.06] They're not code.
[430.06 → 432.34] You can't execute them on their own.
[432.46 → 434.32] They're not software.
[434.80 → 436.24] They're not data per se.
[436.36 → 438.96] But they are kind of like a big bag of numbers at the end of the day.
[439.32 → 444.38] So some of the traditional licenses, I think some people didn't see a clear fit.
[444.50 → 445.74] And so they came up with their own.
[445.96 → 449.82] There are also all these different kind of potential risks that you might want to solve
[449.82 → 454.08] for with a license with a large language model that are different from risks that you look
[454.08 → 455.74] at with software or data.
[456.00 → 460.28] But at the end of the day, IBM really wanted just to keep this simple, like a no-nonsense
[460.28 → 466.34] license that we felt would be able to promote the broadest use from the ecosystem without
[466.34 → 467.20] any restrictions.
[467.20 → 473.92] So we went with Apache 2 because that's probably the most widely used and just easy to understand
[473.92 → 474.96] license that's out there.
[475.84 → 481.84] And I think it really speaks also to where we see models being important building blocks
[481.84 → 482.92] that are further customized.
[482.92 → 489.92] So we really believe the true value in generative AI is being able to take some of these smaller
[489.92 → 493.76] open source models and build on top of it and even start to customize it.
[494.16 → 497.72] And if you're doing all that work and building on top of something, you want to make sure there
[497.72 → 500.00] are no restrictions on all that IP you've just created.
[500.56 → 504.04] And so that's ultimately why we went with Apache 2.0.
[504.28 → 504.68] Understood.
[504.96 → 507.58] And one last follow up on licensing, and then I'll move on.
[508.12 → 510.16] It's partially just a comment.
[510.16 → 517.36] IBM has a really strong legacy as someone in the AI world and decades of software development
[517.36 → 518.24] along with that.
[518.74 → 524.22] I know both Red Hat with the acquisition some years back being strong on open source and
[524.22 → 526.46] IBM both before and after has.
[527.12 → 532.56] Was it, I'm just curious, did that make it any easier do you think to go with open source?
[532.72 → 537.34] Like, hey, we've done this so much that we're going to do that with this thing too, even though
[537.34 → 539.66] it's a little bit newer in context.
[540.16 → 545.50] Culturally, did it seem easier to get there than some companies that possibly really struggle
[545.50 → 547.62] with that don't have such a legacy in open source?
[548.12 → 549.62] I think it did make it easier.
[549.90 → 556.28] I think there are always going to be like any company going down this journey has to take
[556.28 → 558.60] a look at, wait, we're spending how much on what?
[558.70 → 560.14] And you're going to give it away for free?
[560.14 → 565.12] And come up with their own kind of equations on how this starts to make sense.
[565.60 → 571.10] And I think we've just experienced as a company that the software and offerings we create are
[571.10 → 575.62] so much stronger when we're creating them as part of an open source ecosystem than something
[575.62 → 577.36] that we just keep close to the best.
[577.48 → 583.26] So, you know, it was a much easier business case, so to speak, to make and to get the sign
[583.26 → 583.84] off that we needed.
[583.84 → 589.00] Ultimately, our leadership was very supportive in order to encourage this kind of open ecosystem.
[589.72 → 590.04] Fantastic.
[590.68 → 597.40] Turning a little bit, as IBM was diving into this realm and starting, you know, and obviously
[597.40 → 602.12] like you have a history with Granite that, you know, you guys are on 3.2 at this point.
[602.40 → 604.96] That means that you've been working on this for a period of time.
[604.96 → 612.26] But as you're diving into this very competitive ecosystem of building out this open source
[612.26 → 617.50] models that are big, they are expensive to make, and they're, and you're, you know,
[617.64 → 619.28] looking for an outsized impact in the world.
[619.60 → 625.14] How do you decide how to proceed with what kind of architecture you want?
[625.14 → 629.32] You know, how did you guys think about like, like you're looking at competitors, some of
[629.32 → 635.08] them are closed source, like open AI is some of them like meta AI, you know, has llama
[635.08 → 639.74] and you know, that that series, as you're looking at what's out there, how do you make
[639.74 → 643.82] a choice about what is right for what you guys are about to go build, you know, because
[643.82 → 645.54] that's one heck of an investment to make.
[645.72 → 650.10] And I'm kind of curious how you when you're looking at that landscape, how you make sense
[650.10 → 651.68] of that in terms of where to invest?
[652.38 → 652.96] Yeah, absolutely.
[652.96 → 660.38] So, you know, I think it's all about trying to make educated bets that kind of match your
[660.38 → 663.66] constraints that you're operating with and your broader strategy.
[664.20 → 669.96] So, you know, early on into our generative AI journey, when we were kind of getting the
[669.96 → 675.04] program up and running, you know, we wanted to take fewer risks, we wanted to learn how
[675.04 → 680.46] to do, you know, common architectures, common patterns before we started to get more, quote,
[680.46 → 684.40] unquote, innovative and coming up with net new additions on top.
[684.64 → 687.88] So early on the gen, and, you know, also, you have to keep in mind, this field has just
[687.88 → 691.76] been like changing so quickly over the past couple of years.
[691.76 → 694.38] So no one really knew what they were doing.
[694.38 → 698.46] Like, if we look at how models were trained two years ago, and the decisions that were
[698.46 → 705.46] made, the game was all about as many parameters as possible, and having as little data as possible
[705.46 → 706.70] to keep your training costs down.
[706.90 → 708.46] And now we've totally switched.
[709.02 → 714.66] The, you know, general wisdom is as much data as possible, and a few parameters as possible
[714.66 → 717.48] to keep your inference costs down once the model is finally deployed.
[717.48 → 720.68] So the whole field's been going through a learning curve.
[720.80 → 727.40] But I think early on, you know, our goal was really working on trying to replicate some
[727.40 → 731.16] of the architectures that were already out there, but innovate on the data.
[731.70 → 738.52] So really focus in on how do we create versions of these models that are being released that
[738.52 → 744.46] deliver the same type of functionality, but that were trained by IBM as a trusted partner
[744.46 → 751.26] working very closely with all of our teams to have a very clear and ethical data curation
[751.26 → 753.64] and sourcing pipeline to train the models.
[754.20 → 759.84] So that was kind of the first major innovation aim that we had was actually not on the architecture
[759.84 → 760.22] side.
[760.70 → 765.78] Then as we started to get more confident as the field started, I don't want to say mature
[765.78 → 767.90] because we're still very, again, very early innings.
[767.90 → 774.08] But, you know, we started to coalesce to some shared understandings of how these models should
[774.08 → 775.34] be trained and what works or doesn't.
[775.80 → 780.30] You know, then our goal really has started to focus on, from an architecture side, how
[780.30 → 782.44] can we be as efficient as possible?
[783.06 → 787.92] How can we train models that are going to be economical for our customers to run?
[788.42 → 793.22] And so that's where you've seen us focus a lot on smaller models for right now.
[793.22 → 796.04] And we're working on new architectures.
[796.22 → 797.96] So, for example, mixture of experts.
[798.40 → 804.92] There are all sorts of things that we are really focusing in really with kind of the mantra of
[804.92 → 810.12] how do we make this as efficient as possible for people to further customize and to run
[810.12 → 811.28] in their own environments.
[811.76 → 818.50] So that was a fantastic start to, as we dive into Granite itself, kind of laying it out.
[818.50 → 824.52] You know, your last comments, you talked about kind of the smaller, more economical models
[824.52 → 828.04] so that you're getting efficient inference on the customer side.
[828.18 → 832.84] You mentioned a phrase, which some people may know, some people may not, mixture of experts.
[833.28 → 839.86] Maybe talk as we dive into, you know, what Granite is and its versions going forward here.
[839.94 → 843.58] Maybe start with mixture of experts and what you mean by that.
[844.44 → 844.82] Absolutely.
[844.82 → 851.50] So if we think of how these models are being built, they're essentially billions of parameters
[851.50 → 856.62] that are representing small little numbers that basically are encoding information.
[857.50 → 862.24] And, you know, to like draw a really simple explanation, if you have a, you know, a linear
[862.24 → 866.48] regression, like you've got a scatter point, and you're fitting a line, Y equals MX plus B,
[866.60 → 868.96] like M is a parameter in that equation, right?
[869.04 → 871.10] So that except on the scale of billions.
[871.10 → 877.06] With mixture of experts, what we're looking at is, do I really need all 1 billion parameters
[877.06 → 878.88] every single time I run inference?
[879.50 → 880.60] Can I use a subset?
[880.78 → 887.56] Can I have kind of little expert groupings of parameters within my large language model
[887.56 → 892.28] so that at inference time, I'm being far more selective and smart about which parameters
[892.28 → 892.90] get called?
[892.98 → 899.40] Because if I'm not using all, you know, 8 billion or 120 billion parameters, I can run that
[899.40 → 900.70] inference far faster.
[901.16 → 902.60] So it's much more efficient.
[903.22 → 908.52] And so really it's just getting a little bit more nuanced of instead of like, I think a
[908.52 → 912.76] lot of early days of gender VI's just throw more compute at it and hope the problem goes
[912.76 → 913.02] away.
[913.16 → 918.20] We're now trying to like figure out how can we be far more efficient in how we build these
[918.20 → 918.54] models.
[918.54 → 922.62] So I appreciate the explanation on a mixture of experts.
[922.96 → 928.14] And that makes a lot of sense in terms of trying to use the model efficiently for an
[928.14 → 931.04] inference by reducing the number of parameters.
[931.32 → 938.40] I believe you're right now you guys have, is it 8 billion and 2 billion are the model sizes
[938.40 → 941.44] in terms of the parameters or have I gotten that wrong?
[941.60 → 943.38] We got actually a couple of sizes.
[943.58 → 944.28] So you're right.
[944.28 → 946.04] We've got 8 billion and 2 billion.
[946.46 → 951.88] But speaking of this mixture of expert models, we actually have a couple of tiny MOE models.
[952.02 → 953.30] MOE stands for mixture of experts.
[953.46 → 959.76] So we've got a MOE model with only a billion parameters and a MOE model with 3 billion parameters.
[960.34 → 963.54] But they respectively use far fewer parameters at inference time.
[963.62 → 968.84] So they run really, really quick designed for more local applications like running on a
[968.84 → 969.14] CPU.
[969.14 → 977.14] So, and when you make the decision to have different size models in terms of the number
[977.14 → 982.72] of parameters and stuff, do you have different use cases in mind of how those models might
[982.72 → 983.30] be used?
[983.54 → 987.88] And is there one set of scenarios that you would put your 8 billion and another one that would
[987.88 → 989.80] be that 3 billion that you mentioned?
[990.52 → 991.22] Yeah, absolutely.
[991.22 → 997.02] So if we think about it, when we're kind of designing the model sizes that we want to
[997.02 → 1002.04] train, a huge question that we're trying to solve for is, you know, what are the environments
[1002.04 → 1003.42] these models are going to be run on?
[1003.46 → 1007.94] And how do I, you know, maximize performance without forcing someone to have to like buy
[1007.94 → 1009.44] another GPU to host it?
[1009.88 → 1014.80] So, you know, there are models like those small MOE models that were actually designed much
[1014.80 → 1019.06] more for running on the edge locally or on a computer, like just a local laptop.
[1019.06 → 1024.44] We've got models that are designed to run on a single GPU, which is like our 2 billion
[1024.44 → 1026.46] and 8 billion models.
[1026.60 → 1028.62] Those are standard architecture, not MOE.
[1029.18 → 1034.98] And we've got models on our roadmap that are looking at how can we kind of max out what
[1034.98 → 1036.30] a single GPU can run?
[1036.40 → 1040.06] And then how can we max out what a box of GPUs could run?
[1040.12 → 1041.98] So if you got eight GPUs stitched together.
[1041.98 → 1048.94] So, you know, we are definitely thinking about those different kind of tranches of compute
[1048.94 → 1050.82] availability that customers might have.
[1050.88 → 1053.52] And each of those tranches could relate to different use cases.
[1053.52 → 1058.54] Like obviously, if you're thinking about something that is local, you know, there are all sorts of
[1058.54 → 1060.86] IoT type of use cases that that could target.
[1061.06 → 1066.32] If you are looking at something that has to be run on, you know, a box of eight GPUs, you
[1066.32 → 1069.66] know, you're looking at something that you have to be okay with having a little bit more
[1069.66 → 1075.44] latency, you know, time it takes for the model to respond, but where the use cases also probably
[1075.44 → 1080.44] needs to be a little bit higher value because it costs more to run that big model.
[1080.70 → 1085.28] And so you're not going to run like a really simple, like, you know, help me summarize this
[1085.28 → 1088.74] email task hitting, you know, eight GPUs at once.
[1089.50 → 1094.86] So as you talk about kind of the segmentation of these, of the, of the family of models and
[1094.86 → 1098.78] how you're doing that, I know one of the things you guys have a white paper, which we'll
[1098.78 → 1103.94] be linking in on the show notes for folks to go and take a look at either during or after
[1103.94 → 1105.22] they listen here.
[1105.30 → 1110.98] And you talk about some of the models being experimental chain of thought reasoning capabilities.
[1110.98 → 1114.28] And I was wondering if you could talk a little bit about what that means.
[1114.80 → 1114.92] Yeah.
[1115.04 → 1118.88] So really excited with the latest release of our Granite models.
[1119.30 → 1125.76] Just the end of February, we released Granite 3.2, which is an update to our 2 billion parameter
[1125.76 → 1127.60] model and our 8 billion parameter model.
[1128.26 → 1133.44] And one of the kind of superpowers we give this model, the new release is we bring in an
[1133.44 → 1135.06] experimental feature for reasoning.
[1135.42 → 1141.52] And so what we mean by that is there's this new concept, relatively new concept in the
[1141.52 → 1147.40] journey of AI called inference time compute, where if you, what that really equates to just
[1147.40 → 1152.16] to put in plain language, if you think longer and harder about a prompt, about a question,
[1152.68 → 1153.94] you can get a better response.
[1153.94 → 1155.18] I mean, this works for humans.
[1155.30 → 1156.38] This is how you and I think.
[1156.88 → 1159.20] But it's the same is true for large language models.
[1159.48 → 1165.32] And thinking here, you know, is a bit of a risk of anthropomorphizing the term, but it's
[1165.32 → 1166.90] where we've landed as a field.
[1166.96 → 1171.24] So I'll run with it for now is really saying generate more tokens.
[1171.72 → 1176.00] So have the model think through what's called a chain of thought, you know, generates logical
[1176.00 → 1181.84] thought processes and sequences of how the model might approach answering before triggering
[1181.84 → 1183.10] the model to then respond.
[1183.10 → 1191.16] And so we've trained Granite 8B 3.2 in order to be able to do that chain of thought reasoning
[1191.16 → 1195.74] natively, take advantage of this new inference time compute area of innovation.
[1196.30 → 1198.84] And what we've done is we've made it selective.
[1198.84 → 1202.76] So if you don't need to think long and hard about, you know, what is two plus two, you
[1202.76 → 1206.18] turn it off and the model responds faster just with the answer.
[1206.62 → 1211.68] If you are giving it a more difficult question, you know, and pondering the meaning of life,
[1211.72 → 1212.88] you might turn thinking on.
[1213.20 → 1217.92] And it's going to think through a little bit first before answering and answer with a much,
[1218.28 → 1222.86] in general, a longer kind of more chain of thought style approach where it's explaining
[1222.86 → 1225.52] kind of step by step why it's responding the way it is.
[1225.52 → 1231.10] Do you anticipate kind of, and I've seen this done from different organizations in different
[1231.10 → 1236.80] ways, do you anticipate that your inference time compute capability is going to be kind
[1236.80 → 1239.28] of there on all the models, and you're turning it on and off?
[1239.36 → 1244.24] Or do you anticipate that some of the models in your family are more specializing in that
[1244.24 → 1246.06] and that's always on versus others?
[1246.50 → 1249.02] Which way, you kind of mentioned the on and off.
[1249.08 → 1251.40] So it sounded like you might have it in all of the above.
[1251.40 → 1256.04] Yeah, you know, right now it's marked as an experimental feature.
[1256.16 → 1260.42] I think we're still learning a lot about how this is useful and what it's going to be used
[1260.42 → 1260.76] for.
[1260.96 → 1263.64] And that might dictate what makes sense moving forward.
[1263.96 → 1268.70] But what we're seeing is kind of universally, it's useful, one, to try and improve the quality
[1268.70 → 1271.50] of the answers, but two, as an explainability feature.
[1271.70 → 1275.80] Like if the model is going through and explaining more how it came up with the response that helps
[1275.80 → 1278.78] a human better understand the response.
[1278.78 → 1283.72] So, you know, I think it is something we're heavily considering just baking into the models
[1283.72 → 1286.28] moving forward, which is a different approach, right?
[1286.36 → 1289.20] Than some models which are just focused on reasoning.
[1289.46 → 1291.40] I don't think we're going to see that very long.
[1291.58 → 1294.82] You know, I think more and more we're going to see more selective reasoning.
[1295.08 → 1297.52] So like Claude 3.7 came out.
[1297.60 → 1300.74] They're actually doing a really nice job of this where you can think longer or harder
[1300.74 → 1303.28] about something or just think for a short amount of time.
[1303.38 → 1307.36] So I think we're going to see increasingly more and more folks move in that direction.
[1307.36 → 1311.54] But, you know, well, there's still, again, early innings, I'll say it again.
[1311.72 → 1316.62] So we're going to learn a lot over the next couple of months about where this is having
[1316.62 → 1317.52] the most impact.
[1317.60 → 1321.18] And I think that could have some structural implications of how we design our roadmap moving
[1321.18 → 1321.54] forward.
[1322.14 → 1322.26] Gotcha.
[1322.80 → 1328.84] With there has been a larger push in the industry toward smaller models.
[1328.84 → 1335.54] So, you know, kind of going back over the recent history of LLMs and, you know, you saw initially,
[1335.54 → 1340.48] you know, just the number of parameters exploding and the models becoming huge.
[1340.48 → 1344.64] And obviously, you know, we talked a little bit about the fact that that's very expensive
[1344.64 → 1347.24] on inference to run these things.
[1347.24 → 1351.00] And over the last, especially over the last, I don't know, year, year and a half, there's
[1351.00 → 1354.68] been a much stronger push, especially with open source models.
[1354.68 → 1357.62] We've seen a lot of them on hugging face, pushing to smaller.
[1358.14 → 1365.88] Do you anticipate as you're thinking about this capability of being able to reason that
[1365.88 → 1370.54] that's going to drive smaller model use toward models like what you guys are creating, where
[1370.54 → 1375.78] you're saying, OK, we have these large, you know, Claude has the, you know, big models and
[1375.78 → 1380.30] out there, you know, as an option or a LLAMA model that's very large.
[1380.30 → 1385.18] Are you guys anticipating kind of pulling a lot more mind share towards some of the smaller
[1385.18 → 1385.40] ones?
[1385.48 → 1390.32] And do you anticipate that you're going to continue to focus on these smaller, more
[1390.32 → 1394.52] efficient ones where people can actually get them deployed out there without breaking
[1394.52 → 1396.48] the bank of the organization?
[1396.62 → 1398.02] How how how does that fit in?
[1398.24 → 1398.36] Yeah.
[1398.48 → 1404.40] So look, one thing to keep in mind is even without thinking about it, without trying, we're
[1404.40 → 1409.92] seeing small models are increasingly able to do what it took a big model to do yesterday.
[1409.92 → 1416.50] So you look at what a tiny, you know, two billion parameter or granite to be model, for example,
[1417.32 → 1424.10] outperforms on numerous benchmarks, you know, a LLAMA 270B, which is a much larger but older
[1424.10 → 1424.68] generation.
[1424.86 → 1428.72] I mean, it was state of the art when it was released, but the technology is just moving
[1428.72 → 1429.60] so quickly.
[1429.94 → 1437.00] So, you know, we do believe that by focusing on some of the smaller sizes that ultimately
[1437.00 → 1442.00] we're going to get a lot of lift just natively because that is where the technology is evolving.
[1442.00 → 1446.14] Like we're continuing to find ways to pack more and more performance in fewer, fewer
[1446.14 → 1450.90] parameters and expand the scope of what you can accomplish with a small language model.
[1451.28 → 1455.96] I don't think that means we're going to ever get rid of big models.
[1455.96 → 1462.28] I just think if you look at where we're focusing, we're really looking at kind of where are the
[1462.28 → 1467.60] models, you know, if you think of the 80-20 rule, like 80% of the use cases can be handled
[1467.60 → 1470.58] by a model, you know, maybe 8 billion parameters or fewer.
[1470.70 → 1474.02] That's what we're targeting with granite, and we're really trying to focus in.
[1474.40 → 1479.64] We think that there's definitely still always going to be innovation and opportunity and
[1479.64 → 1482.44] complex use cases that you need larger models to handle.
[1483.06 → 1487.56] And that's where we're really interested to see, okay, how do we expand the granite family
[1487.56 → 1494.06] potentially focusing on more efficient architectures like mixture of experts to target those larger
[1494.06 → 1499.18] models and more complex model sizes so that you still get a little bit more of a more practical
[1499.18 → 1504.80] implementation of a big model, recognizing that again, it's not, you're always going to need,
[1505.06 → 1507.62] there's always going to be those outliers, those huge cases.
[1507.62 → 1513.22] We just don't think there's going to be as much business value, frankly, behind those compared
[1513.22 → 1518.12] to really focusing and delivering value on the small to medium model space.
[1518.44 → 1522.82] I think we've, that's one thing Daniel and I have talked quite a bit about is that we would
[1522.82 → 1523.42] agree with that.
[1523.62 → 1528.10] It's, I think the bulk of the use cases are for the smaller ones.
[1528.38 → 1533.16] While we're at it, you know, we've been talking about various aspects of granite a bit, but
[1533.16 → 1538.58] could we take a moment and have you kind of go back through the granite family and kind of
[1538.58 → 1544.40] talk about each component in the family, what it does, you know, what it's called, what it does,
[1544.40 → 1547.82] and just kind of lay out the array of things that you have to offer.
[1548.04 → 1548.44] Absolutely.
[1548.68 → 1553.20] So the granite model family has the language models that I went over.
[1553.20 → 1557.88] So between 1 billion to 8 billion parameters in size.
[1558.06 → 1562.24] And again, we think those are like the, the workhorse models, you know, 80% of the tasks,
[1562.32 → 1565.52] we think you can probably get away with a model that's 8 billion parameters or fewer.
[1565.52 → 1569.66] We also with 3.2 recently released a vision model.
[1570.12 → 1573.96] So these models are for vision understanding tasks.
[1574.06 → 1574.58] That's important.
[1574.72 → 1579.52] It's not vision or image generation, which is where a lot of the early like hype and excitement
[1579.52 → 1581.76] on generative AI came from is like DALI and those.
[1582.16 → 1587.80] We're focused on models where you provide an image and a prompt, and then the output is
[1587.80 → 1589.26] text, the model response.
[1589.46 → 1593.54] So really useful for things like image and document understanding.
[1593.54 → 1601.92] We specifically prioritize a very large amount of document and chart Q&A type data in its
[1601.92 → 1606.26] training data set, really focusing on performance on those types of tasks.
[1606.32 → 1611.72] So you can think of, you know, having a picture or an extract of a chart from a PDF and being
[1611.72 → 1613.40] able to answer questions about it.
[1613.76 → 1615.24] We think there's a lot of opportunity.
[1615.68 → 1618.86] So RAG is a very popular workflow and enterprise, right?
[1619.18 → 1620.60] Retrieval augmented generation.
[1620.60 → 1625.18] Right now, all the images and your PDFs and documents, they all get basically thrown
[1625.18 → 1625.44] away.
[1625.92 → 1631.20] But we really are working on, can we use our vision model to actually include all of those
[1631.20 → 1636.52] charts, images, figures, diagrams to help improve the model's ability to answer questions
[1636.52 → 1637.42] in a RAG workflow.
[1637.70 → 1639.04] So we think that's going to be huge.
[1639.52 → 1641.86] So lots of use cases on the vision side.
[1641.86 → 1648.22] And then we also have a number of kinds of companion models that are designed to work in parallel
[1648.22 → 1651.70] with a language model or a vision language model.
[1652.00 → 1655.58] So we've got our Granite Guardian family of models.
[1656.06 → 1658.18] And these are, we call them guardrails.
[1658.32 → 1662.86] They're meant to sit right in parallel with the large language model that's running the
[1662.86 → 1663.46] main workflow.
[1663.46 → 1668.70] And they monitor all the inputs that are coming into the model and all the outputs that are
[1668.70 → 1675.94] being provided by the model, looking for potential adversarial prompts, jailbreaking attacks,
[1676.44 → 1678.78] harmful inputs, harmful and biased outputs.
[1678.78 → 1681.34] They can detect hallucinations and model responses.
[1681.88 → 1686.30] So it's really meant to be a governance layer that can sit and work right alongside Granite.
[1686.44 → 1688.16] It can actually work alongside any model.
[1688.16 → 1693.02] So even if you've got an open AI model, for example, you've deployed, you can have Granite
[1693.02 → 1694.08] Guardian work right in parallel.
[1694.94 → 1698.38] And ultimately, just be a tool for responsible AI.
[1699.56 → 1704.40] And the last model I'll talk about is our embedding models, which again, is meant to be
[1704.40 → 1707.58] assist a model in a broader generative AI workflow.
[1707.84 → 1713.40] So in a RAG workflow, you'll often need to take large amounts of documents or text and convert
[1713.40 → 1717.86] them into what are called embeddings that you can search over in order to retrieve the
[1717.86 → 1719.74] most relevant info and give it to the model.
[1720.26 → 1724.08] So our Granite embedding models are used for that embedding step.
[1724.48 → 1730.18] So these are meant to do that conversion and can support in a number of different similar kind
[1730.18 → 1734.42] of search and retrieval style workflows working directly with the Granite large language model.
[1735.00 → 1735.10] Gotcha.
[1735.36 → 1740.22] I know there was some comment in the white paper also about time series.
[1740.92 → 1741.06] Yes.
[1741.06 → 1742.54] Can you talk a little bit to that for a second?
[1742.96 → 1743.44] Absolutely.
[1743.98 → 1747.80] So I mentioned Granite is multimodal in that it supports vision.
[1747.86 → 1750.94] We also have time series as a modality.
[1751.50 → 1755.40] And I'm really glad you brought these up because these models are really exciting.
[1755.74 → 1757.88] So we talked about our focus on efficiency.
[1758.26 → 1761.48] These models are like one to two million parameters in size.
[1761.64 → 1766.04] That is teeny tiny in today's generative AI context.
[1766.48 → 1771.48] Even compared to other forecasting models, these are tiny generative AI based time
[1771.48 → 1772.72] series forecasting models.
[1772.72 → 1778.72] But they are right now delivering top of the top marks when it comes to performance.
[1778.72 → 1784.06] So we just, as part of this release, submitted our time series models to Salesforce has a time
[1784.06 → 1785.42] series leaderboard called GIFT.
[1785.50 → 1787.82] They're the number one leaderboard on GIFT right now.
[1787.92 → 1789.88] Number one model on GIFT's leaderboard right now.
[1789.88 → 1792.06] And we're really excited.
[1792.38 → 1795.02] They've got over 10 million downloads on Hugging Face.
[1795.10 → 1796.60] They're really taking off in the community.
[1796.84 → 1803.20] So it's a really excellent offering in the time series modality for the Granite family.
[1803.60 → 1804.12] Okay.
[1804.24 → 1809.96] Well, thank you for going through kind of the layout of the family of models that you guys
[1809.96 → 1810.34] have.
[1810.34 → 1816.54] I actually want to go back and ask a quick question that you talked a bit about Guardian
[1816.54 → 1819.12] kind of providing guardrails and stuff.
[1819.32 → 1824.74] And that's something that if you take a moment to dive into, I think we often tend to focus
[1824.74 → 1829.82] kind of on, you know, the model, and it's going to do X, you know, whatever.
[1830.06 → 1837.30] I love the notion of integrating these guardrails that Guardian represents into a larger architecture,
[1837.30 → 1840.30] you know, to address kind of the quality issues.
[1840.34 → 1843.00] surrounding the inputs and the outputs on that.
[1843.32 → 1845.04] How did you guys arrive at that?
[1845.12 → 1848.68] I'm just, you know, and how did you, you know, it's pretty cool.
[1848.86 → 1852.86] I love the idea that not only is it there for your own models, obviously, but that, you
[1852.86 → 1857.16] know, that you could have an end user go and apply it to something else that they're doing,
[1857.22 → 1858.66] maybe from a competitor or whatever.
[1859.08 → 1861.30] How did you decide to do that?
[1861.30 → 1866.42] And, you know, that's, I think that's a fairly unique thing that we don't tend to hear as
[1866.42 → 1867.58] much from other organizations.
[1868.56 → 1868.72] Yeah.
[1868.72 → 1872.94] You know, so Chris, the one of the values, again, of being in the open source ecosystem
[1872.94 → 1875.94] is we get to like to build on top of other people's great ideas.
[1875.94 → 1879.06] So we actually weren't the first ones to come up with it.
[1879.32 → 1885.26] There's a few other guardrail type models out there, but, you know, IBM has quite a large,
[1885.80 → 1889.02] especially IBM research presence in security space.
[1889.02 → 1893.68] And there are challenges in security that are very similar to the large language models
[1893.68 → 1897.08] in general AI that, you know, it's not totally new.
[1897.40 → 1904.16] And what I think we've learned as a company and as a field is that you always need layers
[1904.16 → 1909.86] of security when it comes to creating a robust system against, you know, potential adversarial
[1909.86 → 1914.88] attacks and dealing with even the models on own innate safety alignment itself.
[1914.88 → 1919.68] So, you know, when we saw some of the work going out in the open source ecosystem on guardrails,
[1919.78 → 1924.84] you know, I think it was kind of a no-brainer from a perspective of this is another great
[1924.84 → 1931.18] way to add a layer on that generative AI stack of security and safety to better improve
[1931.18 → 1936.18] model robustness and figure out, you know, IBM's hyper-focus on what is the practical way
[1936.18 → 1937.28] to implement generative AI.
[1937.28 → 1939.22] So what else is needed beyond efficiency?
[1939.40 → 1940.02] We need trust.
[1940.10 → 1940.68] We need safety.
[1940.88 → 1942.64] Let's create tools in that space.
[1943.38 → 1948.94] So it kind of, you know, number of different reasons all made it a very clear and easy
[1948.94 → 1950.14] when to go and pursue.
[1950.52 → 1953.04] And we are actually able to build on top of Granite.
[1953.18 → 1959.62] So Granite Guardian is a fine-tuned version of Granite that's laser focused on these tasks
[1959.62 → 1964.12] of detecting and monitoring inputs going into the model and outputs going out.
[1964.12 → 1969.62] And the team has done a really excellent job, first starting at, you know, basic harm and
[1969.62 → 1973.70] bias detectors, which I think is pretty prevalent in other guardrail models that are out there.
[1973.80 → 1977.02] But now we've really started to kind of make it our own and innovate.
[1977.22 → 1982.32] So some of the new features that were released in the 3.2 Granite Guardian models include
[1982.32 → 1983.92] hallucination detection.
[1984.10 → 1988.90] Very few models do that today, specifically hallucination detection with function calling.
[1988.90 → 1995.20] So if you think of an agent, you know, whenever an LLM agent is trying to access or submit
[1995.20 → 1997.54] external information, it'll make what's called a tool call.
[1998.20 → 2003.46] And so when it's making that tool call, it's providing information based off of the conversation
[2003.46 → 2008.92] history saying, you know, I need to look up, you know, Kate Sol's information in the HR database.
[2009.28 → 2010.16] This is her first name.
[2010.26 → 2011.98] She lives in Cambridge, Mass X, Y, Z.
[2011.98 → 2017.68] And we want to make sure the agent isn't hallucinating when it's filling in those pieces of information
[2017.68 → 2018.96] it needs to use to retrieve.
[2019.36 → 2023.72] Otherwise, you know, if she made up the wrong name or said Cambridge, UK instead of Cambridge,
[2023.82 → 2028.52] Mass, the tool will provide the incorrect response back, but the agent will have no idea.
[2029.06 → 2033.22] And it will keep operating with utmost certainty that it's operating on correct information.
[2033.72 → 2037.50] So, you know, it's just an interesting example of, you know, some of the observability we're
[2037.50 → 2043.64] trying to inject into responsible AI workflows, particularly around things like agents, because
[2043.64 → 2049.14] there are all sorts of new safety concerns that really have to be taken into account to make
[2049.14 → 2051.24] this technology practical and implementable.
[2051.78 → 2056.96] And, you know, that's actually having brought up agents and stuff and that being kind of the
[2056.96 → 2061.22] really hot topic of the moment of, you know, 2025 so far.
[2061.34 → 2066.50] Could you talk a little bit about Granite and agents and how you guys, you know, how you're
[2066.50 → 2070.28] thinking you've gone through one example right there, but if you could expand on that a little
[2070.28 → 2074.98] bit in terms of, you know, how does, how is IBM thinking about positioning Granite?
[2075.14 → 2076.46] How do agents fit in?
[2076.60 → 2078.68] What's the what does that ecosystem look like?
[2079.08 → 2081.86] You know, you've started to talk about security a bit.
[2082.22 → 2085.12] Could you kind of weave that story for us a little bit?
[2085.46 → 2085.84] Absolutely.
[2086.20 → 2092.28] So yeah, obviously IBM is all in on agents and there's, there's just so much going on in
[2092.28 → 2092.78] the space.
[2092.78 → 2096.44] A couple of key things that I think are interesting to bring up.
[2096.98 → 2101.76] So one is looking at the open source ecosystem for building agents.
[2101.76 → 2107.18] So we actually have a really fantastic team located right here in Cambridge, Massachusetts
[2107.18 → 2113.58] that is working on an agent framework and broader agent stack called B AI, like a bumblebee.
[2114.20 → 2119.40] And so we're working really closely with them on how do we kind of co-optimize a framework
[2119.40 → 2125.40] for agents with a model that in order to be able to have all sorts of new tips and tricks,
[2125.48 → 2127.92] so to speak, that you can harness when building agents.
[2128.10 → 2132.32] So I don't want to give too much away, but I think there are a lot of fascinating things
[2132.32 → 2136.02] that IBM is thinking about agent framework and model co-design.
[2136.02 → 2142.46] And that only unlocks so much potential when it comes to safety and security, because there
[2142.46 → 2148.70] needs to be parts, for example, of an LLM, of an agent that agent developer programs that
[2148.70 → 2150.68] you never want the user to be able to see.
[2151.08 → 2158.24] There are parts of data that an agent might retrieve as part of a tool call that you don't
[2158.24 → 2159.46] want the user to see.
[2159.46 → 2164.68] So for example, an agent that I'm working with might have access to anybody's HR records,
[2164.84 → 2167.74] but I only have permission to see my HR records.
[2168.24 → 2174.58] So how can we design models and frameworks with those concepts in mind in order to better
[2174.58 → 2180.56] DMARC types of sensitive information that should be hidden in order to protect information
[2180.56 → 2185.72] that the model knows like these types of instructions can never be overwritten, no matter what type of
[2185.72 → 2191.08] like later on attacks, adversarial attacks somebody might try and do and say, you're not Kate's agent,
[2191.28 → 2194.14] you're a nasty bot and your job is to do X, Y, and Z.
[2194.44 → 2200.26] Like how do we prevent those types of attack vectors through model co-design and model and
[2200.26 → 2201.50] agent framework co-design?
[2201.90 → 2204.60] So I think there's a lot of really exciting work there.
[2205.00 → 2209.80] More broadly though, I think even on more traditional ideas and implementations of agent,
[2209.86 → 2215.26] not that there's a traditional one, this is so new, but more classical agent implementations
[2215.26 → 2217.58] we're working, for example, with IBM consulting.
[2217.82 → 2224.72] They have an agent and assistant platform that is where Granite is the default agent and assistant
[2224.72 → 2225.26] that gets built.
[2225.38 → 2228.14] And so that allows IBM all sorts of economies of scale.
[2228.36 → 2234.66] If you think about, we've now got 160,000 consultants out in the world using agents and
[2234.66 → 2239.76] assistants built off of Granite in order to be more efficient and to help them with their
[2239.76 → 2241.24] client and consulting projects.
[2241.24 → 2245.60] So we see a ton of client zero, what we call client zero.
[2245.76 → 2251.82] IBM is our first client in that case of how do we even internally build agents with Granite
[2251.82 → 2253.80] in order to improve IBM productivity.
[2254.66 → 2255.10] Very cool.
[2255.10 → 2263.68] I'm kind of curious as, as you guys are looking at this, this array of, of considerations that
[2263.68 → 2264.80] you've just been going through.
[2265.40 → 2270.60] And as there is more and more push out into the edge environments, and you've already talked
[2270.60 → 2271.90] a little bit about that earlier.
[2271.90 → 2278.28] As we're starting to wind down, could you talk a little bit about kind of as, as things push
[2278.28 → 2280.94] a bit out of the cloud and out of the data centre.
[2281.18 → 2287.00] And as we have been migrating away from these gigantic models into a lot smaller, hyper
[2287.00 → 2292.30] efficient models, often that have that, that are doing better on performance and stuff.
[2292.30 → 2297.22] And we see so many opportunities out there in a variety of edge environments.
[2297.50 → 2303.32] Could you talk a little bit about kind of where Granite might be going with that or where it is now?
[2304.08 → 2308.66] And, and kind of what the, what the thoughts about Granite at the edge might look like?
[2308.94 → 2309.12] Yeah.
[2309.26 → 2313.46] So I think with Granite at the edge, there are a couple of different aspects.
[2313.46 → 2321.42] One is how can we think about building with models so that we can optimize for smaller
[2321.42 → 2322.44] models in size.
[2322.70 → 2327.96] So when I say building, I mean, building prompts, building applications so that we're not, you
[2327.96 → 2333.26] know, designing prompts, how they're written today, which I like to call it like the YOLO
[2333.26 → 2338.70] method, where I'm going to give 10 pages of instructions all at once and say, go and do
[2338.70 → 2343.42] this and hope to God, you know, the model follows all those instructions and does everything.
[2343.46 → 2348.42] Beautifully, like small models, no matter how much this technology advances, probably aren't
[2348.42 → 2351.52] going to get, you know, perfect scores on that type of approach.
[2351.78 → 2358.48] So how can we think about broader kind of programming frameworks for dividing things up into much
[2358.48 → 2360.86] smaller pieces that a small model can operate on?
[2361.10 → 2367.64] And then how do we leverage model and hardware co-design to run those small pieces really fast?
[2368.36 → 2373.44] So, you know, I think there's a lot of opportunity, you know, across the stack of,
[2373.46 → 2377.24] how people are building with models, the models themselves and the hardware that the model
[2377.24 → 2382.24] is running on, that's going to allow us to push things much further to the edge than
[2382.24 → 2383.54] we've really experienced so far.
[2383.68 → 2386.02] It's going to require a bit of a mind shift again.
[2386.20 → 2390.42] Like right now, I think we're all really happy that we could be a bit lazy when we write our
[2390.42 → 2394.48] prompts and just like, you know, write kind of word vomit prompts down.
[2394.48 → 2401.22] But I think if we can get a little bit more like kind of software engineering mindset in terms of
[2401.22 → 2406.26] how you program and build, it's going to allow us to break things into much smaller components and
[2406.26 → 2408.58] push those components even farther to the edge.
[2409.12 → 2409.64] That makes sense.
[2409.74 → 2410.82] That makes a lot of sense.
[2411.60 → 2418.50] I guess kind of final question for you as we talk about this, kind of any other thought you talked a
[2418.50 → 2420.72] little bit about kind of where you think things are going right there.
[2420.72 → 2426.62] Anything that you have to add to that in terms of kind of industry or specific to granite,
[2426.72 → 2431.68] where you think things are going, what the future looks like when you are kind of winding up for
[2431.68 → 2436.12] the day, and you're at that moment where you're kind of just your mind wanders a little bit,
[2436.24 → 2439.16] anything that appeals to you that kind of goes through your head?
[2439.64 → 2444.90] So I think the thing I've been most obsessed about lately is, you know, we need to get to the
[2444.90 → 2450.38] point as a field where models are measured by like how efficient their efficient frontier is,
[2450.54 → 2455.38] not by like, you know, did they get to 0.01 higher on a metric or benchmark?
[2455.86 → 2460.22] So I think we're starting to see this with like the reasoning with granite, you can turn it on and
[2460.22 → 2464.48] off with the reasoning with Claude, you can pay more, you know, have harder thoughts, you know,
[2464.54 → 2465.66] longer thoughts or shorter thoughts.
[2466.06 → 2468.30] But, you know, I really want to see us get to the point.
[2468.30 → 2471.56] And I think we've got the like the table is set for this.
[2472.00 → 2478.92] We've got the pieces in place to really start to focus in on how can I make my model as efficient
[2478.92 → 2483.76] as possible, but as flexible as possible so I can choose anywhere that I want to be on that
[2483.76 → 2485.50] performance cost curve.
[2486.18 → 2491.86] So if my task isn't, you know, very difficult, I don't want to spend a lot of money on it.
[2492.14 → 2496.56] I'm going to route this in such a way with very little thinking to a small model.
[2496.56 → 2500.32] And I'm going to be able to achieve, you know, acceptable performance.
[2501.00 → 2504.58] And if my task is really high value, you know, I'm going to pay more.
[2505.20 → 2507.30] And I don't need to like think about this.
[2507.30 → 2511.94] It's just going to happen either from the model architecture, from being able to reason or not
[2511.94 → 2517.78] reason from routing that might be happening behind an API endpoint to send my request to a more
[2517.78 → 2520.96] powerful model or to a less powerful but cheaper model.
[2521.24 → 2524.74] I think all of that needs to be, you know, we need to get to the point where no one's having to
[2524.74 → 2526.68] think about this or solve for it and design it.
[2527.10 → 2531.30] And I really want to see I want to see these curves and I want to be able to see us push
[2531.30 → 2536.26] those curves as far to the left as possible, making things more and more efficient versus
[2536.26 → 2538.32] like here's a here's a number on the leaderboard.
[2538.46 → 2543.88] Like I spent another, you know, X gazillion dollars on compute in order to move that number
[2543.88 → 2544.50] up by point.
[2544.58 → 2544.96] Oh, two.
[2545.14 → 2546.38] And, you know, that's science.
[2546.38 → 2548.68] Like I'm ready to move beyond that.
[2549.10 → 2549.46] Fantastic.
[2549.78 → 2551.30] A great conversation.
[2551.60 → 2556.08] Thank you so much, Kate Soul, for joining us on the Practical AI podcast today.
[2556.46 → 2557.58] Really appreciate it.
[2557.66 → 2559.00] A lot of insight there.
[2559.10 → 2560.00] So thanks for coming on.
[2560.06 → 2561.56] Hope we can get you back on sometime.
[2561.88 → 2562.64] Thanks so much, Chris.
[2562.70 → 2564.00] Really appreciate you having me on the show.
[2564.00 → 2572.02] All right.
[2572.34 → 2574.20] That is our show for this week.
[2574.56 → 2580.52] If you haven't checked out our Changelog newsletter, head to changelog.com slash news.
[2580.72 → 2582.98] There you'll find 29 reasons.
[2583.20 → 2586.40] Yes, 29 reasons why you should subscribe.
[2586.96 → 2588.40] I'll tell you reason number 17.
[2588.98 → 2591.76] You might actually start looking forward to Mondays.
[2591.76 → 2594.62] Sounds like somebody's got a case of the Mondays.
[2595.02 → 2599.56] 28 more reasons are waiting for you at changelog.com slash news.
[2599.76 → 2605.48] Thanks again to our partners at fly.io to Break master Cylinder for the beats and to you for listening.
[2605.86 → 2608.54] That is all for now, but we'll talk to you again next time.
