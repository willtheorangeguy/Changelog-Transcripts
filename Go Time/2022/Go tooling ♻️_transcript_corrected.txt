[0.00 → 11.56] Ah, the dog days of summer. Everyone's taking time off, chilling out, maxing, relaxing all cool, maybe shooting some b-ball outside their school.
[12.14 → 17.64] So today we are rebroadcasting a classic episode of Go Time all about tooling.
[18.20 → 24.26] We took you to the future a few episodes ago. Now we're headed back in time to 2019.
[24.26 → 30.34] This was originally episode 90, and it aired almost three years ago to the day.
[30.84 → 35.48] It was a simpler time then. Generics hadn't landed. COVID, nope.
[36.00 → 40.12] Social distancing was only something nerds knew about. This is the way.
[40.50 → 44.86] We didn't even have an unpopular opinions segment back then.
[45.28 → 50.14] So some of this conversation will be quaint considering all that's changed in the world since then.
[50.14 → 54.22] But most of it is still highly relevant. We think you'll enjoy it.
[54.44 → 61.64] And we'll be back with some freshens next week when Natalie and Ian welcome Donna Steinberg to discuss OOP and Go.
[66.72 → 70.40] This episode is brought to you by our friends at Source graph.
[70.48 → 73.10] They recently launched a new feature called Code Insights.
[73.38 → 76.34] Now you can track what really matters to you and your team in your code base.
[76.34 → 81.10] Transform your code into a durable database to create customizable visual dashboards in seconds.
[81.46 → 84.34] Here's how engineering teams are using Code Insights.
[84.66 → 88.56] They can track migrations, adoption, and deprecation across the code base.
[88.80 → 92.02] They can detect and track versions of languages or packages.
[92.46 → 95.34] They can ensure the removal of security vulnerabilities like Log4j.
[96.14 → 102.40] They can understand code by team, track code smells and health, and visualize configurations and services.
[103.00 → 105.58] Here's what the engineering manager at Prezi has to say about this new feature.
[105.58 → 113.52] Quote, as we've grown, so has a need to better track and communicate our progress and our goals across the engineering team and the broader company.
[113.90 → 118.98] With Code Insights, our data and migration tracking is accurate across our entire code base.
[119.28 → 125.90] And our engineers and our managers can shift out of manual spreadsheets and spend more time working on code.
[126.28 → 126.64] End quote.
[126.64 → 130.94] The next step is to see how other teams are using this awesome feature.
[131.28 → 136.06] Head to about.sourcegraph.com slash code dash insights.
[136.32 → 137.80] This link will be in the show notes.
[137.92 → 142.50] Again, about.sourcegraph.com slash code dash insights.
[142.50 → 158.26] Let's do it.
[158.82 → 159.90] It's go time.
[160.50 → 165.70] Welcome to Go Time, your source for diverse discussions from around the Go community.
[165.70 → 169.74] We take requests, just like all the best wedding DJs.
[170.08 → 176.12] Head to gotime.fm slash request to let us know what you want to hear about on the pod.
[176.70 → 182.18] Special thanks to Vastly for ensuring Go Time reaches your ears superfast wherever you listen.
[182.52 → 184.58] Check them out at fastly.com.
[184.96 → 186.20] Okay, here we go.
[191.98 → 194.44] Hello and welcome to Go Time.
[194.44 → 195.18] I'm Matt Ryder.
[195.38 → 198.12] On today's episode, we're talking about tooling.
[198.62 → 202.94] All those great tools that help us be successful, help us do our job.
[203.50 → 205.98] And we use them, Go tools, all the time.
[206.34 → 207.14] Every day.
[207.26 → 210.14] We use them for building, for running code, for testing.
[210.92 → 215.00] We use them for formatting our code, for linting and vetting.
[215.54 → 218.56] And many, many, many more things too.
[218.56 → 227.44] And I think this show will be useful to anybody new to Go that wants to get a sense of the tooling around that we all use.
[228.16 → 234.40] And I'm sure there will also be some golden nuggets for the seasoned gophers also.
[234.98 → 238.94] And I'm so confident because of who's joining me.
[238.94 → 243.64] I'm joined today by, in no particular order, Jana Dozen.
[244.04 → 244.56] Hello, Jana.
[244.86 → 245.18] Hello.
[245.78 → 246.16] Hey.
[246.44 → 248.28] Welcome back to Go Time.
[248.42 → 249.00] How have you been?
[249.94 → 250.94] Yeah, it's been a while.
[251.06 → 252.30] I've been travelling, I guess.
[253.02 → 253.72] Yeah, yeah, yeah.
[253.78 → 254.82] You went to...
[254.82 → 255.46] Where did you go?
[255.46 → 257.56] I was in Marbella, Spain, right?
[257.72 → 264.28] Like, the last time we talked, like, I was just going for, like, a conference, and then I never came back to the show.
[264.34 → 265.10] I'm so sorry.
[266.44 → 267.14] That's all right.
[267.38 → 272.78] I can understand if you're off and travels to exotic places for work.
[273.76 → 274.62] It's a tough life.
[275.72 → 276.44] Such a yeah.
[276.62 → 281.52] And you told me earlier that everything you do at work is completely confidential.
[281.70 → 283.70] Do you want to just break all the rules and tell us anyway?
[283.70 → 288.24] Well, kind of, like, I mean, I'm actually about to switch to a new job.
[288.40 → 291.16] Like, I mean, not a new job, but sort of like a new role.
[291.62 → 296.66] And currently, I'm still exploring what I'm doing, what I'm supposed to do.
[296.86 → 304.84] And it's confidential, not because it's supposed to be super confidential, but I am not sure about, like, what I will be focusing on.
[304.96 → 307.76] So I think I will need, like, a week or something.
[308.22 → 308.92] That's exciting.
[308.92 → 309.84] Just don't get it personal.
[310.12 → 311.06] It's not about you.
[311.06 → 313.46] It's just, you know, I'm still exploring.
[314.20 → 315.10] Yeah, no, absolutely.
[315.44 → 315.90] I do.
[316.02 → 319.16] Obviously, I do take it very personally, but I'll pretend that I don't.
[320.04 → 324.52] Well, also joining us on today's show, it's only Johnny Portico.
[324.84 → 325.38] Hello, Johnny.
[325.98 → 326.52] Hello there.
[327.22 → 330.96] And speaking of new gigs, you've just started yours, haven't you?
[331.34 → 331.78] Yeah, yeah.
[331.78 → 332.28] Recently.
[332.28 → 332.92] Yeah, recently.
[333.06 → 334.60] It's been a couple of weeks.
[334.94 → 336.64] Still onboarding, as they say.
[337.30 → 338.94] But, yeah, still exciting.
[339.14 → 342.12] Still looking forward to contributing and learning.
[342.94 → 346.12] You know, new gigs are always exciting that way, right?
[346.16 → 353.00] There's that honeymoon period where everything is new, and you're learning, and you're learning about systems and people and all that good stuff.
[353.76 → 356.00] And then at some point, I'm sure I'm going to cross that threshold.
[356.14 → 357.78] I'm like, ah, what is going on?
[357.78 → 359.16] I need to start fixing things.
[359.44 → 361.06] But so far, everything is going well.
[362.10 → 362.72] Oh, good.
[362.78 → 363.46] I'm glad to hear it.
[363.70 → 364.62] Yes, it is exciting.
[364.78 → 366.86] It's scary and exciting all at the same time.
[366.96 → 367.48] New jobs.
[368.28 → 368.82] But, yeah.
[368.96 → 369.78] No, I wish you all the best.
[369.86 → 373.94] Well, if you don't mind, we'll keep asking you about it on the show because I'm very interested.
[373.94 → 380.78] I think it's useful for other people as well to hear about things that we get up to in our professional lives.
[380.96 → 383.82] So, if you don't mind, I'll keep bugging you about that.
[383.98 → 384.36] Sure thing.
[386.06 → 386.76] So, yeah.
[387.12 → 388.16] Let's jump straight in.
[388.22 → 390.18] We're going to be talking about Go Tools today.
[390.88 → 398.02] And I asked on Twitter earlier which of the Go Tools are people's favourites or which ones do they like the most.
[398.02 → 400.86] Mine, I'll just kick off.
[401.22 → 407.88] Mine probably has to be Gourmet or Got or Go Format, however you say it.
[409.20 → 414.16] You see, for those that don't know, it formats all the Go code so it looks the same.
[415.00 → 419.26] And all the rules are baked into the tool.
[419.42 → 421.90] So, you don't get to choose tabs versus spaces.
[422.08 → 424.32] You don't get to choose where the braces go.
[424.32 → 430.24] So, you don't really get to choose a great deal about the actual format of your code.
[430.58 → 437.10] Which, again, I think to some people when they're used to having tools that allow them to configure all this,
[437.18 → 439.18] they feel like that's a deficiency in Go.
[439.48 → 442.26] But it turns out to be one of Go's superpowers in my opinion.
[442.68 → 447.98] Because what happens is all Go code starts to look the same and starts to look familiar.
[447.98 → 456.50] And I've done it where I've been to a project and found that the code just looks like I wrote it and I definitely didn't.
[456.96 → 458.92] And I think that's awesome.
[459.02 → 462.96] If you think about pull requests, you know, with white space.
[463.08 → 469.96] Sometimes pull requests and having loads of white space makes it really difficult to really see what the crux of the change is.
[470.62 → 474.56] Well, with Gourmet, we don't have that problem because it's all formatted nicely.
[474.56 → 478.96] Anyone else? How do you feel about Gourmet?
[479.00 → 481.82] How do you pronounce it, by the way? Let's just get that one out of the way.
[483.18 → 483.88] Gourmet, right?
[484.42 → 485.22] Okay, good.
[485.82 → 487.56] I mean, that's what I know.
[488.46 → 490.30] Yeah, that's what I'm told.
[490.78 → 496.84] It's always awkward when I'm teaching or something, and I say the Jump package, for example,
[497.02 → 500.64] which is, you know, people kind of look at me sideways.
[500.78 → 503.14] I'm like, yeah, I know, I know. Just go with it, right?
[503.14 → 508.12] Because if you say instead, if you say FMT or format, God forbid, like, you know,
[508.28 → 509.84] gophers are going to look at you a little weird.
[510.02 → 511.10] Just go with it.
[511.62 → 518.46] Yeah, it takes a while for people to, I think, parse it initially, and then they learn it and like they take it and like they don't question it.
[519.18 → 522.34] So I'm trying to, you know, keep it consistent by saying Go Fund.
[522.94 → 523.50] Yeah, same.
[523.76 → 525.26] I mean, I agree.
[525.26 → 527.46] Like, I wouldn't have done that.
[527.58 → 529.92] I don't think naturally, but I heard about it.
[530.20 → 532.38] And yeah, I do it for consistency too.
[532.38 → 541.44] So it's funny because like sometimes people will say Golang because when we use Google and when we search or when we use hashtags,
[541.68 → 545.38] we tend to write Golang, but we never say Golang.
[545.86 → 550.12] So it's a little pro tip for anyone that's new to the Go community.
[550.12 → 552.94] When you're talking about the language, just call it Go.
[553.24 → 554.12] Don't say Golang.
[555.34 → 556.18] Same with Pump.
[557.04 → 557.34] Yeah.
[558.86 → 564.40] So in regard to the Pump, well, not Pump, but GoPhumpt, I should say.
[565.80 → 570.28] The reason, well, let me step back a little bit.
[570.28 → 583.88] When I first came across Golang, I was taken aback, honestly, because I wasn't used to basically tooling, sort of formatting my code to look like a standardized sort of any sort of way.
[584.06 → 584.16] Right.
[584.20 → 593.36] So, you know, I come from programming languages where everybody has their little pet peeves, little quirks about, you know, I like my braces, you know, to be lined up together.
[593.36 → 604.00] And another person would be like, I like my braces to me to end at the declaration and then for the closing bracket or brace to be at the end or whatever.
[604.16 → 611.90] And so it's like people would have sort of these back and forth around sort of styling, you know, what's more readable versus what's not as readable.
[612.44 → 614.42] And obviously, it was all sort of subjective, right?
[614.44 → 617.46] Everybody has their own preferences, their own quirks and what they're used to and what they're not used to.
[618.06 → 622.70] But Go Fund sort of threw all of that out at the window when I first came across it.
[622.70 → 630.12] And I'll be honest, I mean, for the first month or so, I was like, I don't like everything about what it does.
[630.30 → 634.48] You know, I'm happy with like 90% of it, but I don't like everything about it.
[634.84 → 648.94] But then over as time went on, I really began to love the tool and what it does because the beauty of it, I think you touched on that, is that every basic Go code started looking like I expected it to, right?
[648.94 → 655.22] So basically, that cognitive load, that aspect of looking at code and reviewing code, that just went out the window.
[655.30 → 659.82] I didn't have to worry about, okay, is this person's code going to look differently formatted than this other one?
[660.22 → 669.42] Basically, I could just focus on the actual code and what it was doing as opposed to, you know, sort of trying to figure out parts in my head, okay, this person's quirks are that way and that person's quirks are that way kind of thing.
[669.42 → 670.76] So it was valuable in that way.
[671.46 → 671.68] Yeah.
[671.84 → 678.20] There's actually something from Robert Grimmer that he used to say, he is the person who is maintaining Go Fund and like all the rules and so on.
[678.42 → 681.46] He says that he doesn't agree with like all the styling.
[682.54 → 689.26] You know, I mean, he doesn't necessarily agree with Go Fund, but it's perfect that like somebody, some tool is enforcing it.
[689.26 → 690.52] So there's no question.
[691.52 → 705.20] I mean, I work for a very large company and I witnessed, it took like four years to just tweak one little side guideline change on the Java style guideline.
[705.20 → 715.16] And can you imagine like, you know, there's all these like hundreds of people with like strong opinions about style, just like wasting four years debating on minor style issues.
[715.34 → 721.42] I like the fact that it is like Go Fund, there's like this canonical place and there's no debate.
[721.74 → 726.58] There's like one source of truth type of thing and everybody has to agree with it.
[726.94 → 731.60] Even if, you know, the formatting is not always what you would desire.
[731.60 → 737.22] Yeah. Do you think they would be able to retrospectively fit that into the tool chain?
[737.34 → 742.10] Say that there wasn't Go Fund originally, and it just came out now.
[742.28 → 746.68] Do you think the community and everyone would rally around it in the same way?
[747.04 → 751.26] Or do you think there's something to be said for the fact that this was there from the very beginning?
[751.94 → 759.70] I think it's necessary that like initially you create some like, you know, initial culture around, you know, just relying on a tool.
[759.70 → 767.90] Because I think it creates like enough people, you know, it creates this community with enough people supporting the idea and understanding why it's valuable.
[768.28 → 773.18] If you try to like to inject this type of tools at a later time, the community is already fragmented.
[773.32 → 782.66] And there are a lot of excuses to, you know, prepare a personal style because you already, for example, invested in one particular style all across a company.
[782.66 → 786.78] And like, there's no way to, you know, just kind of like fix things at a later time.
[786.78 → 790.60] So it's perfect that they, you know, came up with a tool initially.
[790.86 → 791.86] At least that's my opinion.
[792.46 → 793.40] Yeah, I agree with you.
[793.48 → 800.88] I mean, there are a few examples where the foresight or the insight from the team in the original design,
[800.88 → 804.58] I think we really benefit from some of those decisions.
[805.16 → 806.86] And we'll talk about more of them as well.
[806.86 → 812.18] I think the fact that another one of the tools, Go Test, that was there as well from the very beginning.
[812.72 → 817.62] So testing as a concept was part of, it was a first class concern in Go.
[818.04 → 824.96] And that was, of course, makes sense because we, at the time it was being designed, you know,
[824.98 → 827.14] that was kind of how we were building software.
[827.26 → 828.92] Now we were writing tests a lot.
[829.02 → 831.90] It was an important part of software engineering.
[831.90 → 839.54] But the fact that they make these decisions, I think, early just sets a precedent.
[840.18 → 844.14] And yeah, from there, I think it pays dividends every day.
[844.60 → 847.30] Yeah, I think Go is doing a good job in terms of like, you know,
[847.40 → 851.72] identifying 80% of what is essential in software engineering.
[851.92 → 855.40] And I think, you know, tooling is kind of also representing those priorities.
[855.40 → 859.60] Yeah, so extensive thinking beyond Go Fund then.
[859.84 → 863.58] If we look at Glint and also Covet,
[864.16 → 868.18] does anyone want to have a stab at describing the difference between those two
[868.18 → 870.24] or describing what they actually do?
[871.74 → 872.08] Cool.
[872.54 → 876.52] Well, yeah, so Glint.
[876.96 → 879.54] Glint is, I like it.
[879.54 → 887.52] It essentially looks at your code and does some static analysis and can catch common mistakes
[887.52 → 889.38] and kind of give you warnings about them.
[890.02 → 896.02] And usually, sometimes they're not mistakes, but they're just best practices.
[896.68 → 902.30] And you can run the Lint tools on your code and see if it's got any recommendations
[902.30 → 903.94] for things that you might change.
[903.94 → 908.68] So one example is, if you have something in a package that's exported,
[908.94 → 913.92] if it starts with a capital letter, then you should have a comment on that, really.
[914.04 → 915.78] That's the sort of accepted practice.
[916.28 → 918.48] Now, the Go spec doesn't say that.
[918.66 → 922.74] So, of course, nothing, you know, it's not a compile error if you don't have a comment there.
[923.08 → 928.10] But Glint tool will catch it and say, you know, for maximum kind of quality,
[928.30 → 931.94] for the best quality, you should consider putting a comment here.
[931.94 → 934.88] And there are a few rules around how we write comments as well,
[934.94 → 938.82] where we repeat the name as the first word in the comment.
[939.18 → 943.84] And so there are a few little things like that are encoded in the Lint, right?
[944.42 → 944.60] Yeah.
[945.12 → 948.24] There's, you know, initial actually, like we need to mention first,
[948.30 → 950.38] I think there's a difference between that and Lint.
[950.74 → 953.66] That is, you know, reporting more of like suspicious stuff.
[953.66 → 963.16] And, you know, like some patterns that might be just, you know, might be just,
[963.76 → 969.38] I mean, a misuse of the of an API that it may actually, you know,
[969.42 → 971.80] just kind of like corrupt some memory or whatever.
[972.30 → 975.30] Like think about like the typical example of print.
[975.70 → 978.88] If, you know, you pass the wrong type of arguments,
[979.00 → 982.20] Beth is going to complain about it.
[982.20 → 986.70] So both Lint is more about like, I think style errors,
[986.96 → 989.72] more of like, if you don't, for example,
[990.08 → 991.80] Godot, a public API,
[992.16 → 995.24] it's going to complain about that type of problem.
[995.96 → 997.84] So that became a part of the test,
[997.96 → 1003.30] but like not, I think all the things that is reported as a part of Beth is genuine.
[1004.24 → 1008.34] So you can like, there could be like false positives as far as I know.
[1008.34 → 1011.84] And it also applies to Lint as well.
[1011.84 → 1015.64] So these are not like a part of the compiler because, you know,
[1016.00 → 1021.96] there's like some reports that is not accurate or something.
[1022.86 → 1026.22] But it's just generally like, you know, you need to follow.
[1026.22 → 1032.08] So they generally generate like genuine enough reports, and they're really useful.
[1032.74 → 1033.18] Yeah, you're right.
[1033.26 → 1037.40] When it catches, if you use like print for wrap,
[1037.44 → 1039.08] if you use one of those f methods,
[1039.08 → 1044.50] and then you don't put the correct number of verbs or whatever the arguments in,
[1044.90 → 1047.26] catching things like that is extremely useful
[1047.26 → 1051.38] because it's quite hard at a glance to just see those kinds of mistakes.
[1052.16 → 1057.36] So yeah, I think people should switch on those tools for their code base,
[1057.42 → 1058.94] at least run them for their code base,
[1059.06 → 1062.00] and see what kinds of things it is actually saying,
[1062.12 → 1064.38] because you might find you agree with them.
[1064.78 → 1066.22] The comment one's a good example.
[1066.52 → 1069.34] I mean, it's quite dogmatic.
[1069.50 → 1072.00] It just says, okay, it's exported, so it needs a comment.
[1072.00 → 1076.38] Now, if that method is something like,
[1076.52 → 1078.90] or if it's a function that says new thing,
[1079.38 → 1082.12] then it's obvious that's making a new thing.
[1082.24 → 1085.48] And your comment's probably going to say, new thing makes a new thing.
[1085.88 → 1088.56] So we have a little bit of redundancy.
[1088.92 → 1093.24] But I think generally speaking, if you do follow the Lint tools,
[1093.52 → 1097.96] then I find that, you know, the code, again, it starts to look more familiar
[1097.96 → 1101.76] and you get all the other benefits of Go Fund.
[1102.00 → 1105.08] One of the things that I typically do,
[1105.24 → 1109.80] which is probably the reason why, for me,
[1110.28 → 1111.68] like off the top of my head,
[1111.74 → 1115.42] sort of differentiating between the linting and the vetting was sort of,
[1115.76 → 1118.62] I was like, hmm, I guess I've never really thought about the difference that much
[1118.62 → 1120.72] because they're part of my tool chain.
[1120.94 → 1127.90] So like on my day-to-day, I use VS Code and Vim as sort of my editors of choice.
[1127.90 → 1131.62] And basically they have the plugins, you know,
[1131.76 → 1134.60] and the extensions sort of built-in as part of my workflows.
[1134.76 → 1138.78] Every time I hit save, right, these tools are running, right?
[1139.12 → 1142.06] And I'm getting different, basically,
[1142.42 → 1146.18] markers at different spots from different tools, right?
[1146.18 → 1149.06] So there's another popular open source project out there,
[1149.26 → 1150.68] I think it's called the GoMetLinter,
[1151.32 → 1153.94] which includes a bunch of those kinds of tools as well.
[1154.02 → 1157.24] You can configure, you can turn some off and others on and whatnot.
[1157.60 → 1159.14] But these tools together,
[1159.22 → 1163.00] they give you sort of set of outputs that you can basically go through
[1163.00 → 1164.98] and figure out, oh, yeah, I missed, you know,
[1164.98 → 1165.96] I used the wrong verb here.
[1166.02 → 1167.60] I'm supposed to use an integer.
[1167.60 → 1169.12] I'm using a string instead, right?
[1169.32 → 1174.44] Things that the linter and vet would sort of find for you
[1174.44 → 1176.16] and if you run them sort of individually.
[1176.70 → 1178.32] But because they're part of my tool chain,
[1178.82 → 1182.18] basically I just look at the view at the bottom of my editor
[1182.18 → 1184.40] and get a list of things that I go and fix.
[1184.54 → 1188.54] So I've sort of almost basically, I don't care, I should say,
[1188.68 → 1193.36] which tools give me what unless I really need to work with a specific tool.
[1193.82 → 1195.42] But I kind of, you know, it's part of my workflow.
[1195.54 → 1196.44] It's just part of my editor.
[1196.44 → 1198.90] Every time I hit save, formatting gets done.
[1199.62 → 1200.72] Go import says this thing.
[1200.88 → 1203.52] Whatever I've referenced in my code that is not imported,
[1203.74 → 1205.02] it brings that in automatically.
[1205.66 → 1206.88] All these things sort of happen.
[1207.20 → 1211.32] The tooling kind of makes it easy to sort of just focus on writing the code
[1211.32 → 1215.08] and not worry so much about having to run individual tools one at a time.
[1215.86 → 1219.30] Yeah, it's a good point that actually making it that part of, you know,
[1219.34 → 1221.26] the editing experience is really useful.
[1221.82 → 1225.44] Like a special vet is reporting a lot of like, you know, useful stuff like,
[1225.44 → 1229.72] okay, this is unreachable or, you know, you're passing the wrong, you know,
[1229.72 → 1235.36] you're passing, for example, unmartial and non-pointer and like stuff like that.
[1235.42 → 1241.40] Like it's so hard sometimes by just when you're typing and when you're just like coding,
[1241.40 → 1245.34] but like tool is really helping you to do the right thing as you are, you know, programming.
[1245.34 → 1248.60] Yeah, and I extend that to running tests as well.
[1248.76 → 1255.68] I tend to write unit tests which run very quickly, and then you can run those every time you save the package.
[1256.12 → 1262.40] Usually, you know, if they start getting too slow, then of course you have to have a different strategy.
[1262.54 → 1269.32] But certainly in the beginning, if it's unit tests that just run very quickly and the build time in Go is still phenomenal.
[1269.32 → 1275.32] We always kind of forget about it until you have to go and build a different code base.
[1275.52 → 1277.38] Then you appreciate it again.
[1278.24 → 1283.08] And Johnny, by the way, yeah, the MetaLint now apparently is called Golang CI-Lint.
[1283.40 → 1288.18] So if you want to install that into VS Code, it's Golang CI-Lint.
[1288.90 → 1291.14] That's the new name of that.
[1291.60 → 1292.48] Yeah, but you're right.
[1292.54 → 1293.42] It's the MetaLint.
[1293.42 → 1298.78] It runs a range of other Linters and kind of gives you that one view of it.
[1299.02 → 1301.32] And they integrate brilliantly into the IDEs as well.
[1301.40 → 1305.08] So that's the other thing, like you say, you can run it on save, but even if you don't,
[1305.18 → 1311.84] you can still usually integrate it into the IDE in some way that just makes it part of your routine.
[1312.26 → 1318.72] Because, you know, anytime you can get that live feedback from the code, that's valuable.
[1318.72 → 1323.96] You know, because usually as you're working, you learn too.
[1324.32 → 1329.50] And that's a great way to learn things as you're writing code and to see a linter saying,
[1329.62 → 1333.34] oh, you know, this is unreachable now or that thing's over there now.
[1334.68 → 1339.70] You know, and if it's tests too, then, oh, these tests are broken over here that you didn't expect.
[1340.46 → 1344.96] And you just get that feedback from the code, which is so useful when you're working.
[1344.96 → 1352.84] And you shouldn't have to wait until basically, you know, if you have CI, continuous integration, you should.
[1353.14 → 1359.68] You shouldn't have to wait until the code reaches, you know, that remote server where all these tools are run for you to get that feedback.
[1359.94 → 1361.94] It's much easier, much faster, right?
[1362.00 → 1365.98] Like you're saying, that feedback loop is much tighter when it's part of your tooling.
[1366.10 → 1369.74] So there are some things you can do locally, right, to make sure your code is funded,
[1369.96 → 1373.46] make sure it's vetted, it's listed, and all that good stuff.
[1373.46 → 1380.22] And then when it goes up for review for PR, you know, Circle, you know, whatever CI2 you're using, Travis, Circle, whatever,
[1380.70 → 1381.66] there are dozens of them.
[1381.80 → 1388.00] So you can sort of, you know, they give it a blessing, and then now people can just focus on what does the code do, right?
[1388.02 → 1392.42] They don't have to tell you, hey, you forgot to, you know, run GoFundMe or something, right?
[1392.48 → 1394.04] You take advantage of these tools locally.
[1394.56 → 1395.46] They're very good tools.
[1395.62 → 1399.90] So I wholeheartedly encourage folks to sort of make them part of your development workflow.
[1399.90 → 1404.18] Yeah, one of the I think, the best parts is like they are really fast also.
[1404.44 → 1407.82] You know, it's a part of the editing experience because they are fast.
[1409.00 → 1417.36] And, you know, it's just, I'm coming from like background where, you know, I use a lot of Java tools.
[1417.36 → 1421.50] And it's, you know, not like it is, I think, smooth the experience.
[1421.72 → 1426.22] We used to have like similar static tools, but it was not as smooth as all these Go tools.
[1426.80 → 1433.20] So nobody is making it optional because it doesn't really, you know, make the editing experience more challenging
[1433.20 → 1435.26] because they are fast, and they are useful.
[1435.26 → 1449.52] This episode is brought to you by Square.
[1449.78 → 1454.98] Millions of businesses depend on Square partners to build custom solutions using Square products and APIs.
[1454.98 → 1461.84] When you become a Square solutions partner, you get to leverage the entire Square platform to build robust e-commerce websites,
[1462.22 → 1465.34] smart payment integrations, and custom solutions for Square sellers.
[1465.84 → 1468.58] You don't just get access to SDKs and APIs.
[1469.04 → 1476.30] You get access to the exact SDKs and the exact APIs that Square uses to build the Square platform and all their applications.
[1476.96 → 1479.04] This is a partnership that helps you grow.
[1479.18 → 1483.48] Square has partner managers to help you develop your strategy, close deals, and gain customers.
[1483.48 → 1490.52] There are literally millions of Square sellers who need custom solutions so they can innovate for their customers and build their businesses.
[1491.10 → 1492.74] You get incentives and profit sharing.
[1493.14 → 1497.52] You can earn a 25% SaaS revenue share, seller referrals, product bounties, and more.
[1497.84 → 1500.00] You get alpha access to APIs and new products.
[1500.12 → 1502.46] You get product, marketing, tech, and sales support.
[1502.68 → 1504.46] And you're also able to get Square certified.
[1504.66 → 1507.64] You can get training on all things Square so you can deliver for Square sellers.
[1508.10 → 1512.32] The next step is to head to changelog.com slash Square and click become a solutions partner.
[1512.32 → 1514.84] Again, changelog.com slash Square.
[1516.98 → 1527.62] We mentioned Go Test.
[1527.82 → 1529.54] That's another tool that we use a lot.
[1530.04 → 1534.58] Anyone that's not used it, if you write test codes in your Go programs,
[1534.58 → 1539.48] and you do that usually by naming the file with underscore test dot go at the end.
[1540.24 → 1541.68] And then you run Go Test.
[1541.76 → 1547.14] It will look through all those test files, and it will actually run all the test code for you.
[1547.20 → 1553.06] And that's really how, you know, you can, if you do TDD, you know that your code is fulfilling its promises.
[1553.24 → 1555.40] It's doing what you said it was going to do.
[1555.40 → 1562.02] There's also another little feature in the test tool, which I think gets overlooked a little bit.
[1562.24 → 1563.90] And it's the race detector.
[1564.96 → 1572.08] So when you're writing concurrent code, it's possible for you to break the rules
[1572.08 → 1576.02] and sort of try and read and write from the same data at the same time.
[1576.02 → 1581.06] And if you try and do something like that, that's illegal and it will crash the program.
[1581.40 → 1588.30] But of course, it's very difficult to see that sometimes when you, if you've written the concurrent code
[1588.30 → 1593.38] and certainly difficult to write tests for it, because sometimes it might just not happen
[1593.38 → 1595.14] just because of the way that things get scheduled.
[1595.14 → 1603.20] But there is a race flag, which you can pass into Go Test, which will, it's a bit slower,
[1603.32 → 1613.14] but it does some additional checks, and you can catch those potential deadlocks early, which is kind of cool.
[1613.60 → 1619.32] Yeah. And the tooling is also a part of, you know, the standard tooling.
[1619.32 → 1625.66] It's not just a test, but it's a perfect addition that like T-SAN, you know, detector is also a part of the tests
[1625.66 → 1631.16] because we all have this workflow of not merging things if the tests are not passing.
[1631.52 → 1637.10] So you would, you know, ideally want to enable the race detector as a part of your CI.
[1638.00 → 1645.16] And it's amazing, but there's like one thing I think we should mention that your tests should cover concrete cases,
[1645.36 → 1648.94] concrete cases so the, you know, detector can detect them.
[1648.94 → 1654.82] If you don't represent those like concrete, you know, situations, the detector won't be able to detect them.
[1654.96 → 1662.06] But it's amazing because it's, it's just like so on point, and it's easy, and it's a part of the standard tools.
[1662.22 → 1668.54] So you don't have to like, you know, figure out like all these additional extra tools or whatever in order to get the benefits.
[1669.34 → 1675.76] Yeah. Now it's worth saying that the race detector will, if it reports that there's a violation,
[1675.76 → 1681.24] then that is a violation, but it doesn't necessarily catch everything. Isn't that true?
[1682.36 → 1682.64] Yeah.
[1682.92 → 1683.08] Yeah.
[1683.60 → 1694.40] Okay. So, but still, I mean, you know, it's still, to be honest, I've, I've never seen a race condition get through after testing it with.
[1694.40 → 1699.36] Because you are actually good in terms of what you care about your tests.
[1699.36 → 1701.10] So you represent all the cases.
[1702.10 → 1710.04] I've seen a lot of times people are just like, you know, not creating those like situations where concurrency is a problem.
[1710.96 → 1713.76] They have this, all these like super micro tests.
[1714.14 → 1716.50] So they don't really, you know, capture it.
[1716.50 → 1720.64] And I think it's really important to tell that like your tests should represent those cases.
[1720.64 → 1722.48] So the race detector can detect them.
[1723.18 → 1725.60] Hmm. Yeah. Okay. That's, that's a perfect point.
[1726.24 → 1732.86] Well, with TDD, you tend to get good coverage, even though I don't, covering by the way,
[1733.02 → 1739.34] code coverage is also another part of the tooling that we just get for free, which is, is awesome.
[1739.34 → 1747.20] But yeah, I, I never try and shoot for a hundred percent code coverage or anything, but naturally it's quite high with TDD.
[1747.42 → 1752.44] And I suppose naturally you'll also cover a lot of those cases that you talked about as well.
[1752.98 → 1754.98] I like Go Run as well.
[1755.32 → 1767.50] Go Run is like a it, you don't tend to have much magic in Go, but Go Run is probably the magic tool because it actually secretly does a build and then executes,
[1767.50 → 1777.86] you know, it does a few steps behind the scenes, but it's great if you're just learning to code, or you just want to write a little script quickly and just execute a program.
[1778.04 → 1785.32] You can use Go Run and you pass in the name of the file or files and, and it just runs it.
[1785.38 → 1788.46] I mean, it builds it to a temporary directory and I think it gets deleted afterwards.
[1788.68 → 1789.54] Well, I'm not sure.
[1789.54 → 1799.70] Um, but yeah, I think that also is, it's such a nice thing to be able to just quickly see results and see feedback from what you're doing.
[1799.90 → 1802.10] And Go Run is another example of that.
[1802.38 → 1802.90] Yeah.
[1802.92 → 1806.90] I think, uh, people use Go Run for their like first Hello World program.
[1807.42 → 1809.76] Um, it sometimes becomes like complicated.
[1809.76 → 1812.96] So then they, you know, have this habit of like using Go Run.
[1812.96 → 1822.06] Uh, Go Run, I think before Go Pad was a little bit more difficult to rely on because it was some sort of like, you know, it was able to work outside of Go Pad.
[1822.46 → 1826.68] So, um, the behaviour of Go Build and Go Run was not quite the same.
[1826.68 → 1834.70] So, you know, it's just kind of like people have been advocating to always rely on Go Build or install rather than Go Run.
[1834.90 → 1840.66] But I think like, it's just really nice for a Hello World or if you have a script type of thing that you just go run.
[1840.66 → 1842.00] Um, it's still useful.
[1842.74 → 1843.10] Right.
[1843.20 → 1851.92] The, the Go Run, I think, yeah, like you were right, um, Matt, when, when you're saying basically it, from my understanding is that this, it does the same thing as, as Go Build.
[1852.06 → 1856.68] It's just the difference being that, okay, once a program is run, it just discards that temporary artifact.
[1857.34 → 1861.18] Um, at least that's, that's, that's the high level of what I think it does.
[1861.52 → 1866.56] Um, one thing is worth mentioning is also you can run it with a, I believe it is run, you can run with a dash race as well.
[1867.04 → 1870.36] Um, that way, you know, if there's any sort of race conditions in the code,
[1870.36 → 1879.44] it'll actually, um, when, if, when the program fails, if it panics, um, then you'll actually get some information around, um, where that sort of race condition occurred as well.
[1880.58 → 1880.98] Hmm.
[1881.56 → 1882.54] I didn't know that.
[1882.94 → 1883.60] That's brilliant.
[1883.60 → 1883.88] Yeah.
[1883.92 → 1893.10] I think race is, race is supported in, um, like test, build, um, run, like general all across the tools.
[1893.50 → 1893.70] Hmm.
[1893.70 → 1893.82] Hmm.
[1894.42 → 1897.18] But you, but it adds overhead, doesn't it?
[1897.20 → 1898.80] And slows down your program and things.
[1898.84 → 1901.18] It's not something you would just always switch on.
[1901.66 → 1902.04] Yeah.
[1902.04 → 1906.88] That's why I think it's useful to just, you know, make it, uh, an optional thing for tests.
[1907.10 → 1912.50] Um, but you know, apart from that, like you don't want to have the race detector always on.
[1913.28 → 1913.68] Yeah.
[1913.68 → 1917.74] I've, I've had mixed results depending on the size of the code base, obviously.
[1917.98 → 1922.76] Um, the but these days I work on a lot of somewhat small, um, code bases.
[1922.90 → 1924.64] I work a lot with my services, that kind of thing.
[1924.70 → 1928.14] So these, these code bases tend to be somewhat small, relatively speaking.
[1928.14 → 1932.72] Um, so I, I, by default, whenever I, my, the default makes command, right.
[1932.80 → 1933.46] For, I use make.
[1933.58 → 1939.42] So when the default, whenever I run make for the default is basically to just run it with the dash race flag, run the test with dash race flag.
[1939.42 → 1947.74] Um, I, I haven't noticed, um, significant slowdown in that, but again, you know, obviously your mileage is going to vary depending on the size of your project and how many pages we got going on.
[1948.16 → 1960.18] There was a benchmark about this and like, um, I think it was kind of like memory usage is again, like five times, you know, larger if you, um, have the like race detector on.
[1960.30 → 1966.64] And I think execution time wise, like, again, like there was like some reports, but it's really dependent on the use case, as you say.
[1966.64 → 1973.52] So it's kind of like adding some overhead, which could be, I think, um, two to 20 X or something.
[1973.52 → 1976.22] If I can, you know, remember the numbers correctly.
[1976.46 → 1983.46] Uh, there's a perfect blog post actually, or an article on the, uh, go lang.org about the race detector.
[1983.76 → 1986.24] And, uh, there must be like some numbers over there.
[1987.46 → 1988.26] Yeah, cool.
[1988.38 → 1988.64] Okay.
[1988.94 → 1996.30] Well, so I was thinking as well about, um, go get, go get, go get another one of the tools, which I think, you know,
[1996.30 → 2000.62] obviously things have changed a lot, especially in the module space.
[2000.96 → 2009.64] Um, but I've got to say when I was first using go to just be able to install packages by saying, go get, and then the package name.
[2009.64 → 2016.46] And then for that package name also to be the import path and to be the URL of where that package lives.
[2017.10 → 2024.96] Um, I found that to be such an elegant thing that it was very easy to, to install things.
[2024.96 → 2030.06] I mean, this is when we had, this is in a go path world where everything just gets put into one place.
[2030.06 → 2034.58] Um, but go get just really made that very, uh, very easy.
[2035.26 → 2039.88] Um, how do you feel about go get versus the new module tools?
[2039.88 → 2043.58] Because they're the, the working with modules is, is a little bit more complicated.
[2044.46 → 2051.70] So, um, I'll, I'll, I'll punt the modules, um, to, uh, to JVD and let her tackle that.
[2051.70 → 2061.88] But I can tell you that for the when using go get, like, especially when I'm teaching, like being able to say, look, like we're gonna, we're gonna import this package before we can actually import this package and use it in our code.
[2062.10 → 2063.36] You know, we need to go get it.
[2063.40 → 2063.58] Right.
[2063.58 → 2067.80] So, you know, I'd literally say, okay, go get, and then basically I'd find the name of the package.
[2067.80 → 2074.20] If we qualify path, basically, you know, with GitHub.com, whatever, um, or whatever the wherever the public repository is.
[2074.70 → 2078.62] Um, and then, you know, and then basically I'd get this blank stare from the students.
[2078.62 → 2080.42] They'd be like, okay, what just happened?
[2080.92 → 2092.02] You know, and then it, I, it dawned on me that, okay, if I literally copied, right, that path, go into the browser and paste it into your URL bar and navigate to that repository.
[2092.76 → 2095.08] Immediately they were like, oh, okay.
[2095.08 → 2098.06] I see, I see what this is, right?
[2098.08 → 2102.32] You are literally pulling this code that lives at this very path, right?
[2102.34 → 2104.76] You're putting on the command line, you are pulling it down.
[2104.76 → 2111.30] Now I can actually see and read that code, you know, in my browser and see what it is I'm actually pulling down, right?
[2111.30 → 2115.52] So the whole thing about, you know, pulling down the package, you know, it goes in your go path.
[2115.72 → 2118.26] None of that stuff makes sense, right, for them.
[2118.32 → 2124.24] But the moment that I can actually go into a browser and put that very path in, it sort of clicked, right?
[2124.24 → 2133.72] They, now they understood the value of Roget, and it didn't quite, you know, it didn't matter really much where it was being put in the go path.
[2133.88 → 2135.96] It's just the fact that they knew how to get it.
[2136.04 → 2140.36] They knew how to go, where to go and see whatever was being pulled was, was almost magical for them.
[2141.72 → 2143.64] Funny because it's no magic.
[2143.64 → 2148.56] And it's almost the fact that it's so obvious, i.e. that's the URL, go and look at it.
[2148.68 → 2149.90] You know what a URL is.
[2150.84 → 2153.36] I think that that's great.
[2153.66 → 2156.92] And that you, the little story you just told then makes total sense.
[2157.00 → 2166.56] I mean, when, when I use, if I use some NPM stuff for a project, I install a few things and I look in that node modules folder.
[2166.72 → 2168.70] There's 16 million folders in there.
[2168.70 → 2174.48] And yeah, and I don't know where they've come from.
[2174.82 → 2176.24] It's kind of hidden.
[2176.58 → 2177.70] It's, it is magic.
[2178.14 → 2194.64] Whereas it's just, you know, that thing of being very simple and clear, even if you sacrifice some features for that, I always think is, has, has such a positive kind of dividend that it keeps paying again and again later.
[2194.64 → 2198.62] I think we need to make an episode on go month.
[2198.96 → 2202.88] But I think go, I agree that like go get is a perfect, you know, initial experience.
[2203.32 → 2214.62] And one thing I like about is if, if you're go getting a main package, it, you know, installs it, puts in your go, go pat being directory.
[2214.62 → 2215.06] Yeah.
[2215.06 → 2218.62] So it's just like a good way to, you know, distribute tools as well.
[2219.08 → 2226.44] Before I think go, I was just publishing binaries and like making sure that like I have the, you know, the right version all across.
[2226.78 → 2232.32] Versioning still is a problem with go get, but like, I, I think it's a it's an okay sacrifice.
[2233.44 → 2233.96] Yeah.
[2233.96 → 2234.40] Okay.
[2235.30 → 2245.10] I'm just going to, what I'm going to do is just keep moving on to different go tools because I've, I've, I'm already learning things about these as well.
[2246.44 → 2252.74] And the other one, the other one with go build, which I love is the fact that we can do cross compilation.
[2253.40 → 2256.96] Now this, this has been around from, I think the beginning.
[2256.96 → 2266.50] Um, essentially for those that don't know, you can choose the, the target architecture, the target machine to build your go code for.
[2266.90 → 2272.66] That's very useful if you're using Docker, because you can do like on a Mac, you can do the build for Docker.
[2272.90 → 2279.24] And then you've got the doc, you've got the binary, the Linux binary, uh, that you can then put into the Docker image.
[2279.54 → 2284.26] Or you can of course put the code into Docker and build it in there, uh, in that environment.
[2284.26 → 2288.74] But do you, how would you, how's your experience with cross compilation so far?
[2289.40 → 2290.42] I think it was magic.
[2290.42 → 2299.36] Like when I first saw, um, you know, they were typing go, oh, it's go, actually it's pronounced goose, um, and windows and go build.
[2299.36 → 2300.84] And like, you get a window binary.
[2301.00 → 2302.08] It was like, whoa.
[2302.38 → 2302.74] Right.
[2302.74 → 2308.00] Like, um, I, it was fascinating, and I usually generate binaries for Linux.
[2308.00 → 2312.72] So it was like, I kept, you know, working on my Mac without any worry or anything.
[2312.72 → 2313.84] It was so awesome.
[2314.26 → 2314.82] Yeah.
[2315.02 → 2315.96] Have you used it, Johnny?
[2316.50 → 2316.94] Absolutely.
[2317.28 → 2321.14] Um, one of my, uh, first, uh, one of my first jobs using go full-time.
[2321.38 → 2328.68] My responsibility was the basically to, to have, uh, sort of multi, multi-platform, um, build process.
[2328.86 → 2332.78] Um, so basically I relied on, on goose and gorge quite a bit.
[2332.78 → 2342.72] Um, and for those of you who don't know what gorgeous is busy, the that's the companion to, to goose, uh, G O A R C H, um, for go architecture.
[2342.72 → 2344.06] Um, yeah.
[2344.06 → 2345.06] Yeah.
[2345.06 → 2352.10] So using goose and gorge were sort of a bread and butter, um, to having that work done and basically being able to push up binaries for all kinds of different platforms.
[2352.10 → 2358.16] And I mean, there are a ton of them that, you know, go support out of the box, um, for ARM processors.
[2358.16 → 2362.54] And, and, and I mean, there's, there's a, there's a, there's a, the combination, a sheer combination you can have.
[2362.78 → 2370.52] Um, I've lost, I've lost track of, of, of, of basically how all the different variations you can push out, but it's, it's really was a godsend.
[2370.52 → 2375.14] I mean, I, there's no way I would have been able to, to sort of get that job done without, without these things being in there.
[2375.76 → 2382.92] Uh, I think it's also awesome that like, I was doing a lot of developments, uh, for ARM and, you know, for a Raspberry Pi, for example.
[2383.32 → 2390.26] Uh, the processor on a, you know, typical Raspberry Pi is just going to be not comparable to my laptop.
[2390.26 → 2394.92] So I would just, you know, build things on my laptop because it's going to be faster.
[2394.92 → 2400.08] And then I will push it to the Raspberry Pi because it's just so much easier to do cross compilation.
[2400.82 → 2404.18] And, uh, it's just like maybe like 10 times faster or something.
[2404.88 → 2405.32] Wow.
[2406.18 → 2408.04] And so how does it actually work?
[2409.08 → 2418.12] Because obviously the compiler is doing a few steps and then ultimately it then creates a binary that's made up of, um, from the machine code.
[2418.12 → 2422.26] And is it just that the machine code is generated differently depending on the architecture?
[2422.92 → 2423.00] Yeah.
[2423.08 → 2426.16] You know, like, I mean, they know what to generate for each architecture.
[2426.56 → 2431.04] So they just basically take the inputs, and they know what to map it.
[2431.14 → 2436.76] And then they generate, uh, the output based on the, you know, um, operating system and architecture.
[2438.14 → 2444.06] And that must've been possible because of the way that they built the tool system.
[2444.06 → 2449.10] Do you think it was deliberate that they wanted to be able to build to any target architecture?
[2449.10 → 2455.98] Or do you feel like they just realized they could after because they'd just built it and designed it in a simple way?
[2456.76 → 2460.70] I don't think you, you stumble on something like this, um, by accident.
[2460.70 → 2473.70] I think I had, I mean, if I had to guess, I'd say this was by design, um, is considering that the, the creators of, of the language busy to head, they had, um, they see they were building for, for Google.
[2473.70 → 2474.00] Right.
[2474.00 → 2485.30] So I imagine that at some point they need to be able to run, um, binaries on different platforms with different CPU architectures and, you know, 32 bits or 64 bits and all that, and all that good stuff.
[2485.40 → 2490.12] So I imagine this must've been sort of a part of the plan, part of the design.
[2490.34 → 2498.96] This, this seems way too complicated and way too powerful a feature to have just come across, um, um, to have fallen out of the build system.
[2498.96 → 2499.96] Hmm.
[2499.96 → 2500.46] Hmm.
[2500.46 → 2505.56] There's also like, we, uh, I think simplified the process, but there's this intermediate assembly.
[2505.56 → 2510.30] So, uh, the compiler first translates everything to that intermediate assembly.
[2510.30 → 2518.16] And from that point on, uh, they are being compiled to the, you know, the architecture specific, um, machine code, uh, instructions.
[2518.16 → 2524.64] So, so, um, it's, it's actually like, you know, the internals of compilers, like this, like two-step things.
[2524.64 → 2529.36] Uh, and this is like a really typical way the compilers work.
[2529.48 → 2533.50] They're just, you know, taking it, converting everything into an intermediate language.
[2534.04 → 2538.96] And then from that intermediate language, you can just basically target whatever architecture you want to target.
[2539.46 → 2539.98] Hmm.
[2540.28 → 2542.66] And of course you can have build tags as well.
[2543.36 → 2546.62] Does anyone want to describe build tags?
[2547.44 → 2547.66] Yeah.
[2547.72 → 2551.38] Build tags are, uh, it's providing conditional completion.
[2551.38 → 2554.66] And you can create different rules.
[2554.66 → 2560.30] For example, you can have constraints to say, only use this file for Linux builds.
[2560.30 → 2566.48] Or you can say, I just want only arm builds to have this file included in the build.
[2566.70 → 2571.04] Uh, you can, there are many different rules provided by the tool chain.
[2571.16 → 2573.70] Uh, go version is one of them.
[2574.08 → 2576.58] Arbitrary custom build tags is one of them.
[2576.58 → 2590.28] So it kind of gives you this like, you know, possibility to switch to different implementations depending on the go version, uh, depending on the, you know, the, uh, operating system or architecture or some custom build tags.
[2590.64 → 2591.08] Yeah.
[2591.12 → 2594.46] I've used those successfully when it comes to testing.
[2594.46 → 2603.98] Sometimes if there are long-running tests or if there are integration tests that require a different dependency to be running or something, I use build tag in our test files.
[2603.98 → 2607.24] And that's quite an easy way to choose a subset of things to run.
[2607.96 → 2611.64] Um, and it's just a special comment that goes at the top of the file, isn't it?
[2612.14 → 2612.44] Yeah.
[2612.44 → 2617.14] It's just like, I think it, it must be on, um, I mean, it's on the top of the file.
[2617.38 → 2620.02] Um, there's a particular place, but that's it.
[2620.08 → 2621.30] Um, and it's really readable.
[2621.30 → 2630.72] I think my only complaint about these rules, uh, about the build constraints is like, it's just really hard to sometimes just, you know, have like multiple rules represented.
[2630.72 → 2632.68] It becomes really hard to parse.
[2632.68 → 2643.60] Like if you want to have like more complex rules, like, Hey, just include this file on Linux, um, you know, Darwin and blah, blah, but not on this particular thing.
[2643.60 → 2652.48] And I think on top of that, like not for this custom build tag, like I think writing those expressing those, uh, complicated, more complex type of constraints is a little bit hard.
[2652.48 → 2654.70] But otherwise I think it's just pretty straightforward.
[2655.06 → 2656.98] And I use build tags all the time.
[2656.98 → 2670.98] This episode is brought to you by our friends at retool.
[2671.14 → 2677.90] Retool helps teams focus on product development and customer value, not building and maintaining internal tools.
[2677.90 → 2687.60] It's a low code platform built specifically for developers, no more UI libraries, no more hacking together data sources, and no more worrying about access controls.
[2688.10 → 2696.00] Start shipping internal apps to move your business forward in minutes with basically zero uptime, reliability, or maintenance burden on your team.
[2696.34 → 2705.38] Some of the best teams out there trust retool, Bred, Coinbase, Plaid, DoorDash, Legal Genius, Amazon, All birds, Peloton, and so many more.
[2705.38 → 2710.44] The developers at these teams trust retool as their platform to build their internal tools.
[2710.64 → 2711.90] And that means you can too.
[2712.10 → 2713.06] It's free to try.
[2713.20 → 2718.98] So head to retool.com slash changelog again, retool.com slash changelog.
[2718.98 → 2740.08] Okay, well, I want to also mention a couple of tools from the community as well.
[2740.08 → 2748.10] Because remember, you know, we are, we are writing, we are using Go tools all the time, but we can write tools as well.
[2748.22 → 2759.12] And some people have contributed, like I think Go Imports was a Brad Fitzpatrick project that was his own kind of idea that he just did on his own.
[2759.12 → 2765.06] And it essentially wraps Go thumped, so you get all the formatting, but it also resolves imports for you.
[2765.74 → 2768.24] And you can do these things too with your own tools.
[2768.86 → 2774.20] And some of the tooling as well doesn't have to be Go tooling running on our machine.
[2774.54 → 2778.36] Matt Holt has a great JSON to Go service.
[2778.36 → 2787.00] If you Google JSON to Go, you basically paste in a JSON blob, and then it generates the Go structures for that JSON blob.
[2787.72 → 2796.16] Extremely useful, especially if you're going to consume an API and you need all the data, and you don't just, you just don't want to sit and type out all the field names.
[2796.36 → 2797.78] So that's a very useful one.
[2797.80 → 2798.80] And that's a hosted website.
[2798.80 → 2800.44] So you can, you can go to that.
[2800.44 → 2808.40] Any other community, are there any other community tools that we like?
[2809.08 → 2826.34] I personally like the Go report card website, which, which, well, I guess it's less of a local tool, but something that can basically evaluate sort of how close to the idioms, right?
[2826.34 → 2831.16] You have the Go community, your, your, your, your code is, is, is, is being kept at.
[2831.40 → 2834.28] I think it might even incorporate some of the tools we've mentioned before.
[2834.38 → 2836.20] They'll enter the vet, the vet, vetting.
[2836.46 → 2840.24] And it includes some other things like a diplomatic complexity analysis.
[2840.24 → 2846.66] And there's a bunch of other nice sort of basic ads in there as well.
[2846.76 → 2851.14] And I sort of based on these things, it gives your repository a grade, right?
[2851.34 → 2853.82] I think on a scale of A3F or something like that.
[2854.28 → 2855.74] So I find that, you know, useful.
[2855.74 → 2863.58] So especially when I'm evaluating a repository, a package, third-party package to, to, to determine whether I'm going to use it or not.
[2864.18 → 2867.32] If it has a score, I will look at that.
[2867.64 → 2872.54] If it's, if it's anything other than A, then I'm going to take a closer look, right?
[2872.54 → 2879.28] I'm going to be a little bit more hesitant with sort of bringing it in because I'm like, okay, well, what, what best practices, what idioms are you not following?
[2879.48 → 2879.58] Right?
[2879.58 → 2880.76] So I'll take a look at that.
[2880.76 → 2890.82] And, you know, sometimes, you know, I may just, you know, sort of see what's happening and maybe replicate locally without having to bring the package if I don't like the score, so to speak.
[2890.82 → 2895.46] So it's kind of a it's, it's a nice, it's sort of a another data point, right?
[2895.46 → 2901.70] So to speak, to help you sort of evaluate the quality, I should say, of a repository.
[2902.02 → 2904.18] But yeah, it's, it's one of the things I like to see as well.
[2904.48 → 2905.68] The same for Godot.
[2906.54 → 2916.58] Godot is a tool you can run locally, but we have also the godoc.org hosted service, which lets us view documentation for any open source project.
[2916.58 → 2920.24] And so, yeah, I think that's, that's also nice.
[2920.38 → 2923.92] It's a nice way to provide that capability because it makes sense.
[2924.00 → 2925.52] You want to share just a link.
[2925.90 → 2934.52] And the nice thing is for Godot, it's just godoc.org slash, I think maybe PKG slash then the import path.
[2934.68 → 2938.00] So again, you're still referring to that import path and we see it.
[2938.00 → 2942.68] I personally use a lot of tools from Dominic Kenneth.
[2942.88 → 2960.14] Like he has this Go Tools repo, static check tool, which, you know, contains a lot of like, you know, style check, a lot of like linting type of like, you know, features that Glint doesn't support.
[2960.14 → 2966.04] And it's, you know, there are some cases, sometimes like there's a controversial style topic.
[2966.38 → 2969.10] It's not possible to, you know, merge it into the official tool.
[2969.22 → 2973.82] So people would just go and like, you know, put it in the Geostatic tool.
[2974.66 → 2980.62] So it's, it's a really useful to, you know, tool to take a look in terms of, I think, static tools like that.
[2980.70 → 2986.28] I just rely on, you know, static check more than Glint.
[2986.28 → 3002.80] Hmm. Yeah. And, uh, Fatih Asian, um, he made a service, um, which I think is called Fixing Me, which is, it's a kind of, it's a it's a GitHub integration as I understand it.
[3002.80 → 3010.90] And it analyzes, it does a bit like the Go report card, but it actually creates, you know, PRs with changes in it.
[3010.90 → 3021.90] So it actually does the fit, it's sort of proactive, like you've got another member on your team that's cares only, you know, like the pedant who just cares about all the style rules and all that.
[3022.40 → 3025.70] And, um, and that's a project I think it's worth checking out.
[3025.76 → 3030.58] It's called, it's, it's Fix Me, it's spelled F-I-X-M-I-E.
[3030.58 → 3033.12] Um, so have a look for that one too.
[3033.24 → 3038.80] It's a similar kind of idea to the Go report card, but tightly and more tightly integrated into GitHub.
[3039.42 → 3044.40] Has anyone here written any of the any kind of tooling, static analysis or otherwise?
[3044.76 → 3048.50] I only wrote some tools to generate some stuff like from an interface.
[3048.50 → 3055.56] Um, well, these are also some static tools, like, uh, one common case is generating implementations of interfaces.
[3055.56 → 3058.30] And there's like a lot of boilerplate, uh, plate.
[3058.46 → 3064.54] So I wrote a tool that kind of like, you know, takes the interface and creates the, you know, the concrete implementation.
[3064.54 → 3069.22] And then you just go and like, you know, feel the implementation, feel the methods.
[3070.04 → 3076.18] Uh, and do, did you use the AST stuff and the parser and things to build?
[3076.18 → 3076.46] Yeah.
[3076.54 → 3079.24] I used, uh, whatever it was in the standard library.
[3079.34 → 3080.36] It was not that hard.
[3080.64 → 3087.92] Uh, it was not that like, I mean, good-looking either, but like it was possible to, you know, get it done in like a hundred lines or something.
[3088.64 → 3089.08] Yeah.
[3089.30 → 3089.56] Yeah.
[3089.66 → 3091.80] So, okay, cool.
[3091.92 → 3096.80] Well, I think we should also spend some time talking about some of the performance tools as well.
[3097.12 → 3099.54] Um, that, that we just get for free.
[3099.54 → 3101.52] There are some great talks on YouTube.
[3101.52 → 3104.32] It's quite a it's quite an interesting subject.
[3104.32 → 3106.98] And it's talked about quite a lot in from different angles.
[3107.66 → 3116.16] Um, but perhaps Yana, you could tell us a little bit about, did I see you do a talk about the performance tools?
[3116.30 → 3122.32] It might be possible because like I worked on, uh, you know, some of the dynamic tools, uh, when I was working on Go.
[3122.32 → 3124.82] So it was part of my full-time job.
[3124.82 → 3129.44] Um, and I generally have been, you know, working in this area for a while.
[3129.86 → 3134.92] So it's possible that you have seen me giving a talk, but I can't remember because I'm giving too many talks nowadays.
[3136.76 → 3138.90] I thought it was all confidential what you work on.
[3139.36 → 3140.10] It's not.
[3140.26 → 3142.32] Uh, so the confidential stuff is different.
[3142.66 → 3143.36] Oh, what's that?
[3143.54 → 3145.24] None of my performance tools.
[3145.24 → 3148.54] It's more about like computing, you know, products.
[3149.02 → 3149.38] Right.
[3150.60 → 3152.58] We'll figure out in a couple of weeks.
[3154.42 → 3155.50] I'm just trying to, yeah.
[3155.54 → 3161.18] I'm just trying to be like a one of those journalists, hard hitting journalists that tries to get out the information that you don't want to say.
[3161.80 → 3164.86] But if they're too polite, you just say, I'm not going to talk about it.
[3164.88 → 3165.90] And I go, oh, okay.
[3166.18 → 3166.46] Bye.
[3166.46 → 3169.44] Well, the problem is I really don't know.
[3169.52 → 3176.24] Like I know generally what I'm going to be working on, but I don't know the specifics, and I'm a really precise person, I think.
[3177.00 → 3177.20] Yes.
[3177.38 → 3184.30] I don't want to like to give any impressions that I'm going to work on something that like I'm not going to, because people will be upset.
[3185.08 → 3185.32] Yeah.
[3185.78 → 3187.40] It's absolutely fair enough.
[3187.40 → 3187.64] Just joking.
[3187.78 → 3188.04] Yes.
[3188.72 → 3194.68] So, but Ada, could you tell us a bit about the some of these tools though and what they're for, for anyone that doesn't know about them?
[3194.68 → 3195.00] Yeah.
[3195.00 → 3198.96] I think generally speaking, I think let's go beyond the performance tools.
[3199.34 → 3203.54] There are a lot of like dynamic tools in Go, and they are a part of the standard tooling.
[3204.12 → 3205.96] Some of them are related to performance.
[3206.18 → 3209.18] Some of them are more related to like debugging type of stuff.
[3210.30 → 3216.64] The typical, you know, let's, we, we can talk about, for example, performance initially.
[3216.64 → 3233.52] And the Go came around when it first came around, it came around with some of the dynamic tools because we went to the SRE team and SRE team is at Google is just really specific about what they want to put in production.
[3233.52 → 3236.84] So they want to have like, you know, enough visibility into things.
[3237.06 → 3240.52] And one of, some of these were related to, you know, performance.
[3240.98 → 3243.60] They want to be able to, you know, get the profiles.
[3243.76 → 3250.76] They want to get like some runtime traces because they specifically want to be able to understand when there is something going wrong.
[3250.76 → 3253.10] Again, like they want to be able to pinpoint to those.
[3253.10 → 3262.40] So PROF support was baked into, you know, Go since the early times because of that requirement, for example.
[3262.88 → 3264.10] It provides you some profiles.
[3264.92 → 3268.08] You can also add your custom profiles, which is a useful topic.
[3268.84 → 3277.34] But, you know, it provides the CPU profile, memory profile, you know, Go routines and thread profile and new tech contention profile.
[3277.34 → 3291.86] And it was really crucial, you know, to have a language mature enough to put in production because that's basically most of the people think that like performance is about development time.
[3291.96 → 3294.02] But it's also important in production time.
[3294.34 → 3301.42] On top of like PROF support, there is like, you know, good benchmarking support baked into Go test.
[3301.42 → 3309.08] So benchmarking is a first class citizen, which is not really, you know, quite the same situation in other languages.
[3309.74 → 3315.74] And I think it kind of creates this culture where you care about, you know, benchmarking stuff, right?
[3315.78 → 3328.24] Like, I don't know what is your opinion on this, but I've seen, you know, lots of different communities and different opinions about benchmarking just because of the, you know, the tooling or, you know, it's really easy to write benchmarks or not.
[3328.28 → 3329.10] What do you think about it?
[3329.10 → 3334.36] Well, I've seen it used perfectly, and I've also seen it used incorrectly.
[3335.10 → 3346.28] I've seen an example where the benchmark, just because of slight issue with the way it was written, it was reporting completely incorrect results.
[3346.74 → 3355.32] So, yes, I think one, but if it's used in the right way, because like, you know, if it's, if you, depends on what you're testing, I suppose.
[3355.32 → 3364.32] If you're going to be testing something, and you're making HTTP requests, for example, there's so much variation anyway in HTTP, you're not really going to be getting any meaningful information.
[3364.32 → 3374.10] But if you're, if you've got two little algorithms, and you want to know which one's better at certain tasks and stuff, then yeah, it's, it's, it's great.
[3374.16 → 3375.44] And I agree with you, Yannick.
[3375.44 → 3386.92] I love the fact that it's baked straight into the language, and you just have to write a function that starts with, you know, funk benchmark name, take in the special variable.
[3386.92 → 3403.44] And as long as you get the for loop inside it in the right place and also think about setup and tear down work and where that's happening, then yeah, it's a great way to really just find out which is better because sometimes it'd be astounding.
[3403.44 → 3416.24] In fact, I think it would make a great talk if someone out there wants to do it or a presentation of like, here's, here's some code, which one's the fastest and have people kind of guess.
[3416.92 → 3421.06] And sometimes I find it, the results to be very surprising.
[3421.06 → 3421.36] Yeah.
[3421.66 → 3422.00] Yeah.
[3422.00 → 3431.98] I think benchmark in general is a discipline that, you know, takes a lot of time to kind of like learn and what are the, you know, the other factors that actually improve, you know, impacts the performance.
[3432.30 → 3447.14] So I agree with you that like, I've seen a lot of like wrong benchmarks and people are like super strong opinion that it's actually an optimization, but it's actually like, like one specific thing that improves the performance, maybe like for one specific case or something.
[3447.14 → 3447.26] Okay.
[3447.62 → 3458.10] And I think you need to have a perfect understanding of the runtime and everything around the language in order to write good benchmarks as well as like interpret the results correctly.
[3458.10 → 3459.78] So it's, it's a really tough game.
[3460.96 → 3461.54] That's true.
[3461.54 → 3473.54] Would you say that if, so when it comes to benchmarking and performance optimization, like I try very, very hard not to sort of jump to that sort of right away.
[3473.54 → 3478.66] I, you know, I'll try to solve a problem first and then, and then try to optimize.
[3478.78 → 3478.92] Right.
[3478.96 → 3483.98] So basically preventing premature optimization and these tools make it because they're part of the centre, centre tool chain.
[3484.06 → 3489.42] They make it very easy to just, you know, start using them like right then and there, especially start, start leveraging right away.
[3489.42 → 3500.24] Um, and there, there, there was a time, maybe we're still in that time when, you know, it seems like there was a new sort of HTTP, like Mixer router coming out every, every couple of weeks.
[3500.24 → 3509.24] And they were all like, Oh, benchmark compared to this, these other things, you know, this one is zero allocation, and it's, you know, 0.05% faster than the other one.
[3509.24 → 3519.12] So it was, I was, I kind of found it silly a little bit, um, because of all that sort of going on and, and I was like, okay, we're kind of missing the point here a little bit.
[3519.36 → 3522.58] Um, but yeah, I mean, it's, it's having that tool.
[3522.80 → 3523.84] I think it's great.
[3523.92 → 3532.14] You know, and like you, I don't think, I don't think I've seen that busy, that kind of capability sort of built-in, you know, part of, part of the language from, from, from the start.
[3532.14 → 3546.94] So the I tend to sort of be very, I'm very careful with that because it's too easy to, to have, to create a culture within an engineering team of, of, okay, before I can even ship this thing, I have to make sure it's like super optimized.
[3547.44 → 3552.00] And, and we're putting kind of the cart before the horse a little bit there.
[3552.26 → 3553.80] It's too easy to do that.
[3553.86 → 3556.34] So I tend to be, I tend to shy away from that stuff.
[3557.02 → 3559.12] Um, you know, I sort of bring it in when I need to.
[3559.34 → 3560.40] I completely agree.
[3560.40 → 3565.66] I think, um, you know, optimizations in development time is kind of like fabricated problems.
[3565.66 → 3570.06] Like, I mean, you realize what needs to be optimized in production, right?
[3570.14 → 3580.48] Like, um, for example, what we do is, um, continuous profiling, which are we keep collecting some profiles from the, you know, the production binaries.
[3581.00 → 3590.38] And we sort of like have an understanding of like, you know, within this project, what are some of the hot calls and what is like some of the, you know, stuff that is in the critical.
[3590.38 → 3594.42] Like, and what critical paths are like more often being cold.
[3594.42 → 3609.16] And like, you know, what happens if I just optimize this functional or like, what is the, you know, actual cost of this particular function in the, you know, the, the, if you think about the whole system and, you know, depending on the usage and whatever.
[3609.16 → 3615.16] So I think it just really makes more sense to start thinking about these cases in production.
[3615.16 → 3623.68] And like, by looking at the data, you just go back to the development environments and like, try to optimize those things and, you know, keep using these tools.
[3624.24 → 3631.20] Uh, one of the nice things about Go profiling, the actual P-Prof is like, it's a really low overhead type of profiling thing.
[3631.20 → 3633.12] And, uh, you can enable it in production.
[3633.12 → 3642.82] So you can, you know, just keep, you know, getting, uh, profiles from production without impacting the critical paths so crazily, but there's an overhead.
[3643.12 → 3644.98] Uh, but you know, there are some strategies.
[3644.98 → 3655.70] If you have multiple replicas of a web server, for example, you can enable production maybe for like, um, one minute or five minutes, uh, on one replica.
[3656.14 → 3665.72] And it's just like, sort of like, you know, depending on how much latency you will, you know, experience, uh, it's sometimes doable and that's what we do it.
[3665.72 → 3674.20] Uh, that's how, you know, what we do and, um, just try to optimize based on the usage and, you know, what is the critical usage and like, what are some of the hot paths?
[3674.20 → 3680.16] Like identifying those hot paths is also very important before jumping into any, you know, optimizations.
[3680.50 → 3680.60] Right.
[3680.70 → 3682.32] Having a problem before you solve it.
[3682.86 → 3683.14] Yeah.
[3683.60 → 3683.86] Yeah.
[3684.20 → 3694.06] So Yana, when you say you do continuous profiling, when, when you deploy services, do you have P-Prof already enabled in there, and you just switch it on or.
[3694.84 → 3695.08] Yeah.
[3695.12 → 3696.06] Think about like this.
[3696.06 → 3701.08] Um, so although, you know, the Power form P-Prof tools, uh, P-Prof is, can be tweakable.
[3701.08 → 3705.52] Like it's dynamically turned, you can turn it on dynamically, and you can turn it off.
[3705.68 → 3714.96] So what we do is basically turn it on for like several minutes, uh, collect the data, just get the data and, you know, just parse it, store it.
[3715.04 → 3717.38] And then we aggregate all that data.
[3717.68 → 3721.14] And we have this like, you know, daily, weekly, whatever reports.
[3721.14 → 3736.78] And you can take a look at like, oh, this service, particularly this handler is often used and all these like particular functions are, you know, it is, uh, accounting for the like most CPU time or memory or whatever.
[3736.78 → 3741.78] And you can just go and like dig and like, you know, optimize those particular places.
[3743.12 → 3753.34] Um, I, I wish that go ahead, like some tools around maybe supporting this type of like more continuous integration, uh, sort of continuous profiling, uh, features.
[3754.06 → 3759.96] Um, you know, it's possible to write a tool kind of aggregates, you know, multiple P-profiles.
[3759.96 → 3773.26] Maybe it could be possible to write like a library that automatically, you know, just turns it once a while reports to some like central service and then, you know, turns it off and so on.
[3773.40 → 3777.34] Um, I think there's like some, some, some, we can do much better in this field.
[3777.34 → 3786.62] It's just kind of like up to the user right now to plan and, you know, design and just, you know, do this type of thing.
[3786.62 → 3787.90] But like, that's basically what we do.
[3787.90 → 3793.96] I, I gave some, I wrote, uh, on this topic, um, for a while.
[3793.96 → 3801.20] And, um, it's just really like some companies are aware of these methodologies and some companies are not.
[3801.20 → 3809.02] And like, it's just, it would be so nice if community was, you know, producing best practices as well as, uh, more tooling around this.
[3809.56 → 3810.54] Well, there we go.
[3810.60 → 3812.10] There's the call gone out.
[3812.24 → 3817.00] Anyone who's looking for a new open source project or something to hack on?
[3817.00 → 3818.32] What a great problem.
[3818.68 → 3833.76] Um, could you build something that samples running Go code and, you know, periodically at some schedule and, uh, and collects the results up, um, would be extremely useful and really fun probably as well.
[3833.76 → 3834.26] Yeah.
[3834.26 → 3835.54] It's like a lot of fun ones.
[3835.54 → 3841.00] Once you start to see like, for example, a large company, you know, aggregate and all the profile and data.
[3841.00 → 3847.82] So you can see like, Oh, the companies, you know, the for example, you can actually improve your bill on your cloud provider.
[3847.82 → 3852.26] Uh, you can say that like a loss of the calls are actually like dependent on this one function.
[3852.26 → 3858.58] Um, and you know if you optimize it, we can actually cut the billing, like by 10% or something, right?
[3858.58 → 3863.18] Like it's actually pretty useful once you start to do this systematically everywhere.
[3863.66 → 3864.22] Hmm.
[3864.22 → 3870.88] Well, I love, I love the message of when wait till you've got something running and then look at optimizing it.
[3870.94 → 3877.50] I think in some cases you can shortcut it, but generally speaking, yeah, that advice is sound.
[3877.50 → 3889.06] And the idea of being able to profile running production systems and to understand them better, I think is, is, um, a great goal to have.
[3889.06 → 3895.94] And what a great use of the, the tools that we, that we have as part of our ecosystem.
[3897.10 → 3899.42] Well, on that bombshell, I mean, I think that's it.
[3899.50 → 3902.82] I think we've, uh, we've reached the end of the hour.
[3902.82 → 3909.16] And so the end of this episode, thank you very much, Johnny and Jana.
[3909.34 → 3909.98] It's been awesome.
[3910.42 → 3911.68] How have you liked it?
[3912.00 → 3918.36] I can talk about this topic for hours and I think, you know, this was awesome, but we should keep, you know, talking about tools, I think.
[3919.30 → 3920.06] Yeah, absolutely.
[3920.20 → 3930.40] Well, there's a lot, there's lots more to discuss and, um, I might even see if we can bring in some people from the community that have, um, built some of the tools that we're using today.
[3930.40 → 3935.66] One, one other little, uh, a bit of info that I think is quite interesting.
[3936.12 → 3944.02] The only actual contribution I personally made to the Go project was to remove something from Glint.
[3944.38 → 3949.26] So one time Glint got a bit easier, uh, to satisfy.
[3949.58 → 3950.32] Thanks to me.
[3950.48 → 3951.18] You're welcome.
[3952.74 → 3953.26] Yay.
[3953.58 → 3954.02] Yeah.
[3954.20 → 3955.80] I, I, I delete code.
[3956.06 → 3956.74] I delete code.
[3956.82 → 3957.98] I mean, I love it.
[3958.34 → 3959.42] Well, yeah, that's it.
[3959.42 → 3960.54] Thank you so much.
[3960.84 → 3963.78] Um, we'll see you next time on Go Time.
[3971.42 → 3974.68] Thanks for listening to this classic episode of Go Time.
[3975.12 → 3976.12] Subscribe now.
[3976.20 → 3980.16] If you're new, head to GoTime.fm for all the ways.
[3980.56 → 3984.80] And long time listeners, do us a solid by sharing the show with your friends.
[3984.80 → 3986.84] That's the best way people find us.
[3987.06 → 3988.62] In fact, I will cut you a deal.
[3988.98 → 3995.14] Email a personal recommendation to three friends and BCC go time at changelog.com.
[3995.26 → 3997.50] I'll send you a free pack of changelog stickers.
[3997.84 → 3999.00] That's a win, win, win.
[3999.16 → 4000.06] With win, win, win.
[4000.30 → 4000.92] We all win.
[4001.00 → 4004.50] Thanks again to our partners at Vastly for having our CDN covered.
[4004.66 → 4006.58] To BMC for these banging beats.
[4006.94 → 4007.90] And to you for listening.
[4008.44 → 4009.20] We appreciate you.
[4009.20 → 4012.48] Next week, we welcome Donna Steinberg to the show.
[4012.80 → 4017.52] She joins Natalie and Ian to discuss object-oriented programming and Go.
[4018.12 → 4021.56] That's what you can look forward to next time on Go Time.
[4021.56 → 4033.84] Game on.
