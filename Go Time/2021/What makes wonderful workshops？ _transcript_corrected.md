[0.00 → 10.50] From a participant's point of view, like I, which maybe I shouldn't say, but every workshop I go to, I try and find a TA who I can be friends with, who will kind of just like sit near me the whole time.
[10.90 → 12.14] Just like, hey.
[12.52 → 14.46] Explain everything the instructor said.
[14.72 → 15.20] No, literally.
[15.20 → 15.76] Personal tutor.
[16.30 → 25.60] And I mean, honestly, having been in workshops with Jonas and Johnny, now I've said that, they might be able to remember that I kind of recruited one TA to be my life person.
[26.32 → 26.82] I remember.
[26.82 → 32.70] And then they'd start walking away, and I'd be like, I've got a question, actually.
[34.96 → 37.58] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[37.96 → 38.52] We love Linde.
[38.60 → 40.02] They keep it fast and simple.
[40.14 → 42.50] Check them out at linode.com slash changelog.
[42.74 → 44.80] Our bandwidth is provided by Vastly.
[45.16 → 48.70] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[48.98 → 50.68] Get a demo at LaunchDarkly.com.
[51.46 → 52.36] What's up, Gophers?
[52.36 → 62.06] Our friends over Gravitational made a big transition at the end of 2020 to rebrand as Teleport and shared a new product announcement to showcase the direction they're taking.
[62.06 → 69.12] Teleport is operating from a vision of being able to run and access software anywhere in a secure and compliant manner.
[69.42 → 71.52] Something they call environment free computing.
[71.52 → 85.26] With Teleport, engineering teams can quickly access any resource anywhere using a unified access plane that consolidates access controls and auditing across all environments, infrastructure, applications, as well as data.
[85.60 → 92.28] Teleport server access lets you SSH securely into Linux servers and smart devices with a complete audit trail.
[92.62 → 98.52] Teleport Kubernetes access lets you access Kubernetes clusters securely with complete visibility to access and behaviour.
[98.52 → 105.34] And finally, Teleport application access lets you access web apps running behind NAT and firewalls with security and compliance.
[105.86 → 109.40] Try Teleport today in the cloud, self-hosted, or open source.
[109.74 → 112.32] Head to goteleport.com to learn more and get started.
[112.70 → 114.68] Again, goteleport.com.
[114.68 → 136.14] Let's do it.
[136.74 → 137.78] It's go time.
[138.50 → 139.96] Welcome to go time.
[140.10 → 143.26] Your source for diverse discussions from around the go community.
[143.26 → 150.16] We record the show live on YouTube each and every Tuesday at 3 p.m. U.S. Eastern, 7 p.m. UTC.
[150.72 → 155.48] Subscribe at YouTube.com slash changelog to be notified when we go live.
[155.80 → 161.48] And don't forget to follow GoTimeFM on Twitter and vote on our unpopular opinion polls.
[161.80 → 163.22] This is very important stuff.
[163.54 → 164.60] Okay, let's do this.
[164.76 → 165.08] Here we go.
[165.08 → 173.66] Welcome to our workshop edition of Go Time.
[173.92 → 174.80] I am Angelica Hill.
[174.88 → 176.12] I will be your host today.
[176.26 → 180.76] And we are joined by three wonderful women and the incredible Johnny.
[181.22 → 184.42] First, we have Natalie, who wears several hats.
[184.42 → 190.74] Among them, she is a developer advocate, an organizer at GoFer Con Europe, and an instructor of various
[190.74 → 196.10] different workshops, including About ML at GoFer Con in the U.S., and also loves attending
[196.10 → 197.46] workshops and learning.
[197.80 → 198.32] So hello.
[198.52 → 199.22] Welcome, Natalie.
[199.32 → 199.76] How are you?
[199.98 → 200.78] Hi, Angelica.
[200.96 → 202.90] It's great to be here with you as a host.
[203.22 → 205.96] It's always great to have British people in this position.
[206.24 → 206.78] Love the accent.
[207.12 → 207.86] Thanks for doing that.
[208.00 → 211.34] Yeah, Matt and I thought we'd just swap out because most people probably won't tell the
[211.34 → 211.76] difference.
[211.92 → 212.30] We'll see.
[212.30 → 218.82] Secondly, we have one of our guests on this show, Jonas, who is an engineering manager at
[218.82 → 219.60] the New York Times.
[219.94 → 223.50] She formally organized Women Who Go New York City.
[224.08 → 229.54] She also coordinated and led many workshops over the years, including Intro to Go, Go Modules,
[229.68 → 231.22] and Domain Driven Design.
[231.94 → 233.36] So happy to have you, Jonas.
[233.86 → 235.00] Thanks, Angelica.
[235.16 → 236.62] Can't wait to dive in.
[236.72 → 237.58] Very, very excited.
[237.94 → 242.04] Next up, we have Anna, who's actually currently building a workshop herself.
[242.04 → 245.36] From Scratch for Go4Con Europe about security and Go.
[245.90 → 249.42] She organizes the Frankfurt chapter of the Go user group.
[249.88 → 253.44] And in this role, she coordinates and has led various different workshops over the last
[253.44 → 254.02] few years.
[254.52 → 255.82] So happy to have you, Anna.
[256.04 → 257.86] Very excited to hear more about your workshop.
[258.56 → 259.18] Thank you.
[259.32 → 260.46] I'm glad to be here.
[260.46 → 262.12] And yeah, I'm looking forward.
[263.32 → 269.56] And then last, but certainly not least, you may know him as a regular guest on the show.
[269.86 → 276.08] But other than that, he is involved in honestly every single part of the Go community, it seems.
[276.44 → 279.38] He has been teaching Go workshops for a number of years.
[279.38 → 283.38] He has run the Boston Go user group, the Baltimore Go user group.
[283.38 → 286.58] He's taught at Go4Con many, many years in a row.
[286.76 → 290.14] He's chairing this CFP process for Go4Con as well.
[290.70 → 294.98] And he's just generally an incredibly helpful mentor in the Go community.
[295.14 → 296.74] I myself went to one of his workshops.
[296.88 → 298.62] It was my first Go workshop ever.
[299.14 → 301.82] So he is certainly a kind of Go guru in the field.
[302.04 → 306.76] He's also currently doing some of the O'Reilly teaching online.
[306.86 → 308.02] So do check him out.
[308.02 → 313.14] And honestly, any conferences, meetups, Google his name, you'll probably see him at a million
[313.14 → 314.26] and two different meetups.
[314.64 → 316.72] So yeah, very invested in the Go community.
[317.00 → 319.22] So very excited to hear your input here, Johnny.
[319.42 → 320.02] Thanks for having me.
[320.20 → 320.48] Awesome.
[320.58 → 322.00] So we're going to dive right in.
[322.08 → 327.12] And I'd love to hear first, kind of what do you find the most useful about workshops
[327.12 → 332.38] when you're looking to learn or teach as opposed to kind of books, giving talks, presentations?
[332.92 → 335.42] I might turn over to you, Jonas, first.
[335.42 → 339.78] I think the biggest thing for me with the workshop is really the more hands-on part of it and
[339.78 → 345.36] that you have an instructor or a TA or even your fellow learners right there with you as
[345.36 → 345.74] you're learning.
[346.02 → 349.52] So that's the biggest part is its kind of this collaborative learning where you're really
[349.52 → 350.38] getting into it.
[350.52 → 351.56] It's the unique part.
[351.62 → 352.94] I think you can't really do that in a book.
[353.64 → 359.60] And then Anna, I mean, when you're thinking about kind of going into Go4Con Europe and wanting
[359.60 → 364.88] to maybe distribute your wonderful knowledge of security and Go, why did you think a workshop
[364.88 → 368.00] might be the best way to do that as opposed to maybe doing a talk?
[368.14 → 374.46] Yeah, I think a workshop, as Jonas mentioned, gives you more hands-on than just a talk.
[374.96 → 381.48] Like if I tell you something, you probably say I know it or good to know, but you don't
[381.48 → 382.46] do it by yourself.
[382.62 → 387.80] You don't experience what it means to do things wrong or do things correctly or how easy it
[387.80 → 388.02] is.
[388.02 → 394.34] And I think that's something only a workshop can offer so easily because even if I do live
[394.34 → 398.08] coding, you won't do anything as a listener there.
[398.44 → 405.06] And then in terms of when you're trying to begin thinking about what content you're going
[405.06 → 409.10] to include in a workshop, when you're thinking, okay, I've got this, I want to distribute my
[409.10 → 409.36] knowledge.
[409.50 → 413.80] I feel like I have enough experience in a certain topic that I feel ready to kind of teach.
[413.80 → 419.16] Where do you start in terms of thinking about, okay, how do I structure this?
[419.32 → 421.56] How much information should I put into my workshop?
[421.66 → 426.64] I might turn over to you, Johnny, for this one, because I think that really is the highest
[426.64 → 427.12] roadblock.
[427.22 → 430.70] Certainly, like I have only run maybe like one or two workshops ever.
[431.02 → 435.34] And that was the roadblock for me not doing it more is I feel like, okay, I want to help
[435.34 → 436.14] people learn.
[436.24 → 437.42] I want to distribute knowledge.
[437.56 → 439.50] But where do I even start?
[439.50 → 444.34] Well, the good news is at this point with sort of the lifespan of the Go community, there's
[444.34 → 446.50] a lot of content out there, right?
[446.82 → 449.50] When I started doing these workshops, it was a bit harder.
[449.78 → 455.06] There were basically a handful of blogs to sort of rely on and a handful of sorts of learning
[455.06 → 458.52] material, maybe one or two books that folks kept recommending.
[459.04 → 460.74] So it's gotten a lot easier, right?
[460.98 → 466.10] As folks sort of pickup Go, and they're sort of documenting their own journey with learning
[466.10 → 470.26] the certain aspects of Go, it's certainly gotten easier to sort of have a baseline, have a
[470.26 → 473.24] starting point for how you put together curriculum and material.
[473.24 → 480.00] But when I did, it was, and it may seem like to even sort of think about putting together
[480.00 → 484.34] a workshop and thinking about putting together a curriculum, that tends to be a very intimidating
[484.34 → 486.34] concept like to wrap your head around.
[486.50 → 490.74] Like the first time you do it, your imposter syndrome just kicks in hard, right?
[490.74 → 495.10] You're like, who am I to think I can teach other people, right?
[495.10 → 498.12] Like you're just completely like, you know, fear and panic.
[498.28 → 499.52] And then somehow you push through it.
[499.56 → 503.90] And if you have a support system and people that encourage you to sort of move forward
[503.90 → 505.14] and you kind of take advantage of that.
[505.22 → 509.72] But the thing for me was that I was on my own sort of journey of learning Go, right?
[509.76 → 513.32] It's not like I was already an expert in Go when I decided to do my first workshop.
[513.60 → 517.90] Like I was really no better than the person who spent, you know, maybe two or three months
[517.90 → 520.50] just, you know, playing around and go to the Go playground or something.
[520.64 → 522.20] I was no better, right?
[522.20 → 526.58] I knew a little bit more and that's all you really need as a Go or really like any language,
[526.70 → 528.02] anything you're trying to teach.
[528.44 → 532.42] If you spend just a couple of weeks learning something, you are going to be that much better
[532.42 → 535.02] than somebody who spent zero weeks learning something, right?
[535.06 → 539.30] Especially if you're targeting like, you know, beginners for a piece of technology, you are
[539.30 → 543.66] going to know just a little bit more, just enough to be able to say, hey, you who are just
[543.66 → 546.36] starting out and kind of confused, just like I was a couple of weeks ago.
[546.76 → 548.28] Let me show you what I've learned, right?
[548.28 → 552.82] So it's gotten easier, and it's supposed to get easier the more you do it, as with all
[552.82 → 553.66] things in life.
[553.92 → 556.48] But it's not, you don't just wake up one day like, you know what?
[556.52 → 557.32] I'm an expert now.
[557.38 → 558.34] Now I can teach, right?
[558.38 → 559.62] There's no such threshold.
[559.98 → 561.20] Yeah, I absolutely agree.
[561.42 → 566.12] Like for me, most of the workshops were I found something that I'm curious about.
[566.36 → 568.52] I dived right in.
[568.62 → 570.30] I did like all sorts of things with it.
[570.30 → 574.00] I made way more mistakes than many other people.
[575.56 → 579.12] And I just got really familiar with a specific niche.
[579.16 → 582.96] And then I started feeling more comfortable answering questions about this and then kind
[582.96 → 590.22] of putting into words the code behind what I built and then explaining the different parts
[590.22 → 590.56] of it.
[590.62 → 593.74] And this is really kind of a good foundation for what a workshop is.
[593.74 → 598.22] And I think the confidence of making all sorts of mistakes and just knowing that at least
[598.22 → 602.40] some of the questions that people will be asking you, you have experienced yourself and
[602.40 → 608.34] you kind of dealt with that while trying to figure out how to go about this is also helpful
[608.34 → 612.88] in feeling somewhat confident in going and saying, yeah, I can teach this.
[613.18 → 617.88] And in terms of actually like practically, like how do you start structuring it?
[617.94 → 622.90] Is it that you kind of, you get a Google doc up, you start writing notes, you get a slide
[622.90 → 623.42] deck up.
[623.50 → 625.40] I'd love to hear maybe from Anna.
[625.58 → 628.68] I mean, you're literally doing this right now, putting your talk together.
[628.94 → 630.24] How did you start that?
[630.40 → 632.60] Yeah, I started with the idea.
[632.98 → 637.44] And then I thought like, okay, security and ghost like a lot.
[637.44 → 646.30] Then I collected some ideas and Natalie organized also Roberto as a mentor on the idea for me.
[646.54 → 652.18] And I had a, I think, roughly 30-minute call with him where we talked about the ideas.
[652.90 → 659.26] And that was actually really great because he was like, yeah, I think this idea is too
[659.26 → 661.48] techie or too deep dive into it.
[661.72 → 663.84] And that's my experience from doing it.
[664.06 → 670.06] And then we discussed it and came up with kind of, I think a good idea.
[670.38 → 676.44] So I think that's important that you have a vision in mind that you know how your path
[676.44 → 676.94] is going.
[677.30 → 682.80] And now I'm in the state of researching a bit on what's there already.
[683.04 → 687.20] So which resources are there because I can't cover all.
[687.50 → 690.26] So I have to focus on some aspects.
[690.78 → 696.24] I'm currently doing my research on this to write up my slide deck.
[696.80 → 697.24] Awesome.
[697.62 → 698.60] I mean, I would love to hear.
[698.60 → 702.06] I know you talked about Natalie kind of pairing you up with a mentor.
[702.38 → 703.90] Maybe we can just take a step back.
[704.02 → 707.12] Natalie, I'd love to hear a little bit more about the great program you've been putting
[707.12 → 710.92] in place for people putting together workshops for Goodson Europe this year.
[711.10 → 711.36] Yeah.
[711.66 → 717.32] So it's always hard to come up with workshops for conferences as a conference organizer,
[717.50 → 719.30] not as a person who gives a workshop.
[719.30 → 726.48] And different conferences go about different ways in building their workshop offerings.
[726.88 → 731.32] I would say that most talks go about in the same path in the sense that there's a call
[731.32 → 736.26] for papers, people submit talks, there's a review committee, you have a rating, and then
[736.26 → 738.72] based on that, you pick and invite speakers.
[739.34 → 744.00] But for workshops, there is such a big variability of how to do this.
[744.08 → 746.96] I see some conferences just send out invites.
[746.96 → 752.68] Other conferences have sort of call for workshops, and some have something hybrid in between.
[753.06 → 758.68] This year, I wanted to do something that I have not done so far as an organizer of a conference,
[758.74 → 761.38] or as a person who's behind the scenes, not as a person who's giving the workshop.
[761.74 → 770.00] And I asked Johnny, and I asked Bill if they would agree to have a mentee who is a developer,
[770.38 → 775.96] but have not necessarily taught the workshop just yet, and give a workshop together.
[775.96 → 778.12] And it was a pretty open-end request.
[778.44 → 781.56] You can teach an existing workshop, you can build the workshops from scratch, whatever
[781.56 → 782.32] you find right.
[783.02 → 788.38] And Anna and her technical advisor, Roberto and Glottis, thank you very much for doing
[788.38 → 788.62] this.
[788.70 → 790.04] Here's a shout-out to you, Roberto.
[790.46 → 794.08] Anna is a PhD researcher in securities.
[794.34 → 800.18] I guess you get the support behind the stage, and not as two people teaching the workshop.
[800.18 → 806.06] But this is definitely a new format in Gofer Con Europe, and it's pretty exciting.
[806.56 → 806.70] Yeah.
[806.90 → 810.46] In about one and a half months, we'll see how the feedback is, and I'm sure it's going
[810.46 → 811.38] to be anywhere between.
[812.16 → 813.00] This is awesome, too.
[813.08 → 813.66] This is amazing.
[815.06 → 815.50] Nice.
[815.50 → 816.76] You mentioned Johnny.
[816.88 → 818.02] I mean, you're one of the mentors.
[818.76 → 823.90] What happens if you get paired with someone who comes to you bluntly with an idea that
[823.90 → 831.06] isn't fully formed, that is kind of hand-wavy, isn't feeling like a viable, I guess, workshop?
[831.26 → 832.48] Like, how do you coach them?
[832.58 → 837.48] How do you help them form that idea if they're not coming to the table with all the materials,
[837.58 → 839.04] all the ideas that you may have liked?
[839.04 → 843.90] Because, I mean, one of my thoughts is that my problem would be I'd come with just wanting
[843.90 → 848.34] to teach everything to everyone and just getting overexcited and, like, I want to teach everything
[848.34 → 851.78] about Go in an hour, and I can do that for sure.
[851.94 → 856.16] But I'm sure, like, there's the other side of the spectrum where you have people who really
[856.16 → 857.22] want to push themselves.
[857.36 → 858.34] They want to give a workshop.
[858.54 → 859.22] They want to grow.
[859.72 → 867.00] But maybe they are like, oh, I only feel comfortable, perhaps, talking about a few concepts.
[867.00 → 870.72] How do you kind of keep them in their comfort level but also encourage them to, I guess,
[870.78 → 871.26] stretch?
[871.48 → 875.50] Actually, I should take a step back and say thank you to Natalie for sort of coming up
[875.50 → 875.94] with this idea.
[876.02 → 879.76] I think it's an excellent way of creating more bandwidth within the community, right,
[879.80 → 881.02] for people who can teach.
[881.22 → 885.56] And I don't think it's going to be a surprise if you, you know, go online and start searching
[885.56 → 887.44] around for who teaches you around the community.
[887.54 → 889.68] You're going to see the same set of people coming up over and over again.
[890.60 → 892.26] But for better, for worse, I might be one of them.
[892.26 → 897.34] The thing is, we can't sort of rely on just a handful of people to do all the teaching,
[897.54 → 897.70] right?
[898.14 → 899.02] That's not going to scale.
[899.36 → 901.04] And frankly, we need more.
[901.66 → 903.24] We need a diverse representation of teachers.
[903.40 → 906.80] So one of the things, and this is the sort of small tangent, and I'll come back to your
[906.80 → 907.06] question.
[907.24 → 911.70] One of the things that has always sort of bothered me, right, as my day job is as an
[911.70 → 915.00] SRE, but, you know, I do professional training on the side.
[915.12 → 918.54] So one of the things that has always bothered me within that training industry, technology
[918.54 → 923.24] training industry in particular, is that there are so few people who look like me, right?
[923.28 → 929.16] So that bothers me every time I go on PACT or Riley or wherever, and I see the portfolio
[929.16 → 930.56] of trainings happening.
[930.88 → 935.66] And it's like, there's maybe one or two, right, out of, you know, 50 or 100 trainers, right?
[936.18 → 938.54] Professionals who've been doing this for a while and happen to be teaching.
[938.98 → 940.86] There's just one or two faces, right?
[941.12 → 942.08] People who look like me.
[942.18 → 945.64] So even when I get tired, I'm like, oh man, should I retire from training, right?
[945.64 → 948.52] Like, you know, like I've taught, you know, same material over and over again.
[948.78 → 951.94] Part of the joy of teaching the material was because I was learning it at the same time,
[951.98 → 952.14] right?
[952.18 → 956.38] So now I've sort of moved that set of material that I'd like to pursue other things.
[956.50 → 960.34] And then every time I do that, and I go and look at those pages, and I'm like, I can't,
[960.40 → 961.98] you know, we need more people, right?
[961.98 → 964.90] We need the next generation, right, to start coming in.
[965.26 → 969.70] And the best way to do that is to help grow these people, right?
[969.70 → 973.70] They're not going to be just, you know, just show up one day.
[974.08 → 977.52] We have to take an active role in sort of developing and growing these people.
[977.68 → 978.46] So Natalie, thank you.
[978.58 → 979.34] Big shout out to you.
[979.60 → 980.64] I think it's an excellent idea.
[980.80 → 984.96] And I really, really hope it succeeds beyond the Go4Con EU conference.
[985.50 → 989.68] Now, to answer your question more specifically, when someone comes to you and says, well,
[989.96 → 991.74] I really want to teach this particular subject, right?
[991.82 → 995.86] And as you inferred, the idea may need a bit more sort of developing.
[995.86 → 1000.22] It may need a bit more sort of padding, if you will, sort of adding some of the missing pieces, right?
[1000.40 → 1006.10] The biggest thing you can do as sort of mentor is to take the idea and sort of develop it, right?
[1006.18 → 1011.88] Sort of provide the handsets, well, have you thought about if you're sitting down for the first time and doing this?
[1011.96 → 1017.02] Or maybe if you've been doing this for a little while, I might make this more interesting for somebody who's not a complete newbie,
[1017.16 → 1021.60] but, you know, wants to, you know, maybe you get them to think about your particular problem differently, right?
[1021.60 → 1027.66] But if you are a complete newbie, how am I sort of approaching this, you know, when I sit down, how am I going to think through this?
[1027.72 → 1031.26] Because if you yourself happen to be a newbie, you're going to have a very different perspective, right,
[1031.28 → 1035.76] than somebody who's on the other side and has been, you know, maybe playing around with the language for a while, right?
[1035.92 → 1040.40] So it's about giving enough context to that individual to say, hey, you know what?
[1040.72 → 1044.06] In your workshops, very rarely will you have everybody who's at the same exact level.
[1044.14 → 1045.68] I've done this many, many times.
[1045.68 → 1052.54] Sometimes no workshop has, you know, the same level of sort of competence for people coming in for a given piece of technology.
[1052.68 → 1054.42] You might have some people who know a little bit more.
[1055.04 → 1062.36] You might have people who know a lot, and it just showed up just because that's the only block of time they could carve out to come do some practicing, you know,
[1062.40 → 1063.96] but they already know some of the material.
[1064.38 → 1066.24] You might have people who are complete newbies.
[1066.44 → 1068.16] You know, you tell them, you know, open up your shell.
[1068.30 → 1070.32] They look at you, you know, with a blank stare.
[1070.40 → 1070.94] What's a shell?
[1071.20 → 1071.72] Things like that.
[1071.72 → 1081.10] So you have to be able to somehow make the material sort of accessible enough, make it interesting enough that if you are a newbie, it's not overwhelming, right?
[1081.16 → 1088.38] That when you leave that workshop, you're not going to just forget about it because it was, you know, it confirms your suspicion that it was way too complicated, and it's not for you, right?
[1088.42 → 1089.42] You want to avoid that.
[1089.76 → 1091.80] But at the same time, you make it somewhat interesting enough.
[1091.80 → 1096.68] And for somebody who's not a complete beginner to still find joy in the workshop.
[1097.10 → 1102.68] And a lot of times, you know, you end up sort of making these people sort of impromptu TAS in your workshops as well, right?
[1103.06 → 1111.10] So it's about basically, and what I usually tell sort of a new trainer is to basically say, hey, have multiple levels to your material, for example, right?
[1111.10 → 1115.58] So what I really enjoy doing in my material is to basically say, you know, start out with one idea, right?
[1115.66 → 1120.26] And I keep layering on some sophistication to the idea, right, as we go, right?
[1120.26 → 1124.30] So it's the same idea, basically the same thread you're pulling on throughout the entire workshop.
[1124.46 → 1127.12] And then we just keep adding some complexity to it, right?
[1127.36 → 1133.34] Some necessary complexity to it in some ways to actually solve those more complex problems, you know, as we go through the workshop.
[1133.34 → 1139.60] That way, it's the same idea that you're sticking to, you know, you're not sort of, you know, expanding a new domain every time you go do a different exercise, right?
[1139.68 → 1147.30] But that increasing complexity allows somebody whose brand new to be able to, you know, spend time in the sort of lower tiers as they sort of wrap their heads around things.
[1147.30 → 1151.68] And for those who are a bit more experienced, they can go ahead and sort of keep climbing the ladder, right?
[1151.68 → 1153.80] To get to the more complicated and more interesting stuff, right?
[1154.10 → 1155.42] Providing that context, right?
[1155.60 → 1160.10] Of, hey, basically, hey, hey, there's going to be a lot of different folks live with different skill sets in your workshops.
[1160.36 → 1163.22] You got to try to give each of them a little something, right?
[1163.26 → 1164.72] It's one of the core things that I try to teach.
[1164.94 → 1167.70] I mean, off the back of that, I'd love to hear from you, Jonas.
[1167.70 → 1179.08] I know you've taught a lot of different workshops to a lot of different levels from, like, as I mentioned, like, intro to go, the absolute people are walking into this room, have no idea what go is, all the way up to more intermediate, etc.
[1179.22 → 1181.84] And I'd love to hear how, well, two things.
[1181.94 → 1185.84] One, how do you think about what to include per level?
[1185.84 → 1203.86] And secondly, how do you kind of make sure that even though you might say, okay, this is an intermediate or this is a beginner, kind of to what Johnny said, you give everyone enough of a challenge, but also not pushing them too far that they then disengage and go, oh, no, this is too difficult.
[1204.20 → 1205.94] Like, I can't do this.
[1206.16 → 1209.52] It's a good question because it's something always fine-tuning, I think.
[1210.06 → 1212.88] So the first thing I do really think about is my audience.
[1212.88 → 1214.16] I try to be really mindful.
[1214.16 → 1221.14] You know, it will depend on am I doing this workshop through a business or through a Golang meetup?
[1221.24 → 1224.00] You know, you'll have kind of different perspectives coming from that audience.
[1224.12 → 1229.44] And so usually I might try to then cater what I focus on or what I emphasize based on that audience a little bit.
[1229.60 → 1239.82] For example, when I do intros that are more focused on people who are learning programming generally, right, I focus maybe less on why you should use Go and Go is so cool.
[1239.82 → 1242.86] Like, I'm more about using Go to help you understand programming.
[1242.86 → 1244.88] And then I'll kind of note some of the cool things about Go.
[1244.98 → 1249.76] But I want to like, I want you to understand programming first before I convince you that Go is the best language.
[1249.98 → 1259.78] And, you know, and I also try to really focus on whatever level I want to make sure people are leaving, feeling like they've spent time in that workshop, you know, getting enough hands-on experience that they can then take it forward.
[1259.78 → 1263.66] So I think kind of to what Johnny was saying, you know, build on with each exercise.
[1263.94 → 1268.08] You're always going to start a little simple, you know, and even if you have a more advanced, like they'll keep going.
[1268.20 → 1270.76] But I always want to make sure everything should build and feel cohesive.
[1271.24 → 1275.22] That's the main thing I find is like I want everything to kind of connect in the exercises.
[1275.22 → 1284.08] They shouldn't feel just kind of like here's one exercise and here's a totally unrelated one because I think that helps create the flow for even if you're at different levels, you kind of see how it all comes together at the end.
[1284.20 → 1284.70] That's the goal.
[1284.84 → 1286.66] It should be a nice little package at the end.
[1287.02 → 1298.54] And then even just, you know, with the various exercise and hands-on things, I do try to provide different options to pursue so that you'll emphasize it's a beginner workshop, and you're going to get someone there who's like, oh, yeah, I've got this Go server running, you know.
[1298.54 → 1309.40] And so like I try to provide a mix of, you know, oh, if you finish this quickly, try this just so that also there's different ways people can engage because it's hard to get just one kind of skill or expectation in your group.
[1309.40 → 1318.86] And then turning to kind of how workshops have changed since we went into this kind of weird remote world.
[1318.86 → 1333.58] I know we've always had virtual workshops, but I would love to hear from both those who are kind of stepping into doing workshops in the more recent times versus like those like, you know, Johnny Jonas who've been doing them for, you know, many, many years.
[1334.12 → 1348.16] Have you seen a change in kind of the way that you would approach remote workshops, both in terms of live versus remote, but also like remote workshops in normal times versus remote workshops now when people are staring at their screens?
[1348.16 → 1357.80] Like most of the time, like most of the time, is there an adjustment kind of acknowledgement that maybe they need more breaks or, or kind of you need to, I guess, change it up even more?
[1357.80 → 1362.68] Maybe, I know, Natalie or Anna, as you're thinking through your workshop, Anna, maybe?
[1362.98 → 1366.36] That's actually, I got one from attendee perspective.
[1366.76 → 1374.56] I realized that workshops can be much better digital if you have a good speaker.
[1374.56 → 1375.56] Yeah.
[1375.56 → 1383.08] Because you can really use the digital material in the sense that you can make stuff interactive and give breaks.
[1383.58 → 1384.90] But that's really challenging.
[1385.44 → 1389.28] Having said that, I think that's also one of the biggest challenge.
[1389.56 → 1398.00] You have to take into account that you, that you split up your material and make it interactive because you can't go easily to the people.
[1398.00 → 1403.98] And you have to clearly know how to interact with them, where to ask.
[1404.08 → 1405.62] I agree with Anna very much, yeah.
[1406.14 → 1418.24] My experience as a person who gave more in-person workshops and several virtual workshops too, I would say that this, like you need to be more engaging.
[1418.72 → 1424.72] There is something about the energy in the room, which is not the same when it's virtual, and it's very hard to reproduce.
[1424.72 → 1427.44] So it's a lot more on you as the instructor.
[1428.14 → 1434.84] It's also a lot more on the attendee in the sense of when you are in the room, when you're in a physical workshop as an attendee.
[1435.28 → 1443.74] I, as an instructor, can see how many roughly, like, is half the room understanding what I'm doing and half thinking this is too fast or too boring?
[1444.20 → 1445.52] Is it a different split?
[1445.60 → 1446.48] Is everybody bored?
[1446.62 → 1450.12] Is everybody like, oh my God, how did you reach this point?
[1450.12 → 1450.74] And so on.
[1451.04 → 1460.80] When it's virtual and everybody have the video off, the camera off, and maybe, like, two people have a picture, which is static anyway, you have no means of reading the room.
[1461.00 → 1464.94] So it's on you to ask more questions, to give more pauses.
[1464.94 → 1475.54] Also more breaks in the sense that in a physical workshop, it would always be, let's say, three, four, five hours and maybe one or two breaks in between.
[1475.92 → 1481.94] And in virtual workshops, every round hour, you would give 10, 15 minutes because it's impossible otherwise.
[1483.34 → 1487.48] Because that energy is not there, you have to compensate for this means.
[1487.48 → 1493.84] And also having a teaching assistant becomes a completely different type of help that you need.
[1494.80 → 1502.96] And in a virtual workshop or in a physical workshop, it would be you explain something or say, now we exercise this, you leave the thing running on the screen.
[1503.10 → 1506.96] And then you and the teaching assistant go between the crowd and answer all the different questions.
[1507.84 → 1513.10] And you have the option to approach each person one by one, look at their screen together and kind of understand what's going on.
[1513.10 → 1520.46] In a virtual one, you have teaching assistants that people usually for some reason are shy to ask for help.
[1521.34 → 1529.62] And then there's always the two, three people who are very active and very understanding and everything and give you good feedback, but they don't represent the crowd.
[1529.72 → 1531.94] And it's very easy to engage with them and forget that.
[1532.46 → 1539.48] And then there's other two, three people who are very good at giving feedback that they don't know what you're like, where they don't give up with you.
[1539.48 → 1542.72] But they also don't represent the crowd, but they can easily take up your resources.
[1542.72 → 1547.80] And then finding a way to balance all that is another extra work for you as an instructor.
[1547.98 → 1553.30] And then between all that, also try to make sure you meet the time and also keep your cat quiet.
[1553.48 → 1555.48] This is becoming like a whole show.
[1556.48 → 1560.76] Let me tell you, I miss face-to-face workshops.
[1560.76 → 1578.22] I really, really do, because I can't tell you how many times I will introduce a concept and then know how fast to move on, how slow to sort of how to pace myself, how to know when everybody's ready to move on, when nobody's ready to move on.
[1578.30 → 1583.78] As a teacher, you can look at people's faces in the crowd and see who's getting it and who's not.
[1583.78 → 1584.14] Right?
[1584.60 → 1587.82] Like, you can get those physical cues, nonverbal cues.
[1587.98 → 1592.94] Oh, man, they are gold to a teacher because they help you, right, with pacing.
[1593.12 → 1598.22] They help you with sort of knowing that, okay, did this metaphor I just used, did that make sense at all?
[1598.28 → 1602.52] Or do I need to really stick to something simpler or whatever, right?
[1602.52 → 1606.56] So a lot of those cues that you just lose those in an online context.
[1606.84 → 1623.94] And let me tell you, like Natalie's saying, when you do it online and folks a lot of times have their videos off, right, especially if you have a sort of multi-hour, you know, four, five, six, you know, God forbid, an hour, like an eight-hour-long sort of full-day thing, you should expect people to sort of tune in and out.
[1623.94 → 1629.64] Because, you know, yes, they might be in your class for that amount of time, but life's still going on, right?
[1629.70 → 1637.04] They're still getting pinged and buzzed and emailed and, you know, maybe there's a boss asking for something, and they can't, you know, wait till later or whatever the case may be.
[1637.12 → 1639.70] Maybe you have children, you know, pulling on your leg or whatever.
[1640.12 → 1642.30] I mean, things happen, right, in the real world.
[1642.44 → 1651.74] And as a trainer, you kind of, one, be aware of these things and also sort of be willing to sort of change your style a little bit as you go, right?
[1651.74 → 1655.30] So, you know, again, having more questions, you know, keeping people engaged.
[1655.70 → 1662.14] I mean, sitting around, sitting at your desk for eight hours straight, you know, with some breaks in between, that gets tiring very quickly.
[1662.58 → 1668.00] So you have to find a way to keep them engaged, whether it's through questions and whether it's actually letting them do some of the work.
[1668.34 → 1677.72] Like one of the things that really sort of bothers me in terms of training is that if you have somebody sort of talking, you know, at you for eight hours straight, right, you know, minus breaks, whatever it is,
[1677.72 → 1688.04] I need to be able to actually hear what you're saying, see you, show me some examples, and then for me to actually try something, right, using the knowledge you just gave me, right?
[1688.32 → 1696.02] Because otherwise, this might as well be a recording, right, that I can play, pause, whatever, whenever I want, right, and do it at my own time, my own pacing, right?
[1696.24 → 1700.80] And I can find my own exercises if there's not going to be any time for exercising, you know, during a workshop.
[1700.80 → 1712.44] One of the major benefits of actually having a live instructor, right, be it online or face-to-face, one of the key advantages is that you can ask them questions in real time when you don't understand something, right?
[1712.80 → 1721.82] So if it's a video, you can pause it, and then you have to go on your own, and, you know, your specifics might take you a long time to find answers for your specifics.
[1721.82 → 1731.66] But in a live training, you know, you get to ask your specific question, and then the instructor then tells you, well, maybe you're being too specific, you know, think about it this way instead.
[1731.80 → 1734.50] Or, yes, there's an answer to your specific, you know, problem, right?
[1734.62 → 1737.84] So these things, you should take advantage of those things if you happen to be a student.
[1738.02 → 1742.64] But, yeah, to bring it back around, the whole pandemic thing, I can't wait for that to be over, man.
[1742.82 → 1749.06] I need to get back into the classroom looking at people in the face, you know, so I can actually enjoy this again.
[1751.82 → 1768.88] This episode is brought to you by Source graph.
[1769.40 → 1773.84] Source graph is universal code search to let you move fast, even in big code bases.
[1774.34 → 1781.08] Here's CTO and co-founder, Bung Lu, explaining how Source graph helps you to get into that ideal state of flow in coding.
[1781.08 → 1786.30] The ideal state of software development is really being in that state of flow.
[1786.52 → 1796.60] It's that state where all the relevant context information that you need to build whatever feature or bug that you're focused on building or fixing at the moment, that's all readily available.
[1796.78 → 1802.16] Now, the question is, how do you get into that state where, you know, you don't know anything about the code necessarily that you're going to modify?
[1802.16 → 1804.84] That's where Source graph comes in.
[1805.04 → 1808.16] And so what you do with Source graph is you jump into Source graph.
[1808.28 → 1811.60] It provides a single portal into that universal code.
[1811.88 → 1815.26] You search for the string literal, the pattern, whatever it is you're looking for.
[1815.34 → 1818.32] You dive right into the specific part of code that you want to understand.
[1818.76 → 1821.04] And then you have all these code navigation capabilities.
[1821.18 → 1831.56] Jump to definition, find references that work across repository boundaries that work without having to clone the code to your local machine and set up and mess around with editor config and all that.
[1831.56 → 1837.02] Everything is just designed to be seamless and to aid in that task of, you know, code spelunking or source diving.
[1837.34 → 1845.20] And once you've acquired that understanding, then you can hop back in your editor, dive right back into that flow state of, hey, all the information I need is readily accessible.
[1845.44 → 1849.92] Let me just focus on writing the code that influenced the feature or fixes the bug that I'm working on.
[1850.20 → 1850.52] All right.
[1850.56 → 1852.40] Learn more at Sourcegraph.com.
[1852.50 → 1860.50] And also check out their bi-monthly virtual series called DevToolTime, covering all things DevTools at Sourcegraph.com slash DevToolTime.
[1861.56 → 1885.50] Aside from kind of needing to juggle a million and two things, as Natalie said, I'd love to hear whether those of you who have done kind of workshops pre-pandemic, post-pandemic, now fully remote.
[1885.50 → 1893.06] So when you're planning out your workshop, is there a kind of thought put into, putting in like social aspects to it?
[1893.12 → 1897.16] I do a maybe if it's a smaller workshop, an icebreaker at the beginning.
[1897.26 → 1898.86] Hey, everyone introduce themselves.
[1898.86 → 1914.16] Because certainly as someone who loved going to workshops in person, one of the core benefits was I just met so many awesome, amazing people that I could form connections with, learn from through, you know, after the workshop, just honestly just make friends.
[1914.16 → 1920.14] And I'm interested in that, if that's a consideration when you're planning out a remote workshop.
[1920.54 → 1921.68] Is that important?
[1921.96 → 1925.38] Do you feel like you can't really do that in a remote setting?
[1925.70 → 1927.80] Or if you can, how do you do that?
[1928.06 → 1934.42] I mean, if I was planning a workshop, I would just probably get everyone chatting the whole time and not end up getting to the materials.
[1935.36 → 1936.06] I don't know.
[1936.16 → 1938.44] Jonas, is there something you might, you put thought into?
[1938.44 → 1941.62] Yeah, you know, and I'm trying to think back on some remote things.
[1941.76 → 1948.64] I mean, certainly leveraging like the breakout functionalities in these tools is a nice tool.
[1948.74 → 1954.30] Honestly, it's kind of maybe one of the benefits of having remote is you can use those.
[1954.46 → 1963.64] And I sometimes found too, if you have like a cohesive breakout group that you're with throughout the whole training, so you're kind of going back and checking in with the same people, that can be kind of nice.
[1963.64 → 1972.26] And trying to keep up where I've set up like a Slack channel too, so that we're, one, I think a bit to Johnny's point is like you can share updates and the resources you go.
[1972.42 → 1974.74] So if people are jumping in and out, they can kind of catch up.
[1974.96 → 1981.20] But then also it's a space where everyone can just be to chat after or catch up or connect through that means as well.
[1981.38 → 1984.10] So I guess just trying to use all the different tools available.
[1984.42 → 1990.50] In some ways, I just try to think of like what's every technical option I can leverage and let's throw it out there and then see what sticks.
[1990.50 → 1995.34] I think you can also use like nice icebreakers in the beginning.
[1995.64 → 2000.54] I have seen that also already with like putting a needle from where you are.
[2000.72 → 2008.08] Like there was a map and a tool, and you should simply draw a circle or something and put your name next to it or something like this.
[2008.58 → 2014.40] That's something funny or like simple questions you have like, who is a cat lover?
[2014.40 → 2022.98] Or yes, no or something such that you have like a state, you have something to love, and you break the ice a bit.
[2023.62 → 2031.98] I think that's also something you can do digital as well as remote, not remote, analog in person.
[2032.40 → 2033.64] I think that's valuable.
[2034.30 → 2037.86] Having said that, it also depends highly on the attendees.
[2037.86 → 2049.96] I had one lecture and I tried things and I struggled so much because I found it much more difficult to make stuff interactive digital than doing it in person.
[2050.30 → 2053.02] So I felt like, yeah, what should I throw all at you?
[2053.42 → 2055.10] I want to have some interaction.
[2055.84 → 2058.42] That's also something which is really cool.
[2058.56 → 2062.92] But as mentioned before, people have to engage with it.
[2062.92 → 2070.94] And I think it's much easier to be someone on numerous digital now, especially as a lot of people turn their cameras off.
[2071.18 → 2079.28] What I think is not the coolest thing to do, especially in a workshop like this, because in person you would also see each other.
[2080.04 → 2086.04] And a face tells so much, which you can't get only by seeing.
[2086.04 → 2092.46] And if I don't have the camera on, I could also look at a recording or something like this if I don't engage.
[2093.02 → 2096.28] So what's the benefit of attending a live workshop then?
[2097.16 → 2098.86] But that's only my opinion.
[2099.52 → 2100.06] No, for sure.
[2100.44 → 2105.36] I would love to hear, how do you keep your, I mean, it kind of goes to two parts.
[2105.44 → 2111.80] From the veterans who have done a lot of workshops, how do you keep your material fresh and fun and engaging?
[2111.80 → 2116.64] And for those who kind of are newer to the space, how do you think about keeping them entertained?
[2116.76 → 2118.88] I mean, is it like trying to do call-outs?
[2118.98 → 2120.22] Is it telling jokes?
[2120.40 → 2122.88] Is it having interesting analogies?
[2123.02 → 2130.24] I've done a few workshops where I've tried to crack a joke or do like a clever analogy, and it's fallen so flat.
[2131.12 → 2134.32] Everyone's faces, virtual faces were blank.
[2134.32 → 2141.16] Just like, and I don't know whether they just couldn't understand what I was saying or I just, it was a terrible analogy.
[2141.82 → 2142.94] They were laughing on the inside.
[2144.48 → 2147.46] I know, Johnny, you use a lot of analogies.
[2147.62 → 2149.16] Is there a time that it fell flat?
[2149.50 → 2150.08] Oh, absolutely.
[2150.28 → 2157.68] I mean, it's one of those things where over time you sort of find out what works and what works for you, right?
[2157.68 → 2164.90] So I've tried, you know, picking up, you know, random, you know, jokes here and there, but because they didn't come from my life, right?
[2164.92 → 2179.44] They didn't come from my experiences, you know, when I'd tell them, even though I'd find them amusing, people, you know, because the delivery ended up somehow the authenticity of it, you know, because it wasn't my story that I was telling.
[2179.58 → 2180.34] It was missed.
[2180.34 → 2184.94] And I learned very quickly, people can always tell when you're being authentic, right?
[2185.14 → 2188.24] At least they can tell when you're being fake and not completely honest, right?
[2188.42 → 2195.02] These things, like you learn them the hard way and you sort of, you know, for the next one, you try to do better, right?
[2195.08 → 2203.92] One of the sort of the things that I really had to stop doing in my teaching career, if you will, is to basically beat myself up for the last training, right?
[2203.92 → 2209.52] I'm like, oh, I didn't get to teach that thing, or I hated the way I explained this particular thing.
[2209.52 → 2212.72] Like everything else, you get better with it over time, right?
[2212.74 → 2225.68] Like I love analogies, especially like cooking analogies, you know, like I used to use that, you know, how programming is like, you know, cooking, and you have recipes and, you know, you can call methods and pass in recipe, you know, ingredients to, you know, bake a cake, whatever.
[2225.92 → 2230.28] Like I use these things because during that time, right, I was learning how to cook.
[2230.28 → 2236.28] So I found a way to sort of incorporate my real life experience into what I was teaching, right?
[2236.28 → 2241.70] So those deliveries was authentic and people laughed, they could relate, right?
[2242.00 → 2249.90] So these things like you have to somehow tie real things that happened to you, right, to your material in some way to liven it up, to bring it alive.
[2249.98 → 2254.00] And you may not realize like how much of an impact that has, right?
[2254.00 → 2259.04] Trying to tell somebody else's story, you know, tell somebody else's joke is a lot of times is going to fall flat, right?
[2259.04 → 2260.50] So you got to own it.
[2260.56 → 2263.26] You got to own your stuff, own you really.
[2263.62 → 2266.90] Like a lot of it is you're giving so much of yourself as a teacher.
[2267.14 → 2278.68] Oh, the other thing, and I hope we get to this, like teaching other people, like especially if you are somewhat of an introvert, and you may not be able to tell, but I really love being by myself, right?
[2278.68 → 2293.32] Like right now I'm being all open and chatting and, you know, like it's very easy sort of to think that, you know, folks need to be like an extrovert to be able to put yourself out there to teach and to, you know, even to talk at conferences or meetups, whatever it is.
[2293.70 → 2298.00] Like people can be very, very hard to sort of step out of yourself to do that because of that fear, right?
[2298.00 → 2300.74] You always fear that, oh, man, I'm going to stand in front of all these people, right?
[2300.80 → 2305.98] Like, again, like it's very hard to do that, but you don't have to be an extrovert to be a teacher, right?
[2305.98 → 2308.40] That's something that, again, you can train yourself out of.
[2308.54 → 2310.58] But again, anyway, I'm starting to ramble now.
[2312.02 → 2312.68] No, for sure.
[2312.74 → 2318.80] I'd love to hear, Natalie, when you're thinking about how to kind of keep your participants engaged, are you cracking jokes?
[2318.90 → 2320.24] Are you whipping out the analogies?
[2320.34 → 2323.00] How do you keep your participants engaged and excited?
[2323.00 → 2329.20] My ultimate tool, when all else fails, I say, please ask me a question so I can move on.
[2329.52 → 2329.96] Okay.
[2330.20 → 2333.18] And then somebody feels brave enough to ask something.
[2333.18 → 2336.90] And then finally the secret comes out that, oh, I also didn't understand.
[2337.02 → 2337.98] Oh, I also didn't understand.
[2338.06 → 2339.22] And I also didn't understand.
[2339.52 → 2346.56] So this is always like a good question to keep in the toolkit, but probably also good not to use it too much.
[2347.02 → 2347.36] Yeah.
[2347.62 → 2352.68] I try to ask people to keep the cameras on as much as possible.
[2353.08 → 2357.24] I also ask people to keep the videos, to keep the audio on.
[2357.24 → 2362.44] And I encourage people not to just type their question, but also to unmute themselves and to ask them.
[2362.96 → 2370.94] If I have a teaching assistant, I would also say, so if you would like, I can read your question or the teaching assistant can read your question.
[2370.94 → 2377.22] But maybe the person who posted this question, you would like to unmute yourself and then kind of develop a bit of a conversation.
[2377.22 → 2389.48] And I think there is, it's hard to reproduce this peer pressure that is there, that is present in an in-person workshop, right?
[2389.52 → 2396.32] In an in-person workshop, if I tell a joke, somebody laughs because they're polite and then everybody else laughs because, well, people are laughing.
[2396.32 → 2400.96] But when everybody's silent, then it's like I told a joke and maybe one person laughs.
[2401.16 → 2403.30] Nobody gives you this feedback and this acknowledgement.
[2403.96 → 2408.20] Also reminding yourself that, well, at least statistically, at least one person laughs.
[2408.30 → 2409.48] So that joke was okay.
[2410.70 → 2413.36] And this is kind of a few things from the toolkit.
[2414.46 → 2415.48] I'm kind of touching on that.
[2415.54 → 2426.18] I'd love to, because we haven't chatted about it yet, the value of TAS and the fact that like how you can use your TAS to really add to that workshop experience for their participants.
[2426.60 → 2430.46] Johnny, really anyone wants to jump in on how you think about TAS.
[2430.64 → 2433.76] I can jump in, and I really want to hear some of the perspectives as well.
[2434.10 → 2441.04] The reason why I want to jump in is that I think, or at least I'm hoping in my head that all of you will have had the same experience.
[2441.26 → 2446.64] I was a TA before I was a teacher because I was too afraid to actually be the one doing the teaching.
[2447.08 → 2453.24] So, you know, I found at the time I was in Boston, and we had lots of Rails bridge workshops going on.
[2453.40 → 2455.70] And I was doing a ton of Ruby and Rails at the time.
[2455.70 → 2464.26] And I was like, okay, like I know I don't know enough or, well, I knew about the technology, but I didn't know about teaching.
[2464.40 → 2466.70] The two are very, very different things, right?
[2466.78 → 2469.68] Just because you know a technical subject doesn't mean you can teach it.
[2469.78 → 2471.62] Those are very different skill sets, right?
[2471.62 → 2477.58] So I was, you know, self-aware enough to realize, okay, I'm not in a place where I can actually do the delivery of the material.
[2478.30 → 2480.82] There are others who can do that job way better than I can.
[2481.00 → 2482.68] But I can help in other ways.
[2482.76 → 2487.62] I can be in the room, help somebody, you know, figure it out while hopefully not touching their keyboards.
[2487.76 → 2488.44] That's a side note.
[2489.02 → 2490.84] TAS don't touch other people's keyboards.
[2490.84 → 2495.80] That's even more so now, you know, pandemic times, you know, after we're done with this.
[2495.92 → 2499.22] But, you know, even before then, you didn't touch people's keyboards for a different reason, right?
[2499.24 → 2502.26] You know, because if you take that power from them, they're not going to learn as much, right?
[2502.26 → 2503.28] So don't touch people's keyboards.
[2503.90 → 2512.24] Anyway, you know, as a TA, I was like, okay, that's the way for me to sort of immerse myself, expose myself, right?
[2512.24 → 2519.06] And really, like, when you're that up close and personal with somebody who's learning something for the first time, you get to see their struggles.
[2519.26 → 2521.30] You get to see how they struggle, right?
[2521.52 → 2529.24] And then now when it's your turn to teach, because you've been a TA, you know, half a dozen times, you know exactly where the common pain points are.
[2529.36 → 2530.68] You know exactly where they get stuck.
[2530.80 → 2537.52] You know exactly, you know, when somebody up there, you know, at the lectern says something that they think makes sense to them, right?
[2537.52 → 2544.02] Because maybe, you know, they're a little bit more advanced, so, you know, they mention a word, and they think everybody knows what that word is, right?
[2544.40 → 2549.22] You know, I've had students, like, turn around, look at me and says, what did he just say?
[2550.50 → 2562.52] You know, so now we sit down, and I start sort of decomposing what that means, sort of, you know, unpacking, right, all that prerequisite knowledge that, you know, whoever's up there, you know, teaching the subject didn't realize it, they needed to convey, right?
[2562.62 → 2565.40] So now I'm sitting down as a TA sort of explaining some of these things, right?
[2565.40 → 2574.42] So that experience, right, there was invaluable in helping me understand what it is like to actually be, you know, a good sort of conveyor of information.
[2574.92 → 2578.70] Yeah, and I'll just add to that point, like, your TAS, they're your eyes and ears, like, they're so helpful.
[2578.80 → 2588.34] As an instructor, you have so much, I mean, it's stressful, you're trying to balance, like, your slides and you're talking and your exercises and your TAS are really going to help you get that real read on the room.
[2588.44 → 2593.68] Like, you're trying to read the room, but the TAS are, like, right there, and they're letting you know, kind of, where are people getting stuck?
[2593.68 → 2598.64] Slow down, like, you know, and they can help be a bit of an advocate too for that and give you that check.
[2598.80 → 2600.34] So they're a huge resource.
[2600.46 → 2610.24] And I think especially, you know, if maybe you're new, or you're nervous about doing it, like, get TAS and get that help because they're just going to make everything a little less stressful when you're trying to teach.
[2610.64 → 2611.82] And they're good sources of feedback.
[2611.94 → 2614.32] I always try to get feedback from TA sat the end as well.
[2614.44 → 2616.16] You know, they can usually give you some good insight.
[2616.16 → 2622.66] And I always encourage them to kind of jump in as needed too if they might notice that I'm saying something that no one is getting.
[2623.22 → 2624.80] And maybe I don't notice it.
[2624.88 → 2629.56] So I encourage them, like, please step up and add more illustrations or something if I'm failing.
[2629.90 → 2636.22] And I think to points before, I've definitely adopted things from TAS, right, who I've been like, oh, they explained that so well.
[2636.22 → 2637.62] I'm going to use that moving forward.
[2637.86 → 2641.36] So it's an invaluable resource for, you know, someone who's leading a workshop.
[2641.36 → 2649.60] So as a person who's not native in English, as you might have noticed by my accent, a teaching assistant is a term that I first learned in university.
[2649.60 → 2654.90] And this was somebody who was kind of giving classes about whatever the professor was teaching.
[2654.90 → 2662.70] So the teaching assistant was teaching kind of the hands-on or even kind of workshop equivalent to what the professor was theoretically teaching.
[2663.16 → 2670.76] But then when I started teaching workshops, I learned that teaching assistant in this context means something pretty different.
[2670.76 → 2675.00] And this is somebody who has some technical knowledge, like my docker will not run.
[2675.34 → 2676.86] I don't know what this error means.
[2677.20 → 2682.46] But it's not necessarily somebody who's as experienced as you are in the content.
[2682.62 → 2687.08] It's not necessarily somebody who's able to answer questions, all of them, like maybe some yes.
[2687.18 → 2695.60] But many times it would be a person who has more housekeeping duties, let's say, than I, in the beginning, expected from a teaching assistant to have.
[2695.60 → 2700.92] And so in the sense of this is a person who would tell you, hey, this is time to pause.
[2701.36 → 2703.24] Many people are asking you questions.
[2703.62 → 2706.40] You are on mute to this level also.
[2706.80 → 2712.56] And just worth pointing out, I guess, that teaching assistant is such a context-rich word for me.
[2712.56 → 2721.36] And definitely valuable because we talked about this, but reading the room when you're in virtual versus in person is very different.
[2721.42 → 2725.28] And you definitely need a second pair of virtual eyes on your virtual crowd.
[2725.44 → 2732.54] And that's like an extra duty for the teaching assistant, which is also different for a teaching assistant from in person versus to a virtual workshop.
[2732.54 → 2737.16] So is there a perfect equation of teaching assistant to participant?
[2737.62 → 2741.92] Because personally, as an attendee, I would love my own one-on-one TA.
[2742.94 → 2747.38] But I wonder if too many TAS is too many cooks in the kitchen, as it were.
[2747.66 → 2750.06] You're asking what would be an ideal ratio?
[2750.50 → 2750.72] Yeah.
[2750.94 → 2751.98] What is an ideal ratio?
[2752.50 → 2755.04] Is there ever like too many TAS?
[2755.04 → 2762.66] Or is there ever like if you have, say, a workshop of 20 people, like with one TA, that's not enough?
[2762.80 → 2774.92] I'm just interested because from a participant's point of view, like I, which maybe I shouldn't say, but every workshop I go to, I try and find a TA who I can be friends with, who will kind of just like sit near me the whole time.
[2775.48 → 2776.72] I'm just like, hey.
[2777.28 → 2779.24] Explain everything the instructor said.
[2779.62 → 2779.78] Yeah.
[2779.86 → 2780.36] No, literally.
[2780.36 → 2790.48] And I mean, honestly, having been in workshops with Jonas and Johnny, now I've said that, they might be able to remember that I kind of recruited one TA to be my life person.
[2791.24 → 2791.74] I remember.
[2794.08 → 2797.62] And then they'd start walking away, and I'd be like, I've got a question, actually.
[2799.08 → 2800.06] Why don't you just pull up a chair?
[2800.36 → 2801.92] Sit right there.
[2801.96 → 2802.60] You're not going anywhere.
[2802.60 → 2810.06] Anyway, to your question, I've found that the closer the material is to the beginner level, especially how you market the training.
[2810.36 → 2811.52] Or the workshop, whatever it is.
[2812.12 → 2815.76] If you're attracting sort of beginners, you're going to need more TAS, right?
[2815.84 → 2821.36] So for those workshops, I try to have a two to one ratio, you know, two students per TA.
[2821.74 → 2825.10] And it makes it fun when you have like a 40 student workshop.
[2825.10 → 2832.66] And now you have a lot of people who just mostly seemingly just standing around, just going from table to table, but usually ends up working out quite well.
[2832.66 → 2841.58] Now, if the material is on a more advanced side of the equation, then the fewer TAS, because your TAS are no longer helping with some computing basics.
[2841.82 → 2845.18] Like example, I gave earlier, like even somebody not knowing what the terminal is, right?
[2845.26 → 2852.46] You know, they're no longer sort of having to teach some of these things on the way to actually get into the point where they actually can execute on the material, the exercise, right?
[2852.46 → 2860.36] So these people are self-sufficient when the material is advanced and the people you are attracting in that workshop are more advanced.
[2860.46 → 2861.76] They don't need that kind of handholding, right?
[2861.76 → 2867.26] So you can get away with having basically, you know, five, six, seven students per TA, right?
[2867.40 → 2870.28] It depends on really, you know, who you're targeting with your material.
[2870.28 → 2873.74] I have to say I had a way worse ratio.
[2875.74 → 2882.12] Most of the workshops that I've done had a few tens of attendees and I had one at most two TAS.
[2882.80 → 2887.54] And I remember one workshop that I gave that was particularly bad.
[2887.88 → 2890.82] It was a beginner's workshop and I had no teaching assistants.
[2891.24 → 2897.64] It was in a university building, and I was standing in like a huge room where you see probably to teach calculus or something there.
[2897.64 → 2905.02] There's like hundreds of seats, and I was also with a few tens of students teaching basics of elastic search of something not go-over-dated.
[2905.42 → 2908.16] And that was particularly not successful.
[2908.62 → 2916.84] And so definitely I agree, Johnny, with what you say that the more beginner the crowd is, the more you need like a ratio that is closer to one-on-one.
[2917.60 → 2923.74] And then I'd love to hear a little bit about kind of from your experiences, what makes a good TA?
[2923.74 → 2925.80] They feel comfortable interrupting you.
[2927.64 → 2937.14] Yeah, and I think Johnny touched on this a bit, but I think that someone that just recognizes they're there to kind of guide someone, not to solve the problems for them, right?
[2937.24 → 2939.70] Like you're almost more of a rubber duck, right?
[2939.72 → 2941.54] Like you're really just trying to help them understand.
[2941.88 → 2943.92] You never want to just kind of come in and fix it for them.
[2944.02 → 2947.58] So understanding that your role is more to kind of help them, guide them along.
[2947.74 → 2948.74] That's kind of the main thing.
[2948.74 → 2954.68] And just empathy and kind of understanding that don't make any assumptions of where the person's coming from or where they might be caught.
[2954.74 → 2961.50] Just try to be really open to where they're struggling and just like try to understand where they're getting stuck and help them.
[2961.60 → 2965.12] And don't kind of like just be like, oh, this, you know, oh, we'll jump through this.
[2965.22 → 2965.62] It's easier.
[2965.84 → 2966.94] You know, like avoid that kind of stuff.
[2966.98 → 2969.58] Just really be open and take them step by step.
[2969.58 → 2972.02] What I'll add to that is like you touched on it, Jonas.
[2972.20 → 2973.80] You kind of have to realize that it's not about you.
[2974.18 → 2975.68] People are there to learn.
[2976.10 → 2984.54] I have vivid recollections of workshops I've taught that I've basically targeted at sort of underrepresented folks in tech.
[2984.54 → 2990.10] And I have vivid recollections of folks sitting there struggling, right?
[2990.18 → 2992.02] A lot of them to cover some of the basics.
[2992.32 → 2999.38] So the thing is, here I was showing up to teach, you know, go and I've prepared my material.
[2999.98 → 3000.92] You know, I'm feeling myself.
[3001.02 → 3001.90] I'm like, oh, this is good.
[3001.94 → 3002.94] This is good stuff, right?
[3002.96 → 3005.04] This is going to be a great workshop.
[3005.16 → 3007.50] There's going to be so much information being relayed.
[3007.54 → 3014.24] And by the end of it, they're going to walk out of there, you know, being go newbies and sort of ready to start internships and careers and everything.
[3014.24 → 3020.66] And I was like, my aspirations were so high for the results of the workshop that it became about me.
[3020.82 → 3021.26] All right.
[3021.32 → 3022.98] And not about the people doing the learning.
[3023.22 → 3023.42] Right.
[3023.86 → 3027.46] Truth be told, I didn't get, you know, like halfway through the work, to the content.
[3027.46 → 3037.28] And because I didn't realize that my target audience, right, they had so much sort of learning to do to even get to the point where the stuff I was talking about had made sense.
[3037.46 → 3037.64] Right.
[3038.02 → 3039.10] Same thing for my TAS.
[3039.10 → 3046.22] You know, we huddle up afterwards, and they tell me, man, like a lot of these folks are struggling with sort of basics of computing.
[3046.46 → 3054.98] They have a laptop, whatever it is, and they bring it in, and you tell them to go to the command line, or you tell them to install a program or to run a program, whatever it is.
[3055.12 → 3058.66] And they're kind of like, well, where is the icon on the desktop?
[3059.16 → 3059.34] Right.
[3059.38 → 3062.10] Like I need to double-click that thing and launch it, whatever.
[3062.10 → 3066.92] Again, that's part of the, you know, how you market your training, how do you attract your target audience and a lot of that.
[3067.04 → 3085.86] But if you are targeting beginners, right, especially if you're targeting folks who are not, who are really underrepresented in tech, you should expect, right, to have an uneven sort of distribution of some of that basic knowledge, right, that you might expect with folks that are sort of represented or overrepresented in tech, depending on how you want to look at it.
[3085.86 → 3086.02] Right.
[3086.26 → 3090.32] So it's not about you, the teacher or the trainer.
[3090.46 → 3092.28] It's about the people you are going to teach.
[3092.28 → 3103.50] And sometimes you have to adjust on the fly, right, which I've had to do many, many times, realizing that, okay, once you get into a workshop, and you realize, okay, this is how fast I can go.
[3103.72 → 3104.94] Sometimes you can't go fast at all.
[3105.02 → 3109.56] Sometimes you have to realize, okay, I accept that I'm not going to get through half of this material.
[3110.26 → 3113.78] Now, once you accept that, now slow the F down.
[3113.78 → 3132.12] And then make sure that you're actually, you know, making sure that when people walk out of there, they have enough baseline knowledge, right, and enough zeal for continuing to learn on their own, right, which is the key thing that I really, that's my bar for Successful Workshop.
[3132.12 → 3141.38] When you leave that workshop, are you going to get in touch with me afterwards and says, hey, so I'm continuing to do some of the exercises, and I'm stuck here, right?
[3141.88 → 3150.54] When that happens, I am overjoyed because that means that I did the job that I was supposed to do, which was as a teacher, I'm supposed to inspire you to keep learning.
[3150.54 → 3162.36] I'm supposed to make the material that seemed, before you walked into the workshop, seemed so complex and so over what your capabilities, your abilities to actually learn and be able to, you know, like do, right, that fear that you had.
[3162.60 → 3172.16] I want you to walk out of that room no longer having that fear, knowing that there's a challenge there, but that you can do it, right, and you can do it on your own and that you have people to help you, right?
[3172.16 → 3181.52] You can get in touch with me to help you if you need it, but you can walk out of there having lost that fear and having gained zeal for learning the material, right?
[3181.62 → 3185.04] That's my job as a teacher when I teach, right, to remove that fear.
[3185.44 → 3186.84] Again, it's not about the teacher.
[3187.02 → 3187.80] It's not about the TA.
[3188.28 → 3191.46] We have to take a back seat in order to actually serve our students.
[3202.16 → 3210.24] Linde is simple, affordable, and accessible cloud computing the developers trust.
[3210.58 → 3212.16] Linde is our cloud of choice.
[3212.26 → 3219.42] We trust them, and we think you should build anything you're working on, a fun side project, or that next big infra move at work with Linde.
[3219.42 → 3222.48] The best part, you can get started on Linde with $100 in free credit.
[3222.48 → 3231.86] Get all the details at Linode.com slash changelog or text changelog to 474747 and get instant access to that $100 in free credit.
[3232.24 → 3234.22] Again, Linode.com slash changelog.
[3248.28 → 3251.08] Along that line, it's all about your attendees.
[3251.08 → 3256.62] I would love to hear how you think about, like, almost, like, attendee management.
[3257.06 → 3269.02] Like, if you have a group who aren't speaking up or there are a few people who, you know, haven't, you're not seeing them engage, how do you kind of help them feel comfortable, encourage them to participate?
[3269.02 → 3277.70] And on the flip side, if you have someone, and I'm, if I'm honest, if I think back to myself in workshops in the early days, I think I was this person.
[3277.96 → 3291.72] If you have one person who's taking up a lot of space and is asking, like, a million and two questions, and unbeknownst to them, maybe taking time away from others, how do you maybe help them give others space?
[3291.72 → 3306.12] Maybe, I don't know, Anna, when you're either from, like, when you've been lecturing, when you're thinking about your workshop, how are you thinking about almost, like, people management and trying to make sure everyone feels, included, everyone feels like they've had a little bit, at least, of, like, one-on-one attention, I guess?
[3306.12 → 3310.86] It's actually a very good question and a challenging one.
[3311.20 → 3313.92] I try to engage people.
[3314.56 → 3320.82] So if you engage them, you get directly feedback from them and know how it's going.
[3321.22 → 3328.80] If I see that someone is asking questions over and over, I had that once in a local meetup or workshop, small one.
[3328.80 → 3332.08] I said to the one person, there are other questions.
[3332.46 → 3334.16] Try to Google it, search it.
[3334.24 → 3335.40] I give them a hint.
[3335.54 → 3340.86] And then I moved on to the next person to equally spread my end.
[3341.22 → 3344.78] I actually had one TA their time.
[3344.78 → 3353.56] Because if we were, like, 10 or 15 people, it's not possible that two people concentrate only on one person all the time.
[3354.28 → 3357.90] And saying that friendly, I think that's okay.
[3357.90 → 3359.34] Being aware of that.
[3359.66 → 3360.18] No, for sure.
[3360.32 → 3360.76] And I agree.
[3360.86 → 3361.76] It's very challenging.
[3362.20 → 3362.88] 100%.
[3362.88 → 3367.66] I don't know whether, Natalie or Johnny or Jonas, you have any tips.
[3368.36 → 3369.76] Because it's certainly very difficult.
[3370.46 → 3376.08] Yeah, I mean, I think if it is the case for someone speaking up a lot, you know, yeah, I'll often use the like, hey, you know what?
[3376.12 → 3377.14] I feel like you have a ton of questions.
[3377.24 → 3378.30] Why don't we chat a bit later?
[3378.38 → 3379.98] I want to make sure everyone else has time, you know?
[3379.98 → 3383.98] Or, you know, kind of get that, like, try to note that, like, yes, I want to help you, but we got to help everyone.
[3384.32 → 3386.12] And that usually works pretty well.
[3386.12 → 3391.30] And I think for the quieter folks, I'll just, I'll note again that TAS are great for that, too.
[3391.40 → 3396.42] Sometimes if I see someone that looks quiet, you know, I might just ask a T, like, hey, why don't you just check in with them a bit?
[3396.46 → 3397.04] They might be shy.
[3397.14 → 3399.28] They may not want to talk up, but, like, just check in on them.
[3399.52 → 3401.20] So TAS help with that a lot, too.
[3401.54 → 3402.02] No, for sure.
[3402.02 → 3402.58] Awesome.
[3402.76 → 3408.52] So I'm going to ask one last question until we move into what can arguably be my favourite part, which is unpopular opinions.
[3409.26 → 3417.18] But the last thing is just for people looking for workshops, what are some tips for looking for workshops that are going to be beneficial?
[3417.46 → 3419.96] Is it that you should look for the levelling?
[3420.32 → 3423.48] You should look for who's kind of going to be leading it and look at that background.
[3423.48 → 3427.06] How do you identify good workshops as someone looking to learn?
[3427.28 → 3429.90] Of course, take the instructor with the most Twitter followers.
[3429.90 → 3446.14] I would probably evaluate that a workshop feels pretty good if it has a clear explanation of what is your expected knowledge.
[3446.28 → 3447.70] Kind of, is this for complete beginners?
[3448.00 → 3449.34] Should you have some knowledge?
[3449.34 → 3457.28] So this will help me understand that this is a little bit of levelling and kind of like being on the same page of what will be the level of it.
[3457.28 → 3459.94] Because what is intermediate for you is not intermediate for me.
[3460.04 → 3467.02] But if you say I need to be somebody who developed at least one web app and deployed it once, I will understand a little bit better what does it mean.
[3467.54 → 3476.06] And also something like here's the list of the either topics we will cover or maybe this is all what you can expect that we will have accomplished.
[3476.06 → 3481.64] Then I feel that this is a workshop that is framed enough, and I know what am I stepping into.
[3482.02 → 3486.62] I guess just also be mindful of your learning style and kind of what's effective for you.
[3486.62 → 3489.38] And how they're catering it and if it's going to work for you.
[3489.68 → 3492.90] Be realistic about what kind of things work for you and don't.
[3493.28 → 3498.34] So I definitely feel like especially in a virtual world, I've tried different things and I realized like, oh, this is horrible.
[3498.44 → 3499.22] I can't pay attention.
[3499.34 → 3501.96] I need to recognize that this is not a good format for me.
[3502.24 → 3503.26] You want to get the most out of it.
[3503.36 → 3507.44] So kind of recognize what sort of things helps you really learn versus not.
[3507.58 → 3508.42] This is a hard one.
[3508.58 → 3510.04] Anna, were you about to jump in?
[3510.38 → 3510.66] Yeah.
[3511.60 → 3512.76] Please, please do.
[3512.76 → 3527.98] I wanted to add to Jonas' answer that I think it's important that you be aware of what works for you and that you also leverage people you know.
[3528.68 → 3532.64] But like Natalie asked, forget information about what's working.
[3532.64 → 3539.78] And one other thing I realized for myself is also looking a bit more into your timetable.
[3540.68 → 3542.70] If you have the time to attend this workshop.
[3543.12 → 3553.22] Because for me, being like for several hours in some workshop now in the virtual setting is much more exhausting than it was before.
[3553.22 → 3563.42] So if I know I have a week full of meetings, I found even the coolest workshop hour get together more exhausting than before.
[3563.56 → 3566.64] And then it's like, do I learn a lot afterwards?
[3567.00 → 3570.86] So that's something very specific to this remote setting.
[3571.14 → 3574.52] But I think it's also important that you're aware of this.
[3575.18 → 3575.34] Awesome.
[3575.34 → 3581.84] Well, we have come to what is arguably my favourite part, which is where we hear your unpopular opinion.
[3582.18 → 3583.54] It can be about anything.
[3583.82 → 3586.38] It does not have to be technology related, go related.
[3586.92 → 3589.04] It can be about genuinely anything.
[3593.04 → 3594.56] Unpopular opinion.
[3594.86 → 3595.68] You what?
[3595.76 → 3597.50] I actually think she'd probably leave.
[3597.50 → 3602.50] Unpopular opinion.
[3605.34 → 3610.14] So I'm going to turn over to our lovely guest Anna first.
[3610.64 → 3612.22] What is your unpopular opinion?
[3613.74 → 3624.40] Recently, I realized that this awesome compile time of Go eliminates my too deep press when compiling it because it's too fast.
[3624.40 → 3636.50] When doing my markdown, I have like, it compiles, and I know I can take too deep press before looking at the screen, seeing the errors or seeing that it succeed and be happy.
[3637.00 → 3641.76] And for the Go program, that doesn't work because I get the results directly.
[3643.68 → 3646.30] So it's a bit too fast, which is great.
[3647.40 → 3648.94] So that's your unpopular opinion.
[3649.08 → 3650.34] Go is too fast.
[3650.34 → 3650.94] Yeah.
[3652.26 → 3653.22] The camp fan.
[3653.78 → 3655.00] Oh my God, I love that.
[3655.18 → 3655.42] Okay.
[3656.02 → 3661.22] And then our lovely other guest, Jonas, what is your unpopular opinion?
[3661.44 → 3664.60] This is one that I feel like I've noticed more since being remote.
[3664.60 → 3670.74] But I really generally don't like Slack threads, except for maybe a few exceptions.
[3670.74 → 3674.54] And I think based on how everyone uses Slack, I'm in the minority.
[3674.94 → 3676.62] But I get lost.
[3676.80 → 3678.18] I have a hard time finding things.
[3678.70 → 3681.56] And it's like, it's just too much.
[3681.76 → 3683.98] And there are now threads in DMs.
[3684.06 → 3684.70] And that's absurd.
[3684.88 → 3685.28] I'm sorry.
[3685.36 → 3686.74] That just doesn't need to be a thing.
[3687.84 → 3688.62] Don't like it.
[3688.62 → 3692.86] I have to say, at least for me, this is an unpopular.
[3693.06 → 3693.58] I love this.
[3693.66 → 3694.92] It keeps everything organized.
[3695.28 → 3696.00] It's so nice.
[3696.48 → 3698.36] I could not enjoy this more.
[3699.52 → 3700.04] Me too.
[3700.76 → 3700.98] See?
[3701.26 → 3701.60] All right.
[3701.66 → 3702.12] Yeah, clearly.
[3702.32 → 3703.12] I'm the minority here.
[3703.24 → 3703.84] You're the winner.
[3703.84 → 3704.84] This is a...
[3704.84 → 3713.54] I mean, is there a way to find a middle ground where if a thread gets to 15, then you have
[3713.54 → 3716.08] to change it to some other forum?
[3716.08 → 3718.32] I mean, I've been trying to implement that one.
[3718.44 → 3721.88] Like, if a thread gets over a certain number, then we have to jump in a Google Hangout.
[3722.08 → 3724.36] But not everyone's decided that they want to do that.
[3724.40 → 3728.46] Because arguably, people don't really want to be in Google Hangouts.
[3728.64 → 3729.50] And I am...
[3729.50 → 3733.24] They're more adverse to the Google Hangout than this massive thread I found.
[3734.80 → 3738.02] People are actually chatting on Slack already about that.
[3738.20 → 3738.40] Really?
[3739.78 → 3741.34] Everyone's going to put things in threads.
[3741.34 → 3742.34] Like...
[3742.34 → 3750.46] Like, this option to send the messages from the thread also to the overall thread.
[3750.62 → 3751.72] And sometimes it's used.
[3751.84 → 3754.12] And that's starting to be confusing.
[3755.48 → 3756.28] Multi-threading.
[3756.96 → 3757.78] No, I'm terrible.
[3758.10 → 3763.58] If I come to a thread that's, like, longer than I care to read, I'll often be like, hey,
[3763.58 → 3764.26] guys.
[3764.38 → 3765.00] Really sorry.
[3765.08 → 3766.34] Can someone give me the TLDR?
[3766.34 → 3770.72] So that I don't have to read this massive thread?
[3772.64 → 3774.48] I think that's definitely up for debate.
[3774.58 → 3777.04] I'd be interested to see who finds that unpopular.
[3778.56 → 3781.84] And then, Natalie, do you have an unpopular opinion for us?
[3782.24 → 3786.28] Mine is also about a very useful tool in the text here, Twitter.
[3786.92 → 3787.16] Okay.
[3787.16 → 3794.10] I think we should stop following people and adopt lists instead.
[3794.42 → 3802.38] So I saw this as a recommendation of Cindy, aka Copy Construct, who I think is a great, really
[3802.38 → 3805.24] great person about everything infrastructure related.
[3806.06 → 3808.82] And Cindy said that she stopped following everybody.
[3808.96 → 3811.50] I think she has something like zero people she's following.
[3811.60 → 3813.34] And she just organized that into lists.
[3813.34 → 3819.72] And not only it does not show you ads, which is nice, or promoted tweets, but also you
[3819.72 → 3826.00] get to build kind of your feeds to whatever content you want to see now.
[3826.48 → 3829.08] And I slowly started implementing this as well.
[3829.20 → 3833.94] And I'm step by step unfollowing people and putting them into more categories.
[3834.42 → 3839.08] If only a few people do this, if I unfollow everybody in this chat, it will be a little
[3839.08 → 3839.56] bit rude.
[3839.88 → 3842.64] As if I don't care about you and I don't like you, but it's actually not true.
[3842.64 → 3847.70] I am consuming your content only when I want something related to what you tweet about.
[3848.26 → 3852.22] And if we're all going to do this, then it's not going to be about polite or not, or who
[3852.22 → 3857.08] has more or less followers, or I don't follow you, and you don't follow me or something in
[3857.08 → 3859.32] the Twitter manners, in the Twitter sphere manners.
[3859.82 → 3861.54] But it will be just organized for everybody.
[3862.98 → 3863.42] Nice.
[3863.66 → 3868.74] Because my social capital and my self-worth is directly correlated to how many Twitter followers
[3868.74 → 3869.28] I have.
[3869.88 → 3871.12] Because I know I'm popular opinion.
[3871.12 → 3873.60] That isn't actually true.
[3875.02 → 3876.40] That is not actually true.
[3877.18 → 3879.16] Honestly, I feel like we are over time.
[3879.50 → 3884.64] But if Johnny, if you have a very succinct, pointed, unpopular opinion, I'm ready for it.
[3884.70 → 3885.04] I do.
[3885.32 → 3886.42] And maybe you'll like it.
[3886.52 → 3886.70] Okay.
[3886.70 → 3892.20] I think every programmer should at some point try management for a short stint.
[3893.12 → 3894.38] Try going into management.
[3894.98 → 3896.92] You know, even if it's just six months to a year.
[3897.18 → 3900.56] And you can go back to being an individual contributor if you want, but you should at least
[3900.56 → 3901.40] try it once.
[3901.84 → 3904.88] That's going to change your perspective on a lot of things.
[3904.88 → 3906.38] So, yeah.
[3906.98 → 3907.98] Managers are not the enemy.
[3908.20 → 3908.96] Plus 100.
[3910.56 → 3913.64] And product managers are your best friend.
[3914.04 → 3914.44] Yep.
[3917.94 → 3918.72] Side note.
[3918.72 → 3922.78] Well, thank you so, so much, everyone.
[3922.92 → 3926.20] This was truly a delightful conversation.
[3926.56 → 3928.46] I'm really sad that we didn't have more time.
[3928.54 → 3931.08] I think we should have talked for hours on end on this topic.
[3931.40 → 3932.42] But thank you so much.
[3932.64 → 3935.24] Please check out Anna's workshop coming up.
[3935.62 → 3937.06] You can check it out, Option Europe.
[3937.70 → 3938.72] I'm sure it's going to be brilliant.
[3939.32 → 3942.86] And obviously, all the lovely speakers will be on Overslack.
[3942.98 → 3945.36] So ping them with many, many, many questions.
[3945.88 → 3947.72] And hopefully you'll attend their workshops.
[3948.14 → 3948.76] Thank you, everyone.
[3949.22 → 3949.64] Thank you.
[3949.76 → 3950.06] Thanks.
[3950.06 → 3950.62] Thank you.
[3958.18 → 3959.64] Thank you for listening to Go Time.
[3960.02 → 3962.88] If you enjoy the show, please do share it with a friend.
[3963.32 → 3967.00] Personal recommendations are the number one way people find new podcasts.
[3967.06 → 3967.68] They love.
[3967.96 → 3970.14] And of course, subscribe if you haven't yet.
[3970.24 → 3970.96] We're on Spotify.
[3971.36 → 3972.54] We're on Apple Podcasts.
[3972.56 → 3973.18] We're pretty much everywhere.
[3973.52 → 3977.30] You can also check out the back catalogue of awesome episodes at GoTime.fm.
[3977.42 → 3980.48] There you'll find our recommended episodes, plus listener favourites.
[3980.68 → 3983.34] And you can even request your own guest or topic.
[3983.98 → 3987.28] Go Time is produced by Jared Santo with music by Break master Cylinder.
[3987.28 → 3991.76] Thanks again to our awesome sponsors, Vastly, Launch Darkly, and of course, Linde.
[3992.24 → 3996.76] Next up on Go Time, John and Chris welcome a couple of special guests
[3996.76 → 3999.70] to dive deep into event-driven systems.
[4000.08 → 4001.14] Stay tuned for that one.
[4001.38 → 4002.92] It'll be coming at you next week.
[4002.92 → 4004.66] So, I'll catch you next week.
[4007.54 → 4007.58] Okay.
[4019.54 → 4020.26] Bye.
[4020.32 → 4022.86] So, we're out of Somerset.
[4022.86 → 4024.28] We're out of hoping this time.
[4025.28 → 4031.46] A
[4035.26 → 4036.72] lie
