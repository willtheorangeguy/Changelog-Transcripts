[0.00 → 7.46] It's already been a big day, but we do have one more thing.
[22.10 → 27.62] Welcome to Change Login' Friends, a weekly talk show about spatial computing.
[27.62 → 33.30] Thanks to our partners for helping us bring you great developer pods each and every week.
[33.54 → 38.24] Check them out at FASI.com, fly.io, and typesense.org.
[38.46 → 39.72] Okay, let's talk.
[45.26 → 49.04] So we are here joined by Mike McQuaid with Homebrew.
[49.14 → 49.78] What's up, Mike?
[50.00 → 51.76] Hey, I'm going good, thank you.
[52.18 → 53.24] Thanks for having me on, guys.
[53.88 → 54.56] It's been a while.
[54.56 → 60.52] Well, it has been too long, which is why we're so happy to have this new format where we can just invite old friends on and talk to them.
[60.64 → 62.46] Yeah, no, it's nice to come here.
[62.52 → 65.42] It's good timing as well with WWDC recently.
[65.60 → 68.66] Lots of interesting spicy things to talk about.
[68.92 → 75.42] We were joking in the Homebrew maintainer slack yesterday about how it's generally our time of year to be like,
[75.42 → 81.42] what is Apple going to break this time that we have to desperately try and fix in the next three months before everyone complains.
[81.88 → 82.82] Right, right.
[83.32 → 85.48] Well, you probably don't find that out on Monday, though.
[85.56 → 90.32] So the keynote goes out, but that's like the big consumer retail news.
[90.46 → 93.66] But like the developer news kind of trickles out throughout the week.
[93.70 → 94.54] Isn't that the case usually?
[94.54 → 100.48] Yeah, but also there's, I think they've got, they landed one of the developer betas for macOS Sonoma already.
[100.78 → 107.10] So like we actually, one of our maintainers fixed some stuff and made a release yesterday so that Sonoma could work.
[107.18 → 107.54] Wow.
[107.62 → 107.84] Wow.
[108.16 → 110.04] Sonoma could work at a very high level.
[110.20 → 114.38] I not immediately like to fail on startup when you run Homebrew, but.
[114.58 → 117.50] You're not declaring full support, but you probably think it's going to work.
[117.66 → 117.80] Yeah.
[118.06 → 122.02] What are some of the things they tend to break when it comes to new OSes?
[122.02 → 127.88] I mean, you had the major change from obviously Intel to M1 or M2 or just the Apple Silicon world.
[127.98 → 128.34] Right.
[128.54 → 133.04] That had to move where Homebrew actually lives in the file system.
[133.32 → 134.66] What typically breaks?
[135.12 → 138.06] I mean, it could be any number of the things we rely on, really.
[138.18 → 140.14] Like we use the macOS sandbox.
[140.30 → 144.12] So sometimes when they change stuff there, then we need to like work around things.
[144.20 → 151.70] It's sometimes like API calls or like Apple Attention as well, like make the huge changes they want to make with like Xcode.
[151.70 → 155.70] And like map those to like macOS versions as well.
[155.84 → 162.12] So it might be the compiler all of a sudden starts doing slightly different things or giving slightly different output.
[162.30 → 176.70] It might be that they have deprecated the system Ruby and then finally they're actually removing it or, you know, all these types of like little things that you often have like a bit of advanced warning for, but like, you know, require work.
[176.70 → 177.10] Yeah.
[178.30 → 178.58] Right.
[179.40 → 182.54] Why the mood from slash user local to slash opt?
[182.78 → 187.62] This was an Apple Silicon thing, but I don't, and I had to do it on an installation, but I don't know.
[187.70 → 193.18] Was there like, did they push you guys out of user local or was it like easier to have to install at the same time?
[193.26 → 194.56] What was that change about?
[194.56 → 195.00] Yeah.
[195.00 → 195.20] Yeah.
[195.32 → 211.78] It's interesting because we, we sort of debated a few different approaches around that because I mean, there's been some people for like literally since day, well, not literally day one, but probably not far off day one, probably literally since day 30 or a hundred or something in homebrew.
[211.88 → 212.14] Sure.
[212.14 → 214.10] Who hate the homebrew isn't user local.
[214.22 → 215.58] Because they're like, that's not what it's for.
[215.90 → 217.24] Other stuff uses it too.
[217.40 → 219.30] You just kind of bank it up with stuff.
[219.88 → 226.10] And so there's been that sort of like gentle pressure for a while that like, this is not the best place to put homebrew.
[226.18 → 227.28] Maybe you should go somewhere else.
[227.66 → 237.94] But then I think the big one for us was when they released the first M1s, you had Rosetta, which could run old homebrew very well.
[237.94 → 244.86] If you were happy on your Mac, just running x86 codes, well, x86, 64 to be pedantic.
[245.50 → 247.44] And you were fine with all that.
[247.54 → 250.52] And you wanted to buy an M1 Mac and just keep doing things that way.
[250.78 → 253.34] Say like, you know, you're just using it to run CLI tools.
[253.50 → 259.72] Like you're not using it to like to generate code that needs to be embedded in an application of a particular architecture or whatever.
[260.08 → 262.64] Then yeah, you could just continue to use user local then.
[262.64 → 268.78] And well before we had decent ARM support, that continued to work for you.
[268.96 → 275.46] But all our binary packages, well, most of them require you to be in a particular location on disk.
[275.72 → 283.16] So if we built the binary package for user local, you can't randomly install your homebrew somewhere else and have that binary package work.
[283.16 → 293.16] So we were like, well, we have this kind of three problems of A, we don't have binary packages for ARM yet at all.
[293.66 → 297.76] B, some of the big stuff that we really need to make a lot of binary packages.
[297.98 → 301.82] Like in the I think it was a pretty long time before we had Java working at all.
[301.94 → 304.20] And like lots of stuff relies on Java.
[304.36 → 307.92] So if you don't have any Java support, then you can't do a lot of things.
[307.92 → 314.10] And then see this kind of desire to like be able to actually run two homebrews side by side.
[314.68 → 319.52] So you could have the ARM stuff, maybe if you're building stuff locally that you kind of care about.
[319.76 → 324.16] But you can have a separate homebrew installation that lives away by itself that you can install everything.
[324.38 → 325.10] And that all works.
[325.58 → 331.66] And to be able to as well, like for us developing to be able to kind of have some sort of migration path between the two and stuff like that.
[331.66 → 335.68] So that's what sort of ended up with the two separate locations.
[335.88 → 338.90] And it's worked pretty well from that perspective there, I think.
[339.34 → 349.50] And I think literally the only downside really, other than just, you know, I still occasionally get confused as to why I go to user local and all my homebrew stuff's not there.
[350.00 → 352.06] And I'm like, oh, wait, no, no, I moved that.
[352.96 → 353.04] Right.
[353.04 → 360.84] But yeah, the other minor one is like that some tools don't have user local almost like built into their default kind of search paths.
[361.14 → 371.60] But I guess like homebrew is big enough and established enough now that like homebrew in a lot of cases has just got added to those default search paths for these other tools.
[371.68 → 376.22] Where when it was originally created, like that wasn't guaranteed that that was ever going to happen.
[376.22 → 379.04] Some other installers have been using the home directory.
[379.62 → 382.96] So like ASD will have like a hidden ASD folder.
[383.14 → 385.20] A lot of tools now that are installing things.
[385.26 → 390.48] Did you guys consider that versus slash opt as just like make it user local to their home directory?
[390.78 → 390.96] Yeah.
[391.12 → 394.98] So that gets you back to that binary package problem I mentioned earlier.
[395.12 → 395.40] Okay.
[395.48 → 402.54] I guess what we could do is we could do that and mandate that everyone uses the same username, which sounds like an amusing joke.
[402.66 → 404.24] But that's actually what we do on Linux.
[404.24 → 405.58] So on Linux.
[405.94 → 406.34] Oh, really?
[406.68 → 406.92] Yeah.
[406.96 → 415.96] It's under home Linux brew because the Linux homebrew port, which is now rolled into the main project, but was originally called Linux brew.
[416.24 → 419.76] When they started, it was kind of from a scientific infrastructure perspective.
[419.76 → 433.92] And they found it was actually quite easy to get system administrators to just create a user and give everyone on the system permissions to that user's home directory more than it was to create some other random directory on disk, like under opt or user local or whatever.
[434.24 → 443.74] So we effectively have like three different locations that are like my gosh, homebrew defaults where binary packages are built depending on what platform and architecture and things you're on.
[443.84 → 444.12] Fun.
[444.48 → 444.88] Indeed.
[445.32 → 446.36] Fun, fun, fun.
[446.36 → 452.30] Well, as long as I can go without bringing up the big topic.
[452.70 → 452.84] Yeah.
[452.84 → 455.80] I was like, I want to go one more layer, but it's bearing the lead, Jared.
[455.96 → 456.52] It's bearing the lead.
[456.62 → 456.78] Yeah.
[456.78 → 457.62] Let's not do it.
[457.62 → 462.12] So yesterday, as we record this, this is Tuesday morning for us.
[462.12 → 467.48] As we record yesterday was Apple's WWDC keynote, as everybody pretty much knows at this point.
[467.72 → 472.40] And we were watching it live in our Apple nerds channel as we do and just commenting as we go.
[472.52 → 478.48] And about 80 minutes into that keynote, I posted this all caps message that said, show us the VR thing.
[478.54 → 479.18] I'm getting bored.
[479.56 → 481.30] It's kind of what we've been doing so far.
[481.30 → 490.18] Shortly after that, Apple unveiled this Apple Vision Pro new product, but they never actually did show us the VR thing.
[490.68 → 494.00] They said Apple Vision Pro will introduce us to spatial computing.
[494.16 → 505.86] So in the same way that Mac introduced us to personal computing and iPhone introduced us to mobile computing, Apple Vision Pro will introduce us to spatial computing.
[506.36 → 509.30] They said augmented reality is a profound technology.
[509.30 → 513.66] I believe that augmented reality is a profound technology.
[514.14 → 517.98] And they said it's the first Apple product you look through, not at.
[518.58 → 522.30] It's the first Apple product you look through and not at.
[522.70 → 523.42] I thought that was interesting.
[523.52 → 524.28] They never said VR.
[524.80 → 526.82] They never said metaverse that I heard.
[527.16 → 530.08] They didn't even really bring up video games, or maybe I missed that part.
[531.02 → 534.22] But they're talking about augmented reality.
[534.22 → 538.32] I just love your guys' reaction to that, because, Mike, we were talking about VR in our channel.
[538.68 → 540.90] And you have opinions about VR.
[541.32 → 543.04] But this is not pitched as a VR thing.
[543.12 → 543.82] They never said VR.
[543.94 → 545.30] They said augmented reality.
[545.38 → 548.38] They said you look right through it, which is technically not true.
[548.78 → 557.98] But I guess conceptually, they want you to have this idea of looking through these goggles and seeing the world, even though you're seeing a digital representation of the world that's right in front of your face.
[558.46 → 559.44] So what do you guys think about that?
[559.44 → 561.48] Yeah, I thought that was interesting as well.
[561.58 → 563.86] I had a similar realization kind of this morning.
[564.10 → 571.50] And I think it's, I guess it's like AR is kind of more social and kind of human, I guess.
[571.96 → 578.94] It was the vibe that they were going for, at least it felt like from their pitch, where it's a lot more kind of blended with your existing computing.
[578.94 → 593.78] Whereas AR, sorry, VR, like the thing I kind of love about it, like particularly during periods in which, you know, when I was during COVID lockdowns, when we had a three-month-old and a two-year-old who was potty training at home.
[594.08 → 601.14] Like I find it incredibly relaxing to just shut out the entire world in my VR headset and like go to another place.
[601.14 → 603.34] Right. And you have no peripheral vision.
[603.48 → 604.60] You can't see anything else.
[604.60 → 609.56] Like you can press a button to get like a really sort of Jacky sort of AR.
[610.02 → 611.32] Where am I in my room?
[611.44 → 613.48] Just so you don't walk into things sort of view.
[613.60 → 617.50] But like this idea that you're completely put into another space.
[617.50 → 622.02] And that was, I guess, I felt I was expecting they were going to go down that route.
[622.10 → 624.40] And that feels like the metaverse route.
[624.54 → 627.04] And that feels like not at all what they were doing.
[627.46 → 630.24] Like, yeah, I think it's interesting for sure.
[630.98 → 631.12] Yeah.
[631.70 → 632.18] What do you think, Adam?
[632.58 → 637.24] Well, the metaverse route really removes the real world.
[637.90 → 639.56] The augmenting obviously keeps it.
[639.64 → 642.24] So it's not like escaping reality.
[642.24 → 646.74] It's more like blending realities, which is what augmented reality really is, right?
[646.74 → 647.18] Yeah.
[647.72 → 648.06] Yeah.
[648.08 → 649.44] It's not what I was expecting them to do.
[649.72 → 652.00] Even from a safety standpoint, right?
[652.06 → 654.50] Like that you can still see your surroundings.
[654.74 → 658.48] Whereas with you, if you've got like the Oculus Rift on or whatever it's called these days,
[658.50 → 660.48] I can't even keep up with the direction of it.
[660.54 → 661.16] I've got Quest.
[661.32 → 661.90] Is that what it's still called?
[661.94 → 662.64] Or was it the old name?
[662.98 → 663.98] There's the MetaQuest.
[664.28 → 664.64] MetaQuest.
[664.68 → 665.44] MetaQuest Pro.
[666.08 → 666.60] There you go.
[667.12 → 668.20] There's a two and a three.
[668.34 → 669.86] I know the three, they're about 500 bucks.
[669.98 → 671.00] I just hear these things.
[671.08 → 676.54] I've used one, but maybe Mike, you have more because you've been purchasing different VR things.
[676.74 → 679.80] The point is though, is when you put those on that you can't see the rest of the world.
[679.80 → 682.20] Like you can fall over things.
[682.20 → 683.50] You can break an arm.
[683.56 → 684.84] You can break your TV.
[684.98 → 686.50] You can smash things.
[686.60 → 687.04] Go ahead, Mike.
[687.10 → 687.84] You've done this, I'm sure.
[687.92 → 688.16] Right?
[688.40 → 692.20] I was going to say you guys who are on video for the benefit of the podcast listeners,
[692.20 → 704.76] I'm pointing to a very slight discolouration of my wall behind me where I think I literally thought I was crow barring a head crab or something and just punched my hand straight into my wall.
[705.70 → 706.10] Right.
[706.26 → 710.60] I didn't manage to destroy my VR controller in the process.
[710.72 → 712.70] But yeah, that's definitely a thing.
[712.70 → 717.32] And I guess some people can see that as in some situations, that's the appeal.
[717.58 → 719.48] And in some situations, it's really not.
[719.98 → 720.12] Right.
[720.88 → 724.58] Well, we're talking about the positioning really is like the positioning, not in the metaverse.
[724.68 → 725.46] So it's really about that.
[725.50 → 726.36] It's like not versus.
[726.54 → 734.06] It's more like, how did they pitch this when meta is so well known with acquiring Oculus, meta quest, et cetera.
[734.34 → 736.48] The whole name shift from Facebook to meta.
[736.68 → 737.86] Was about the metaverse.
[737.94 → 738.10] Yeah.
[738.18 → 740.72] Is in of itself about the direction they're going.
[740.72 → 741.02] Right.
[741.12 → 742.20] So they didn't say metaverse.
[742.34 → 743.84] They didn't say VR.
[743.94 → 753.08] And I had a great pun, a world-class pun, thanks to Silicon Valley, the TV show, because there's a slight spoiler in there.
[753.14 → 759.46] There's an acquisition of a VR company because they have to have this big old Hooligan keynote.
[759.60 → 761.42] Essentially, everything falls apart.
[761.52 → 762.84] They had to make a last minute change.
[762.92 → 765.84] And they acquired this VR company to make their keynote good.
[766.14 → 768.96] And long story short, he says, who out there is excited?
[768.96 → 770.66] I know VR.
[771.24 → 773.48] Like, that's a world-class pun, right?
[773.88 → 777.00] So there was no VR mentioned at all.
[777.22 → 779.42] Augmented reality, even spatial.
[779.68 → 784.94] The word spatial to me is pretty cool because it's like all the design stuff in there was very touchable.
[785.02 → 786.72] They did a great job from a design standpoint.
[787.36 → 789.64] So spatial design, augmented reality.
[790.16 → 791.14] That's the good stuff, I think.
[791.18 → 792.44] I think they went the right direction, really.
[792.44 → 799.80] And they have the whole app store and all the apps that came with it, whereas Meta was really recreating the unknown, right?
[799.80 → 803.62] They were really trying to pioneer the future or what they perceived as the future.
[803.90 → 804.02] Right.
[804.12 → 807.20] And it was not appealing because it's not relatable.
[807.52 → 810.18] You have Safari inside this thing.
[810.64 → 811.30] That's kind of cool.
[811.38 → 812.44] You have your apps in there.
[812.48 → 815.16] It's kind of you already know what it does and how it works.
[815.20 → 817.02] So you can kind of like to pull up your calendar.
[817.02 → 818.72] Yeah, it's familiar.
[819.08 → 819.44] Precisely.
[819.52 → 820.58] You know, messages there.
[820.78 → 827.52] It's like putting some of your apps that you're used to inside of iOS or macOS right there inside this thing.
[828.04 → 830.96] I don't honestly know, though, if I want that as much.
[831.06 → 833.84] Like, maybe I'm just the guy who's ready to escape sometimes.
[834.22 → 836.92] And I should say, like, the pitch is augmented.
[837.14 → 840.32] But if you notice, they have this digital crown, which they stole from the watch, right?
[840.32 → 841.64] They put it on the top of these goggles.
[841.86 → 845.92] And you crank this crown, and it changes the size of what is being presented.
[845.92 → 848.94] And you can go, like, full VR mode, it seems like.
[849.02 → 850.44] It's just not what they're talking about.
[850.66 → 850.82] Right.
[850.90 → 852.80] Because a lot of their pitch was entertainment.
[853.16 → 856.58] And it was like, look at these big movies you can watch right in front of your face.
[856.80 → 859.30] But they're, like, inside this AR.
[859.64 → 862.64] But they're also, like, putting a screen inside augmented reality.
[862.64 → 865.98] But you can crank that screen up to, like, full size to where there's nothing else to see.
[866.06 → 867.58] So I think they get there.
[867.64 → 868.94] They're just coming at it from a different angle.
[869.42 → 870.42] It reminded me in some ways.
[870.54 → 871.58] It's funny you mentioned the Apple Watch.
[871.58 → 877.76] It reminded me of the Apple Watch keynote as well, where I can't remember what I thought at the time when I saw it.
[878.12 → 881.76] But I definitely remember being somewhat underwhelmed, right?
[881.80 → 886.82] Because they pitched it as a particular type of device that I didn't care about.
[887.02 → 887.30] Yes.
[887.58 → 888.52] It was a fashion thing.
[888.56 → 889.22] A lot of it was fashion.
[889.26 → 889.38] Yeah.
[889.44 → 890.30] It was fashion.
[890.54 → 891.26] It was apps.
[891.36 → 892.12] It was all this type of stuff.
[892.18 → 895.98] Whereas for me, like, I love my, like, health and fitness measurements, right?
[895.98 → 901.20] And I sent a thing from my Apple Watch today to my wife where it's, like, my resting heart rate.
[901.28 → 902.50] I had a fever over the weekend.
[902.82 → 904.32] And I sent her, like, a thing.
[904.38 → 906.14] And I was, like, spot when I was sick, right?
[906.16 → 907.62] And you can see my resting heart rate's normal.
[907.76 → 910.62] And at the weekend, it tanks up and then slowly gets better.
[910.72 → 915.78] And then, like, there's a weird thing, like, even today where it's, like, today's the first day my resting heart rate's kind of back to normal.
[916.06 → 920.16] And almost, like, psychologically being, like, oh, like, maybe that means I'm better now.
[920.24 → 922.46] Like, I might go and do my spin class this week.
[922.46 → 929.46] Like, it feels like it's providing almost, like, metrics data that I might use in, like, an ops role.
[929.54 → 929.86] Right.
[929.94 → 931.94] But on my own body measurements.
[932.24 → 934.44] Like, and that was not pitched at all, right?
[934.56 → 940.40] And it felt like what they were doing yesterday was throwing out, like, 20 use cases.
[940.62 → 943.12] And, like, 10 of them will be flops, right?
[943.18 → 945.06] 10 of them will, it will just be bad.
[945.26 → 949.98] And one of the ones to me, for example, like, like reading about the resolution and stuff like that,
[949.98 → 960.50] the idea that I'm going to do my work on these things, like, and this kind of floating windows in front of me instead of using monitors for any, like, meaningful amount of time.
[960.58 → 965.92] Like, I'm not going to say that that won't happen, but they made a big deal about, like, 4K per eye, right?
[966.40 → 970.50] Put your face right up to your 4K monitor and see how impressive that is, right?
[970.58 → 975.56] If you let the 4K monitor completely fill your peripheral vision, that's not actually a lot of pixels, right?
[975.56 → 980.78] It's a lot of pixels when it is, you know, a foot, like, half a meter away from your face.
[980.80 → 982.64] But it's not a lot when it's that close.
[982.68 → 986.74] And we have other VR headsets already that will do that sort of resolution.
[987.06 → 993.12] And, like, people already do not find them sufficiently high resolution enough to do that type of work all the time, right?
[993.14 → 998.62] Like, it's going to be annoying compared to a 4K monitor unless you're in a situation where you need their kind of, like,
[998.76 → 1004.02] I need to just have, like, 500 windows all around me that I can kind of turn my neck around and look around and all this type of stuff.
[1004.02 → 1010.72] But on the flip side, some people thought it was slightly dystopian, but maybe I'm enough of a nerd that I thought it was awesome.
[1010.94 → 1017.24] Like, the idea of, like, being at your kid's birthday party, right, and, like, putting this thing on and taking a 3D video,
[1017.64 → 1027.28] which you can in then 1, 2, 5, 10, 20 years watch back and put yourself effectively in, like, an almost, like, VR fixed viewpoint.
[1027.48 → 1028.00] 3D.
[1028.00 → 1028.32] Yeah.
[1028.32 → 1028.40] Yeah.
[1028.48 → 1039.74] I mean, because for me, like, I buy the new iPhone every year because I have young children and I want to capture their temporary likenesses in as high a resolution as I can.
[1039.92 → 1040.38] Yeah, yeah, yeah.
[1040.38 → 1045.32] Because I look back at those memories and, like, I love looking back at pictures from my kids.
[1045.50 → 1046.94] I'm with you, Mike, on that one for sure.
[1046.94 → 1054.46] Because for me, I have the and I think you do too, Jared, you have the photos' widget placed somewhere in your phone.
[1054.52 → 1056.82] And, like, every day I'm getting some memory.
[1057.32 → 1060.18] And I'm an iCloud believer because I got my photos in there.
[1060.20 → 1063.90] And they're doing a great job of, like, reminding me of my life.
[1063.98 → 1069.68] Now, the thing is, though, while that's amazing, this is the ultimate new dad camcorder kind of situation, right?
[1069.68 → 1071.66] Like, this is, like, remember dads back in the day?
[1072.04 → 1072.56] It is.
[1072.56 → 1075.30] You got the dad with the camcorder who looks like a Dolphus, basically.
[1075.54 → 1075.78] Yeah.
[1075.94 → 1077.90] But the memory is captured, so you've got that memory.
[1077.98 → 1081.80] And that's, you sort of sacrifice, you know, maybe your ego for the moment.
[1082.36 → 1083.60] But I don't know if I want to wear that.
[1083.68 → 1089.96] I want the artifact after Mike, but I don't want to be the dad wearing this headgear during my kid's birthday.
[1090.10 → 1093.44] Like, I want them to remember me just as much as us remember that memory.
[1093.60 → 1093.92] Right.
[1093.98 → 1095.20] So I think this is temporary.
[1096.04 → 1099.50] The actual video of the guy, you know, like, you're not going to be like, hold on, don't move.
[1099.58 → 1101.16] I'm going to go put these goggles on, you know?
[1101.16 → 1104.64] Like, none of us are going to actually do that unless we're going to be the camcorder dad.
[1104.78 → 1107.32] Because we can see the future use of it.
[1107.74 → 1108.76] I think that's temporary.
[1108.86 → 1111.42] So, like, the recording side, that does look dystopian.
[1111.50 → 1116.02] Like, I'm looking at this real-world thing through goggles that show me a digital representation of the real-world thing.
[1116.22 → 1117.34] Minority Report had that.
[1117.60 → 1120.26] Yeah, but I think the actual, the playback is what we want.
[1120.48 → 1121.98] And so that's what we all agree on.
[1122.30 → 1125.32] And so I think, like, 3D recording is going to come to the iPhone, right?
[1125.32 → 1132.98] Like, you'll be able to record 3D on some other thing and then watch it back on these goggles and get that immersive experience.
[1133.22 → 1133.40] Yes.
[1133.44 → 1136.48] For now, it's, like, just a weird place where it's, like, it also records.
[1136.60 → 1137.22] Where's the robot?
[1137.48 → 1141.80] Put those goggles on a robot that has infinite charge, never dies.
[1142.00 → 1144.06] I'll let my robot wear that thing on my behalf.
[1144.34 → 1146.80] And it's fine because, like, Rosie can do that.
[1146.86 → 1150.06] That's the name of the I believe that was the name of the robot in the Jet sons, right?
[1150.12 → 1151.22] Like, Rosie, I believe?
[1151.32 → 1151.88] Oh, yeah, Rosie.
[1152.30 → 1153.16] So give me a Rosie.
[1153.16 → 1153.88] I want a Rosie.
[1154.08 → 1161.80] Is there any girl out there who can resist the charms of a solar-powered alloy chassis with turbo-driven schematics and LED eyes?
[1161.98 → 1162.38] Beep, beep.
[1162.44 → 1165.34] A robotic maid named Rosie changed the Jet sons.
[1165.34 → 1171.46] Well, speaking of infinite charge, I mean, there are so many indicators that this device is just not, I mean, the price, of course,
[1171.56 → 1176.06] but, like, the device is not going to be ready for regular consumer usage when it ships.
[1176.24 → 1180.62] It's going to be for enthusiasts, developers, business people, and that's about it.
[1180.66 → 1181.50] The ultra-wealthy?
[1181.50 → 1183.04] Yeah, ultra-wealthy, of course.
[1183.54 → 1184.82] But they just buy everything, don't they?
[1184.88 → 1186.62] So everything's for them if they want it.
[1187.14 → 1190.16] Two-hour charge, and you've got to have a battery stick in your pocket.
[1190.68 → 1197.44] I did watch a video this morning, the hands-on, because they let some YouTubers get access yesterday.
[1197.62 → 1197.86] Yeah.
[1198.26 → 1200.72] I think Om Malik had a hands-on with it as well.
[1200.90 → 1201.86] I didn't catch that, though.
[1202.18 → 1202.66] Who'd you see?
[1203.08 → 1204.40] This is Sarah Kitschy, I think.
[1204.44 → 1205.08] Rhymes with Peachy.
[1205.08 → 1208.04] She saw it, and she wore it, YouTuber.
[1208.54 → 1209.08] And she said...
[1209.08 → 1215.58] There is a reason why the battery pack is not on the headset, because the headset is heavy.
[1215.72 → 1216.98] It is very heavy.
[1217.16 → 1224.64] I think a lot of initial reports said, oh, we're going to put the battery pack, so it's going to be lighter than a Quest, lighter than, you know, any headset out there.
[1224.64 → 1230.16] They did that because it would just be too heavy if the battery pack was on the headset.
[1230.42 → 1236.92] So with that out of the way, that it is heavy, it will be uncomfortable on your face for probably more than an hour.
[1237.04 → 1238.06] So that was kind of a bummer to hear.
[1238.06 → 1246.54] But she did say that the actual 4K display, kind of against what you're saying there, Mike, I don't know what's the truth, but she said, like, it's spectacular.
[1246.90 → 1249.30] The eye tracking is insane.
[1249.46 → 1251.32] So you do a setup that takes one or two minutes.
[1251.62 → 1254.02] The digital crown is essentially your home button.
[1254.18 → 1260.60] And you have all of your apps on the home screen, and you just look at whatever you want, and then you pinch to select.
[1260.76 → 1265.64] If you're scrolling through photos or Safari, you basically pinch and then scroll.
[1265.64 → 1271.68] And the clarity of, say, a Safari tab, you're reading an article, is so good.
[1271.90 → 1273.68] The words are super crisp.
[1274.06 → 1279.22] And I honestly felt more excited about the productivity elements to it than even the entertainment.
[1279.38 → 1283.88] And I think it's like three or four times what resolution that the MetaQuest currently has.
[1284.36 → 1285.12] Maybe that's enough.
[1285.24 → 1290.20] But she's, like, incredibly impressed with that and was like, this is the future, but it just, it's going to hurt.
[1290.48 → 1292.40] And that's kind of where a lot of these things are.
[1292.40 → 1295.68] I think it depends on the content a lot on this stuff.
[1295.82 → 1299.02] Like, I think for movies and stuff, like, I think the resolution doesn't.
[1299.22 → 1301.78] I mean, you know, like a 4K movie looks great, right?
[1301.84 → 1310.30] But, like, when we were watching 1080p stuff, it looks pretty, like, you know, you were watching Lord of the Rings and 1080p being like, ugh, I can see the pixels.
[1310.58 → 1311.86] Ugh, this film's ruined.
[1311.86 → 1313.76] And, like, I think it's all relative.
[1313.90 → 1319.80] And I think, like, video content and, like, gaming experiences, whatever, I think lend themselves to that kind of blend.
[1319.90 → 1324.24] But I think it feels like reading text on a non-retina display now is just like, ugh.
[1324.30 → 1324.76] Oh, yeah.
[1324.84 → 1325.34] Like, ugh.
[1325.40 → 1327.20] Why would I go through that, right?
[1327.28 → 1335.34] And I guess I can't imagine, like, write code, say, like, spending a long day, like, looking at text for significant periods of time.
[1335.84 → 1336.98] I would do that in a heads-up.
[1337.04 → 1338.50] But, Mike, what if you weren't writing the code?
[1339.18 → 1340.16] What if you weren't writing the code?
[1340.16 → 1342.00] What if you were watching it, code?
[1342.24 → 1348.78] Conjuring the code through voice and LLM behind it that, you know, knows homebrew through and through.
[1348.92 → 1349.82] Knows it better than you do.
[1350.10 → 1350.38] Yeah.
[1351.24 → 1352.30] All this good stuff.
[1352.38 → 1353.94] And all you're doing is watching the code, really.
[1354.50 → 1360.72] Yeah, just got ChatGPT to generate the 95% right, 5% catastrophically wrong code for me.
[1361.94 → 1365.54] But, no, I guess it's funny because, like, you know, again, like, on the weight, right?
[1365.54 → 1369.02] Like, I have my nice, meaty valve index here.
[1369.16 → 1371.48] And, like, that's more than twice the weight.
[1371.90 → 1373.48] And, like, even by default.
[1373.72 → 1378.48] And I actually bought more weights to add on the back to kind of counterweight the thing.
[1378.48 → 1380.36] And it makes it feel better.
[1380.44 → 1387.40] And, like, when my kids play around with it, like, they don't have their necks, like, getting crushed forwards by it and stuff like that.
[1387.68 → 1390.06] And it's funny because, like, on the comfort side, I would agree.
[1390.20 → 1394.18] Like, that you don't want to be wearing that for hours and hours and hours.
[1394.18 → 1403.42] But, like, it's interesting to me to see for, I guess, a mass market appeal that something, like, dramatically lighter is still, like, too heavy, wouldn't be comfortable.
[1404.16 → 1409.48] I kind of wonder whether that's just something where, I don't know, like, Apple are good at making things smaller and lighter, right?
[1409.52 → 1413.28] But, like, at the end of the day, like, wearing something reasonably heavy on your head.
[1413.36 → 1414.80] Like, even, like, a big pair of headphones.
[1415.30 → 1420.00] Like, some people would just find a big pair of over-the-ear cans uncomfortable to wear for a few hours, right?
[1420.00 → 1426.42] And you're not going to get, like, a vision thing with built-in headphones that's going to be lighter than a pair of cans.
[1426.92 → 1433.38] I imagine down the road, you know, you're probably looking at something similar to what Adam's wearing right now, which is, like, thick-rimmed glasses.
[1433.80 → 1435.80] And all the tech can fit into those glasses.
[1435.94 → 1437.86] You know, kind of what the Google Glass wanted to be.
[1438.48 → 1444.96] And so, at that point, like, you could, and depending on battery life and stuff, you could just wear these things all day long.
[1444.96 → 1451.32] It goes back, again, to the VR-AR distinction because you don't want to augment your reality for just, like, you know, 45 minutes.
[1451.66 → 1453.42] It's like wearing your Apple Watch for half the day.
[1453.58 → 1455.42] Like, I'm missing out on the other half of the day's steps.
[1455.78 → 1461.72] But to escape reality, right, to have a VR moment, to watch a movie for two hours or to play a game for an hour.
[1462.12 → 1465.02] I know some people play games for hours upon hours.
[1465.14 → 1469.30] But that seems more feasible even for, like, the heavy headsets that you've been buying, Mike.
[1469.42 → 1470.76] Like, I'll put up with it.
[1470.96 → 1471.16] Yep.
[1471.16 → 1475.46] But for, you know, 18 hours, it's going to have to be lighter and smaller.
[1475.72 → 1478.20] And, yeah, like you said, Apple's good at these things over time.
[1479.30 → 1480.40] We'll see if it gets there.
[1480.80 → 1481.00] Yeah.
[1481.14 → 1483.76] Did you see the movie Ready Player One, Mike?
[1484.02 → 1484.88] I didn't, actually.
[1484.98 → 1492.82] I've had a bunch of people, particularly in the VR space, who've said, oh, I basically haven't seen any good films since my kids were born, really.
[1493.44 → 1494.56] I wouldn't call it a good film.
[1494.64 → 1496.22] It's a great film, but not a good film.
[1496.44 → 1497.38] Is it good or better than great?
[1497.42 → 1497.76] I don't know.
[1498.12 → 1498.50] Hold on.
[1498.54 → 1499.10] Let's stop.
[1499.48 → 1500.90] It's not good, but it's great.
[1500.90 → 1502.36] Please, tell us more.
[1503.44 → 1506.60] Well, you got Robert Zemeckis behind it.
[1506.88 → 1512.32] Pop culture references galore, which is always, you know, that's a classic right out the gate, you know?
[1512.40 → 1512.74] I see.
[1512.92 → 1517.30] It opens up with a quintessential rock song from, I believe, the 80s.
[1517.32 → 1518.78] I can't remember the name of it at this moment.
[1519.16 → 1520.02] But did you see it, Jared?
[1520.62 → 1523.34] No, but you talk about it a lot, so I feel like I know something about it.
[1523.34 → 1523.60] Right.
[1523.60 → 1531.40] Well, I'm not going to talk about the movie necessarily, but more or less reference it because this Vision Pro looks almost identical to the film.
[1531.78 → 1543.04] And there's even, during those cut scenes and montages and demonstrations they showed, there's even this one where the person holds them out and then puts them on and that camera sort of swoops around, and you see through them.
[1543.04 → 1547.94] That is literally shot for shot, angle for angle from Ready Player One.
[1548.04 → 1549.62] So they stole that, or it was an homage?
[1549.98 → 1550.66] It could be an homage.
[1550.92 → 1551.82] They could have licensed it.
[1551.88 → 1552.34] I don't know.
[1552.42 → 1554.16] I'd love to know the legality is there.
[1554.16 → 1556.96] But, like, it was exactly like Ready Player One.
[1557.46 → 1561.72] And Ready Player One is all about escaping, but it's not what Apple went.
[1561.84 → 1571.06] But the point I'm trying to make is, like, if you've seen that film, these goggles, Vision Pro, look almost, like, shape-wise identical.
[1571.54 → 1572.84] And you can see through them.
[1572.92 → 1575.10] So there's a lot of, like, inspiration.
[1575.10 → 1578.36] Like, you've got, what was the thing called from Star Trek?
[1578.42 → 1579.86] I'm not a Star Trek fan, unfortunately.
[1580.48 → 1582.08] That was, like, the iPhone.
[1582.56 → 1583.18] Yeah, the recorder.
[1583.36 → 1583.68] Recorder.
[1583.68 → 1584.32] Recorder.
[1584.52 → 1586.70] So, like, that predated the iPhone.
[1586.88 → 1590.36] So, like, there's science fiction meets, you know, future reality.
[1590.54 → 1595.36] So at some point we dream about it, and then they're like, well, that's actually really possible if we do this, this, and this.
[1595.70 → 1596.70] Digital crown that.
[1596.86 → 1597.60] Speakers here.
[1597.98 → 1602.14] And, you know, on our iPhones today we have all those cameras in the front to do Face ID and whatnot.
[1602.14 → 1605.86] Like, they've already got a lot of the tech in place.
[1605.96 → 1608.18] You know, I don't know if it's, what's the material of this thing?
[1608.20 → 1608.64] Is it aluminum?
[1609.08 → 1610.14] Like, the rest of their gear?
[1610.14 → 1619.44] According to them, a singular piece of three-dimensionally formed laminated glass flows into an aluminum alloy frame that curves to wrap around your face.
[1619.70 → 1620.10] Aluminum.
[1620.60 → 1621.12] Aluminum.
[1621.12 → 1621.38] Go ahead.
[1621.52 → 1622.36] Aluminum, indeed.
[1622.36 → 1625.76] Yeah, so, like, I was going to say, I think that's the interesting thing about it as well.
[1625.82 → 1633.12] Because I think the other thing that may help bring the price down is right now that thing has so many freaking sensors on it, right?
[1633.20 → 1636.04] Like, it's got, like, I think it's like 15 cameras.
[1636.30 → 1638.00] It's got the iris reader on the inside.
[1638.08 → 1644.00] It's got that screen on the outside to, like, show you the eyes of the person inside because.
[1644.40 → 1645.24] The creepiest part.
[1645.24 → 1646.22] You need to see that.
[1646.58 → 1648.18] Yeah, like, it's got all this stuff.
[1648.50 → 1653.62] Like, when you're Apple size, right, you can build loads of things.
[1653.74 → 1653.92] Yeah.
[1654.04 → 1656.78] Throw them at the wall, right, and see what sticks.
[1657.14 → 1658.66] I don't think that's a bad thing either.
[1658.76 → 1660.26] I'm not criticizing that.
[1661.14 → 1663.40] Mike's dog Lucy makes a cameo here shortly.
[1663.76 → 1665.70] Don't worry, she only sticks around for a minute or so.
[1665.80 → 1669.24] And her second cameo near the end of the show is totally on point.
[1669.24 → 1671.68] I'm not criticizing that.
[1671.92 → 1680.48] I'm jealous because, you know, I'm co-founding a startup nowadays where we have the exact opposite problem of, like, grand visions and.
[1680.98 → 1681.60] Lack of resources.
[1681.94 → 1682.10] Yeah.
[1682.24 → 1687.24] And right now, like, 1.4 people to actually build them.
[1687.80 → 1689.82] But, yeah, like, it's interesting.
[1689.82 → 1699.70] And it wouldn't surprise me if that's what ends up bringing the price down is that they can have the non-pro edition or whatever just doesn't have the screen on the front, right?
[1699.74 → 1701.74] Because no one, turns out no one cared about that.
[1701.84 → 1705.22] And even, like, you know, we've been talking a lot about the AR, VR thing.
[1705.32 → 1710.52] And arguably, this is a device where there's been a few devices in the past in this kind of space.
[1710.72 → 1715.42] I would say all of them are primarily VR or primarily AR.
[1715.42 → 1724.80] And this is the one that does seem to be, like, it is being described as an AR device, but it's definitely one that seems equally competent at both, right?
[1724.92 → 1726.50] I think it was the Microsoft HoloLens.
[1726.60 → 1729.58] I never actually used one in person, but that was a lot more of an AR thing.
[1729.76 → 1744.26] Like, the Valve Index I've got here, it has two, like, basically black and white cameras on it for doing really limited AR of, like, you know, am I going to step into a wall without, like, it does, like, when I get too near to a wall,
[1744.26 → 1749.58] it shows, like, a green sort of matrix-style outline of, like, what I'm near or whatever.
[1750.08 → 1752.98] So I can kind of see and step out the way and all this type of stuff.
[1753.36 → 1759.40] They could have gone, right, let's stick some really high-end cameras in here and make an amazing AR device and build amazing AR games.
[1759.44 → 1760.80] But they decided to not do that.
[1760.86 → 1762.18] They decided to go the VR direction.
[1762.66 → 1771.40] So it does make me wonder whether if Apple decides to go full AR, they can probably throw away a bunch of the kinds of VR side of things and make something that might look a bit better.
[1771.40 → 1780.56] Because that's the other reason why they're ski goggles and not glasses, right, is if you want to do VR and you want to have that level of immersion, you have to be able to block out all the light.
[1780.82 → 1781.24] Everything else.
[1781.58 → 1781.86] Exactly.
[1782.46 → 1791.38] But then on the AR side, if you want to do that, you're going to have a lot more high-end cameras, and you have to be able to maybe do some of the kind of eye-tracking stuff and things like that.
[1791.56 → 1795.54] I guess that was another interesting thing we've not mentioned as well is, like, there are no controllers.
[1795.54 → 1802.18] That's another distinction between all the VR kit is its all, like, hand gestures, eye gestures, all this type of stuff.
[1802.24 → 1802.50] Right.
[1802.62 → 1805.70] As opposed to these, like, physical controllers and stuff like that.
[1805.74 → 1809.74] And that's going to be another thing that it's going to be interesting to see how well that goes, right?
[1810.22 → 1811.76] Yeah, they didn't show us how you calibrate it.
[1811.78 → 1818.18] Like, with Face ID, you've got to do that weird head motion to, you know, teach the thing, you know, your face from all angles.
[1818.38 → 1819.76] So they didn't show any of that calibration stuff.
[1819.88 → 1820.38] So it was probably like—
[1820.38 → 1822.70] So Sarah Kitschy said there's, like, one or two-minute setup.
[1822.98 → 1823.22] Okay.
[1823.28 → 1824.58] It's like a two-minute eye calibration.
[1824.58 → 1826.38] She said the eye-tracking is spectacular.
[1826.66 → 1829.50] Like, you look at the thing, and it focuses the, you know, the context.
[1829.60 → 1831.86] Like, if you look on this Safari tab, it's going to switch tabs.
[1832.20 → 1836.08] And she says it works pretty much the way you'd expect it to work very, very well.
[1836.34 → 1841.70] She didn't talk about the hand gestures to me because there's, like, downward-facing cameras that are, like, looking at your hands.
[1842.32 → 1846.78] And as you, you know, you pinch and stuff with your hands, just the air, and that's the other aspect.
[1846.90 → 1852.26] So it's eyes and finger motions, which to me kind of looks like the person in the demo in the video is, like,
[1852.26 → 1856.68] having a mini seizure, you know, as they sit on their couch and their hands are, like, shaking in weird ways.
[1856.76 → 1862.92] But I guess we do all kinds of weird things, you know, like talking to the air with our AirPods in our head.
[1862.92 → 1871.52] And I guess the idea that you can use one of your existing input devices as well, you can use your keyboard or mouse on your Mac or your game controller or whatever.
[1871.66 → 1878.72] But, like, I mean, it's definitely, again, in comparison to, like, the actual hardware I have, like, the Valve Index has kind of some of the kind of better controllers.
[1879.26 → 1883.78] And, like, they have these that you put your hands inside, and then it has finger tracking.
[1883.78 → 1890.96] So when I do, like, this, I can see in a game, say, like, my fingers move around because it knows where my fingers are all relative to the controller.
[1891.20 → 1891.48] Right.
[1891.54 → 1893.36] But I'm not having to actually, like, hold the thing.
[1893.44 → 1898.14] It's, like, sort of attached in this weird, if anyone's on the podcast, you can go and look that up.
[1898.20 → 1900.72] You can see how your hand sort of fits in, sort of like a glove.
[1901.42 → 1905.80] And, again, it's the thing where, I guess, moving on to kind of gaming stuff as well,
[1906.00 → 1911.12] they had a slide about gaming where I think they showed up something like their 11 kind of launch games.
[1911.12 → 1913.66] But I don't know. I love Apple and I love games.
[1914.00 → 1923.06] But I think for, like, people who would describe themselves, like, as a gamer and play, like, AAA big budget games, like, Apple's not a meaningful gaming platform.
[1923.28 → 1923.48] Right.
[1923.54 → 1931.50] It's, like, something where, you know, if you're someone who plays a game for a couple of hours every year, you can get enough stuff that you could play a game on your Mac or whatever.
[1931.66 → 1932.62] Like, that's fine.
[1932.64 → 1937.08] But if you want to do, like, serious gaming on your Mac, like, you're in for a pretty sad time.
[1937.08 → 1942.66] And, like, in some ways, like, that, here are our launch titles, like, this kind of 11 things.
[1942.84 → 1950.44] Like, the fact that you can fit them on a slide is, like, is very Apple, like, in a good and a bad way.
[1950.64 → 1950.90] Right.
[1950.98 → 1957.80] Because it shows, like, we've carefully selected these, like, 11 beautiful representations or whatever.
[1957.88 → 1960.36] One of the games is one that I have played in VR.
[1960.36 → 1966.36] I guess it's almost like being, like, our drinks' menu in our restaurant has 11 drinks on it.
[1966.44 → 1966.64] Right.
[1966.92 → 1971.74] Across all alcoholic and non-alcoholic drinks, we've selected 11 of the nicest drinks.
[1971.86 → 1973.92] And it's like, well, I don't like any of those.
[1974.34 → 1976.04] Well, okay, don't come to our restaurant.
[1976.28 → 1979.30] Go to the one next door where the drinks' menu has 200 instead.
[1979.50 → 1979.66] Yeah.
[1979.66 → 1991.02] And, like, that's the sort of Apple take it or leave it sort of way that, like, to me shows that they're not, again, certainly I think a lot of people thought that this was going to be, like, primarily a gaming device.
[1991.36 → 1993.72] And that's very much not what they're doing.
[1993.84 → 2001.04] Like, in some ways, I find it interesting that they had any mention of gaming at all because it seems to be so not what they're going for.
[2001.04 → 2001.08] Sure.
[2001.60 → 2003.10] Let's fill up the script a little bit, though.
[2003.16 → 2009.94] Let's not look at it from a, I've got a Valve index and I kind of know some things like you do.
[2010.04 → 2012.56] Think of it from a game developer standpoint.
[2012.78 → 2014.98] What do you think game developers are thinking about this?
[2014.98 → 2024.16] Like, if you're in that space, and you can make things for brand new, I mean, we have to recognize this is sort of a brand-new world, a brand-new computing platform.
[2024.84 → 2027.64] What do you think game developers are thinking?
[2027.64 → 2031.44] While there may only be 12 in this launch, and you got to start somewhere.
[2032.48 → 2032.88] 11.
[2033.06 → 2033.28] Sorry.
[2033.46 → 2035.04] I was going for the baker's dozen.
[2035.80 → 2036.60] Actually, that's 13.
[2036.82 → 2037.26] Sorry about that.
[2038.50 → 2039.38] Either way, I have one more.
[2040.34 → 2041.14] What do you think, Mike?
[2041.14 → 2042.82] What do you think the game developers are thinking?
[2042.92 → 2044.32] Like, what do you think about this paradigm?
[2044.80 → 2052.08] Because I'm thinking, like, you could do some fascinating things with it, not in the typical gaming way, potentially, even.
[2052.16 → 2053.44] Like, what do you think they're thinking about?
[2053.90 → 2056.48] I'm friends with some game developers, but I've never worked in that space.
[2056.48 → 2061.68] But I think the interesting thing there is, like, even PC VR gaming, right?
[2061.76 → 2064.82] The long-running joke about it has been its kind of a niche within a niche, right?
[2064.88 → 2077.76] Because I have, for reasons due to not wanting to reward scalpers and all this type of thing, I have, like, a, you know, one and a half K dollarwise graphics card in my machine.
[2077.76 → 2081.26] That sounds like a small jet engine in my house.
[2081.36 → 2083.00] It's ludicrously overpowered.
[2083.32 → 2091.22] Like, and I have, as I said, like, all my VR setup that required me to physically drill things into my walls to mount my VR stations.
[2091.42 → 2093.52] And, you know, I guess the point I'm making is, like...
[2093.52 → 2094.08] You went pretty far.
[2094.36 → 2095.82] It's taking it pretty far, right?
[2095.96 → 2096.22] Right.
[2096.66 → 2097.06] Enthusiast.
[2097.06 → 2103.44] But even all of this stuff, you're probably talking less than half the price of the vision, right?
[2103.62 → 2103.90] Right.
[2103.98 → 2105.14] So I think that's the thing.
[2105.22 → 2119.14] I think if you're targeting it as a game developer, you would need to be targeting, like, either multiple platforms, in which case you're somewhat limited in being able to do really intriguing things just for the vision alone.
[2119.14 → 2126.78] Or you're targeting it thinking this is going to become a mass market device when they bring the cost down or whatever it may be.
[2127.18 → 2132.22] Like, or you're doing it as, like, some interesting proof of concept that kind of, like, buys into another platform, whatever.
[2132.40 → 2138.80] But imagine how it is right now where it's, like, I don't know, say, like, Sony has announced the PS6 or whatever.
[2139.14 → 2140.68] And they're going to release it in 2024.
[2141.02 → 2142.74] And it's going to cost you $3,500.
[2143.36 → 2145.22] And you can only buy it in North America.
[2145.22 → 2151.20] Like, people would probably not be rushing out to build stuff for that and really excited about that.
[2151.30 → 2157.46] And that's the opposite of the direction that console gaming seems to have gone, where it's more and more commodity hardware.
[2157.82 → 2164.02] It's more and more, like, kind of incremental changes and not this kind of big bang revolutions and stuff.
[2164.24 → 2165.36] Massive paradigm shifts, yeah.
[2165.60 → 2166.82] I think the potential is huge.
[2166.90 → 2174.04] Like, I think, like, you could do some really, fascinating things, I think, particularly with the kind of the VR AR blend there.
[2174.04 → 2181.12] That I've looked for a long time for games that will use the even very limited, like, AR kind of functionality in my VR headset.
[2181.26 → 2186.26] Just because I think it's sort of an intriguing idea to sort of, like, combine those two spaces.
[2186.60 → 2187.58] But I don't know.
[2187.62 → 2192.70] It just seems like it's so expensive right now that it would be hard to see that.
[2192.70 → 2205.62] I guess the thing I could maybe see, like, rather than games, is, like, for high-end training or whatever, like, flight simulation or the type of thing where basically almost like conference tickets, right?
[2205.62 → 2215.80] Where the idea, like, of, again, now that I'm actually, like, a co-founder somewhere, you notice the fact that, like, oh, this conference costs, like, two or three thousand dollars.
[2216.04 → 2220.64] Like, that's actually quite a lot of money when I can't get my employer to pay for it for me, right?
[2220.64 → 2228.52] Like, I'm probably not going to pull out my credit card and spend the price of, like, a family vacation on going to a conference.
[2228.90 → 2228.92] Like.
[2229.10 → 2229.52] For sure.
[2229.66 → 2231.96] And I feel it could be the same in reverse here, right?
[2231.96 → 2237.46] Where am I, as a gamer, going to, like, buy one because some launch title looks really great?
[2237.60 → 2238.76] Like, no.
[2239.00 → 2253.36] But, like, if my employer can get more than 3.5K's worth of value out of it, and it's dramatically better than some of the alternatives there, then, yeah, I wouldn't imagine that would be particularly hard for people to justify.
[2253.86 → 2259.44] Like, if you could kind of tap into that sort of market, I guess, like, high-end training for whatever.
[2260.10 → 2260.50] Yeah.
[2260.50 → 2272.00] Such a small, well, maybe not a small market, but such a specific market where, like, you almost have highly specialized devices where Apple is not known to be OpenAI.
[2272.16 → 2275.90] They're not known to be not literally Open APIs and the OpenAI.
[2275.98 → 2276.72] You get what I'm trying to say.
[2277.32 → 2281.80] You know, that you can program for it, but you don't have full access like you do even on a Mac.
[2281.80 → 2291.20] You have a lot more access to the system, you know, in iOS devices, tvOS, etc., iPadOS, and now VisionOS.
[2291.56 → 2300.52] I got to imagine, like, these highly specialized things require certain APIs that you may not have access to, you know, and you're going to spend a lot of money to get into that ecosystem.
[2300.52 → 2307.08] And you sort of have to follow where Apple may allow you to go because they're in control of the keys, the kingdom.
[2307.60 → 2308.80] So, specialized.
[2309.12 → 2310.80] That's a highly specialized spot, for sure.
[2310.80 → 2317.14] Well, I did think, like, when, Mike, you held up that controller, like, that thing screams video games, right?
[2317.20 → 2317.34] Yeah.
[2317.34 → 2323.42] Like, just, like, you have buttons, you have D-pads, you have joysticks, etc.
[2323.42 → 2328.74] And the fact that there is nothing like that, it's such a more of an iPhone kind of thing, right?
[2328.74 → 2334.94] Like, it's an Apple thing to be like, well, we're going to have cool new games that you're going to use your fingers to, you know, manipulate the air and play.
[2335.16 → 2337.52] And it's like, that's going to create a certain type of game.
[2338.04 → 2344.58] Just like the iPhone, you know, the single pane of glass created a certain kind of game that was different from other kinds of games.
[2344.58 → 2355.18] And I feel like they had a huge opportunity, they had so much interest, and still do, of just people using these things to create a gaming platform that just blew everything else out of the water.
[2355.66 → 2359.60] And they just did kind of what they did to the podcast for many years, was just ignore it, you know?
[2359.76 → 2360.78] They just let it go.
[2360.90 → 2366.52] They didn't provide the developers what they need to really have a different monetization option.
[2366.52 → 2380.56] So everything went in-app purchase, everything went Candy Crush, and it ended up being like these very shallow, addictive, but ultimately, I guess, unsatisfying games that ended up ruling the iOS platform.
[2380.76 → 2392.32] And it's probably similar, I would guess, that eventually would rule this thing, unless they actually get dedicated to it early in order to provide developers, game developers, what they need to make better games.
[2392.32 → 2396.22] And I just don't see Apple ever, like you said, Mike, I just don't think they care about it that much.
[2396.22 → 2397.76] They're going to have their 11 games.
[2398.30 → 2404.58] They'll all be beautiful and very handpicked, but ultimately, you're like, well, I get bored with 11.
[2405.02 → 2407.62] In fact, I only like three of the 11, and now what are we going to do?
[2410.50 → 2411.38] Hello, friends.
[2411.78 → 2415.02] This is Jared here to tell you about Changelog++.
[2415.70 → 2423.22] Over the years, many of our most diehard listeners have asked us for ways they can support our work here at Changelog.
[2423.46 → 2425.90] We didn't have an answer for them for a long time.
[2426.22 → 2433.04] But finally, we created Changelog++, a membership you can join to directly support our work.
[2433.26 → 2444.26] As a thank you, we save you some time with an ad-free feed, sprinkle in bonuses like extended episodes, and give you first access to the new stuff we dream of.
[2444.72 → 2448.14] Learn all about it at changelog.com slash plus.
[2448.14 → 2451.66] You'll also find the link in your chapter data and show notes.
[2452.16 → 2455.32] Once again, that's changelog.com slash plus.
[2455.46 → 2456.14] Check it out.
[2456.54 → 2457.54] We'd love to have you with us.
[2457.54 → 2464.66] Let me give you a scenario.
[2464.76 → 2466.14] You're in the doctor's office, right?
[2466.18 → 2468.08] You're there waiting for your next turn, right?
[2468.10 → 2470.20] You're just there for a random checkup.
[2470.26 → 2470.82] You're good to go.
[2471.06 → 2471.40] Okay.
[2471.40 → 2480.20] And, you know, somewhere in the room, you got now you currently have like an iPhone talk or somebody's on the phone talking super loud in a waiting room.
[2480.28 → 2482.60] It's just like a non-social norm, right?
[2483.10 → 2487.14] Now, flip the script and say, okay, now affordable, years down the road, whatever.
[2487.14 → 2493.88] Even today, whenever this thing's available, somebody's sitting next to you with this Vision Pro on their face, and you can kind of see their eyes or whatever.
[2494.08 → 2497.60] You can just, maybe you hear nothing from them because maybe, I don't even know.
[2497.74 → 2498.64] I don't know if it makes sound.
[2498.70 → 2501.04] If it's just for you or if it's for everybody else, they can hear it.
[2501.26 → 2504.54] But just imagine them going to town on like whatever it could be.
[2504.58 → 2505.44] It could be Candy Crush.
[2505.54 → 2508.54] They could be like, they could be safariing.
[2508.60 → 2509.50] They could be photoing.
[2509.58 → 2510.58] They could be doing whatever they want.
[2510.70 → 2512.14] You know, like just imagine that scenario.
[2512.14 → 2516.92] Like you see somebody sitting across to you with this Vision Pro on their face in a social setting.
[2516.92 → 2517.74] Which is totally possible.
[2517.88 → 2519.18] Fully immersed in Tetris.
[2519.40 → 2519.58] Yeah.
[2519.88 → 2520.32] What are you thinking?
[2520.62 → 2522.64] Well, obviously I'd just, I'd steal their wallet.
[2523.46 → 2524.22] That's the move.
[2524.40 → 2524.74] For sure.
[2525.76 → 2528.90] It wouldn't have anything in it because they've bought an Apple VR headset.
[2528.92 → 2529.32] That's right.
[2529.38 → 2529.76] They're broke.
[2530.56 → 2533.30] You got to steal the goggles if you're going to steal anything of value.
[2533.70 → 2533.96] I don't know.
[2534.00 → 2539.42] It's funny because with a lot of the VR stuff, like you've seen some of those transitions for games as well.
[2539.56 → 2541.22] I've seen this with my kids as well.
[2541.22 → 2546.22] Like Fruit Ninja, the iPhone game, they have a VR version that my like five-year-old,
[2546.92 → 2548.32] really likes.
[2548.32 → 2554.58] Where you physically have two actual swords that you use to cut fruit coming through the air and stuff.
[2554.70 → 2559.14] And I think that's the fascinating like paradox with VR stuff is that it is,
[2559.50 → 2565.50] you don't need instructions or tutorials for most games because it's immediately obvious.
[2565.70 → 2569.94] Like you can put someone who's not even a gamer in and within seconds they know
[2569.94 → 2572.90] because it's what you're doing in the space and whatever.
[2572.90 → 2579.22] But on the flip side, you have this problem which a small minority of people have with like existing games.
[2579.32 → 2585.18] So I had a flatmate at university college who couldn't play first-person shooters because they made it motion sick, right?
[2585.46 → 2587.30] And I'd be like, you're just making that up.
[2587.36 → 2588.28] That's not true.
[2588.42 → 2591.10] And I saw him and I was like, oh, that's actually a thing, right?
[2591.26 → 2591.38] Yeah.
[2591.38 → 2597.84] But with VR, like that affects a lot more people and a lot, like some people just can't really handle VR games.
[2597.92 → 2601.04] And certainly like VR where you have like motion and stuff like that.
[2601.10 → 2605.04] Like if you're sitting in a moving car in VR, I played a lot of VR.
[2605.24 → 2607.28] I don't get motion sick in real life and stuff like that.
[2607.40 → 2610.52] But that will make me motion sick and I need to stop, right?
[2610.58 → 2612.20] And some of that is like programming.
[2612.36 → 2615.68] Some of that is just like essential, like how your brain works.
[2615.68 → 2622.80] And, you know, it's tricky because I think that's the other thing that could stop this going, for gaming at least, going super-duper mainstream.
[2623.14 → 2629.62] It's like you just can't necessarily build something that everyone's brain and vision system and stuff like that can handle.
[2630.26 → 2643.98] I guess one of my biggest fears, though, of all of this is that like this, whenever Apple releases some big visionary product like this, I think of, do you guys remember the legendary like slash dot comment from Commander Taco 2001?
[2643.98 → 2644.46] Yes.
[2644.46 → 2648.12] About the iPod, no wireless, less space than a nomad.
[2648.56 → 2648.86] Lame.
[2649.10 → 2649.34] Lame.
[2649.42 → 2649.72] Right.
[2649.92 → 2650.28] Yes.
[2650.40 → 2651.60] He still isn't living it down.
[2651.66 → 2651.98] Exactly.
[2652.14 → 2661.46] And you just, I can just imagine like everything we've said in this conversation today brought up in five or ten years when everyone just wearing their goggles 24-7.
[2661.92 → 2664.22] And we're just like, you guys are such fools.
[2664.60 → 2665.36] You knew nothing.
[2665.46 → 2665.74] Right.
[2665.88 → 2666.38] What would come.
[2667.06 → 2669.62] And how we'd all embrace our Apple goggles.
[2669.62 → 2676.96] The lore inside could be enough at some point, but like I just come back to current, I don't know, would you call it user experience to be how you wear it?
[2677.08 → 2678.48] I think it's more like inside the thing.
[2679.16 → 2681.02] It's more like just experience generally.
[2681.32 → 2682.38] It's a headset.
[2682.72 → 2682.94] Right.
[2683.50 → 2686.62] Who wants to wear a headset for several hours at a time?
[2686.70 → 2687.88] I barely want to wear these headphones.
[2688.04 → 2689.22] And I'm a, you do, Mike?
[2689.40 → 2690.06] Mike does it.
[2690.16 → 2690.48] Gosh.
[2690.50 → 2691.44] He's playing his games.
[2691.80 → 2694.74] So like I, again, I'm with you to an extent I would put on the headset.
[2694.82 → 2696.14] And I've played the VR games.
[2696.14 → 2697.74] I feel like an old person right now.
[2697.80 → 2698.54] I've played the VR.
[2699.12 → 2706.60] I love, I've had a lot of fun, even with groups, you know, because like you're watching the person, they're acting a fool, and you can get them to cast up onto a TV.
[2706.74 → 2707.92] So you're kind of seeing what they're seeing.
[2707.96 → 2710.62] It's not exactly the same, but you're actually there with them for an extent.
[2711.06 → 2711.78] And it's a riot.
[2711.88 → 2713.74] Like it's not isolationist.
[2713.80 → 2716.96] Like it can be a communal experience, which is really cool.
[2717.18 → 2719.30] But that's for a constrained time period.
[2719.80 → 2724.02] And I'm not going to wear anything for all day long on my face.
[2724.02 → 2733.86] But even that, like the thing that makes it social is the fact that the person in VR who's actually getting to play right now when everyone else is not able to play looks like a massive dork.
[2734.08 → 2734.18] Right?
[2734.30 → 2734.68] Like that.
[2734.90 → 2735.48] Yeah, exactly.
[2735.64 → 2736.84] That is the bonding experience.
[2736.84 → 2740.88] It's like you're having the time of your life, and you look like a loser while you're doing it.
[2740.94 → 2741.12] Right?
[2741.54 → 2741.90] Right.
[2742.08 → 2742.36] Oh my gosh.
[2742.38 → 2747.74] It's hard to see that almost like mapping to like a Fortune 500 boardroom, you know?
[2750.32 → 2751.84] Well, maybe it would.
[2751.84 → 2753.66] You know, let the boss use it for a while.
[2753.66 → 2757.26] And I'll laugh at the boss, you know, while they're doing their thing.
[2757.60 → 2757.86] Yeah.
[2758.14 → 2759.86] Here's Jared coming in on their Vision Pro.
[2760.44 → 2761.32] Hey, Jared, how are you doing?
[2761.46 → 2763.38] And they're augmented, basically.
[2763.76 → 2765.76] Speaking of that, they have this FaceTime feature.
[2766.02 → 2766.90] Like how does that work?
[2766.92 → 2769.10] Because you can FaceTime inside the Vision Pro.
[2769.62 → 2772.32] But if I'm on the other side of that call with you, right?
[2772.56 → 2773.48] I'm seeing what?
[2773.56 → 2775.04] Because you have goggles on.
[2775.30 → 2776.48] Am I seeing just your eyes?
[2776.70 → 2777.48] You're seeing Zuck.
[2777.52 → 2778.58] You're seeing Zuckerberg, man.
[2778.68 → 2780.36] It's the persona thing, right?
[2780.60 → 2782.16] Like they had, it's like this.
[2782.16 → 2783.32] So that's more metaverse.
[2783.32 → 2783.72] Yeah.
[2783.82 → 2786.04] It's almost like this little like fuzzy avatar thing.
[2786.10 → 2788.08] I think they had a little bit of that during the demo.
[2788.26 → 2788.58] I didn't.
[2788.84 → 2789.08] Okay.
[2789.16 → 2790.04] I might have missed that part.
[2790.30 → 2790.44] Yeah.
[2790.88 → 2791.28] Yeah.
[2791.64 → 2792.56] Seems not ideal.
[2792.68 → 2796.44] But, you know, again, we are seeing what we've seen yesterday.
[2796.66 → 2798.82] But, you know, this is going to be a product that iterates.
[2798.92 → 2803.18] Apple is so good at just relentless iteration.
[2803.44 → 2804.82] Just year after year.
[2804.82 → 2808.40] Small incremental changes that after five, ten years.
[2808.54 → 2809.06] It's amazing.
[2809.22 → 2815.96] I mean, the iPhone 4 and 5, those models compared to the original iPhone.
[2816.28 → 2820.26] It's absolutely astonishing how much progress they made in half a decade.
[2820.44 → 2820.58] Yep.
[2820.94 → 2821.14] Yeah.
[2821.14 → 2825.74] If you have the original iPhone or the 3, 4, 5, and now what?
[2825.78 → 2826.30] The 14?
[2826.30 → 2829.20] You see the progress in the iteration.
[2829.58 → 2832.98] And I think that Apple is the kind of company that would not get into the ring unless they
[2832.98 → 2834.58] can do some damage, essentially.
[2834.78 → 2837.26] They can do something with the platform.
[2837.36 → 2842.64] And even if it's a niche for a while, that's probably okay for them because that's why it's
[2842.64 → 2843.60] priced so high.
[2843.68 → 2845.00] So they can go down from here.
[2845.10 → 2845.96] You can't go up.
[2845.96 → 2850.80] If you came out at like, you know, $5.99 and $8.99, maybe that's a harder selling point
[2850.80 → 2851.14] for them.
[2851.96 → 2853.86] They're not going to get in the ring unless they could do something.
[2854.20 → 2854.70] That's for sure.
[2854.96 → 2856.02] That's the kind of company they are.
[2856.02 → 2863.80] So they've definitely made everybody pay attention to spatial design, augmented, and if not VR,
[2864.30 → 2866.20] then, you know, augmented reality, AR.
[2866.80 → 2872.66] Something that Box founder Aaron Levy said, and this just sort of like kind of goes back
[2872.66 → 2875.34] to some things you said, Jared, about Sarah Kitschy.
[2875.34 → 2877.74] He says, just got to try the Apple Vision.
[2878.00 → 2878.72] Definitely wild.
[2879.26 → 2882.04] Hand and eye tracking is basically perfect.
[2882.64 → 2884.36] Instantly understandable UX.
[2884.90 → 2887.66] The graphics are incredible, and the setup was seconds.
[2887.86 → 2891.82] So that gives you like a good base, like even wherever it could go.
[2892.40 → 2894.96] It's got an incredible, you know, easy setup.
[2895.08 → 2895.94] It's not kludge.
[2896.02 → 2896.62] It's not hard.
[2896.64 → 2899.64] So all the things you can improve on it over time will only get better.
[2899.72 → 2903.26] The weight, the size, you know, whatever it might be.
[2903.26 → 2905.94] Maybe they introduced controllers next year.
[2906.08 → 2907.66] Hey, now we have these controllers making.
[2907.82 → 2908.36] Now you're happy.
[2908.70 → 2914.58] And by the way, we can give you like these coin sized, just slap on your wall sensors rather
[2914.58 → 2915.20] than having to drill.
[2915.28 → 2920.36] You just tape it, and it's there, and it's infinitely powered by, I don't know, gravity or something
[2920.36 → 2920.76] like that.
[2920.76 → 2925.64] So you've got, you know, in a year's time, maybe you can have a couple of years time,
[2925.70 → 2929.68] you can have brand-new paradigm shifts in this platform that make it far more appealing.
[2930.22 → 2930.96] I think that's interesting.
[2931.28 → 2935.02] I guess the thing is, I keep forgetting this myself because I get so overexcited.
[2935.16 → 2939.44] But, you know, my wife has seen me phone over enough Apple product launches that she was
[2939.44 → 2943.76] like, yeah, but didn't you always say that you shouldn't buy the first generation of new
[2943.76 → 2948.14] Apple stuff because the second release is always like fixes all the huge problems.
[2948.14 → 2950.24] And I was like, yeah, yeah, you're right.
[2950.44 → 2953.52] Like that for me is like that combined with the price.
[2953.64 → 2957.66] I think Apple are, again, really lucky with their customer base because a ton of people
[2957.66 → 2958.90] are going to go out and buy this, right?
[2958.94 → 2964.46] And give them really great feedback on what the second iteration of the device should be.
[2964.52 → 2968.72] And when they do make a device that's half the price, a third, the price, whatever, like
[2968.72 → 2972.28] what the mass market needs that device to be.
[2972.76 → 2976.02] And the other thing that occurred to me while you were talking, Adam, is just like the
[2976.02 → 2976.82] demo they did yesterday.
[2976.82 → 2979.48] I mean, they're so good at like these types of demos.
[2979.64 → 2980.58] It's kind of absurd.
[2980.78 → 2986.14] Like, and when you look at the head start that Meta has had here, I'm like, I mean, basically
[2986.14 → 2993.30] Meta have been like gaming and this weird second life metaverse thing that like everyone just
[2993.30 → 2995.10] like literally laughs at, right?
[2995.18 → 3000.78] Whereas Apple, before they were even ready to show the headset to anyone, they have like
[3000.78 → 3002.30] 20 integrations, right?
[3002.30 → 3007.06] Like in the demo, and they've got a bunch of launch partners on board, and they've got Disney
[3007.06 → 3007.58] on board.
[3007.58 → 3012.50] And like, you know, they're just, I mean, obviously it's an early product, but it's an early Apple
[3012.50 → 3012.90] product.
[3012.90 → 3014.62] And like the level of polish, right?
[3014.62 → 3021.46] I've seen various memes today about like how Zuck must be feeling after that keynote yesterday.
[3021.60 → 3022.96] But like, yeah, I mean, it's...
[3022.96 → 3024.02] I'd be excited if I were him.
[3024.22 → 3025.44] It's not good, right?
[3025.48 → 3029.92] If you're a company that's like betting on the metaverse and someone who's not even in
[3029.92 → 3035.12] this space comes along and like does this, like it reminds me of when the iPhone came
[3035.12 → 3035.54] out, right?
[3035.60 → 3039.26] And all the phone companies were like, I literally remember speaking to a high level Nokia executive
[3039.26 → 3043.08] about six months after the iPhone came out, and they said, we're not worried.
[3043.26 → 3044.22] They're not a phone company.
[3044.86 → 3048.02] Like, and it's like, well, now you're not a phone company.
[3049.10 → 3049.54] Right.
[3050.06 → 3050.26] Right.
[3050.66 → 3054.34] You know, and it makes me wonder whether we could say the same sort of thing with like
[3054.34 → 3059.46] VR and metaverse and AR and whatever, where it's like, you just didn't deliver a good enough
[3059.46 → 3064.76] product and someone else has taken their time, delivered something good and your lunch
[3064.76 → 3065.52] could well be stolen.
[3065.52 → 3065.64] Yeah.
[3066.90 → 3071.02] Well, what's interesting about this time around is that Apple has announced and shown their
[3071.02 → 3073.34] cards, but there's no pre-sale.
[3073.44 → 3074.92] There's no, you know, get it here.
[3075.12 → 3076.00] It's a year away.
[3076.18 → 3077.36] I mean, they're saying it's next year.
[3077.64 → 3078.90] That's a long time period.
[3078.98 → 3083.42] I remember the first iPhone, I think it was six months announced in January, shipped at
[3083.42 → 3084.76] the end of June, something like that.
[3085.30 → 3088.70] I think the Apple Watch was maybe another six months, maybe three quarters of a year.
[3088.76 → 3089.42] I can't remember exactly.
[3089.84 → 3090.04] Yeah.
[3090.10 → 3090.52] Good point.
[3091.06 → 3092.72] I had to be North America as well.
[3092.72 → 3093.08] Yeah.
[3093.08 → 3096.08] And, you know, prohibitively expensive for consumers.
[3096.34 → 3098.70] So three things that they don't normally do.
[3098.76 → 3100.34] They're definitely changing their playbook slightly.
[3100.48 → 3105.00] I wonder why they felt like they had to get it out there a year before they're actually
[3105.00 → 3105.64] ready to ship.
[3105.72 → 3110.36] It was a pressure from something that I know that the rumour mill had been, you know, swirling
[3110.36 → 3110.92] for years.
[3111.30 → 3116.30] They said that they've been building the technology for a decade, but I think I heard they've been,
[3116.56 → 3120.04] they've actually had a dedicated team earnestly working on this for seven years.
[3120.04 → 3123.16] So, I mean, that's a long time to work without ever shipping something.
[3123.30 → 3125.48] Maybe it was like, you know, we got to ship something.
[3125.88 → 3127.50] They're still not shipping, but they're at least they're showing.
[3128.32 → 3129.38] That's interesting to think about.
[3130.16 → 3130.92] Why now?
[3131.68 → 3136.32] Well, one thing Insider did say, a headline at least, that we can potentially agree on
[3136.32 → 3139.30] is Apple short kicked Meta's butt today.
[3139.46 → 3139.86] Right?
[3139.86 → 3142.34] That's their headline.
[3142.48 → 3143.24] That's their headline.
[3143.42 → 3145.90] And they say, Apple finally released its new headset Monday.
[3146.32 → 3150.06] It sure seems a lot better than Meta's headset if the marketing is to be believed.
[3150.52 → 3153.24] But does anybody really want to put something on their face like this?
[3153.80 → 3154.86] And Mike, you raise your hand.
[3154.92 → 3155.40] You say, yeah.
[3155.52 → 3156.88] So I guess the answer is yeah.
[3157.42 → 3159.26] If I were Zuck, though, I'd be like, you know what?
[3159.28 → 3162.06] I'm a little worried because they're good at hardware.
[3162.48 → 3163.86] They're being Apple.
[3163.86 → 3170.34] But at the same time, it's like, here's part of the Fang mafia, basically, throwing their
[3170.34 → 3172.82] product into the ring to say, let's go to battle.
[3173.14 → 3175.48] It just deepens the pot, really.
[3175.66 → 3177.10] Like, it's going to be the future of something.
[3177.18 → 3177.76] Who wins?
[3178.14 → 3178.98] Doesn't really matter.
[3179.18 → 3182.74] I mean, will Apple take over the entire market share?
[3183.26 → 3183.86] I don't know.
[3184.04 → 3184.88] Android's still out there.
[3184.94 → 3186.40] There are still tons of Android users.
[3186.88 → 3192.52] Just because Apple's out there kicking butt and taking Meta names doesn't mean that Meta
[3192.52 → 3195.46] can't still find a way to make their own place.
[3195.62 → 3201.04] And maybe they're focused on immersive, true VR, which is quite different from this.
[3201.16 → 3206.96] But if Apple gets this right in this augmented space, like you said before, Mike, it's not
[3206.96 → 3210.86] a far stone's throw to get into the VR space, too.
[3211.04 → 3216.62] Like, if they conquer this and rule this, they could have two products, Vision Pro and Vision
[3216.62 → 3216.90] VR.
[3217.28 → 3218.92] You know, they can divide the market.
[3219.20 → 3219.64] It is interesting.
[3219.74 → 3221.90] They shipped with a pro, like, in the whole concept.
[3221.90 → 3223.44] Like, they're announcing the Vision Pro.
[3223.64 → 3223.86] Right.
[3223.92 → 3227.02] And, like, normally you announce a product and then you kind of come out with the pro
[3227.02 → 3227.34] line.
[3227.46 → 3228.52] I mean, that's been their style.
[3228.78 → 3229.00] Right.
[3229.08 → 3230.58] But maybe they're just like, this thing is so expensive.
[3230.68 → 3231.50] We've got to call it the pro.
[3231.78 → 3232.20] I don't know.
[3232.56 → 3233.42] That could be it, Jared.
[3233.76 → 3234.56] That's how I read it.
[3234.92 → 3238.32] And also just like what I was saying earlier about, like, the number of sensors and,
[3238.44 → 3243.80] like, the amount of functionality this device has is, like, unnecessary for some of
[3243.80 → 3244.66] the use cases, right?
[3244.84 → 3249.36] I actually really wouldn't be surprised if you end up essentially with the pro.
[3249.36 → 3251.80] So this is why they don't let me work in branding.
[3252.04 → 3257.24] Whether you have something like a Vision AR, a Vision VR, and then the Vision Pro could
[3257.24 → 3259.46] kind of do both of those things, right?
[3259.48 → 3263.96] And has essentially all the sensors and all the chips for both devices.
[3264.54 → 3267.64] And instead, the other two devices are like a third of the cost.
[3268.54 → 3269.98] What about the Vision Pro Max?
[3270.14 → 3271.08] When are they going to come out with that?
[3271.08 → 3274.58] That's just if you've got a huge head.
[3275.62 → 3275.90] Yeah.
[3276.82 → 3280.86] Well, I guess somewhat sliding into that concept, you know, people wear glasses.
[3281.20 → 3282.14] And so this is something.
[3282.30 → 3283.16] Like, what about Adam?
[3283.20 → 3284.10] He's got glasses.
[3284.22 → 3285.32] Are those just for fashion?
[3285.44 → 3286.76] Or are those actually corrective?
[3286.98 → 3288.46] These are corrective and fashion.
[3288.50 → 3288.70] Okay.
[3288.76 → 3290.46] So you got corrective lenses on over there.
[3290.82 → 3292.26] And the thing's expensive as is.
[3292.26 → 3294.18] But they have a solution for glasses wearers.
[3294.30 → 3296.58] They partner with some sort of lens company.
[3296.94 → 3297.22] Weiss.
[3297.34 → 3298.32] I didn't pay close attention.
[3298.54 → 3298.82] Weiss.
[3298.82 → 3302.08] The most well-known lens maker in the world.
[3302.36 → 3302.60] Okay.
[3302.68 → 3303.78] Of course, Apple would do that.
[3304.08 → 3307.18] You can buy lenses for your goggles, or they fit them perfectly.
[3307.26 → 3308.14] I don't know exactly how it works.
[3308.60 → 3312.60] But so like if you have bad vision, you're paying even more, right?
[3312.62 → 3316.92] You got to have the corrective lenses added to your goggles.
[3317.14 → 3318.26] So that's interesting.
[3318.46 → 3318.60] Yeah.
[3318.64 → 3320.32] And this one doesn't work with old versions.
[3320.32 → 3324.34] So now you got to get new lenses, and you're trying to sell your exact prescription on eBay.
[3324.66 → 3325.16] Trying to hawk it.
[3325.50 → 3326.30] What a world, right?
[3326.36 → 3326.74] What a world.
[3326.74 → 3330.50] And you can't swap lenses because they've been like, you know, sealed into the thing.
[3330.74 → 3332.08] Because that's the way Apple does it.
[3332.60 → 3333.88] Where are we all most excited?
[3333.94 → 3337.54] I've got a most excited myself where I would put down some dollars for this.
[3337.82 → 3341.18] Not at this price point, but I would put out, and maybe, I don't know.
[3341.76 → 3345.74] It would be to combine this kind of thing with what I already have.
[3345.78 → 3347.56] I was saying in our Apple Nerds chat.
[3347.60 → 3350.04] By the way, you heard Jared mention that at the top of the show.
[3350.12 → 3350.92] We have a Slack.
[3351.00 → 3351.72] You can join it.
[3351.72 → 3353.58] ChangeLaw.com slash community.
[3353.70 → 3354.26] It's totally free.
[3354.40 → 3359.44] Hang with Mike, me, Jared, and many others whenever WWDC happens and other things.
[3359.86 → 3365.72] But I would combine Vision Pro with an existing home theatre setup.
[3366.18 → 3369.38] So if I could take, I mean, and maybe you already have your screen and that's super cool.
[3369.58 → 3376.52] But if this thing is to be believed, and it is that cool, and I can immerse myself, imagine if I can watch a movie as if I'm hovering over the earth.
[3376.52 → 3377.12] Right.
[3377.38 → 3383.30] The augmented reality around me, you know, my reality is sort of like, is there still yet to some degree if somebody walks in?
[3383.50 → 3389.52] But I'm hovering above the earth, or I'm kind of hanging out in the universe, and I've got this just massive screen in front of me.
[3389.82 → 3393.80] And I've got a banging sound system around me literally there.
[3393.80 → 3400.46] So I don't have to listen on, you know, headphones or whatever the Vision Pro offers in terms of audibility.
[3400.66 → 3407.44] I can use existing high end, super awesome audio and this thing to just make the experience different.
[3407.78 → 3410.50] That might be something that's pretty cool.
[3410.88 → 3414.14] It is still a niche because I mean, how many people have banging home theatres?
[3414.26 → 3417.64] Not many people, but they are people who shell out lots of dollars.
[3417.64 → 3418.08] Yep.
[3418.30 → 3423.26] And just to give an example, I bought a 120-inch screen.
[3423.74 → 3424.56] This is not a TV.
[3424.68 → 3427.16] This is just a screen to project onto recently.
[3427.66 → 3429.56] More than $3,000 for this thing.
[3429.80 → 3430.34] Oh my goodness.
[3430.62 → 3430.92] Oof.
[3431.22 → 3431.38] Yeah.
[3431.64 → 3432.04] $3,500?
[3432.30 → 3433.52] You could have got a Vision Pro.
[3433.74 → 3434.28] I could have gotten.
[3434.38 → 3435.22] Yeah, I could have gotten a Vision Pro.
[3435.76 → 3437.02] I could have gotten a Vision Pro.
[3437.48 → 3440.06] But so you got people like that are willing to spend that kind of thing.
[3440.62 → 3442.82] I mean, you could build your own, but it's not as good.
[3442.82 → 3446.70] I mean, yeah, I won't make excuses for why I justified the expenditure.
[3446.70 → 3448.08] But I did.
[3448.32 → 3448.82] You did it.
[3448.96 → 3452.90] $3,500 for this just screen to project onto on the wall.
[3453.74 → 3455.68] So I mean, people will pay for experiences.
[3456.06 → 3456.98] Well, they do for sure.
[3457.38 → 3463.68] I mean, for me as well, I'm currently sporting a nice pair of Apple AirPods Max.
[3463.82 → 3469.02] I actually own, I have AirPods, AirPods Pro and AirPods Max, and I use them all in different
[3469.02 → 3469.70] situations.
[3469.92 → 3471.42] Oh man, you collected them all.
[3471.42 → 3475.46] But like, yeah, like the Max, like they're so expensive.
[3475.46 → 3479.56] And I really weighed it up for a long time, like whether I would get them.
[3479.66 → 3481.96] And I was like, okay, I'm going to indulge myself.
[3482.14 → 3483.02] Would you buy them again?
[3483.40 → 3483.68] Yeah.
[3484.06 → 3484.48] In a heartbeat.
[3484.74 → 3485.74] They're absolutely incredible.
[3485.88 → 3486.32] That's the thing.
[3486.42 → 3491.50] And I think like that's part of the thing that makes me think with Apple on these cases,
[3491.66 → 3491.86] right?
[3491.86 → 3496.06] Is that the funny thing is for me is like the pairing, when you were talking about that,
[3496.18 → 3499.54] Adam, like I kind of want what you want, but almost the opposite.
[3499.54 → 3504.30] And I do have a pretty nice surround sound system at home and stuff like that.
[3504.42 → 3510.28] But whenever I watch like TV or movies right now, like it's generally when my kids are sleeping,
[3510.44 → 3510.62] right?
[3510.64 → 3516.76] And if I watch some like war movie or the Game of Thrones finale, like I'm quite an audio
[3516.76 → 3517.72] influence person.
[3517.84 → 3520.82] I'm a sort of pre-children musician, all this type of thing, right?
[3520.82 → 3526.30] So for me, like I love the idea of being able to watch like Lord of the Rings or some other
[3526.30 → 3533.78] big epic battle scene with my AirPods Max on over my ears, like my vision on my face,
[3533.98 → 3537.62] have this enormous cinema screen, have it like absolutely blasting into my ears.
[3537.72 → 3539.14] And I'm not bothering anyone else, right?
[3539.30 → 3539.46] Yeah.
[3539.54 → 3541.66] And I could do that in my house when my kids were sleeping.
[3541.76 → 3543.40] I could do that on a plane.
[3543.54 → 3545.06] That was the other case that I could see.
[3545.22 → 3549.82] If I was doing a lot of business travel, like I had done in the past, I'm not any more really.
[3549.82 → 3555.76] But if I was travelling like long haul every month or so, people would drop almost half
[3555.76 → 3558.64] that on really decent noise-cancelling headphones, right?
[3558.78 → 3565.06] So like the idea that like it's the best possible way to watch a movie on a plane, like people
[3565.06 → 3565.94] would do that, right?
[3566.04 → 3567.46] Or be able to work on a plane.
[3567.46 → 3571.36] Like if you can have all your desktop in front of you, like, yeah, it's not as nice as your
[3571.36 → 3576.00] 4K display, but slapping the stewardess accidentally as she walks by because you're pinching and
[3576.00 → 3576.20] zoom.
[3576.20 → 3577.28] Oh, I didn't mean to pinch you.
[3577.70 → 3578.56] I was trying to pinch Safari.
[3578.94 → 3579.56] That's terrible.
[3579.98 → 3581.34] I wasn't, I didn't pinch you on purpose.
[3581.80 → 3584.04] You can get yourself, you know, thrown in jail for that.
[3584.22 → 3584.60] That's right.
[3585.04 → 3587.70] Actually, the plane is the most compelling moment.
[3587.80 → 3589.56] Like when would I actually use this?
[3589.62 → 3592.56] For me, it's none of the real life moments like that they demoed.
[3593.04 → 3596.82] It's literally like when I see them on a plane and thinking like, what do I want to do when
[3596.82 → 3597.34] I'm on a plane?
[3597.42 → 3599.54] I want to just tune out everything around me.
[3599.82 → 3600.00] Yeah.
[3600.00 → 3601.62] And have some sort of distraction.
[3601.92 → 3606.50] And for me, like that epic movie with the spatial audio right there in your ears, it
[3606.50 → 3607.80] blacks out everything else.
[3607.90 → 3611.96] I go full VR mode and watch a movie for two hours on a two-hour flight.
[3612.50 → 3614.10] Like that to me, like, I would like to do that.
[3614.16 → 3616.50] I want to go there, but that's pretty much it.
[3616.60 → 3617.26] Everything else.
[3617.38 → 3620.78] I don't even like to have, like, I'm watching a movie on my iPhone, like holding it here.
[3620.94 → 3621.08] Yeah.
[3621.12 → 3622.54] I set it on my leg.
[3622.56 → 3624.34] I put it on the table in front of me.
[3624.76 → 3626.78] I'm always like, is this person next to me watching?
[3626.88 → 3631.32] Actually, I watched Game of Thrones one time on a plane for like a few minutes, and it was
[3631.32 → 3632.48] inappropriate.
[3632.88 → 3636.36] I was like super embarrassed, you know, because you have to like to tell the person like, no,
[3636.40 → 3637.12] this is Game of Thrones.
[3637.20 → 3638.70] This is not soft core, you know?
[3638.90 → 3639.22] Yeah.
[3639.38 → 3641.26] And they're just not going to hear you on that.
[3641.38 → 3643.86] So I don't like that experience on a plane.
[3643.90 → 3647.10] I would love to just tune everybody else out and be able to have an escape.
[3647.50 → 3648.12] Yeah, that's true.
[3648.28 → 3649.48] This would make it totally private.
[3649.48 → 3650.66] No one else can see what you're seeing.
[3651.18 → 3653.34] And yeah, that's exactly where I would want to do that.
[3653.34 → 3658.48] And I would even say when they get the price point down, if they can just make it about
[3658.48 → 3663.42] immersive viewing of any sort, maybe not, you know, interacting like a game, but immersive
[3663.42 → 3663.80] viewing.
[3664.44 → 3668.80] Anybody that has the tiniest apartment would totally drop some down on this.
[3668.84 → 3673.54] Because like if you can skip buying a TV for 500 bucks, 300 bucks and fill the rest with it
[3673.54 → 3678.46] up with, you know, the remaining amount with the expense of buying this, and you have immersive
[3678.46 → 3682.26] viewing, then maybe, and you live alone potentially even, and you only have cats.
[3682.26 → 3686.58] You know, there's a this is getting more and more niche, but either way you have, you don't
[3686.58 → 3690.26] have the ability to install a screen or, you know, it's not really feasible to put a big
[3690.26 → 3691.56] old TV there or something like that.
[3691.64 → 3696.86] All it really requires is maybe internet and, and battery.
[3697.22 → 3698.62] That to me is interesting.
[3699.04 → 3699.88] That's the other thing.
[3699.94 → 3704.30] Like, even if it is feasible to get the screen, you know, like we've, I've been historically
[3704.30 → 3710.64] limited by previous houses and by my lovely spouse on like how big our TV is allowed to
[3710.64 → 3710.92] be.
[3711.22 → 3711.46] For sure.
[3711.76 → 3716.42] And now we're in a place that like we could have a edentulous size TV.
[3716.62 → 3722.30] And once you start to get huge OLED TVs, like you're definitely stepping above the
[3722.30 → 3724.22] vision pro in terms of a price point, right?
[3724.46 → 3725.66] They're expensive for sure.
[3725.82 → 3730.28] Like, so I guess that's another thing is that like, if they can nail the experience such
[3730.28 → 3736.72] that like, it is actually a cinema, like movie theatre, uh, like experience then.
[3736.94 → 3737.28] Yeah.
[3737.40 → 3739.04] Again, maybe that's compelling, right?
[3739.04 → 3744.76] Like if you're really into watching stuff, like can have one more nail in the coffin of
[3744.76 → 3749.36] the current kind of, uh, cinema movie theatre industry post COVID.
[3749.94 → 3754.98] Well, I mean, there's usually only one person maybe who really enjoys the biggest of big TVs.
[3755.12 → 3758.68] I mean, everyone else will endure it if they have to, but like, there's usually one person
[3758.68 → 3763.68] vying for the biggest experience, the most expensive things in my whole household.
[3763.76 → 3764.50] It's usually me.
[3764.64 → 3767.38] My wife's like this size TV is perfectly fine.
[3767.68 → 3772.60] And I've moved on to projectors and screens versus TVs because I want big.
[3773.02 → 3776.30] As I mentioned, my screen is 120 inches diagonal.
[3776.46 → 3780.02] So that's like way bigger than most TVs you can buy at a feasible price.
[3780.84 → 3783.84] Although I did disclose how much I pay for the screen only.
[3784.28 → 3788.54] So there's that either way, you know, you can drop the dime.
[3788.68 → 3792.46] This thing, because you got one person maybe in the household who's really wanting the
[3792.46 → 3794.42] more immersive version of it, you know?
[3794.42 → 3798.50] So maybe you get a typical TV or a common TV for everybody else.
[3798.50 → 3801.14] And then you get the vision pro for the one person who's like, you know what?
[3801.64 → 3803.62] I want to hover above the earth and watch a film.
[3803.62 → 3810.58] I love the mental picture of like having like a 20-inch TV that everyone is watching perfectly
[3810.58 → 3815.34] happy with, except for like Michael Adam, who's just sitting there with a vision pro on their
[3815.34 → 3818.82] face, watching it on like the virtual.
[3819.22 → 3820.46] With the biggest smile ever.
[3820.56 → 3820.76] Yeah.
[3820.86 → 3822.78] The virtual biggest TV in the world.
[3823.76 → 3824.06] Yeah.
[3824.42 → 3825.44] All by himself.
[3825.44 → 3830.40] So there were, believe it or not, there were other things announced at this event.
[3830.50 → 3832.30] We've been talking about this the whole time.
[3832.44 → 3832.54] We can.
[3832.72 → 3835.72] I was going to say, Jay, we're, we're deep on vision pro only.
[3835.82 → 3838.12] We can stop here, or maybe we can hit on a few things.
[3838.16 → 3843.14] Maybe let's just talk on a few highlights from each of us on the other things mentioned.
[3843.14 → 3846.66] Because they are shipping some new hardware, 15-inch MacBook airs.
[3846.78 → 3848.60] The Mac studio gets an upgrade.
[3848.98 → 3853.04] Mac pro for the first time with Apple Silicon, by the way, talk about banking.
[3853.04 → 3857.40] Starting at 69 99, seven grand starting price on that.
[3857.48 → 3861.74] So, you know, that's not the actual price you're going to pay when you land one of those,
[3861.74 → 3868.26] as well as iOS 17 updates, a bunch of stuff, iOS, iPad, OS 17, new macOS.
[3868.66 → 3872.52] We don't have time to go through everything, but what were some highlights for you guys from
[3872.52 → 3873.08] this event?
[3873.16 → 3877.74] Looking forward to things that are actually shipping either right now or soon.
[3878.26 → 3882.98] So for me, a bizarre one that really stuck out was like the family sharing.
[3883.04 → 3884.54] For iCloud keychain.
[3885.26 → 3889.42] I'm sad to say that I have fallen out of luck with one password.
[3889.52 → 3891.16] I was a one password very early adopter.
[3891.26 → 3893.56] I've like got all my family using it and all this type of stuff.
[3893.78 → 3898.96] And I just, in the last year or so, it's felt like it is annoying me more than it helps me.
[3899.06 → 3901.90] And stuff that used to work, it's not working anymore and whatever.
[3902.44 → 3902.80] So, yeah.
[3902.88 → 3907.86] So like, it's one of those things where I'm a kind of like, if I can use the defaults and
[3907.86 → 3911.90] if I can use Apple's built-in stuff, I generally try and do that.
[3912.04 → 3918.08] So for me, like the iCloud, like family sharing of passwords, like that's the one thing that
[3918.08 → 3922.92] was my super hard blocker for me, able to like potentially move myself and my wife or
[3922.92 → 3927.06] even like my parents over to using iCloud keychain instead.
[3927.34 → 3927.46] Yeah.
[3927.46 → 3927.96] So, yeah.
[3928.06 → 3930.12] So for me, like that's, that's pretty compelling.
[3930.24 → 3934.38] Like I'll need to kind of give that an investigation of whether I can kind of migrate over.
[3934.66 → 3938.32] The issue with one password is not, it's not native, and it's never going to be native.
[3938.70 → 3940.32] I mean, it's native to the platform.
[3940.68 → 3942.34] I guess actually it's not now.
[3942.54 → 3945.02] It's less native now because now they're on Electron.
[3945.26 → 3945.62] Exactly.
[3945.72 → 3949.66] It's going to be always a third party application, obviously, unless it gets acquired by Apple.
[3950.12 → 3953.80] The problem for me, Mike, and I want to believe in that world, is that I have things
[3953.80 → 3956.14] that aren't only in the Apple ecosystem.
[3956.14 → 3962.18] And so for those reasons, it makes me want to have a robust, not first party, because
[3962.18 → 3964.68] I'm not only in the Apple world.
[3964.88 → 3968.40] And I store other things in their like credit cards and driver's license and just other sensitive
[3968.40 → 3973.46] information that I would not want to have to put on an encrypted disk or in a password
[3973.46 → 3977.92] protected file, you know, with permissions or whatever like that to some degree harder
[3977.92 → 3980.06] to share because I can't share that.
[3980.30 → 3981.64] So I want to believe in that.
[3981.64 → 3986.08] If they can do what they can do first party, but also give me actual one password.
[3986.14 → 3986.90] Type of things.
[3987.34 → 3991.54] Store my driver's license in there, you know, store my credit cards in there, share them
[3991.54 → 3994.52] with my wife and other family members or whatever that would be.
[3994.62 → 3997.52] And I guess I kind of do that already with like purchase sharing to some degree, like
[3997.52 → 3998.20] wallet or whatever.
[3998.40 → 4004.52] If they can kind of make that more in the Apple world, but also let me have things that are
[4004.52 → 4008.84] non-Apple in there and an actual application to control it, then I'd be in it with you.
[4009.16 → 4012.78] Because I like the idea of the sharing, but that's why I've never really bought into the
[4012.78 → 4017.02] Apple first party ways because I need more than it gives.
[4017.72 → 4021.74] I've heard this said, I think maybe Jason Snell wrote about it, but what they really need
[4021.74 → 4024.80] is an actual password app, you know, like a first party.
[4024.80 → 4027.52] Because it's in there, like it's part of the settings.
[4027.66 → 4031.04] It's super weird when I have to like to show my parents that, yeah, you can just get your
[4031.04 → 4031.60] passwords out there.
[4031.68 → 4032.08] Like how?
[4032.20 → 4036.38] I'm like, well, I just swipe down and search for passwords, and it's had different names
[4036.38 → 4037.76] throughout the years, throughout the versions.
[4038.00 → 4040.88] And so it's really just an unknown feature for so many people.
[4040.94 → 4044.20] But like if they had an actual app, just like they have a wallet app, have an app called
[4044.20 → 4046.30] passwords with all this stuff centralized.
[4046.30 → 4051.08] I think that would go a long way for people realizing how good their password offerings
[4051.08 → 4051.28] are.
[4051.32 → 4054.18] Because they have, I mean, you can do one time passwords, you can do all kinds of stuff
[4054.18 → 4057.28] inside there, but people just don't know about it.
[4057.34 → 4058.88] So they should do that.
[4059.18 → 4061.56] I just used my first passkey today with Home Depot.
[4061.56 → 4066.72] I actually enabled Home Depot to have a passkey to allow it to use the device, the website
[4066.72 → 4071.42] to use either my thumbprint, which I'm not using, or my face ID.
[4071.88 → 4074.46] So that's first passkey user literally yesterday.
[4074.46 → 4077.42] So yeah, GitHub's passkey support is pretty good, actually.
[4077.72 → 4081.80] Like I think they maybe even shipped like after I left, but yeah, it works pretty nicely,
[4081.80 → 4082.08] actually.
[4082.18 → 4086.10] Like it's just whenever you would have been prompted for 2FA, like you just get prompted
[4086.10 → 4090.32] for your biometric information, and it's synced between all your devices using iCloud.
[4090.58 → 4094.98] And, you know, if you need to log in on a Windows machine, it can't be like your only like
[4094.98 → 4096.46] secondary authentication or whatever.
[4096.58 → 4098.66] But yeah, it works pretty nicely for another one.
[4098.94 → 4100.82] And yeah, I think I enabled on my Google account as well.
[4100.82 → 4107.42] So it will similarly do that instead of prompting for my 2FA code or spamming my YouTube app
[4107.42 → 4107.96] on my phone.
[4108.54 → 4109.74] That is a kludge experience.
[4110.20 → 4110.78] It's secure.
[4111.26 → 4116.68] 2FA with like a verify or authenticator, I believe it's called, is secure, but it's
[4116.68 → 4117.68] not convenient.
[4118.02 → 4120.46] It's like, oh gosh, let me get this OTP out real quick.
[4120.58 → 4122.84] And it's just not cool.
[4123.06 → 4123.88] I got to remember it.
[4124.16 → 4127.50] And then if you're like in a social setting, you can potentially be phished quickly.
[4127.50 → 4127.94] Yeah.
[4128.06 → 4131.36] Because I don't know about you, but I can't remember six characters without like somehow
[4131.36 → 4135.30] saying them out loud, either my brain or literally out loud to myself.
[4135.36 → 4137.58] I might whisper it like 603452.
[4138.26 → 4141.88] It's like, you know, I got to do that to some degree to like remember that six-digit number.
[4142.32 → 4143.22] Okay, Jared, what about you?
[4143.28 → 4145.00] What's something that stood out to you for this one?
[4145.00 → 4147.06] Find my Apple TV remote already.
[4147.20 → 4148.00] Come on, people.
[4148.72 → 4149.12] Finally.
[4149.76 → 4155.10] They're breezing through the Apple TV portion, and they announced that you can now find your
[4155.10 → 4160.66] Apple TV remote from your phone when you lose it, which we lose ours constantly.
[4161.42 → 4163.76] And I've long said they just need to put an AirTag in that thing.
[4163.84 → 4166.62] Just build an AirTag into the Apple TV remote.
[4167.06 → 4169.90] What's interesting is this just seems like a software upgrade.
[4170.02 → 4173.90] Like they didn't say, and you have to get a new Apple TV remote, or I don't know if it
[4173.90 → 4175.12] like makes a noise.
[4175.30 → 4176.36] It was also fast.
[4176.36 → 4179.68] I'm sure I could go back and watch it again and see exactly how it works, but somehow
[4179.68 → 4181.72] I'm sure it makes a noise, or it locates.
[4182.66 → 4187.42] And so, yeah, you know, you got your Apple TV between the couch cushions or your three
[4187.42 → 4191.44] year old takes it downstairs to the other TV for some reason and leaves it, and you lose
[4191.44 → 4192.52] it for days upon days.
[4193.16 → 4195.30] No longer going to find that sucker.
[4195.58 → 4199.18] So that, I mean, it's small, but like quality of life improvements.
[4199.94 → 4201.64] Did you guys see how this is going to work?
[4201.66 → 4202.38] I didn't see it.
[4202.38 → 4206.56] All I know is it's like just with a new TV OS, it's going to work now.
[4206.70 → 4207.34] It's like, what?
[4207.66 → 4208.88] Why did you guys wait so long?
[4209.12 → 4213.16] I thought it was going to be like the hardware literally didn't exist inside the remote, you
[4213.16 → 4213.34] know?
[4213.90 → 4215.88] And so you have to upgrade your remote to get the findable one.
[4215.98 → 4217.32] I figured they would do that eventually.
[4217.70 → 4219.78] Like, and this new Apple TV has a findable remote.
[4219.78 → 4221.56] Is the remote Bluetooth or is it IR?
[4221.92 → 4222.34] It's Bluetooth.
[4223.10 → 4224.52] Well, then that means it's already there, right?
[4224.58 → 4228.92] Like you can just like beak into the Bluetooth with your phone or your network.
[4229.16 → 4232.48] That's why you have that allow applications to search your network thing.
[4232.62 → 4232.72] Yeah.
[4232.74 → 4235.98] But does that give, like, how do they know where it's located in the room?
[4236.14 → 4237.54] Does Bluetooth provide that?
[4237.86 → 4238.36] Oh, that's true.
[4238.42 → 4238.56] Yeah.
[4238.58 → 4239.44] I guess spatially.
[4240.88 → 4241.82] True, man.
[4242.00 → 4244.04] They're tracking my stuff already.
[4244.34 → 4247.82] If any of you all know how they're doing this, holler at us because I would love to know.
[4247.82 → 4251.14] But I don't actually care all that much because as long as it works, I can find my remote.
[4251.68 → 4252.56] Life's going to be good.
[4253.18 → 4257.26] I'm excited about the completion of the Mac transition to Apple Silicon.
[4257.76 → 4258.72] That's what I'm excited about.
[4259.04 → 4260.10] Just being done.
[4260.28 → 4261.18] I'm sure you are too, Mike.
[4261.30 → 4263.16] I'm like, you're like, no more surprises.
[4263.54 → 4263.74] Okay.
[4264.08 → 4266.46] We got some OS surprises once every two years.
[4266.88 → 4271.80] Let's have no more hardware surprises or any other chip surprises that you can't navigate around.
[4271.94 → 4272.82] You know what that means?
[4272.98 → 4277.22] Which I knew this today would be coming from basically the day they announced the M1 chip, right?
[4277.22 → 4282.90] It's like counting down the days until there is a macOS release that does not support Intel anymore.
[4283.32 → 4291.18] You should run a sweepstakes or something for the listeners of like, how many more releases do we get after Sonoma before?
[4291.72 → 4294.38] If you're on an Intel chip, you can't upgrade, right?
[4294.78 → 4298.34] Oh, probably two more, three more, maybe I'd say.
[4298.52 → 4298.70] Yeah.
[4298.72 → 4300.36] I think about that sort of ballpark as well.
[4300.42 → 4304.06] Like I would be surprised if they killed it off like next year or whatever, but like.
[4304.24 → 4305.52] They'll freeze you to a certain OS.
[4305.52 → 4309.44] Are they still selling Intel based anything?
[4309.72 → 4310.64] As of this, no.
[4310.84 → 4312.32] The last one was this Mac Pro.
[4312.50 → 4313.36] They were still selling it.
[4313.44 → 4315.44] When did they sell their very last Intel?
[4316.18 → 4320.82] So as of yesterday or maybe Sunday, they may have sold a Mac Pro that was Intel.
[4320.94 → 4326.16] With laptops, they've not been selling Intel like MacBooks for two years plus probably now.
[4326.42 → 4330.12] It was funny how much of the ecosystem had not woken up to this.
[4330.12 → 4339.32] I definitely saw a few times when some companies ended up with slightly unpleasant situations announcing that, oh, we will support doing this on M1 in a few years.
[4339.32 → 4344.64] And be like, oh, everyone who buys a new Apple MacBook today cannot run your stuff anymore.
[4345.16 → 4349.82] Had a slightly faster turnaround once one of their internal developers pointed that out to them.
[4349.82 → 4357.30] But the M2 Ultra, which I heard in the chat, it was everyone could say M1 Ultra, which is a mind control thing.
[4357.42 → 4358.42] MK is mind control.
[4359.38 → 4360.48] Yeah, there's a perfect movie.
[4360.88 → 4362.98] I think it's called Kill Room, if I recall correctly.
[4362.98 → 4371.46] If you haven't seen that film, and you like the idea of M1 Ultra and not so much the idea of it, but like just storylines around it.
[4371.58 → 4373.18] What about the Manchurian Candidate?
[4373.26 → 4375.10] Wasn't that also about M1 Ultra?
[4375.28 → 4375.48] Yes.
[4375.48 → 4376.20] The Manchurian Candidate.
[4376.44 → 4378.26] Well, I would say Kill Room is better, though, than that movie.
[4378.34 → 4378.52] Okay.
[4379.08 → 4379.28] Yeah.
[4379.46 → 4381.06] Manchurian Candidate was a perfect movie, too, though.
[4381.68 → 4381.96] Okay.
[4382.12 → 4383.18] But just not as good as Kill Room.
[4383.64 → 4384.44] Pick which one you want.
[4384.70 → 4384.84] Yeah.
[4385.00 → 4385.94] Watch both, Jared.
[4386.00 → 4386.44] You know this.
[4386.78 → 4387.98] Why choose one where you can watch both?
[4388.42 → 4388.88] That's true.
[4389.04 → 4389.54] Watch them both.
[4389.54 → 4393.36] So M2 Ultra, and now I guess PCI Expansion.
[4394.22 → 4403.18] I won't need it myself, but, you know, anybody who needs like massive amount of NVMe storage, you can get carrier cards, PCI Expansion cards, which I think is pretty cool.
[4403.26 → 4406.74] You can have 30 some terabytes of NVMe storage.
[4406.84 → 4408.78] So if you're doing like, I don't know.
[4409.08 → 4409.18] Right.
[4409.24 → 4410.04] That's where I fail.
[4410.26 → 4413.42] I can't even hypothesize what you might be doing, but you have extreme needs.
[4413.76 → 4414.72] Well, there you go, then.
[4414.80 → 4416.04] You can do that with the Mac Pro.
[4416.04 → 4418.68] I think that's kind of cool that they left it because they could have abandoned it.
[4418.68 → 4428.98] I mean, not many people need PCI Expansion, but when you have a device with a $7,000 starting price tag, you should probably keep that, right?
[4429.40 → 4430.54] Just for the enthusiast.
[4430.68 → 4432.68] You can get two Vision Pros for that much.
[4432.82 → 4433.20] I mean, come on.
[4433.20 → 4433.40] That's right.
[4434.06 → 4439.34] Does anyone else have the least favourite feature that was announced yesterday, one that you're dreading?
[4439.52 → 4440.46] Oh, good question.
[4440.56 → 4441.10] Good question.
[4441.10 → 4453.00] Mine was them changing the Hey Siri to being just Siri because I have, maybe it's the Scottish accent, but I have a dog called Lucy and a wife called Lindsay.
[4453.00 → 4462.22] And when I say either of those things, all of my devices, particularly Lucy, like when I'm angry at my dog for doing something disgusting, I'm like, Lucy!
[4462.80 → 4467.48] Then like all of my devices are like, oh, like, you're asking for me?
[4467.64 → 4470.80] Like, yeah, they all already think that I'm asking for Siri.
[4471.04 → 4477.00] So I look forward to every time I say my dog's name, every Apple device spamming me.
[4477.00 → 4479.30] Yeah, that's a good one.
[4479.52 → 4484.36] So while you're talking Siri, I should close the loop on my prediction from a few months back.
[4484.48 → 4487.62] So I went on record when we had Simon Willison on the show.
[4487.72 → 4489.30] I think that was LLM's Break the Internet.
[4489.52 → 4496.56] And I said, I think this year's WWDC, which is usually in June, end of May, early June.
[4496.76 → 4500.70] I think Apple is going to have an answer to what's all been going on.
[4500.76 → 4503.44] I think they can't afford to do nothing for much longer.
[4503.44 → 4510.28] My guess is they're going to have some sort of either like upgraded Siri or Siri replacement that will be LLM powered.
[4511.10 → 4513.88] And I think they almost have to at this point.
[4514.30 → 4515.64] So I think it's coming.
[4515.76 → 4516.50] I think they're just waiting.
[4516.94 → 4524.28] I agree that they got some serious constraints around the way it needs to work and how good it has to be in order to keep their brand intact.
[4524.36 → 4526.04] But I think they're going to have something to announce.
[4526.10 → 4527.24] And I have no idea.
[4527.38 → 4528.42] It just makes sense.
[4530.16 → 4531.70] And they totally didn't.
[4531.70 → 4539.58] They did mention transformer powered autocorrect and transformer based dictation inside the keyboard.
[4539.74 → 4544.68] Those are like I was waiting for the large language model keyword, and they never use it.
[4544.72 → 4550.86] They did mention transformers a few times, but Siri didn't get touched except for taking the hay off the front was pretty much all they've done there.
[4550.94 → 4552.12] So Siri still useful.
[4552.24 → 4552.74] I was wrong.
[4553.24 → 4555.96] I thought they would step up their game in that way.
[4556.18 → 4557.02] I'm sad you're wrong.
[4557.08 → 4561.10] Honestly, I really wish they would just make Siri more intelligent.
[4561.10 → 4561.54] Yeah.
[4561.84 → 4563.54] Siri is terrible at this point.
[4563.68 → 4565.16] Like it's kind of embarrassing.
[4565.56 → 4566.38] So bad.
[4566.58 → 4567.16] It's embarrassing.
[4567.62 → 4573.48] It almost feels like with Siri, like when you compare Siri to something like, I know it's got the voice recognition part as well.
[4573.56 → 4581.78] But like when you compare Siri to like ChatGPT or whatever nowadays, it's like what we were saying earlier about like meta and, you know, how Zuck must be feeling right now.
[4581.78 → 4589.60] Like it's just, yeah, like Siri's imagine trying to use Siri for like the stuff that you're trying to use ChatGPT for, right?
[4589.64 → 4590.64] It's embarrassing, right?
[4590.68 → 4594.32] Like it's a Nokia compared to an iPhone back in whatever it was, 2007.
[4594.86 → 4595.80] Like it's.
[4596.06 → 4596.84] They're not a phone company.
[4596.84 → 4597.40] Yeah.
[4597.64 → 4606.90] It feels like the tough conflict there is like Apple's approach to AI about being very privacy focused, very on device as much as possible.
[4607.62 → 4610.60] Maybe that just means you can't do AI well, right?
[4610.68 → 4617.20] Like compared to the like privacy invasive, we're wrong 1% of the time approach.
[4617.68 → 4617.72] Like.
[4617.82 → 4618.02] Right.
[4618.02 → 4622.98] I kind of respect them for that if that's the case, but yeah, I still just wish it was a bit better.
[4623.36 → 4627.84] It seems like we're moving to a place where Apple's on device stuff is really going to pay off.
[4627.88 → 4633.50] It just, they're just sleeping on it because the ability to take these large models, put them on your device, right?
[4633.86 → 4639.00] Pre-trained and then fine tune and do inference on device just makes to me a lot of a sense.
[4639.16 → 4644.18] In terms of least wow moments, like when I'm going to go to the bathroom, I don't really care that this was announced,
[4644.18 → 4647.60] but I honestly don't care that it was announced was new app journal.
[4648.24 → 4649.38] I just went to the bathroom.
[4649.64 → 4650.84] Oh, that's a bummer.
[4651.22 → 4652.60] I just don't care about their journal app.
[4653.26 → 4654.02] I don't journal.
[4654.68 → 4655.50] I don't want it.
[4655.56 → 4656.14] I don't need it.
[4656.20 → 4660.36] It's going to go into a folder or whatever you call that thing and never be used again.
[4660.42 → 4661.26] But that's just me.
[4661.32 → 4662.06] Adam, what about you?
[4662.16 → 4663.56] Least favourite and then we'll call it a show.
[4664.08 → 4666.68] Well, I want to layer on one for you with that.
[4666.80 → 4672.18] So day one is a pretty well known, well-designed iOS, macOS native application.
[4672.18 → 4674.70] I believe I don't think they're on other platforms.
[4674.82 → 4675.30] I could be wrong.
[4675.84 → 4678.50] It's no, actually it says Android, iPad and Mac.
[4678.58 → 4679.74] So maybe they're on Android.
[4680.38 → 4681.80] I think the journaling is a good thing.
[4681.94 → 4684.70] I was not excited about it, but it's kind of cool that it might be native.
[4684.92 → 4685.90] Just like free form.
[4686.34 → 4690.54] I think for me, I kind of go to sleep anytime iPad's mentioned because I'm not an iPad user
[4690.54 → 4692.56] and I see some of the things they're doing there.
[4692.62 → 4693.46] I'm like, that's kind of cool.
[4693.52 → 4698.76] But every time I see myself wanting to use an iPad, I think it might be consumption.
[4698.76 → 4700.04] But then I'm like, I got this big phone.
[4700.04 → 4703.96] So I can just like to sacrifice some pixels for this experience.
[4704.28 → 4708.46] I know Nick Needed in the chat said that he primarily uses his iPad for consumption.
[4708.76 → 4713.54] And I'm just like, you know, in every case, shape and form, if I was a digital artist and
[4713.54 → 4719.74] I use the Apple pen and I used specific things that the iPad enables for an artist, then I'd
[4719.74 → 4721.64] probably be excited about the iPad, but I'm not.
[4721.78 → 4722.58] So I'm not.
[4722.58 → 4727.24] And so for me, anytime I hear iPad things, I just think like, I just wish they would
[4727.24 → 4733.78] make a super inexpensive internet device that my kids can use in the Apple ecosystem.
[4733.78 → 4738.52] It wasn't 500 plus dollars or more like that's just so much to shell it to a kid.
[4738.90 → 4742.54] But, and you do want to give them, you know, these fun things and stuff like that on trips,
[4742.60 → 4743.20] especially on trips.
[4743.22 → 4744.18] Like we're taking trips all the time.
[4744.20 → 4748.52] It's like, gosh, when we're driving, let's give them something to do so they can, you know,
[4748.52 → 4750.38] I'm not going to buy them a vision pro.
[4750.80 → 4752.42] So you stole my joke.
[4753.66 → 4754.52] Sorry about that, Mike.
[4754.68 → 4756.68] You set us up, and then you stole the joke.
[4757.28 → 4758.68] Well, that's how it goes.
[4758.82 → 4759.82] That's my least favourite thing though.
[4759.82 → 4761.26] Is anything iPad related?
[4761.42 → 4766.86] Just because it's to me, uh, iPad for me in particular is just a give me a smaller form
[4766.86 → 4772.14] factor, a kids focused device that is affordable for parents that have privacy features.
[4772.14 → 4773.42] That's something I'd be excited about.
[4773.90 → 4775.98] I like the iPad for what it is, but not for me.
[4776.38 → 4777.44] Closing loop on day one.
[4777.44 → 4779.00] I said, doesn't Microsoft own that?
[4779.08 → 4779.52] I was wrong.
[4779.64 → 4785.66] Once again, owned by our friends at automatic owners of things such as wordpress.com, Tumblr.
[4785.88 → 4786.56] That's right.
[4786.72 → 4791.82] Pocket casts, other cool Matt Mullenweg, just building like this fascinating software
[4791.82 → 4793.18] conglomerate.
[4793.24 → 4794.92] What do you call it when you have disparate products?
[4794.96 → 4795.32] I don't know.
[4795.54 → 4796.80] He just owns a lot of cool stuff.
[4797.04 → 4797.38] So, yeah.
[4797.84 → 4802.48] Well, Paul Maine should really get some credit there because Paul Maine drove that from day
[4802.48 → 4802.86] one.
[4803.24 → 4803.90] Thank you.
[4804.18 → 4805.06] Last puns.
[4805.06 → 4809.18] Uh, and then I think they partnered with automatic, which just made it a good acquisition, but
[4809.18 → 4814.10] they're still separate from what I understand owned by automatic got the resources, but still
[4814.10 → 4817.50] very much operating as bloom built LLC.
[4817.50 → 4818.96] If Google's correct.
[4818.96 → 4821.98] So Paul Maine is, uh, behind that.
[4822.18 → 4824.26] Been wanting to, you know, help people take notes.
[4824.36 → 4825.92] Great for forever.
[4826.18 → 4826.56] Basically.
[4826.94 → 4827.66] Great for forever.
[4828.04 → 4828.54] All right.
[4828.54 → 4829.90] Let's wrap it right here.
[4830.04 → 4831.98] These have been our WWDC hot takes.
[4832.14 → 4834.04] A lot of vision pro hot takes.
[4834.10 → 4836.94] We'll see how well they cool off over time.
[4837.66 → 4841.98] Uh, hopefully better than commander taco on the iPod.
[4841.98 → 4842.46] We'll see.
[4842.58 → 4843.28] Time will tell Mike.
[4843.34 → 4845.68] Thanks for hanging out with us and chatting.
[4845.78 → 4846.30] Always a joy.
[4846.40 → 4848.84] Where's the best place folks can connect with you on the internet?
[4848.94 → 4849.36] Thanks dudes.
[4849.58 → 4852.84] Uh, primarily probably Mastodon nowadays.
[4853.22 → 4855.54] I'm Mike McQuaid at Mastodon.social.
[4855.78 → 4856.12] There we go.
[4856.22 → 4860.26] But yeah, also my, everything's linked, and I've got some writing and stuff like that on
[4860.26 → 4862.06] my website at Mike McQuaid.com.
[4862.70 → 4867.66] You'll probably have to look at how to spell my lovely surname, but that's the best place
[4867.66 → 4868.04] to find me.
[4868.06 → 4869.72] We'll leave that as an exercise for the listener.
[4869.84 → 4873.94] Of course, the links are always in the show notes, so you can click through there as well.
[4874.06 → 4874.44] All right.
[4874.50 → 4875.26] Anything else, Adam?
[4876.54 → 4878.50] Let's try to spell McQuaid.
[4878.74 → 4880.04] I don't know how to spell McQuaid.
[4882.24 → 4883.32] How do you spell McQuaid, Mike?
[4883.36 → 4883.74] Real quick.
[4883.86 → 4885.28] M-C-Q-U-A-I-D.
[4886.02 → 4886.34] Okay.
[4886.52 → 4887.32] I thought I was right.
[4887.48 → 4887.68] Okay.
[4888.54 → 4889.24] MikeMcQuaid.com.
[4889.28 → 4889.68] Check it out.
[4890.24 → 4890.58] That's it.
[4890.58 → 4891.10] All right, you all.
[4891.20 → 4892.00] We'll catch you on the next one.
[4892.06 → 4898.38] There you have it.
[4898.44 → 4900.58] Our Apple Vision Pro hot takes.
[4900.96 → 4901.94] What do you think?
[4902.10 → 4903.78] Let us know in the comments.
[4904.02 → 4904.92] We'd love to hear from you.
[4905.22 → 4907.78] There's a link in your show notes for easy clicking.
[4908.20 → 4911.50] We have Matt Refer queued up for the next Change Login, friends.
[4912.02 → 4916.34] The topic is still to be determined, but we better come up with one soon, or he'll show
[4916.34 → 4918.38] up and want to just play his guitar for an hour.
[4918.38 → 4925.10] Special thanks again to our partners, FASC.com, fly.io, and typesense.org.
[4925.10 → 4929.32] And to Break master Cylinder for bumping out the best beats in the entire biz.
[4929.68 → 4933.74] If you dig the stuff we're putting out, share the Change Log with developers you know.
[4934.02 → 4938.62] Tell them we have the software world's best weekly news brief on Mondays, deep technical
[4938.62 → 4941.28] interviews on Wednesdays, and this talk show on Fridays.
[4941.80 → 4943.74] They'll thank you later, and I'll thank you right now.
[4943.74 → 4945.26] We appreciate you spreading the word.
[4945.52 → 4946.26] All right, that's it.
[4946.30 → 4948.92] This one's done, but let's talk again real soon.
[4953.86 → 4958.14] But this is for like those ultra high-end film studios potentially, or somebody who needs
[4958.14 → 4968.30] like extreme IO, or they need infinite amount of M2, um, MIME, Geez, I just got a frog
[4968.30 → 4968.68] in my throat.
[4969.46 → 4972.38] MIME, M2 drives, and that kind of thing.
[4972.38 → 4972.84] So.
[4973.76 → 4975.92] You should say that again, because it sounds like you're crying.
[4976.16 → 4977.70] Just clear your throat and say it again.
[4978.06 → 4979.42] Doesn't it sound like you got choked up?
[4979.74 → 4980.42] Yeah, gosh.
[4980.64 → 4981.92] I was crying about M2.
[4981.92 → 4981.94] I was crying about M2.
