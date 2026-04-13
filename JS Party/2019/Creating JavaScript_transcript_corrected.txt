[0.14 → 4.04] Greetings, JS Party listeners. We're doing something a little different today in the podcast feed.
[4.36 → 7.34] We partnered with Red Hat to promote Season 3 of Command Line Heroes.
[7.92 → 11.20] And today, we're bringing you Episode 3 to our feed.
[11.42 → 15.18] It's called Creating JavaScript. This is an original podcast from Red Hat.
[15.38 → 17.72] It's hosted by Saran ya Barak of Code Newbie.
[18.00 → 20.20] And to learn more and subscribe to this awesome podcast,
[20.66 → 24.66] head to redhat.com slash commandlineheroes or check the show notes for a link.
[25.02 → 25.38] Here we go.
[25.38 → 34.70] Brendan Eich was 34 years old when he sat down at his desk in the Netscape headquarters.
[35.50 → 39.18] He was committing himself to a massive 10-day sprint of coding.
[39.82 → 46.76] A new language, a whole new programming language in just 10 days.
[47.34 → 53.28] It was 1995, and the world of programming languages was about to change forever.
[55.38 → 61.40] I'm Saran ya Barak, and this is Command Line Heroes, an original podcast from Red Hat.
[62.24 → 67.92] All season long, we're exploring the power and promise of programming languages,
[68.60 → 73.68] discovering how our languages shape the world of development and how they supercharge our work.
[74.46 → 77.98] This time, we're tracking the creation of JavaScript.
[78.86 → 81.24] Maybe you've heard the story of Brendan Eich before,
[81.24 → 85.08] but how does something like JavaScript really get created?
[85.78 → 89.84] There was Brendan's sprint, sure, but there's so much more to the story.
[92.00 → 97.96] Our JavaScript tale begins in the midst of a war, a browser war.
[97.96 → 107.50] The browser wars of the 1990s may seem like history, but they were hugely consequential.
[108.06 → 113.96] On one side of the battlefield, Netscape, which had formed an alliance with Sun Microsystems.
[114.38 → 118.06] On the other, you've got Microsoft, software behemoth.
[118.60 → 120.76] And what were the spoils they were fighting over?
[120.76 → 125.40] It was a battle to decide who would be the gatekeeper of the Internet.
[126.16 → 128.20] The stakes could not be larger.
[129.36 → 132.68] To really understand how the browser wars went down,
[133.16 → 137.32] I called up one of my favourite tech historians, author Clive Thompson.
[137.98 → 139.16] His most recent book?
[139.50 → 142.98] Coders, The Making of a New Tribe and The Remaking of the World.
[143.48 → 146.24] Clive and I got talking about the browser wars.
[146.58 → 148.96] But let me really set the scene for you.
[150.76 → 155.88] You've got Netscape, realizing that the browser was this key piece of software
[155.88 → 158.60] that people were going to use to get online.
[159.16 → 160.72] And then you've got Microsoft.
[161.38 → 165.60] Their whole business model was packaging stuff inside Windows.
[166.32 → 168.52] They hadn't really been interested in browsers.
[169.40 → 175.80] Until in the 1990s, Microsoft realized that maybe they'd been sleeping at the wheel.
[175.80 → 178.42] The world was moving online.
[178.70 → 182.98] And there was nothing inside of Microsoft Windows that would help them get there.
[183.88 → 187.16] But these guys over here, some company called Netscape,
[187.46 → 189.88] they're offering an on-ramp to the Internet.
[190.56 → 195.76] All of a sudden, Microsoft's industry-wide dominance doesn't look so absolute.
[196.50 → 199.38] The browser wars begin at that moment.
[199.38 → 203.68] The moment when Microsoft wakes up to the power of the Internet
[203.68 → 206.68] and squints its eye at their new competition.
[207.38 → 208.84] So, that's my setup.
[209.28 → 212.24] Here's me and Clive hashing out what happened next.
[212.44 → 216.88] The fight was over who was going to be the main portal to going online.
[217.58 → 221.74] You have to realize that in the early 90s, no one was really online very much.
[221.74 → 225.88] And when Mosaic came along and eventually turned into Netscape,
[226.16 → 230.46] they were the first browser that anyone could download that would let you look at the web.
[230.70 → 233.20] And they went online in December 1994.
[233.94 → 237.28] And so, suddenly, you know, thousands and millions of people
[237.28 → 240.76] are able to use the Internet in this kind of graphical way.
[240.84 → 244.36] They're just getting massive, massive downloads and huge amounts of press.
[244.42 → 245.68] And everyone's basically saying, yeah,
[245.82 → 248.30] Netscape is kind of the future of this thing called the Internet.
[248.30 → 254.60] So, you know, over in Seattle, you've got Microsoft watching this with enormous alarm
[254.60 → 256.92] because they had pretty much ignored the Internet.
[257.28 → 259.38] They were focused on selling Windows.
[260.28 → 264.38] And they had really not paid any attention to this crazy newfangled thing called the Internet.
[264.62 → 267.40] So, they had to play a very rapid game of catch-up.
[267.50 → 271.20] They did not get their own browser out for almost a year later.
[271.36 → 274.14] In the fall of 1995, their browser came out.
[274.20 → 277.00] And that was essentially the beginning of the browser wars,
[277.00 → 282.56] the moment when Microsoft was trying to fight to be the portal by which people went online.
[282.76 → 283.08] Okay.
[283.20 → 286.10] So, a year to me doesn't sound like, that doesn't sound like too bad, right?
[286.10 → 288.08] That's not too wrong, right?
[288.28 → 290.90] That seems like a reasonable amount of time.
[290.92 → 291.32] No, it's true.
[291.40 → 295.18] It doesn't sound like a long time, but things were moving so rapidly back then.
[295.34 → 298.12] And there was a strong sense of first mover advantage
[298.12 → 303.06] that the first company that could sort of brand themselves as the way you get online
[303.06 → 305.88] would be the winner for years and years and maybe forever.
[305.88 → 308.92] Because I remember how rapid the pace of development was.
[309.02 → 312.64] I mean, Netscape was putting out a new browser every couple of months, right?
[312.70 → 316.10] Like, they would be, wow, now we've got email integrated into the browser.
[316.44 → 319.26] Now we've got, you know, a sort of little search bar up top.
[319.38 → 321.58] It just kept on becoming better and better.
[321.70 → 325.70] You could sort of see, you know, all the things you could do online
[325.70 → 330.50] and swimming into view as they've rapidly iterated and rapidly pushed things out.
[330.88 → 333.00] Microsoft was accustomed to developing very slowly.
[333.44 → 336.50] Here's your four-year-long, you know, development process.
[336.58 → 339.16] At the end, it's as bug-free as we can get it.
[339.26 → 339.90] Put it in a box.
[340.26 → 341.02] Goes out to the stores.
[341.22 → 344.10] And we don't release a new version for four years, you know?
[344.60 → 347.38] Netscape comes along and is the first company to say,
[347.72 → 350.94] no, we're going to put out kind of a substandard product.
[351.42 → 354.92] But it works well enough, and we're going to have a new one for you to download
[354.92 → 357.12] in three months and three months and three months.
[357.26 → 359.16] And this completely destabilized Microsoft.
[359.66 → 361.80] Okay, so if I'm Microsoft, I can look at it and go,
[361.86 → 363.06] oh my goodness, this is the future.
[363.18 → 364.54] I need to catch up.
[364.58 → 365.52] I need to compete.
[365.88 → 367.74] Or I can say, ah, it's a fad.
[367.74 → 375.98] So what is it about the browser that made Microsoft pick the first option
[375.98 → 378.94] that made Microsoft go, oh my goodness, this is a real thing.
[379.00 → 379.60] I need to compete.
[380.10 → 384.70] The thing about the browser was that it had a huge amount of cultural cachet.
[385.06 → 389.98] It was the first thing you could do on the internet that was like culturally fun.
[390.22 → 393.60] You know, you could go to suddenly a band's webpage
[393.60 → 395.92] and see posts by them and photos by them.
[395.92 → 402.48] You could go and research, you know, your hobby by finding all the model train people in Florida, right?
[402.74 → 405.90] So, you know, everything about the internet before that had seemed nerdy.
[406.56 → 408.86] Email, you know, file transfers, whatnot.
[409.06 → 413.10] I mean, suddenly the browser made the internet look like a magazine,
[413.52 → 415.44] you know, like a fun thing to interact with.
[415.80 → 420.28] And so newspapers and CNN and magazines were sort of writing about it
[420.28 → 422.48] in this very excited way for the first time.
[422.48 → 427.64] This was the moment that technology moved from being buried deep inside the business section
[427.64 → 430.54] to being on page A1 of the New York Times.
[430.88 → 434.72] So what was appealing about Netscape or even just the browser in general
[434.72 → 436.18] when it comes to developers?
[436.40 → 437.44] Why were they so into it?
[437.70 → 439.22] I've met a lot of developers.
[439.44 → 441.54] Suddenly the internet comes along with the browser
[441.54 → 446.26] and you can just have a webpage that says, you know, just download my cool piece of software.
[446.26 → 452.48] So it unlocked the entire world of the way that we see software being made today.
[453.22 → 458.30] I should mention here that at first, Microsoft actually offered to buy Netscape,
[458.58 → 461.06] though they were offering a pretty tiny amount.
[461.54 → 463.22] But Netscape turned them down.
[463.52 → 466.06] So Microsoft had to build a browser of their own.
[466.60 → 468.56] They called theirs Explorer.
[468.56 → 474.50] Microsoft spent a year frantically working on a browser.
[475.14 → 478.36] And they got it out in the fall of 1995.
[479.22 → 483.32] And they did sort of the same thing that Netscape did.
[483.40 → 486.04] They produced something quickly without worrying if it was perfect.
[486.40 → 487.48] And it got better and better.
[487.48 → 494.18] But what really emerged over the latter half of the 90s was a war over, you know,
[494.48 → 501.32] whose browser would be the most interesting, the most, you know, sort of interactive and sophisticated.
[502.54 → 506.78] Keep in mind that Netscape by no means had the upper hand here.
[507.02 → 509.06] Microsoft just had a very powerful position.
[509.38 → 512.92] You know, when you ship Windows to, you know,
[513.30 → 516.68] on the order of 80 to 90 percent of all computers on the planet,
[516.68 → 519.58] it's pretty easy to make your software the default.
[519.72 → 520.70] And that's exactly what they did.
[521.08 → 525.06] And so you see, you know, Explorer sort of rise and rise and rise.
[525.80 → 530.36] In a way, poor old Netscape was always the underdog in that battle.
[530.86 → 532.04] But here's the thing.
[532.50 → 536.20] Before the battle was over, they threw a beautiful Hail Mary.
[536.44 → 542.42] And it turns out that would become an incredible score for the whole world of programming.
[542.42 → 550.58] That is the fascinating and weird story of the creation of JavaScript.
[550.58 → 557.26] All that heat around the web, around the potential of life in a browser,
[557.82 → 560.06] had made one thing very clear.
[560.76 → 565.78] We needed a new programming language, something that went far beyond HTML.
[565.78 → 571.52] We needed a language tailor-made for all that new web-based development.
[572.44 → 576.98] We wanted a language that didn't just survive online, but thrived there.
[579.48 → 583.24] How do you create a programming language for the browser?
[584.60 → 587.78] That, my friend, was the billion-dollar question.
[587.78 → 593.66] So, around the time Netscape saw that Microsoft was competing with them,
[594.12 → 595.54] they took a look at Java.
[596.36 → 599.36] Was Java going to be the language for web development?
[602.42 → 605.56] Java was this rich, compiled language.
[606.06 → 608.44] It performed just as well as C++.
[609.20 → 611.72] But it did still need to be compiled.
[612.56 → 615.48] Developers really wanted something more lightweight,
[615.48 → 619.40] something that could be interpreted instead of compiled,
[619.98 → 623.64] something that would appeal to all those non-professional programmers
[623.64 → 625.66] that were swarming to the web.
[626.26 → 630.94] Those new programmers wanted to work directly on the web page, after all.
[631.52 → 632.70] That was the dream.
[635.04 → 639.40] Netscape needed a programming language that would run inside their browser,
[639.94 → 644.42] something that would allow developers to bring those static web pages to life.
[644.42 → 647.06] Wouldn't it be great, they thought,
[647.26 → 650.08] if they could release a new, lightweight language
[650.08 → 652.52] that worked wonders for web programming,
[652.88 → 656.80] at the same time that they released Netscape 2.0 in beta?
[657.50 → 659.04] There was only one hitch.
[659.58 → 664.26] That gave them exactly 10 days to create a new language.
[665.58 → 669.66] Actually, it gave one guy, Brendan Eich, 10 days.
[669.66 → 672.98] He was the one tasked with pulling this off.
[673.54 → 677.32] There was no doubt that, if anybody could do it, this guy could.
[677.92 → 680.70] When Brendan was a student at the University of Illinois,
[681.06 → 683.48] he used to create new languages for fun,
[683.82 → 685.54] just to play around with syntax.
[686.36 → 689.30] The key to Brendan Eich is that Brendan Eich,
[689.36 → 690.44] when he built JavaScript,
[690.68 → 693.90] had become sort of a language junkie.
[693.90 → 697.42] To understand what Ike actually pulled off,
[697.74 → 699.84] we reached out to Charles Severance,
[700.12 → 703.52] a professor at the University of Michigan School of Information.
[704.38 → 706.88] JavaScript was sort of created an environment
[706.88 → 709.72] where Java was seen as the future.
[710.44 → 711.64] And so in 1994,
[712.58 → 716.74] we thought that it was the thing that was going to solve everything.
[716.74 → 719.12] One year later,
[719.52 → 722.64] the thing that would actually solve everything was about to appear,
[723.02 → 723.96] but it couldn't say,
[724.18 → 725.40] hey, I've solved everything,
[725.54 → 728.32] because everybody, myself included,
[728.92 → 730.58] believed in 94, 95,
[731.06 → 733.48] that we had seen the future of rock and roll.
[733.66 → 735.18] And it was the Java programming language.
[735.68 → 737.08] They had to build a language
[737.08 → 739.36] that seemed irrelevant,
[740.02 → 740.68] seemed silly,
[741.00 → 741.86] seemed meaningless,
[742.54 → 745.12] and yet was the right solution.
[745.12 → 746.82] What Ike delivered
[746.82 → 749.10] was not just a toy language, though.
[749.66 → 752.14] It was sophisticated in hidden ways,
[752.74 → 754.62] drawing on major inspirations
[754.62 → 756.56] from languages that had come before.
[756.88 → 758.52] If you look at the basic syntax,
[758.86 → 762.00] it's very clear that it's inspired by the C language
[762.00 → 764.62] with its curly braces and semicolons.
[765.16 → 766.32] Some of the string patterns
[766.32 → 768.10] were taken from the Java programming language,
[768.24 → 771.02] but the object-oriented underlying pattern
[771.02 → 773.36] was taken from a programming language
[773.36 → 774.34] called Module 2,
[774.34 → 776.92] which had this notion of first-class functions,
[777.04 → 778.76] which to me is really
[778.76 → 780.78] one of the most amazing choices
[780.78 → 782.30] that made JavaScript
[782.30 → 784.04] such a powerful and extensible language,
[784.20 → 785.86] and that is that the function,
[786.04 → 787.00] the body of the function,
[787.12 → 788.98] the code that makes up a function itself,
[789.58 → 790.40] is also data.
[790.88 → 792.18] And the other thing
[792.18 → 794.16] that really was a part of the inspiration
[794.16 → 795.40] was HyperCard.
[796.18 → 798.18] JavaScript was always running in a browser,
[798.18 → 802.46] which meant it had a basic data context
[802.46 → 804.74] of the document object model,
[804.84 → 806.54] which is an object-oriented representation
[806.54 → 807.56] of a web page.
[807.94 → 810.42] It is not like a traditional programming language.
[810.96 → 813.74] The JavaScript code didn't start at the beginning.
[813.86 → 815.60] The first thing that it was a web page.
[816.28 → 819.68] And so it ended up with this event-oriented programming.
[819.68 → 824.30] When JavaScript was released,
[824.44 → 826.78] along with Netscape Navigator 2.0,
[827.06 → 828.80] on November 30, 1995,
[829.52 → 831.66] all that magic was housed
[831.66 → 834.26] into a powerful little seed of a language.
[834.94 → 836.16] 28 companies,
[836.72 → 839.16] including America Online and AT&T,
[839.62 → 842.78] agreed to use it as an open standard language.
[843.34 → 844.40] When it was released,
[844.72 → 846.12] there were some old pros
[846.12 → 848.54] looking down their noses at JavaScript.
[848.54 → 851.30] They thought it was just a language for newbies.
[851.74 → 854.04] They missed its revolutionary potential.
[855.58 → 857.88] Brendan decided he would sneak in
[857.88 → 860.70] all these super advanced concepts
[860.70 → 863.64] from languages that are not well known,
[863.76 → 864.72] that were very like advanced
[864.72 → 865.86] object-oriented languages.
[866.46 → 868.98] And so JavaScript is almost like a Trojan horse.
[869.16 → 871.20] It sort of sneaked into our collective consciousness
[871.20 → 874.60] with the idea that it was silly and fun
[874.60 → 875.52] and easy and lightweight,
[875.52 → 878.10] but then built in from almost
[878.10 → 878.94] the very beginning
[878.94 → 881.04] was a powerful, deeply thought,
[881.14 → 882.58] well-thought-out programming language
[882.58 → 883.82] that's capable of doing
[883.82 → 886.04] literally almost anything in computer science.
[886.54 → 889.84] The result was a language native to the browser
[889.84 → 893.24] that could evolve as our online lives evolved.
[893.70 → 895.76] It didn't take long before JavaScript
[895.76 → 898.46] became the de facto web development option.
[898.98 → 900.04] JavaScript was a language
[900.04 → 901.70] that I had no choice but to learn.
[902.16 → 902.72] And literally,
[903.12 → 903.94] people that learn JavaScript
[903.94 → 905.48] usually have no choice
[905.48 → 906.86] because they're like,
[906.92 → 908.12] I want to build a browser application
[908.12 → 909.72] and I want it to have interactive elements.
[909.92 → 910.48] And the answer is,
[910.70 → 911.90] therefore, you must learn JavaScript.
[912.46 → 913.66] If you imagine, like,
[913.76 → 915.14] what is your favourite language?
[915.72 → 916.90] The answer to that question
[916.90 → 918.28] has almost got to be
[918.28 → 919.52] X plus JavaScript.
[920.52 → 920.66] Right?
[920.76 → 921.50] Someone might say,
[921.64 → 923.94] I like Python and JavaScript.
[924.32 → 926.26] Or I like Scala and JavaScript.
[926.82 → 928.74] Because it's like the one language
[928.74 → 930.48] everyone is required to learn.
[930.48 → 936.28] Charles Severin's is a professor
[936.28 → 937.88] at the University of Michigan
[937.88 → 938.88] School of Information.
[943.92 → 946.04] Netscape had been incredibly strong
[946.04 → 947.02] coming out of the gate.
[947.40 → 949.94] And they fought hard during the browser war.
[950.48 → 952.28] But in the end...
[952.28 → 954.64] Netscape just disappears as a serious product.
[954.64 → 959.10] Microsoft's industry-wide domination
[959.10 → 961.18] was an overwhelming force.
[961.78 → 963.18] Despite being a year late
[963.18 → 964.08] to the browser game,
[964.42 → 966.10] they were able to pull themselves
[966.10 → 968.04] back on top and win the day.
[968.68 → 969.66] But you know,
[969.94 → 971.16] Netscape's Hail Mary,
[971.60 → 972.96] its creation of JavaScript,
[973.36 → 974.36] was a success.
[974.84 → 977.16] Because long after the fight was over,
[977.62 → 978.74] this gem of a language
[978.74 → 980.96] that came out of their browser war,
[981.50 → 982.96] it would have an afterlife
[982.96 → 984.56] that changed everything.
[984.64 → 992.44] If you started coding more recently,
[992.92 → 994.36] you might take for granted
[994.36 → 995.38] that you can develop
[995.38 → 996.80] interactive web pages
[996.80 → 998.48] that change and update
[998.48 → 1000.40] without pulling a whole new copy
[1000.40 → 1001.76] of the page from the server.
[1002.86 → 1004.88] But imagine for a sec
[1004.88 → 1005.94] what it was like
[1005.94 → 1007.08] when doing that
[1007.08 → 1008.92] became a brand-new option.
[1009.60 → 1011.00] We asked Michael Clayton,
[1011.24 → 1013.04] a software engineer at Red Hat,
[1013.24 → 1014.32] to help us understand
[1014.32 → 1016.34] what a huge shift that was.
[1017.26 → 1019.66] In, I want to say, 2004,
[1020.42 → 1022.88] Google Mail was released.
[1023.26 → 1023.50] Gmail.
[1023.50 → 1027.02] And it was, to my knowledge,
[1027.44 → 1029.06] the first web application
[1029.06 → 1030.82] that really took JavaScript
[1030.82 → 1031.80] to the next level,
[1032.10 → 1033.94] that used it to
[1033.94 → 1036.32] dynamically switch content out
[1036.32 → 1037.40] that you were looking at.
[1038.18 → 1040.06] Say you're looking at your inbox
[1040.06 → 1041.52] and you click on an email.
[1042.02 → 1043.02] In the old days,
[1043.18 → 1044.24] your email viewer
[1044.24 → 1046.26] would load a whole new page
[1046.26 → 1046.96] in your browser
[1046.96 → 1048.54] just to show you that email.
[1049.20 → 1051.16] Then, you close that email
[1051.16 → 1052.36] and it would reload
[1052.36 → 1053.82] the whole inbox.
[1053.82 → 1055.74] It created a lot of latency.
[1056.04 → 1056.84] There was a lot of waiting
[1056.84 → 1057.60] when you would switch
[1057.60 → 1059.06] back and forth between views
[1059.06 → 1060.96] and Gmail changed all that.
[1061.42 → 1062.76] They used JavaScript
[1062.76 → 1064.66] to, in the background,
[1064.84 → 1065.66] fetch the content
[1065.66 → 1066.78] that you wanted to view
[1066.78 → 1068.32] and just put it in front of you
[1068.32 → 1069.66] without you having to wait
[1069.66 → 1071.96] for a brand-new page view.
[1072.96 → 1075.38] That saved a ton of time
[1075.38 → 1076.10] and energy.
[1076.60 → 1078.26] But really think about it.
[1078.26 → 1080.64] It changed more than just the speed.
[1080.64 → 1082.62] It changed the very nature
[1082.62 → 1083.54] of our work.
[1084.70 → 1085.80] So, web developer
[1085.80 → 1087.40] as a job title
[1087.40 → 1088.84] has gone from
[1088.84 → 1091.24] being a server-side,
[1091.38 → 1093.02] kind of behind-the-scenes role
[1093.02 → 1095.48] to being just a very thin layer
[1095.48 → 1096.46] away from the user
[1096.46 → 1097.52] since they're writing code
[1097.52 → 1098.56] directly in the browser
[1098.56 → 1100.36] that the user is viewing
[1100.36 → 1101.26] the web page through.
[1101.74 → 1102.86] It changed everything.
[1103.66 → 1104.30] In fact,
[1104.30 → 1105.80] you can pretty much
[1105.80 → 1106.74] credit JavaScript
[1106.74 → 1108.12] with ushering in
[1108.12 → 1110.00] the Web 2.0 revolution.
[1110.64 → 1112.26] Anybody with the web browser
[1112.26 → 1114.00] suddenly had a development
[1114.00 → 1115.02] environment
[1115.02 → 1116.36] right in front of them.
[1117.06 → 1117.68] But,
[1117.98 → 1119.10] as I mentioned before,
[1119.64 → 1120.42] the old guard
[1120.42 → 1121.54] didn't necessarily
[1121.54 → 1122.56] feel comfortable
[1122.56 → 1124.18] with how democratic
[1124.18 → 1125.22] things were getting.
[1125.62 → 1127.02] That early antagonism
[1127.02 → 1127.84] of JavaScript,
[1128.46 → 1130.50] I was part of that myself.
[1130.86 → 1132.44] I had the browser extensions
[1132.44 → 1133.26] that would prevent
[1133.26 → 1134.42] JavaScript from running.
[1135.08 → 1136.02] I thought it was
[1136.02 → 1137.96] a useless toy language.
[1137.96 → 1140.06] and I kind of
[1140.06 → 1140.82] had this feeling
[1140.82 → 1141.40] of anger
[1141.40 → 1142.10] whenever I went
[1142.10 → 1143.00] to a web page
[1143.00 → 1144.66] that had JavaScript
[1144.66 → 1146.34] required for some
[1146.34 → 1147.26] critical feature
[1147.26 → 1148.26] of the site.
[1148.82 → 1149.48] I was like,
[1149.56 → 1150.12] you should build
[1150.12 → 1150.72] your website
[1150.72 → 1151.66] the right way
[1151.66 → 1152.70] without JavaScript.
[1153.26 → 1153.92] Soon enough,
[1154.00 → 1154.24] though,
[1154.58 → 1155.20] the beauty
[1155.20 → 1156.32] and the potential
[1156.32 → 1157.32] inherent in
[1157.32 → 1158.00] Brendan Eich's
[1158.00 → 1158.98] 10-day language
[1158.98 → 1160.08] became obvious
[1160.08 → 1160.74] to everyone.
[1161.34 → 1162.08] And now,
[1162.30 → 1163.36] it's conquering
[1163.36 → 1164.58] not just the browser,
[1164.98 → 1165.66] but the server,
[1165.66 → 1166.00] too.
[1166.62 → 1167.50] With Node.js,
[1167.82 → 1169.22] a whole new territory
[1169.22 → 1170.40] for that little language
[1170.40 → 1170.90] that could
[1170.90 → 1172.36] has opened up.
[1172.62 → 1173.74] When I heard that
[1173.74 → 1174.82] JavaScript was going
[1174.82 → 1175.98] to be run on servers,
[1176.44 → 1177.22] I thought,
[1177.44 → 1178.12] why would anyone
[1178.12 → 1179.08] want to do that?
[1179.46 → 1180.48] And at that point,
[1180.50 → 1181.10] I was already
[1181.10 → 1182.38] a JavaScript developer
[1182.38 → 1183.26] professionally.
[1183.60 → 1185.20] I wrote a lot of JS
[1185.20 → 1185.84] every day,
[1186.04 → 1187.28] and I still didn't
[1187.28 → 1188.06] quite see
[1188.06 → 1189.54] why it belonged
[1189.54 → 1190.34] on servers.
[1191.10 → 1192.32] And it's turned out,
[1192.56 → 1193.40] as many listeners
[1193.40 → 1194.10] will know,
[1194.62 → 1195.02] Node.js
[1195.02 → 1196.96] is a huge force
[1196.96 → 1198.14] in the industry now.
[1198.70 → 1199.88] And I think
[1199.88 → 1200.48] there's good reason
[1200.48 → 1200.98] for that.
[1201.54 → 1202.20] One of the things
[1202.20 → 1203.56] that Node.js taps into
[1203.56 → 1204.16] that's made it
[1204.16 → 1204.92] so successful
[1204.92 → 1207.64] is the huge community
[1207.64 → 1209.14] of front-end
[1209.14 → 1210.36] JavaScript developers,
[1210.88 → 1212.20] client-side developers.
[1212.44 → 1213.14] They write code,
[1213.34 → 1214.02] they write JavaScript
[1214.02 → 1214.94] for the browser.
[1215.38 → 1216.26] There are a lot
[1216.26 → 1217.40] of those developers
[1217.40 → 1217.96] out there.
[1218.54 → 1219.32] And by making
[1219.32 → 1220.60] the same programming
[1220.60 → 1221.58] language available
[1221.58 → 1222.96] for writing servers,
[1222.96 → 1223.10] servers,
[1223.54 → 1225.02] they just immediately
[1225.02 → 1226.90] have a huge
[1226.90 → 1228.34] population of people
[1228.34 → 1229.68] who can start
[1229.68 → 1231.08] contributing to servers.
[1231.48 → 1232.76] The tool is already
[1232.76 → 1233.60] in your toolkit,
[1234.12 → 1235.22] and you can simply
[1235.22 → 1235.82] pull it out,
[1236.42 → 1237.34] install Node.js,
[1237.90 → 1238.68] and you're off
[1238.68 → 1239.16] to the races.
[1239.16 → 1242.56] So, first in the browser
[1242.56 → 1243.88] and then on servers,
[1244.58 → 1245.64] JavaScript was this
[1245.64 → 1246.54] unpretentious,
[1246.84 → 1247.96] secretly elegant,
[1248.44 → 1249.56] sometimes buggy,
[1250.00 → 1250.46] language.
[1250.90 → 1251.68] A survivor
[1251.68 → 1252.84] from the browser war
[1252.84 → 1253.80] that everybody
[1253.80 → 1254.68] underestimated.
[1254.68 → 1256.42] JavaScript has been
[1256.42 → 1257.64] kind of Cinderella
[1257.64 → 1258.98] story of programming
[1258.98 → 1259.46] languages,
[1260.00 → 1260.98] starting in that
[1260.98 → 1261.96] early state
[1261.96 → 1263.30] of being
[1263.30 → 1264.30] essentially whipped
[1264.30 → 1265.82] together in 10 days,
[1266.00 → 1266.86] going through a lot
[1266.86 → 1267.46] of derision
[1267.46 → 1268.22] from the rest
[1268.22 → 1268.78] of the programming
[1268.78 → 1269.30] community,
[1269.80 → 1271.10] and still somehow
[1271.10 → 1272.28] continuing to find
[1272.28 → 1273.64] success and growth.
[1274.30 → 1275.44] And then coming
[1275.44 → 1275.96] to the point
[1275.96 → 1276.58] we're at now
[1276.58 → 1277.56] where JavaScript
[1277.56 → 1279.42] is either first
[1279.42 → 1280.34] or second place
[1280.34 → 1281.58] in the most popular
[1281.58 → 1282.50] programming languages
[1282.50 → 1283.10] in the world.
[1283.10 → 1284.28] JavaScript is
[1284.28 → 1285.54] essentially everywhere.
[1286.18 → 1287.22] The ability to run
[1287.22 → 1288.42] inside a web page
[1288.42 → 1289.88] meant that JavaScript
[1289.88 → 1291.22] was as pervasive
[1291.22 → 1292.34] as the web is,
[1292.72 → 1293.86] which is quite pervasive.
[1297.82 → 1298.90] Michael Clayton
[1298.90 → 1299.76] is an engineer
[1299.76 → 1300.66] at Red Hat.
[1302.40 → 1303.52] Did JavaScript
[1303.52 → 1304.40] eat the world?
[1304.94 → 1305.80] Did it ride
[1305.80 → 1306.78] on the coattails
[1306.78 → 1307.40] of the web
[1307.40 → 1308.18] to a kind of
[1308.18 → 1309.34] language domination?
[1309.96 → 1311.36] I wanted to find out
[1311.36 → 1312.16] where the edges
[1312.16 → 1312.92] of JavaScript
[1312.92 → 1313.98] actually are.
[1314.50 → 1315.34] Hi, my name is Clint
[1315.34 → 1315.66] Finley.
[1315.78 → 1316.32] I'm a writer
[1316.32 → 1317.38] for Wired.com.
[1317.60 → 1318.42] Clint was curious
[1318.42 → 1319.40] about the same thing.
[1320.16 → 1321.42] And the more he looked
[1321.42 → 1322.36] at the way JavaScript
[1322.36 → 1323.40] runs today,
[1323.76 → 1325.24] the more he realized
[1325.24 → 1326.58] it's got its fingers
[1326.58 → 1327.60] in every part
[1327.60 → 1329.20] of his online life.
[1330.00 → 1330.88] JavaScript has become
[1330.88 → 1331.64] something that can
[1331.64 → 1333.04] empower entire applications
[1333.04 → 1333.64] before you even
[1333.64 → 1334.06] have a chance
[1334.06 → 1334.96] to decide whether
[1334.96 → 1336.22] you want all of these
[1336.22 → 1337.00] different applications
[1337.00 → 1338.74] to run on your computer.
[1338.86 → 1339.82] They just start running.
[1340.26 → 1340.76] And some of them
[1340.76 → 1341.50] aren't there involved
[1341.50 → 1343.02] with advertising
[1343.02 → 1344.92] or facilitating
[1344.92 → 1346.02] the tracking
[1346.02 → 1347.42] that advertisers use.
[1347.92 → 1349.12] So there's a lot
[1349.12 → 1349.84] of things happening
[1349.84 → 1351.32] invisibly in your browser
[1351.32 → 1352.80] that you might not
[1352.80 → 1354.32] really even know about
[1354.32 → 1355.70] or want to have happened.
[1356.22 → 1357.70] So Clint decided
[1357.70 → 1359.26] to run a little experiment.
[1360.00 → 1361.10] I decided to try
[1361.10 → 1362.58] just using the web
[1362.58 → 1363.30] without JavaScript
[1363.30 → 1364.00] for a while.
[1364.34 → 1365.16] So I decided
[1365.16 → 1365.88] to give it a shot
[1365.88 → 1367.28] and spent a week
[1367.28 → 1368.16] with JavaScript
[1368.16 → 1369.36] disabled in my browser.
[1370.32 → 1371.56] Sounds simple enough.
[1372.12 → 1373.04] But foregoing
[1373.04 → 1373.96] all JavaScript
[1373.96 → 1375.88] had some surprising effects.
[1376.64 → 1377.48] Because JavaScript
[1377.48 → 1379.08] has become so big,
[1379.26 → 1380.40] so all-consuming,
[1380.90 → 1381.64] the language
[1381.64 → 1382.86] famous for being lightweight
[1382.86 → 1384.24] actually takes up
[1384.24 → 1385.44] a lot of space
[1385.44 → 1386.32] and energy now.
[1386.84 → 1387.74] When Clint blocked
[1387.74 → 1389.16] that one language...
[1389.16 → 1389.72] In general,
[1389.88 → 1390.44] it was just
[1390.44 → 1391.90] a much better
[1391.90 → 1392.74] web experience
[1392.74 → 1393.70] in a lot of ways
[1393.70 → 1395.24] in terms of pages
[1395.24 → 1396.04] loading quicker,
[1396.80 → 1397.66] pages being cleaner,
[1398.30 → 1399.00] the battery life
[1399.00 → 1399.52] on my computer
[1399.52 → 1400.32] lasting longer,
[1401.02 → 1402.26] and just having
[1402.26 → 1403.68] more of a sense
[1403.68 → 1404.16] of control
[1404.16 → 1404.70] over what was
[1404.70 → 1405.64] happening on my computer.
[1406.00 → 1406.46] Because there's not
[1406.46 → 1407.02] all of these
[1407.02 → 1407.96] just weird,
[1408.06 → 1408.48] invisible,
[1409.02 → 1409.76] random programs
[1409.76 → 1410.76] running in the background.
[1411.34 → 1412.64] And just imagine
[1412.64 → 1413.44] the bliss
[1413.44 → 1414.38] of living without
[1414.38 → 1415.34] pop-up ads
[1415.34 → 1416.76] for the first time.
[1417.02 → 1417.70] So much of it
[1417.70 → 1418.62] depends on JavaScript
[1418.62 → 1419.94] to even load.
[1420.88 → 1422.08] So web pages
[1422.08 → 1423.16] came out
[1423.16 → 1423.86] a lot simpler,
[1424.46 → 1425.28] fewer ads,
[1425.42 → 1426.12] fewer distractions.
[1426.92 → 1428.22] That clutter-free
[1428.22 → 1429.22] web experience
[1429.22 → 1430.76] isn't the whole picture,
[1430.86 → 1431.06] though.
[1431.72 → 1432.54] Parts of the web
[1432.54 → 1434.06] can't function at all
[1434.06 → 1435.68] if you unplug JavaScript.
[1436.22 → 1436.86] A lot of things
[1436.86 → 1438.24] just didn't work.
[1438.50 → 1439.48] Gmail redirected me,
[1439.58 → 1439.78] I think,
[1439.88 → 1442.40] to a different version
[1442.40 → 1443.02] that's designed
[1443.02 → 1445.12] for old mobile phones.
[1445.70 → 1446.22] Facebook did
[1446.22 → 1447.30] sort of the same thing
[1447.30 → 1449.18] where a lot of the
[1449.18 → 1450.76] smooth interactions
[1450.76 → 1451.44] weren't there.
[1451.44 → 1452.02] where it became
[1452.02 → 1452.84] more like
[1452.84 → 1454.80] a series of web pages.
[1455.94 → 1456.36] So Netflix
[1456.36 → 1457.06] didn't work,
[1457.22 → 1458.10] YouTube didn't work.
[1458.64 → 1458.78] Yeah,
[1458.86 → 1459.70] anything that's
[1459.70 → 1460.32] really heavily
[1460.32 → 1461.56] based on
[1461.56 → 1463.02] interactivity
[1463.02 → 1464.46] just didn't work.
[1464.92 → 1465.40] Ultimately,
[1465.56 → 1467.02] taking JavaScript away,
[1467.52 → 1468.44] there was good and bad,
[1468.50 → 1469.34] and I had to decide
[1469.34 → 1470.48] that it's better
[1470.48 → 1471.22] to have JavaScript
[1471.22 → 1472.28] than to not have it
[1472.28 → 1472.74] at all.
[1474.00 → 1474.94] Clint Finley
[1474.94 → 1475.84] is a staff writer
[1475.84 → 1477.58] for Wired.com.
[1481.80 → 1482.80] Most predict
[1482.80 → 1483.46] that JavaScript
[1483.46 → 1484.84] will only continue
[1484.84 → 1485.62] to dominate
[1485.62 → 1486.86] mobile and desktop
[1486.86 → 1487.74] app development.
[1488.30 → 1489.62] The level of complexity
[1489.62 → 1490.30] possible
[1490.30 → 1491.36] for things like
[1491.36 → 1492.54] browser-based games,
[1492.76 → 1494.10] browser-based art projects,
[1494.48 → 1495.28] et cetera, et cetera,
[1495.36 → 1496.66] is shooting through the roof.
[1497.16 → 1498.32] And the ever-growing
[1498.32 → 1498.84] JavaScript community
[1499.48 → 1500.86] is making the most
[1500.86 → 1501.66] of that potential.
[1501.66 → 1504.70] It's worth taking
[1504.70 → 1505.50] a step back
[1505.50 → 1506.54] and remembering here.
[1507.22 → 1508.42] In 1995,
[1508.92 → 1510.24] just a couple of decades ago,
[1510.86 → 1511.50] Brendan Eich
[1511.50 → 1512.70] was sitting in a room
[1512.70 → 1513.68] hammering out
[1513.68 → 1514.40] a new language.
[1515.02 → 1515.66] And today,
[1516.04 → 1516.80] that language
[1516.80 → 1517.50] permeates
[1517.50 → 1518.72] everything we do.
[1519.32 → 1520.04] It might sound
[1520.04 → 1520.64] a bit cliché
[1520.64 → 1521.30] to say that
[1521.30 → 1522.64] some new string of code
[1522.64 → 1523.24] is going to
[1523.24 → 1524.48] change the world,
[1524.88 → 1525.80] but it does happen.
[1526.46 → 1527.88] A command-line hero
[1527.88 → 1529.14] marshals all their
[1529.14 → 1530.20] love for languages
[1530.20 → 1531.64] into a 10-day
[1531.66 → 1532.44] day sprint.
[1532.98 → 1534.26] And the world's DNA
[1534.26 → 1536.10] is changed forever.
[1539.80 → 1541.34] We can thank JavaScript
[1541.34 → 1542.62] for Google Docs,
[1542.70 → 1543.18] for YouTube,
[1543.58 → 1544.12] for Netflix.
[1544.86 → 1545.88] But, you know,
[1546.30 → 1547.32] with great power
[1547.32 → 1548.84] comes great responsibility.
[1549.70 → 1550.80] And as JavaScript's
[1550.80 → 1551.70] influence continues
[1551.70 → 1552.36] to grow,
[1552.92 → 1553.54] pushed along
[1553.54 → 1555.14] by a huge number
[1555.14 → 1556.64] of open-source libraries,
[1557.16 → 1558.28] that responsibility
[1558.28 → 1559.70] doesn't just lie
[1559.70 → 1560.90] with one person anymore.
[1560.90 → 1562.86] A broader community
[1562.86 → 1564.38] has taken the reins.
[1565.22 → 1565.86] Slash Data
[1565.86 → 1567.14] recently estimated
[1567.14 → 1567.92] the number of
[1567.92 → 1568.92] JavaScript developers
[1568.92 → 1571.46] at 9.7 million.
[1572.18 → 1572.74] And,
[1572.86 → 1573.60] over at GitHub,
[1574.26 → 1575.28] JavaScript has more
[1575.28 → 1576.04] pull requests
[1576.04 → 1577.84] than any other language.
[1578.50 → 1579.34] Power lies
[1579.34 → 1580.50] with the whole world
[1580.50 → 1582.22] of command-line heroes,
[1582.76 → 1584.00] helping JavaScript grow
[1584.00 → 1585.06] as we develop
[1585.06 → 1585.94] our tomorrow.
[1585.94 → 1589.40] next time,
[1589.76 → 1590.90] command-line heroes
[1590.90 → 1591.58] gets caught
[1591.58 → 1592.80] in a web of languages,
[1593.32 → 1594.46] and we'll explore
[1594.46 → 1596.28] how Perl came to thrive
[1596.28 → 1598.08] in a wild new frontier.
[1600.26 → 1601.62] Command-line heroes
[1601.62 → 1603.00] is an original podcast
[1603.00 → 1603.62] from Red Hat.
[1603.62 → 1607.18] By the way,
[1607.50 → 1608.50] a listener shared
[1608.50 → 1609.84] our Hello World episode
[1609.84 → 1610.82] from last season,
[1611.06 → 1612.20] where we also spoke
[1612.20 → 1612.96] about Brendan Eich
[1612.96 → 1613.50] in JavaScript.
[1614.10 → 1614.84] In that one,
[1615.16 → 1615.86] a guest said
[1615.86 → 1617.20] that during those 10 days,
[1617.58 → 1618.34] Brendan probably
[1618.34 → 1619.26] didn't get much,
[1619.36 → 1619.86] if any,
[1620.14 → 1620.48] sleep.
[1621.00 → 1621.56] Well,
[1621.82 → 1622.60] Brendan responded
[1622.60 → 1623.28] on Twitter
[1623.28 → 1624.38] to say he did
[1624.38 → 1625.30] indeed get sleep
[1625.30 → 1626.16] during that sprint.
[1626.86 → 1628.46] To learn even more
[1628.46 → 1629.22] about what happened
[1629.22 → 1630.28] during those 10 days,
[1630.68 → 1631.16] check out the
[1631.16 → 1632.22] Dev Chat Podcast
[1632.22 → 1633.50] interview with Brendan.
[1633.88 → 1634.52] We'll throw a link
[1634.52 → 1635.22] in our show notes.
[1636.20 → 1637.24] I'm Saran ya Barak.
[1637.48 → 1638.44] Until next time,
[1638.72 → 1639.54] keep on coding.
