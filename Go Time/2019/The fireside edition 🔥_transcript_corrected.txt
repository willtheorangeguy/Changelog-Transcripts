[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.40 → 17.84] This episode is brought to you by DigitalOcean.
[18.14 → 22.06] DigitalOcean is the simplest cloud platform for developers and teams
[22.06 → 27.14] with products like droplets, spaces, Kubernetes, load balancers, block storage,
[27.14 → 28.86] and pre-built one-click apps.
[28.86 → 32.76] You can deploy, manage, and scale cloud applications faster
[32.76 → 34.80] and more efficiently on DigitalOcean.
[35.14 → 37.74] Whether you're running one virtual machine or 10,000,
[38.06 → 41.20] DigitalOcean makes managing your infrastructure way too easy.
[41.56 → 43.98] Head to do.co slash Changelog.
[44.18 → 47.00] Again, do.co slash Changelog.
[47.00 → 58.88] Let's do it.
[59.52 → 60.50] It's Go Time.
[61.06 → 65.42] Welcome to Go Time, a podcast featuring a diverse panel and special guests
[65.42 → 70.62] discussing cloud infrastructure, distributed systems, microservices, Kubernetes, Docker.
[71.04 → 72.16] Oh, and also Go.
[72.16 → 75.94] We record live every Tuesday at 3 p.m. Eastern, noon Pacific.
[76.34 → 78.78] Join the community of Slack with us in real time during the show
[78.78 → 81.32] in the Go Time FM channel and go for Slack.
[81.54 → 82.20] Follow us on Twitter.
[82.32 → 83.58] We're at GoTimeFM.
[83.86 → 86.30] Listen live at changelog.com slash live
[86.30 → 89.10] or subscribe at changelog.com slash Go Time.
[89.22 → 90.54] And now on to the show.
[90.54 → 96.64] Hello there and welcome to Go Time.
[96.78 → 101.48] I'm Matt Ryder and welcome to a very special Fireside edition of Go Time
[101.48 → 104.38] where we essentially just get very close to the microphone.
[105.08 → 105.92] It's very intimate.
[106.60 → 110.12] We'll be chatting with each other and asking each other questions
[110.12 → 111.52] and also taking your questions.
[112.02 → 113.92] You can tweet at us.
[113.92 → 116.84] If you tweet at me at Matt Ryder, M-A-T-R-Y-E-R,
[117.44 → 119.20] I'll ask your question on the show
[119.20 → 122.24] or you can join in the conversation on Go for Slack
[122.24 → 125.18] in the Go Time FM channel.
[125.78 → 129.30] So I'll introduce my fellow hosts today.
[129.74 → 132.58] It's JB, JC and JD.
[133.30 → 137.36] It's Johnny Portico, John Calhoun and Yana B. Dugan.
[137.54 → 137.98] Hello.
[138.60 → 139.04] Hello.
[139.32 → 139.54] Hello.
[139.92 → 140.44] How are we doing?
[141.00 → 142.24] I think we're all doing good.
[142.42 → 143.36] I hope we're doing good.
[144.38 → 145.72] Well, I'm glad to hear it.
[146.34 → 148.08] Yeah, so I thought we could start off.
[148.08 → 150.76] This is something that I always wonder about other devs
[150.76 → 153.36] because, of course, we're a busy bunch often.
[153.46 → 154.50] If we're lucky, we're busy.
[155.18 → 159.68] And sometimes we either aren't really able to do side projects
[159.68 → 162.72] for whatever reason in our companies or in our day jobs,
[163.30 → 165.86] or maybe we just don't have the time or the energy or whatever
[165.86 → 167.08] after doing a full day.
[167.08 → 173.38] So given that, if you could just have two weeks to build anything,
[173.46 → 177.54] to do anything in Go, what would you do?
[178.10 → 180.90] Say you've just got two weeks, or if you need more time, you can have it.
[181.30 → 182.38] It's really relaxed.
[182.82 → 183.42] What would you do?
[183.46 → 186.04] Is there anything in mind that you'd build or work on,
[186.08 → 187.50] or is there anything you're interested in exploring?
[188.26 → 189.56] I guess I can kick this one-off.
[190.48 → 193.84] So building something isn't necessarily something I'd do.
[194.22 → 195.38] Well, I guess I'd build something.
[195.66 → 199.32] But what I'd more be focused on is I'd love to spend some more time
[199.32 → 202.36] looking at different aspects of how we design code
[202.36 → 204.68] and just spending more time on that.
[204.82 → 207.68] Specifically, I would love to actually build a project
[207.68 → 209.60] using global and all sorts of things,
[209.70 → 211.14] like basically just leaving global everywhere,
[211.28 → 213.68] like a global DB connection, a global set of templates,
[213.68 → 217.80] things like that, and just set it all up and actually write tests for it
[217.80 → 220.18] to sort of show what that looks like.
[220.78 → 223.56] Is that just to give Peter Organ an aneurysm?
[223.78 → 224.04] No.
[224.82 → 227.38] If I had the time, what I'd like to do is take that
[227.38 → 230.42] and then gradually refactor it to something that doesn't use the global
[230.42 → 235.70] and to actually see in each little refactor how that changes things
[235.70 → 239.04] and actually see what changes, how the tests change,
[239.58 → 243.28] how you can actually tell what's required a little bit better in some areas.
[243.28 → 245.88] And maybe even in some areas, I might find that, you know,
[246.00 → 248.26] global weren't actually as bad as we made them out to be.
[248.72 → 250.60] Because I know like in my own stuff, there's a couple of times
[250.60 → 253.72] where I'll do all this jumping through hoops to make global not necessary.
[254.50 → 256.00] And at the end of the day, I'm like,
[256.10 → 258.02] I don't know that I actually needed to do this.
[258.42 → 261.04] I think like the one example that always comes to my mind is
[261.04 → 265.18] whenever I'm building a web application where I'm generating HTML from the server,
[265.56 → 269.62] I will have like all this stuff that I do to make my HTML templates not global.
[269.62 → 273.24] And if I just had a global registry of like all my templates that were parsed,
[273.34 → 275.16] it probably wouldn't be that big of a deal.
[275.80 → 278.42] But, you know, I like try to avoid it for all these reasons.
[278.42 → 281.50] And then at the end of the day, I'm like, I'm not really sure if it's worth it.
[281.60 → 283.40] Because when I go to read the files,
[283.40 → 285.78] I often like to require them to be in a certain file structure
[285.78 → 288.26] on a local file system at a certain spot to work anyway.
[289.06 → 291.68] So, you know, and like that might be configurable,
[291.68 → 293.58] but there's still like limitations to it.
[293.64 → 294.72] And at the end of the day, it's like,
[294.72 → 299.36] is it really worth making it so they can completely customize the file structure
[299.36 → 302.76] of all these template files versus like just put them in the right structure?
[303.60 → 305.70] Yeah, that is an interesting point.
[306.10 → 309.28] We do talk, we tend to talk a lot in terms of absolutes.
[309.32 → 313.60] And we'll say like, don't use global variables as a general rule.
[314.24 → 316.60] Because if you're just getting started,
[316.60 → 322.28] or if you don't want to have to worry too much about some of the other aspects of code,
[322.28 → 325.54] then I can see why these rules help.
[325.62 → 328.92] They guide you and just prevent a kind of whole class of problems.
[329.48 → 332.52] But like with almost everything, and it's rare,
[332.64 → 335.22] and I don't know that there are even anywhere I would say,
[335.48 → 337.60] absolutely, this is the answer to something.
[337.90 → 339.72] I think there is a lot of gray area.
[339.84 → 343.76] And sometimes, yeah, a global variable is just so easy.
[343.94 → 345.62] And in the context of what you're doing,
[345.70 → 349.60] like this is just my little program that I'm going to run,
[349.64 → 351.28] or just me and one other or something.
[352.28 → 354.12] Versus, you know, this is a big open source package,
[354.12 → 355.48] and I think that would change things.
[355.64 → 358.14] But yeah, I can sometimes see that being the case.
[358.52 → 359.26] It's an interesting one.
[359.58 → 362.32] But do you, John, you do a lot of teaching, don't you?
[362.44 → 367.56] So is your interest in that because you then want to teach people?
[368.04 → 369.12] It would partially be that,
[369.20 → 372.50] but I think it's partially just like exploration for myself to see like,
[373.20 → 374.52] is it really worth doing it here?
[374.76 → 376.76] Because I mean, I think we get in these habits of like,
[377.10 → 378.96] I do it this way because I've been doing it this way.
[378.96 → 382.30] And sometimes it's like, are the trade-offs of what I'm doing actually worth it?
[383.18 → 384.62] You know, and spending some time exploring,
[384.72 → 387.30] that would be useful for like, you know, long term.
[387.84 → 389.70] But it's just hard to find that time of like,
[390.26 → 393.44] can I find, you know, a couple of hours to actually try these two different approaches
[393.44 → 395.46] and see which one's better whenever one's working.
[395.60 → 397.36] And like, you know, I've got a lot of other things to do.
[398.46 → 401.42] Yeah, I think the same thing applies to testing as well,
[401.42 → 406.90] because I've been through all different kind of cycles of TDD
[406.90 → 409.48] and all kinds of things where there's been times
[409.48 → 413.38] when I've been very adamant that everything is red-green tested.
[413.38 → 415.48] So I would have a unit test fail
[415.48 → 418.82] before I write any of the main program code
[418.82 → 421.48] and be very strict with myself about that.
[421.94 → 424.08] And I found that it had some benefits.
[424.24 → 429.12] But of course, the trade-off was that the tests were so tightly bound
[429.12 → 431.96] to exactly what my program code was.
[432.38 → 435.82] It was a little bit like having a test for a CSS file
[435.82 → 438.04] that just says like, this text colour has to be red.
[438.04 → 441.96] And then in another file, you say, make sure that that text colour is red.
[442.10 → 443.74] You're just saying the same thing twice.
[443.74 → 446.08] And that's not quite, that wasn't quite useful.
[446.28 → 448.94] So then I kind of go the other way and look at,
[449.20 → 451.90] let's do a just end-to-end testing.
[452.28 → 454.30] So don't worry about the internals.
[454.30 → 458.64] As long as the whole system works, I know it's working.
[459.06 → 461.82] That had, again, benefits and other problems.
[461.82 → 463.96] And one of the downsides to that was
[463.96 → 468.84] you didn't get any kind of laser focus on where things had broken.
[468.98 → 472.04] You just knew that the things weren't working as they should.
[472.04 → 475.92] You didn't have much help on where the problems were
[475.92 → 478.86] or what the impact was that you'd had that was unexpected.
[479.86 → 482.14] So yeah, and I think I'll do the same thing
[482.14 → 484.26] with what you're talking about, John.
[484.50 → 487.74] So that we try it with, have a little project
[487.74 → 489.76] and unit test it very tightly.
[490.28 → 493.10] Have the same project and just have integration tests
[493.10 → 495.52] and then play around somewhere in the middle
[495.52 → 499.36] because probably that's where the perfect solution is somewhere.
[499.36 → 502.42] I'm probably not a perfect solution, but a solution, maybe.
[503.26 → 504.86] So, okay, anyone else?
[504.96 → 508.74] What would you build if you could just could do anything?
[509.12 → 510.16] Let me ask you this first then.
[510.38 → 513.08] Can you work on side projects?
[514.08 → 515.82] Let me talk to my lawyer.
[518.36 → 520.48] Hang on, I have to text him real quick.
[520.48 → 524.22] Well, so, time, time.
[524.44 → 526.08] When you asked that question, I was just thinking,
[526.28 → 529.16] man, if I had like two weeks of uninterrupted time,
[529.32 → 530.46] what I would do with that?
[530.88 → 535.00] And really my mind immediately went to teaching
[535.00 → 538.04] because that's something I enjoy doing like a lot,
[538.24 → 541.62] but slightly different from sort of the live teaching.
[541.86 → 543.32] So recently I've been thinking about,
[543.44 → 546.88] okay, you enjoy teaching, and you enjoy doing it live.
[546.88 → 550.54] There's something about sort of seeing that light bulb go on
[550.54 → 552.06] in somebody's face, right?
[552.22 → 554.22] There's something about that I just find magical.
[554.70 → 556.66] I enjoy that tremendously.
[556.92 → 558.74] But at the same time, I do realize that,
[558.84 → 560.26] okay, I'm still one person.
[560.36 → 563.30] How do I scale myself, right, so to speak?
[563.74 → 568.04] How do I basically do that, have a sort of wider impact, right?
[568.12 → 569.66] At least the kind of impact I want to have.
[569.66 → 572.58] And I've been thinking, okay, maybe the way to do that
[572.58 → 575.70] is to dive into sort of recorded courses
[575.70 → 577.74] where maybe like a YouTube channel
[577.74 → 581.20] and try to live up to the likes of Frances
[581.20 → 583.22] and Just for Funk or something along those lines.
[583.82 → 586.84] You know, basically to try and sort of,
[587.78 → 590.72] I mean, I'm not going to use grandiose terms
[590.72 → 593.48] like change the world and any of that nonsense,
[593.48 → 599.18] but basically just to find a way to reach more people,
[599.40 → 601.78] I think is what I would like to do, right?
[601.84 → 604.16] So having recorded courses and, you know,
[604.20 → 606.22] making some for free, available for free
[606.22 → 608.26] and, you know, making some for paid as well
[608.26 → 610.24] because, you know, I do have a family
[610.24 → 612.14] to take care of that kind of thing.
[612.24 → 614.16] But really that's where my mind went,
[614.24 → 616.70] just basically trying to find a way to reach more people
[616.70 → 618.48] and hopefully serve more people.
[619.16 → 621.78] Yeah, the nice thing is when you teach somebody something, Johnny,
[621.78 → 626.42] you kind of enable them to then do things
[626.42 → 627.74] that they couldn't do before
[627.74 → 630.26] so that you get this sort of exponential effect.
[630.74 → 634.36] And I think that's easy to overlook, but so important.
[634.92 → 636.10] And so, yeah, I think that's great.
[636.18 → 637.92] And I've never been in one of your classes,
[638.04 → 639.86] but I have heard good things about them.
[640.08 → 641.06] So, yeah.
[641.14 → 643.68] Do you tend to do that at conferences then?
[644.80 → 645.44] Yeah, I do.
[645.58 → 646.64] I do them at conferences,
[646.64 → 648.06] usually a pre-conference workshop.
[648.06 → 652.44] And also I do the Go Bridge workshops.
[653.14 → 656.94] Oh, actually, this is a good time for me to mention that
[656.94 → 659.32] if you live in the Baltimore area,
[659.62 → 662.06] there is a Go Bridge workshop coming up
[662.06 → 664.36] on the 7th of December next month.
[664.52 → 668.18] So this will be my last Go Bridge workshop of the year.
[668.18 → 672.98] And basically, I just wanted to sort of give the opportunity
[672.98 → 674.96] for those that are looking to enter the year,
[675.10 → 677.08] you know, with a new skill,
[677.56 → 679.14] provide the opportunity, the learning opportunity
[679.14 → 680.50] for them to do so.
[680.68 → 682.76] So if you are listening to this
[682.76 → 686.40] and you know somebody in the Baltimore metro area,
[686.60 → 687.78] D.C., Virginia, that kind of thing,
[687.84 → 691.04] that could benefit from a full-day workshop to learn Go,
[691.62 → 693.64] this is a great opportunity to do so.
[694.50 → 696.78] And how do they find out more information about that?
[696.78 → 701.44] Well, they would go to gobridge.org
[701.44 → 705.86] and that will probably link them to the GitHub report.
[706.14 → 708.44] I forgot we changed that now.
[708.86 → 710.90] Actually, if you go on meetup.com
[710.90 → 713.56] and you look for the Baltimore Go meetup,
[713.86 → 716.10] that is one of the events listed.
[716.68 → 719.02] So you can just either Google for it
[719.02 → 721.28] or go to meetup.com slash Baltimore Go.
[721.84 → 723.58] I think Baltimore Go link for it
[723.58 → 724.36] to make it easier to find.
[724.36 → 726.94] And then basically you'll see the event.
[727.28 → 729.52] And if you are in a target demographic,
[730.40 → 731.54] I encourage you to sign up.
[732.42 → 732.82] Great.
[734.48 → 735.30] Awesome stuff.
[736.58 → 737.82] These are good answers so far.
[740.12 → 741.80] Another question I had was,
[742.10 → 743.86] what's the thing if you had to pick,
[743.96 → 745.02] which you do,
[745.74 → 747.10] is the thing that grinds your...
[747.10 → 749.00] I still have to answer, Matt.
[749.30 → 750.82] Yeah, don't forget about Yana.
[751.18 → 751.34] Oh, sorry.
[751.82 → 753.88] I just assumed that you...
[753.88 → 754.70] If you are out of time,
[754.82 → 755.62] it's actually okay.
[756.04 → 757.86] This question really hit me hard
[757.86 → 759.80] because I have exactly two weeks
[759.80 → 760.90] at the end of this year
[760.90 → 763.06] to do whatever I want to do.
[763.64 → 764.08] Ooh.
[764.96 → 766.14] And the question is,
[766.14 → 767.78] probably I will use Go, right?
[767.82 → 769.20] If I want to write code.
[769.20 → 770.82] And the question is,
[770.94 → 772.04] what am I going to do?
[772.90 → 774.00] This is more of like
[774.00 → 775.60] an existential crisis
[775.60 → 778.08] type of question from you, probably.
[778.60 → 780.42] There was like one crazy idea
[780.42 → 781.92] I had for a long time.
[782.06 → 783.50] I was wondering if it's possible
[783.50 → 785.04] to highlight
[785.04 → 787.70] some of the concurrency-related stuff
[787.70 → 788.84] in a text editor.
[789.06 → 790.06] Like, imagine
[790.06 → 792.14] if a library,
[792.42 → 794.20] if like you're making a call,
[794.26 → 795.66] it starts a Go routine, whatever.
[796.16 → 796.84] You just don't know
[796.84 → 798.28] from the API surface.
[798.96 → 799.66] But it, you know,
[799.72 → 800.76] just starts a Go routine,
[800.88 → 801.90] just runs some stuff
[801.90 → 802.84] in other Go routines
[802.84 → 803.36] and whatever.
[803.96 → 804.86] I wonder if you can
[804.86 → 806.42] like highlight
[806.42 → 807.40] in the editor
[807.40 → 808.14] that, oh,
[808.18 → 809.24] some of the pieces
[809.24 → 810.92] here in this block
[810.92 → 812.00] is just going to run
[812.00 → 812.90] in a different Go routine
[812.90 → 813.54] or may run
[813.54 → 814.46] in a different Go routine
[814.46 → 814.92] or whatever.
[815.28 → 815.96] So I was like thinking
[815.96 → 818.14] about this dynamic tool.
[818.68 → 820.08] You just run your program.
[820.20 → 821.38] It is just like, you know,
[822.08 → 823.46] maybe collect some profile
[823.46 → 824.02] or whatever.
[824.30 → 825.40] And then you apply
[825.40 → 826.10] that profile
[826.10 → 827.06] to your text editor
[827.06 → 828.30] and it gives you
[828.30 → 829.46] all this like different colours.
[829.68 → 830.52] Like this has been run
[830.52 → 831.40] in this like different
[831.40 → 832.74] Go routines and so on.
[832.92 → 834.16] So it like helps you to,
[834.26 → 836.14] it's not like a perfect solution,
[836.14 → 836.92] but it could be
[836.92 → 838.68] a good experimentation point
[838.68 → 840.48] and may kind of like influence
[840.48 → 841.80] maybe some other people
[841.80 → 843.98] to work on this type of problem.
[844.56 → 846.58] Because, you know,
[846.62 → 848.00] we had this discussion last week.
[848.62 → 850.10] There is no good way to say,
[850.42 → 851.50] hey, I'm just going to run
[851.50 → 851.98] some stuff
[851.98 → 853.06] in a different Go routine.
[853.94 → 854.62] Some libraries
[854.62 → 855.88] are doing a good job
[855.88 → 857.20] documenting this,
[857.42 → 858.76] but some others don't.
[859.40 → 860.86] So that's an interesting area
[860.86 → 862.20] to, you know, work on.
[862.92 → 863.08] Yeah.
[863.16 → 864.34] Would it look like
[864.34 → 865.98] the code coverage stuff
[865.98 → 866.96] where the background
[866.96 → 867.88] kind of changes colour?
[867.96 → 869.10] So you might see like
[869.10 → 870.18] red would be used
[870.18 → 871.04] for the main thread,
[871.18 → 872.04] but you kicked off
[872.04 → 872.90] a Go routine somewhere
[872.90 → 873.76] and you can see that code.
[873.76 → 873.84] Exactly.
[873.94 → 874.74] It's the same idea.
[874.92 → 875.12] Yeah.
[875.12 → 877.34] And you run the program.
[878.14 → 879.38] It only can capture,
[879.50 → 880.54] just like the test coverage,
[880.74 → 881.18] it can only,
[881.34 → 882.62] test coverage can only capture
[882.62 → 884.52] the tests you're running.
[884.90 → 885.18] You know,
[885.22 → 885.92] it just kind of like
[885.92 → 887.08] goes over those lines
[887.08 → 887.82] as it's running.
[888.08 → 889.42] So it's going to be the same.
[889.76 → 891.06] You run your program.
[891.56 → 892.94] It will only capture the cases
[892.94 → 894.82] that like you actually executed.
[895.34 → 896.76] But it might give you some hints,
[896.76 → 897.60] like maybe,
[898.00 → 898.82] I don't know,
[898.90 → 899.70] maybe over time,
[899.78 → 900.54] maybe it could be
[900.54 → 901.84] an incremental thing.
[902.70 → 903.86] Maybe it could be even
[903.86 → 905.18] like a global repository
[905.18 → 906.20] of something.
[906.64 → 907.38] This is just like
[907.38 → 908.52] a very rough idea.
[908.70 → 909.38] I just want to,
[909.52 → 909.68] you know,
[909.70 → 910.16] experiment.
[911.14 → 912.56] And it sounds cool.
[912.82 → 913.22] Thanks.
[913.62 → 913.90] Thanks.
[914.26 → 915.68] I don't know his last name.
[915.72 → 916.42] I will look it up.
[916.54 → 918.12] But there's a great talk
[918.12 → 920.02] by Ivan about
[920.02 → 921.40] visualizing concurrency.
[921.76 → 922.66] I don't know if you've seen it.
[922.76 → 923.12] Exactly.
[923.26 → 924.24] From the Gopher Con
[924.24 → 925.70] a couple of years ago, right?
[925.88 → 926.04] Yeah.
[926.10 → 926.46] So anyone,
[926.64 → 927.40] if you haven't seen that,
[927.52 → 928.00] check that out.
[928.12 → 929.00] It is amazing.
[929.28 → 930.72] And I chat to him
[930.72 → 931.40] every time I see him
[931.40 → 931.84] at conferences
[931.84 → 932.68] and he was kind of
[932.68 → 933.46] talking about
[933.46 → 934.78] maybe even like
[934.78 → 936.30] augmented reality
[936.30 → 937.52] or virtual reality
[937.52 → 939.54] ways of visualizing.
[939.54 → 940.00] You're just like
[940.00 → 940.98] basically running
[940.98 → 942.64] into your Go routines
[942.64 → 943.56] and all that stuff.
[944.26 → 944.52] Yeah.
[944.60 → 946.02] You'd be inside somehow
[946.02 → 947.44] and see the things
[947.44 → 948.20] around you.
[948.74 → 949.24] Let's see the
[949.48 → 949.64] you know,
[949.68 → 950.00] and maybe,
[950.12 → 951.14] maybe you'd be able
[951.14 → 952.42] to actually see hotspots.
[952.52 → 953.08] I don't know if,
[953.62 → 954.54] if we could somehow
[954.54 → 955.84] visualize the contention
[955.84 → 956.60] or something like that.
[956.68 → 957.64] Imagine being able to
[957.64 → 959.00] go and actually look
[959.00 → 959.98] and see heat spots
[959.98 → 961.36] of where there are things
[961.36 → 962.46] in contention
[962.46 → 962.86] or something.
[962.92 → 963.22] I don't know,
[963.26 → 963.42] but.
[963.92 → 964.12] Yeah.
[964.26 → 965.08] It was amazing
[965.08 → 966.46] just to see things
[966.46 → 966.98] in 3D,
[967.08 → 967.52] to be honest.
[967.58 → 968.12] Like I've seen
[968.12 → 969.28] like visualization tools
[969.28 → 970.16] only in 2D,
[970.44 → 971.76] but it made so much sense
[971.76 → 972.48] because you have like
[972.48 → 974.16] one level of more dimension
[974.16 → 975.38] when there's concurrency.
[975.86 → 976.30] And,
[976.44 → 976.56] you know,
[976.60 → 977.10] it was like,
[977.18 → 978.28] I think the right model.
[978.38 → 979.86] So I'm really excited
[979.86 → 981.94] about the virtual reality thing.
[982.70 → 983.14] Yeah.
[983.30 → 984.78] It finally makes us look
[984.78 → 985.48] like the hackers
[985.48 → 986.74] from the movies as well.
[986.82 → 987.04] Yeah.
[987.04 → 987.80] You know what I mean?
[987.84 → 988.08] Where,
[988.34 → 988.64] yeah,
[988.66 → 989.82] it's like a 3D cube
[989.82 → 991.16] and we'll complete the cube
[991.16 → 991.82] and that's when we know
[991.82 → 992.48] we're finished.
[992.88 → 993.24] Do you know what I mean?
[993.30 → 994.36] Like there's no scope
[994.36 → 995.74] creep in that world.
[996.48 → 996.88] Everything's,
[997.08 → 998.74] it's just when the cube's done,
[998.82 → 999.24] we're done
[999.24 → 1000.32] and we can go home.
[1000.74 → 1000.82] Well,
[1000.86 → 1002.06] that's all we want,
[1002.16 → 1002.44] isn't it?
[1002.80 → 1003.90] Is that what you would build
[1003.90 → 1004.74] through two weeks, Matt?
[1005.14 → 1006.10] Some way for us to code
[1006.10 → 1006.90] in a 3D world?
[1007.86 → 1008.20] Well,
[1008.40 → 1010.24] people have kind of
[1010.24 → 1010.94] played around with it
[1010.94 → 1011.36] a little bit.
[1011.42 → 1012.14] It is a kind of
[1012.14 → 1013.36] quite an exciting thing.
[1013.50 → 1014.72] Even just thinking of
[1014.72 → 1017.42] having a virtual reality headset
[1017.42 → 1018.64] and then having
[1018.64 → 1020.30] many monitors
[1020.30 → 1021.32] in front of you.
[1021.38 → 1021.50] I mean,
[1021.52 → 1022.52] it's the most boring
[1022.52 → 1023.34] possible use
[1023.34 → 1024.04] of that technology
[1024.04 → 1025.18] but it could be
[1025.18 → 1026.10] essentially like,
[1026.32 → 1027.44] and you could mix it
[1027.44 → 1028.76] with the
[1029.26 → 1029.50] you know,
[1029.54 → 1030.54] what's actually being
[1030.54 → 1031.54] seen as well
[1031.54 → 1032.54] so that it isn't just
[1032.54 → 1033.70] like screens only
[1033.70 → 1035.16] but you can have
[1035.16 → 1035.86] other backgrounds,
[1035.98 → 1036.30] I guess,
[1036.34 → 1036.62] and things.
[1036.94 → 1038.02] It's going to look nice
[1038.02 → 1038.44] basically.
[1038.72 → 1039.34] Put it that way.
[1040.14 → 1041.04] We're getting off-topic
[1041.04 → 1041.40] slightly,
[1041.52 → 1041.88] I guess,
[1041.98 → 1042.58] but that's okay.
[1042.58 → 1044.66] I saw one cool VR demo
[1044.66 → 1045.42] where somebody had it
[1045.42 → 1045.70] where like,
[1045.74 → 1046.50] you actually just saw
[1046.50 → 1048.06] a JavaScript editor
[1048.06 → 1048.94] you were coding in
[1048.94 → 1049.68] but like,
[1049.74 → 1050.22] when you made
[1050.22 → 1051.06] 3D models
[1051.06 → 1051.70] and things like that
[1051.70 → 1052.32] you'd actually just
[1052.32 → 1052.80] look to your right
[1052.80 → 1053.24] and you would see
[1053.24 → 1054.20] it actually rendering it.
[1054.40 → 1054.92] Oh, yeah.
[1054.94 → 1055.40] So it was like
[1055.40 → 1057.38] the coolest use case
[1057.38 → 1057.88] where it's like,
[1058.04 → 1058.12] yeah,
[1058.16 → 1059.04] you just get to see it
[1059.04 → 1059.72] in 3D
[1059.72 → 1060.20] and you can like
[1060.20 → 1060.66] walk around,
[1060.76 → 1060.90] you know,
[1060.90 → 1061.36] move around
[1061.36 → 1062.28] and sort of see the thing
[1062.28 → 1063.06] and like,
[1063.14 → 1063.90] I see stuff like that
[1063.90 → 1064.18] and I'm like,
[1064.24 → 1064.44] all right,
[1064.52 → 1065.54] VR could be awesome
[1065.54 → 1066.68] if we get there.
[1066.80 → 1067.86] It's just going to
[1067.86 → 1068.82] take some time sadly.
[1070.10 → 1070.44] Yeah,
[1071.02 → 1071.44] probably,
[1071.44 → 1072.40] but they're working
[1072.40 → 1072.64] on it,
[1072.70 → 1072.96] aren't they?
[1073.84 → 1074.32] Let's hope.
[1076.58 → 1077.06] All right,
[1077.14 → 1077.60] now Matt,
[1077.64 → 1078.28] I suppose you can
[1078.28 → 1079.00] go to your question.
[1079.44 → 1079.64] Yeah,
[1079.66 → 1079.78] well,
[1079.78 → 1080.40] I was going to ask
[1080.40 → 1081.34] about if there's
[1081.34 → 1082.06] anything in Go
[1082.06 → 1084.12] that would grind
[1084.12 → 1085.04] one's gears
[1085.04 → 1085.88] as it were.
[1086.24 → 1087.02] That's what the kids
[1087.02 → 1087.96] say these days,
[1087.96 → 1088.32] I think.
[1088.48 → 1089.32] I actually had to
[1089.32 → 1089.88] look it up.
[1089.96 → 1090.80] I actually had to
[1090.80 → 1091.28] look it up
[1091.28 → 1092.16] just to make sure
[1092.16 → 1093.68] that it means
[1093.68 → 1095.14] what I assume
[1095.14 → 1095.92] it means.
[1096.44 → 1096.62] Oh,
[1096.70 → 1096.90] no.
[1097.68 → 1098.12] Sure,
[1098.30 → 1098.50] yeah.
[1099.12 → 1100.12] I need to really
[1100.12 → 1101.94] think more about
[1101.94 → 1102.76] before I speak.
[1103.12 → 1103.64] I think
[1103.64 → 1104.80] it's hard
[1104.80 → 1105.26] as a native
[1105.26 → 1105.96] English speaker,
[1106.20 → 1107.26] like all the
[1107.26 → 1108.04] random phrases
[1108.04 → 1108.84] and stuff like that
[1108.84 → 1110.42] that don't
[1110.42 → 1111.66] necessarily make sense
[1111.66 → 1112.30] out of,
[1112.50 → 1112.98] like if you weren't
[1112.98 → 1113.50] used to them.
[1113.84 → 1114.68] This is kind of
[1114.68 → 1115.74] like obvious,
[1116.04 → 1116.40] I mean,
[1116.40 → 1117.34] it's not that obvious,
[1117.54 → 1117.72] I mean,
[1117.74 → 1118.34] it's obvious,
[1118.54 → 1119.32] you can guess,
[1119.44 → 1119.72] right?
[1120.44 → 1120.96] I don't know,
[1121.00 → 1121.32] actually.
[1121.64 → 1122.42] That's a good
[1122.42 → 1122.80] question.
[1122.98 → 1123.86] I'm ignored by
[1123.86 → 1125.22] anyone that speaks
[1125.22 → 1126.86] multiple languages,
[1127.40 → 1128.58] so I can't really
[1128.58 → 1129.34] imagine what that's
[1129.34 → 1129.62] like,
[1129.68 → 1130.26] so I don't know
[1130.26 → 1131.28] is the honest answer.
[1131.74 → 1132.62] I like hearing
[1132.62 → 1133.98] phrases in other
[1133.98 → 1135.58] languages translated
[1135.58 → 1137.12] and you don't have
[1137.12 → 1137.94] any of the context
[1137.94 → 1138.34] or anything.
[1138.62 → 1139.68] They are brilliant.
[1139.98 → 1140.68] Some of them
[1140.68 → 1141.78] are absolutely
[1141.78 → 1142.14] brilliant.
[1142.56 → 1143.20] I should give you
[1143.20 → 1143.60] a listen,
[1143.82 → 1145.82] like I can score
[1145.82 → 1146.24] you.
[1147.18 → 1147.42] Yeah.
[1148.00 → 1148.16] Oh,
[1148.24 → 1149.68] we should do
[1149.68 → 1150.20] that on Twitter.
[1150.38 → 1151.18] That's hilarious.
[1151.56 → 1152.56] We should definitely
[1152.56 → 1153.12] start that.
[1153.66 → 1153.86] So,
[1154.06 → 1154.78] speaking of
[1154.78 → 1155.58] grinding gears,
[1155.90 → 1156.56] what's the thing
[1156.56 → 1157.38] that annoys you
[1157.38 → 1158.74] the most about
[1158.74 → 1159.00] Go?
[1159.42 → 1159.94] That was another
[1159.94 → 1160.58] question I thought
[1160.58 → 1161.00] might be an
[1161.00 → 1161.56] interesting one
[1161.56 → 1162.16] to chat about.
[1162.32 → 1163.68] I have a couple
[1163.68 → 1164.18] of things.
[1164.28 → 1164.42] I mean,
[1164.44 → 1165.12] I actually have
[1165.12 → 1166.12] one specific
[1166.12 → 1166.38] thing,
[1166.54 → 1167.04] shadowing.
[1167.44 → 1167.62] You know,
[1167.66 → 1168.22] there's like all
[1168.22 → 1168.92] this convenience
[1168.92 → 1170.60] stuff for error
[1170.60 → 1171.92] types and then
[1171.92 → 1172.70] it just sometimes
[1172.70 → 1173.06] works,
[1173.16 → 1173.88] sometimes doesn't
[1173.88 → 1175.14] work or it
[1175.14 → 1176.00] doesn't quite
[1176.00 → 1177.48] work what I
[1177.48 → 1178.14] want it to
[1178.14 → 1178.92] work like,
[1178.92 → 1179.54] so it's just
[1179.54 → 1180.50] very inconsistent.
[1181.16 → 1181.52] How would you
[1181.52 → 1182.34] change it then?
[1182.52 → 1183.04] Would you just
[1183.04 → 1183.76] disallow it?
[1183.90 → 1184.56] So if you try to
[1184.56 → 1184.90] use it,
[1184.96 → 1185.24] it says,
[1185.56 → 1185.84] you know,
[1185.90 → 1186.42] this variable's
[1186.42 → 1187.04] already been used
[1187.04 → 1187.74] in another block
[1187.74 → 1188.40] or do you allow
[1188.40 → 1188.74] it?
[1189.34 → 1189.98] What would you
[1189.98 → 1190.20] do?
[1190.34 → 1190.72] How would you
[1190.72 → 1191.14] change it?
[1191.38 → 1191.98] So currently,
[1192.30 → 1193.08] they only allow
[1193.08 → 1193.86] shadowing of
[1193.86 → 1194.44] errors,
[1194.88 → 1195.30] right?
[1196.08 → 1196.88] So if they
[1196.88 → 1197.84] take it further
[1197.84 → 1199.36] to allow people
[1199.36 → 1199.62] to,
[1199.76 → 1199.86] you know,
[1199.92 → 1200.48] for convenience
[1200.48 → 1200.94] to shadow
[1200.94 → 1202.10] the other
[1202.10 → 1203.10] variables,
[1203.10 → 1203.70] I think it would
[1203.70 → 1204.26] be way too
[1204.26 → 1204.70] much.
[1204.70 → 1206.04] So I would
[1206.04 → 1206.56] say that,
[1206.68 → 1206.86] like,
[1206.90 → 1207.38] I think it's
[1207.38 → 1208.66] fair as it
[1208.66 → 1209.02] is,
[1209.12 → 1209.44] but it's
[1209.44 → 1211.28] annoying because
[1211.28 → 1211.84] it gives me
[1211.84 → 1212.00] this,
[1212.06 → 1212.14] like,
[1212.20 → 1213.16] inconsistency.
[1213.36 → 1214.20] I can see,
[1214.32 → 1214.52] like,
[1214.54 → 1214.96] there's no
[1214.96 → 1215.60] other way to
[1215.60 → 1216.14] do this.
[1216.32 → 1216.72] They can
[1216.72 → 1217.76] completely disable
[1217.76 → 1218.70] it and that
[1218.70 → 1219.40] would be such
[1219.40 → 1220.08] an inconvenient
[1220.08 → 1220.86] thing because,
[1221.04 → 1221.16] you know,
[1221.20 → 1221.52] you have,
[1221.64 → 1221.70] like,
[1221.74 → 1222.28] errors all
[1222.28 → 1222.70] around,
[1222.84 → 1223.06] so you
[1223.06 → 1223.38] want to be
[1223.38 → 1224.16] sometimes on a
[1224.16 → 1225.34] shadow of it
[1225.34 → 1225.60] for the
[1225.60 → 1226.04] convenience,
[1226.64 → 1227.14] but it's just,
[1227.28 → 1227.36] like,
[1227.42 → 1228.24] annoying and
[1228.24 → 1229.04] sometimes I need
[1229.04 → 1229.64] to declare the
[1229.64 → 1230.42] variable and
[1230.42 → 1231.08] sometimes I
[1231.08 → 1231.36] don't.
[1231.42 → 1231.76] It's just,
[1231.90 → 1232.00] like,
[1232.02 → 1232.52] I don't know,
[1232.52 → 1232.70] like,
[1232.76 → 1233.28] I really
[1233.28 → 1234.02] don't like
[1234.02 → 1235.20] how inconsistent
[1235.20 → 1236.14] it sometimes
[1236.14 → 1236.94] looks and
[1236.94 → 1237.72] people are just
[1237.72 → 1238.46] copy-pasting the
[1238.46 → 1239.42] style sometimes
[1239.42 → 1239.78] like,
[1239.92 → 1240.74] and they're just
[1240.74 → 1241.58] assuming that
[1241.58 → 1242.24] that's the only
[1242.24 → 1242.96] way to do or
[1242.96 → 1243.32] whatever,
[1243.54 → 1243.70] so,
[1243.82 → 1244.00] like,
[1244.30 → 1244.66] you know,
[1245.18 → 1246.02] not my taste
[1246.02 → 1246.38] maybe.
[1246.94 → 1247.40] Yeah,
[1247.54 → 1248.34] that thing
[1248.34 → 1249.00] sometimes when
[1249.00 → 1249.42] you have to
[1249.42 → 1250.50] switch the
[1250.50 → 1251.38] colon equals
[1251.38 → 1251.78] with the
[1251.78 → 1252.26] equals,
[1252.52 → 1253.26] things like
[1253.26 → 1253.90] those little
[1253.90 → 1254.28] things and
[1254.28 → 1255.48] also not being
[1255.48 → 1256.10] able to declare
[1256.10 → 1256.64] a variable
[1256.64 → 1257.74] without using
[1257.74 → 1259.24] it has great
[1259.24 → 1259.62] kind of
[1259.62 → 1260.08] foundations,
[1260.24 → 1260.48] but when,
[1260.60 → 1261.42] as you're in
[1261.42 → 1262.46] in the weeds
[1262.46 → 1263.04] of something
[1263.04 → 1263.84] sometimes,
[1264.10 → 1264.34] you know,
[1264.38 → 1264.70] it would be
[1264.70 → 1265.14] nice to be
[1265.14 → 1265.70] able to just
[1265.70 → 1266.70] declare a
[1266.70 → 1266.96] variable and
[1266.96 → 1267.22] just don't
[1267.22 → 1267.58] use it,
[1267.84 → 1268.48] take it out,
[1268.72 → 1269.52] if the compiler
[1269.52 → 1270.64] knows you've
[1270.64 → 1271.20] not used this
[1271.20 → 1271.48] variable,
[1271.74 → 1272.24] just take it
[1272.24 → 1272.48] out,
[1272.88 → 1273.28] just know what
[1273.28 → 1273.44] I mean,
[1273.52 → 1273.86] I know,
[1274.10 → 1274.48] like,
[1274.70 → 1275.18] put a warning
[1275.18 → 1275.48] on or
[1275.48 → 1275.74] something,
[1275.88 → 1276.46] but pop it
[1276.46 → 1276.68] out,
[1276.84 → 1277.16] don't worry
[1277.16 → 1277.62] about it,
[1277.94 → 1278.18] that would
[1278.18 → 1278.44] be my
[1278.44 → 1278.76] advice.
[1279.14 → 1279.52] I suspect
[1279.52 → 1280.04] some of that
[1280.04 → 1280.74] stems from
[1280.74 → 1281.48] knowing what
[1281.48 → 1281.96] imports you
[1281.96 → 1282.38] have and all
[1282.38 → 1282.80] that stuff,
[1282.92 → 1283.00] like,
[1283.08 → 1283.76] it leads to
[1283.76 → 1284.22] a lot more
[1284.22 → 1284.66] things.
[1285.36 → 1285.54] Yes,
[1285.64 → 1286.16] yes.
[1286.34 → 1286.76] It's also,
[1286.92 → 1287.00] like,
[1287.04 → 1287.50] the shadowing
[1287.50 → 1287.98] stuff can be
[1287.98 → 1288.18] annoying,
[1288.24 → 1288.50] like you
[1288.50 → 1288.74] said,
[1288.82 → 1289.68] if some
[1289.68 → 1290.36] code changes
[1290.36 → 1290.80] and now all
[1290.80 → 1291.06] of a sudden
[1291.06 → 1291.76] the colon equals
[1291.76 → 1292.34] doesn't work,
[1292.84 → 1293.26] it can be
[1293.26 → 1293.72] annoying when,
[1293.80 → 1293.96] like,
[1293.98 → 1294.46] you have to
[1294.46 → 1294.96] change a line
[1294.96 → 1295.26] that has
[1295.26 → 1295.94] nothing to do
[1295.94 → 1296.48] with the PR,
[1296.72 → 1296.90] like,
[1297.02 → 1297.46] or what you're
[1297.46 → 1297.78] changing,
[1298.40 → 1298.88] so it's just
[1298.88 → 1299.08] like,
[1299.12 → 1299.44] why did you
[1299.44 → 1299.82] change this
[1299.82 → 1300.00] line?
[1300.08 → 1300.24] It's like,
[1300.28 → 1300.70] the code will
[1300.70 → 1301.08] not work
[1301.08 → 1301.44] without me
[1301.44 → 1301.96] changing that
[1301.96 → 1302.18] line.
[1302.74 → 1303.08] Yes,
[1303.16 → 1303.92] I agree with
[1303.92 → 1304.50] you completely.
[1304.92 → 1305.40] That's why I
[1305.40 → 1306.30] like the extra
[1306.30 → 1307.02] comma at the
[1307.02 → 1307.66] end of lists,
[1307.66 → 1308.44] because you can
[1308.44 → 1310.14] just change
[1310.14 → 1310.54] lines,
[1310.66 → 1311.20] you don't have
[1311.20 → 1312.08] to go and
[1312.08 → 1312.86] reformat another
[1312.86 → 1313.62] line in an
[1313.62 → 1314.50] unrelated way.
[1315.32 → 1315.60] Yeah,
[1315.70 → 1316.36] completely agree
[1316.36 → 1316.68] with that.
[1317.22 → 1317.50] My,
[1317.78 → 1318.52] I wouldn't say
[1318.52 → 1319.60] grinds my gear
[1319.60 → 1321.52] as much as...
[1321.52 → 1322.06] Not cool enough.
[1322.46 → 1322.94] Yeah,
[1323.38 → 1324.54] perhaps that's
[1324.54 → 1325.00] not cool enough.
[1326.22 → 1327.66] It's kind of
[1327.66 → 1328.16] closely related
[1328.16 → 1328.44] to that,
[1328.66 → 1329.42] to what Yang
[1329.42 → 1330.42] was saying,
[1330.52 → 1331.90] is that I
[1331.90 → 1333.14] see it often,
[1333.92 → 1334.34] especially,
[1334.54 → 1334.88] I think the
[1334.88 → 1335.46] typical example
[1335.46 → 1335.86] that's given
[1335.86 → 1337.02] is if you're
[1337.02 → 1337.68] in a for loop,
[1337.80 → 1338.94] you have an
[1338.94 → 1339.24] iterator,
[1339.32 → 1339.62] you have an
[1339.62 → 1340.38] I variable or
[1340.38 → 1340.60] something,
[1340.78 → 1341.82] and then you're
[1341.82 → 1342.22] launching a
[1342.22 → 1342.54] grow machine
[1342.54 → 1342.74] and it's
[1342.74 → 1343.16] out of there.
[1343.62 → 1344.90] Because of the
[1344.90 → 1346.06] closure that
[1346.06 → 1346.64] happens over
[1346.64 → 1347.10] the variable,
[1347.26 → 1347.62] you think you
[1347.62 → 1347.96] can actually
[1347.96 → 1348.84] use the
[1348.84 → 1349.72] iterator inside
[1349.72 → 1350.78] of your
[1350.78 → 1351.32] grow routine,
[1351.54 → 1351.86] inside your
[1351.86 → 1352.22] function,
[1352.94 → 1353.44] and then not
[1353.44 → 1354.14] realizing that
[1354.14 → 1354.76] basically you're
[1354.76 → 1355.68] not really using
[1355.68 → 1356.42] a copy of
[1356.42 → 1357.40] that variable,
[1357.54 → 1358.08] basically using
[1358.08 → 1358.54] the same
[1358.54 → 1359.30] reference to
[1359.30 → 1359.42] it.
[1359.52 → 1360.02] So your
[1360.02 → 1360.46] grow routines
[1360.46 → 1360.80] end up
[1360.80 → 1361.88] stepping all
[1361.88 → 1362.16] over each
[1362.16 → 1362.36] other.
[1362.58 → 1363.36] So I've
[1363.36 → 1364.14] seen code
[1364.14 → 1364.80] like that
[1364.80 → 1365.98] pop up
[1365.98 → 1366.84] enough times
[1366.84 → 1367.96] that I
[1367.96 → 1368.70] don't quite
[1368.70 → 1369.34] have a
[1369.34 → 1371.14] solution for
[1371.14 → 1371.32] it,
[1371.38 → 1371.70] but it's
[1371.70 → 1372.06] just something
[1372.06 → 1373.10] that happens
[1373.10 → 1374.02] often enough.
[1374.12 → 1374.62] I'm not
[1374.62 → 1375.54] sure a way
[1375.54 → 1375.88] around that
[1375.88 → 1376.20] other than
[1376.20 → 1377.36] teaching people
[1377.36 → 1378.10] to, hey,
[1378.18 → 1378.66] this is actually
[1378.66 → 1379.20] what happens
[1379.20 → 1380.52] because of the
[1380.52 → 1380.78] closure.
[1381.00 → 1381.40] If you don't
[1381.40 → 1381.86] pass in a
[1381.86 → 1382.50] copy of
[1382.50 → 1383.16] this variable,
[1383.44 → 1385.44] you're going
[1385.44 → 1385.58] to get
[1385.58 → 1385.90] unexpected
[1385.90 → 1386.46] results.
[1387.02 → 1387.66] We could
[1387.66 → 1388.42] probably detect
[1388.42 → 1388.74] that.
[1389.34 → 1390.38] Is there a
[1390.38 → 1390.86] linter or
[1390.86 → 1391.44] something that
[1391.44 → 1392.48] warns or
[1392.48 → 1393.04] some warning
[1393.04 → 1393.72] tool that
[1393.72 → 1394.80] checks that?
[1395.20 → 1395.72] I feel like
[1395.72 → 1395.98] that would
[1395.98 → 1397.34] be able to
[1397.34 → 1398.54] detect that
[1398.54 → 1399.22] statically.
[1399.22 → 1401.06] I don't
[1401.06 → 1401.26] know.
[1401.40 → 1401.68] I don't
[1401.68 → 1401.88] know if
[1401.88 → 1402.08] there are
[1402.08 → 1402.36] or not.
[1402.48 → 1402.82] It wouldn't
[1402.82 → 1403.32] shock me if
[1403.32 → 1404.06] it's possible
[1404.06 → 1404.54] to detect,
[1404.70 → 1405.66] but one of
[1405.66 → 1406.00] the issues
[1406.00 → 1406.42] you run into
[1406.42 → 1406.82] there is
[1406.82 → 1407.88] that a
[1407.88 → 1408.44] beginner who
[1408.44 → 1408.80] is most
[1408.80 → 1409.28] likely to
[1409.28 → 1409.64] run into
[1409.64 → 1410.12] the issue
[1410.12 → 1410.82] is the
[1410.82 → 1411.30] least likely
[1411.30 → 1411.74] person to
[1411.74 → 1412.02] have that
[1412.02 → 1412.52] linter set
[1412.52 → 1412.76] up.
[1413.00 → 1414.24] So it's
[1414.24 → 1414.84] like you're
[1414.84 → 1415.26] solving a
[1415.26 → 1415.70] problem that
[1415.70 → 1416.24] by the time
[1416.24 → 1416.54] they know
[1416.54 → 1416.98] to use that
[1416.98 → 1417.72] tool, they
[1417.72 → 1418.22] don't necessarily
[1418.22 → 1418.62] have the
[1418.62 → 1419.02] problem.
[1419.86 → 1419.96] Right.
[1420.14 → 1420.60] So we need
[1420.60 → 1420.98] to time
[1420.98 → 1422.10] travel packages.
[1422.92 → 1423.48] Packages that
[1423.48 → 1424.00] time travel
[1424.00 → 1424.28] are enabled.
[1424.30 → 1424.54] It would
[1424.54 → 1424.96] almost have to
[1424.96 → 1425.74] be built into
[1425.74 → 1426.44] stuff, which I
[1426.44 → 1426.68] don't know.
[1429.22 → 1429.66] Right.
[1430.62 → 1431.20] So instead of
[1431.20 → 1431.76] doing time
[1431.76 → 1432.28] travel as a
[1432.28 → 1432.82] package, you
[1432.82 → 1433.12] think it
[1433.12 → 1433.38] should be
[1433.38 → 1433.84] built in.
[1433.98 → 1434.70] That's the
[1434.70 → 1436.06] challenge with
[1436.06 → 1436.76] doing time
[1436.76 → 1437.58] travel code.
[1437.66 → 1437.84] I'm just
[1437.84 → 1437.98] going to
[1437.98 → 1438.38] ignore you
[1438.38 → 1438.60] Matt.
[1439.02 → 1439.58] Yeah, fair
[1439.58 → 1439.76] enough.
[1441.04 → 1441.86] Fair enough.
[1442.56 → 1443.32] So I know
[1443.32 → 1443.88] like for me,
[1443.94 → 1444.22] one of the
[1444.22 → 1444.56] things that
[1444.56 → 1445.04] kind of gets
[1445.04 → 1445.68] me at times,
[1445.84 → 1446.22] and this is
[1446.22 → 1446.86] like a very
[1446.86 → 1447.58] minor grief,
[1447.84 → 1449.46] but like I
[1449.46 → 1450.22] like avoid
[1450.22 → 1450.88] using inline
[1450.88 → 1451.44] structs or
[1451.44 → 1452.10] when you just
[1452.10 → 1452.54] define a
[1452.54 → 1453.52] struct inside
[1453.52 → 1454.08] of something,
[1454.50 → 1454.82] there are a
[1454.82 → 1455.22] lot of times
[1455.22 → 1455.50] where I'll
[1455.50 → 1456.04] avoid doing
[1456.04 → 1456.58] that simply
[1456.58 → 1458.02] because like
[1458.02 → 1458.86] recreating that
[1458.86 → 1459.68] type then later
[1459.68 → 1460.44] becomes slightly
[1460.44 → 1461.00] more annoying.
[1461.38 → 1461.82] Like you can't
[1461.82 → 1463.26] just construct the
[1463.26 → 1463.76] whole thing without
[1463.76 → 1464.40] being like, oh,
[1464.44 → 1464.88] and I have a
[1464.88 → 1465.46] struct here and
[1465.46 → 1465.84] here are all the
[1465.84 → 1466.42] fields and then I
[1466.42 → 1466.84] have to, you
[1466.84 → 1467.42] know, it just
[1467.42 → 1467.94] seems like so
[1467.94 → 1468.64] much extra work
[1468.64 → 1469.08] at times.
[1469.52 → 1470.24] So like it would
[1470.24 → 1470.80] be nice if there
[1470.80 → 1471.44] was an easier way
[1471.44 → 1472.18] to do that because
[1472.18 → 1473.20] I do think reading
[1473.20 → 1474.16] inline structs is
[1474.16 → 1475.50] very useful at
[1475.50 → 1475.70] times.
[1475.80 → 1476.24] Like there's all
[1476.24 → 1476.74] sorts of cases
[1476.74 → 1477.36] where I'm like, I
[1477.36 → 1477.96] don't actually need
[1477.96 → 1478.52] another type.
[1478.64 → 1479.16] I could just
[1479.16 → 1480.06] throw this in
[1480.06 → 1480.22] there.
[1480.28 → 1480.68] It's just sort of
[1480.68 → 1481.42] nested data in
[1481.42 → 1481.80] this type.
[1482.30 → 1482.72] So that's the
[1482.72 → 1483.36] type of thing that
[1483.36 → 1484.42] it would be nice to
[1484.42 → 1485.38] simplify some of
[1485.38 → 1485.60] that.
[1485.96 → 1487.12] And it must be
[1487.12 → 1488.00] able to do that
[1488.00 → 1489.62] because they're
[1489.62 → 1490.78] statically typed.
[1490.92 → 1491.66] So it knows the
[1491.66 → 1492.86] type, doesn't it,
[1493.18 → 1494.18] the compile time?
[1494.48 → 1494.96] Yeah, like you
[1494.96 → 1496.68] can do like var
[1496.68 → 1498.00] t thing and then
[1498.00 → 1498.48] like you can do
[1498.48 → 1499.76] t dot, you know,
[1499.82 → 1500.96] dot a dot b dot c
[1500.96 → 1501.94] equals something and
[1501.94 → 1502.50] like it gives them
[1502.50 → 1503.24] all zero value.
[1503.38 → 1504.24] So like it definitely
[1504.24 → 1505.12] knows that it's there.
[1505.24 → 1505.82] It's just a matter
[1505.82 → 1507.04] of like when you're
[1507.04 → 1508.28] declaring it or
[1508.28 → 1508.86] setting it up,
[1509.04 → 1509.78] it's you have to do
[1509.78 → 1510.16] it a slightly
[1510.16 → 1510.82] different way,
[1511.32 → 1512.42] which I just don't
[1512.42 → 1512.98] like that it leads
[1512.98 → 1513.56] to code that it's
[1513.56 → 1514.16] like, why did you do
[1514.16 → 1514.98] it this way this time?
[1515.02 → 1515.36] It's like, well,
[1515.38 → 1516.28] because I'm using
[1516.28 → 1517.08] these nested things,
[1517.08 → 1518.02] it looks a little
[1518.02 → 1518.60] bit weird if I
[1518.60 → 1519.08] can do it that
[1519.08 → 1519.34] way.
[1520.30 → 1520.84] Yeah, again, the
[1520.84 → 1521.24] same thing.
[1521.32 → 1522.28] It's nice for the
[1522.28 → 1522.60] code.
[1522.96 → 1523.72] If you're doing
[1523.72 → 1524.54] something, it's nice
[1524.54 → 1525.12] for there to be a
[1525.12 → 1525.98] reason for it, not
[1525.98 → 1528.14] just being happy.
[1529.94 → 1530.62] Happy is good.
[1531.04 → 1531.16] Yeah.
[1540.84 → 1542.00] This episode is
[1542.00 → 1542.68] brought to you by
[1542.68 → 1544.62] Strong DM, manage and
[1544.62 → 1545.68] secure remote access
[1545.68 → 1546.72] to any database,
[1546.94 → 1547.90] any server, on
[1547.90 → 1548.52] prem or in the
[1548.52 → 1549.44] cloud and
[1549.44 → 1550.30] environments.
[1550.68 → 1551.46] They make it easy
[1551.46 → 1552.54] for DevOps teams to
[1552.54 → 1553.54] enforce the security
[1553.54 → 1554.28] and controls
[1554.28 → 1555.32] Infosec teams
[1555.32 → 1555.78] require.
[1556.24 → 1556.58] So if your
[1556.58 → 1557.08] engineers need
[1557.08 → 1558.28] access, you need
[1558.28 → 1558.92] Strong DM.
[1559.26 → 1559.68] So what can
[1559.68 → 1560.58] Strong DM do for
[1560.58 → 1561.06] your team?
[1561.32 → 1561.96] First off, more
[1561.96 → 1562.64] control, less
[1562.64 → 1563.12] hassle.
[1563.60 → 1564.60] Grant or revoke
[1564.60 → 1565.52] access to any
[1565.52 → 1566.58] database or server
[1566.58 → 1567.42] in one command.
[1567.82 → 1569.02] Use your SSO to
[1569.02 → 1569.90] manage access to
[1569.90 → 1570.72] every database,
[1570.94 → 1571.70] every server and
[1571.70 → 1572.16] environment.
[1572.16 → 1573.42] Second, total
[1573.42 → 1574.02] visibility.
[1574.48 → 1575.40] Strong DM upgrades
[1575.40 → 1576.24] your audit logs,
[1576.34 → 1576.82] log every
[1576.82 → 1577.86] permission change,
[1578.06 → 1578.74] every query,
[1579.12 → 1580.38] every SSH and
[1580.38 → 1581.54] every RDP command
[1581.54 → 1582.16] and know who
[1582.16 → 1583.10] issued those changes.
[1583.62 → 1584.20] And of course,
[1584.40 → 1585.12] faster SOC 2
[1585.12 → 1586.18] compliance, easily
[1586.18 → 1587.14] enforce access
[1587.14 → 1588.22] controls and
[1588.22 → 1589.34] instantly answer
[1589.34 → 1590.26] auditors' questions.
[1590.76 → 1590.94] Head to
[1590.94 → 1592.16] StrongDM.com slash
[1592.16 → 1593.12] Go Time to learn
[1593.12 → 1594.26] more and request a
[1594.26 → 1594.80] free demo.
[1595.16 → 1595.50] Again,
[1595.62 → 1597.10] StrongDM.com slash
[1597.10 → 1597.64] Go Time.
[1609.26 → 1610.52] So next question.
[1610.96 → 1611.30] Yes.
[1611.56 → 1612.28] Unless you have
[1612.28 → 1612.90] something, Matt, you
[1612.90 → 1613.58] wanted to talk about
[1613.58 → 1614.12] that grinds your
[1614.12 → 1614.36] gears.
[1616.48 → 1616.92] No.
[1617.28 → 1617.64] Okay.
[1618.12 → 1618.42] Nothing.
[1618.52 → 1619.06] I don't use that
[1619.06 → 1619.66] phrase, actually.
[1619.66 → 1623.94] So since I'm
[1623.94 → 1624.44] working in a
[1624.44 → 1625.08] bright pink room
[1625.08 → 1625.76] right now, or
[1625.76 → 1626.58] recording for one,
[1626.76 → 1627.34] and if you haven't
[1627.34 → 1628.30] seen the tweet, you
[1628.30 → 1628.96] can go check that
[1628.96 → 1629.18] out.
[1629.68 → 1630.26] Basically, the
[1630.26 → 1630.92] question is, what
[1630.92 → 1631.48] is your ideal
[1631.48 → 1632.28] working environment?
[1632.44 → 1633.14] And that can be
[1633.14 → 1634.22] room, you know,
[1634.36 → 1635.76] like, you know,
[1635.78 → 1636.48] basically anything
[1636.48 → 1637.14] like open work
[1637.14 → 1637.84] environment, you
[1637.84 → 1638.50] know, open space
[1638.50 → 1639.92] versus an office,
[1640.66 → 1641.58] headphones, you
[1641.58 → 1642.10] know what type of
[1642.10 → 1642.92] music, anything like
[1642.92 → 1643.14] that.
[1643.22 → 1643.68] I'm just kind of
[1643.68 → 1644.44] curious, like, what
[1644.44 → 1645.28] do you guys prefer?
[1645.40 → 1645.82] What makes you
[1645.82 → 1646.16] productive?
[1646.76 → 1647.44] Definitely not
[1647.44 → 1648.26] open spaces.
[1648.26 → 1649.26] Yeah.
[1653.90 → 1654.78] That was the first
[1654.78 → 1655.58] thing I thought, too.
[1655.92 → 1657.06] Definitely not open
[1657.06 → 1657.84] plan offices.
[1658.26 → 1658.88] I have a feeling
[1658.88 → 1659.54] that they're just,
[1659.76 → 1660.74] like, way cheaper
[1660.74 → 1661.30] or something.
[1661.44 → 1662.00] Like, there's just a
[1662.00 → 1663.12] really obvious reason
[1663.12 → 1664.80] why they exist.
[1664.80 → 1666.12] I think it depends on
[1666.12 → 1666.74] sometimes.
[1666.74 → 1667.88] Like, sometimes in
[1667.88 → 1668.54] the beginning of a
[1668.54 → 1669.36] project, you just,
[1669.44 → 1670.68] like, want to design,
[1670.80 → 1672.10] you want to just,
[1672.20 → 1673.70] you know, discuss,
[1673.76 → 1674.78] like, for hours or
[1674.78 → 1675.92] hours and whatever.
[1676.74 → 1678.08] I mean, it's nice if
[1678.08 → 1678.92] you can just go to a
[1678.92 → 1679.66] meeting room, whatever,
[1679.80 → 1680.46] but, like, sometimes
[1680.46 → 1681.54] you want to be in the
[1681.54 → 1682.98] same environment and
[1682.98 → 1684.28] still keep, you know,
[1684.32 → 1685.30] debating or whatever.
[1685.84 → 1686.46] But, you know, open
[1686.46 → 1687.56] space is also not really
[1687.56 → 1688.50] good for this type of
[1688.50 → 1689.30] stuff because you don't
[1689.30 → 1690.02] want to disturb the
[1690.02 → 1691.02] people around you.
[1691.02 → 1692.42] But maybe I've seen
[1692.42 → 1693.26] this other model,
[1693.88 → 1694.68] this, like, old school
[1694.68 → 1695.90] offices for four or
[1695.90 → 1696.52] five people.
[1696.64 → 1697.48] You just put the team
[1697.48 → 1699.36] in, you know, your,
[1699.50 → 1701.02] like, immediate peers
[1701.02 → 1702.60] and you are working
[1702.60 → 1703.74] from the same office.
[1703.92 → 1704.84] It has doors and
[1704.84 → 1705.56] everything, so you can
[1705.56 → 1706.28] actually, you know,
[1706.28 → 1707.06] close the door.
[1707.24 → 1707.94] You can have as many
[1707.94 → 1709.10] meetings as possible
[1709.10 → 1711.34] if that's what you're
[1711.34 → 1712.04] going for.
[1712.52 → 1713.84] So I really personally
[1713.84 → 1715.36] like my sofa a lot.
[1715.86 → 1717.04] And recently I realized
[1717.04 → 1717.98] that I'm, like, way
[1717.98 → 1719.36] more productive when I'm
[1719.36 → 1720.16] working from home.
[1721.02 → 1722.14] Because, you know, I
[1722.14 → 1722.56] don't have any
[1722.56 → 1723.88] interruptions or anything.
[1724.76 → 1725.02] Yeah.
[1725.50 → 1726.76] I still think the open
[1726.76 → 1727.72] office space was, like,
[1727.72 → 1728.58] a recruiting tactic.
[1728.76 → 1728.96] Why?
[1729.44 → 1730.84] Because, like, as a
[1730.84 → 1731.96] new college grad, if you
[1731.96 → 1732.88] walk into an office space
[1732.88 → 1733.36] with a bunch of
[1733.36 → 1734.62] cubicles and then you
[1734.62 → 1735.28] walk into, like, an
[1735.28 → 1736.54] open space, like,
[1736.62 → 1737.40] Facebook office or
[1737.40 → 1739.36] something, the one just
[1739.36 → 1740.36] seems like a much,
[1740.78 → 1741.80] like, more, like, it
[1741.80 → 1742.38] seems like a better
[1742.38 → 1743.28] environment from where
[1743.28 → 1743.98] you're coming from.
[1744.46 → 1744.76] Like, you don't
[1744.76 → 1745.00] necessarily...
[1745.00 → 1745.60] Because you're a fool.
[1745.84 → 1746.32] Yeah, because, like,
[1746.34 → 1746.98] you don't know any
[1746.98 → 1747.70] better at that point.
[1747.90 → 1748.94] And, like, a lot of
[1748.94 → 1749.64] the companies I've seen
[1749.64 → 1751.00] push them higher a
[1751.00 → 1752.10] lot of new grads.
[1752.42 → 1753.48] So, like, it's almost
[1753.48 → 1754.04] like they're, like,
[1754.10 → 1755.04] optimizing for that in
[1755.04 → 1755.52] some ways.
[1755.68 → 1756.24] I don't know if that's
[1756.24 → 1757.10] actually true, but it
[1757.10 → 1757.92] seems that way.
[1758.44 → 1759.14] Because I've worked in
[1759.14 → 1760.82] the cubicle spaces and
[1760.82 → 1762.44] I get when you walk in
[1762.44 → 1763.00] the office, you're like,
[1763.04 → 1763.76] this looks kind of,
[1763.82 → 1764.80] like, corporate and
[1764.80 → 1765.76] boring and, like, not
[1765.76 → 1766.08] cool.
[1766.44 → 1767.20] But at the same time,
[1767.20 → 1768.04] it's nice to be able to
[1768.04 → 1768.74] sit down and be like,
[1768.92 → 1769.82] this is my space.
[1769.90 → 1770.78] Like, nobody's bugging
[1770.78 → 1770.94] me.
[1770.98 → 1771.86] I don't hear as much.
[1771.86 → 1774.02] So, I'm going to speak
[1774.02 → 1774.98] from experience here.
[1775.12 → 1776.06] Because once upon a
[1776.06 → 1778.00] time, I was in an
[1778.00 → 1779.04] environment that
[1779.04 → 1781.42] specifically designed the
[1781.42 → 1782.78] office space to be an
[1782.78 → 1784.60] open floor plan with
[1784.60 → 1786.86] glass walls, if you
[1786.86 → 1787.36] call that.
[1788.02 → 1788.94] Even the conference room
[1788.94 → 1789.92] was kind of like a
[1789.92 → 1790.78] fishbowl, right?
[1790.80 → 1791.44] It was glass.
[1791.60 → 1792.34] And if you walked into
[1792.34 → 1793.44] the office as you walk
[1793.44 → 1794.62] by, even if you were
[1794.62 → 1795.72] having meetings in that
[1795.72 → 1797.32] office, in that conference
[1797.32 → 1798.16] room, you know, it was
[1798.16 → 1798.78] all glass.
[1799.32 → 1800.28] It looked beautiful.
[1800.60 → 1801.68] I mean, I'm not going
[1801.68 → 1801.96] to lie.
[1802.16 → 1802.96] Could you, like, write on
[1802.96 → 1803.10] it?
[1803.32 → 1804.32] Yes, yes, you could.
[1804.42 → 1805.04] Yeah, yeah, absolutely.
[1805.22 → 1805.86] It was meant for that.
[1805.98 → 1806.98] It was beautiful.
[1807.36 → 1808.80] And it was basically, it
[1808.80 → 1809.88] was an agency, a digital
[1809.88 → 1810.68] agency, right?
[1810.70 → 1811.80] So, there was a lot of
[1811.80 → 1813.04] sort of creative folks
[1813.04 → 1814.24] seated all over the
[1814.24 → 1814.58] place.
[1814.76 → 1816.12] And when you walked in
[1816.12 → 1817.74] there, the effect, when
[1817.74 → 1818.44] you walked in there, you
[1818.44 → 1819.58] could see people working
[1819.58 → 1821.40] on illustrations, design
[1821.40 → 1822.36] work, doing really
[1822.36 → 1823.10] beautiful stuff.
[1823.50 → 1823.98] And I think that was
[1823.98 → 1825.34] part of the reason for
[1825.34 → 1825.74] that, right?
[1825.86 → 1826.98] If you bring a prospect
[1826.98 → 1828.66] into the office, you
[1828.66 → 1829.40] bring a customer into
[1829.40 → 1831.00] the office, the impact,
[1831.08 → 1832.22] right, that that brings,
[1832.34 → 1833.38] like, immediately you get
[1833.38 → 1833.90] hit with that.
[1833.94 → 1834.96] You're like, okay, this
[1834.96 → 1836.22] place is serious, right?
[1836.82 → 1837.86] The coders didn't sit
[1837.86 → 1838.24] up front.
[1838.38 → 1839.96] The designers did, because
[1839.96 → 1840.78] they were doing the cool
[1840.78 → 1841.30] stuff, right?
[1841.34 → 1842.08] The coders, I mean, we
[1842.08 → 1842.92] just look at techs all
[1842.92 → 1843.02] day.
[1843.06 → 1843.62] There's nothing, you
[1843.62 → 1844.40] know, appealing about
[1844.40 → 1845.02] that, even when you
[1845.02 → 1845.60] first walk into the
[1845.60 → 1845.82] office.
[1845.98 → 1847.48] But, you know, that was
[1847.48 → 1849.30] part of the appeal of it,
[1849.34 → 1849.48] right?
[1849.50 → 1850.70] It was, like, modern
[1850.70 → 1851.20] looking.
[1851.66 → 1852.82] It had less of a like,
[1852.90 → 1854.30] nice open and airy feel
[1854.30 → 1854.72] to it.
[1855.04 → 1856.46] I mean, in your own, if
[1856.46 → 1857.22] you think about it, in
[1857.22 → 1858.08] your own home, I mean,
[1858.08 → 1858.76] in my home right now, I'd
[1858.76 → 1859.60] like to knock down a few
[1859.60 → 1860.46] walls, you know, make it
[1860.46 → 1861.86] open, make it airy, you
[1861.86 → 1862.56] know, make it, you know,
[1862.96 → 1863.82] feng shui or whatever,
[1863.98 → 1864.60] you know, like, you know,
[1864.60 → 1865.18] you want that.
[1865.30 → 1866.92] But, you know, it didn't
[1866.92 → 1868.34] take long before we
[1868.34 → 1869.34] quickly realized, okay,
[1869.54 → 1871.44] this is a sort of focus
[1871.44 → 1871.82] killer.
[1872.34 → 1872.84] If you're trying to get,
[1872.94 → 1874.62] it's fine to look at, but
[1874.62 → 1875.12] if you're trying to get
[1875.12 → 1876.20] work done with all the
[1876.20 → 1877.08] buzzing, the activity,
[1877.26 → 1877.82] everything going on
[1877.82 → 1878.86] around you, you just can't
[1878.86 → 1879.52] get anything done, which
[1879.52 → 1880.50] is why, you know, it
[1880.50 → 1880.92] didn't take long.
[1881.04 → 1882.00] I got a month in, everybody
[1882.00 → 1882.80] got, you know, noise
[1882.80 → 1884.20] cancelling headphones, because
[1884.20 → 1885.06] we just couldn't get
[1885.06 → 1885.52] anything done.
[1888.08 → 1890.62] Is it as disruptive as,
[1891.00 → 1892.12] you know, noise?
[1892.88 → 1894.56] It's an echoed, like,
[1894.62 → 1895.30] noise, you know, somebody
[1895.30 → 1896.70] could be having, like,
[1896.96 → 1897.60] basically, you could have
[1897.60 → 1898.42] two people sitting on the
[1898.42 → 1899.92] other side of the office
[1899.92 → 1901.14] and you could still hear
[1901.14 → 1902.20] them, like, if you're on
[1902.20 → 1903.14] the other end, because
[1903.14 → 1904.18] there's nothing in between.
[1904.56 → 1905.32] Yeah, it sounds like the
[1905.32 → 1906.50] entire office was a stage
[1906.50 → 1907.96] or something, stage for
[1907.96 → 1908.72] the customers.
[1909.40 → 1910.88] You're just running a show.
[1912.70 → 1914.00] It was, it was literally,
[1914.06 → 1914.90] it was like a performance.
[1915.00 → 1916.02] We were performing work.
[1916.22 → 1917.64] It was, it was incredible.
[1918.08 → 1919.28] I'm a big believer in
[1919.28 → 1920.58] letting the engineering
[1920.58 → 1922.74] team decide how it works
[1922.74 → 1923.92] and I wonder how many
[1923.92 → 1925.88] would choose that kind
[1925.88 → 1926.36] of setup.
[1926.82 → 1927.86] Well, let's not go to
[1927.86 → 1928.52] the extreme now.
[1928.66 → 1930.68] I mean, it's, it's, I
[1930.68 → 1931.70] mean, I don't, don't get
[1931.70 → 1932.00] me wrong.
[1932.10 → 1933.08] I like the look of the
[1933.08 → 1933.38] office.
[1933.48 → 1934.40] I like the feel of the
[1934.40 → 1934.72] office.
[1934.84 → 1937.08] It did feel like, you
[1937.08 → 1938.08] know, welcoming in some
[1938.08 → 1939.96] ways, because I sort of,
[1940.00 → 1940.64] you know, had a punch
[1940.64 → 1942.32] on towards the, the nice
[1942.32 → 1943.52] eclectic and sort of
[1943.52 → 1944.36] modern look.
[1944.62 → 1945.56] You know, I think these
[1945.56 → 1946.30] days I've kind of swung
[1946.30 → 1947.30] back around to the more
[1947.30 → 1949.14] cozy and warm kind of
[1949.14 → 1950.78] feel, but it did have an
[1950.78 → 1951.76] appeal to it that you
[1951.76 → 1952.54] walk into the office,
[1952.62 → 1953.66] you're like, okay, these,
[1953.86 → 1954.70] these folks are serious.
[1954.70 → 1955.02] Right.
[1955.08 → 1956.38] So, but you know, it was
[1956.38 → 1957.02] just that there was a
[1957.02 → 1957.98] downside to it that we
[1957.98 → 1959.12] just didn't know because
[1959.12 → 1960.32] at the time, this was
[1960.32 → 1961.14] like, you know, well over,
[1961.26 → 1962.12] you know, like a decade
[1962.12 → 1963.72] and a half ago at the
[1963.72 → 1965.66] time, open floor plan was
[1965.66 → 1966.36] the thing, right?
[1966.56 → 1967.78] Everybody wanted to have
[1967.78 → 1968.62] an open floor plan.
[1968.74 → 1969.52] It was like, you know,
[1969.58 → 1970.42] articles were being
[1970.42 → 1971.98] written, you know, it's
[1971.98 → 1973.30] kind of funny because the
[1973.30 → 1974.48] same, I don't know if
[1974.48 → 1975.24] it's the same people, but
[1975.24 → 1975.98] you know, you see
[1975.98 → 1977.76] articles about how open
[1977.76 → 1978.92] floor plan is the new
[1978.92 → 1979.66] is, right?
[1980.06 → 1981.22] And then now you're
[1981.22 → 1981.98] seeing a bunch of
[1981.98 → 1982.90] articles saying, no,
[1983.12 → 1984.34] that it's not is.
[1984.40 → 1985.66] It's just, you know,
[1985.72 → 1987.70] crap, you know, don't
[1987.70 → 1988.02] do it.
[1988.30 → 1989.22] I mean, it's like the
[1989.22 → 1991.02] pendulum has swung,
[1991.14 → 1991.42] right?
[1991.50 → 1992.54] You know, you go back
[1992.54 → 1993.50] and forth, which is why
[1993.50 → 1994.72] that's really just a
[1994.72 → 1995.36] warning that, hey,
[1995.74 → 1996.54] whatever is hot and
[1996.54 → 1998.36] cool today, just, you
[1998.36 → 1999.12] know, give it a few,
[1999.34 → 2000.24] give it a moment, settle
[2000.24 → 2001.30] down a little bit, learn
[2001.30 → 2002.42] to see what's what and
[2002.42 → 2003.52] then make a decision
[2003.52 → 2004.02] on your own.
[2004.10 → 2004.80] Just don't get carried
[2004.80 → 2005.10] away.
[2005.20 → 2005.38] Yeah.
[2005.88 → 2006.94] That's great advice.
[2007.96 → 2009.46] I like working remotely
[2009.46 → 2011.46] and have done that now
[2011.46 → 2012.66] for the last five years.
[2012.76 → 2014.52] So, and sometimes I
[2014.52 → 2016.48] miss like the office and
[2016.48 → 2017.58] occasionally I have to go
[2017.58 → 2019.26] out into town or, you
[2019.26 → 2019.92] know, I go because I
[2019.92 → 2020.82] want to, if any of my
[2020.82 → 2021.42] friends are listening,
[2021.78 → 2022.44] which they're not.
[2023.96 → 2025.04] But I, um, you don't
[2025.04 → 2025.52] have, you don't have
[2025.52 → 2025.80] friends.
[2025.90 → 2026.72] No, no, I do have
[2026.72 → 2027.46] friends, but they don't
[2027.46 → 2028.28] listen to go Tom.
[2028.28 → 2031.62] Oh, JS party, JS party,
[2031.70 → 2031.94] mate.
[2032.94 → 2033.86] That competitor.
[2034.52 → 2034.80] Yeah.
[2034.86 → 2036.30] So, uh, and I miss it.
[2036.34 → 2037.98] I miss the kind of, uh,
[2037.98 → 2039.50] atmosphere, uh, that you
[2039.50 → 2040.82] can get when you are
[2040.82 → 2042.38] co-located, but for
[2042.38 → 2045.08] practical productivity, I
[2045.08 → 2047.16] can't beat screen
[2047.16 → 2047.66] sharing.
[2047.66 → 2049.46] Um, you know, working
[2049.46 → 2051.48] with people have the
[2051.48 → 2052.04] audio on.
[2052.12 → 2053.00] So you're sharing, you're
[2053.00 → 2053.50] just chatting.
[2053.62 → 2054.38] One of you sharing the
[2054.38 → 2054.66] screen.
[2054.90 → 2055.92] I do pair programming a
[2055.92 → 2056.16] lot.
[2056.48 → 2058.06] And so it's nice because
[2058.06 → 2059.28] you're not physically next
[2059.28 → 2061.00] to the person, but you're
[2061.00 → 2061.98] having the same kind of
[2061.98 → 2062.76] experience.
[2063.30 → 2064.52] How do you pair program
[2064.52 → 2065.44] without a physical
[2065.44 → 2065.80] contact?
[2065.88 → 2066.88] I've never been in a
[2066.88 → 2068.06] situation where there is
[2068.06 → 2069.20] like pair programming going
[2069.20 → 2069.46] on.
[2069.50 → 2070.66] Like how does it work
[2070.66 → 2071.00] nowadays?
[2072.08 → 2072.48] Yeah.
[2072.54 → 2074.14] Well, you just share the
[2074.14 → 2074.46] screen.
[2074.56 → 2075.26] That's how we do it.
[2075.26 → 2076.02] I do it with David.
[2076.02 → 2077.28] We just share the screen
[2077.28 → 2078.68] and one of us is
[2078.68 → 2079.50] driving and the other
[2079.50 → 2080.10] one's watching the
[2080.10 → 2081.14] screen and we sort of
[2081.14 → 2082.78] build things together
[2082.78 → 2084.16] and we get the immediate
[2084.16 → 2085.30] knowledge share that
[2085.30 → 2086.52] happens automatically
[2086.52 → 2087.26] because we're both
[2087.26 → 2087.90] doing this.
[2088.02 → 2089.80] We also get the two
[2089.80 → 2091.94] minds at the same time
[2091.94 → 2093.06] and often we think about
[2093.06 → 2093.92] things in slightly
[2093.92 → 2095.48] different ways or we
[2095.48 → 2095.84] have different
[2095.84 → 2096.98] perspectives, or we care
[2096.98 → 2097.90] about different things.
[2098.16 → 2099.40] So what we end up with
[2099.40 → 2101.52] is usually a pretty good
[2101.52 → 2102.72] first version of things
[2102.72 → 2103.50] because it's kind of,
[2103.56 → 2104.26] it's almost like the
[2104.26 → 2105.24] second version already
[2105.24 → 2106.62] because it's had two of
[2106.62 → 2107.20] us build it.
[2107.28 → 2108.56] We also share a lot
[2108.56 → 2110.06] philosophically like we
[2110.06 → 2111.26] will happily just throw
[2111.26 → 2112.10] things away.
[2112.54 → 2113.50] We're not precious about
[2113.50 → 2114.88] even if we spend a lot
[2114.88 → 2115.76] of time building it,
[2116.06 → 2117.22] we know that there's a
[2117.22 → 2118.16] lot of value that isn't
[2118.16 → 2119.00] just in the code.
[2119.18 → 2120.26] So throwing the code
[2120.26 → 2122.28] away and restarting
[2122.28 → 2123.10] things like that,
[2123.42 → 2125.02] which are very privileged
[2125.02 → 2126.64] practices to be able
[2126.64 → 2127.02] to do.
[2127.14 → 2127.98] I know a lot of dev
[2127.98 → 2130.42] teams that sound like
[2130.42 → 2131.92] a kind of crazy luxury
[2131.92 → 2132.88] that they just don't
[2132.88 → 2133.20] have.
[2133.58 → 2134.40] To some dev teams,
[2134.50 → 2135.32] testing sounds like a
[2135.32 → 2135.56] luxury.
[2135.56 → 2136.30] I mean,
[2136.34 → 2136.90] I think they're
[2136.90 → 2138.82] necessary and that's
[2138.82 → 2139.52] what you have to do if
[2139.52 → 2140.60] you can is fight for
[2140.60 → 2141.26] those things.
[2142.14 → 2143.30] So it's nice because
[2143.30 → 2145.16] there was actually a
[2145.16 → 2145.52] tech,
[2145.60 → 2146.22] piece of tech,
[2146.30 → 2146.90] it was an app called
[2146.90 → 2147.82] Screen Hero that
[2147.82 → 2148.72] Skype bought.
[2149.56 → 2150.02] And Skype,
[2150.16 → 2151.04] it may have it,
[2151.24 → 2152.42] I'm not sure if they've
[2152.42 → 2153.58] got it integrated or not,
[2153.66 → 2155.20] but that was great
[2155.20 → 2156.00] because it was basically
[2156.00 → 2157.64] screen share with audio
[2157.64 → 2158.84] and it gave you two
[2158.84 → 2159.90] mouse pointers.
[2160.34 → 2161.82] One was basically fake,
[2162.40 → 2163.16] but it gave you the
[2163.16 → 2163.94] impression that the
[2163.94 → 2165.00] other person was sat
[2165.00 → 2165.62] there with you and
[2165.62 → 2166.22] they had their own
[2166.22 → 2167.44] pointer on your screen.
[2168.02 → 2168.82] So as you're talking,
[2169.04 → 2170.04] you can see them
[2170.04 → 2171.20] circling something when
[2171.20 → 2172.02] they're drawing your
[2172.02 → 2172.68] attention to it,
[2172.78 → 2174.38] pointing about some
[2174.38 → 2175.04] code and say,
[2175.46 → 2176.30] it's this or what
[2176.30 → 2176.92] about this?
[2177.24 → 2178.28] And they can even
[2178.28 → 2179.36] type too,
[2179.44 → 2180.04] so you could both
[2180.04 → 2180.56] type.
[2181.20 → 2181.78] So someone,
[2182.04 → 2182.60] if they know,
[2182.76 → 2183.12] oh no,
[2183.20 → 2183.80] this is how we should
[2183.80 → 2184.06] do it,
[2184.10 → 2184.26] look,
[2184.30 → 2185.12] they can just jump in
[2185.12 → 2185.68] at any point.
[2186.30 → 2187.30] Stuff like that was
[2187.30 → 2188.78] just so useful for us
[2188.78 → 2191.12] and we just got so
[2191.12 → 2191.76] good at that.
[2191.82 → 2192.66] We got so used to
[2192.66 → 2193.50] that way of working.
[2193.96 → 2195.58] If we meet up now in
[2195.58 → 2196.44] real life,
[2196.44 → 2198.20] we tend not to be very
[2198.20 → 2198.58] productive.
[2198.84 → 2200.08] We try and do other
[2200.08 → 2201.10] things other than
[2201.10 → 2201.86] coding.
[2202.00 → 2202.74] We don't meet up to
[2202.74 → 2203.48] code or anything like
[2203.48 → 2204.50] that just because it's
[2204.50 → 2204.74] so,
[2205.28 → 2206.62] works so well for us.
[2207.06 → 2208.06] Do you think that it's
[2208.06 → 2209.18] also a thing between
[2209.18 → 2210.14] you two?
[2210.34 → 2210.66] Like,
[2210.66 → 2211.46] I find it very
[2211.46 → 2212.38] intimidating to
[2212.38 → 2213.88] pair program myself,
[2214.60 → 2215.52] especially with people
[2215.52 → 2217.56] like who I've never
[2217.56 → 2219.02] worked with before.
[2219.84 → 2220.68] So maybe it's just
[2220.68 → 2221.62] kind of also like,
[2221.84 → 2223.04] you know,
[2223.06 → 2223.60] just like the
[2223.60 → 2224.40] environment and you
[2224.40 → 2225.92] feel productive because
[2225.92 → 2227.02] of the peer,
[2227.30 → 2227.86] specific peer.
[2228.08 → 2228.30] Anyway,
[2228.30 → 2229.18] it's slightly a different
[2229.18 → 2229.90] topic probably.
[2231.20 → 2231.68] No,
[2231.72 → 2232.40] but it's an interesting
[2232.40 → 2233.30] point because you're
[2233.30 → 2233.56] right.
[2233.76 → 2234.38] You do have to,
[2234.44 → 2235.44] it doesn't work with
[2235.44 → 2235.64] everybody.
[2235.76 → 2236.36] It's not the same
[2236.36 → 2236.94] experience.
[2236.94 → 2237.38] In fact,
[2237.48 → 2238.62] every pair programming
[2238.62 → 2240.22] session is unique.
[2240.46 → 2240.70] And if,
[2240.86 → 2242.08] and because there's two
[2242.08 → 2242.36] people,
[2242.44 → 2242.60] you know,
[2242.64 → 2243.20] if it's a different
[2243.20 → 2243.60] person,
[2243.66 → 2244.00] of course,
[2244.04 → 2244.50] it's going to be a
[2244.50 → 2245.08] different dynamic.
[2245.08 → 2245.76] And yeah,
[2245.80 → 2247.16] we've just found a
[2247.16 → 2248.74] way where it's okay
[2248.74 → 2249.72] for us to be wrong.
[2249.84 → 2251.02] We aren't embarrassed
[2251.02 → 2252.08] if one of us is wrong.
[2252.28 → 2253.12] If you can get that
[2253.12 → 2253.66] in your team,
[2254.02 → 2255.22] I think you're really
[2255.22 → 2255.98] ahead of the curve
[2255.98 → 2257.88] because you have to be
[2257.88 → 2258.74] able to be wrong
[2258.74 → 2259.26] about things.
[2259.28 → 2259.88] Otherwise we're going
[2259.88 → 2260.94] to be too careful
[2260.94 → 2262.12] with ideas, and we're
[2262.12 → 2263.48] going to have to do
[2263.48 → 2264.68] too much research
[2264.68 → 2265.14] before.
[2265.64 → 2266.52] And there might be
[2266.52 → 2267.42] people in the team
[2267.42 → 2268.64] that have a similar
[2268.64 → 2269.14] idea,
[2269.36 → 2270.14] have maybe tried
[2270.14 → 2270.86] things before.
[2271.20 → 2271.68] You know,
[2271.70 → 2272.26] you get a lot of
[2272.26 → 2273.12] benefits from having
[2273.12 → 2273.94] that space where you
[2273.94 → 2275.06] can just be wrong.
[2275.06 → 2275.82] And it's okay.
[2276.40 → 2277.34] Things like that
[2277.34 → 2278.32] definitely help.
[2278.32 → 2289.86] This episode is brought
[2289.86 → 2290.82] to you by Good
[2290.82 → 2292.34] with native integrations
[2292.34 → 2292.88] for Kubernetes
[2292.88 → 2294.22] and a helm chart
[2294.22 → 2295.28] to quickly get started.
[2295.74 → 2297.36] Good is an easy choice
[2297.36 → 2298.42] for cloud native teams.
[2298.42 → 2299.86] With Good running
[2299.86 → 2300.44] on Kubernetes,
[2300.60 → 2301.40] you define your build
[2301.40 → 2302.56] workflow and let
[2302.56 → 2303.68] Good provision
[2303.68 → 2304.78] and scale build
[2304.78 → 2305.66] infrastructure on the
[2305.66 → 2306.40] fly for you.
[2306.40 → 2308.36] Good installs as a
[2308.36 → 2309.32] Kubernetes native
[2309.32 → 2309.94] application,
[2310.40 → 2310.94] which allows for
[2310.94 → 2311.96] ease of operations,
[2312.36 → 2313.32] easily upgrade and
[2313.32 → 2314.46] maintain Good using
[2314.46 → 2314.88] helm,
[2315.22 → 2315.94] scale your build
[2315.94 → 2317.06] infrastructure elastically
[2317.06 → 2318.04] with a new
[2318.04 → 2319.28] elastic agent that
[2319.28 → 2319.86] uses Kubernetes
[2319.86 → 2320.68] conventions to
[2320.68 → 2321.40] dynamically scale
[2321.40 → 2322.24] Good agents.
[2322.74 → 2323.82] Good also has
[2323.82 → 2325.12] first class integration
[2325.12 → 2325.64] with Docker
[2325.64 → 2326.20] registries,
[2326.68 → 2327.52] easily compose,
[2328.02 → 2328.44] track,
[2328.66 → 2329.22] and visualize
[2329.22 → 2329.98] deployments on
[2329.98 → 2330.34] Kubernetes.
[2330.94 → 2331.62] Learn more and get
[2331.62 → 2332.14] started at
[2332.14 → 2333.40] GoCD.org slash
[2333.40 → 2333.86] Kubernetes.
[2334.38 → 2334.76] Again,
[2334.88 → 2336.08] GoCD.org slash
[2336.08 → 2336.52] Kubernetes.
[2346.96 → 2348.04] With the pairing,
[2348.56 → 2349.44] I keep thinking
[2349.44 → 2351.90] that even with
[2351.90 → 2353.26] things that I've
[2353.26 → 2354.32] taught or talked
[2354.32 → 2355.36] about or explained
[2355.36 → 2356.66] like a dozen times
[2356.66 → 2358.16] on, you know,
[2358.36 → 2359.42] wherever, right?
[2359.42 → 2360.62] The moment I get
[2360.62 → 2361.52] on a pairing
[2361.52 → 2363.36] session, it's
[2363.36 → 2364.68] almost like I'm
[2364.68 → 2366.00] seized by this
[2366.00 → 2367.36] sort of, I
[2367.36 → 2368.16] think Yana might
[2368.16 → 2368.96] have hit on the
[2368.96 → 2369.98] nail, like the
[2369.98 → 2371.12] nail on the
[2371.12 → 2371.74] head, basically
[2371.74 → 2373.00] this intimidation
[2373.00 → 2374.08] that I feel like
[2374.08 → 2375.44] there's a pressure
[2375.44 → 2376.16] to be right.
[2376.68 → 2377.10] you know, like
[2377.10 → 2377.78] you're saying,
[2378.42 → 2379.44] Matt, you
[2379.44 → 2380.22] established a
[2380.22 → 2381.22] rapport, right?
[2381.38 → 2381.96] Especially, you
[2381.96 → 2382.74] know, I think that
[2382.74 → 2383.56] comes with if you've
[2383.56 → 2383.98] been working with
[2383.98 → 2384.66] somebody for a
[2384.66 → 2385.20] while, but you
[2385.20 → 2385.66] established a
[2385.66 → 2386.32] rapport to the
[2386.32 → 2386.62] fact where you
[2386.62 → 2387.48] can be wrong.
[2387.48 → 2388.08] But, you know,
[2388.10 → 2388.80] right now at
[2388.80 → 2389.46] work, you know,
[2389.52 → 2390.20] I get to pair
[2390.20 → 2390.72] with, you know,
[2390.74 → 2391.44] with folks from
[2391.44 → 2392.74] other teams and
[2392.74 → 2393.26] sometimes we're
[2393.26 → 2393.62] pairing for the
[2393.62 → 2395.02] first time and
[2395.02 → 2395.80] they're basically
[2395.80 → 2396.62] saying, hey, I'm
[2396.62 → 2397.08] trying to do this
[2397.08 → 2398.56] go thing, you
[2398.56 → 2399.22] know, they say
[2399.22 → 2399.42] you're the
[2399.42 → 2400.04] person to help
[2400.04 → 2400.86] and then all of
[2400.86 → 2401.22] a sudden I'm
[2401.22 → 2401.84] like, I feel that
[2401.84 → 2402.34] pressure, it's like,
[2402.40 → 2403.54] oh crap, okay, I
[2403.54 → 2403.96] don't know who
[2403.96 → 2405.30] told you what, now
[2405.30 → 2405.62] there's this
[2405.62 → 2406.62] expectation that I'm
[2406.62 → 2407.38] going to solve all
[2407.38 → 2408.22] problems, you know,
[2408.26 → 2409.44] related to go and
[2409.44 → 2410.28] then now like I
[2410.28 → 2411.02] feel like, okay, we're
[2411.02 → 2411.58] talking, and we're
[2411.58 → 2412.14] explaining something
[2412.14 → 2412.74] and I'm like, okay,
[2413.14 → 2414.24] normally it would be
[2414.24 → 2415.46] me sitting and
[2417.48 → 2418.70] now you're asking
[2418.70 → 2419.40] me to do this in
[2419.40 → 2420.64] real time, right?
[2420.74 → 2421.74] Like I have to
[2421.74 → 2423.62] basically say, okay,
[2423.80 → 2424.84] how would I do
[2424.84 → 2425.06] this?
[2425.12 → 2425.62] How would I do
[2425.62 → 2425.86] this?
[2426.08 → 2427.14] And they're sitting
[2427.14 → 2427.94] there waiting for
[2427.94 → 2428.72] me to sort of
[2428.72 → 2430.00] provide, you know,
[2430.04 → 2430.68] some guidance and
[2430.68 → 2431.50] answer, and I'm
[2431.50 → 2432.08] like sitting there
[2432.08 → 2433.00] thinking like, crap,
[2433.10 → 2433.72] normally I'd be
[2433.72 → 2434.28] sitting down and
[2434.28 → 2434.74] thinking through
[2434.74 → 2435.02] this thing.
[2435.12 → 2435.64] I mean, it takes
[2435.64 → 2436.62] hours for me to
[2436.62 → 2436.90] come up with
[2436.90 → 2437.62] something good and
[2437.62 → 2438.38] now I have to do
[2438.38 → 2439.22] it in real time and
[2439.22 → 2439.86] come up with the
[2439.86 → 2440.60] right design pattern,
[2440.72 → 2441.12] come up with the
[2441.12 → 2441.78] right abstraction,
[2441.98 → 2442.36] come up with the
[2442.36 → 2443.70] right way to, you
[2443.70 → 2444.30] know, have these
[2444.30 → 2444.90] contains communicate
[2444.90 → 2445.46] with each other,
[2445.58 → 2446.06] whatever it is.
[2446.06 → 2446.46] I mean, it's like
[2446.46 → 2447.58] it's, there's this
[2447.58 → 2448.74] pressure in the
[2448.74 → 2449.48] moment that just
[2449.48 → 2450.54] feels like
[2450.54 → 2451.72] insurmountable and
[2451.72 → 2452.90] I mean, I think I've
[2452.90 → 2453.56] been getting better
[2453.56 → 2455.30] at it but like for
[2455.30 → 2456.18] that reason alone,
[2456.18 → 2457.54] I don't enjoy
[2457.54 → 2459.50] pairing as much if
[2459.50 → 2459.94] I'm not doing
[2459.94 → 2460.96] driving but I
[2460.96 → 2462.82] realize that if I'm
[2462.82 → 2463.92] going to help
[2463.92 → 2464.70] somebody else,
[2465.10 → 2466.06] they need to be the
[2466.06 → 2466.52] one doing the
[2466.52 → 2467.14] driving because
[2467.14 → 2467.86] they're the ones
[2467.86 → 2468.60] that are going to
[2468.60 → 2469.12] learn from that
[2469.12 → 2470.00] experience and they
[2470.00 → 2470.66] can't do that if
[2470.66 → 2471.14] they're just watching
[2471.14 → 2471.80] you do the work,
[2471.88 → 2471.98] right?
[2472.00 → 2472.64] They have to do the
[2472.64 → 2472.82] work.
[2472.92 → 2473.62] So it's like a
[2473.62 → 2474.34] personal problem that
[2474.34 → 2475.24] I have to kind of
[2475.24 → 2475.92] get over but
[2475.92 → 2477.22] yeah, I'm just
[2477.22 → 2478.52] pairing is just the
[2478.52 → 2479.10] one of my least
[2479.10 → 2479.66] favourite things to
[2479.66 → 2480.62] do, but you know,
[2480.66 → 2481.24] I realize I have to
[2481.24 → 2481.92] lean into it kind of
[2481.92 → 2482.08] thing.
[2482.58 → 2483.22] Yeah, one of the
[2483.22 → 2484.30] first jobs I had in
[2484.30 → 2485.12] tech, we were
[2485.12 → 2486.60] actually pairing a
[2486.60 → 2487.96] lot and at that
[2487.96 → 2488.80] time I wish that
[2488.80 → 2489.68] like I was able to
[2489.68 → 2490.78] you know, tell
[2490.78 → 2492.14] myself that like you
[2492.14 → 2492.94] don't have to pair
[2492.94 → 2494.14] this is like only one
[2494.14 → 2494.80] way because it was
[2494.80 → 2495.64] giving me way too
[2495.64 → 2496.42] much stress,
[2496.62 → 2497.28] especially as a
[2497.28 → 2498.02] junior person that
[2498.02 → 2498.74] you don't feel that
[2498.74 → 2500.60] security and so on.
[2500.60 → 2502.12] if I can, you know,
[2502.12 → 2503.14] go back in time I
[2503.14 → 2504.54] would probably, you
[2504.54 → 2505.60] know, just like tell
[2505.60 → 2506.96] myself that like, hey,
[2507.24 → 2508.08] you know, you can just
[2508.08 → 2509.66] like ask to work in a
[2509.66 → 2510.94] different environment or
[2510.94 → 2511.92] like with like regular
[2511.92 → 2512.98] code reviews or whatever,
[2513.26 → 2514.62] which I think brings us to
[2514.62 → 2515.86] the next question.
[2516.20 → 2517.66] The next question is
[2517.66 → 2519.56] what advice would you give
[2519.56 → 2520.84] yourself at the start of
[2520.84 → 2521.86] your tech career?
[2522.14 → 2523.08] It's a great question.
[2523.26 → 2524.20] And I think I answered,
[2525.10 → 2526.12] you know, right, like I
[2526.12 → 2527.54] wouldn't necessarily think
[2527.54 → 2528.54] that pair programming
[2528.54 → 2529.46] is my thing.
[2529.96 → 2530.82] So I wouldn't really
[2530.82 → 2532.22] stress myself out because
[2532.22 → 2533.06] I'm not perfect in
[2533.06 → 2533.28] it.
[2534.14 → 2534.84] Yeah, I think that's a
[2534.84 → 2535.34] great one.
[2535.68 → 2536.84] Mine would be something
[2536.84 → 2540.50] about it being okay to
[2540.50 → 2542.84] not know everything when
[2542.84 → 2544.18] you start a project.
[2544.44 → 2547.04] It was very kind of
[2547.04 → 2549.08] tempting to fall into
[2549.08 → 2550.02] this trap and believe
[2550.02 → 2551.96] that the best software
[2551.96 → 2553.64] was designed meticulously
[2553.64 → 2555.86] and then implemented in
[2555.86 → 2556.70] that kind of waterfall
[2556.70 → 2557.52] fashion, which is
[2557.52 → 2559.42] how I assumed things
[2559.42 → 2559.92] worked.
[2560.62 → 2561.92] And it wasn't until it
[2561.92 → 2563.26] took me years, I think,
[2563.28 → 2564.58] to sort of shed that
[2564.58 → 2566.78] and instead focus on
[2566.78 → 2568.60] or realize really that
[2568.60 → 2569.82] as you're building it,
[2569.84 → 2571.26] you learn so much that
[2571.26 → 2572.52] and that that should
[2572.52 → 2573.80] influence then what
[2573.80 → 2574.30] you're doing.
[2574.68 → 2576.40] You feel something back
[2576.40 → 2577.88] from the code as well
[2577.88 → 2578.98] as you're not just in
[2578.98 → 2579.66] control of it.
[2579.70 → 2581.62] It kind of feeds back
[2581.62 → 2582.80] information to you as
[2582.80 → 2583.06] well.
[2583.64 → 2584.92] So if as you're building
[2584.92 → 2585.76] something, something
[2585.76 → 2587.50] doesn't quite fit or
[2587.50 → 2588.84] doesn't feel right or
[2588.84 → 2591.26] maybe it's just the
[2591.26 → 2592.40] abstractions wrong,
[2592.50 → 2593.32] something like that,
[2593.86 → 2595.54] that often in the early
[2595.54 → 2596.92] days felt like, well,
[2596.94 → 2598.34] then we'd failed, like
[2598.34 → 2599.84] the design had failed in
[2599.84 → 2600.62] some way when it
[2600.62 → 2601.70] hadn't because it got us
[2601.70 → 2602.64] to that point where we
[2602.64 → 2603.72] then had the extra
[2603.72 → 2604.78] learning that we wouldn't
[2604.78 → 2605.64] have had without it.
[2605.64 → 2607.74] So that's the it would be
[2607.74 → 2609.00] something along those lines.
[2609.10 → 2610.32] I mean, you know, I assume
[2610.32 → 2612.06] I'm there for a while if
[2612.06 → 2613.04] I could have to go into
[2613.04 → 2614.14] all this detail, but
[2614.14 → 2615.88] unfortunately not a snappy
[2615.88 → 2617.22] little one-liner, but it
[2617.22 → 2618.30] was, would be something
[2618.30 → 2620.06] around that, I would say.
[2620.32 → 2621.56] Did you get that impression
[2621.56 → 2623.10] because of your perception
[2623.10 → 2623.98] of like the other
[2623.98 → 2624.94] engineering fields?
[2624.94 → 2626.32] Because, you know, like the
[2626.32 → 2628.06] feedback loop in, in
[2628.06 → 2629.34] software engineering is
[2629.34 → 2630.66] really fast compared to
[2630.66 → 2631.44] everything else.
[2631.44 → 2633.38] you know if you're
[2633.38 → 2634.34] designing cars, for
[2634.34 → 2635.48] example, yeah, you're
[2635.48 → 2636.58] designing and like you
[2636.58 → 2637.68] over time, yes, learn,
[2637.88 → 2639.64] but like it takes years
[2639.64 → 2640.96] and sometimes decades to
[2640.96 → 2642.28] actually iterate on things.
[2642.70 → 2643.78] And in software is just
[2643.78 → 2644.92] like the matter of weeks
[2644.92 → 2646.22] or days, right?
[2647.14 → 2647.90] Yeah, exactly.
[2648.04 → 2648.50] That's it.
[2648.58 → 2650.24] We do have this virtual
[2650.24 → 2652.42] kind of world that we are
[2652.42 → 2654.14] operating in and the rules
[2654.14 → 2654.66] are different.
[2654.86 → 2656.48] It has its own laws of
[2656.48 → 2657.90] physics, kind of.
[2658.54 → 2659.56] So yeah, that is it.
[2659.84 → 2660.22] You're right.
[2660.22 → 2661.18] We can do things
[2661.18 → 2662.04] differently like that.
[2662.06 → 2663.26] And I think it was just
[2663.26 → 2664.66] a kind of ignorance,
[2664.78 → 2665.90] really, to the fact that
[2665.90 → 2667.86] people, it just seemed
[2667.86 → 2669.14] like that's the way
[2669.14 → 2670.50] people did things.
[2670.58 → 2671.42] I saw, you know, in the
[2671.42 → 2673.08] places I worked, people
[2673.08 → 2675.14] would very often ask for,
[2675.26 → 2676.36] right, well, give me the
[2676.36 → 2677.56] exact plan of what's
[2677.56 → 2678.34] going to happen, when
[2678.34 → 2679.32] it's going to happen by.
[2679.78 → 2680.90] And it felt like if you
[2680.90 → 2682.04] don't know these dates of
[2682.04 → 2682.88] when these things are going
[2682.88 → 2684.10] to be delivered, then
[2684.10 → 2685.00] that was, you weren't
[2685.00 → 2686.02] good enough or something.
[2686.38 → 2687.42] What I didn't realize,
[2687.74 → 2688.84] which I now know, is
[2688.84 → 2690.54] nobody knows how long
[2690.54 → 2691.32] these things are going to
[2691.32 → 2691.64] take.
[2691.94 → 2693.14] It's just some of us are
[2693.14 → 2694.10] honest about that and
[2694.10 → 2695.62] others, for whatever
[2695.62 → 2697.48] reason, aren't.
[2698.62 → 2700.88] But yeah, so this sort of
[2700.88 → 2702.82] things would be my, I would
[2702.82 → 2703.78] say to my young self.
[2703.92 → 2705.44] And be creative and play
[2705.44 → 2705.88] around.
[2706.08 → 2708.16] I mean, you know, when I was
[2708.16 → 2709.50] very young, what first
[2709.50 → 2710.80] interested me and got me
[2710.80 → 2712.14] interested in programming was
[2712.14 → 2713.72] that I could control this
[2713.72 → 2716.44] kind of crazy world in ways
[2716.44 → 2720.26] which were unique and just
[2720.26 → 2721.96] felt kind of, it was amazing
[2721.96 → 2722.94] to be able to do this.
[2723.24 → 2724.58] You know, we do things like
[2724.58 → 2727.48] write out the computer games
[2727.48 → 2730.04] from magazines, and we wrote
[2730.04 → 2732.00] a pool game once, and we were
[2732.00 → 2734.00] able to dig around in the
[2734.12 → 2735.34] they had these arrays that
[2735.34 → 2736.84] described where the pockets
[2736.84 → 2737.18] were.
[2737.38 → 2738.58] So we're able to make the
[2738.58 → 2739.70] pockets huge.
[2739.98 → 2741.18] And so then we were able to
[2741.18 → 2742.62] play this pool game with
[2742.62 → 2744.70] massive pockets, you know,
[2744.70 → 2745.74] and so that sort of
[2745.74 → 2747.08] control, and it was a
[2747.08 → 2748.92] childlike sort of thing of
[2748.92 → 2750.20] being able to manipulate
[2750.20 → 2751.64] this kind of world and do
[2751.64 → 2752.56] these crazy things.
[2752.66 → 2754.86] And that is still what
[2754.86 → 2755.90] drives me to do things
[2755.90 → 2756.26] today.
[2756.32 → 2757.38] That never changed.
[2758.28 → 2759.76] So that would be more
[2759.76 → 2761.24] advice for my young self
[2761.24 → 2762.62] would be, and I do say
[2762.62 → 2764.32] this to people, it's okay
[2764.32 → 2765.72] to play and to do things
[2765.72 → 2766.22] for fun.
[2766.32 → 2768.40] I mean, if you do, then
[2768.40 → 2770.48] your work is much more
[2770.48 → 2771.56] enjoyable, much easier.
[2771.56 → 2772.76] And sometimes it doesn't
[2772.76 → 2773.72] even feel like work.
[2774.14 → 2774.54] Yeah, totally.
[2775.04 → 2776.10] Even like it's trying to,
[2776.20 → 2777.20] you know, estimations is
[2777.20 → 2778.64] completely, I think, you
[2778.64 → 2779.24] know, nonsense.
[2779.58 → 2780.82] But even if you want to
[2780.82 → 2782.04] estimate, you know, you
[2782.04 → 2783.14] just want to play around
[2783.14 → 2784.76] just a bit like a POC or
[2784.76 → 2785.92] whatever, just kind of like
[2785.92 → 2787.20] understand what are some of
[2787.20 → 2788.56] the trade-offs and so on,
[2788.68 → 2790.26] some of the difficulties and
[2790.26 → 2791.54] so on before actually saying
[2791.54 → 2792.28] anything, right?
[2793.04 → 2793.38] Yeah.
[2793.54 → 2796.14] Another similar piece of
[2796.14 → 2797.28] advice I would say as well is
[2797.28 → 2799.98] the if you do TDD or if
[2799.98 → 2802.52] you're into testing a lot,
[2802.80 → 2804.14] there are times when
[2804.14 → 2805.58] prototyping and playing
[2805.58 → 2808.06] around is what's needed for
[2808.06 → 2809.02] you to figure out what to
[2809.02 → 2809.28] do.
[2809.76 → 2811.12] And tests can get in the way
[2811.12 → 2812.14] sometimes for that.
[2812.34 → 2812.90] It depends.
[2813.20 → 2815.24] Because if you sometimes need
[2815.24 → 2816.36] to know exactly what you're
[2816.36 → 2817.94] going to build for the test,
[2818.06 → 2819.26] to get the testing right,
[2819.92 → 2820.20] you know.
[2820.28 → 2822.14] So sometimes now I will
[2822.14 → 2823.90] actually do some prototyping
[2823.90 → 2826.22] first, get a sense of what
[2826.22 → 2827.80] kind of thing this is going
[2827.80 → 2828.16] to be.
[2828.68 → 2830.36] And then I'll actually start
[2830.36 → 2831.42] with some tests and make
[2831.42 → 2832.68] sure I've got some bits that
[2832.68 → 2834.18] I'm kind of confident are
[2834.18 → 2835.52] good foundations to build on.
[2836.36 → 2838.28] But yeah, so again, it tends
[2838.28 → 2839.48] to come down to being a bit
[2839.48 → 2841.72] more relaxed and not too
[2841.72 → 2843.06] strict about things, you know,
[2843.10 → 2844.78] because it is a it is a
[2844.78 → 2846.00] complicated process.
[2846.16 → 2847.22] I mean, building, writing
[2847.22 → 2849.62] software is absurd, absurdly
[2849.62 → 2850.14] complicated.
[2850.14 → 2851.46] And I'm, I'm constantly
[2851.46 → 2853.08] surprised anything's working
[2853.08 → 2854.48] at all, ever.
[2855.28 → 2856.72] But it does.
[2857.60 → 2858.38] John, you've been quiet.
[2859.62 → 2860.48] No, I was just thinking,
[2860.60 → 2860.90] I guess.
[2861.62 → 2862.84] For me, I think the biggest
[2862.84 → 2863.88] thing I would tell myself
[2863.88 → 2865.40] isn't specific to coding.
[2865.58 → 2867.68] It's more like what to expect
[2867.68 → 2868.62] in a work environment.
[2869.68 → 2870.42] I thought you were honestly
[2870.42 → 2871.28] going to say the lottery
[2871.28 → 2871.78] or something.
[2872.50 → 2873.42] Hear your numbers.
[2873.72 → 2874.38] It wouldn't, it wouldn't be
[2874.38 → 2874.98] so much go.
[2875.12 → 2876.18] It would be more about what
[2876.18 → 2877.38] to expect in the lottery
[2877.38 → 2877.86] numbers.
[2878.42 → 2880.50] No, like, what I mean is,
[2880.64 → 2881.96] I think a lot of people
[2881.96 → 2883.00] graduate, and they go
[2883.00 → 2883.96] take a job, and they're like,
[2884.00 → 2884.42] all right, you're going to
[2884.42 → 2885.36] be a junior engineer or
[2885.36 → 2885.56] whatever.
[2885.66 → 2886.56] You're going to have a mentor
[2886.56 → 2888.42] and in their mind, what they
[2888.42 → 2889.72] expect that to be versus
[2889.72 → 2891.32] what it actually is, is very
[2891.32 → 2891.68] different.
[2892.14 → 2893.02] I think in your head, you
[2893.02 → 2893.78] imagine I'm going to have
[2893.78 → 2894.78] this guy who's going to, a
[2894.78 → 2896.24] guy or girl, whatever, who's
[2896.24 → 2897.00] going to look over my
[2897.00 → 2898.32] shoulder, show me what I'm
[2898.32 → 2899.46] doing things wrong, like going
[2899.46 → 2900.08] to be there.
[2900.24 → 2901.38] And they forget that this
[2901.38 → 2902.86] mentor is somebody who has
[2902.86 → 2903.40] their own job.
[2903.48 → 2904.30] They have their own work to
[2904.30 → 2904.72] get done.
[2905.22 → 2906.92] And like, depending on how
[2906.92 → 2908.54] much time they have, they can
[2908.54 → 2909.74] check some things, but you
[2909.74 → 2910.96] still have to go figure a lot
[2910.96 → 2911.78] of this out on your own.
[2912.46 → 2914.16] And I know like at some of my
[2914.16 → 2915.94] first companies I worked at, I
[2915.94 → 2916.92] would get thrown all these
[2916.92 → 2918.02] different technologies and all
[2918.02 → 2918.66] these things.
[2919.00 → 2920.50] Like Google is especially kind
[2920.50 → 2921.44] of rough with that, where they
[2921.44 → 2922.62] have all this internal stuff
[2922.62 → 2924.26] and it's all really useful.
[2924.36 → 2925.18] But when you're first learning
[2925.18 → 2925.96] it all, it can feel
[2925.96 → 2926.50] overwhelming.
[2926.96 → 2928.10] So there's a while where you
[2928.10 → 2928.86] feel like you're just
[2928.86 → 2929.94] drowning and all this stuff.
[2929.98 → 2931.96] And you really like you kind
[2931.96 → 2932.96] of doubt whether you should be
[2932.96 → 2933.62] there at times.
[2933.62 → 2935.90] And I, from talking to people
[2935.90 → 2937.46] I've learned now that that's
[2937.46 → 2938.10] kind of normal.
[2938.84 → 2939.64] You know, it's just too much
[2939.64 → 2940.60] for somebody to comprehend
[2940.60 → 2941.20] all at once.
[2941.28 → 2942.90] You sort of take it one small
[2942.90 → 2944.94] step at a time and you, you
[2944.94 → 2946.12] know, gradually improve and
[2946.12 → 2947.30] learn about more stuff and you,
[2947.44 → 2949.14] you know, do the best you can.
[2949.58 → 2951.06] But it's kind of rough when
[2951.06 → 2951.88] you're there at the moment,
[2951.88 → 2954.00] just thinking like, how am I
[2954.00 → 2954.82] ever going to get through all
[2954.82 → 2955.04] this?
[2955.10 → 2955.80] How am I going to figure out
[2955.80 → 2956.80] how these things work?
[2956.98 → 2958.78] You know, like, and you don't
[2958.78 → 2959.74] have a mentor who's there
[2959.74 → 2960.78] showing you every step of the
[2960.78 → 2961.04] way.
[2961.04 → 2962.22] So like, it just can be like,
[2962.70 → 2963.72] you feel like you're failing
[2963.72 → 2964.60] even though you're not.
[2964.82 → 2966.24] So I'd probably just sort of
[2966.24 → 2967.46] have a conversation around
[2967.46 → 2968.76] that sort of aspect of like,
[2969.28 → 2971.24] it's okay to feel lost or
[2971.24 → 2973.28] confused or to feel like you
[2973.28 → 2974.26] don't know everything like
[2974.26 → 2974.86] that's normal.
[2975.44 → 2977.22] And, you know, in 10 years
[2977.22 → 2978.30] from now, you'll be amazed at
[2978.30 → 2979.38] how much, you know, and how
[2979.38 → 2980.20] much you take for granted
[2980.20 → 2983.16] that like, you'll be almost
[2983.16 → 2984.24] making the same mistakes that
[2984.24 → 2985.30] current senior engineers are
[2985.30 → 2986.04] making where they're just
[2986.04 → 2986.94] assuming, you know, all these
[2986.94 → 2987.24] things.
[2987.24 → 2988.16] And it's not intentional.
[2988.16 → 2990.42] It's just 10 years brings you
[2990.42 → 2991.02] a lot of knowledge.
[2991.04 → 2992.44] An experience that you just
[2992.44 → 2994.26] it's hard to, you know, forget
[2994.26 → 2996.42] that that's all stuff you know.
[2996.64 → 2997.78] Yeah, it's a perfect point,
[2997.86 → 2999.02] especially like the questioning.
[2999.46 → 3000.36] And sometimes you question
[3000.36 → 3001.92] yourself because the tools are
[3001.92 → 3003.42] broken or like not documented,
[3003.56 → 3003.80] whatever.
[3004.30 → 3005.44] You immediately think that the
[3005.44 → 3006.60] problem is you, but it's
[3006.60 → 3007.64] actually like the environment
[3007.64 → 3009.08] and everything is like always
[3009.08 → 3010.28] like, you know, nothing is
[3010.28 → 3011.72] really well polished or like
[3011.72 → 3012.78] complete in tech.
[3013.32 → 3014.60] Everything is like lots of
[3014.60 → 3015.74] bugs, like all these like
[3015.74 → 3016.80] legacy decisions.
[3017.14 → 3018.88] So you're somewhat questioning
[3018.88 → 3019.90] yourself because it doesn't
[3019.90 → 3021.98] truly align with what is maybe
[3021.98 → 3023.04] the ideal.
[3023.68 → 3025.58] And then, you know, you have
[3025.58 → 3026.80] to accumulate some knowledge
[3026.80 → 3028.26] and experience in order to
[3028.26 → 3029.94] understand why things ended up
[3029.94 → 3030.72] being that way.
[3030.96 → 3032.68] And, you know, that comfort I
[3032.68 → 3034.24] think comes in eventually
[3034.24 → 3036.28] because you understand how the
[3036.28 → 3038.34] industry works and, you know,
[3038.34 → 3040.28] how like everything is like
[3040.28 → 3041.98] completely always broken and it
[3041.98 → 3044.08] really depends on the specific,
[3044.28 → 3045.42] you know, experience, whatever.
[3045.42 → 3047.42] I always try to, you know, tell
[3047.42 → 3048.68] people that like, you know, if
[3048.68 → 3050.24] if you kind of like are
[3050.24 → 3052.08] struggling with a tool or with
[3052.08 → 3053.42] some many library or whatever,
[3053.52 → 3054.06] it's not you.
[3054.16 → 3054.96] It's just like, you know,
[3054.98 → 3056.54] everything is completely broken
[3056.54 → 3057.46] all the time.
[3058.20 → 3061.00] And, you know, and the easiest
[3061.00 → 3062.58] way to do is to be able to
[3062.58 → 3064.06] access to the right people to
[3064.06 → 3065.02] ask how it works.
[3066.02 → 3067.96] So I think, you know, it's just
[3067.96 → 3069.98] hard when you're very junior, but
[3069.98 → 3071.80] that's the only way, I guess.
[3071.80 → 3075.34] So my advice I'd give to
[3075.34 → 3077.66] myself, what I've found, and
[3077.66 → 3079.18] you can all probably attest to
[3079.18 → 3080.62] this as well, that over time,
[3080.62 → 3081.90] I've found myself being
[3081.90 → 3083.40] concerned less with the
[3083.40 → 3084.68] technical aspect of things and
[3084.68 → 3086.62] more with the sort of, we
[3086.62 → 3088.10] like to call it soft skills in
[3088.10 → 3089.24] this industry, but I think
[3089.24 → 3090.42] they're just skills, honestly.
[3091.00 → 3093.18] The lessons basically that I've
[3093.18 → 3094.50] taken to heart over the last,
[3094.76 → 3097.20] I think, I've forgotten how
[3097.20 → 3097.96] long I've been doing this at
[3097.96 → 3099.92] this point now, but basically
[3099.92 → 3101.24] the core lessons for me,
[3101.24 → 3103.30] the first one I'd say I'd
[3103.30 → 3104.64] give to myself and perhaps
[3104.64 → 3106.20] anybody out there who's had a
[3106.20 → 3107.86] similar path is basically
[3107.86 → 3108.78] you'll never be good at
[3108.78 → 3110.24] estimating simply because you
[3110.24 → 3111.02] can't predict the future,
[3111.44 → 3111.64] right?
[3111.92 → 3114.24] You might get better by some
[3114.24 → 3115.84] definition of better at
[3115.84 → 3117.42] estimating, but there's too
[3117.42 → 3119.26] many variables that you
[3119.26 → 3120.74] certainly do not control on the
[3120.74 → 3122.22] business side and maybe on the
[3122.22 → 3123.20] marketing side and whatever,
[3123.46 → 3123.60] right?
[3123.64 → 3125.04] There are things at play that
[3125.04 → 3126.80] you do not control that, you
[3126.80 → 3128.60] know, trying to put a specific
[3128.60 → 3129.64] date or time frame on
[3129.64 → 3130.82] something, especially something
[3130.82 → 3132.52] that is not quite yet defined.
[3132.62 → 3133.42] It's just futile.
[3133.88 → 3135.24] I've been doing this for at
[3135.24 → 3136.44] least 20 years, and I've never
[3136.44 → 3138.28] been successfully able to do
[3138.28 → 3138.50] that.
[3138.64 → 3139.80] So at some point I realized,
[3139.88 → 3141.46] okay, it's not me, right?
[3141.48 → 3143.22] I can't blame myself for being
[3143.22 → 3143.88] bad at estimating.
[3143.96 → 3144.94] It's just the nature of the
[3144.94 → 3145.90] business, right?
[3145.90 → 3146.76] It's just the nature of the
[3146.76 → 3146.98] beast.
[3147.22 → 3148.62] So chill with that, right?
[3148.62 → 3148.78] Yeah.
[3148.78 → 3150.08] It reminds me of what John said
[3150.08 → 3151.84] earlier about you, you feel
[3151.84 → 3152.96] like you're failing, but you're
[3152.96 → 3153.26] not.
[3153.38 → 3155.02] And estimations do that to us as
[3155.02 → 3155.18] well.
[3155.18 → 3157.44] We feel like if we don't hit our
[3157.44 → 3158.96] deadlines, we feel bad.
[3159.30 → 3160.96] Well, these deadlines were, they
[3160.96 → 3162.74] were crazy in the first place.
[3163.24 → 3164.30] And so we should really shouldn't
[3164.30 → 3165.06] feel bad, but we did.
[3165.14 → 3165.52] We do.
[3166.04 → 3168.76] And when people say, oh, just, we
[3168.76 → 3170.38] just want a ballpark number.
[3170.56 → 3171.94] You're not going to hold you to
[3171.94 → 3172.24] it.
[3172.24 → 3174.46] I just want to say, why did we
[3174.46 → 3175.58] just work the weekend then?
[3176.44 → 3176.72] Right.
[3176.78 → 3177.90] Because it does happen.
[3178.02 → 3179.58] People do tie other commitments
[3179.58 → 3180.12] to it.
[3180.18 → 3182.16] It does get into the, into the
[3182.16 → 3183.70] other side of the business, the
[3183.70 → 3185.14] side of it, which is whatever
[3185.14 → 3186.52] isn't the tech bit.
[3186.90 → 3189.30] But yeah, so we are asked to, I
[3189.30 → 3190.62] think, do our best or whatever.
[3190.74 → 3192.56] But yeah, I just think it's a bad
[3192.56 → 3192.98] practice.
[3193.04 → 3194.08] And I think I like the sort of
[3194.08 → 3198.50] agile, the idea of be very, make,
[3199.16 → 3201.78] expose the progress, show people
[3201.78 → 3203.34] the progress and that, and that,
[3203.66 → 3205.22] that's a great way to get a sense
[3205.22 → 3206.80] of what's actually happening.
[3206.80 → 3208.52] Because that's often what people,
[3208.86 → 3209.96] sometimes that's really what they
[3209.96 → 3212.00] really want from these estimations.
[3212.08 → 3213.54] They just want to make sure things
[3213.54 → 3215.12] are happening, and it might be their
[3215.12 → 3216.10] job to make sure things are
[3216.10 → 3216.38] happening.
[3217.02 → 3218.34] And so we, there might be other
[3218.34 → 3220.24] ways that we can, we can do that.
[3220.62 → 3222.44] But yeah, it is one of those things
[3222.44 → 3225.38] where you constantly were feeling
[3225.38 → 3229.10] like we were behind and late and we
[3229.10 → 3230.66] weren't, we really weren't.
[3230.66 → 3232.48] We were very fast and, and
[3232.48 → 3233.90] delivering, you know, very
[3233.90 → 3234.36] rapidly.
[3235.54 → 3236.92] So it should feel like that.
[3237.18 → 3237.58] Yeah.
[3237.62 → 3239.34] We never value the ambiguity.
[3240.28 → 3242.78] We, I think our company is doing a
[3242.78 → 3244.50] better job, like some sort of like
[3244.50 → 3247.28] they measure, like if you want to go
[3247.28 → 3249.20] become a very senior engineer, it's
[3249.20 → 3251.68] just like your skills to deal with
[3251.68 → 3252.20] the ambiguity.
[3252.20 → 3253.60] And it's not about the technical
[3253.60 → 3254.12] challenges.
[3254.12 → 3255.56] It's about the business challenges.
[3256.20 → 3258.12] It's about like, you know, negotiating
[3258.12 → 3260.10] people, like communicating things.
[3260.56 → 3262.44] Isn't it like funny that like we call
[3262.44 → 3264.16] this stuff soft skills, like these
[3264.16 → 3266.08] are very hard stuff, and it's just
[3266.08 → 3267.62] like completely not up to you.
[3267.84 → 3269.94] You may have like some skills or like
[3269.94 → 3272.46] you may just help the situation, but
[3272.46 → 3273.94] it's just like extraordinarily
[3273.94 → 3274.78] complicated.
[3275.34 → 3277.84] You need to have like perfect
[3277.84 → 3280.10] skills all across, including technical
[3280.10 → 3282.08] skills to deal with any of this.
[3282.40 → 3284.26] And you sort of like feel like the only
[3284.26 → 3286.34] limit is just becoming this type of
[3286.34 → 3287.42] issues.
[3288.08 → 3289.66] You know, like technically, I think
[3289.66 → 3290.76] everything is possible.
[3291.36 → 3292.66] I mean, not everything is possible.
[3292.86 → 3294.76] I think technical problems are easy.
[3295.34 → 3297.20] The actual limitations are this type
[3297.20 → 3298.12] of problems.
[3299.20 → 3301.34] And it's amazing that we call them
[3301.34 → 3303.70] underestimate them as soft skills.
[3304.52 → 3306.12] Personally, I think these are part of
[3306.12 → 3307.84] problem-solving skills.
[3308.68 → 3310.12] And for me, the best way of
[3310.12 → 3312.34] understanding problems is to basically
[3312.34 → 3313.56] understand the business you're in.
[3313.72 → 3315.26] And that means you're talking to people
[3315.26 → 3317.44] that are not other, you know,
[3317.56 → 3318.56] techies, right?
[3318.58 → 3319.92] That are not in the room coding with
[3319.92 → 3321.38] you or designing with you or whatever,
[3321.54 → 3321.70] right?
[3321.70 → 3323.72] So you have to actually step outside
[3323.72 → 3325.78] your bubble to understand basically
[3325.78 → 3328.74] the greater world around you and the
[3328.74 → 3329.52] people you work with.
[3329.64 → 3331.12] And, you know, hey, take the sales
[3331.12 → 3333.02] person out, you know, for coffee and
[3333.02 → 3334.60] get them to explain what the process
[3334.60 → 3336.34] is like, you know, go sit down with
[3336.34 → 3338.40] marketing and see what they do all
[3338.40 → 3338.86] day, right?
[3339.36 → 3341.34] And, you know, talk to operations,
[3341.34 → 3342.30] operations, right?
[3342.32 → 3343.64] The business operations folks and
[3343.64 → 3344.90] see what they, I mean, you're going
[3344.90 → 3346.60] to get a view of the business that
[3346.60 → 3347.98] is going to inform how you solve
[3347.98 → 3349.50] problems and actually recommend
[3349.50 → 3350.98] solutions that keep moving a ball
[3350.98 → 3351.62] forward, right?
[3351.68 → 3354.14] So, but that starts with people and
[3354.14 → 3355.38] being able to interact with people.
[3355.56 → 3357.30] So along those lines, I usually tell
[3357.30 → 3358.46] people like, look, at the end of the
[3358.46 → 3360.62] day, the tech is a tool that enables
[3360.62 → 3362.76] some entity to arrive at a particular
[3362.76 → 3363.12] goal.
[3363.72 → 3366.10] Be that goal money or, you know,
[3366.32 → 3367.90] doing good in the world, whatever the
[3367.90 → 3368.72] case may be, right?
[3368.82 → 3369.86] Tech is a tool, right?
[3369.86 → 3371.24] And you're a specialist, you're
[3371.24 → 3372.36] who knows how to use the tool.
[3372.46 → 3373.88] So tech doesn't matter as much as
[3373.88 → 3374.82] people, right?
[3374.90 → 3376.64] So, you know, be kind, right?
[3376.70 → 3377.86] And interact, learn or interact,
[3378.08 → 3378.26] right?
[3378.60 → 3379.42] Give love yourself.
[3379.96 → 3381.42] Give and you will receive, right?
[3381.48 → 3383.84] Not money, but, you know, time.
[3384.04 → 3385.20] Like give of yourself, right?
[3385.78 → 3387.44] So, and basically along those lines,
[3387.52 → 3389.98] the last thing I'll add is that
[3389.98 → 3392.86] basically I've found an over time,
[3393.60 → 3394.90] I like to use that phrase sort of
[3394.90 → 3395.64] ego is the enemy.
[3395.82 → 3397.68] Like I found like over time, like
[3397.68 → 3401.24] basically the your ego yourself is
[3401.24 → 3402.86] always putting obstacles in your way,
[3403.00 → 3403.18] right?
[3403.26 → 3404.84] The whole thing I talked about earlier
[3404.84 → 3406.72] about when I, when I pair, I feel the
[3406.72 → 3408.34] intense pressure to perform, right?
[3408.72 → 3409.70] That's ego, right?
[3409.70 → 3411.10] That's basically saying, hey, you
[3411.10 → 3411.86] better look good.
[3411.96 → 3413.36] Our survival depends on it, right?
[3414.08 → 3415.66] So it's like, you know, there's a
[3415.66 → 3417.32] constantly, you have this voice in the
[3417.32 → 3418.90] back of your head that's saying, hey,
[3419.28 → 3421.26] you know, oh, you messed up here, man.
[3421.30 → 3422.32] Like you shouldn't have done that.
[3422.32 → 3423.94] Or you got to say the perfect thing
[3423.94 → 3424.16] here.
[3424.24 → 3425.28] You got to be the perfect person
[3425.28 → 3425.52] here.
[3425.62 → 3426.98] I mean, that's like basically just,
[3427.34 → 3428.98] just in, you know, causing you to
[3428.98 → 3430.30] act a certain way, causing you to
[3430.30 → 3431.84] act selfishly, causing you to like,
[3431.86 → 3433.50] you know, to pretend to be things or
[3433.50 → 3434.74] not all these things.
[3434.86 → 3436.12] And that's just part of the self and
[3436.12 → 3438.14] keeping tabs on, stay on top of that.
[3438.60 → 3439.88] I mean, honestly, that's, that's the
[3439.88 → 3441.32] part, that's the next decade over,
[3441.42 → 3443.20] over my, my life that I'm honestly
[3443.20 → 3444.52] trying to work on is basically try
[3444.52 → 3446.76] to identify when ego is taking me for
[3446.76 → 3448.10] a ride and just kicking him out the
[3448.10 → 3448.32] car.
[3449.04 → 3449.44] Great.
[3449.80 → 3450.12] Yeah.
[3450.12 → 3451.90] You know, that little small voice in
[3451.90 → 3453.28] your head that tells you not to say
[3453.28 → 3453.76] things.
[3454.28 → 3455.46] What, what is that?
[3456.80 → 3457.76] How do you get one?
[3459.44 → 3460.20] You want one of those?
[3460.20 → 3461.56] Is it like an in-app purchase?
[3463.18 → 3464.46] That'd be good if you could just in-app
[3464.46 → 3465.80] purchase stuff into your brain,
[3465.86 → 3466.08] wouldn't it?
[3466.90 → 3468.38] We think of like, it's the matrix,
[3468.62 → 3470.52] but it wouldn't be free, would it?
[3470.78 → 3471.94] You're going to have to pay for that.
[3472.02 → 3473.10] If you want to, if you want to learn
[3473.10 → 3475.60] how to fly that helicopter, sit down,
[3475.76 → 3477.10] put your head, put this in your head,
[3477.10 → 3478.74] but you know, put your credit card
[3478.74 → 3479.00] here.
[3479.92 → 3480.82] That's how it would be.
[3482.10 → 3483.68] But that's great advice, Johnny,
[3483.78 → 3484.12] actually.
[3484.30 → 3485.96] And I also do recognize that.
[3486.32 → 3487.52] And, and that's the thing about finding
[3487.52 → 3489.32] a good partner and a good team to work
[3489.32 → 3492.08] with is if you can, if, if they're
[3492.08 → 3494.48] decent people as well, it's easier to
[3494.48 → 3495.94] get over some of that things.
[3495.94 → 3497.40] And you can sometimes be honest about
[3497.40 → 3498.66] it and say, yeah, do you know what?
[3498.82 → 3501.04] I think that was unreasonable there or
[3501.04 → 3501.10] whatever.
[3501.68 → 3503.28] You can sort of be a little bit more
[3503.28 → 3504.96] open about these kinds of things and
[3504.96 → 3506.68] then you can move past it and stuff.
[3506.68 → 3507.40] I think that's great.
[3507.94 → 3508.08] Yeah.
[3508.10 → 3509.92] I think in order to like let go of
[3509.92 → 3511.56] the ego, you need to be vulnerable
[3511.56 → 3512.46] a bit.
[3512.90 → 3514.58] And, you know, this is also working the
[3514.58 → 3517.62] same way in relationships, any sort
[3517.62 → 3518.28] of relationship.
[3518.28 → 3520.14] And I think like a couple of years
[3520.14 → 3521.80] ago, I was in a sort of like a
[3521.80 → 3523.48] situation where I finally ended up
[3523.48 → 3525.60] feeling more comfortable being
[3525.60 → 3527.50] vulnerable, and it completely changed
[3527.50 → 3528.12] my life.
[3528.44 → 3531.42] I finally understood, you know, what I
[3531.42 → 3533.68] need to do and to do the next
[3533.68 → 3534.14] thing.
[3534.14 → 3536.52] And now like similarly to Johnny,
[3536.72 → 3538.64] probably I will spend the next 10
[3538.64 → 3540.26] years working on this type of
[3540.26 → 3540.64] skills.
[3541.22 → 3543.32] I think it's, I mean, it goes to show
[3543.32 → 3545.12] that when Matt talks about pair
[3545.12 → 3546.50] programming all this time, he talks
[3546.50 → 3547.98] about a co-founder that he's been
[3547.98 → 3549.22] doing this with for a long, long
[3549.22 → 3549.58] time.
[3550.32 → 3552.34] And whenever you talk about like when
[3552.34 → 3553.94] you feel uncomfortable, it's with new
[3553.94 → 3554.26] people.
[3554.26 → 3555.52] It's with people you don't have that
[3555.52 → 3557.70] trust with or that relationship with.
[3557.70 → 3559.42] And I suspect that's part of the
[3559.42 → 3561.52] reason why, like, I know I'm included
[3561.52 → 3561.88] in this.
[3562.06 → 3564.04] I don't like doing live, just live
[3564.04 → 3565.40] streaming myself coding on like
[3565.40 → 3567.24] Twitch or something because I'm like,
[3567.30 → 3569.00] if I make a mistake, there's going to
[3569.00 → 3571.18] be that one person there who like makes
[3571.18 → 3572.10] a big deal out of it.
[3572.10 → 3573.40] And it's like, we all make mistakes.
[3574.24 → 3575.14] Somebody's going to be like, that guy
[3575.14 → 3575.90] doesn't know what he's doing.
[3575.98 → 3577.54] Like, you know, he did that mistake.
[3577.68 → 3579.04] So you just get worried and paranoid.
[3579.04 → 3581.20] But like, I also know that I've done
[3581.20 → 3583.70] screen sharing, like to either to review
[3583.70 → 3585.40] code or to look at some tough parts of a
[3585.40 → 3587.66] you know, code base at a startup I was
[3587.66 → 3588.22] at a while back.
[3588.24 → 3589.66] And it was like the actual founder and I
[3589.66 → 3590.80] both did this all the time.
[3591.00 → 3592.52] But we had a perfect relationship.
[3592.52 → 3594.40] And that just made it like I didn't mind
[3594.40 → 3595.54] jumping in there and being like, I have
[3595.54 → 3597.52] no idea what's going on here or how to
[3597.52 → 3598.10] deal with this.
[3598.36 → 3599.52] And it was easy to solve.
[3599.54 → 3600.88] And like, we both had that relationship
[3600.88 → 3602.30] where he could do that with me, too.
[3602.34 → 3604.04] And it solved a lot of problems.
[3604.32 → 3605.76] But when you don't know somebody, it's
[3605.76 → 3606.76] hard because you're like, how are they
[3606.76 → 3608.80] going to react when like that's what I
[3608.80 → 3610.20] have to tell them is like, I don't know.
[3611.40 → 3611.72] Yeah.
[3612.06 → 3613.72] Well, from a tech leadership point of
[3613.72 → 3614.88] view, it's a red flag.
[3614.88 → 3617.54] When somebody never says, I don't know.
[3617.74 → 3619.76] If there's somebody who's always certain
[3619.76 → 3622.46] about everything, then they probably
[3622.46 → 3623.56] obviously they're not.
[3624.00 → 3625.08] Something else is going on.
[3625.50 → 3626.92] So that's a good bit of advice.
[3626.92 → 3629.60] I think for people are, you know, and
[3629.60 → 3631.28] again, it's very easy for me to say this.
[3631.38 → 3632.82] And we're now more senior.
[3633.02 → 3636.26] So it is easier to struggle to remember
[3636.26 → 3637.54] what it was really like.
[3637.92 → 3640.04] Although it's not that many years ago,
[3640.04 → 3640.32] is it?
[3640.38 → 3640.80] Come on.
[3640.80 → 3643.28] Some good leaders actually like create
[3643.28 → 3645.00] some opportunity to, you know, make
[3645.00 → 3646.24] themselves look vulnerable.
[3646.96 → 3648.74] Like they even actually like just create
[3648.74 → 3651.54] situations that like they can easily
[3651.54 → 3653.22] like say that like, hey, I don't know.
[3653.32 → 3654.86] We need to understand this, whatever.
[3654.86 → 3657.78] So they would like just like keep reminding
[3657.78 → 3660.32] you that like, you know, nothing.
[3660.98 → 3661.96] It's not you.
[3661.96 → 3664.46] It's not your lack of knowledge or experience
[3664.46 → 3665.04] or whatever.
[3665.38 → 3667.52] So that's like one step, I think, further
[3667.52 → 3669.54] saying, I don't know, it's like a good
[3669.54 → 3669.90] step.
[3669.90 → 3672.28] But like if you actively are creating those
[3672.28 → 3674.30] moments, that just really gives a lot of
[3674.30 → 3675.64] comfort to people around you.
[3676.14 → 3677.14] Yeah, that's interesting.
[3677.26 → 3679.78] I know I did a pair programming session
[3679.78 → 3681.34] a few years ago with a more junior
[3681.34 → 3684.68] developer, and we were plowing through
[3684.68 → 3686.00] something, and it was kind of halfway
[3686.00 → 3686.26] through.
[3686.34 → 3688.42] I realized that I'm probably just going
[3688.42 → 3691.76] way too fast and making this look like
[3691.76 → 3694.44] I probably look perfect doing it,
[3694.52 → 3696.62] but I make this look really hard.
[3696.62 → 3699.06] And like you have to be some, you know,
[3699.12 → 3701.32] amazing coder to be able to do it,
[3701.38 → 3703.12] which of course isn't the case.
[3703.50 → 3704.48] And so, yeah, right.
[3704.54 → 3706.40] You have to sort of be mindful of that
[3706.40 → 3706.66] as well.
[3706.68 → 3708.42] I was just doing my thing trying to
[3708.42 → 3710.32] solve a problem, and I wasn't bringing
[3710.32 → 3712.06] people along with me in that case.
[3712.22 → 3714.24] So that was an important lesson for me.
[3714.74 → 3716.62] I think it's kind of a great way to
[3716.62 → 3718.70] work, but yeah, it does rely on that
[3718.70 → 3721.14] sort of trust in the teams and things.
[3721.40 → 3722.52] And I think you're right, being
[3722.52 → 3725.30] vulnerable and admitting, yeah, I don't
[3725.30 → 3725.98] know about this.
[3726.14 → 3727.12] We're going to have to figure it out
[3727.12 → 3729.74] together, and we'll succeed together
[3729.74 → 3732.10] or we won't succeed together, you know.
[3732.42 → 3735.86] It's better because you remove any of
[3735.86 → 3737.98] this sort of, a lot of these personal
[3737.98 → 3742.64] difficult challenges that people feel.
[3742.72 → 3744.54] You can remove a lot just by having a
[3744.54 → 3746.14] slightly different culture like that.
[3747.02 → 3747.42] Yeah.
[3747.94 → 3749.44] I think you even see it with like how
[3749.44 → 3750.64] people react to issues.
[3750.78 → 3752.02] Like we've all heard those stories
[3752.02 → 3754.22] about like, oh, some junior developer
[3754.22 → 3755.66] deleted the whole database or something
[3755.66 → 3756.20] like that.
[3756.36 → 3758.56] And how the company responds to that,
[3758.64 → 3760.92] like demonstrates how they're going to
[3760.92 → 3762.46] take that vulnerability, like how they're
[3762.46 → 3764.26] going to treat it very, like it's a very
[3764.26 → 3765.00] clear indicator.
[3765.44 → 3766.74] So like when you see a company that's
[3766.74 → 3768.18] like, well, this happened, it shouldn't
[3768.18 → 3768.92] have been able to happen.
[3769.02 → 3770.06] Like we're not blaming him.
[3770.18 → 3771.10] Here's how we're fixing it.
[3772.18 → 3773.56] Like then you're like, okay, I have way
[3773.56 → 3775.42] more confidence in, you know, being
[3775.42 → 3776.16] vulnerable here.
[3776.40 → 3777.88] But when you see the person get fired,
[3777.96 → 3779.72] you're like, well, time to not let
[3779.72 → 3780.86] anybody know about my mistakes.
[3781.66 → 3781.98] Right.
[3782.14 → 3782.46] Exactly.
[3782.56 → 3782.80] Yeah.
[3783.10 → 3783.38] Yeah.
[3783.38 → 3784.18] It's a bad signal.
[3785.36 → 3785.46] Yeah.
[3785.54 → 3786.54] Cloudflare did it recently.
[3786.54 → 3789.16] There was an issue that was just a bad
[3789.16 → 3790.88] config file that got pushed or something.
[3791.58 → 3793.18] And they just sort of transparent about
[3793.18 → 3794.22] it, open about it.
[3794.42 → 3796.86] And people were asking and someone said,
[3796.94 → 3798.14] you know, is this person going to be
[3798.14 → 3798.80] fired or something?
[3798.90 → 3800.62] And the answer was no.
[3800.88 → 3804.12] I think the CTO said, no, these things
[3804.12 → 3804.46] happen.
[3804.62 → 3806.62] You know, it's a process issue we have to
[3806.62 → 3806.98] look at.
[3807.18 → 3808.66] And I think that is the right attitude.
[3809.00 → 3809.16] Yeah.
[3809.20 → 3810.22] Because otherwise what happens?
[3810.32 → 3811.96] Think about what happens if you create
[3811.96 → 3813.18] this sort of toxic cultures.
[3813.18 → 3815.96] I mean, this is a whole other area,
[3816.18 → 3818.02] I think, for another time.
[3818.20 → 3822.02] I believe our hour has come up now.
[3822.18 → 3824.36] Thank you very much to everybody for
[3824.36 → 3825.02] joining me.
[3825.42 → 3826.98] Jana, John and Johnny.
[3827.46 → 3830.68] And we'll see you next time on Go Time.
[3834.34 → 3835.02] All right.
[3835.08 → 3836.34] Thank you for tuning in to this week's
[3836.34 → 3837.60] episode of Go Time.
[3837.68 → 3839.70] If you're not yet, hang with us and go
[3839.70 → 3840.16] for slight.
[3840.26 → 3842.00] We have a channel called Go Time FM.
[3842.00 → 3843.16] Look it up.
[3843.22 → 3843.96] You'll find us.
[3844.38 → 3845.90] Hang with us during the live shows.
[3846.04 → 3846.94] Connect with other members of the
[3846.94 → 3847.30] community.
[3847.84 → 3848.54] Share stories.
[3849.12 → 3849.70] Share codes.
[3849.88 → 3850.68] Share coffee recipes.
[3850.80 → 3851.02] Whatever.
[3851.44 → 3852.36] It's a lot of fun.
[3852.74 → 3854.26] Also, we have discussions at
[3854.26 → 3856.34] changelaw.com on every episode.
[3856.82 → 3858.86] Head to changelaw.com slash Go Time.
[3858.98 → 3861.06] Find this episode and discuss it with
[3861.06 → 3861.50] the community.
[3861.96 → 3863.56] Also, thanks to Vastly, our bandwidth
[3863.56 → 3865.36] partner, Rollbar, for helping us move
[3865.36 → 3866.92] fast and fix things.
[3867.20 → 3868.64] And Linde for hosting the Change Law
[3868.64 → 3869.18] platform.
[3869.64 → 3871.34] Our music is produced by the mysterious
[3871.34 → 3872.44] Break master Cylinder.
[3872.92 → 3874.14] And if you want to hear more awesome
[3874.14 → 3876.32] podcasts like this, subscribe to our
[3876.32 → 3876.94] master feed.
[3877.02 → 3879.08] It's one feed to rule them all, plus
[3879.08 → 3880.82] some extras that only hit the master
[3880.82 → 3881.30] feed.
[3881.66 → 3883.90] Head to changelaw.com slash master or
[3883.90 → 3885.68] search for Change Law Master in your
[3885.68 → 3886.48] podcast client.
[3886.56 → 3887.22] You'll find us.
[3887.56 → 3888.40] Thanks for tuning in.
[3888.40 → 3889.46] We'll see you next week.
[3889.46 → 3889.50] We'll see you next week.
[3889.50 → 3889.78] We'll see you next week.
[3889.78 → 3919.76] Thank you.
[3919.78 → 3949.76] Thank you.
