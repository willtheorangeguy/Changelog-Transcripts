[0.00 → 4.08] I think when people talk about data now in terms of data that affects personalization
[4.08 → 9.28] and identification, I think the argument to be made now by any data scientist or AI practitioner
[9.28 → 14.52] is the argument on what you need and why you need it and being able to justify that going
[14.52 → 15.72] forward in general.
[15.94 → 17.76] There are many exceptions to that, obviously.
[17.76 → 24.72] But yes, I think the burden has changed to us to show not only why we need it and what
[24.72 → 31.16] we need it for, but why that's a good thing and why it does not cause damage unintentionally.
[31.52 → 35.80] And so we've come a far cry from the early collect everything.
[36.26 → 41.08] Only intelligence agencies these days collect absolutely everything, you know, the way the
[41.08 → 41.68] world works now.
[41.68 → 58.34] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[58.60 → 59.66] and accessible to everyone.
[60.02 → 60.82] Subscribe now.
[60.96 → 64.80] If you haven't already, head to practicalai.fm for all the ways.
[65.18 → 70.14] Special thanks to our partners at Vastly for delivering our shows superfast to wherever
[70.14 → 70.80] you listen.
[70.80 → 72.96] Check them out at Fastly.com.
[73.22 → 75.36] And to our friends at Fly.io.
[75.68 → 79.32] We deploy our app servers close to our users and you can too.
[79.66 → 81.56] Learn more at Fly.io.
[87.52 → 93.14] Well, welcome to another fully connected episode of the Practical AI podcast.
[93.72 → 99.60] This is where Chris and I keep you fully connected with everything that's going on in the AI community.
[99.60 → 106.66] We'll discuss some recent AI issues or news and dig into some learning resources to help
[106.66 → 109.18] you level up your machine learning game.
[109.80 → 110.58] I'm Daniel Snack.
[110.70 → 116.06] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[116.06 → 119.18] Benson, who is a tech strategist with Lockheed Martin.
[119.74 → 120.40] How are you doing, Chris?
[120.66 → 121.56] Doing very well, Daniel.
[121.70 → 122.74] It's a good day.
[122.88 → 125.30] I'm looking forward to having a fun conversation with you.
[125.36 → 126.38] Hope our listeners are too.
[126.38 → 126.82] Yeah.
[127.54 → 129.86] Have you been flying much recently?
[130.06 → 132.00] For listeners, Chris is a pilot.
[132.28 → 133.86] Have you been up in the air very much?
[134.20 → 134.82] I did.
[134.96 → 139.16] We took a vacation with my daughter a little while back and did a lot of flying for that.
[139.36 → 144.72] And then ironically that you asked this today, tonight, pilots have to do what's called currency
[144.72 → 147.50] flying to keep your night rating going every three months.
[148.00 → 149.04] Tonight is the night.
[149.04 → 154.24] So I'm going to go fly tonight after a couple, a little while after dark and do some night
[154.24 → 154.70] landings.
[154.80 → 155.58] Always enjoy those.
[155.68 → 156.42] The lights are beautiful.
[156.84 → 162.22] Well, in terms of some of the things that I'd like to discuss today, this might seem like
[162.22 → 164.60] a random question, but I think it's relevant.
[165.20 → 170.08] So I know you're doing these certifications and other things, and you've got to keep things
[170.08 → 170.34] up.
[170.34 → 178.12] If you were told that the FAA or whoever, they wanted to have a camera mounted in your plane
[178.12 → 184.24] and monitor all of your whatever is going on in the cockpit during each of your flights
[184.24 → 188.18] to judge whether you were a good pilot or not.
[188.36 → 194.90] And there would be constant monitoring of you, maybe an AI model identifying certain things
[194.90 → 196.72] you did wrong or something.
[196.72 → 199.12] How would that make you feel?
[199.62 → 201.04] Oh, not good at all.
[201.28 → 202.12] Not good at all.
[202.24 → 208.46] I mean, aside from all the moments where maybe I take liberties that the FAA wouldn't
[208.46 → 213.78] go for, just in general, every bad landing noticed, that kind of thing.
[214.18 → 214.34] Right.
[214.68 → 215.28] Oh, boy.
[215.44 → 215.64] Yeah.
[215.74 → 217.14] That doesn't appeal to me at all.
[217.36 → 220.90] It would feel like a fairly substantial invasion of my privacy.
[220.90 → 221.38] Yeah.
[221.80 → 231.74] But I think one could argue that if you wanted to know and certify only pilots that did the
[231.74 → 237.32] right things a certain percentage of time or something, I guess there's a sort of in that
[237.32 → 243.88] case, there's maybe a balance between, hey, on one side, I'm going to make an argument about
[243.88 → 251.82] some type of safety over privacy or accuracy over privacy or something like that.
[251.82 → 257.94] And on the other end, of course, it's a natural maybe in what we would most people would consider
[257.94 → 259.84] in this sort of hyperbolic situation.
[260.12 → 263.72] Most people would consider an invasion of privacy.
[264.40 → 266.78] Yeah, I think there's a balance to be struck there.
[266.86 → 267.22] Certainly.
[267.22 → 271.34] I mean, when you raise public safety, that's a legitimate concern.
[272.10 → 276.78] But I know that it is a topic that, you know, in the use case that you brought up, pilots
[276.78 → 284.46] do talk about that because with current technologies, the oversight is becoming increasing for pilots.
[285.02 → 291.14] And I think that that's very important when, like if you were an airline pilot, and you have
[291.14 → 293.52] passengers in the back, that's super important.
[293.52 → 299.40] And for me, I worry about, do I really need that level of oversight if I'm doing the mountain
[299.40 → 300.12] flying that I do?
[300.16 → 302.14] I tend to do low mountain flying and lower areas.
[302.48 → 307.16] But if I were to pass a hiker on a ridge top without realizing they were there, technically,
[307.44 → 310.08] I would be breaking a regulation and I could get in trouble.
[310.64 → 313.80] And frankly, I think that might be like a step too far.
[313.96 → 318.74] So I think the privacy concerns are something we need to figure our way through.
[319.22 → 322.16] I'm guessing that there's an AI angle going on this one.
[322.16 → 328.58] Yeah, I think that I bring up this topic and in these episodes, it's just you and me, of
[328.58 → 331.50] course, we get a chance to discuss some of the things on our mind.
[331.66 → 336.46] And this has been one of the things on my mind recently, not so much the cameras in the
[336.46 → 342.24] cockpit sort of scenario, because I'm not a pilot, but general sort of privacy concerns
[342.24 → 349.32] and thinking about even for my own team, like what are the balances that we need to strike
[349.32 → 356.04] and where the privacy concerns within our own workflows in terms of making sure that we're
[356.04 → 362.10] comfortable and responsible with the ways in which we're handling data, the data that
[362.10 → 367.66] we're feeding into our models, the types of data that we're storing in certain places and
[367.66 → 371.72] that sort of thing has definitely been on our mind recently.
[371.72 → 372.54] I don't know.
[373.06 → 376.48] So when I got into this stuff, I don't know.
[376.80 → 380.72] I don't know if we've talked about this, Chris, but if whenever you got into things like
[380.72 → 386.12] this, but when I got into this sort of stuff, it was sort of the beginning of data science
[386.12 → 389.26] hype, not so much the AI hype yet.
[389.26 → 389.56] Right.
[389.58 → 393.52] Like there was this hype around sort of data science is the new thing.
[393.52 → 396.46] And so getting a job as a data scientist.
[396.66 → 402.32] And I remember at that time, there's sort of this thinking, well, you don't know what
[402.32 → 403.56] data you're going to need.
[403.56 → 407.16] So just make sure you store it all, and you have it all.
[407.36 → 408.64] That was kind of the mindset.
[409.14 → 412.04] I remember very distinctly at the time that was the mindset.
[412.24 → 415.40] How do you think that mindset, maybe do you relate to that?
[415.44 → 417.24] And how do you think that's shifted over time?
[417.32 → 418.42] Oh, I remember that.
[418.62 → 423.18] You're showing your age, Daniel, by the way, you know, because that certainly changed
[423.18 → 426.32] dramatically over the last couple of decades.
[426.94 → 431.54] You know, when you talk about those early days of data science and, you know, everyone
[431.54 → 433.14] was pioneering their way through that.
[433.14 → 439.52] And yes, you were trying to find data to use and there often wasn't enough data around.
[439.78 → 443.48] And when you found it, you collected all you could to combine with others.
[443.74 → 446.98] And obviously, today things are somewhat different.
[446.98 → 453.66] And with the capabilities, it is privacy and things like data bias and such as that.
[453.66 → 459.10] And they're all interrelated has changed the landscape dramatically, especially when
[459.10 → 460.64] you consider all the use cases out there.
[460.94 → 466.16] Yeah, I bring this up because the like, let's just say that we want to strive for privacy
[466.16 → 468.36] or a reasonable amount of privacy.
[468.58 → 469.98] Let's make that argument first.
[470.06 → 474.68] There's probably a separate argument of like, well, maybe we don't need the privacy that we,
[474.68 → 476.96] a lot of people are after.
[477.50 → 478.60] Maybe that's another discussion.
[478.60 → 481.52] But let's assume that we're striving for some level of privacy.
[481.88 → 487.40] I would say the first thing that comes to my mind in terms of making something, quote,
[487.48 → 493.96] private is if you don't collect or store the data, then that's just about as private as
[493.96 → 494.74] you can get.
[494.84 → 500.22] Now, maybe there's like other logs and certain things that we maybe wouldn't think immediately
[500.22 → 503.00] of as data that are revealing certain things.
[503.00 → 506.90] But I think one principle is I even saw this term.
[507.44 → 510.04] So I was looking through several things leading up to this.
[510.20 → 516.58] One of them that I look at occasionally is Google has this responsible AI practices page
[516.58 → 524.84] and they use this term data minimization, which I know probably listeners are thinking,
[525.12 → 528.48] well, what would we have to learn from Google about privacy?
[528.48 → 531.82] Because they know everything and have all the data.
[532.42 → 536.98] So it's kind of interesting to think about Google talking about data minimization.
[537.40 → 544.66] But I find this term interesting in the sense of like one way to improve privacy is to just
[544.66 → 546.36] plain not have data.
[547.12 → 552.36] Have you been in those sorts of discussions within your career around like, do we actually
[552.36 → 556.36] need to store this data, or should we not store it?
[556.40 → 557.50] Those sorts of conversations.
[557.50 → 563.68] Yeah, I think the burden has flipped to the opposite side from those early days that you
[563.68 → 564.18] talked about.
[564.56 → 568.66] I think when people talk about data now in terms of data that affects personalization
[568.66 → 574.18] and identification, I think the argument to be made now by any data scientist or AI practitioner
[574.18 → 579.58] is the argument on what you need and why you need it and being able to justify that going
[579.58 → 580.78] forward in general.
[581.00 → 583.82] I would say, you know, there are many exceptions to that, obviously.
[583.82 → 591.74] But yes, I think the burden has changed to us to show not only why we need it and what we need it
[591.74 → 597.74] for, but why that's a good thing and why it does not cause damage unintentionally.
[598.08 → 603.30] And so we've come a far cry from the early collect everything data.
[603.30 → 608.92] I think only intelligence agencies these days collect absolutely everything, you know, the
[608.92 → 610.24] way the world works now.
[610.56 → 610.72] Yeah.
[611.16 → 612.62] I think there has been a shift.
[612.62 → 618.26] I think there are a lot more conversations going on about within companies talking about
[618.26 → 624.20] whether they should store certain pieces of data, maybe about a user, let's say a name
[624.20 → 626.50] or a location, right?
[626.56 → 632.66] Something that is useful in maybe marketing purposes or whatever it is, right?
[633.00 → 636.98] Do we really need to store that to do our marketing the way that we want to do our marketing?
[636.98 → 639.50] That's like a question that comes up probably.
[640.20 → 645.86] And it comes up, I think, in relation to like Facebook and others have or meta or whatever
[645.86 → 647.24] I should refer to them as.
[648.08 → 653.22] They've changed their APIs and other things to where you don't get some of that data in
[653.22 → 654.40] many scenarios.
[655.08 → 658.12] So maybe some of that is just we don't even get it anymore.
[658.12 → 664.88] But I think that as much as I love Hugging Face and the Hugging Face Hub and that community,
[665.46 → 671.86] I think there is this sort of shift with the recent AI, more AI related hype around like,
[672.18 → 675.82] what are all the AI data sets we can create, right?
[675.98 → 679.86] And there's definitely bias concerns that have come up with that.
[679.96 → 683.24] I think there's probably privacy concerns as well, though.
[683.24 → 689.48] I remember very distinctly, I tried to actually find if there is like a blog post about this
[689.48 → 689.92] or something.
[690.04 → 697.76] But I remember Jim Lunar, who used to work for Immune, I attended a talk by him and he
[697.76 → 706.82] showed how you could reconstruct a real person's face from the parameters of like a facial recognition
[706.82 → 709.70] model because the parameter space was so large.
[709.84 → 711.42] So there's a very large model.
[711.42 → 715.00] There's a lot of information encoded in the parameters of that model.
[715.12 → 719.68] And he could sort of reconstruct, or he showed some research where someone did.
[719.80 → 723.64] I forget the exact details, but you could sort of reconstruct something from that.
[723.72 → 729.86] So even these like very, very large models that are released and the parameter spaces of
[729.86 → 732.72] those models could even have privacy concerns.
[732.72 → 737.32] So I think this sort of proliferation of like, let's get all the data sets on the hub.
[737.40 → 739.12] Let's get all the models on the hub.
[739.12 → 743.34] I think that overall is like, you know, 99.
[743.58 → 744.20] Oh, I don't know.
[744.36 → 747.96] I don't want to put a percentage of it, but I think overall, like it's a very, very good
[747.96 → 748.26] thing.
[748.44 → 752.08] And obviously, I think if you've listened to this show very much, you know how much I
[752.08 → 753.60] love that effort.
[753.60 → 760.16] But I think with it, there's sort of this maybe a shift back in thinking towards like, let's
[760.16 → 761.54] accumulate all the data.
[761.78 → 763.66] Let's release all the models.
[764.02 → 770.76] And these models themselves may even have sort of certainly bias concerns, but privacy concerns
[770.76 → 772.32] as well within them.
[772.52 → 774.90] So, yeah, that's one thing that I don't know.
[775.12 → 780.88] I don't really have a definitive statement on, but I've been thinking about as I've seen
[780.88 → 782.26] the community grow around that.
[782.26 → 788.56] You know, you raise a really important point in terms of the implications of what you just
[788.56 → 789.06] described.
[789.38 → 795.92] And that's the fact that as the capabilities are evolving over time, the way we're choosing
[795.92 → 800.70] to make evaluations about how our privacy is affected is also changing.
[801.02 → 803.30] So it's not a static decision.
[803.82 → 808.18] It's a decision where if you look back a few years and look at where it's at, you're like,
[808.18 → 810.62] I'm okay with that, you know, I could see that.
[811.06 → 811.56] They're not going back.
[811.64 → 816.62] But at this point, the sophistication level is becoming so much higher.
[817.24 → 821.92] And the fact that you can do that, that reconstruction that you just described, you know, makes one
[821.92 → 822.80] reevaluate.
[823.02 → 827.40] And then if you add in the fact that there are also considerations like who is it that's
[827.40 → 832.78] doing it and why and what, and that changes depending on who it is.
[832.78 → 838.78] We all are making decisions every day about what privacy compromises we're willing to make.
[839.14 → 842.82] And we all have different profiles in that capacity.
[843.18 → 848.18] If you choose to install security cameras, you know, like the doorbells that everyone
[848.18 → 853.86] has now, and you now know that every time you walk in and out of your front door, you're
[853.86 → 856.38] on camera, and it's recognized, you know, it has a model there.
[856.46 → 857.30] It knows who you are.
[857.36 → 861.18] It's recognizing you even before anything is done with the data.
[861.38 → 863.50] And we've all made, and I've made that choice.
[863.58 → 868.56] I have a Nest on my doorbell and I have other devices around my house that know who I am.
[868.94 → 874.16] So there's some level of that, but it also depends on whether I have some level of
[874.16 → 880.16] control of that data in terms of its usage, what the rights that I have as a consumer are,
[880.40 → 885.34] and whether it's from a public sector perspective or a private sector perspective.
[885.64 → 888.44] So all those are considerations that we can delve into.
[904.16 → 917.18] So Chris, the first term that I had run across that I wanted to bring up was that term data
[917.18 → 921.52] minimization, which is, you know, maybe you do need data to do something.
[921.62 → 922.20] Maybe you don't.
[922.28 → 928.32] That's one consideration with privacy is certainly the easiest way to deal with the privacy concern
[928.32 → 929.52] is to not have the data.
[929.52 → 937.06] I think, though, many cases, either we step into a project and data exists already and
[937.06 → 941.86] is maybe stored within our organization or, you know, we have some data set that we're
[941.86 → 946.66] interested in working with that, you know, maybe we don't know what the sort of identifying
[946.66 → 951.22] information within that data set is or the privacy concerns with it.
[951.22 → 959.12] The next term that I ran across as I was sort of probing this space was data identification.
[959.58 → 967.20] I was reading a blog from, again, Amu ta, which I think we've had Amu ta on the show before
[967.20 → 971.06] here, and they've, of course, done a lot of thinking in this space.
[971.48 → 977.06] But they have a nice blog post, which we can link in the show notes about data identification,
[977.06 → 983.66] and they talk about various sorts of pieces of data that you might want to disidentify
[983.66 → 985.34] within data sets.
[985.56 → 990.14] I think for practicalities purposes, I'll just mention a few of those since this is practical
[990.14 → 990.50] AI.
[991.10 → 995.60] So they have a long list that I won't read all of them, but they talk about names, dates,
[995.76 → 996.46] telephone numbers.
[996.46 → 1001.30] Those are probably ones that would be immediately assumed.
[1001.30 → 1008.68] Maybe ones that people might not be, you know, thinking about immediately would be a device
[1008.68 → 1010.84] identifier or serial number.
[1011.06 → 1015.96] So like maybe that's a Mac address or maybe that's like a browser fingerprint.
[1016.40 → 1019.96] Web URLs might be identifying.
[1020.46 → 1026.46] Like there's such a proliferation of analytics data within URLs these days.
[1026.46 → 1030.70] That's one thing I was thinking about, like the, you know, all the query strings that are
[1030.70 → 1034.52] added onto a URL to track you in various ways.
[1034.52 → 1041.52] Or like there could be an account ID in some URL or something like that, which is, you know,
[1041.58 → 1043.54] something that could happen.
[1043.72 → 1045.34] And they list out a bunch more.
[1045.50 → 1050.96] But those are the types of, when we refer to identifiers, the types of identifiers that
[1050.96 → 1052.70] were, we have in mind.
[1052.70 → 1058.12] And as you sort of look at that list, Chris, do these things come up in your mindset in
[1058.12 → 1059.28] data sets that you work with?
[1059.60 → 1059.86] Absolutely.
[1060.26 → 1065.88] You know, going through the process of trying to get them removed, to disidentify them while
[1065.88 → 1071.06] not losing the potential value of what you're trying to create from a model.
[1071.16 → 1077.68] Because, I mean, let's face it, many of the models we create, humans are central to the
[1077.68 → 1079.76] output, to the inferences of those models.
[1079.76 → 1084.02] And so if you're going to deal with humans, you're going to be dealing with these identifying
[1084.02 → 1084.54] traits.
[1084.78 → 1089.52] But if you take out too many, too much, sometimes you run the risk of the model not being able
[1089.52 → 1092.44] to be productive, even for the best use.
[1092.76 → 1099.02] So it's a bit of a challenge for the data scientist of today to try to, there's this balance
[1099.02 → 1103.46] of a bunch of hard things that we need to accomplish from an ethical standpoint.
[1103.86 → 1106.64] And we do the best we can with the tooling available.
[1106.64 → 1112.66] Yeah, I also think that the person giving you their data needs to have agency to give
[1112.66 → 1113.92] you their data, right?
[1114.34 → 1119.38] But I also think that the public doesn't understand the implications of some of the
[1119.38 → 1120.90] data that they might give you.
[1121.08 → 1129.12] So I think that you, as maybe a practitioner in the AI space, probably could also not just
[1129.12 → 1137.74] assume because the user gave me this, it's going to be okay, or at least not have any
[1137.74 → 1141.16] issues if I use this identifying field or something.
[1141.60 → 1145.86] I listened to a podcast about the we talk about the boarding pass thing.
[1146.18 → 1147.34] This is another flight thing.
[1147.70 → 1148.38] I don't think so.
[1148.50 → 1149.00] Go for it.
[1149.14 → 1152.92] So I listened to, I think this is another Dark net Diaries.
[1153.00 → 1154.04] I love that podcast.
[1154.04 → 1158.34] I've mentioned it a couple of times on the show, but what had happened was, you know,
[1158.40 → 1160.80] people, they go on a trip, right?
[1160.88 → 1165.30] And they like post a picture of their boarding pass on Instagram or something, right?
[1165.30 → 1168.92] Like I'm going on my vacation, look at my boarding pass or whatever.
[1169.44 → 1171.78] It's very common, you know, hashtag boarding pass.
[1172.20 → 1177.30] Well, there was a guy that said, you know, there's some, gotta be something on this boarding
[1177.30 → 1182.66] pass that is like the airline doesn't tell you that your boarding pass is a security risk
[1182.66 → 1184.00] and should be private, right?
[1184.58 → 1186.00] And so people post them all.
[1186.00 → 1193.00] But what this guy learned was that the like booking ID, so it was like a Qantas flight,
[1193.52 → 1193.70] right?
[1193.82 → 1197.92] And he saw the booking ID was on the boarding pass.
[1198.18 → 1202.30] And what's interesting is that he found, I think it was the Australian prime minister
[1202.30 → 1206.00] posted a picture of one of his boarding passes somewhere he was going.
[1206.46 → 1212.12] So he took the booking ID from the Australian prime minister, took it to the Qantas website,
[1212.12 → 1218.30] and turns out all you needed was the booking ID and a bit of personal information like your
[1218.30 → 1223.16] name, where you were from, which is obviously all public record for a prime minister.
[1223.78 → 1229.16] And he just logged right into Qantas as the prime minister of Australia.
[1229.46 → 1232.18] Of course, at that point, the flight had already happened.
[1232.60 → 1234.94] But then he was like, well, I wonder what else is here.
[1234.94 → 1240.26] And then he just did page view source on the logged in Qantas site.
[1240.58 → 1246.78] And in the source of the page, there was a JSON field, which included all the info about
[1246.78 → 1252.16] the account holder, including passport number, phone number, etc.
[1252.62 → 1255.06] And of course, the podcast is really great.
[1255.12 → 1256.90] Maybe I'll link that in the show notes, too.
[1256.90 → 1262.48] But it's like, who would have thought that posting a picture of a boarding pass, which
[1262.48 → 1265.32] the airline doesn't tell you is a security risk.
[1265.66 → 1272.20] But obviously, there was a security risk there and a privacy concern because there's sort of
[1272.20 → 1274.26] passport information and such.
[1274.84 → 1280.02] But people, sometimes the companies don't even understand how people might put this data
[1280.02 → 1286.88] together, which I guess influences like maybe the scope of the concern here and how you really
[1286.88 → 1293.30] want to consider both data minimization and data identification, at least in many cases.
[1293.30 → 1299.66] Yeah, you really raised the point about the burden being on us as the data scientists, data
[1299.66 → 1305.82] scientists of goodwill and good ethics, because the public doesn't understand a lot of
[1305.82 → 1306.30] these things.
[1306.30 → 1313.96] Any of these documents, the whole purpose of a boarding pass is to identify you as the
[1313.96 → 1320.30] rightful user of that airline seat and to admit you to the plane and such.
[1320.94 → 1322.70] So by definition, it's an ID thing.
[1322.86 → 1328.36] And anything that serves an identification purpose should be treated pretty carefully.
[1328.86 → 1333.78] It's hard to do today for the public, not only in the context of how data can be used in
[1333.78 → 1339.54] an AI context, but just in the broader world, there are so many opportunities for data leakage
[1339.54 → 1341.96] that affects us in that personal way.
[1342.10 → 1347.16] I have gotten probably more insight into that than most people because of two things.
[1347.26 → 1352.70] A, I'm in this world that we're talking about, you know, AI, ML and data science, but I'm also
[1352.70 → 1353.74] in the defence industry.
[1353.94 → 1359.40] And we go through classes about how to protect yourself because of, for obvious reasons, you
[1359.40 → 1361.20] know, with nefarious folks out there.
[1361.20 → 1363.60] And so there are so many opportunities.
[1364.02 → 1371.92] So it really does raise the need for the data science and the AI, ML community kind of step
[1371.92 → 1376.04] up to meet those needs because you can abuse it, and you can, you can use it.
[1376.08 → 1379.96] You can get away with what you want to get away with probably in many cases, but that hurts
[1379.96 → 1380.94] us all in the long run.
[1381.00 → 1385.00] It causes harm not only to others, but to ourselves in this industry.
[1385.00 → 1390.40] So definitely something to be thinking about in every possible part of your life that has
[1390.40 → 1391.98] any form of identification associated.
[1392.22 → 1392.42] Yeah.
[1392.86 → 1398.50] There's a big concern here, but there is a lot of good thinking and tooling around this
[1398.50 → 1401.32] sort of identification side of things as well.
[1401.32 → 1408.24] In the Amu ta article, they talk about, okay, well, if we assume that, as you mentioned,
[1408.68 → 1413.86] us as practitioners want to be responsible with the data that we're processing and the
[1413.86 → 1414.96] way that we're handling it.
[1415.28 → 1421.98] One scenario, let's say that we didn't do the we couldn't do or didn't do data minimization,
[1422.24 → 1422.44] right?
[1422.46 → 1423.32] We have data.
[1423.70 → 1428.74] We need to use it for a specific purpose, but we also are maybe concerned.
[1428.74 → 1433.88] Maybe it's text fields, and we're concerned that there are names or phone numbers, these
[1433.88 → 1435.60] sorts of things, account numbers.
[1436.14 → 1441.40] Maybe it's individual structured data, but maybe it's just raw data, and we don't exactly
[1441.40 → 1441.82] know.
[1442.32 → 1445.54] There are disidentifying methods out there.
[1445.84 → 1451.14] So of course, this is a lot easier probably if, I mean, in the language space, if you're
[1451.14 → 1458.44] using English, for an example, you have an advantage because you could, for example,
[1458.44 → 1465.24] take a named entity recognition model and figure out where the names are and replace the names
[1465.24 → 1466.64] with pseudonyms, right?
[1466.80 → 1472.02] So like for your AI model, it probably doesn't even care what the name is, right?
[1472.02 → 1473.08] As long as it's a name.
[1473.08 → 1479.86] So you can sort of do pseudonyms or fake phone numbers and this sort of thing and, or, you
[1479.86 → 1483.64] know, hash certain fields or obfuscate them in certain ways.
[1483.70 → 1488.52] So that's like this using a replace type of method for these fields.
[1488.92 → 1490.80] You could, you know, just identify them.
[1490.86 → 1492.06] I know there's Python tooling.
[1492.34 → 1496.56] I've used, I forget what the update is on the best one to use.
[1496.64 → 1498.38] We've used one called Scrub-a-Dub.
[1498.38 → 1503.82] I think there's Python libraries to like to find these things and identify them or replace them.
[1504.36 → 1510.94] The Amu ta article emphasizes this type of, you know, masking or pseudonyms and that sort
[1510.94 → 1511.40] of thing.
[1511.90 → 1514.60] And it probably, again, depends on the data type.
[1515.02 → 1519.54] Maybe if you've got an image with people's faces in it, maybe that's a different scenario
[1519.54 → 1524.72] than if you have sort of a text field with a name in it, and you can replace the name.
[1524.72 → 1527.92] It's maybe, maybe more difficult to replace.
[1528.18 → 1533.28] I mean, there are ways now, of course, you know, maybe this is another positive use of
[1533.28 → 1535.02] the deep fake sort of methods.
[1535.20 → 1538.14] You can replace faces and images and that sort of thing.
[1538.70 → 1544.72] But if you're, there's probably certain methodologies like facial recognition, which by their very
[1544.72 → 1547.50] nature are identifying methodologies, right?
[1547.56 → 1552.98] So you don't want the whole point of facial recognition is to identify someone, right?
[1552.98 → 1560.54] So there's probably a range of scenarios as well, where like if I'm just trying to do like
[1560.54 → 1565.98] predict a marketing campaign or something like that, maybe the sort of obfuscation and
[1565.98 → 1568.22] masking methods are really relevant.
[1568.22 → 1575.48] If I'm actually, though, trying to identify a face for a security reason in my building
[1575.48 → 1578.58] or something, I am actually trying to identify someone.
[1578.58 → 1583.72] And that probably brings up other issues of how you log that and store that identification,
[1584.14 → 1585.24] which we can talk about.
[1585.86 → 1586.30] Yeah.
[1586.50 → 1588.46] It gets complicated in that way.
[1588.60 → 1593.04] And that kind of going back, you know, building on your last point a little bit there, it goes
[1593.04 → 1594.06] back to the use case.
[1594.14 → 1596.76] It goes back to who is, who is using that data.
[1597.04 → 1601.00] Is the government that you happen to be fall under in whatever country you're in?
[1601.00 → 1606.48] Are they looking for facial recognition or is this your nest doorbell, and you've made an
[1606.48 → 1607.08] accommodation?
[1607.72 → 1609.58] It's pretty crucial, and it's pretty hard.
[1610.12 → 1616.68] One of the from an identification standpoint, your, I think your airline example a few minutes
[1616.68 → 1623.08] ago was really pertinent in that it's very easy for user who may be making a choice about
[1623.08 → 1629.00] offering their data to misunderstand that they may look at the data that they're giving up and go,
[1629.00 → 1630.88] this is okay, this isn't too much.
[1631.40 → 1637.16] But if the, the model creator is combining that data that they've chosen to give up with other
[1637.16 → 1642.82] data, a lot of privacy can be, can be compromised by combining different data types together.
[1643.04 → 1645.90] That may not be part of that, that initial thing.
[1645.92 → 1648.74] It may be something that you already have available or from another source.
[1649.02 → 1650.92] So it gets, it gets challenging.
[1659.00 → 1680.46] The challenge that you brought up Chris around, I guess, the expectations of users of how their
[1680.46 → 1683.18] data is going to be used or combined with other things.
[1683.18 → 1686.78] It's a really challenging one that can get really complicated.
[1687.00 → 1693.38] Like I'm thinking of even in my own scenario, we've had discussions before because maybe we've
[1693.38 → 1702.66] got a, a recording from someone across the world, some language recording in our archives,
[1702.80 → 1703.04] right?
[1703.08 → 1710.10] And they, they gave permission for that data to be used or collected and stored in the archive.
[1710.10 → 1714.94] And like for language documentation purposes or something like that, right?
[1715.42 → 1718.80] Maybe we no longer have access to that person, right?
[1718.80 → 1724.90] So we can't get their explicit permission to use that in any other way, even though we know,
[1725.12 → 1728.62] well, this would be useful to add to an AI data set, right?
[1728.80 → 1732.02] Like, so we're talking about that all the time internally.
[1732.02 → 1738.42] And our team is like, when the data collect was collected, that's a very crucial time to,
[1738.42 → 1746.68] you know, help the, help the company express to the user how their data is going to be used
[1746.68 → 1752.02] and have the user understand and, you know, have agency over that.
[1752.22 → 1757.64] But also there's, that brings up the additional point that like, yeah, you could give them a
[1757.64 → 1761.82] long list with the terms and conditions thing that no one's going to read, right?
[1761.88 → 1765.78] Is that really giving them control over how their data is being used?
[1765.86 → 1770.42] Because for any reasonable person, you could assume that they're not going to read through
[1770.42 → 1771.26] all that, right?
[1771.58 → 1774.62] Everyone will assume they're not going to read it, but the lawyers involved, of course.
[1774.82 → 1775.96] But the lawyers, yeah.
[1776.54 → 1778.78] The lawyers are assuming they've read every word.
[1780.20 → 1781.68] I mean, you raise a great point.
[1781.68 → 1788.08] I confess I probably shouldn't do it in such a public way, but I have agreed to many terms
[1788.08 → 1790.54] and conditions where I have not read the full verbiage.
[1790.96 → 1793.50] There might've been more than a few where I didn't read any of the verbiage.
[1793.80 → 1799.80] And so we are often making these choices of convenience that may have some fairly long-term
[1799.80 → 1801.16] repercussions, as you're pointing out.
[1801.66 → 1807.38] The other kind of major category within the data identification that Immune brings up,
[1807.38 → 1812.94] and actually the many other places do as well, I think, including that Google responsible
[1812.94 → 1820.74] AI practices is something having to do with randomization and differential privacy.
[1821.50 → 1828.96] So a case of this that we've been talking about internally is if we have a device in the
[1828.96 → 1830.24] field, right?
[1830.24 → 1839.62] And we're gathering either text, audio, video, one choice for us would be to send all of that
[1839.62 → 1844.94] audio back to a central location, store it in S3, and do a bunch of things with that,
[1845.02 → 1845.16] right?
[1845.48 → 1851.24] That's probably the worst case scenario because now we've got just recordings of audio from
[1851.24 → 1853.58] some random place and maybe people don't know.
[1854.38 → 1859.30] Hopefully they knew that they were getting recorded and understood what was happening.
[1859.30 → 1867.16] But still, that's a very hard situation because you actually got the raw data, and it's sent
[1867.16 → 1868.30] to a central location.
[1868.80 → 1874.00] I think one thing in that scenario that is a best practice is if you can do any of that
[1874.00 → 1878.40] processing at the edge, if you can push your models out to the edge, and let's say I'm
[1878.40 → 1886.34] doing transcription of the audio, and then I'm detecting something about what is said in
[1886.34 → 1886.84] the audio.
[1887.34 → 1889.88] Maybe I don't even want to send the transcript back.
[1889.96 → 1895.58] I just want to send metadata back about like, hey, I did a transcription, and I'm not sending
[1895.58 → 1896.10] the audio.
[1896.26 → 1897.46] I'm not sending the transcription.
[1898.36 → 1902.38] And of course, that's a much better scenario because the audio is staying on the device.
[1902.54 → 1907.08] The model was run at the edge and the only thing you're sending back is metadata.
[1907.08 → 1915.52] Of course, that's still probably a tricky situation because you're knowing maybe something was said
[1915.52 → 1921.46] at a certain time at a location from a device, which brings up this randomization piece.
[1921.68 → 1921.78] Right.
[1921.88 → 1927.94] So the other thing you can do is take those messages that you would send back to the central
[1927.94 → 1933.64] location and randomize their timestamps or their ordering or that sort of thing to where,
[1933.64 → 1941.14] for example, if someone said something that had political implications at a certain time
[1941.14 → 1947.28] at a location, whoever had access to that central source of data, they couldn't really tie it back
[1947.28 → 1952.74] to a central or a certain location at a certain time and maybe identify the person that said that
[1952.74 → 1955.20] and persecute them for saying that.
[1955.34 → 1960.32] So this sort of randomization comes, and it can be taken as far as this idea of differential
[1960.32 → 1970.18] privacy, which offers a mathematical guarantee around sort of privacy and the masking of
[1970.18 → 1971.98] direct identifiers.
[1972.26 → 1974.70] And that's come up also with federated learning.
[1974.82 → 1981.34] So I think the edge computing side of this comes in and actually to a lot of benefit to
[1981.34 → 1982.44] the privacy situation.
[1982.44 → 1986.82] If you're able to do things at the edge and the things that you're communicating over a network
[1986.82 → 1992.54] are randomized in some way, there's some guarantee around privacy, and maybe you're just
[1992.54 → 1997.62] communicating metadata and not the raw data that stays at the edge.
[1998.20 → 2004.56] So that, of course, makes infrastructure a lot harder to deal with, but it's overall a better
[2004.56 → 2005.22] situation.
[2005.22 → 2012.86] As you were saying that, I'm struck with the fact that it takes a good actor to be willing
[2012.86 → 2014.06] to do these things.
[2014.32 → 2021.64] By way of example, so many of the laws that we have, both here in the United States and in other
[2021.64 → 2027.94] countries, are not sufficient to kind of enforce these things that we're talking about here in this
[2027.94 → 2031.34] episode as good practices and as ethical practices.
[2031.92 → 2037.56] I know that here where I'm at physically in the state of Georgia, I can record a phone call
[2037.56 → 2043.66] legally, and only one party of the phone call has to know it's being recorded, and that's me as the
[2043.66 → 2044.06] recorder.
[2044.44 → 2050.04] So I can record a phone call without the other person having any knowledge that that call is being
[2050.04 → 2050.46] recorded.
[2050.78 → 2054.18] And that data is data that I have available to me.
[2054.26 → 2054.98] It has their voice.
[2055.14 → 2057.22] It may, who knows what they say on the call.
[2057.66 → 2062.18] You're kind of going back to your point about political comments, whatever, and how I use that
[2062.18 → 2062.56] data.
[2062.90 → 2069.26] What I'm getting at is, as we kind of build this ethical framework as good actors in the data
[2069.26 → 2077.22] science community, we really need to find ways of having these techniques kind of acknowledged
[2077.22 → 2083.62] beyond our community and be able to be integrated in as best practices in a legal framework to help
[2083.62 → 2084.10] enforce it.
[2084.10 → 2087.62] Because I know I'm not going to do anything nefarious, and I know you're not going to do
[2087.62 → 2088.34] anything nefarious.
[2088.34 → 2093.30] But there are a few people out there that might do something that is nefarious, and it
[2093.30 → 2100.38] raises a fairly challenging kind of enforcement or compliance concern in terms of implementing
[2100.38 → 2105.40] these techniques that are going to be necessary for us to be responsible with this data going
[2105.40 → 2105.68] forward.
[2106.22 → 2106.32] Yeah.
[2106.32 → 2114.56] And I think that as a person that builds tools that maybe various clients will use, one thing,
[2114.56 → 2121.34] like if you're in that situation, like if you're creating software products that might
[2121.34 → 2129.06] be used by a variety of organizations, I think it's your sort of duty to take into account
[2129.06 → 2135.88] how you can ensure that your software product isn't going to be used for malicious purposes
[2135.88 → 2142.20] rather than assuming or writing in a terms and conditions or a licensing agreement that you
[2142.20 → 2143.54] agree not to do this.
[2143.54 → 2151.20] So for example, like in that scenario of communicating audio back to a central place, if you only make
[2151.20 → 2157.62] it is possible for your software product to communicate metadata back to a cloud location, I mean, someone
[2157.62 → 2161.36] could hack it and maybe do something else, but at least you're making it much harder.
[2161.58 → 2167.38] Whereas if you make it to where there's an option to send the audio back as well, well, then
[2167.38 → 2172.22] you're in a whole nother scenario where people could do all sorts of things with that.
[2172.22 → 2178.84] So I think that also understanding what might be possible, whether you think you are working
[2178.84 → 2186.72] with good actors or bad actors is within the sort of duties of us as practitioners to think, because
[2186.72 → 2194.12] even our managers or executives that are promoting the things that we build, they might not understand the
[2194.12 → 2198.46] implications of what could be done with what we're building.
[2198.46 → 2212.62] So at some point we have to kind of own that and hope that over time, the sort of regulations and guidance we get from maybe governing bodies or other places is we'll catch up to where the technology is.
[2212.62 → 2214.62] That's a great point you're making.
[2214.62 → 2221.24] And that is, do what you have the ability to do to kind of police the set of circumstances
[2221.24 → 2222.24] that are out there.
[2222.24 → 2235.00] So if you don't have a strong legal framework to fall back on that will protect your users in that capacity, as a data scientist, being able to say, well, this is the software I'm going to give you.
[2235.12 → 2238.08] This is the capability that I will provide.
[2238.70 → 2244.04] And eliminating some of those cases that could be used nefariously is really important.
[2244.04 → 2256.16] I would love to hear examples from our listeners about how they might be doing some of these things and maybe share some of their ideas with us on some of our social media outlets for the show, because this is important.
[2256.44 → 2270.04] Our community is leading the way in the sense of how to affect privacy with all of these new technologies coming through and all the capabilities that AI has surged forward on in the last few years.
[2270.48 → 2271.72] We're the vanguard.
[2272.06 → 2272.86] We're the tip of the spear.
[2272.86 → 2274.54] Yeah, I totally agree.
[2274.90 → 2284.08] Well, in the last few minutes here, it may be worth just quickly mentioning a learning resource and maybe a couple of things happening in the AI community.
[2284.34 → 2301.60] One interesting thing, Chris, I wanted to mention before we close out here is that you can now run this Stable Diffusion model on a hugging face space, which is one of these recent text to image models that does really amazing things.
[2301.60 → 2302.60] When you put in a variety of text.
[2302.60 → 2304.06] When you put in a variety of text.
[2304.06 → 2307.26] So I just in our Slack channel, I sent you a message.
[2307.26 → 2314.08] I put in two cool guys recording an AI podcast, and maybe I can post this in our show notes or something.
[2314.08 → 2316.44] But they don't look like Chris and me.
[2317.04 → 2318.92] But no, it's cooler than we are.
[2318.92 → 2322.32] In a couple of the photos, they're wearing sunglasses.
[2322.56 → 2324.02] Maybe we should consider that.
[2324.22 → 2332.00] I do notice that there's a trend where at least three of them, one of the guys is bald, and the other one is not bald.
[2332.32 → 2333.82] Well, I have very short hair.
[2333.82 → 2340.62] Maybe I should shave my head, and we need one bald guy and another.
[2341.00 → 2341.16] Yeah.
[2341.52 → 2345.34] Also, there's some interesting text going on.
[2345.70 → 2348.82] Two Korunas.
[2349.10 → 2350.42] I don't even know what that means.
[2351.22 → 2356.46] Anyway, very interesting AI generated two cool guys recording an AI podcast.
[2356.46 → 2364.74] But they have other examples, too, like a small cabin on top of a snowy mountain in the style of Disney art station.
[2365.32 → 2367.98] An insect robot preparing a delicious meal.
[2368.64 → 2370.16] So anyway, something to play with.
[2370.26 → 2378.30] If you don't have access to the OpenAI Dally 2 model yet, and you're on the wait list, wait no longer.
[2378.46 → 2383.52] You can use Stable Diffusion on Hugging Face and have some fun there.
[2383.52 → 2389.58] I also saw a pretty cool release from Spacey from the NLP world.
[2390.04 → 2397.46] They've been on the podcast before, but they released Floret, which is an extended version of Fast Text, which uses Bloom embedding.
[2397.60 → 2404.28] So Bloom was this huge language model that was a collaborative effort and a big language model that came out recently.
[2404.28 → 2416.02] And Spacey has implemented this sort of combination of Fast Text embeddings and Bloom embeddings, which is efficient and built right into the Spacey ecosystem.
[2416.28 → 2425.14] And I'm excited to try those things out where this will allow you to compare words to other words and see their similarities.
[2425.14 → 2436.28] But also build models on top of this sort of embeddings, which could allow you to do things like text classification or named entity recognition and these sorts of things.
[2436.34 → 2441.28] These are really the building blocks of modern NLP or these embeddings.
[2441.54 → 2451.42] And it's interesting, these combine both word and subword embeddings, which could handle like misspellings or rare occurrences of words and that sort of thing.
[2451.42 → 2465.16] So really cool effort from Spacey to make this sort of cutting edge NLP building block really an easy-to-use piece of their really user-friendly packaging.
[2465.52 → 2467.70] So really cool to see that.
[2467.82 → 2480.72] The last thing that I saw, which is more of a learning resources, I see there's an upcoming Intel workshop on FPGAs, which seems pretty interesting to me.
[2480.72 → 2483.00] I'll link that in the show notes.
[2483.20 → 2486.70] I don't know anything about FPGAs, but I hear them mentioned occasionally.
[2487.00 → 2490.06] And so maybe I'll join the workshop and find out some more.
[2490.54 → 2491.00] Sounds good.
[2491.06 → 2491.72] It looks interesting.
[2492.14 → 2502.54] And I will say, without jumping into detail, there are a lot of really cool things happening in that space with hardware and processors and single board computers right now.
[2502.76 → 2507.70] And so a lot of new AI capabilities are coming out by various companies.
[2507.70 → 2511.48] So, yeah, I would imagine this workshop is a pretty cool place to go.
[2511.68 → 2511.82] Cool.
[2512.06 → 2512.90] Well, thanks, Chris.
[2513.00 → 2514.22] It's been a fun discussion.
[2514.66 → 2516.66] Let's think more about our privacy.
[2516.96 → 2521.50] And I promise I won't install a camera in the cockpit of your plane.
[2521.98 → 2523.10] Thank goodness.
[2523.30 → 2523.80] Oh, boy.
[2523.92 → 2524.50] Thanks, Daniel.
[2524.72 → 2525.30] On that note.
[2525.52 → 2525.92] All right.
[2526.00 → 2526.50] See you, Chris.
[2526.82 → 2527.30] Talk to you later.
[2527.30 → 2536.84] All right.
[2536.98 → 2538.56] That is our show for this week.
[2538.80 → 2541.18] If you dig it, don't forget to subscribe.
[2541.66 → 2544.36] Head to practicalai.fm for all the ways.
[2544.88 → 2550.30] And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or colleague.
[2550.66 → 2553.62] Word of mouth is the number one way people find shows like ours.
[2553.62 → 2562.88] Thanks again to Vastly for fronting our static assets, to Fly.io for backing our dynamic requests, to Break master Cylinder for the beats, and to you for listening.
[2563.12 → 2563.78] We appreciate you.
[2564.02 → 2564.98] That's all for now.
[2565.18 → 2566.68] We'll talk to you again on the next one.
