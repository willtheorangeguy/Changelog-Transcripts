[0.00 → 16.58] let's do if it's go time welcome to go time your source for diverse discussions from all around
[16.58 → 22.68] the go community connect with us on the socials we're on Twitter at go time FM and on mastodon
[22.68 → 28.86] at go time at changelog. Social thank you to our friends at fast go time ships fast globally
[28.86 → 34.48] because quickly is fast globally that's how it works check them out at fastly.com and to fly
[34.48 → 40.90] deploy your app servers and database close to your users no ops required learn more at fly.io
[40.90 → 42.94] okay here we go
[43.52 → 57.78] hello and welcome to go time today we are going to be talking to tech lawyer
[57.78 → 63.62] Louis via who returns to go time to school us once again on the intellectual property concerns
[63.62 → 68.84] of software creation in the crazy days we live in this time around however we're going to be focusing
[68.84 → 74.86] on the implications of large language models code generation and where this leaves us on the
[74.86 → 82.44] question of who owns our code and on that note I would like to introduce you to Louis who is a
[82.44 → 87.72] programmer turned attorney he's been involved in open source since college he's worked at Mozilla
[87.72 → 93.56] where he revised the Mozilla public license Wikimedia Foundation where he briefly led the community
[93.56 → 100.36] team he's been a lawyer for Google Amazon and many small startups, and currently he's the co-founder
[100.36 → 106.74] of tide lift which works to make open source better for everyone by paying maintainers what a concept
[106.74 → 113.80] welcome to the podcast once again lovely to have you I'm glad to be back, and we're happy to have you
[113.80 → 118.02] round two as always our conversation got far too interesting the first time around so we had to do
[118.02 → 123.62] another one well you know, and it's all feels so new it's funny I mean I think we knew this when did
[123.62 → 129.84] we record the last one like October yeah I gave a talk in early November and I was looking at those
[129.84 → 135.52] slides in December I gave a talk on machine learning and IP and open source in November and I looked at
[135.52 → 141.82] the slides in December and to my surprise they were not embarrassing because it felt like it feels like
[141.82 → 149.04] the pace of change right now is so much that like even in a month things can get out of date so I was
[149.04 → 156.72] pleased that those are merely like mildly mistaken now so that's well uh excited to dive even deeper
[156.72 → 160.86] and hear about all the new thoughts that might have come on and the things that stay the same
[160.86 → 166.30] yeah and I'll pass along in our little chit-chat got two people who are never getting out of date
[166.30 → 172.10] never going to get old never going to give you up and never going to give you don't get me started um
[172.10 → 181.78] Chris happy 2023 hello happy new year happy new year how are you I'm doing excellent you know it's a new
[181.78 → 190.80] year we get to make all these resolutions and whatnot hoping to change our lives and yeah no I made some
[190.80 → 196.04] good resolutions for myself I do like small habit changes I don't do resolutions are like
[196.04 → 201.86] too big it's like I'll go to the gym every day it's like no, no work out more like just try and
[201.86 → 207.36] slightly improve things and just do that continuously so yeah leave it open to interpretation go to the
[207.36 → 213.26] gym more I never went to the gym so going once this year it counts yeah it's also good to like if one
[213.26 → 218.90] of your resolutions is to go to the gym start in like February so then the gym is more empty because
[218.90 → 223.14] everybody that started their resolutions in January is like I can't do this anymore and then leaves
[223.14 → 228.24] January kick yeah then you have all the equipment and everything it's good very, very excited to chit
[228.24 → 233.98] chat and hear all the both meta and direct thoughts and feelings you may have I'm excited
[233.98 → 243.14] hi Natalie hi angelica as always we're here again yes yet another conversation that went long
[243.14 → 250.36] yes another conversation how are you great yes celebrating all the new years there's one more
[250.36 → 256.46] new year to start this year right the Hebrew new year already happened the Georgian new year like
[256.46 → 261.42] gregorian yeah that's what I wanted to say thank you the orthodox new year so just the
[261.42 → 266.02] Chinese new year is coming up, and we're good awesome well excited to have this conversation
[266.02 → 272.90] as I mentioned in our intro we're going to be focusing more on kind of ml AI etc but before we
[272.90 → 278.52] dive in there I'm going to be a little bit cheeky and for those who haven't listened to our first round
[278.52 → 284.18] of this part one I'm going to ask you Louie whether you can give us a TLDR and I know that's an ask
[284.18 → 290.54] of generally how do we think about code ownership just to kind of set us up as we go into this deeper
[290.54 → 298.92] dive conversation the TLDR for copyright ownership of code is the same as it is with every piece of
[298.92 → 306.88] music every piece of art every poet piece of poetry if a human writes it down it's copyrighted but of
[306.88 → 311.90] course you see already where we're going with that which is the if a human part and that's where this
[311.90 → 319.26] all gets very complicated fast right because the basics of code you don't have to there's a lot of
[319.26 → 323.90] sort of common mythologies around intellectual property right I need to put all rights reserved
[323.90 → 330.46] I need to put the years there was a big curl the popular get things from the internet program
[330.46 → 337.68] recently did a big commit a couple of days ago removing all the years from the headers of all of it's
[337.68 → 343.80] because somebody finally convinced the author like because he had done a commit saying like oh yeah
[343.80 → 349.00] well we're going to add 2023 and somebody's like you know you don't actually have to do that and he's
[349.00 → 354.48] like really I've been wasting my time all these 20 some years that he's been maintaining curl updating
[354.48 → 361.30] those every year and a few on Twitter and mastodon a few people chimed in saying like no
[361.30 → 367.74] really you don't you don't have to do it and he was like okay great bonk gone but there are these sort
[367.74 → 373.42] of kinds of mythologies built up but like the bottom line is really like if you as a human being exercising
[373.42 → 378.84] some kind of in the U.S. in particular exercising some kind of creativity if you're writing down a phone book
[379.00 → 383.12] you don't get copyright on that and again the exercising creativity part is going to come in
[383.12 → 387.98] then you have ownership of your code the one other thing that's relevant in this context
[387.98 → 395.08] is of course that our employers often can contract that right away from us right so when we sign our
[395.08 → 399.70] employment contracts there's a clause in there that essentially says yeah you're going to write a
[399.70 → 405.66] bunch of copyrightable stuff and we your employers are going to own that so yeah there's some nuance
[405.66 → 410.70] there but like that's the general gist of it is that if you're writing for an employer that employer
[410.70 → 416.40] is going to own that stuff and so then we come to this question of okay well what happens if a machine
[416.40 → 422.16] writes it right but before I want to talk about that I want to tell like my favourite funny story
[422.16 → 428.96] which is very relevant so at Wikipedia there was a one of the big things that the Wikipedia legal team does
[428.96 → 437.66] is it defends people who edit Wikipedia against legal claims so that can be like very dramatic
[437.66 → 444.54] stuff like a politician is suing because they think their biography is slander or libellous, or it can be
[444.54 → 452.78] very silly things like a monkey took a picture took a selfie and somebody uploaded that selfie to Wikipedia
[452.78 → 459.56] and there's this very I mean it ended up being in some ways a sort of sad story but the person who
[459.56 → 464.46] owned the camera who's a nature and wildlife photographer told us that he owned the copyright
[464.46 → 470.84] told Wikipedia that he owned the copyright in the photo and long story short the Wikipedia legal department
[470.84 → 477.74] believed that this takedown request was not quite right wasn't done with the proper formalities and that
[477.74 → 485.28] also his original story was that the animal had taken the selfie and as I said a human and this is
[485.28 → 489.92] where it ties into the machine learning part of things a human has to take the picture and so there
[489.92 → 496.54] was a whole big drawn-out drama threats of litigation over this question of well okay did the monkey take
[496.54 → 503.76] the picture and eventually the U.S. copyright office sort of in just sort of footnote kind of way weighed in
[503.76 → 509.58] it was like we're pretty sure monkeys cannot take if a monkey takes a selfie no copyright right there
[509.58 → 514.64] wasn't a human involved in that loop and that was the sort of abstract thing because it turns out the
[514.64 → 522.08] the category of there is a category on Wikipedia of art created by animals which is fairly small but
[522.08 → 527.54] includes like paintings done by elephants a few other there's some sheep selfies in there if I recall
[527.54 → 533.20] correctly and that gets us to this question though of like okay well when we use machine learning to
[533.20 → 539.32] create code to create as we've all seen over the past few months fascinating works of
[539.32 → 547.18] imagery is that more like the monkey what happens to the humans who are in that loop to the computers
[547.18 → 552.64] who are in that loop to the data that's in that loop, and it suddenly gets it gets very complicated
[552.64 → 558.22] very fast and I think in part of the challenge is that honestly attorneys can understand that the
[558.22 → 563.26] monkey stole the camera and point of the say as soon as you start talking to them about like well
[563.26 → 569.76] here's how we trained the model like eyes start to glaze over, and it gets very complicated fast
[569.76 → 575.30] so I don't know is that where we start today do we want to talk about like how much are you assuming
[575.30 → 580.82] that you're it feels like every technologist has wanted to dig into machine learning I don't know
[580.82 → 586.10] how much of you three have had time to do that not as much as i I want to I guess I have generally
[586.10 → 593.86] been not like anti-ai person but I've always just been like it's just fancy statistics so it's like
[593.86 → 598.22] one of those on my long list of things to learn like I have stats and I'm like well should just
[598.22 → 605.52] learn stats before I learn fancy stats so I know enough that I can like generally describe what the
[605.52 → 609.48] things are doing but not enough to like go implement something or like read some code that's doing it like
[609.48 → 614.22] I'm like I don't know what any of that says but like the concepts I'm like okay i grog these concepts i
[614.22 → 619.56] understand these concepts and kind of along those lines in the interest of kind of setting up everyone
[619.56 → 625.70] to kind of have the same baseline understanding when we're talking about like AI machine learning
[625.70 → 632.82] at the basic concept level what are we talking about here I have the answer from ChatGPT for this I'm
[632.82 → 641.00] ready so it's an AI is a field of computer science that involves creating intelligent machines that can
[641.00 → 648.18] perform tasks that require human intelligence and if you ask what is ml that is a subset or part of AI
[648.18 → 652.88] where machines do things not because you program them to do that but because they have enough data
[652.88 → 661.48] to take a decision to do something okay one mentions a level of curation and one mentions data so in fact
[661.48 → 667.40] should we be talking about these as very separate in the legal field maybe this is all even Chris
[667.40 → 673.76] like AI as you described it there had a level of it began I can't remember the exact sentence maybe
[673.76 → 681.84] Nathalie can with like a has implemented this from an individual and machine learning
[681.84 → 687.54] references giving it data, and it does its thing which maybe is less human involvement
[687.54 → 695.52] I looked this up the other day I find that definition of AI and ml interesting because the like hot minute
[695.52 → 699.40] of research I did on AI and ml because I was like what is the difference between these two things
[699.40 → 704.44] and the answer i kind of came back with is like AI is as you said this general type of like we want
[704.44 → 712.84] computers to be intelligent and ml is a way of making computers intelligent right ml implements the AI
[712.84 → 719.06] interface for us nerds who write code so that's the general way that I've come to see and think about
[719.06 → 722.82] it so these are like two things that you kind of have to like talk about more or less together
[722.82 → 725.50] because like AI it's like a little bit too abstract if you like
[725.52 → 731.90] you don't have anything else like behind it really AI is just a very general one so in addition to
[731.90 → 739.70] ml is part of AI but also things like computer vision is equivalent to ml and is under AI
[739.70 → 745.18] yeah well I mean as somebody said I was trying to explain that my sister has a master's in
[745.18 → 752.14] now I think about it, I don't know if it's in AI or ml but our father who is not in computers at all
[752.14 → 755.60] ask like well what's the difference between all these and what's the difference between those
[755.60 → 760.42] things and an algorithm and what we told him was that an algorithm is something that's actually
[760.42 → 766.34] implemented and a ml is something that hasn't yet actually been implemented this was a few years ago
[766.34 → 771.88] and now of course that feels like it's changed a little bit I mean Chris this gets to your point
[771.88 → 778.32] about like it's all just fancy stats right I feel like in some ways machine learning when we use that
[778.32 → 786.66] is the variation of this that is really fancy stats versus like we programmed the thing to learn from
[786.66 → 791.64] its environment or something right i kind of feel like it's similar to like if you ask
[791.64 → 796.84] of what's the difference between a CPU and a GPU it's like basically like the type of math they're
[796.84 → 801.34] doing like they're both just adding numbers, but they just add numbers in like slightly different
[801.34 → 805.40] ways and I feel like that's what like all of this stuff is it's like what's the difference between
[805.40 → 810.60] like traditional statistics or like Bayesian statistics and AI, and it's like okay well it's
[810.60 → 817.12] like different flavours of those same underlying things right well and this is where it's actually been
[817.12 → 822.82] very interesting but also frustrating to talk about this with attorneys right because attorneys
[822.82 → 828.72] would really as a general matter like to come in when things are a little better defined
[828.72 → 837.32] and when the programmers are still like sort of quibbling about definitions and struggling
[837.32 → 843.30] with definitions that make our job as attorneys much more difficult both because we lack often lack
[843.30 → 849.96] the technical chops and even if we do have the technical abilities trying to get precise about
[849.96 → 856.68] this in language is a large part of what we do and so if you all can't get precise about the language
[856.68 → 863.76] then we are we're up the creek right we're in trouble so I find it helpful and I think probably
[863.76 → 871.84] helpful for somebody to make a distinction into sort of three phases right, so the first one is
[871.84 → 879.78] data gathering and training right so we're getting a lot of data from usually from the internet it could be
[879.78 → 884.80] from you know there are a lot of these things for medical fields now, but you're getting a lot of
[884.80 → 891.58] data and Chris again to your point you were learning the statistical patterns in that data and that to me
[891.58 → 898.58] is where the learning part comes in is that you are setting some software to analyze find learn the patterns
[898.58 → 905.12] in that data so you know that's often called training right or learning would be a similarly appropriate
[905.12 → 911.16] term I think so what's the output of that training the output of that training is the statistical model
[911.16 → 919.14] right it is literally the pile of numbers that constitute our statistical knowledge about
[919.14 → 926.62] these things right it's an n-dimensional graph of weights and blanking on the other term right now but
[926.62 → 932.86] but at the end of the day it is numbers and which by the way maybe we'll get into it later maybe not
[932.86 → 938.68] copyright law tends to struggle with numbers right we tend to sort of assume that numbers are not creative
[938.68 → 945.30] not protectable they don't look like the things our intuitions as attorneys and as the people who wrote
[945.30 → 949.52] the statute and as the people have been arguing about this for 100 years right because we've been arguing
[949.52 → 954.90] about copyright in legal systems and like modern legal systems for depending on how you want to count
[954.90 → 963.66] 300 150 years pretty much all that was about poetry books biography music, so there's not much like we often
[963.66 → 969.32] argue about these things by analogy and as you can guess and as I think maybe we talked about in the last episode
[969.32 → 974.96] the analogies are bearable they're not very useful and in part in this area one of the things
[974.96 → 979.28] that's not useful is that what you've actually got is this pile of numbers right so you've got the
[979.28 → 985.92] training you've got data, and you've got and training is by the way an active thing right, and then you've
[985.92 → 993.38] got the model the output of the training then you use that model to create outputs and so each of those
[993.38 → 999.12] three are sort of different from an intellectual property perspective right so you can't really say
[999.12 → 1004.16] a lot of people have said this on the internet, but it grates every time I see it something like
[1004.16 → 1010.42] machine learning is fair use or machine learning is a copyright violation right like that's a category
[1010.42 → 1016.64] error you can't say machine learning as a whole is a copyright problem you have to say the training is
[1016.64 → 1022.46] a copyright problem or the model is a copyright problem or the outputs are a copyright problem because
[1022.46 → 1029.06] each of those are potentially very different so let's try to go through them real quick right so
[1029.06 → 1034.40] training what kind of intellectual property rights are involved you're taking a bunch of stuff which
[1034.40 → 1039.80] remember since when a human writes it down it's copyrighted all that stuff that you're taking pretty much
[1039.80 → 1044.92] by definition there's going to be some exceptions but pretty much by definition all that is going to be
[1044.92 → 1051.06] copyrighted right so you've got this big pile of copyrighted stuff, and now you're trying to extract patterns
[1051.06 → 1056.94] from it well okay what do we have to do to extract patterns step one literally we copy it from one
[1056.94 → 1063.24] you know from a hard drive into ram, so there's literal again a copy right is literally the right
[1063.24 → 1070.50] to prevent somebody else from copying so you've got one copy there going from, and now you've got another
[1070.50 → 1076.90] copy into like your arrays that you're then doing all the magic GPU stuff right as you said Chris it's
[1076.90 → 1084.20] just edition lots of it and that's another set of copies, and then you're creating this model that
[1084.20 → 1091.42] is numbers sort of right, but the numbers represent some patterns that we learn from this other thing
[1091.42 → 1098.58] right okay so one thing that may or may not be true right or a question that we can ask that first step
[1098.58 → 1104.78] of copying where we're doing the training is that a copyright violation so that's one question we can ask
[1104.78 → 1110.54] then the model, so the model contains all these numbers, but the numbers represent strings or
[1110.54 → 1119.30] patterns in imagery do those represent a copy right or are they some sort of abstract thing because if
[1119.30 → 1125.70] it's a copy then there's a copyright infringed but if it's sort of like very abstract it's not really
[1125.70 → 1132.04] related to the thing okay well then probably not, but that's an intelligible question we can ask
[1132.04 → 1137.94] and then finally we can look at the creation of the output, and we can say like oh well it turns out
[1137.94 → 1143.50] that the way we created this output actually everything's like just so weird and out there
[1143.50 → 1150.60] that it's not a problem or like maybe we've trained a model that actually repeats itself an awful lot
[1150.60 → 1155.40] and you know contains things that look an awful lot like some other copyrighted thing
[1155.40 → 1161.80] right so we can ask at each of those stages has there been some there's also by the way
[1161.80 → 1166.50] patents we can talk about those a little bit separately but so that's what we have to ask at
[1166.50 → 1172.12] each of those stages right and who does this of course may be separate right like if I am using
[1172.12 → 1180.06] copilot I'm not doing training so I'm not infringing by training you know Microsoft did that or open AI
[1180.06 → 1186.70] or however there but if I'm outputting code there's still that question about the output right like it may
[1186.70 → 1193.10] be that the first stage is fine, and the output stage is not I just went through a lot there so let me pause
[1193.10 → 1199.54] and like hopefully it's fairly clear but like I'd love any questions or thoughts or anything from slack
[1199.54 → 1204.36] I have like a meta thought because you brought up the whole like we can't copyright numbers thing which
[1204.36 → 1208.68] always like reminds me of that I don't know if it's famous but the whole intel thing of like
[1208.68 → 1213.18] the reason they renamed their line of processors to like Pentium starting with the fifth generation
[1213.18 → 1218.88] so they went to the courts, and they were like we would like to copyright like 586 and the courts
[1218.88 → 1224.38] were like no you can't copyright a number, or maybe it was with the 486 and then someone tried to knock
[1224.38 → 1229.28] it off, and then they were like you can't copyright a number sorry like you can't or trademark it you
[1229.28 → 1233.64] can't do things with these numbers so you just hit on the thing this is one of these things where it's
[1233.64 → 1239.22] all complicated right and where, so actually the question there is trademark right, so trademark is when
[1239.22 → 1245.16] you're using some set of numbers or colours or even there are a few cases now about trademarking smells
[1245.16 → 1252.86] in commerce right you're using it to identify a brand so like you know red shoe soles is a thing
[1252.86 → 1257.16] I'm blank I really want to say a little bit of time, but that's not if it's uh I think it is Louis baton
[1257.16 → 1262.84] yeah maybe it's a ton, but that's a trademark right that is used to identify your product to the public
[1262.84 → 1270.80] and so exactly that Chris I think it was 386s or 486s where a court didn't say that it was impossible
[1270.80 → 1277.94] to trademark a number but like there's a higher trademark the more creative they are the less
[1277.94 → 1284.10] skeptical courts are is the short and simple version of it right and a number obviously not very creative
[1284.10 → 1290.90] very it's like literally a part number, and you know where's Pentium much more creative and in that
[1290.90 → 1295.58] sort of weird sense of it's one word this is why you get all these weird startups that don't call
[1295.58 → 1300.44] themselves a name that has anything to do with the thing they're doing right partially because it's
[1300.44 → 1305.42] more memorable but partially because the less it sounds like the thing the easier it is to trademark
[1305.42 → 1311.48] but that is a separate body of law like trademark is the one body of intellectual property law that's
[1311.48 → 1317.42] very pro the humans at the end of the process because the whole thing is that trademarks are supposed to
[1317.42 → 1323.34] not confuse you right so in fact it's companies that bear a lot of the burden there sort of the
[1323.34 → 1328.90] other way around with copyright right where it's supposed to prohibit you from ripping the company off
[1328.90 → 1334.52] but yeah there are layers here that are and again I mostly haven't touched on patents I assume that all
[1334.52 → 1341.84] these AI companies are patenting things out the Yazoo, but patents apply to processes usually not to
[1341.84 → 1347.32] particular things right so you could patent I'm simplifying a little bit here there's some
[1347.32 → 1355.16] exceptions, but you can patent how you do training right so like if you created a new way to train a
[1355.16 → 1361.22] model more efficiently more effectively then you can patent that and if you figured out a new
[1361.22 → 1368.28] way to do outputs from a model the process of creating those outputs you could patent but actually
[1368.28 → 1376.00] patenting the model itself with some sort of edge cases probably not patentable right which gets to
[1376.00 → 1379.80] one of the recurring themes that we're going to have here and this gets back to Chris what you were
[1379.80 → 1385.94] saying about numbers little unclear that the model actually is protectable by anything in modern
[1385.94 → 1392.64] intellectual property law like there's actually sort of an open question whether that
[1392.64 → 1398.14] thing is something that that copyright law can fit into one of its boxes because that's the thing
[1398.14 → 1404.42] intellectual property law generally has boxes of things right like patents are for processes that
[1404.42 → 1409.52] we invented well that's a little bit of a simplification but for our purposes that'll do
[1409.52 → 1416.60] copyright is creative works that you created trademark is brands that you're using to sell a thing if it
[1416.60 → 1421.98] doesn't fit into one of those boxes and this has actually been a problem with databases right so like
[1421.98 → 1426.40] databases I mentioned phone books I think maybe I mentioned this in the last episode too
[1426.40 → 1431.62] under U.S. copyright law you can't copyright a phone book because the supreme court said there's no
[1431.62 → 1437.16] creativity there right the only creativity was you wanted to find the phone number of every person in
[1437.16 → 1444.96] town now if you said the hundred most popular debutantes in town right like which is actually a
[1444.96 → 1451.76] was a thing in New York in the late 1800s like that list because it involved creativity and judgment
[1451.76 → 1458.42] that list you could get a copyright on now if somebody else has a list that's like my 100 and
[1458.42 → 1463.90] it's 95 of them are the same it's going to be hard to protect but at least in theory you could protect
[1463.90 → 1471.12] that thing right and so databases the European Union has a whole separate set of laws just for
[1471.12 → 1478.76] databases that they call the database right and so in theory databases are in practice turns out to
[1478.76 → 1483.96] have been not all that useful, but they invented 20 years ago 25 years ago they were like you know
[1483.96 → 1490.34] what we need to encourage more databases so we're going to create a database right so there it
[1490.34 → 1496.04] is in EU law turns out to be mostly unused though we'll see if with machine learning maybe some people
[1496.04 → 1499.34] will say that the models are databases I think that's going to be a little bit of a hard trick to
[1499.34 → 1505.34] pull off but I'd be shocked if somebody doesn't at least try to protect models under European
[1505.34 → 1511.92] database rights which by the way quick I think I touched on this last time around but copyright law
[1511.92 → 1516.92] global platform and this is one of these where the analogies to programming actually works really well
[1516.92 → 1522.54] essentially every country on earth has signed what's called the burn convention which makes the
[1522.54 → 1527.58] basic concepts of copyright are more or less the same globally a lot of implementation details as with
[1527.58 → 1533.24] any time you're creating an instance you're implementing an API the implementation details matter
[1533.24 → 1539.34] but at the high level copyright is the same globally the U.S. has no equivalent of the EU database law
[1539.34 → 1546.60] the EU is regulating a lot right now on privacy which bears on training right like what if you have
[1546.60 → 1551.78] private information in the model U.S. federal law says nothing about that copyright law says nothing
[1551.78 → 1556.46] about that the European Union has very strong opinions on what happens if you accidentally encode private
[1556.46 → 1562.22] information especially say like medical information in a model, so there's a whole other field of law
[1562.22 → 1567.62] like I think one of the cool things about machine learning law but the very frustrating thing for
[1567.62 → 1573.34] programmers asking us about opinions because programs just want to know like is this stuff legal can I use
[1573.34 → 1581.04] it and the answer is it depends because like copyright patent trademark privacy law database rights
[1581.04 → 1587.04] all these things are like you know step one is like I don't know are you in the EU or are you in japan
[1587.04 → 1592.18] or are you in the U.S. because the answer might be different in all those places so yeah we talked a
[1592.18 → 1598.30] little bit about this sort of big buckets of things right one thing that I put in the show notes and that
[1598.30 → 1603.84] we just talked a little bit about like what analogies do we use and so maybe it would be helpful I don't know
[1603.84 → 1608.42] but where you all want to go to talk about some of the analogies the courts have used for this kind of
[1608.42 → 1615.12] stuff in the past love a good analogy so I talked about monkeys so like one serious analogy that you
[1615.12 → 1622.34] could make here right is that once it's in a model there's no human involved and so if you just press
[1622.34 → 1629.62] the button and say like please spit me out some code there's no human copyright in that code that's
[1629.62 → 1636.72] emitted by copilot and so you can use it however you please right like that's the most naive
[1636.72 → 1642.72] like you hired a monkey to write some code for you, and so we know monkeys can't copyright a selfie
[1642.72 → 1650.80] and so this is just like that monkey right it's definitely 100 free of copyright that's an analogy
[1650.80 → 1656.26] that would be nice and simplifying I don't think it completely works, but it's a good starting point
[1656.26 → 1662.48] it's a lot closer I think than you know the flip side of that is I hired a human to write code for me
[1662.48 → 1667.66] so if I hire a human to write code for me there's definitely copyright right I definitely have to
[1667.66 → 1674.10] have a provision in my contract so like if copilot were just going to like an ultra-fast typist at
[1674.10 → 1680.64] Microsoft headquarters that typist you'd have to have an arrangement with that typist right like I had an
[1680.64 → 1687.98] old boss who broke both of his wrists in a snowboarding accident, and so he like literally hired a MIT
[1687.98 → 1693.50] undergrad to be his code typist for like a month because he couldn't type and accessibility features
[1693.50 → 1699.02] especially on Linux in the early 2000s were not there so he had to have a contract with that person
[1699.02 → 1705.78] right that said like anything you output is definitely copyright our startup you don't own anything in it
[1705.78 → 1710.68] if you had a monkey in the same situation you would not have to have a contract you obviously can't sign
[1710.68 → 1715.60] a contract with monkey which is like a good hint similarly you can't sign a contract with copilot
[1715.60 → 1722.16] so like that's one analogy we could look at for the whole system I mean have there been arguments I'm
[1722.16 → 1728.04] sure this is a very obvious argument but kind of just want to ask it as the silly question like copilot
[1728.04 → 1735.02] wouldn't exist without a physical human being having been hired by Microsoft to work on that feature
[1735.02 → 1743.42] and to input and ensure that the output is xyz this is like correct so I guess like you've got the
[1743.42 → 1748.10] three parts that you mentioned you've got obviously training model outputs we've established training
[1748.10 → 1754.52] is you need somebody to train it and ensure the output is accurate but I feel like going off the
[1754.52 → 1760.96] kind of monkey analogy like that monkey did something that had they not done it you would not have the end
[1760.96 → 1768.28] product therefore in the kind of maybe copilot analogy had that initial engineer not trained effectively
[1768.28 → 1772.72] you would not therefore have that and so could you trace it back
[1772.72 → 1774.62] could an argument be made legally
[1774.62 → 1781.74] that there you can trace that code back to a person who wrote it slash also to Microsoft if contractually
[1781.74 → 1787.88] their code is owned by Microsoft or is it truly legally in these three buckets
[1787.88 → 1794.64] I mean yeah so that's one thing is all of this is TBD okay I mean there's like a little bit of
[1794.64 → 1800.56] since we last talked there is now a court case about copilot okay I don't want to talk about it too much
[1800.56 → 1805.80] because it's a little weird in a few ways I don't want to overfocus on it, but the thing is that
[1805.80 → 1811.12] this is where it's really important to make sure we've as you called out correctly Angela
[1811.12 → 1817.36] that there are three different things going on here right there's the training there's the model and there's the output
[1817.36 → 1825.96] so those human employees at Microsoft who did that setup and that initial design of copilot that initial
[1825.96 → 1831.78] training of copilot there are probably some rights or at least arguably and this is where we get into
[1831.78 → 1837.64] the question of well it's just a pile of numbers like in the model itself right like if I printed out
[1837.64 → 1843.52] the model onto sheets of paper and then like photocopy them and start handing them out Microsoft having
[1843.52 → 1850.16] done that creative work to create that model they will probably feel entitled and probably correctly
[1850.16 → 1856.08] I mean though it's a complicated thing to come after me for printing out the model and activating
[1856.08 → 1864.34] the model is arguably a lot more like I mean they put a lot of work into creating ms dos right or what
[1864.34 → 1869.78] Windows 12 is that where we're at now I've been a Linux and Mac user too long now you know they put a lot
[1869.78 → 1875.00] of work into that, but they don't run around claiming like ah well the operating system helped
[1875.00 → 1882.54] you invoke VS Code therefore we have some copyright in the thing right like there's sort of a natural
[1882.54 → 1888.20] barrier there between the creation of the tool and the use of the tool I feel like a good analogy here
[1888.20 → 1893.54] too would be to like a compiler where it's like yeah someone wrote the compiler but like you input your
[1893.54 → 1899.62] source code you get out an artifact that represents that, and it's like the input that went into it is the
[1899.62 → 1904.80] thing that's copyrightable and just because people wrote the compiler doesn't give them any permission
[1904.80 → 1910.58] or copyrights around that but also doesn't give them like permission for the input of it right so
[1910.58 → 1916.52] they can't say oh well because you ran that copyright material through my compiler now I have the ability
[1916.52 → 1922.20] to grant that copyright to you, and it's like that's not how that works so some corrections because some
[1922.20 → 1927.08] things were not correctly said it's a good time for me to remind that I am an open AI developer
[1927.08 → 1935.78] ambassador so i I like to focus on my small little details here Microsoft is the owner of GitHub
[1935.78 → 1944.66] GitHub is using the API of the model that was created by open AI that is called codex that is the
[1944.66 → 1950.72] underlying engine for copilot so actually when you go to VS Code, and you type something, and you have the
[1950.72 → 1958.36] plugin on for copilot what actually happens is that there is a line of code from GitHub which belongs
[1958.36 → 1963.82] to Microsoft I don't know the separation of the entities you know definitely better so they have
[1963.82 → 1971.38] the API that they're using that part of the API that they're using is it has something for me that i
[1971.38 → 1976.00] wrote right in VS Code it has a part that they added which is called the prompt which is something along
[1976.00 → 1980.58] the lines of this is what she wrote so far what do you think she wants to do can you complete so this
[1980.58 → 1987.80] is their own personal just GitHub not open AI not Microsoft and then this is pinging the endpoint
[1987.80 → 1996.50] of codex that is an engine that belongs to open AI, but it runs on the Microsoft Azure cloud, so there's
[1996.50 → 2000.84] actually all sorts of steps in between to make it even more complicated, but it's not a Microsoft thing
[2000.84 → 2006.78] and the hot rumour is that Microsoft is buying 49 percent of open AI like sometime this week
[2006.78 → 2011.82] either yes or no but open AI is actually capped profit so they have an interesting structure that
[2011.82 → 2016.56] the labs belong to that company that is capped profit so once they hit the 30x what happens the
[2016.56 → 2023.64] rest of the money goes up to the NGO yeah there's a whole-complicated discussion around and actually i
[2023.64 → 2028.60] mean one of the things that we have to talk about here is this question that i didn't mean to back into
[2028.60 → 2035.18] quite yet but something to signpost for the viewers in oh my goodness we are flying is this question of
[2035.18 → 2040.24] what does it mean to be open in this space right because we don't really know what the rights are
[2040.24 → 2045.64] and we don't know what power is in this space we're learning a lot on the fly and so you'll see a lot of
[2045.64 → 2050.80] stuff labelled open in the space and i don't mean this specific to open AI Natalie because there's like
[2050.80 → 2058.34] a lot of folks using open very loosely in this space some of your listeners may or may not know
[2058.34 → 2062.88] the open source initiative for a long time has defined what open source means in software
[2062.88 → 2069.58] there's a lot of again nuance there, but it's there is a list of like these are the open source licenses
[2069.58 → 2075.84] and there's a list of criteria like open source licenses have to meet certain criteria amongst
[2075.84 → 2081.72] others of which is everybody's got to be able to use it for anything you can't use this for
[2081.72 → 2088.34] nuclear weapons, or you can't use this for human rights violations if you slap that kind of restriction
[2088.34 → 2094.66] on if it's no longer open source as defined by the open source initiative there's a lot of AI
[2094.66 → 2099.82] stuff that has exactly that kind of language in it no human rights violation no harassment
[2099.82 → 2107.06] and are calling themselves open anyway and the gray area there is a fascinating one, and it's
[2107.06 → 2113.48] one that I've been exploring a lot i have a newsletter called open ml.FYI that it hasn't
[2113.48 → 2118.22] published yet this year but hopefully this afternoon for the first time this year when I'm exploring
[2118.22 → 2125.50] exactly these questions of what does it mean to be open and open source where you know Chris to get
[2125.50 → 2130.36] back to your example because i do want to get this back on track a little bit the compiler right we have
[2130.36 → 2135.32] a very certain assumption open source is based on some assumptions of their source code there's a compiler
[2135.32 → 2141.84] there's an executable and those assumptions don't hold true in the same way right like there is no
[2141.84 → 2150.84] source code for a model per se right like there's the data set there's like the way you trained
[2150.84 → 2158.64] the data set into the model, but that's not the same as source code from a perspective of i mean the
[2158.64 → 2163.82] data set may be literally too big to download it may be impossible for you to do
[2163.82 → 2169.40] on commodity hardware enough training it may be illegal for you to download because that data set
[2169.40 → 2175.14] may include private information contractually restricted information so what does it mean to be
[2175.14 → 2182.10] open when you can't reconstruct the whole thing from one end to the other is a fascinating one
[2182.10 → 2186.44] and one that i don't think we have a great i think a lot of the assumptions of the industry has been
[2186.44 → 2191.50] built on right everybody who uses go and Chris to your point about the compiler and about the
[2191.50 → 2195.18] programming language i mean that's the other part of this right like Chris if you've got a compiler
[2195.18 → 2199.52] you assume that you can just use the outputs of the compiler right well same thing with the
[2199.52 → 2206.54] programming language right every standard library of every major programming language out there is under a
[2206.54 → 2213.64] super permissive license because you do actually i mean the one sort of exception to what you're saying
[2213.64 → 2218.16] Chris about like oh well the compiler just spits out a thing at the end, and it's the
[2218.16 → 2222.50] a lot of compilers in a lot of languages depends on the language the technology etc right
[2222.50 → 2229.88] will compile in part of the standard library into your executable and so in fact if the standard
[2229.88 → 2235.36] library has some kind of like use restriction on it that's a problem now of course as a practical
[2235.36 → 2239.18] matter nobody does that with our languages because i would be shooting your language in the foot if you
[2239.18 → 2244.12] had a clause like that right so everybody says yeah sure use the standard library however you want
[2244.12 → 2251.90] we're not going to like nitpick over that right, and we haven't mostly yet reached that point like in
[2251.90 → 2257.96] some ways you can think of these restrictions around a lot of these models as sort of equivalent to a
[2257.96 → 2263.30] standard library in some way right like it's the developers really want you to live within these
[2263.30 → 2271.50] platforms within these frameworks but unlike the standard library or like the core operating systems
[2271.50 → 2278.42] windows Linux mac they don't say like you can't use this for a laundry list of things mostly don't
[2278.42 → 2282.12] say you can't use this for this laundry list of things that you're a developer you take for granted
[2282.12 → 2289.72] that that can be done and right now a lot of this ai especially the big platforms but the models you can
[2289.72 → 2294.40] download as well come with a lot of restrictions an interesting question and this gets back to this
[2294.40 → 2301.86] question of is the model copyrightable or not is can we actually make those stick so like the way
[2301.86 → 2307.00] we are something we haven't really talked about a little bit and gets back to this TLDR right if i
[2307.00 → 2314.48] create a binary of a piece of software, and you start making copies of it to use it you need a copyright
[2314.48 → 2320.48] license from me to do that so that means i can start sticking conditions in the copyright license
[2320.48 → 2326.68] like you have to pay me every time you do that or every time you spin up a new instance in the cloud
[2326.68 → 2333.62] you've got to pay me for that, or you shouldn't use this for x y and z bad purposes you shouldn't
[2333.62 → 2339.62] use this to compete with me right we put this laundry list of restrictions into binaries we know
[2339.62 → 2345.64] as a matter of law that binaries are like executables of traditional software are copyrightable
[2345.64 → 2351.38] we don't actually know for a fact that models are so when somebody gives you a model and says yeah
[2351.38 → 2356.02] by the way here's all these restrictions if you violate these restrictions I'm going to take away
[2356.02 → 2361.68] your license to use the model it's not actually clear that that works right it's not actually clear
[2361.68 → 2368.04] that you need a copyright to use that thing and if you don't then how do we enforce these ethical
[2368.04 → 2373.54] restrictions that the AI industry for very good reasons is very concerned about people following
[2373.54 → 2380.74] right like Natalie i don't know how you I'm curious how you got into the AI space Chris was saying he
[2380.74 → 2384.72] wanted to dabble i had forgotten that you're an ambassador in this space you've thought about a
[2384.72 → 2391.68] fair bit right a lot of the open AI model releases because Natalie didn't say this but open AI has
[2391.68 → 2395.62] released a lot of different models under a lot of different terms right codex is one of them
[2395.62 → 2400.46] there are quite a few others some under more permissive some under the more restrictive licenses
[2400.46 → 2405.34] and some of those are restrictive for very good reasons like don't use this to stop people don't
[2405.34 → 2411.84] use this for deep fake porn, but it's unclear how that gets enforced like we don't actually know as
[2411.84 → 2417.58] lawyers yet how that will work we've all got theories, but you know that would have to be episode three
[2417.58 → 2444.34] the changelog is deep discussions in and around the world of software, and it's been going for over a decade
[2444.34 → 2450.78] we interview hackers like Chris Anderson from 3d robotics at the time drones were like predators
[2450.78 → 2456.60] and global hawks and military industrial they were classified and super you know 10 billion dollar
[2456.60 → 2462.66] things, and we had just built a drone with Lego pieces around the dining room table programmed by a
[2462.66 → 2468.22] nine-year-old, and it's like okay that should not be possible you know it's not it when a nine-year-old
[2468.22 → 2474.44] can do something that is classified that literally export control is munition with Lego with toy pieces
[2474.44 → 2480.32] it was something important in this world has changed leaders like Devin fuel from GitHub
[2480.32 → 2486.78] in the like 10 to 15 year range or 20 year range what i would really like is for if you have like
[2486.78 → 2491.68] three 12-year-olds hanging out and one of them's like i want to be a firefighter another one's like i
[2491.68 → 2494.74] want to be a lawyer i want one of them to say that i want to be an open source developer
[2494.74 → 2500.40] and innovators like Abel Hussein I've yet to kind of see applications at scale that don't use multiple
[2500.40 → 2507.08] languages that don't you have just arcane stories behind why this weirdo thing exists you know like
[2507.08 → 2511.62] all right when you open this file you're going to have to turn around three times and tap your nose
[2511.62 → 2520.94] once like it's just the most hilarious story you know, but applications are living breathing they have
[2520.94 → 2529.22] craft that's normal so I want to normalize weirdness because that's just how applications evolve over
[2529.22 → 2535.10] time welcome to the changelog please listen to an episode from our catalogue that interests you
[2535.10 → 2537.78] and subscribe today we'd love to have you with us
[2537.78 → 2545.52] I would love to hear Natalie how you got into the space and what your perception here is
[2545.52 → 2550.80] from the other side i.e. like as an ambassador are there mumblings in the space that you've had
[2550.80 → 2556.84] I don't understand the question like you got into this space as an ambassador as someone who works in
[2556.84 → 2562.86] you know open AI when you're thinking about I don't work in open AI as an ambassador then who has
[2562.86 → 2572.48] interacted with open AI and knows some stuff about it, I would love to hear either yourself or people
[2572.48 → 2578.72] you've chatted to in that space more directly how they're thinking about like open sourcing giving
[2578.72 → 2583.42] out models for use whether as Louie you mentioned with parameters around like don't use it for this
[2583.42 → 2590.50] or like hey you can use this for whatever use case you need it to like to have you heard of any opinions on
[2590.50 → 2595.94] or do you have any information on how they make those decisions the answer can be no I think that's just
[2595.94 → 2599.80] a fascinating like I'd love to be in the room when they're thinking about like oh we've got this
[2599.80 → 2606.36] new cool model should we put some restraints on it should we give any like PSA don't use this for xyz
[2606.36 → 2612.88] yes that's many questions definitely so what I do there is I volunteer there you can say I'm a
[2612.88 → 2617.12] developer ambassador which means that people who get access to that it was more relevant to the time
[2617.12 → 2623.32] that it was rolling access to that to gpt3 and then to Dali and so on then people would come to my
[2623.32 → 2628.50] office hours and just ask me questions mostly technical questions but sometimes also can I do that or
[2628.50 → 2635.90] think about things with me so I mostly interact with the users, so there are all sorts of restrictions
[2635.90 → 2641.30] on place for example when Dali just started being public you could not put all sorts of words in
[2641.30 → 2646.08] there and then came the other side of this entire thing when mid-journey came out and then
[2646.08 → 2652.52] you could write anything, and then it obviously ended up in weird parts of the internet as it tends to
[2652.52 → 2657.14] be when you have free access to everything so I think this is kind of two edges to that and the balance
[2657.14 → 2665.72] will be somewhere in between one way of enforcing now good usage it's a very wide definition is that
[2665.72 → 2672.28] you always have to go through a review if you use open AI in production so if you use it for fun
[2672.28 → 2679.44] use it for fun if you want to actually use that you have to get like a PR as we know it from our world
[2679.44 → 2683.66] of context, but actually somebody from open AI will go through your plan of what are you going to do with
[2683.66 → 2690.52] that in production how is it going to be reasonably safe and so on, so this is how it's happening right
[2690.52 → 2695.98] now how will it be in the future that's a great question another interesting question of what is now
[2695.98 → 2701.40] versus what is later is something that has been surfacing on you know hacker news Reddit and so on so
[2701.40 → 2709.84] there's a professor that is called Scott Bronson I want to say he came to open AI for a year of
[2709.84 → 2716.46] research so he's now in the middle of it, and he's driving the concept or the idea of watermarking
[2716.46 → 2723.20] output of text we know watermark from images you know if you go to stock images you pay money and
[2723.20 → 2727.44] then you don't get that watermark, and then they have the idea of or some people in the team have
[2727.44 → 2733.92] the idea of doing that for text and there's discussion yes or no good or bad and so on, and it's
[2733.92 → 2739.16] also interesting to do that for code, but it's a lot harder and I think this is where one of the
[2739.16 → 2745.30] things that I'm super interested in openness original open source it was in some sense just
[2745.30 → 2751.22] an IP law thing right like it was just a copyright license, but it redistributed power in the industry
[2751.22 → 2758.64] right it made it possible for a small startup like google because their original plans were like well
[2758.64 → 2763.42] we're gonna need in order to do this we're going to need tens of thousands of machines of course you know
[2763.42 → 2768.44] now it's tens of millions or whatever right but at the time the idea that you could license 10,000
[2768.44 → 2774.10] machine like operating systems again to this question of copyright licensing from at the time
[2774.10 → 2779.04] your options were sun or Microsoft right that would have been implausible right it just would have been
[2779.04 → 2786.64] too costly to create google and open source allowed new competitors to come in, and we've seen this in a
[2786.64 → 2793.30] variety of different spaces right it tends to i won't say it ends control because obviously we've ended up
[2793.30 → 2797.60] in a world where there's a small number again of controlling they're just using different tools to control
[2797.60 → 2804.28] the industry so where are we going to be at that because there's Natalie mentioned codex there's a
[2804.28 → 2811.10] project called big code which is an open is you can join the slack you can download the models you can
[2811.10 → 2818.12] discuss their ethical restrictions and that is all being done in the open right it's not inside any
[2818.12 → 2826.68] one company there are some corporate sponsors to buy GPU time, but it is going to be research oriented
[2826.68 → 2833.68] alternative to codex but if that's out there in the open or what I've been calling open is in my
[2833.68 → 2839.92] newsletter because it's open with some restrictions are they huge restrictions small restrictions we
[2839.92 → 2844.78] don't really know yet open AI is going to be doing this like very good I think very interesting work on
[2844.78 → 2850.12] things like fingerprinting like you say if you want to deploy in production open AI is going to like
[2850.12 → 2855.76] challenge you on the safety of your usage okay well but once it's out there if somebody else is doing an
[2855.76 → 2861.98] open competitor open is competitor what's the infrastructure for and this gets again to these
[2861.98 → 2870.94] other layers I think if your listeners take away any one thing from this talk right it's that for a long
[2870.94 → 2880.16] time we used intellectual property licenses to govern the ethics of our software that was weird
[2880.16 → 2886.02] and probably not very good, and we should stop doing that as like the first line of defence
[2886.02 → 2893.06] right because there's just too many other tools of government regulation Natalie's example of a
[2893.06 → 2900.66] platform regulating what's being used codes of conduct this like 25-year period where intellectual
[2900.66 → 2906.88] property was the hook that we did all of our ethical regulation through was a very weird period and
[2906.88 → 2911.48] like it was very lucrative for me as an intellectual property lawyer but like probably not the right
[2911.48 → 2916.88] thing for the industry right so again for your listeners if there's any one thing to take away from
[2916.88 → 2922.74] this it's that if somebody says hey we should use an IP license to make human beings behave better
[2922.74 → 2928.54] your instinctive reaction should not be oh hey that's what the free software people did
[2928.54 → 2935.86] your instinctive reaction should be oh if we must is that's the only tool we've got
[2935.86 → 2941.28] then yeah maybe, but it's almost never the only tool we've got there are so many other layers of
[2941.28 → 2947.98] regulation now that we can use to try to govern how we work together that are probably better suited for
[2947.98 → 2953.36] it because IP is just I mean like I said to get back to this like we don't even know right and we
[2953.36 → 2957.50] haven't even gotten into some of the weird side corners I don't know how much time we've got left
[2957.50 → 2963.24] but yeah so I've been thinking about something, and it's related to this whole like you know co-pilot
[2963.24 → 2968.10] or like really any model that writes code for you, and it feels like there's like kind of this spectrum
[2968.10 → 2973.24] of things when it comes to writing code where it's like fundamentally all of us write code based on code
[2973.24 → 2977.88] that we've seen before, but we like to learn the code learn the syntax learn algorithms learn all that and
[2977.88 → 2983.12] then we can like to use our own creative ability to like to write something and then there's like kind of the
[2983.12 → 2987.52] other end of it where you can just like copy and paste something else that you found and go use
[2987.52 → 2994.36] that and the thing I've been thinking about is like where is the line in that gray space when it tips to
[2994.36 → 3001.24] one side or the other right like if I copy the whole thing and then modify it a bunch is that like how
[3001.24 → 3006.62] much does that amount to like okay this is a new derivative thing that doesn't have the old copyright
[3006.62 → 3010.92] thing because once again like you're reading code you're absorbing code from tons of other different
[3010.92 → 3015.18] like our minds are doing the things that the models do at the end of the day like our brain is a model
[3015.18 → 3020.94] in and of itself so it's like we're producing stuff that would be said okay this is your copyright
[3020.94 → 3025.30] because you wrote it, but it's based on everybody else's work so where's like where does that
[3025.30 → 3030.72] derivative line exist and like what actions are required to make it happen because obviously like
[3030.72 → 3034.92] if I copy and paste some code from one place to another place I don't get the copyright to that code
[3034.92 → 3040.32] because I've just copied it right, and it creates a new derivative work but if I like retype all that
[3040.32 → 3047.08] code and change some things along as I'm retyping it like is that still a derivative work if I'm not
[3047.08 → 3052.46] looking at it does that make it less of a derivative work than if I am looking at it like it feels like
[3052.46 → 3058.24] this whole space is like super murky and I feel like the answer is like we haven't really found an
[3058.24 → 3063.26] answer to any of this so one absolutely correct we haven't found an answer, or we've sort of found
[3063.26 → 3068.72] several answers and none of them are great right because it's going to depend on things like well so one
[3068.72 → 3074.16] analogy we sort of got off the analogies track but one analogy here is googled book search where they
[3074.16 → 3081.46] said up front we are copying all the world's books, but we did a lot on the back side right on the user
[3081.46 → 3088.30] interface to make it really hard for people to get more than a fraction of the book out at any one time
[3088.30 → 3095.04] right, and we created a lot of new value by making all these books searchable so a court looked
[3095.04 → 3100.64] at that and was like well yeah all that copying very bad but all the value that was created and
[3100.64 → 3107.20] the reasonable steps taken to protect it means that it's what courts lawyers literally call a balancing
[3107.20 → 3114.60] test right the court was sort of like so that's one analogy right and in that case as long as the
[3114.60 → 3120.44] co-pilot folks are taking like good faith steps co-pilot at least is going to be protected
[3120.44 → 3125.78] maybe if you're copying a section of a book out of Google book search or a copy of code at a co-pilot
[3125.78 → 3130.90] you might be in trouble but Microsoft and open AI will probably be okay right because it might be like
[3130.90 → 3134.68] google book search to a court but there's a case in front of the supreme court right now about Andy
[3134.68 → 3142.30] Warhol and there are some cases in California but federal courts about the song blurred lines
[3142.30 → 3150.84] and where like only a handful of notes in the blurred lines case was enough to make that song
[3150.84 → 3157.32] a copyright infringement now a lot of IP attorneys are like horrified by that outcome because it's like
[3157.32 → 3163.18] so small and to a certain extent the judge was like you know what it just has the same vibe and IP
[3163.18 → 3167.94] lawyers are like, but you can't copyright vibe and the judge was like yeah I can watch me do it
[3167.94 → 3174.92] so code by the way co-pilot is the easy case right because there's not much vibe in code but like
[3174.92 → 3180.58] they're like as soon as we start getting into like dolly that Natalie already mentioned mid-journey all
[3180.58 → 3185.44] these things like okay well then we get into like and this is where the Warhol thing and the Warhol case
[3185.44 → 3193.42] comes in like there's that Warhol vibe is that protectable is that like and I shouldn't actually
[3193.42 → 3197.50] say I should say the Warhol case is not about Warhol's vibe Warhol in this case
[3197.50 → 3203.56] is the copier not the person being copied but the same kinds of questions like are just going to
[3203.56 → 3209.06] keep popping up, and we don't know Chris we don't know yet where these lines are going to be and
[3209.06 → 3215.10] again the outcomes are going to be different for the company that makes the model and the person who
[3215.10 → 3221.96] uses the model so the one thing that I've told people consistently is I think that GitHub is probably
[3221.96 → 3227.44] actually safe here I don't think running co-pilot is itself an infringement I think it's
[3227.44 → 3233.64] a lot like google book search using co-pilot 99 of the time is going to be fine but if you're doing
[3233.64 → 3242.68] something like clean rooming somebody's API imagine like if you tell co-pilot like hey I've got this API
[3242.68 → 3247.46] it happens to be somebody else's API and by the way that company might be using GitHub behind the
[3247.46 → 3252.30] scenes we don't even know, and it starts re-implementing their entire API for you
[3252.30 → 3259.24] that's where again the vibes the balancing might be a lot different it's funny I was having a
[3259.24 → 3263.06] conversation with a friend who I assumed his company was doing no clean rooming and I was
[3263.06 → 3266.38] like oh yeah well the only thing is like as long as you're not clean rooming, and he like literally
[3266.38 → 3271.72] picks up his phone in Texas out of his CTO, and it's like we need to talk tomorrow morning because
[3271.72 → 3276.30] it turns out this friend's company was doing some clean rooming of something with a company that
[3276.30 → 3281.06] hates them on the other side of it is right so like that's where you get into that's the other thing
[3281.06 → 3285.22] right like a lot of these things are hypothetical because nobody's gonna nobody's going to know or care
[3285.22 → 3291.68] 95 of the time but if you're, i would definitely not use co-pilot to re-implement any oracle APIs
[3291.68 → 3295.36] that's my one other piece of advice to you that you should remember from this podcast
[3295.36 → 3300.92] oracle is like the uh the litigious people that do lead us forward in some ways like their
[3300.92 → 3306.34] their fun poem in their what is it their connection protocol so you can't implement it
[3306.34 → 3310.90] without copyright infringement they have all the creative stuff they kept me very
[3310.90 → 3315.76] employed for a long time on the Google oracle case I've worked for Google to be clear the
[3315.76 → 3321.86] oracle people can go rod in a swamp as far as I'm concerned but is that my unpopular opinion or
[3321.86 → 3326.70] does that count as a popular opinion I guess it depends on who you are and for our listeners
[3326.70 → 3329.96] can you just define what clean rooming is because some people might not be familiar with that term
[3329.96 → 3335.90] oh yeah, yeah sure there are times when you might want to copy what another company is doing
[3335.90 → 3341.50] right and so clean rooming is the idea it comes originally from patent law because you might want
[3341.50 → 3347.64] to get to the same result but get there differently, so somebody will write out here's
[3347.64 → 3352.06] the result we want to get you're not allowed to look at anything the other company did
[3352.06 → 3359.52] so that's what when originally when IBM re-implemented java way way way back in the day they literally
[3359.52 → 3365.42] they gave instructions to people like well here's the API headers the java API headers you can't look
[3365.42 → 3369.94] at anything you have to promise up and down I haven't looked at anything that oracle's ever done
[3369.94 → 3376.16] I haven't it was a clean room because it was clean of anything that oracle had done if you did the same
[3376.16 → 3382.04] thing today and somebody used co-pilot like you yourself might be clean of anything that oracle had
[3382.04 → 3388.10] done, but we don't know if co-pilot is clean of anything, but we are now eight minutes past where
[3388.10 → 3393.52] angelica was saying frantically in chat we have to stop we have to stop so let's stop thank you all
[3393.52 → 3398.88] for having me it's so hard to cut off such wonderful uh conversation I always struggle like this is the
[3398.88 → 3403.86] last thought oh, but this is fascinating let's let this go on longer sounds like we need a part
[3403.86 → 3409.80] three I know that's what I was just thinking I'm like we're going to do a part of three we may well need
[3409.80 → 3414.90] one maybe I'll finally start restart my own podcast and bring you all for a know crossover
[3414.90 → 3424.02] maybe, maybe awesome well we're gonna now dive into unpopular opinions which I'm very excited about
[3424.02 → 3428.86] so get them ready get your brain clogs going if you haven't got one and here we go
[3428.86 → 3457.74] so what is your unpopular opinion lewis over to you super, super hot take blockchain was good
[3457.74 → 3466.32] because it took everybody's attention away from ml for several years so that people could actually
[3466.32 → 3472.90] like get some stuff done before the like buckets of money sloshed in and now that people have realized
[3472.90 → 3478.04] that blockchain is actually all terrible the buckets of money are sloshing into ml and that's like
[3478.04 → 3483.12] you know it's good and bad right it can be its great in some ways, but it can be distracting in
[3483.12 → 3489.82] other so I'm sort of actually glad that blockchain like took that energy for a few years responses do
[3489.82 → 3495.48] we think that's popular unpopular I mean I hesitate with anything that's like blockchain is good but
[3495.48 → 3501.82] I told you it was a good hot take I mean in general it feels like that's like it like oh we were able to
[3501.82 → 3506.54] go do some good stuff because we kept the boatloads of money and all the bad stuff that comes with it away
[3506.54 → 3512.12] from this space for a bit I can get on board with that blockchain and crypto in general though I'm just
[3512.12 → 3521.76] kind of like let me mint that yeah I've been watching some coffee Villa on YouTube recently
[3521.76 → 3527.54] he's like this investigator that like goes into like all of these different types of scams and I'm just
[3527.54 → 3535.58] like it is so easy to just like to create a new coin and then just like extract money from people and I'm
[3535.58 → 3542.26] like this is a wild space all started because of this blockchain thing but then again like most of
[3542.26 → 3549.66] finance also we've had Ponzi schemes for a very very very long time so okay we'll see what what
[3549.66 → 3556.04] the twitter public think Chris do you have an unpopular opinion I don't think I do I mean I'm sure I have
[3556.04 → 3561.62] many unpopular opinions I don't have one like prepared at this exact moment okay I guess my
[3561.62 → 3568.04] unpopular opinion would be like new year's resolutions suck, and you should just try like the
[3568.04 → 3574.12] who's it cap gray has some good videos on like theme like have themes have a theme for the season
[3574.12 → 3581.18] of like you know oh I will uh the season of learning or whatever those are much better than like I'll go to
[3581.18 → 3586.24] the gym five days a week or things like that you know build some good flexibility into them but i
[3586.24 → 3592.12] don't think that you know new year's resolutions suck is an unpopular opinion I think a lot of people
[3592.12 → 3598.98] hold that opinion I was going to ask if you had an unpopular resolution like I'm going to steal candy from
[3598.98 → 3605.38] a baby once a week or something like that I do think i have one of my resolutions is like
[3605.38 → 3610.36] crazy, but it's not crazy because like I can do it but like I'm trying to like write
[3610.36 → 3617.32] more I recently did a review of how much journaling I've done and over the past few years past two
[3617.32 → 3622.58] years actually coming up in the anniversary when I started journaling like heavily I think I'm
[3622.58 → 3628.46] approaching about 3.6 million words written over the course of two years, so one of my resolutions is
[3628.46 → 3632.94] to write more so I think that'd be unpopular with many people because that sounds insane
[3632.94 → 3638.72] you write millions of words per year yes I write millions of words per year yeah that's 5 000
[3638.72 → 3645.90] words a day man yes well done I think that might be an unpopular resolution I will not be taking on
[3645.90 → 3652.02] writing more than 5 000 words a day personally interestingly it only takes me about an hour to do
[3652.02 → 3658.96] so it's not like it's now you just show it off Chris I write really slowly okay you put me to shame
[3658.96 → 3664.22] I maybe write like five words a minute oh this is what happens when you're a writer you just the brain
[3664.22 → 3668.88] is brimming with things that need to get out of it to make space for the other things well I look
[3668.88 → 3679.52] forward to reading your encyclopedia length journal next week Natalie unpopular resolution or opinion
[3679.52 → 3686.10] my unpopular resolution slash opinion I guess you can make them into one I've been trying to eat
[3686.10 → 3693.28] seasonal, and it's terrible in winter at least here in the north slash central part of Europe
[3693.28 → 3698.52] like all the fruits you get if you try to eat fruits and veggies mostly you get apples and roots
[3698.52 → 3705.14] so my unpopular resolution will be to eat slightly less seasonal and my unpopular opinion is that we
[3705.14 → 3711.50] should make seasonal food better or different and that was me thinking you just were drinking an
[3711.50 → 3718.96] obscene amount of pumpkin spice lattes I mean pumpkins show up on time you can use spice latte
[3718.96 → 3726.76] on them in there if you yeah grill them but no I just mean like produce yeah okay so eat less seasonally
[3726.76 → 3730.98] fair enough and now tomorrow I'm going to see like tomatoes on the house or something it's the worst
[3730.98 → 3736.38] thing you can say what is your unpopular opinion angelica oh i always whatever I haste to get out of it
[3736.38 → 3745.96] um my unpopular opinion slash view is let's think I've got one but I don't know I think it would
[3745.96 → 3750.28] actually be unpopular and I think I'd get some slack for saying it, but it's actually what I think right
[3750.28 → 3760.22] now is sometimes it is okay to not do your own construction work and just make someone else do it
[3760.22 → 3767.16] for you context being I've tried to put a picture up yesterday because I thought I was like no I can
[3767.16 → 3773.80] do it myself I can hang up this picture I did, and then it fell down and smashed all over my floor
[3773.80 → 3780.24] about a day later after I had spent about half an hour getting quite irate in a friend who said that
[3780.24 → 3784.62] he would just come help me because he didn't think I could do it and I was really trying to prove myself
[3784.62 → 3793.34] and then I called him and I was like it fell so did you use some guide or did you just like take a
[3793.34 → 3800.42] hammer my unpopular opinion is sometimes it's okay to admit you can't do the thing that you spent half
[3800.42 → 3806.54] an hour being very offended because someone thought you couldn't that pride sometimes gets you it did
[3806.54 → 3811.12] I have to buy a whole new frame it is like smashed everywhere it was a whole thing and I have a hole in
[3811.12 → 3818.94] my wall now but anyway so that is my unpopular popular opinion I mean it's unpopular with me
[3818.94 → 3823.80] those posters back there those bookshelves I put all those up myself Chris this is like
[3823.80 → 3830.70] Chris can do everything show off show today what's up maybe you should help me Chris I mean I could
[3830.70 → 3838.12] but your friend could also help you like someone else can do it for me is the basis of a good source
[3838.12 → 3844.22] so like I think it's okay and trust you to bring it all together for us Louis thank you so much
[3844.22 → 3852.52] we'll have a wonderful rest of your days thank you listeners and that's it unfortunately bye
[3852.52 → 3864.24] that is our show for this week thanks for listening if you missed part one of this conversation
[3864.24 → 3871.46] scroll back in the feed to october 2022 and give it a listen that's episode number 252 I'll also link
[3871.46 → 3877.58] it in the chapter data for easy clickings oh and if your podcast app doesn't support chapters maybe
[3877.58 → 3882.92] it's time for an upgrade if you get value from go time return some value with a changelog plus
[3882.92 → 3888.58] membership as a bonus you can ditch the ads get closer to the metal with bonuses and extended episodes
[3888.58 → 3894.16] and more check it out at changeholder.com slash plus thanks once again to our partners quickly
[3894.16 → 3900.38] and fly for helping us bring go time to you check them out at fastly.com and fly.io and thank you to
[3900.38 → 3904.96] our mysterious friend break master cylinder for supplying us with the best beats in the business
[3904.96 → 3911.48] next time on go time Natalie is joined by ole bull book and Sandor souks to discuss long-term
[3911.48 → 3915.22] code maintenance stay tuned for that we'll have it ready for you next week
