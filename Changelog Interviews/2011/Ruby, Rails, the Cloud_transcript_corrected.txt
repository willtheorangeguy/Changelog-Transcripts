[0.00 → 2.46] This is Dr. Nick Williams, and you are listening to The Changelog.
[17.68 → 20.70] Welcome to The Changelog, episode 0.5.0.
[20.92 → 21.92] I'm Adam Stachowiak.
[22.26 → 23.16] And I'm Wynne Netherlands.
[23.32 → 24.18] This is The Changelog.
[24.22 → 26.22] We cover what's fresh and new in the world of open source.
[26.44 → 29.46] If you found us on iTunes, we're also on the web, thechangelog.com.
[29.46 → 30.74] We're also on GitHub.
[31.24 → 32.76] Head to GitHub.com slash explore.
[32.84 → 37.00] You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[37.24 → 41.16] And if you're on Twitter, follow Changelog Show, Changelog Jobs, and me, Adam Stack.
[41.54 → 43.98] And I'm Penguin, P-E-N-G-W-Y-N-N.
[44.50 → 46.28] This episode is sponsored by GitHub Jobs.
[46.38 → 49.32] Head to thechangelog.com slash jobs to get started.
[50.04 → 54.18] If you'd like us to feature your job on the show, select Advertise on the Changelog when you post your job,
[54.26 → 55.22] and we'll take care of the rest.
[55.48 → 58.06] Up this week, our friends at Pusher over in London.
[58.06 → 60.70] I'm looking for someone that knows the vented scene.
[61.10 → 64.54] Experience with Node.js, Regis, and message queues are a big bonus.
[65.20 → 70.40] I prefer people that can work in the U.S. remote or in the London neighbourhood of EC1.
[70.84 → 74.44] If you're interested, LG.Gd slash 8c.
[74.44 → 79.16] If you're a software dev in the Toronto area, in the Python and PHP community,
[79.30 → 81.76] and love the fast-paced and creative environment of a startup,
[82.06 → 85.68] FreshBooks is looking for a disciplined developer who doesn't sneer at scripting languages,
[85.80 → 88.56] but also knows their enterprise-level stuff.
[89.08 → 91.40] Check out LG.Gd slash 8c.
[91.40 → 93.62] Fun episode this week.
[93.70 → 98.10] Steve and I sat down with Dr. Nick Williams, a hilarious Aussie from down under.
[98.68 → 104.12] Now lives in San Francisco, works at Engine Yard, big in the Ruby community, works on the cloud.
[104.40 → 105.28] You'll find out what that means.
[106.62 → 108.60] He's keynoting at RedDirtRubyConf.
[108.66 → 109.90] We'll be there doing a live episode.
[109.90 → 113.26] That is in April, April 21st and 22nd.
[113.26 → 114.96] Prior to that, he'll be at Comecon.
[115.08 → 118.28] Be sure and catch him there, as will our buddy Steve Flank,
[118.34 → 121.68] will be the official changelog correspondent at GitHub Comecon.
[122.46 → 127.80] And in March, March 11th through the 13th is the main conference, Pylon in Atlanta.
[128.60 → 132.76] Kenneth will be there, hopefully, with a big bag of changelog tees.
[133.36 → 133.74] Absolutely.
[134.08 → 134.58] And a mic.
[135.70 → 136.50] And a mic.
[136.50 → 139.78] And for all of you guys out there actually asking us for more Python,
[140.88 → 144.00] head up Kenneth for that because he can help us out there.
[144.18 → 147.96] And if you're going to be at Pylon, and he's got a mic in his hand, go say hi.
[148.42 → 152.48] Say, I have this cool Python project and needs to be on the changelog.
[152.56 → 154.72] Just grab him by the arm and say, interview me now.
[155.32 → 155.78] That's right.
[156.06 → 156.52] Interview him now.
[156.74 → 159.24] And this is episode 50, so this is a big thing for us.
[159.34 → 163.32] We're excited about being on the air and thanking you for listening to us
[163.32 → 164.48] and supporting us all this time.
[164.48 → 169.84] And thanks to GitHub and thanks to all the people who have us promote their jobs
[169.84 → 174.60] and everything for readers and Wynn and the rest of the team for supporting us.
[174.66 → 175.14] It's been awesome.
[176.00 → 177.92] Thanks for putting up with us for 50 episodes.
[178.04 → 179.08] Hopefully, here's to 50 more.
[179.88 → 180.38] All righty.
[180.72 → 181.32] Fun episode this week.
[181.38 → 181.94] You want to get to it?
[182.38 → 183.02] Let's do it.
[183.02 → 194.72] We're chatting today with Dr. Nick Williams from Engine Yard.
[195.00 → 197.84] So, Dr. Nick, for those that don't know you, I want you to introduce yourself
[197.84 → 199.02] and your role over at Engine Yard.
[199.52 → 205.04] I am one of the early Rails developers and users and fell in love with Rails back in 2005
[205.04 → 212.20] when Ajax came out and fell in love with Ruby and made lots and lots of little open source projects.
[213.16 → 215.94] And I think lots of people have used at least one of them.
[216.40 → 222.98] So, I ended up finding my way over to Engine Yard over here in San Francisco, America,
[223.78 → 225.04] which is not where I come from.
[225.04 → 233.42] And I now have the very cool job of both looking after our large open source program over here,
[233.48 → 240.60] which is the Ruinous, Ruby, Fog, and Rails in general, as well as our grants program.
[241.26 → 245.58] And I also sort of take a developer advocate role here for our products.
[246.54 → 250.56] Well, believe it or not, we have a lot of non-Subsists that listen to this show.
[250.74 → 253.28] So, what does Engine Yard specialize in?
[253.28 → 258.74] We specialize in Ruby, specifically getting Ruby into the cloud.
[258.98 → 262.12] So, for Rails apps, Rack apps, Sinatra, MIR,
[262.64 → 268.58] we think there's a huge marketplace for just that niche in of itself.
[270.18 → 273.92] So, we essentially deploy to two different infrastructures,
[274.34 → 277.10] which is the fancy phrase for Amazon and Terra mark.
[278.50 → 282.16] Because, yeah, I mean, a lot of people don't even know that Terra mark exists and why,
[282.16 → 287.88] because there's just different customers have different reasons for different needs of their infrastructure,
[288.00 → 289.24] and Amazon doesn't provide all of them.
[290.58 → 291.70] So, you say cloud.
[291.88 → 292.82] Oh, I know, cloud.
[292.90 → 293.60] Isn't that a cool name?
[294.08 → 296.10] I've heard of a hundred different definitions for cloud.
[296.10 → 300.44] You drive down the 101 here out of San Francisco,
[300.44 → 303.70] and there are big billboards with the word cloud on it,
[303.78 → 305.90] and Microsoft attempting to tell you what cloud is.
[307.86 → 312.26] So, essentially, cloud is – I trivialize it for my own amusement.
[312.54 → 315.90] Cloud is the shiny new name for this thing we call the internet.
[315.90 → 322.94] But what it is allowing us to provision resources,
[323.48 → 327.50] like compute resources, storage resources via APIs,
[327.80 → 329.72] and pay for them on a sort of rental basis,
[330.20 → 333.50] which means that you don't have to go off to Dell and fill up the back office
[333.50 → 338.04] or fill up a data centre with machines in case you might get traffic.
[338.04 → 343.14] You can start small and grow based on success of the business or the traffic that you drive,
[343.70 → 348.88] which is really, really important for nearly every app that's being built these days.
[349.32 → 354.22] The whole world is moving to cloud, but that doesn't make it necessarily easy.
[354.32 → 355.76] It just means that you know you have to go there.
[357.02 → 358.04] Yeah, that's definitely true.
[358.18 → 360.58] I have a lot of friends who come from a non-web perspective,
[360.84 → 364.86] and they do the standard, oh, poo-poo, cloud kind of thing,
[364.92 → 366.68] and so we talk about this stuff a lot.
[366.68 → 369.24] But I definitely agree the cloud is becoming super important.
[369.42 → 373.18] You guys have done a lot of great stuff, and historically we've done a lot for Ruby.
[373.44 → 377.36] So one of the things that's always interested me, I guess, about you,
[377.44 → 382.22] as long as I've known about you, is that you have 154 public repos on GitHub.
[382.40 → 384.38] Like you said, you have a lot of open source projects,
[384.46 → 386.16] and everybody's used probably at least one of them.
[386.40 → 388.58] And I find myself in the same position.
[388.58 → 392.66] Like I literally wrote and released a tiny little Ruby gem last night
[392.66 → 394.64] after I was tired when I came home
[394.64 → 397.58] because there was some little idea that I wanted to bring up there.
[397.72 → 400.92] So how do you manage running that many projects
[400.92 → 403.10] and keeping abreast of if they need something?
[403.20 → 405.22] Do you sort of abandon a lot of old ones?
[405.32 → 408.44] Do you actively try to work on your older projects?
[408.52 → 409.24] How does that all work?
[409.60 → 411.00] I actively abandon them.
[411.50 → 413.14] I mean, you just can't.
[413.34 → 414.36] I think I did a talk.
[414.78 → 416.82] I mean, if you ever sit down and think about it,
[416.82 → 417.82] you mathematically just can't.
[417.82 → 420.12] I think I did a talk at Future Ruby,
[420.56 → 424.06] which is whilst a Ruby conference had lots and lots of different content.
[424.42 → 428.08] And I think all the talks for Future Ruby were put on Info,
[428.18 → 429.24] so you can go back and find those.
[429.30 → 430.40] A lot of interesting talks.
[430.84 → 434.16] The topic that I talked about was how you have 1,000 projects.
[434.78 → 437.36] Because I did this back of a napkin-type calculation.
[437.52 → 439.96] After three years of doing open source, I had 75 projects.
[440.90 → 444.74] And 75 kind of realism projects, not just demo apps or something.
[444.74 → 447.72] And I kind of figured if you did the math, and you had a job,
[447.84 → 451.80] did this for 40 years, which what we do in open source is wonderful.
[451.98 → 454.60] It's like being a garage mechanic, except you get to do it in public.
[455.12 → 458.44] You make shiny things and show them off and let other people use them.
[459.00 → 460.64] Why wouldn't you end up with 1,000 projects?
[461.60 → 464.00] And I quickly realized that was going to be disastrous
[464.00 → 466.70] for my social and martial life.
[467.50 → 470.38] Yeah, so I had to figure out what the solution to that problem was,
[470.58 → 471.88] and I figured it was worth sharing.
[471.88 → 477.90] And active, aggressive abandonment is an important part of that.
[478.40 → 480.82] And that's only really possible now because of things like GitHub.
[481.44 → 484.30] Back in the subversion and CVS days,
[484.40 → 486.18] you couldn't really just abandon projects
[486.18 → 489.22] and assume that they might survive.
[489.32 → 491.02] But with GitHub, people can discover projects,
[491.14 → 493.58] people can fork them, have their own permission structures.
[494.50 → 496.24] Now, in Ruby, you're allowed to release gems,
[497.24 → 498.36] even in your own name,
[498.36 → 501.92] I assume in different communities or different packaging environments,
[502.04 → 503.18] they'll have their own solution to that.
[503.96 → 507.14] So really, in this modern world, in 2010, 2011,
[507.78 → 510.64] making projects as ideas and releasing them,
[510.86 → 512.68] we're really enabled to do that these days.
[513.54 → 514.78] Yeah, I almost wonder,
[515.10 → 517.10] having taken on two of Y's old projects,
[517.28 → 519.36] I almost wonder if that wasn't part of his deal,
[519.46 → 521.36] was having too many things open at once
[521.36 → 523.90] because Hacking and Shoes is a handful enough for me,
[523.98 → 524.76] as it is,
[524.80 → 526.76] not that I'm the same person Y is, obviously,
[526.76 → 530.84] but it's definitely hard to contribute to so many things at once.
[531.18 → 534.10] James Buck, who created a project,
[534.22 → 536.36] he created a bunch of projects in his early Ruby days,
[536.44 → 538.20] but his most hugely popular one
[538.20 → 541.18] was a deployment tool called Cristiano,
[541.86 → 546.56] which was the definitive way that Ruby applications got deployed.
[546.92 → 549.88] And then one day, he publicly declared
[549.88 → 551.78] he was abandoning the project,
[552.06 → 552.62] which I thought was,
[553.12 → 556.56] and he got massive feedback of praise and admiration,
[556.56 → 557.40] and thanks.
[557.92 → 559.00] And I thought that was genius
[559.00 → 560.08] because it never occurred to me
[560.08 → 561.46] to publicly tell people I was nervous,
[561.52 → 562.44] I'm going to work on something.
[563.18 → 565.82] So I thought that was pretty genius at the time.
[567.48 → 571.08] So, yeah, I think there are a lot of examples of people
[571.08 → 573.02] who start a wonderful project.
[573.46 → 575.78] And sometimes just the community just needs to know
[575.78 → 576.90] that they're allowed to participate.
[577.48 → 579.28] GitHub, again, has really,
[579.46 → 580.62] and that whole community notion
[580.62 → 583.12] has really been fostered around open source.
[583.78 → 587.64] And I think the less people need to be actually explicitly told
[587.64 → 588.36] they can participate,
[588.90 → 590.26] I think more, and more people know
[590.26 → 593.26] they can just fork, add features, send pull requests.
[594.38 → 596.96] So I think it's very healthy, I think, these days
[596.96 → 599.52] to feel that you can just start a new project
[599.52 → 601.06] and know that someone will turn up and help.
[601.50 → 602.86] You know, Kenneth and Steve tell me
[602.86 → 603.64] I'm not a real developer
[603.64 → 606.52] until I get firmly in the world of Vim
[606.52 → 607.60] and leave TextMate behind.
[607.60 → 611.56] But I think I've discovered you via all your TM bundles.
[611.70 → 613.30] So is TextMate still your primary editor?
[613.44 → 613.70] Oh, yeah.
[614.88 → 616.14] Look, okay, okay.
[616.24 → 618.30] So do I have an issue with people
[618.30 → 620.58] going back to 1960s technology?
[620.76 → 622.48] I don't actually know when Vim and Emacs came out.
[622.54 → 624.10] But I mean, Emacs is ancient, isn't it?
[624.54 → 628.28] When Emacs is the canonical base of GNU,
[628.40 → 630.44] I mean, that was Stallman's big project.
[631.52 → 632.76] But, you know, do I have an issue
[632.76 → 634.94] with people picking up legacy technologies?
[635.16 → 636.16] I mean, yeah, I do.
[636.16 → 637.42] I have a big issue with it.
[637.74 → 641.58] Do I poo-poo them publicly on public podcast radio?
[642.92 → 643.94] I guess I just did.
[645.94 → 648.50] Well, Vim is 95, to defend it a little bit,
[648.54 → 649.20] if I remember correctly.
[649.22 → 649.24] That's right.
[649.24 → 650.92] Let's all go and get record players
[650.92 → 653.40] and Windows 95 and live the good life.
[654.22 → 655.54] Hey, Windows 95 is cool.
[655.68 → 658.26] You could, you know, put the Simpsons theme
[658.26 → 659.90] all over your machine.
[660.26 → 663.16] Anyway, but what's more important
[663.16 → 665.12] is that these people are aggressively
[665.12 → 666.18] trying to pick tools
[666.18 → 669.20] and chop and change their tool set
[669.20 → 670.64] that they use as developers.
[671.22 → 672.88] And if they think they're not getting the right,
[673.64 → 675.54] you know if they don't feel enabled by TextMate,
[675.62 → 677.30] but they do feel enabled by Vim or Emacs,
[677.36 → 678.30] that's great, really,
[678.44 → 680.60] because that is, you know,
[680.62 → 682.82] if you're going to do this profession for 40 years
[682.82 → 685.12] and truly get the most out of it,
[685.14 → 686.36] you've got to constantly keep chopping
[686.36 → 687.36] and changing a tool set
[687.36 → 690.46] and find out what set of tools, languages, libraries,
[691.18 → 693.74] you know, and teammates that you want to work with.
[694.08 → 695.74] So best of luck to them.
[696.46 → 696.70] Totally.
[696.90 → 698.72] I spend a lot of time SSH into servers,
[698.86 → 700.64] and so having one editor in most places
[700.64 → 701.96] is the main reason that I use Vim.
[702.04 → 704.44] But I just installed Janus yesterday, actually,
[704.86 → 706.68] and a friend looked over my shoulder and said,
[706.80 → 709.10] oh, so now your Vim is TextMate, basically.
[709.84 → 711.10] And I thought that was fascinating.
[711.10 → 713.86] And I have used TextMate in the past.
[713.98 → 715.42] It's just, you know, I'm more used to Vim.
[715.76 → 718.28] So these wars will forever happen
[718.28 → 719.58] when the program is arguing about tools.
[719.68 → 721.76] I'm really excited about Redcap as well.
[722.94 → 726.90] I know that Engine Yard used to be involved with Ruby,
[726.98 → 729.06] but then that is not really happening anymore,
[729.20 → 730.66] and I know that's sort of the segue.
[731.02 → 732.62] No, we are still very involved with Ruby.
[732.74 → 735.08] I apologize if we haven't communicated
[735.08 → 737.00] their involvement well enough.
[737.00 → 739.56] No, when the three guys,
[739.56 → 743.08] Charlie, Tom, and Nick left Oracle.
[743.42 → 744.22] They came to Engine Yard,
[744.26 → 747.18] and we started ensuring that that work carried on,
[747.40 → 751.30] and we have that as an alpha product at the moment
[751.30 → 752.12] for people to try.
[753.76 → 754.96] But no, the world needs, I mean,
[755.18 → 756.94] Engine Yard needs more people using Ruby.
[757.08 → 758.28] That's our belief.
[758.74 → 760.16] Ruby is a wonderful language.
[760.64 → 762.54] Yeah, I mean, we're not anti-poly gut,
[762.62 → 763.74] but I mean, as a base language
[763.74 → 765.96] for building web-scale applications,
[766.22 → 768.06] which, you know, it's the same for mobile, right?
[768.06 → 769.20] If you're building mobile apps,
[769.68 → 772.58] every app these days needs some sort of central back end,
[772.94 → 776.40] and we believe Ruby is still the best language
[776.40 → 778.18] and has the best frameworks for doing that.
[778.72 → 781.36] So Ruby helps spread that message,
[781.74 → 785.14] and it's also, it's possibly, you know,
[785.18 → 788.48] the best VM in and of itself.
[788.60 → 790.04] I mean, I can say that today,
[790.10 → 791.14] and it might change tomorrow,
[791.14 → 791.92] but, I mean, it is,
[792.42 → 795.20] Ruby on top of the JVM is a tremendous product.
[795.20 → 795.68] Totally.
[796.88 → 799.02] The segue to that, I guess, was Red Car,
[799.20 → 800.54] so have you tried it?
[800.94 → 801.26] I have.
[801.26 → 802.30] I don't think I've tried it.
[802.82 → 804.58] It's actually very aggressively being developed.
[804.70 → 806.60] I think I played with it a few months ago.
[807.74 → 810.26] At the time, I wasn't quite ready to give up TextMate itself,
[810.34 → 812.18] but I definitely understand what they're trying to achieve.
[813.52 → 815.42] It seems like it changes quite often.
[815.72 → 816.20] Yeah, like you said,
[816.22 → 817.82] it's definitely aggressively being developed.
[817.94 → 818.98] I had a friend give a presentation
[818.98 → 821.12] on my local Ruby Brigade about it,
[821.12 → 823.24] and the commands he had looked up the week before
[823.24 → 825.12] didn't work while he was giving his presentation
[825.12 → 826.12] because they changed the API.
[826.52 → 828.66] Yeah, that's awkward for demoing.
[829.84 → 833.12] And, again, if it means that, like Emacs,
[833.28 → 835.44] it's built in a language that you can hack
[835.44 → 836.30] and you can modify,
[836.62 → 839.00] that's very empowering for a lot of developers.
[839.32 → 841.58] So, you know, especially what we've lived
[841.58 → 843.50] in the dark ages of TextMate,
[843.58 → 845.48] which is, I think, why many people leave TextMate.
[845.56 → 847.48] It's not because there's anything necessarily wrong with it.
[847.48 → 851.78] But they are just fed up with lack of, you know,
[851.96 → 854.96] activity from the public eye.
[856.42 → 859.48] But Redcap being written in a language that,
[859.74 → 860.92] even if you're not a Ruby developer,
[861.12 → 862.84] I mean, just knowing that it's written in a language
[862.84 → 865.60] that you could learn and that you could modify
[865.60 → 868.88] and you can contribute to in the editor itself,
[869.00 → 870.28] obviously it has bundles as well,
[870.34 → 872.54] like TextMate and all the other editors,
[873.18 → 875.30] I think is going to empower it greatly.
[875.30 → 877.56] So I look forward to them getting to a stage
[877.56 → 879.38] where the world starts to realize
[879.38 → 881.94] it is a wonderful editor and gets a lot of traction.
[882.98 → 884.94] Well, you also do Objective-C development, right?
[885.66 → 886.34] I dabbled.
[886.58 → 887.30] I was a dabbler.
[887.92 → 890.42] I mean, I recall Apple.
[890.82 → 891.54] Is there a difference?
[891.62 → 891.76] No.
[892.10 → 896.30] So when the iPhone SDK came out,
[896.38 → 899.00] I just happened to be playing with Ruby Coco.
[899.22 → 900.24] This was 2007.
[901.08 → 901.84] Ruby Coco.
[901.84 → 905.14] And so I was very desperate to figure out,
[905.18 → 907.02] could I get Ruby running on the iPhone?
[907.28 → 908.86] Unfortunately, I just wasn't clever enough
[908.86 → 909.78] to solve that problem.
[910.30 → 911.44] I'm just not a C person.
[911.60 → 912.84] I'm just...
[913.50 → 914.58] Have you ever...
[914.58 → 916.56] 2007, I got a linking error.
[916.94 → 918.98] I didn't realize people still had linking errors.
[919.56 → 920.10] That was weird.
[920.18 → 920.82] I felt like...
[920.82 → 923.68] I know Objective-C is this beautiful syntax
[923.68 → 925.66] relative to the underlying language,
[925.66 → 929.82] but I wasn't ready for a linking error emotionally.
[930.22 → 933.68] But no, I did some Objective-C back in 2005 and 2007
[933.68 → 935.88] and made a bunch of Ruby test libraries
[935.88 → 939.34] to sort of make it easier to test your Objective-C.
[940.20 → 941.94] And my consultancy at the time
[941.94 → 943.98] did a bunch of iPhone work.
[944.40 → 948.18] But I was pretty annoyed by Apple's anti-open source,
[948.62 → 950.60] you know, approach at the time
[950.60 → 951.98] because it had that NDA in place.
[952.48 → 954.20] And so a bunch of Objective-C people
[954.20 → 955.22] just wouldn't talk to each other.
[955.84 → 957.28] iPhone developers wouldn't talk to each other
[957.28 → 958.34] because they're all scared of Apple.
[959.26 → 962.64] What did Objective-C cause you to appreciate about Ruby?
[965.40 → 967.06] That was an excellent question.
[967.20 → 968.28] And I say it's an excellent question
[968.28 → 969.34] because I don't know what the answer is.
[971.84 → 972.12] It's...
[972.12 → 974.26] Well, it's such a lot of things in Ruby,
[974.38 → 976.38] you know, just like string concatenation, right?
[976.46 → 978.10] Look, I'm very excited about Mac Ruby.
[978.36 → 981.00] I mean, Mac Ruby is sort of blending the two things together.
[981.54 → 983.52] And I believe it's going to become...
[983.52 → 985.60] I mean, I have heard whispers and ideas
[985.60 → 988.24] that it may become a first-class language in line.
[989.00 → 991.10] And that'll be very exciting for anyone
[991.10 → 993.82] that wants to do, you know,
[993.88 → 996.14] sort of application development for the Mac
[996.14 → 999.24] without having to go down to the Objective-C level.
[1000.12 → 1001.34] And it looks very similar.
[1001.50 → 1003.50] I mean, I think I even created a TextMate bundle
[1003.50 → 1004.58] for Mac Ruby
[1004.58 → 1006.32] so that you could copy documentation in
[1006.32 → 1008.10] and generate Mac Ruby syntax.
[1008.10 → 1009.10] But...
[1009.10 → 1011.76] So I...
[1011.76 → 1012.88] What did I learn?
[1013.82 → 1016.94] I learned appreciation for all the things
[1016.94 → 1018.44] that I no longer have to think about.
[1019.06 → 1019.94] Managing memory.
[1021.72 → 1022.04] Exactly.
[1022.56 → 1023.94] Just remember, what did I do with that object?
[1024.00 → 1025.80] I had an object lying around here somewhere.
[1025.98 → 1026.94] What did I do with it?
[1027.02 → 1027.90] I don't know if you remember that.
[1027.90 → 1030.14] I was very excited to see Engine Yard
[1030.14 → 1032.72] team up with Accelerator for mobile apps.
[1032.78 → 1034.18] So I guess you guys are providing plumbing
[1034.18 → 1036.54] for back-end API type steps for...
[1036.54 → 1038.02] Again, really, what's the...
[1038.02 → 1039.98] There aren't many iPhones,
[1040.14 → 1041.12] sort of mobile apps
[1041.12 → 1042.86] that have a significant purpose in the world
[1042.86 → 1043.98] if they're not going to have a back-end.
[1044.50 → 1045.90] And making it easy for people...
[1046.56 → 1048.72] Rails makes it easy to build that middleware layer
[1048.72 → 1050.92] or Rails or Ruby and Rack
[1050.92 → 1051.70] make it easy.
[1051.70 → 1053.84] Maybe getting it up and running
[1053.84 → 1055.36] in a production environment.
[1055.86 → 1057.82] I mean, if your app's going to take off,
[1057.96 → 1059.72] then you need to make sure your back-end scales.
[1060.72 → 1063.26] So we worry that people are making
[1063.26 → 1065.72] some awesome apps, you know, mobile apps,
[1065.90 → 1068.04] but don't have the expertise to ensure
[1068.04 → 1069.60] that their app doesn't look ridiculous
[1069.60 → 1070.74] because their back-end failed.
[1071.14 → 1073.78] So it's pretty important that those guys
[1073.78 → 1074.94] get the support they need.
[1075.10 → 1076.42] So yes, we're very cool,
[1076.52 → 1077.68] very excited that Accelerator...
[1077.68 → 1078.84] They're doing some very cool stuff.
[1078.84 → 1082.62] So Rails Installer,
[1082.86 → 1085.00] I've been spending a lot of quality time
[1085.00 → 1086.70] with the Ruby Installer project lately,
[1087.06 → 1088.26] and it's been great.
[1088.84 → 1090.72] Luis took a couple of hours on a Saturday
[1090.72 → 1093.02] to help me with some things involved with it,
[1093.06 → 1093.88] and it's been a great project.
[1094.08 → 1096.42] And so I'm excited to see Rails Installer
[1096.42 → 1097.84] bringing the same kind of thing.
[1098.46 → 1100.16] One of the things I saw him say
[1100.16 → 1101.68] was that he's sick of people saying
[1101.68 → 1102.94] that the answer to Ruby on Windows
[1102.94 → 1104.36] is installed Ubuntu in a VM.
[1104.92 → 1106.36] And so it'd be great to have Rails
[1106.36 → 1108.20] actually be a first-class citizen on Windows,
[1108.20 → 1109.42] as much as I hate Windows.
[1109.94 → 1111.06] There are people that love it,
[1111.22 → 1112.50] and so getting Rails to them
[1112.50 → 1114.02] is a good thing overall.
[1114.38 → 1117.28] So I guess congrats on that project.
[1117.86 → 1119.52] It's a really important project.
[1119.90 → 1121.98] I mean, people just need to...
[1121.98 → 1123.14] I'll tell you a funny story.
[1123.42 → 1124.00] It's a funny story.
[1124.22 → 1126.50] If you go to the Rails 3 guide,
[1126.72 → 1129.16] which I think is at guides.rubionrails.org,
[1129.24 → 1131.44] and you go to how to get started on Windows,
[1132.06 → 1133.44] the answer to that problem
[1133.44 → 1135.40] was a project called Instant Rails.
[1136.28 → 1138.64] And Instant Rails was how I got started in Rails
[1138.64 → 1139.64] back in 2005.
[1140.24 → 1143.18] Unfortunately, it hadn't been maintained since 2007.
[1143.90 → 1145.58] It was distributing a version of Ruby
[1145.58 → 1147.40] that didn't work with Rails 3.
[1147.96 → 1151.44] And so what you had was people being told
[1151.44 → 1152.40] that if you're on Windows,
[1152.74 → 1154.42] to go and install a set of software
[1154.42 → 1156.86] that didn't work with Rails 3.
[1157.94 → 1160.26] So it was pretty much low-hanging fruit, really,
[1160.42 → 1162.00] for a project that needed doing.
[1162.00 → 1165.06] Really, really important.
[1165.64 → 1167.84] And so now if you go to the Instant Rails project,
[1167.96 → 1170.40] it now says, you know, please use Rails installer.
[1170.82 → 1173.30] But all we did was we packaged it up like a gift bag
[1173.30 → 1175.80] of things that we think make your life
[1175.80 → 1180.84] as a Rails Ruby developer functioning and pleasant.
[1181.02 → 1183.80] So it's not just the fact that it bundles Ruby installer.
[1184.18 → 1186.10] It's that it includes Git.
[1186.78 → 1188.74] It's that it attempts to set up, you know,
[1188.74 → 1190.86] future version are going to set up your SSH keys
[1190.86 → 1192.62] and your Git config.
[1192.92 → 1193.68] And just, you know,
[1194.30 → 1196.64] get you not just ready to be a Rails developer.
[1197.22 → 1200.44] So it's going to, like it includes my SQLite.
[1200.56 → 1202.86] Not just SQLite Jam, but also SQLite itself.
[1203.32 → 1205.30] So, you know, you're just ready.
[1205.98 → 1208.16] You don't have to go and look any further.
[1208.58 → 1210.62] But it also, once you take that next step
[1210.62 → 1212.36] and you want to start getting other gems
[1212.36 → 1214.60] or get source, participate in the GitHub,
[1214.82 → 1215.88] you know, centric community,
[1215.88 → 1217.20] you're ready to rock and roll
[1217.20 → 1219.84] because we just want to lower the barriers
[1219.84 → 1220.90] to people participating.
[1221.86 → 1222.76] Yeah, that's awesome.
[1222.94 → 1225.72] I actually wish that I had remembered that
[1225.72 → 1226.94] over the last couple of days.
[1227.32 → 1228.52] So we're actually,
[1228.72 → 1230.84] the shoes project is built with Ruby installer.
[1231.10 → 1232.96] And so I'm essentially doing the same kind of deal.
[1233.04 → 1235.06] All these extra recipes on top of Ruby installer.
[1235.34 → 1237.40] And so a lot of those same things are there.
[1237.56 → 1239.06] Git, SQLite, all those things.
[1239.20 → 1240.30] So I probably could have gotten some help
[1240.30 → 1241.14] from looking at your code.
[1241.14 → 1244.72] I mean, Luis is, I mean-
[1244.72 → 1245.22] He's fantastic.
[1245.50 → 1246.62] Nothing bad ever happens to Luis.
[1246.94 → 1247.92] He is a machine.
[1248.46 → 1250.84] Similar to, I remember I accused Charlie Nutter once
[1250.84 → 1252.04] of there being three of him
[1252.04 → 1254.12] because he seemed to be available and online
[1254.12 → 1255.30] helping 24 hours a day.
[1255.38 → 1258.74] And I think Luis is just a phenomenal human being
[1258.74 → 1261.06] for the effort he puts in
[1261.06 → 1266.66] and his knowledge about the Ruby ecosystem of software.
[1266.98 → 1268.10] And if there's a bug,
[1268.10 → 1271.10] he kind of knows where that bug is most likely to exist.
[1271.64 → 1273.06] The fact that he's now on Ruby call
[1273.06 → 1274.10] to be able to look after Windows
[1274.10 → 1276.38] is very enabling and wonderful.
[1277.68 → 1278.22] No, so it was,
[1278.96 → 1280.14] he was our jungle guide
[1280.14 → 1282.04] when we were building the Rails installer.
[1282.76 → 1284.00] Yeah, I talked to him once
[1284.00 → 1285.84] and then he spent six hours on a Saturday
[1285.84 → 1289.34] helping me find an obscure bug in Ruby
[1289.34 → 1290.04] and then said,
[1290.14 → 1291.30] oh, I'm sorry, I need to go now.
[1291.38 → 1293.54] My fiancé is going to be mad at me or something.
[1293.78 → 1295.22] So he's just, he's totally,
[1295.40 → 1296.24] he's a machine, it's great.
[1296.46 → 1297.96] Yeah, we need to have some words with his fiancé.
[1298.52 → 1300.12] I hope she understands how,
[1300.72 → 1301.12] what he does,
[1301.18 → 1302.16] how valued and appreciated.
[1302.38 → 1303.78] We're hoping that he's going to be coming up
[1303.78 → 1304.82] to Hailstone.
[1306.24 → 1307.66] So if you have no other reason
[1307.66 → 1309.28] for Ruby Develops to come to Hailstone,
[1309.38 → 1310.36] it's just to come and see Luis
[1310.36 → 1312.80] and at least to thank him for what he does.
[1313.48 → 1314.38] Speaking of conferences,
[1314.64 → 1316.10] you are speaking at Comecon, right?
[1316.32 → 1317.00] Oh, I am.
[1317.64 → 1318.78] And that's going to be exciting.
[1318.98 → 1320.36] I even know what I'm going to talk about now.
[1320.36 → 1324.42] I could be accused of many things
[1324.42 → 1327.82] and definitely one of them is to pick my topic of a talk,
[1328.08 → 1329.94] you know, as late as possible,
[1330.38 → 1332.32] where the conference organizers get really cranky
[1332.32 → 1332.50] and say,
[1332.58 → 1334.22] Nicholas, we need,
[1334.30 → 1334.98] they never say Nicholas,
[1335.10 → 1335.58] that's my mother.
[1335.94 → 1336.16] They'll say,
[1336.24 → 1337.34] Dr. Nick, we need,
[1337.84 → 1339.08] and my mother doesn't run conferences,
[1339.26 → 1339.80] so it's Dr. Nick.
[1339.88 → 1340.24] Dr. Nick,
[1340.30 → 1342.18] we need to know what you're talking about.
[1342.18 → 1344.60] But in this case,
[1344.68 → 1345.98] I actually went over to GitHub yesterday
[1345.98 → 1346.72] and Chris and I
[1346.72 → 1348.98] nodded out a talk idea
[1348.98 → 1350.46] and that's going to be around the tool set,
[1350.60 → 1352.08] a theme that we sort of,
[1352.12 → 1352.30] you know,
[1352.32 → 1353.80] talked about here earlier on the podcast.
[1354.76 → 1356.52] Just the importance of constantly evolving
[1356.52 → 1357.38] and picking your tools
[1357.38 → 1358.94] and building your own,
[1359.12 → 1360.32] looking at what other people are using,
[1360.86 → 1362.18] why it is okay to use Vim,
[1362.24 → 1363.70] even though I personally dislike it.
[1364.28 → 1364.68] I mean,
[1364.68 → 1367.40] if you have to put the shortcuts on a coffee mug,
[1367.86 → 1370.16] I don't know,
[1370.20 → 1370.82] I just think that's,
[1370.82 → 1372.54] there's something for us to learn from that.
[1374.34 → 1374.70] Yeah,
[1374.82 → 1376.40] I'm excited for Comecon
[1376.40 → 1378.48] and one of the interesting things about it,
[1378.54 → 1378.98] I noticed,
[1379.10 → 1379.54] it's great.
[1380.84 → 1381.42] It seems like,
[1381.48 → 1381.88] someone said,
[1381.96 → 1383.80] it seems like every Ruby conference
[1383.80 → 1385.32] has to have some sort of controversy
[1385.32 → 1386.12] and so,
[1386.80 → 1387.08] the Ruby,
[1387.30 → 1388.94] or Comecon is going to have like
[1388.94 → 1389.66] 40,
[1389.82 → 1390.06] 30,
[1390.16 → 1391.38] 40% women speaking
[1391.38 → 1393.84] and not to broach the whole,
[1393.92 → 1394.12] you know,
[1394.12 → 1394.92] women CS,
[1395.06 → 1395.62] oh my God,
[1395.82 → 1396.12] topic,
[1396.30 → 1398.02] but I think that's going to be really exciting
[1398.02 → 1399.76] and it looks like we've got a great lineup,
[1399.98 → 1400.14] so,
[1400.46 → 1400.76] you know,
[1400.82 → 1401.90] I'm excited to go to it
[1401.90 → 1402.76] and see everyone else.
[1402.76 → 1403.92] I don't think it's a pure Ruby conference,
[1404.04 → 1405.64] I think people are talking about
[1405.64 → 1406.42] other languages,
[1406.58 → 1407.04] other stuff,
[1407.20 → 1407.28] and,
[1407.28 → 1408.32] there's lots of JavaScript,
[1408.88 → 1409.28] uh,
[1409.42 → 1411.08] Josh Eschenankis,
[1411.20 → 1412.44] or however you say his last name,
[1412.64 → 1412.88] uh,
[1412.88 → 1414.30] Ash kenos,
[1414.38 → 1414.76] that's right.
[1414.92 → 1415.94] I've butchered it more than anybody.
[1416.08 → 1416.62] I remember,
[1416.90 → 1417.76] you guys talked to him,
[1417.80 → 1418.60] you had a conversation about this.
[1418.60 → 1420.38] I believe your show has talked about his projects
[1420.38 → 1421.22] more than anyone else,
[1421.22 → 1423.94] so if anyone's going to get his name pronunciation correct,
[1424.16 → 1425.04] it would be you guys.
[1426.46 → 1426.70] Uh,
[1426.82 → 1427.04] yeah.
[1427.04 → 1427.98] He's done some wonderful stuff,
[1427.98 → 1428.20] I mean,
[1428.26 → 1428.32] the
[1428.32 → 1428.50] the
[1428.50 → 1429.36] the document cloud,
[1429.74 → 1431.28] he works over at the document cloud.
[1431.90 → 1432.30] Right.
[1432.44 → 1432.68] Yeah.
[1432.68 → 1432.90] I mean,
[1432.90 → 1435.52] they've done some awesome projects that have come out of there,
[1435.52 → 1435.90] um,
[1435.90 → 1437.60] before and after coffee script.
[1437.76 → 1438.56] It was great.
[1438.84 → 1439.18] Uh,
[1439.18 → 1439.76] I'm really,
[1439.92 → 1440.24] really,
[1440.24 → 1440.86] uh,
[1440.86 → 1441.60] happy with it,
[1441.60 → 1444.72] even though I wrote a blog post that said I sort of wasn't almost,
[1444.72 → 1445.18] um,
[1445.18 → 1445.64] it's great.
[1445.74 → 1446.48] It's been fantastic.
[1446.60 → 1447.62] I've been using it for every project.
[1447.84 → 1448.12] The
[1448.12 → 1448.40] uh,
[1448.40 → 1449.82] the cloud crowd project,
[1450.18 → 1450.54] um,
[1450.56 → 1451.72] the underscore one.
[1452.02 → 1453.04] So there are a bunch of stuff.
[1453.04 → 1454.12] Coffee script is my favourite.
[1454.18 → 1454.26] Oh,
[1454.28 → 1454.64] absolutely.
[1454.78 → 1455.48] It goes with that.
[1455.56 → 1455.72] I mean,
[1455.74 → 1456.20] it just,
[1456.44 → 1456.72] you know,
[1456.76 → 1457.32] it'd be,
[1457.80 → 1458.96] it's a brilliant invention.
[1459.30 → 1459.58] Um,
[1459.90 → 1461.20] very glad makes me.
[1461.30 → 1463.62] So if you just now picked your topic for code cone,
[1463.64 → 1465.38] I guess you don't have a clue what you're going to talk about at,
[1465.38 → 1465.62] uh,
[1465.62 → 1466.02] red dirt,
[1466.22 → 1466.68] uh,
[1466.68 → 1467.04] red dirt,
[1467.10 → 1467.18] I,
[1467.32 → 1468.02] the red dirt,
[1468.10 → 1468.38] uh,
[1468.38 → 1469.44] Ruby nation and,
[1469.44 → 1469.94] uh,
[1470.06 → 1470.52] rails cone.
[1470.62 → 1471.30] I'm going to go with the
[1471.30 → 1472.28] the rails' installer theme.
[1472.34 → 1473.30] I've never really gone with,
[1473.36 → 1475.40] with giving the same talk at multiple conferences,
[1475.40 → 1476.32] but unfortunately,
[1476.40 → 1476.92] I say,
[1476.98 → 1477.32] unfortunately,
[1477.50 → 1478.22] this would be awesome.
[1478.30 → 1479.26] I get to get better at it,
[1479.26 → 1481.30] but this message about rails installer,
[1481.44 → 1481.94] which is,
[1482.00 → 1482.74] um,
[1483.26 → 1486.92] getting the rails developers to get back out and,
[1486.92 → 1487.44] you know,
[1487.44 → 1488.50] sharing rails again.
[1488.78 → 1489.26] That's,
[1489.32 → 1489.50] I mean,
[1489.52 → 1491.74] rails installer is obviously a tool for new people,
[1491.74 → 1497.34] but it's also a tool for current rails developers to be able to share rails with confidence,
[1497.34 → 1500.20] which is why we're building an OS X and probably a Linux one.
[1500.72 → 1501.00] Um,
[1501.30 → 1503.26] so that you can point to it,
[1503.32 → 1505.14] this one URL and say,
[1505.22 → 1505.80] this is,
[1505.94 → 1506.74] and say with confidence,
[1506.74 → 1507.90] this is the place you go to,
[1507.94 → 1509.98] to get started in rails and have a heavy experience.
[1510.86 → 1511.22] Um,
[1511.32 → 1511.52] I mean,
[1511.56 → 1513.58] that's one of the reasons Google took off was,
[1513.74 → 1514.44] you know,
[1514.46 → 1517.76] you could share the Google address with someone and have confidence that people,
[1517.90 → 1518.28] your friend,
[1518.36 → 1518.68] your mother,
[1518.84 → 1519.04] your,
[1519.20 → 1519.50] you know,
[1519.94 → 1521.84] siblings were going to have a positive experience,
[1521.84 → 1522.60] um,
[1522.64 → 1523.40] searching the internet.
[1523.76 → 1524.10] Uh,
[1524.10 → 1524.40] so we,
[1524.48 → 1526.86] we want rails installer to have that same,
[1526.86 → 1527.46] um,
[1527.46 → 1527.86] message.
[1528.66 → 1531.18] When you talk about going to multiple conferences to speak,
[1531.18 → 1532.94] to get that message out there,
[1532.94 → 1536.52] it's actually drawing back to one of the things that sort of problem with rails.
[1536.52 → 1541.06] And I wonder if you know how this is going to be fixed in the future is that we sort of have developed a culture of,
[1541.48 → 1543.50] so if you just read these like 15 blogs,
[1543.50 → 1547.50] you'll get all the documentation and all the knowledge about what's going on and what you should be using.
[1547.50 → 1550.04] And I've had problems in the past with people Googling answers.
[1550.04 → 1553.10] And since Google's page rank accumulates links over time,
[1553.18 → 1553.32] you know,
[1553.34 → 1554.06] you'll get answers from,
[1554.20 → 1554.30] Oh,
[1554.34 → 1557.42] there are some 2006 articles that you just must read.
[1557.76 → 1557.98] Yeah,
[1558.06 → 1558.56] exactly.
[1558.78 → 1560.90] So how is rails going to overcome that in the future?
[1561.06 → 1561.40] That is,
[1561.52 → 1561.76] uh,
[1561.76 → 1562.20] and,
[1562.20 → 1562.26] and,
[1562.26 → 1567.78] and that is certainly one in the mission statement of rails installer from the website perspective is a term to bring that together.
[1568.38 → 1568.78] Um,
[1568.86 → 1569.12] you know,
[1569.12 → 1570.74] the getting started information.
[1570.74 → 1571.54] Um,
[1571.54 → 1571.82] but I mean,
[1571.84 → 1572.82] that's not to take away from,
[1572.96 → 1573.56] from some of the
[1573.56 → 1573.82] the
[1573.82 → 1574.18] um,
[1574.48 → 1575.76] the textbooks that have been written,
[1575.76 → 1577.90] like the rails three-way and,
[1577.90 → 1578.18] uh,
[1578.56 → 1579.06] um,
[1579.62 → 1579.84] uh,
[1579.84 → 1580.82] the one Ryan big and,
[1580.82 → 1581.56] and you who wrote,
[1581.56 → 1582.12] um,
[1582.12 → 1582.40] you know,
[1582.40 → 1582.54] I mean,
[1582.56 → 1584.98] that people are putting a lot of effort into those and,
[1584.98 → 1585.02] and,
[1585.02 → 1585.20] and,
[1585.20 → 1585.40] you know,
[1585.40 → 1587.20] paying 30 bucks for books to get the
[1587.36 → 1587.52] you know,
[1587.56 → 1589.40] rock solid getting started experience,
[1589.40 → 1591.22] a bunch of people are doing training.
[1591.34 → 1591.44] I mean,
[1591.46 → 1594.26] engineer university exists on top of other people doing,
[1594.26 → 1594.72] you know,
[1594.72 → 1594.94] the
[1594.94 → 1595.86] the rails train,
[1596.06 → 1596.60] uh,
[1596.60 → 1596.98] training,
[1597.14 → 1597.26] uh,
[1598.26 → 1599.18] podcasts and,
[1599.18 → 1599.78] and peep code,
[1599.88 → 1600.18] et cetera.
[1600.74 → 1601.22] Um,
[1601.46 → 1602.36] a bunch of different,
[1602.40 → 1602.64] you know,
[1602.64 → 1603.62] getting started experiences.
[1604.42 → 1604.80] Um,
[1604.82 → 1607.26] so I do want to make,
[1607.48 → 1607.58] yeah,
[1607.58 → 1609.00] that is definitely in the mission statement though,
[1609.00 → 1612.66] to bring that all together so that people can get started.
[1612.82 → 1615.12] We may even put it into the bundle it in ourselves.
[1615.28 → 1615.76] So that's,
[1615.84 → 1616.12] you know,
[1616.12 → 1616.96] everything's work.
[1617.62 → 1622.18] You don't have too many good ideas versus a capacity to execute.
[1622.18 → 1622.46] So,
[1622.98 → 1623.40] um,
[1623.60 → 1623.94] but no,
[1624.20 → 1626.66] the lots of people making that much easier.
[1627.22 → 1627.66] Um,
[1627.72 → 1630.08] but if we can stop people going to Google for answers,
[1630.08 → 1632.06] the
[1632.10 → 1632.52] the longer,
[1632.62 → 1632.90] the better.
[1633.80 → 1635.26] And if we can keep people on Windows,
[1635.34 → 1635.60] the longer,
[1635.70 → 1635.98] the better.
[1637.46 → 1645.24] I don't want people to think that they need to go and buy a Mac because then they stop being experts on Windows and the community dies.
[1646.92 → 1647.88] Question from Twitter.
[1647.88 → 1651.28] Casey Carroll wants to know your thoughts on the Jenkins Hudson drama.
[1652.78 → 1653.10] The
[1653.46 → 1653.88] well,
[1653.92 → 1654.80] I think it's look at,
[1654.80 → 1656.68] I think it's a wonderful lesson to,
[1656.68 → 1657.00] to,
[1657.00 → 1657.32] to,
[1657.36 → 1657.46] uh,
[1657.46 → 1658.80] to businesses involved in,
[1658.84 → 1659.16] in,
[1659.20 → 1659.34] uh,
[1659.34 → 1660.08] open source that,
[1660.26 → 1661.00] that they,
[1661.12 → 1663.28] they very likely don't get it.
[1663.28 → 1664.10] I mean,
[1664.14 → 1666.52] so engineer has an experience with open source.
[1667.08 → 1667.48] Um,
[1667.48 → 1671.64] we currently don't really lay any claims over trademarks or IP on,
[1671.64 → 1671.96] on,
[1671.96 → 1672.16] uh,
[1672.16 → 1675.64] Ruinous or J Ruby or fog or any of the projects that we've gone to full-time,
[1675.64 → 1676.38] uh,
[1676.38 → 1677.96] which included rails too recently.
[1678.68 → 1679.04] Um,
[1679.40 → 1679.64] you know,
[1679.64 → 1679.82] we,
[1679.84 → 1681.50] we contribute to them because they're part of our,
[1681.54 → 1683.58] our product or a part of the community that,
[1683.66 → 1684.94] that uses those things.
[1685.50 → 1685.86] Oracle,
[1686.20 → 1686.76] you know,
[1686.76 → 1688.22] bought this huge company called sun,
[1688.30 → 1689.66] which was the largest owner of,
[1689.76 → 1691.08] of open source,
[1691.08 → 1692.52] I think in the owner,
[1692.64 → 1693.08] so to speak,
[1693.16 → 1694.98] the largest orchestrator of open source.
[1695.76 → 1696.20] And,
[1696.32 → 1697.28] you know,
[1697.28 → 1698.88] they're having some teething problems,
[1699.00 → 1701.06] figuring out what do they do with those assets?
[1701.66 → 1702.06] Um,
[1702.12 → 1702.74] and they've,
[1702.98 → 1704.02] sorry,
[1704.96 → 1706.78] they're coming for you.
[1707.78 → 1709.34] We'll just have pause.
[1709.88 → 1711.06] It's the Oracle police.
[1715.18 → 1721.06] I had someone that says Oracle's new open source strategy is to find every single developer and just kick them in the balls.
[1721.08 → 1723.68] And that's their new like initiative going forward to,
[1723.68 → 1724.00] you know,
[1724.00 → 1725.14] reach out to the community.
[1725.30 → 1725.46] Yeah.
[1725.46 → 1725.92] Perhaps they'll,
[1725.98 → 1727.44] perhaps they'll have little booths at,
[1727.44 → 1727.74] at,
[1727.74 → 1728.10] um,
[1728.10 → 1729.50] at shopping centres where you can,
[1729.66 → 1730.12] as a developer,
[1730.24 → 1731.12] come and have your balls kicked.
[1732.70 → 1734.96] I had an idea for Netflix completely off the topic.
[1735.00 → 1736.12] I went and saw a Netflix talk,
[1736.12 → 1736.64] uh,
[1736.64 → 1737.54] and we'll get back to Jenkins.
[1737.90 → 1738.10] Um,
[1738.10 → 1738.32] yeah,
[1738.40 → 1739.42] I went to a talk on,
[1739.42 → 1739.60] uh,
[1739.60 → 1741.34] no SQL at Netflix the other night down.
[1741.34 → 1741.54] And,
[1741.62 → 1741.88] um,
[1742.00 → 1743.30] it was actually the Facebook office.
[1743.30 → 1743.54] Uh,
[1743.54 → 1743.92] it was the
[1743.92 → 1744.14] uh,
[1744.14 → 1745.00] what is it?
[1745.00 → 1746.24] The Bay Area cloud computing,
[1746.32 → 1747.94] one of the multitude of cloud computing things,
[1748.02 → 1748.52] uh,
[1748.52 → 1748.84] meetups.
[1748.84 → 1749.36] And,
[1749.36 → 1749.66] um,
[1749.82 → 1750.26] and I just,
[1750.40 → 1750.70] I was,
[1750.80 → 1752.36] I had this cool idea of Netflix,
[1752.46 → 1753.28] wherever they go and talk,
[1753.34 → 1755.52] they should have these like cardboard post box,
[1756.04 → 1756.24] you know,
[1756.24 → 1757.30] like a blue or red,
[1757.30 → 1757.78] uh,
[1757.78 → 1760.28] mailbox that they could put at the front of the room.
[1760.36 → 1763.04] And people just know that if you're going to see a Netflix talk,
[1763.10 → 1766.74] you can take your Netflix DVDs with you and drop them off there because,
[1766.74 → 1767.42] you know,
[1767.52 → 1769.18] who's got time to go to the post these days.
[1769.54 → 1771.12] And I thought that would be a cool idea.
[1771.12 → 1773.08] I saw a really ridiculous thing,
[1773.14 → 1775.32] thing about the Facebook login controversy with people,
[1775.42 → 1775.66] again,
[1775.68 → 1777.56] using Google inappropriately where,
[1777.68 → 1777.86] uh,
[1777.86 → 1781.34] I guess red box has received a number of complaints of people thinking that
[1781.34 → 1784.52] they're Amazon just because they're both red and they both DVDs.
[1787.02 → 1787.46] Or,
[1787.62 → 1788.82] or maybe it was the other way around.
[1788.88 → 1789.84] Maybe it was Amazon or,
[1789.84 → 1790.12] uh,
[1790.66 → 1791.10] the
[1791.24 → 1794.02] the people trying to return their red box things in their,
[1794.02 → 1794.34] uh,
[1794.34 → 1795.28] Netflix papers.
[1795.28 → 1796.54] But I thought that was like,
[1796.80 → 1798.50] it's something we have to overcome as developers,
[1798.50 → 1798.92] you know,
[1798.92 → 1801.14] I was like getting out to people and having them understand this stuff.
[1801.50 → 1801.68] Yeah.
[1802.18 → 1802.42] Um,
[1802.42 → 1802.56] so,
[1802.64 → 1803.64] so Jenkins back to Jenkins.
[1803.78 → 1804.46] So what do I think?
[1804.50 → 1805.50] I think it is,
[1805.56 → 1805.88] um,
[1805.94 → 1806.28] I show,
[1806.40 → 1808.96] it shows just the power of the tools and the power of the community to
[1808.96 → 1810.08] decide that,
[1810.20 → 1810.70] um,
[1810.96 → 1811.16] that,
[1811.28 → 1812.96] that you can fork something.
[1812.96 → 1813.32] I mean,
[1813.36 → 1815.20] forking when renaming wasn't just,
[1815.20 → 1815.74] you know,
[1815.88 → 1816.62] Jenkins itself.
[1816.82 → 1818.18] It was every plugin.
[1818.76 → 1818.94] I mean,
[1818.94 → 1819.70] every plugin is,
[1819.76 → 1820.06] is,
[1820.14 → 1820.40] um,
[1820.40 → 1821.76] essentially had to fork itself,
[1821.94 → 1822.62] rename itself,
[1822.62 → 1824.26] then go back to the original,
[1824.26 → 1824.96] um,
[1824.96 → 1826.78] mailing list or original project and say,
[1826.86 → 1828.12] I no longer want to be a contributor.
[1828.12 → 1829.06] I mean,
[1829.32 → 1831.22] as a grassroots movement,
[1831.40 → 1831.76] it was,
[1831.88 → 1832.52] it was,
[1832.58 → 1832.88] um,
[1833.02 → 1834.28] exceptionally well executed.
[1835.08 → 1835.48] Um,
[1835.48 → 1836.34] and I don't know that,
[1836.34 → 1836.58] uh,
[1836.58 → 1839.52] Oracle's really left with anything that they aren't trying to,
[1839.56 → 1839.76] you know,
[1839.76 → 1840.52] make up themselves.
[1841.40 → 1841.80] Um,
[1842.24 → 1843.20] but it was very disappointing.
[1843.30 → 1843.44] I mean,
[1843.48 → 1846.66] it was annoying that Oracle first went and got the trademark that they
[1846.66 → 1847.56] realized they didn't have.
[1848.38 → 1848.74] Um,
[1849.02 → 1850.82] they weren't really putting any resources into it,
[1850.82 → 1853.76] except turning up to meeting the one meeting I went to for Hudson and
[1853.76 → 1855.20] they had an Oracle representative there.
[1855.20 → 1857.06] So everyone assumed they had the brand,
[1857.18 → 1857.58] the trademark,
[1857.72 → 1859.84] but it turns out they didn't right up until they decided that they were
[1859.84 → 1860.34] going to,
[1860.34 → 1860.58] you know,
[1860.58 → 1861.36] start meddling.
[1862.38 → 1862.52] Hmm.
[1863.52 → 1864.82] So have you seen Travis?
[1867.30 → 1869.62] This is a product because I don't know anyone called Travis.
[1870.88 → 1871.70] Have you met Travis?
[1872.80 → 1874.30] It's a very social conversation.
[1874.52 → 1874.60] No,
[1874.68 → 1874.86] but,
[1874.94 → 1875.04] uh,
[1875.04 → 1875.72] what about Barry?
[1875.72 → 1876.24] Uh,
[1876.48 → 1878.96] so Travis just dropped,
[1879.08 → 1879.26] I guess,
[1879.30 → 1879.52] uh,
[1879.52 → 1880.14] this last week,
[1880.14 → 1882.28] it's a very alpha distributed,
[1882.28 → 1882.98] uh,
[1882.98 → 1883.48] continuous,
[1883.48 → 1884.04] uh,
[1884.04 → 1885.12] integration for Ruby.
[1885.28 → 1885.44] Oh,
[1885.70 → 1887.54] I do remember the name.
[1887.60 → 1887.66] No,
[1887.68 → 1888.32] I haven't played with it.
[1888.38 → 1888.54] I,
[1888.62 → 1888.84] I,
[1888.84 → 1889.14] I,
[1889.22 → 1889.46] um,
[1890.30 → 1891.00] um,
[1891.46 → 1892.78] I must admit I've,
[1892.78 → 1896.14] I've kind of made decisions around about this and people should just use
[1896.14 → 1897.40] Jenkins and be done with it.
[1897.78 → 1898.26] I mean,
[1898.26 → 1898.74] it works.
[1898.80 → 1899.48] It's rock solid.
[1899.84 → 1900.18] Um,
[1900.18 → 1901.16] they've got the plugins.
[1901.16 → 1901.70] We are,
[1901.80 → 1902.14] there's,
[1902.32 → 1902.42] um,
[1903.02 → 1903.26] uh,
[1903.26 → 1905.66] there are people building J Ruby plugin for it.
[1906.00 → 1906.44] Um,
[1906.60 → 1907.30] the frontiers,
[1907.40 → 1907.60] uh,
[1907.60 → 1908.12] front side,
[1908.22 → 1908.38] uh,
[1908.56 → 1908.86] uh,
[1908.86 → 1909.26] but anyway,
[1909.26 → 1910.66] Charles Lau and,
[1910.70 → 1910.88] uh,
[1910.88 → 1912.40] his brother are building a J Ruby plugin.
[1912.52 → 1914.52] So people can write plugins that are in Ruby.
[1915.14 → 1915.58] Um,
[1915.78 → 1916.80] and no doubt the work they do,
[1916.86 → 1919.14] they will make it easier for people to write in other languages as well.
[1919.62 → 1921.64] It is just a rock solid,
[1921.64 → 1922.50] uh,
[1922.54 → 1923.00] CI,
[1923.38 → 1924.26] um,
[1924.30 → 1925.52] workflow engine.
[1925.78 → 1928.52] People are building businesses on top of Jenkins that aren't,
[1929.26 → 1929.56] you know,
[1930.20 → 1930.98] continuous integration.
[1931.16 → 1932.54] They're using it for its workflow engine.
[1933.28 → 1933.60] Um,
[1933.86 → 1934.88] so I get it.
[1934.92 → 1937.02] The people that building your own CI tool,
[1937.10 → 1937.52] and this is no,
[1937.64 → 1937.90] I,
[1937.98 → 1939.20] this is only slightly disrespectful.
[1939.26 → 1939.62] To,
[1939.70 → 1939.84] to,
[1939.96 → 1941.22] to everyone else that's building their own.
[1941.28 → 1941.64] I get it.
[1941.74 → 1942.06] I mean,
[1942.06 → 1943.24] I've certainly built my own stuff.
[1943.68 → 1944.08] Um,
[1944.08 → 1944.44] but I,
[1944.44 → 1945.10] I implore,
[1945.22 → 1945.72] uh,
[1945.80 → 1947.56] real companies that,
[1947.66 → 1949.46] that have projects that need a CI,
[1949.98 → 1950.22] uh,
[1950.22 → 1952.00] need a continuous deployment solution.
[1952.24 → 1953.98] I implore them to at least investigate Jenkins.
[1954.62 → 1955.00] Um,
[1955.00 → 1956.80] if we can all just agree that this thing is awesome,
[1956.80 → 1957.48] um,
[1957.48 → 1960.08] and we start making our open source contributions around that product,
[1960.18 → 1961.90] I think we'll all get a tremendous outcome.
[1962.44 → 1963.36] I get nothing out of it.
[1963.38 → 1963.92] I just think it's,
[1964.04 → 1964.34] it's,
[1964.42 → 1964.66] it's,
[1964.66 → 1967.26] it's important that we all sort of focus our energies.
[1968.98 → 1969.34] Uh,
[1969.34 → 1972.16] I also need to get Ruby developers to get over this whole Java thing.
[1973.00 → 1973.22] Yeah.
[1973.22 → 1973.66] Um,
[1974.66 → 1976.10] so I guess one more general,
[1976.10 → 1976.78] uh,
[1976.96 → 1978.38] open source question.
[1978.78 → 1979.06] Uh,
[1979.18 → 1980.22] I've had a lot of people,
[1980.54 → 1980.78] um,
[1980.94 → 1981.42] actually I got,
[1981.42 → 1983.68] I got two or three patches to a couple of my projects in the last week.
[1983.68 → 1984.28] And people said,
[1984.38 → 1985.08] um,
[1985.60 → 1986.20] please,
[1986.64 → 1986.96] uh,
[1987.10 → 1987.26] be,
[1987.26 → 1987.58] uh,
[1988.72 → 1990.22] I guess I want to say careful or like,
[1990.26 → 1991.38] this is my first patch.
[1991.38 → 1993.02] So I apologize if something's wrong.
[1993.02 → 1994.04] And they were like incredibly,
[1994.04 → 1995.02] uh,
[1995.08 → 1995.32] you know,
[1995.38 → 1997.30] tenuous about their contribution.
[1997.30 → 1997.78] So,
[1997.78 → 1998.36] uh,
[1998.36 → 2003.50] what do you think the open source community can do to actually encourage people to get into open source and contribute?
[2003.70 → 2003.82] I mean,
[2003.84 → 2005.50] this has been sort of a long question,
[2005.88 → 2006.04] but,
[2006.34 → 2006.76] um,
[2006.80 → 2008.46] I think,
[2008.82 → 2009.10] uh,
[2009.10 → 2012.86] I think we should always remember that we're lucky that open source exists anyway.
[2013.46 → 2013.94] Um,
[2013.94 → 2014.74] and that's full of,
[2014.74 → 2015.04] of,
[2015.04 → 2018.14] of disparate humans who all have different motivations and,
[2018.16 → 2018.42] and,
[2018.42 → 2018.64] and,
[2018.64 → 2020.54] and some days we're happy and some days we're sad.
[2020.62 → 2023.32] Some days our wives appreciate what we do and some days they get annoyed at us.
[2023.88 → 2024.32] Um,
[2024.64 → 2025.66] and that if you don't get the
[2025.74 → 2026.00] you know,
[2026.00 → 2026.34] if you,
[2026.34 → 2027.80] if you make your first contribution to,
[2027.90 → 2029.72] to a project, and you don't get the positive,
[2029.90 → 2030.96] warm,
[2031.06 → 2033.48] loving cuddle that you expected or thought you should,
[2033.52 → 2034.02] you might get,
[2034.40 → 2034.80] um,
[2034.90 → 2035.22] don't,
[2035.30 → 2035.84] don't give up.
[2036.02 → 2036.28] You know,
[2036.32 → 2036.48] not,
[2036.72 → 2038.52] not everyone's going to get back to you.
[2038.56 → 2041.42] If you contribute to one of my projects, and you don't hear back from me for,
[2041.50 → 2042.58] for six to 12 months,
[2043.10 → 2043.60] um,
[2043.80 → 2044.92] that is unfortunate.
[2045.38 → 2045.58] Uh,
[2045.58 → 2049.00] and so I assume that I'm just catching that for myself.
[2049.64 → 2049.92] Um,
[2049.92 → 2052.22] it is not that I don't like you or don't know who you are or whatever.
[2052.64 → 2052.90] Um,
[2052.90 → 2054.12] if I'm not using that project,
[2054.12 → 2055.74] it's really hard for me to validate the
[2055.74 → 2056.76] the merit of,
[2056.82 → 2057.36] of your patch.
[2057.80 → 2058.20] Um,
[2058.32 → 2058.86] but I mean,
[2059.00 → 2061.54] just keep contributing,
[2061.72 → 2062.72] understand that you,
[2062.92 → 2063.36] that's,
[2063.42 → 2064.52] that's your first step to,
[2064.76 → 2065.08] you know,
[2065.08 → 2065.20] of,
[2065.20 → 2065.50] of,
[2065.50 → 2066.76] of 10,000 contributions.
[2067.66 → 2068.02] Um,
[2068.02 → 2068.96] and,
[2068.96 → 2069.46] uh,
[2069.48 → 2069.76] I,
[2069.76 → 2069.80] I,
[2069.80 → 2071.62] I am very glad.
[2071.74 → 2071.86] I,
[2071.86 → 2072.04] I,
[2072.04 → 2074.36] I wish there was like a badge that you could get.
[2074.44 → 2075.68] I made my first commit.
[2075.80 → 2078.04] It probably is one of those little badges that you can get.
[2078.40 → 2078.64] Uh,
[2078.64 → 2079.74] it was a wonderful experience.
[2079.74 → 2080.02] And I,
[2080.08 → 2080.28] I,
[2080.28 → 2080.82] I must admit,
[2080.90 → 2082.84] I forget what it's like to make my first contribution.
[2082.84 → 2085.70] It was back in the subversion days.
[2085.78 → 2087.50] I remember I had to figure out how subversion worked.
[2087.84 → 2088.02] There was,
[2088.36 → 2089.46] there's a big,
[2089.50 → 2095.20] there's a big learning curve just to making your first contribution to go from being a user of libraries to becoming a contributor library.
[2096.00 → 2096.36] Um,
[2096.36 → 2096.84] definitely.
[2097.24 → 2097.58] I mean,
[2097.58 → 2100.64] I think I wrote a blog post that's very old and tired and there's probably better ones now,
[2100.64 → 2100.86] but,
[2101.34 → 2101.64] um,
[2102.68 → 2104.86] I just,
[2105.06 → 2105.22] uh,
[2105.22 → 2106.38] for the people making the contributions,
[2106.72 → 2106.90] keep,
[2107.06 → 2107.26] you know,
[2107.56 → 2107.94] I,
[2108.02 → 2108.30] I,
[2108.30 → 2109.42] I employ you to do it.
[2109.44 → 2109.62] I mean,
[2109.62 → 2110.18] I know that we,
[2110.84 → 2113.30] a lot of employers are certainly here at Engine Yard.
[2113.44 → 2114.42] We look at GitHub,
[2114.76 → 2115.14] um,
[2115.14 → 2115.60] accounts.
[2115.80 → 2116.76] We look at your commits,
[2116.86 → 2117.68] look at your projects,
[2118.16 → 2118.74] you know,
[2119.08 → 2120.74] because we want to see what you're interested in,
[2120.78 → 2121.74] what you're capable of.
[2121.94 → 2123.70] We want to see that you've taken that,
[2123.80 → 2124.76] that manly step.
[2125.10 → 2126.28] I don't mean manly,
[2126.36 → 2126.64] uh,
[2126.64 → 2126.88] sorry,
[2127.02 → 2127.74] in the sense of,
[2127.74 → 2128.32] of gender,
[2128.52 → 2130.98] that maturity step of,
[2131.08 → 2134.28] of knowing that you can contribute beyond just your own code base,
[2134.28 → 2135.48] that solving the
[2135.76 → 2138.88] your own application problem sometimes involves fixing other people's stuff.
[2139.52 → 2139.88] Um,
[2139.88 → 2140.44] because that's,
[2140.44 → 2141.66] that it shows initiative.
[2142.32 → 2142.60] Um,
[2142.60 → 2143.18] so you think the
[2143.18 → 2143.34] uh,
[2143.34 → 2145.66] open source portfolio is the new developer resume?
[2147.24 → 2147.72] Yep.
[2148.06 → 2148.46] Absolutely.
[2148.76 → 2149.78] I think I,
[2149.78 → 2151.38] I know there was a project recently that,
[2151.38 → 2151.68] uh,
[2151.74 → 2153.12] GitHub resume project.
[2153.12 → 2153.84] That was kind of cute.
[2154.40 → 2154.80] Um,
[2154.92 → 2156.34] I don't think that's the end of it,
[2156.60 → 2156.98] um,
[2157.22 → 2157.48] but,
[2157.56 → 2157.68] uh,
[2157.68 → 2159.04] it might be cool for people to add tag.
[2159.12 → 2160.18] This is my favourite commit.
[2160.58 → 2160.86] Um,
[2161.62 → 2162.84] but,
[2162.98 → 2163.22] uh,
[2163.32 → 2165.04] I think that certainly it's,
[2165.16 → 2165.34] um,
[2165.82 → 2166.92] it's a starting point for,
[2167.10 → 2168.46] for real conversation,
[2168.46 → 2169.52] but it's also,
[2169.64 → 2169.86] you know,
[2169.86 → 2170.26] getting out,
[2170.30 → 2170.86] learning the
[2170.96 → 2171.98] how to talk in front of public,
[2172.02 → 2174.22] going and talking at local groups about your project,
[2174.32 → 2174.86] communicating,
[2174.86 → 2175.92] um,
[2175.92 → 2176.86] why you did something.
[2177.32 → 2178.06] I think that is,
[2178.28 → 2180.40] that is how you're going to get real jobs and real distinction.
[2181.28 → 2181.56] Um,
[2181.60 → 2182.32] contributing is,
[2182.32 → 2182.60] is,
[2182.60 → 2185.40] is one part of that contributing code is one part of that contributing,
[2185.40 → 2186.14] uh,
[2186.34 → 2187.00] at meetings,
[2187.54 → 2188.50] helping run meetings.
[2188.64 → 2191.76] Each of those is valuable and gives you a visibility and,
[2191.76 → 2192.16] you know,
[2192.38 → 2194.02] and with visibility comes opportunities.
[2195.26 → 2198.02] What's been your biggest adjustment to life in the Northern Hemisphere?
[2198.02 → 2198.26] Well,
[2198.92 → 2199.76] it took me a few weeks,
[2199.94 → 2200.08] but,
[2200.20 → 2200.36] uh,
[2200.40 → 2201.98] I now drive on the correct side of the road.
[2203.84 → 2204.24] Um,
[2204.32 → 2204.92] that's,
[2204.98 → 2205.80] that's not obvious.
[2205.98 → 2206.40] Uh,
[2206.40 → 2209.70] those multi-lane freeways are really quite treacherous if you're on the wrong one.
[2210.48 → 2210.84] Um,
[2210.84 → 2212.98] uh,
[2212.98 → 2213.90] you flash your headlights,
[2214.08 → 2214.30] uh,
[2214.30 → 2215.04] but nothing changes.
[2215.14 → 2216.10] They get furious at you.
[2216.80 → 2217.18] Um,
[2217.98 → 2218.78] I actually got my,
[2218.82 → 2220.18] my temporary driver's license the other day.
[2220.24 → 2221.02] Biggest adjustments,
[2221.48 → 2221.90] um,
[2221.90 → 2224.22] is dealing with my children's accents changing,
[2225.06 → 2228.00] dealing with them picking up new words,
[2228.02 → 2228.62] words that,
[2228.70 → 2229.08] uh,
[2229.16 → 2229.80] you know,
[2230.34 → 2230.80] we always,
[2230.92 → 2232.24] we thought accent might be the issue,
[2232.30 → 2233.46] but then coming back with,
[2233.58 → 2234.76] with all the American phrases,
[2234.76 → 2235.58] uh,
[2235.58 → 2236.62] and then pronunciations,
[2236.76 → 2237.42] that's actually,
[2237.56 → 2238.54] that's a bit of an adjustment.
[2238.54 → 2243.20] It is weird realizing that we are the foreigners and someone else's country.
[2243.56 → 2243.68] Uh,
[2243.68 → 2244.32] we've lived overseas,
[2244.32 → 2245.24] so this is not that,
[2245.34 → 2245.50] that,
[2245.56 → 2246.20] that new to us,
[2246.24 → 2247.50] but hearing our children,
[2247.50 → 2248.02] uh,
[2248.02 → 2249.16] evolves so quickly is,
[2249.16 → 2249.44] is,
[2249.44 → 2249.64] uh,
[2249.64 → 2250.50] emotionally challenging.
[2250.88 → 2252.04] And you've got a new edition.
[2252.44 → 2253.00] We do.
[2253.12 → 2253.32] Uh,
[2253.52 → 2253.84] and,
[2253.92 → 2254.12] uh,
[2254.12 → 2254.88] three-week-old,
[2254.94 → 2255.22] Charlie,
[2255.34 → 2255.58] he's,
[2255.62 → 2255.84] his,
[2255.88 → 2256.06] uh,
[2256.06 → 2257.62] accent is still pretty rock solid.
[2257.62 → 2258.60] Australian at the moment.
[2259.06 → 2259.34] Uh,
[2259.34 → 2262.08] he can do like Australian.
[2263.04 → 2263.44] Um,
[2263.64 → 2263.94] that's,
[2264.04 → 2264.10] uh,
[2264.10 → 2264.24] yeah,
[2264.28 → 2264.40] we,
[2264.50 → 2265.40] uh,
[2265.76 → 2265.94] yeah,
[2265.98 → 2266.80] we'll worry about him,
[2266.88 → 2267.08] uh,
[2267.08 → 2268.24] in a year's time when he starts.
[2269.72 → 2272.56] Because we were tweeting back and forth about a post I'd done the change log.
[2272.56 → 2276.58] And then I found out later that everybody's congratulating you on the edition.
[2276.90 → 2277.02] And you,
[2277.18 → 2277.52] it was,
[2277.58 → 2278.60] I was actually in a hospital.
[2278.60 → 2279.02] So for,
[2279.10 → 2279.58] for listeners.
[2279.80 → 2279.96] So,
[2279.96 → 2280.22] um,
[2280.52 → 2280.74] yeah,
[2280.74 → 2281.54] there was the post.
[2281.68 → 2282.12] What was it?
[2282.50 → 2284.10] It was just inappropriately titled.
[2284.34 → 2288.24] It was a post of really as a list of things people should do in their project.
[2288.84 → 2290.88] But then you put some wacky title on it.
[2290.88 → 2293.84] Like I'm not going to use your project unless you do the following.
[2294.90 → 2295.38] You know,
[2295.42 → 2295.64] blah,
[2295.64 → 2295.86] blah,
[2295.96 → 2296.14] blah.
[2296.24 → 2297.02] Sucks to be you.
[2297.46 → 2297.74] Um,
[2297.74 → 2299.78] but then your tweet said something completely different.
[2299.96 → 2300.92] And so I was,
[2301.00 → 2301.12] look,
[2301.18 → 2303.80] I was confused as to what message you were trying to convey.
[2304.20 → 2304.58] Uh,
[2304.58 → 2304.98] and yes,
[2304.98 → 2306.46] I did happen to be in the hospital,
[2307.02 → 2309.32] standing next to my wife who had just been put into the
[2309.44 → 2309.76] you know,
[2309.76 → 2311.44] the post delivery room.
[2311.80 → 2312.20] Um,
[2312.20 → 2313.74] it wasn't entirely the best timing,
[2313.74 → 2314.34] but you know,
[2314.42 → 2316.62] you started a fight on the internet and I needed to.
[2318.74 → 2319.26] It's like,
[2319.42 → 2319.52] I,
[2319.64 → 2319.82] uh,
[2319.82 → 2322.06] speaking of people that are tirelessly helpful,
[2322.30 → 2322.52] um,
[2322.60 → 2324.56] Wayne from RVM one time,
[2324.62 → 2326.90] I heard a podcast where he was giving an interview, and they heard some
[2326.90 → 2327.74] typing, and they said,
[2328.12 → 2328.30] Wayne,
[2328.36 → 2330.48] are you on IRC helping someone right now?
[2330.48 → 2330.92] And he was like,
[2330.96 → 2331.26] yeah,
[2331.26 → 2331.72] maybe.
[2332.08 → 2333.88] And I guess like while he was being interviewed,
[2333.88 → 2337.42] he was like helping somebody out fixing their RVM problem over on
[2337.42 → 2337.82] free node.
[2338.38 → 2338.64] Oh yeah.
[2338.70 → 2339.74] That is a red dirt.
[2340.14 → 2340.50] Yeah.
[2340.50 → 2341.22] He'll be at red dirt.
[2341.46 → 2341.78] Um,
[2342.18 → 2342.36] I,
[2342.36 → 2342.70] I,
[2342.94 → 2343.10] yeah,
[2343.10 → 2343.56] so Wayne,
[2343.72 → 2344.00] uh,
[2344.00 → 2344.86] Wayne and I work together,
[2345.00 → 2346.30] obviously in part on,
[2346.30 → 2347.00] on rails install,
[2347.12 → 2347.30] but,
[2347.40 → 2347.62] um,
[2347.68 → 2347.86] Wayne,
[2347.92 → 2348.64] Wayne's here at engineer,
[2348.90 → 2349.18] uh,
[2349.18 → 2350.40] doing some internal stuff as well,
[2350.40 → 2351.28] um,
[2351.48 → 2351.72] for,
[2351.88 → 2352.00] for,
[2352.14 → 2352.44] you know,
[2352.44 → 2354.52] customers and all the projects that are going on here.
[2354.90 → 2355.26] And,
[2355.38 → 2355.60] uh,
[2355.78 → 2356.26] and it is,
[2356.26 → 2358.00] is a wonderfully energetic man.
[2358.06 → 2358.82] It's awesome to work with.
[2358.82 → 2360.20] I'm very glad he came back to engineer.
[2360.56 → 2360.92] Um,
[2361.04 → 2362.88] I'm glad he's not somewhere else helping someone else.
[2364.38 → 2366.00] So what out there has got you excited?
[2367.46 → 2369.24] What open source do you just want to play with?
[2370.02 → 2371.04] The last month or so,
[2371.10 → 2372.16] I've been doing a couple of internals,
[2372.16 → 2372.62] uh,
[2372.62 → 2373.16] you know,
[2373.16 → 2375.12] projects that we're going to release to the customers.
[2375.30 → 2376.86] So I must admit that that's kind of,
[2377.10 → 2380.36] whilst it's still having the excitement of building a new product and a
[2380.36 → 2382.30] project that I would have otherwise done anyway as a
[2382.30 → 2382.80] as a non,
[2382.94 → 2383.50] uh,
[2383.50 → 2384.26] company person.
[2384.26 → 2385.18] Um,
[2385.82 → 2387.62] I guess those have been my attraction.
[2388.00 → 2388.52] I look,
[2388.56 → 2391.32] I'm pretty desperate to get my hands on some of this stuff around J Ruby
[2391.32 → 2391.96] and Jetty.
[2392.16 → 2392.34] And,
[2392.34 → 2392.60] uh,
[2392.68 → 2393.04] um,
[2393.50 → 2393.86] uh,
[2393.86 → 2396.10] Carl Lurch has been building a thing called Kirk,
[2396.28 → 2397.40] which is,
[2397.40 → 2397.92] uh,
[2397.92 → 2398.22] uh,
[2398.22 → 2399.52] like a new web server for,
[2399.62 → 2399.76] uh,
[2399.76 → 2400.30] for J Ruby,
[2400.52 → 2401.04] which,
[2401.18 → 2401.58] um,
[2401.60 → 2402.20] a bunch of,
[2402.24 → 2402.36] you know,
[2402.36 → 2403.06] zero deploy,
[2403.06 → 2403.52] uh,
[2403.70 → 2404.10] invented.
[2404.10 → 2404.54] And,
[2404.66 → 2404.86] uh,
[2404.86 → 2406.62] I think that's going to be very enabling it.
[2406.66 → 2408.24] And hopefully we can get it out of product if it's,
[2408.44 → 2408.46] uh,
[2408.66 → 2408.94] you know,
[2409.06 → 2410.06] help it get rock solid.
[2410.06 → 2411.10] Um,
[2411.76 → 2415.76] I want to learn more about all the fun stuff that's in the Java community
[2415.76 → 2416.50] that I get to,
[2416.80 → 2418.46] if I just knew what it was,
[2418.46 → 2419.34] because I've,
[2419.66 → 2420.30] okay,
[2420.38 → 2421.22] so here's the card,
[2421.48 → 2421.76] right?
[2421.80 → 2421.94] Oh,
[2421.94 → 2422.46] I follow the
[2422.60 → 2425.22] there's a Ruby gem Twitter account and all it is,
[2425.22 → 2426.36] is all the things get released,
[2426.44 → 2428.22] which is hundreds a day.
[2428.22 → 2428.78] I get it.
[2428.78 → 2428.92] Right.
[2428.92 → 2429.26] So my,
[2429.26 → 2430.70] my Twitter feed is half filled with,
[2430.78 → 2431.88] with these product announcers,
[2432.00 → 2432.90] but at least I'm,
[2432.98 → 2433.14] I'm,
[2433.20 → 2434.84] I have a vague awareness of what's coming out.
[2435.04 → 2436.20] Plus Ruby news and,
[2436.20 → 2436.50] and,
[2436.50 → 2436.78] um,
[2436.78 → 2437.18] JavaScript,
[2437.52 → 2437.74] you know,
[2437.74 → 2438.16] retweets,
[2438.28 → 2438.58] et cetera.
[2439.02 → 2440.36] But I have no idea what,
[2440.54 → 2442.02] what the Java world is building.
[2442.40 → 2442.76] Therefore,
[2442.88 → 2444.54] what I'm not being able to use because I,
[2444.56 → 2445.38] I don't know about it.
[2445.50 → 2446.04] So that's,
[2446.12 → 2449.96] that's the challenge with the J Ruby project is it allows you to do all this
[2449.96 → 2450.30] stuff,
[2450.30 → 2452.92] but then you've kind of got to live in two communities to be able to take
[2452.92 → 2453.56] advantage of it.
[2454.20 → 2454.56] Um,
[2455.32 → 2455.68] and I,
[2455.68 → 2455.86] I,
[2456.00 → 2456.22] you know,
[2456.52 → 2459.56] this building massive web scale applications,
[2459.56 → 2460.20] I think,
[2460.58 → 2463.02] I think there's a bunch of cool stuff that I reckon we'll find over in the
[2463.02 → 2465.14] Java community if we were just to go and have a dig around.
[2465.88 → 2466.20] So,
[2466.60 → 2466.80] uh,
[2466.80 → 2467.88] what am I excited about at the moment?
[2467.96 → 2468.46] That's Kirk.
[2468.84 → 2471.58] What am I excited about in the future is finding more gold.
[2472.28 → 2472.68] Um,
[2472.68 → 2473.94] I'm also very still excited about,
[2474.02 → 2474.76] about the Jenkins,
[2474.76 → 2475.76] um,
[2475.76 → 2476.10] project.
[2477.38 → 2477.82] Um,
[2477.82 → 2477.94] I,
[2478.06 → 2479.84] I want to see someone lay the foundation.
[2479.94 → 2480.92] We have a CLI for that.
[2481.00 → 2483.18] It's a bit more sort of client Ruby orientated.
[2483.28 → 2486.98] So you can sort of point it at a project and go sort of Jenkins create dot,
[2487.04 → 2490.22] and it automatically creates a job and starts running your tests without
[2490.22 → 2490.96] doing any setup.
[2491.12 → 2491.90] That's very cool.
[2492.28 → 2492.44] Uh,
[2492.44 → 2494.00] so pushing that further out and sort of making,
[2494.22 → 2494.52] you know,
[2494.52 → 2496.62] continuous deployment easy.
[2496.96 → 2497.92] It's more testing to be,
[2497.92 → 2498.06] you know,
[2498.06 → 2500.30] doing CI to be easier than not to do than not to.
[2500.64 → 2501.80] Is that too much to ask?
[2502.14 → 2502.46] Seriously?
[2503.24 → 2503.60] Indeed.
[2503.74 → 2504.92] Everyone writes tests.
[2504.92 → 2507.94] How many people actually got functioning CI servers running?
[2507.94 → 2508.76] I mean,
[2508.92 → 2509.32] hearts,
[2509.64 → 2509.98] you know,
[2510.18 → 2513.08] promises that look after they care about it.
[2513.22 → 2514.82] And I don't think it's enough people.
[2515.56 → 2516.08] I think,
[2516.26 → 2518.92] I think there's a lot of lip talk to this whole conversation.
[2518.92 → 2521.06] And part of it is it's still just not easy enough.
[2521.74 → 2524.68] And this is me looking at this Travis article that you guys did the other day.
[2525.04 → 2525.40] And,
[2525.48 → 2525.68] and,
[2525.78 → 2525.98] you know,
[2526.06 → 2527.26] there's still steps, and it's still,
[2527.32 → 2528.02] you got to set it up,
[2528.02 → 2529.04] um,
[2529.16 → 2529.72] and,
[2529.86 → 2530.20] uh,
[2530.52 → 2531.22] and maintain it.
[2531.22 → 2532.34] So I think there's,
[2533.06 → 2533.66] you know,
[2533.92 → 2534.28] there's a
[2534.34 → 2536.60] there's a big space there to people make the world a better place,
[2536.60 → 2537.52] which is keeping,
[2537.72 → 2538.74] keeping CI simple.
[2540.42 → 2540.74] Well,
[2540.76 → 2541.60] we know you're a busy man.
[2541.98 → 2544.02] Surely appreciate you taking the time to talk with us.
[2544.32 → 2545.86] Look on the change log show.
[2546.22 → 2547.96] This is the biggest show in the world at the moment.
[2548.42 → 2549.60] Thank you very much for inviting me.
[2549.64 → 2550.18] It's been awesome.
[2550.18 → 2550.26] Awesome.
[2550.66 → 2551.18] Awesome.
[2551.18 → 2552.18] Awesome.
[2552.18 → 2553.18] Awesome.
[2553.18 → 2554.18] Awesome.
[2554.18 → 2555.18] Awesome.
[2555.18 → 2556.18] Awesome.
[2556.18 → 2557.18] Awesome.
[2557.18 → 2558.18] Awesome.
[2558.18 → 2559.18] Awesome.
[2559.18 → 2560.18] Awesome.
[2560.18 → 2561.18] Awesome.
[2561.18 → 2565.20] Awesome.
[2579.30 → 2579.78] Awesome.
[2582.00 → 2583.90] Awesome.
[2584.14 → 2585.14] Awesome.
[2589.20 → 2589.62] Awesome.
[2589.62 → 2590.14] Awesome.
