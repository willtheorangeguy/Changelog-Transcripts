[0.00 → 3.30] I'm Lazio Month and you are listening to The Change Log.
[12.50 → 16.66] Welcome back everyone, this is The Change Log, and I'm your host Adam Stachowiak.
[16.92 → 24.06] This is episode 186 and on today's show we're talking to Lazio Month, also known as Late.
[24.42 → 26.86] He's building the ultimate hacking keyboard.
[26.86 → 31.42] That's right, the ultimate hacking keyboard, also known as UK.
[32.06 → 39.44] We talked all aspects, hardware, software, the open source around it, how it's a platform for hackers to hack on and make it their own.
[39.82 → 46.22] We also had four awesome sponsors, Code ship, Top Tile, Harvest, and also Linde.
[46.94 → 52.30] Our first sponsor is Code ship, and they've got an awesome e-book totally for free for you to download today.
[52.30 → 60.46] Head to resources.codeship.com slash e-books, and you're going to see a book there called Why Containers in Docker Are the Future.
[60.94 → 67.14] Now this e-book is going to help you learn what the differences are between their traditional virtual machine and container stacks.
[67.54 → 71.94] You'll also learn about Docker and its ecosystem and why it's such a big deal.
[72.38 → 76.74] And you'll also learn about Docker and its community and how they're helping to standardize the container workflow.
[76.74 → 81.74] Now you can go to resources.codeship.com slash e-books right now and download this e-book.
[82.16 → 88.04] And I shouldn't tell you this, but when you do that, you're going to get access to three other e-books from Code ship.
[88.52 → 94.32] Diving deep into Docker, continuous delivery, and how to do all this with native Docker support.
[94.86 → 100.22] Head to resources.codeship.com slash e-books and download those e-books right now.
[100.32 → 102.10] Or head to our show notes for the link.
[102.58 → 103.68] And now on to the show.
[103.68 → 116.60] Everyone, I'm here joined today by Lasso Monday, also known as Lacey.
[116.88 → 122.84] And now maybe, Lao, you can describe, because you're Hungarian, how names work for you.
[123.02 → 123.34] Yes.
[123.46 → 128.34] So in Hungary, the first name comes last, and the last name comes first.
[128.34 → 135.04] So in Hungary, I'm Monday Lasso, and in the U.S., I'm Lasso Monday.
[135.20 → 137.08] So which one is actually your first name then?
[138.16 → 138.56] Lasso.
[138.88 → 139.52] Lasso, okay.
[139.84 → 140.00] Yep.
[140.36 → 144.36] But your friends and the Hungarian nickname for you is Lacey.
[145.44 → 146.24] Yep, exactly.
[146.52 → 148.40] And so for this show, I'm going to call you Lacey.
[149.10 → 150.00] Okay, thank you.
[150.18 → 150.78] That's awesome.
[150.86 → 151.30] I like that.
[151.58 → 155.42] Well, you know, we like to be very personal with our guests around here at the Change Law.
[155.42 → 165.68] We love, you know, not just the software you produce and the community that thrives around that software and what gets open sourced and the educations you share.
[165.76 → 167.36] But we also care about our guests.
[167.80 → 173.50] And, you know, one of the things we love most is just kind of diving deep into the past of a guest.
[173.62 → 183.24] Now, maybe to set up the topic at hand, though, is we're going to be talking mainly about this keyboard you've made, this Ultimate Hacking Keyboard is what the name of it is.
[183.24 → 183.56] Yep.
[183.86 → 193.36] And if I can recall correctly, in Change Law Weekly, issue number 36, we linked to a post that you shared on the Top Tile blog called,
[193.46 → 196.74] From the Ground Up, How I Built the Developer's Dream Keyboard.
[196.80 → 198.66] And that was the number one clicked link.
[198.74 → 206.78] And for those out there listening to this show that subscribe to Change Law Weekly, we have sponsored links in there, and they're clearly marked.
[207.22 → 210.76] This was a sponsored link, and it was the number one link in the entire email.
[210.76 → 211.98] So we were pretty stoked about that.
[212.02 → 213.14] What did you think about that?
[213.14 → 214.50] Did you even know about that?
[215.52 → 216.10] Not really.
[216.84 → 224.10] It was crazy because the attention that the post got was way above our expectations.
[224.60 → 234.44] And it got reposted in various sites, and it gave us about 2,000 subscribers.
[234.44 → 242.14] And when we talk about some days, too, for that post, that post was posted on, let's see if I can see the date here.
[243.90 → 250.52] I can't tell a date, but I know that ChangeLog36 came out around the same time of that post.
[250.52 → 254.56] And that was in January 17th of this year.
[254.72 → 257.76] So all year long, you've been working hard at this.
[258.02 → 262.52] You wrote that blog post on the Top Tile blog, and you're also part of the Top Tile network.
[262.68 → 267.24] So Gooding here a little bit, a little disclosure to you and the listeners.
[268.04 → 271.50] Top Tile has been a sponsor of this show for many years now.
[272.06 → 273.12] They love what we do here.
[273.16 → 277.66] They support almost every single show, but we have a deep partnership with Top Tile.
[277.66 → 281.44] And they're actually sponsoring this show in particular just by happenstance.
[281.54 → 285.34] They didn't even know that you were coming on the show, but you're also part of the Top Tile network.
[285.68 → 288.58] Can you speak a little bit about your experience so far at Top Tile?
[289.58 → 293.86] So I went through their interview process and became part of the network.
[294.08 → 296.66] I haven't yet worked through Top Tile.
[297.28 → 303.10] I created a couple of blog posts on their blog.
[303.10 → 306.32] And this was the most popular so far.
[306.32 → 311.74] So I was talking to Anna, who is also a Top Tile member.
[312.26 → 317.86] And she mentioned me that I should really write a blog post to the Top Tile blog.
[318.26 → 325.18] And for what I gathered, I've talked to Brennan Bene shat, the co-founder and CTO or COO, as a matter of fact.
[325.28 → 326.08] And you probably know Brennan.
[326.30 → 326.48] Yep.
[326.48 → 334.22] But part of the Top Tile network isn't just about helping developers get plugged into actual paying gigs where you're getting projects.
[334.22 → 338.82] It's also becoming a part of this worldwide developer network.
[338.82 → 347.98] And I really don't want to make this an ad for them, but I think this is fascinating because this is a chance for us to talk to and Top Tile or are here on the show.
[347.98 → 354.78] And share a bit about what their process is and kind of how you stepped into that.
[355.20 → 358.24] And while you may not have taken on any engagements, you've blogged.
[358.46 → 364.42] And as you'd mentioned, this particular blog post that we covered in Change Law Weekly, issue 36, was huge for you.
[364.54 → 366.96] So what was the ramifications?
[366.96 → 370.20] What came from that initial blog post about this project?
[371.06 → 375.40] Well, what do you mean by saying ramifications?
[375.92 → 378.92] Well, when I say like what was the ripple effect?
[379.00 → 380.22] So you posted the blog post.
[380.36 → 381.34] We obviously covered it.
[382.32 → 386.20] Who else found interest in this post and was like, wow, this is fascinating?
[387.00 → 387.26] Okay.
[388.10 → 394.40] So this post got featured on the blog.
[394.40 → 403.26] And then I think the blog has, the Top Tile blog has 7,000 subscribers or viewers.
[403.62 → 405.54] So it got huge attention.
[407.42 → 411.44] And if you see at the end of the post, there are dozens of comments.
[412.26 → 422.58] And then it got reposted on, there is a site, java.dzone.com, where it received a huge attention again.
[422.58 → 428.82] And then I sent it to Slashdot, where it got featured on the main page.
[428.82 → 429.10] Wow.
[429.46 → 432.78] So it was a huge ripple effect for sure.
[433.00 → 435.88] And it helped us tremendously.
[436.64 → 441.74] And we got our 2,000 subscribers just based on this one post.
[441.74 → 448.64] Now, as our listeners know, we do like to dive a little deeper into the past and history of our guests.
[449.42 → 452.48] And like I said, this Ultimate Hacking Keyboard is the main topic.
[452.54 → 456.86] I got a couple more questions that kind of, you know, kind of tee that up a bit.
[456.94 → 460.24] But we are going to dive deeper into you're past a bit and find out where you came from.
[460.24 → 465.52] But if I go back to this blog post, and listeners will have this in the show notes for the show.
[465.66 → 467.62] So as you know, go ahead and head there.
[467.70 → 473.00] Look for the post from the ground up, how I built the developer's keyboard or dream keyboard.
[473.22 → 475.46] And you'll see the post we're talking about if you want to follow along.
[475.54 → 478.62] But if I look through this post, it's talking about Arduino.
[479.48 → 484.50] And the look of the keyboard that's being shown here is different from the look of the keyboard.
[484.66 → 487.74] Now, what stage was this keyboard in?
[487.74 → 490.26] And what was the stage of the project when this post went out?
[490.30 → 490.86] Was it early?
[491.00 → 493.12] Was it still not quite where it's at today?
[494.50 → 502.52] Yeah, I guess that was our third generation prototype that we featured in that post.
[503.28 → 508.82] And back then, the two keyboard halves were connected by a retractable cable,
[509.32 → 514.30] which had a totally different look than the current cord cable.
[514.30 → 517.20] It's like a telephone cord right now, shorter.
[518.46 → 519.36] The spiral cable.
[519.94 → 520.44] Yep, yep.
[520.72 → 520.92] Yeah.
[521.30 → 522.28] I kind of like that better.
[522.44 → 523.16] I can imagine.
[523.24 → 527.62] I haven't touched it yet to know, but I feel like that's a better kind of cable.
[528.24 → 528.68] Absolutely.
[529.06 → 531.08] Which is why I asked you that, because it does look a lot different.
[531.82 → 532.12] Yeah.
[532.68 → 539.10] So those retractable cables failed on us like there is no tomorrow.
[539.78 → 540.00] Right.
[540.00 → 543.08] Those were super unreliable.
[543.50 → 549.76] And the funny thing is that there is a manufacturer on the market who says they keep their keyboards
[549.76 → 551.60] with that cable.
[552.40 → 557.64] And some customers complain that it's unreliable.
[557.64 → 573.88] And because we had so many iterations with their prototype, we were able to throw that cable and use another one that is actually reliable.
[573.88 → 577.70] So we won't have complaints later on.
[578.06 → 578.18] Gotcha.
[578.80 → 585.72] Well, Late, I mean, I think the listeners have got enough so far to understand that English might not be your native language,
[585.72 → 587.10] your first speaking language.
[587.54 → 587.94] Yep.
[587.94 → 591.06] And I find it very interesting.
[591.20 → 597.76] Like the last show we had, episode 185, if I recall correctly.
[597.90 → 599.20] Let me go back to my notes real quick.
[600.02 → 605.78] We talked to Ahmad Masri, who is from Syria originally.
[605.88 → 613.58] And he had this really rich story of how he came to software, how using the Internet was illegal in Syria.
[613.58 → 617.68] But yet he found and others found a way around hurdles.
[618.52 → 624.30] And you can take that same conversation we had in the last show and take it back to Mitchell Hashimoto
[624.30 → 628.52] and several other guests we've had that have been influential software developers that come on the show.
[629.76 → 632.56] Maybe I teed that up in a good way, maybe a bad way.
[632.60 → 634.50] But what is it about your history?
[634.58 → 635.60] You're from Hungary.
[636.08 → 639.90] What can you share about where you came from to get to being a software developer?
[640.04 → 641.68] Where should we start with that?
[641.68 → 647.22] Well, I got my first computer in the age of six.
[647.82 → 649.82] It was a Commodore 64.
[650.88 → 654.44] And from that point, there was no going back.
[655.74 → 660.72] So I guess I'm just the geeky type who likes to tinker.
[662.08 → 665.72] And programming pretty much allows this.
[666.36 → 670.00] You can break down problems and solve them.
[670.00 → 675.64] And it just makes sense to me, and it's attractive to me.
[677.08 → 679.80] And later I got my first PC.
[680.68 → 689.14] And around the year 2000, broadband internet access became widespread in Hungary.
[689.14 → 693.72] And I got into web programming.
[693.72 → 699.86] And over the years I used many languages.
[700.02 → 704.30] Java, .NET, Python, JavaScript, Bar shell.
[704.30 → 710.78] And I wrote all kinds of applications.
[711.44 → 714.10] GUI, command line, client, server.
[714.72 → 717.78] And lately programming microcontrollers.
[718.06 → 721.98] And understanding the various layers of the software stack.
[722.38 → 724.94] And I guess I'm pretty much full stack.
[724.94 → 727.00] Pretty much full stack.
[727.06 → 727.58] I would think so.
[727.66 → 733.98] I mean, here in all the languages and things you've messed with, that's definitely full stack.
[734.04 → 737.66] And I think it depends on who you talk to, what full stack means.
[737.72 → 744.76] I would actually probably label you polyglot more than full stack, even though full stack is a better, probably totally accurate.
[744.76 → 755.42] I think full stack is sometimes used to describe somebody on the web, potentially, that's, you know, backend, database, you know, ops, frontend, design even.
[757.16 → 758.92] But maybe polyglot.
[758.98 → 759.96] What do you think about polyglot?
[760.62 → 765.58] Yeah, I think it's a better term in my case.
[765.58 → 775.72] Because it's not only, the UHC is not only about programming, but also about designing hardware and soldering microcontrollers on the circuit board.
[776.06 → 779.50] So, yeah, polyglot is a better term, I believe.
[780.24 → 790.82] So, whenever you look at a problem, and that problem involves design, software, how do you first think about it?
[790.82 → 800.28] Do you think, how do you reverse engineer a problem to say, this is the language I would use, and I would use this feature, this feature, and this feature?
[800.84 → 803.26] How do you approach some of the things you've done here?
[803.26 → 807.86] Or maybe even some of the first problems you had whenever you were first learning a program?
[809.82 → 810.36] Oh, Geez.
[810.54 → 811.92] It was such a long time ago.
[813.04 → 815.74] We have so much more opportunities right now.
[815.74 → 823.82] Nowadays, I use JavaScript whenever possible, because it's so easy to prototype stuff in JavaScript.
[825.04 → 844.78] But, well, back then I used Basic for the Commodore, and learned C, and then scripting languages, and realized how much easier it is to achieve to solve problems in scripting languages.
[844.78 → 847.10] It's a pretty general question.
[847.56 → 847.88] Yes.
[848.08 → 849.64] And then I'm sure how to answer it.
[849.96 → 856.26] Well, I think from the polyglot standpoint, you know, whenever, okay, let's maybe, instead of going back in the past, let's stay to now.
[856.26 → 875.22] Or in the last few years, whenever, as a polyglot, when you look at a problem, what are, you know, how do you, you know, for those out there who may not know what a polyglot is, or have an idea, want to be one, which is someone who loves and knows many languages, and can look at a problem agnostically and say, well, I'd use this language for this problem, or I would use that for that.
[875.22 → 876.98] How do you think about things like that?
[878.40 → 889.30] Yeah, I guess lately I had to learn so, so, so much stuff that I ended up using mainly JavaScript.
[889.30 → 890.30] Yeah.
[890.30 → 893.16] So JavaScript is your thing now?
[893.16 → 894.16] Yep.
[894.16 → 895.16] Yep.
[895.16 → 915.64] Because earlier I used Python for certain purposes, and then Node became widespread, and the whole library, JavaScript library ecosystem got so rich that I realized that I can solve almost any problem that I encounter with JavaScript.
[915.64 → 919.64] And I adapted it as my number one language.
[919.64 → 930.64] Earlier, I used PHP and Python for many of those tasks, but nowadays, it's mostly JavaScript for sure, and C for microcontroller programming.
[930.64 → 931.64] Yep.
[931.64 → 952.76] So maybe I'm not the best guy to answer these questions because I just had to learn way too much stuff lately, and I had a lot of things on my brain, and I have to focus on one language.
[952.76 → 953.76] Gotcha.
[953.76 → 954.76] Gotcha.
[954.76 → 962.26] Well, when it comes to, I guess, some history, what was, you know, you mentioned the Commodore 64, and you mentioned the PC.
[962.26 → 974.96] Can you remember some of the very first substantial things you've done that were, like, that played a pivotal role into either you're building the UK keyboard?
[975.58 → 985.60] Like, what was it that was pivotal earlier in your life that is a, you know, a fun story that you can tell that's about how you got to where you're at today?
[986.76 → 987.32] Wow.
[987.32 → 994.48] Could be an influencer, could be, you know, a particular project, maybe some client work.
[994.62 → 1000.38] What was it that got you, you know, prepared to be the person behind this awesome keyboard?
[1001.32 → 1005.72] It's so hard to pick a single experience.
[1007.12 → 1007.70] Tell many.
[1007.70 → 1024.50] Yeah, so, for example, I was working on a government system for a client, and for that I use PHP and Qualified, so to speak, a major UI component.
[1025.50 → 1027.48] That was a filter table.
[1027.48 → 1033.12] And then I was working on a startup as a co-founder.
[1034.18 → 1036.28] It was called One Layer.
[1037.06 → 1039.64] And so it worked like you logged in.
[1039.98 → 1045.10] It was a web 2.0 site, if I can use that term, because it's a web 2.0 term.
[1045.10 → 1045.54] Yeah.
[1046.44 → 1051.48] So the way it worked, you logged in, and you searched for songs.
[1052.08 → 1059.40] And you added the song of your choice to your playing, to your wish list.
[1059.40 → 1065.56] And then the system was listening to about 100 radio stations.
[1066.26 → 1075.40] And as soon as on one of those stations it encountered with a song on your playlist, it recorded it.
[1076.52 → 1080.26] And so you could play it back or download it in your browser.
[1080.68 → 1084.92] So this was a pretty cool and fancy web application.
[1085.86 → 1086.16] Gotcha.
[1086.16 → 1094.30] And as I understand it, kind of fast-forwarding a little bit closer to today in preparation for all this happening,
[1094.60 → 1098.96] and I guess to tee up prior to the break, we got about three or four minutes before the next break.
[1099.66 → 1102.44] But just to tee up the next conversation and maybe prime it a little bit,
[1104.56 → 1109.86] the UK, the Ultimate Hacking Keyboard, has not a Kickstarter.
[1109.86 → 1116.48] It's something different that I haven't personally heard of until I went to this one, which is Crowd Supply.
[1116.58 → 1120.32] So if you go to CrowdSupply.com, it's similar to Kickstarter.
[1120.46 → 1127.08] I don't know, why did you choose Crowd Supply over something else to, in quotes, kickstart this thing?
[1127.08 → 1135.52] Yeah, so the two major crowdfunding sites are Kickstarter and Indiegogo.
[1136.04 → 1143.50] And about two years ago, we were contacted by Indiegogo and Crowd Supply independently.
[1143.50 → 1155.50] And initially, I was hesitant to choose one over the other, but I guess Crowd Supply better appeals to the geeky type.
[1155.50 → 1167.48] If you take a look at their campaigns, there are many developer-related projects, like hardware projects and developer boards.
[1167.48 → 1176.28] And I think these products appeal to our type, to our kind.
[1176.86 → 1187.76] And they not only do the crowdfunding stage, but they can also help you in PR and in contacting manufacturers.
[1188.72 → 1192.44] And yep, they do all this extra.
[1192.62 → 1194.48] So Crowd Supply is a little different from Kickstarter.
[1194.48 → 1196.46] I never really looked into the details.
[1196.74 → 1200.78] Like, I almost imagine that you're in charge of your own Kickstarter.
[1200.98 → 1205.86] It's essentially a platform for bringing, you know, the interests of the masses.
[1205.86 → 1211.30] But it's up to you to build out your page, do a video, source materials.
[1211.94 → 1214.48] So this seems like it's a little bit more...
[1215.60 → 1219.22] Here in America, we have a show that you probably watch yourself.
[1219.88 → 1220.92] It's called Shark Tank.
[1220.92 → 1226.74] And it almost reminds me a little bit of that, where if you work with a shark, which is what they're called in the show,
[1227.30 → 1230.34] then they bring their own attributes to help you get to your goals.
[1230.46 → 1235.68] So not only do they bring, you know, buying into equity with funding or whatever,
[1235.76 → 1237.96] they'll bring in licensing partners.
[1237.96 → 1239.52] They'll bring in retail manufacturers.
[1239.52 → 1243.32] They'll bring in distribution, you know, operators they've been working with for years.
[1243.32 → 1251.24] So is this similar with Crowd Supply, where, you know, not only are you hosting your fundraising campaign on there,
[1251.24 → 1253.74] but they're also helping you in other ways too?
[1255.08 → 1255.38] Yep.
[1255.44 → 1257.18] They are able to, if you ask them.
[1257.40 → 1257.60] Okay.
[1258.42 → 1258.60] Yep.
[1258.82 → 1259.18] Absolutely.
[1259.54 → 1261.10] Does that mean they take a bigger piece of the pie?
[1261.20 → 1265.74] Or does that mean that's just an à la carte feature that you could just use if you want to or don't?
[1265.74 → 1276.98] Well, I'm not actually sure what's the deal is regarding the extra services like contacting manufacturers,
[1277.22 → 1285.26] because in all honesty, we didn't use that feature because we built up the connections with manufacturers.
[1285.66 → 1287.10] You already had your own contacts then?
[1287.80 → 1288.04] Yep.
[1288.32 → 1288.52] Good.
[1288.52 → 1288.62] Good.
[1289.62 → 1298.70] Yeah, but it's pretty interesting about crowdfunding that many people think that Kickstarter or Indiegogo
[1298.70 → 1302.08] is a way better platform because they are a better known.
[1302.90 → 1307.28] And the truth is that really you had to bring the people to the site.
[1307.94 → 1317.86] So prior to launching our campaign, we were proactively working on developing this subscriber base,
[1317.86 → 1320.88] collecting all these peoples via our site.
[1322.08 → 1328.90] So if you don't do that, then you won't be able to make your campaign a success.
[1329.78 → 1332.36] Well, I'm glad you mentioned campaign because that was next on my list.
[1332.48 → 1337.92] Before we go into this break is there's a campaign, as you can guess, on Crowd Supply,
[1337.98 → 1341.80] because as we've been talking about here, the campaign's name is Ultimate Hacking Keyboards.
[1341.92 → 1344.04] If you're going there and searching, feel free to.
[1344.04 → 1348.62] But we're going to put the link to the campaign show page in our show notes.
[1348.62 → 1356.50] And right now, before we go into the break, you are 104% funded, which means you don't really need the help of this show,
[1356.68 → 1359.28] which the funding ends this Sunday.
[1360.14 → 1367.16] So we're recording this on December 9th around mid-afternoon here in U.S. Central Standard Time.
[1367.16 → 1372.14] And we'll have it edited and live on Friday morning.
[1372.30 → 1377.42] So if you're listening to this, it's either Friday, Saturday, Sunday, or later, obviously.
[1377.72 → 1384.16] But if you're listening to this now, and now for you is December 11th, December 12th, or December 13th,
[1385.10 → 1389.38] if this is an interesting topic to you, you can go to the URL we'll have in our show notes
[1389.38 → 1396.48] and commit some support to this project at whatever level, and we'll talk more detail about those levels.
[1396.76 → 1403.42] So I always find it interesting to have these kinds of conversations on this show
[1403.42 → 1406.56] because it's sort of two parts.
[1406.78 → 1410.82] And in some ways, if Jared was on the show today, which he's not, he had some things going on, by the way.
[1411.32 → 1412.82] So that's why it's just me on the show.
[1412.82 → 1420.28] But in some ways, we don't really want to be the show where we have funding things on this show
[1420.28 → 1421.92] because we kind of feel spammy in a way.
[1422.42 → 1425.02] But there's so much open source you're doing behind this,
[1425.02 → 1430.16] and it's such a core component to being a hacker to have the ultimate hacking keyboard.
[1430.26 → 1432.86] It only made sense to have this conversation.
[1433.44 → 1437.42] So this is the last time I'm going to really press the issue of going there and checking it out.
[1437.46 → 1439.32] And if you want to fund it, then you can.
[1439.52 → 1441.92] So as I said today, we're recording it on the 9th.
[1441.92 → 1446.10] And the campaign ends on the 13th, which is December 13th.
[1446.12 → 1449.86] So if you're listening to this between the 11th, 12th, and 13th, you still have time.
[1450.02 → 1453.80] After that, maybe before the closing break, you can tell the listeners
[1453.80 → 1457.18] if they're listening to it on the 14th, 15th, 16th, or beyond,
[1457.82 → 1463.38] what can they do after the funding is over to kind of hop in and take part and support this?
[1464.66 → 1464.98] Yes.
[1465.14 → 1468.40] So while you're crying, we will take pre-orders.
[1468.40 → 1472.30] So right now, a keyboard costs $200.
[1473.30 → 1480.92] And beginning from the 15th, it will cost $220.
[1481.12 → 1485.70] A little bit more expensive, but still cheaper than after the shipping,
[1486.70 → 1490.82] which will happen on the July of the next year.
[1490.82 → 1491.26] Gotcha.
[1492.36 → 1497.80] And then also to mention, on that note, if people are going there now to support it,
[1498.38 → 1503.34] you're shipping potentially, what, mid to end of 2016?
[1503.64 → 1506.02] So it's the end of 2015 now.
[1506.08 → 1509.16] So it's almost a year turnaround until someone might have this in their hands.
[1509.30 → 1511.34] Is that roughly your estimate?
[1512.36 → 1514.20] Well, it will happen in July.
[1514.60 → 1514.88] Okay.
[1515.02 → 1515.06] Shipping.
[1515.56 → 1515.76] Yep.
[1516.14 → 1518.82] So July 2016 is when shipping kicks off.
[1518.82 → 1519.82] Exactly.
[1520.14 → 1520.34] Yep.
[1520.54 → 1520.76] Good.
[1521.14 → 1522.10] Well, all right.
[1522.56 → 1524.36] Lots of that takes us into our first break.
[1524.44 → 1525.80] So let's take a quick break.
[1526.30 → 1529.28] When we come back, we're going to dive a lot deeper into the UK.
[1529.42 → 1531.44] What it is, the software behind it,
[1531.56 → 1535.08] what it takes to actually make hardware and software meld together.
[1535.96 → 1537.70] This has been a labour of love for Lacey,
[1537.78 → 1539.00] so I'm sure we've got lots to cover.
[1539.18 → 1541.86] But for now, let's break real quick here from a sponsor,
[1542.08 → 1542.84] and we'll be right back.
[1542.84 → 1551.26] Total is by far the best place to work as a freelance software developer right here on today's show.
[1551.74 → 1554.52] Lacey and I talked about his experience at Total
[1554.52 → 1558.54] and how he's enjoyed being a part of a global network of engineers
[1558.54 → 1562.04] and the impact that has had on the ultimate hacking keyboard.
[1562.04 → 1564.54] If you're freelancing right now as a software developer
[1564.54 → 1568.48] and you're looking for a way to work with top clients on products that are interesting to you,
[1568.90 → 1572.06] challenging, and using technologies you want to use,
[1572.52 → 1574.18] Total might just be the place for you.
[1574.78 → 1580.56] Also, a new perk to mention is being able to apply for a grant to work on open source of your choice
[1580.56 → 1584.22] so you can take a break from client engagements and give back to open source
[1584.22 → 1586.50] with the financial help of Total.
[1586.50 → 1592.48] Now, if you want a personal introduction, reach out to me, Adam at changelog.com,
[1592.52 → 1596.72] and I will gladly put you in touch with the right people at Total.
[1597.02 → 1600.34] Otherwise, head to toptal.com slash developers to learn more
[1600.34 → 1602.08] and tell them that Changelog sent you.
[1605.22 → 1608.34] All right, we're back with Lacey.
[1608.54 → 1613.04] So, you know, Lacey, I'm just so excited about the conversation coming up
[1613.04 → 1615.98] because we're diving deep into the ultimate hacking keyboard.
[1615.98 → 1620.66] Now, I'm going to preface this next two parts of the show with the fact that
[1620.66 → 1624.84] I've personally never thought about using something like this.
[1624.92 → 1631.18] Now, I'm primarily a front-end guy, designer, user experience, fluent in SaaS, HTML, JavaScript,
[1631.30 → 1634.00] those kinds of things, but more on front-end web development.
[1634.20 → 1637.08] So I've never really thought about personally using one of these.
[1637.52 → 1640.50] And I know Jared uses a similar keyboard.
[1640.62 → 1644.60] It's more for ergonomics, not for re-key mapping and like totally hacking this keyboard.
[1644.60 → 1652.10] But I'm kind of curious if you can share where this idea came from for you.
[1652.18 → 1656.56] Like what made you think, man, I need to make a keyboard that's totally for hackers?
[1656.56 → 1662.08] Yeah, so it was back in the August 2007.
[1662.82 → 1668.18] And I noticed moving my hands between the various blocks of the keyboard.
[1668.74 → 1678.56] Like there is the alphanumeric block and there are the F keys and the navigation block and the jumped.
[1678.56 → 1686.84] And I thought that it would be great if I could stay on the home row and never leave it.
[1687.80 → 1697.10] And of course, it's possible with various editors like for like VI, but you aren't always in VI.
[1697.10 → 1703.92] And I wanted to stay on the home row in a universal manner in every application.
[1705.12 → 1708.20] So that was a major design principle.
[1709.22 → 1721.84] The other thing was I wanted it to be a split keyboard because I noticed my hand in this rather uncomfortable posture close to each other.
[1721.84 → 1730.54] And I thought that it would be great if I could just separate the keyboard halves and position and orient them in any way I want.
[1731.22 → 1737.78] And I also wanted to make it in a way that the two halves can be attached as one.
[1739.06 → 1744.02] And so it's super compact for transportation purposes.
[1744.02 → 1755.82] So I came up with this idea and became super excited about it and created a Linux user.
[1756.54 → 1767.02] And I created an GOODMAN keyboard, which is basically there are these files, these GOODMAN files that you can write.
[1767.02 → 1771.38] And they contain various keyboard mappings.
[1771.92 → 1780.96] And I configured my software mapping in a way that I pressed the Windows key along with JK LI.
[1781.62 → 1785.20] And it mapped to left, right, up, down.
[1785.34 → 1793.32] So I created the navigation block in the JK LI keys.
[1793.32 → 1799.32] And I mapped other keys like page up, page down, home, and to that region.
[1799.98 → 1803.80] And this way I didn't have to move my hand, only my fingers.
[1804.94 → 1818.74] But it wasn't ideal because for switching between these layers that is reaching the navigation function via the Windows key, it wasn't really comfortable.
[1818.74 → 1823.50] And I was thinking how to make it more comfortable.
[1823.50 → 1833.40] And I realized that if space is split, then one part of it, one side of it, can be used as space.
[1833.70 → 1837.22] And the other can be used as a layer switcher key, so to speak.
[1837.22 → 1844.82] So on the UH key, the right space is this space, actually, and the left space is the MUD key.
[1845.14 → 1848.92] And if you keep MUD, this is a layer switcher key.
[1848.92 → 1859.08] If you keep it pressed, then JK LI will trigger left, down, right, up.
[1859.70 → 1867.00] And the way H becomes page up and page down, and 7 becomes F7.
[1867.00 → 1876.80] So you basically map every key outside the alphanumeric block to the alphanumeric block with the MOD layer.
[1877.34 → 1880.06] To paint the picture, we mentioned that it breaks apart.
[1880.26 → 1883.12] So at the middle of the keyboard, I'm not sure which exactly.
[1883.20 → 1883.90] I got a picture up here.
[1883.94 → 1886.46] Let me go over real quick so I can reference this.
[1886.46 → 1902.54] But basically, if you're looking at your typical keyboard from the number row down to the space bar row, you got 6, T, G, B, and what is normally a space bar, which is actually split between a MOD key and a space key on either side.
[1902.90 → 1904.60] That's where the keyboard splits.
[1905.34 → 1906.70] And that's on the left-hand side.
[1906.76 → 1912.70] On the right-hand side, you got, again, from the number row down to the space, you got 7, Y, H, N.
[1912.78 → 1915.72] And what's typically the space bar, that's on the right-hand side.
[1915.72 → 1922.50] So at that point in the keyboard, if you're looking at your own keyboard right now, that's where you can see the split that Lacey is talking about.
[1922.90 → 1929.72] And so I just wanted to paint that picture up because you're describing it to kind of paint that picture for the listeners because this is not a visual.
[1930.66 → 1930.78] Sure.
[1931.08 → 1931.40] Okay.
[1931.96 → 1935.68] So the keyboard is split according to touch typing rules.
[1936.50 → 1943.26] So if you do correct touch typing, then you should be comfortable and not reach over to the other keyboard half.
[1943.26 → 1947.82] Which means the J key and the F key has got that little knobby that you can kind of feel with your pointer finger.
[1948.76 → 1949.04] Yep.
[1949.24 → 1949.44] Yep.
[1949.60 → 1949.78] Okay.
[1949.78 → 1966.84] And the six key is always a subject of debate because in the U.S., U.S. people are trained to press the six key with their right hand.
[1966.84 → 1975.98] But for various parts of the world, for example, in Hungary, we are trained to press it with the left finger.
[1976.40 → 1980.38] I guess I really thought about what hand I used to press the six key.
[1981.64 → 1984.86] I guess maybe I just did a little test here as I was listening to you.
[1984.92 → 1988.32] I'm thinking I would probably go with either.
[1988.48 → 1988.76] I don't know.
[1988.76 → 1990.24] I guess it depends on how my brain feels.
[1990.30 → 1993.88] I never really thought that there's a particular pattern that's already existing there.
[1994.68 → 2000.48] So the reason the six key is on the left half is because of symmetry.
[2000.94 → 2003.60] Because the keyboard is more symmetrical this way.
[2004.02 → 2004.30] Right.
[2004.40 → 2005.74] So this is the reason.
[2005.74 → 2015.42] So there is the base layer that features HJKL and the other keys.
[2015.54 → 2016.70] And there is the mod layer.
[2016.88 → 2025.70] If you keep the mod key pressed, then this becomes left, down, right, and all the other navigation keys.
[2025.70 → 2030.42] And there is the mouse key that is in the place of caps lock.
[2030.66 → 2036.58] And if you keep it pressed, then JK LI will move the mouse pointer.
[2037.28 → 2046.74] And this works without installing any special drivers because the keyboard exposes standard USB descriptors towards the host.
[2047.78 → 2050.24] And then there is the FN layer.
[2050.78 → 2052.56] You are all familiar with the FN key.
[2052.56 → 2060.76] And it has various MIDI shortcuts like volume up, volume down, and all these kinds of stuff.
[2060.94 → 2070.18] So there are these four layers that makes you access all the functionality of the standard keyboard and more.
[2070.66 → 2073.14] I do want to dive into that because there are four layers.
[2073.36 → 2075.90] And even the mouse that you'll probably dive into as well.
[2076.04 → 2079.18] Like even the mouse you can tap into and kind of remap.
[2079.26 → 2081.08] We have some questions specifically around that.
[2082.56 → 2085.14] And I also noticed as you're describing it.
[2085.62 → 2091.58] So for the listeners out there, we'll put some links in the show notes that you can kind of watch along.
[2091.66 → 2093.34] Because this is not a video podcast.
[2093.56 → 2094.68] It's an audio podcast.
[2094.68 → 2096.28] As you can tell, you've been listening for years.
[2096.64 → 2100.48] But nonetheless, we'll put some show notes in there for links out to images.
[2100.68 → 2105.90] And if you're following along, Lace, on the left-hand side, when we talk about the brick of the keyboard,
[2105.90 → 2107.92] we have a mod key and a space key.
[2107.92 → 2112.32] So typically where the space key is, on the left-hand side, there's a mod key.
[2112.66 → 2118.84] And beneath that is this extra, which is typically like this outer boundary of the keyboard that's not used,
[2119.28 → 2120.24] which is a space key.
[2120.64 → 2125.80] And on the right-hand side, you have the space key and then the mod key, which is alternated.
[2125.98 → 2126.14] Why?
[2127.52 → 2129.06] What's the alternation there?
[2129.06 → 2132.06] Is it that you can kind of set...
[2132.72 → 2135.32] I don't know, because this can be completely remapped.
[2135.40 → 2136.38] It could be your own keyboard.
[2136.50 → 2137.46] No keyboard is the same.
[2137.56 → 2139.94] You can move your settings around as you want to, which we'll talk about, I'm sure.
[2140.06 → 2146.80] But it seems like, you know, why would you have the mod key and the space key be alternated on either side?
[2146.80 → 2147.08] Okay.
[2147.62 → 2156.50] So the guiding principle is that every modifier key should be featured both on the left and the right side.
[2156.50 → 2162.86] Because in order to access various shortcuts, it's just comfortable.
[2162.86 → 2174.60] So just this way, the mod and space is accessible by both hands, but in a diagonal manner.
[2175.44 → 2186.10] Because if you use the UK for a week, then you will fire your brain to use this layout or your own layout, if you so choose.
[2186.10 → 2193.84] And most of the time, you won't have to use the case buttons that you mentioned.
[2194.48 → 2198.44] And the case buttons exist simply because it's easy.
[2198.82 → 2202.40] They are easy to reach by our thumbs.
[2202.98 → 2204.72] So there is a large amount of space there.
[2205.56 → 2209.10] And this way, you could make the layout symmetrical.
[2210.06 → 2214.34] I mean, feature the modifiers on both sides.
[2214.34 → 2214.82] Gotcha.
[2214.82 → 2214.90] Gotcha.
[2215.70 → 2217.30] We got a little ahead of ourselves.
[2217.42 → 2221.90] I wanted to dive that deep a little bit later on, but that's okay.
[2222.66 → 2232.82] What I'm looking for at this point is to kind of escalate this conversation over the next 20 or so or 30 or so minutes.
[2232.82 → 2240.98] Is to figure out what was going on in your brain, in your mind, in your day-to-day life as a software developer.
[2240.98 → 2245.74] What made you be like, man, this, you know, because there's mechanical keyboards out there.
[2245.94 → 2248.16] You know, there's ergonomic keyboards out there.
[2248.16 → 2257.26] Why did you not like what was currently available on the market, whether it's open source, not open source, crowdfunded or not?
[2257.26 → 2271.06] What problems were you hitting as a software developer that was like, I've got to make this UK, even if it was back in 2007, which is, you know, almost eight years now, more than a little over eight years now since this problem has been existing for you.
[2271.06 → 2276.82] What, what were you hitting, what happened to make you think I need to build something that's much better for developers?
[2276.82 → 2283.10] So, two keywords are productivity and economy.
[2283.94 → 2297.84] So, if you, if I don't have to move my, my hands, it's, in my mind, this is great because really all this started from, for me moving my hands across the various blocks.
[2297.84 → 2317.96] And it's, if you, if you use a dedicated mouse, it's also much easier to access it this way because there is a the distance is shorter between the keyboard and the mouse because there is no navigation block and a jumped.
[2317.96 → 2328.58] And the other thing, the economy, the economy is, it just, it's so much more comfortable to orient keyboard halves.
[2329.06 → 2347.70] You can even, you can even use it in Shudder with this whole, this whole design, this compact, truly split design that merges as one and reconfigurable, this whole concept, these features just made sense as a software developer, not moving my hand.
[2347.96 → 2353.00] Hence, holding my finger or being able to reposition my, the keyboard halves.
[2353.90 → 2354.20] Gotcha.
[2354.76 → 2372.18] So, obviously ergonomic keyboard made sense, even mechanical keyboard made sense, but the, the lacking of the remapping, the lacking of the open source underlying software, whether it's a CAD drawing, whether it's the, the JavaScript agent, various things we'll talk about.
[2372.56 → 2375.00] These things were something that you wanted to bring to fruition.
[2375.00 → 2375.60] Mm-hmm.
[2375.80 → 2381.00] So, what were the, the, I guess I didn't understand fully your question.
[2381.10 → 2381.54] Could you please?
[2381.94 → 2382.90] Well, it wasn't really a question.
[2382.98 → 2386.46] It was more like a statement priming you to, to chime in.
[2386.54 → 2389.74] Like, so you've got open source obviously involved here.
[2389.74 → 2396.36] Uh, and as I understand it, it's the, the, the, the, the firmware, the electronics design files.
[2396.36 → 2402.24] So, I'm assuming there's some sort of CAD pieces in there that you're actually, you know, open sourcing on GitHub.
[2402.24 → 2405.92] You got the agent and these are all coming under the GPL license.
[2405.92 → 2412.32] So, you know, to, to kind of take a step back, you've got ergonomic keyboards, which have been there, you know, whether they break apart or not.
[2412.32 → 2442.30] Mm-hmm.
[2442.32 → 2450.28] And to never leave the home row, as you've described, and to never do the things that you're describing, which is to have to touch a mouse.
[2451.16 → 2465.04] And so, I'm, I'm just wondering behind the scenes, you know, what the motivations were, not just to solve a problem, but also to put some power back into the community, which is through open source, through open source diagrams and those kinds of things.
[2465.04 → 2465.64] Gotcha.
[2465.64 → 2465.74] Gotcha.
[2466.50 → 2466.70] Yeah.
[2466.70 → 2481.64] So, I, I, I've been using Linux for a year, 2000, and it just makes sense for me as a developer to, to open up product to, to make it super customizable.
[2481.64 → 2482.32] Right.
[2482.32 → 2493.28] Because I've been in situations when, uh, I've had a router and I, I, uh, wanted to use a third party, uh, dynamic DNS provider.
[2493.28 → 2504.34] And I couldn't because that router, uh, offered me about three options and my preferred options wasn't amongst those.
[2504.34 → 2512.80] So, and it's, it seemed really trivial to be able to specify a URL to be pinged, but it, it couldn't do it.
[2512.80 → 2526.54] And, or I'm, or I'm, my sister purchased the DVD player and, uh, uh, uh, put in a disc and then a sub, subtitle fonts were, were very small.
[2526.54 → 2540.18] And there wasn't a way to enlarge them, which is ridiculous because if the software was open source, that, that would have been so much easy to implement.
[2540.18 → 2550.66] So I encountered with all these limitations, and we are surrounded by these devices, uh, containing general purpose, uh, processors.
[2550.66 → 2551.38] Yeah.
[2551.38 → 2551.50] Yeah.
[2552.00 → 2561.14] And we are unable to, to exploit their full potential because, because the whole thing is a black box and I hate it.
[2561.42 → 2572.84] So what I hear you saying is that whether it's a DVD player, whether it's whatever out there, there's a general purpose software that's available that makes literally no sense to have as, you know, in quotes proprietary.
[2572.84 → 2582.52] Like maybe the company is not trying to hide it or keep it or close the source purposefully, but it sounds like what I'm, what I'm hearing from you is that really irks you.
[2582.52 → 2597.28] And to be able to build something that was physical, you know, actual hardware object that has software tie-ins and to make that software open source so that those who want to tinker, like you've said you wanted to in your past, we're able to, we're free to do so.
[2597.28 → 2606.98] And obviously in the end, uh, you know, on the on your GitHub repos, you do have the ability to veto or not veto pull requests.
[2607.06 → 2614.96] So that doesn't mean that every single pull request has to be committed back to master, but that means that the power of the people is available.
[2614.96 → 2617.08] And that sounds like that's a motivating factor for you.
[2617.72 → 2618.24] Yeah.
[2618.32 → 2618.50] Yeah.
[2618.58 → 2620.62] And number of, I think empowering people.
[2620.92 → 2621.14] Yep.
[2621.14 → 2621.82] Yeah.
[2622.36 → 2624.80] That's exactly what the change log is all about.
[2624.90 → 2630.76] This show, why Jared and I do this is because we exist to enrich the lives of developers.
[2630.98 → 2639.14] And there is no better way that we can think of right now in today's age, other than through great community and open source software development.
[2639.14 → 2641.76] So that's, that's what I love to hear about.
[2641.82 → 2645.88] Cause you know, part of this show is going deep and technical.
[2645.88 → 2658.04] And part of this show is, is this is discovering the wise, the, the mysteries of why Lacey and his team would say, we need to rebuild this hardware thing and make all of it open source, you know?
[2658.30 → 2667.50] And I want the listeners to understand where you're coming from because you've been through some sort of, you know, some, some sort of past that got you to where you're at now.
[2667.56 → 2668.78] And that's important.
[2670.18 → 2670.62] Yep.
[2670.62 → 2672.14] All right.
[2672.24 → 2674.60] So it's a it is time for another break.
[2674.64 → 2677.96] I'm going to, I'm going to fast-forward the time by three minutes.
[2677.96 → 2682.24] So if you're listening to this, and you think, man, this break is coming just a hair too soon.
[2682.30 → 2682.66] It is.
[2682.66 → 2686.58] It's coming exactly two minutes and 56 seconds too soon.
[2686.58 → 2696.72] Because when I come back diving deeper into this topic with Lacey, I want to go even deeper to all the tech behind it, how things mapped out.
[2696.72 → 2699.28] And that's a pun on purpose.
[2699.28 → 2702.34] So we'll hear, we'll hear more when we get back.
[2702.46 → 2703.52] So not for another break.
[2703.60 → 2704.04] We'll be right back.
[2707.34 → 2712.52] If you thought harvest was only about time tracking, check again, fast invoicing and payments.
[2712.62 → 2717.48] You can easily create and send invoices and accept payments with PayPal, Stripe, and many more.
[2717.94 → 2719.66] You got expense tracking without the mess.
[2719.74 → 2723.00] You got an iPhone or an Android app to go on the go with you.
[2723.34 → 2725.68] Snap those receipts and store them in the harvest app.
[2725.68 → 2730.90] You can also connect favourite tools like Slack and use chat commands to start and stop your timers.
[2731.30 → 2733.84] Head to getharvest.com and start your free trial.
[2734.30 → 2739.26] And once that trial is over, use our code changelog to save 50% off your first month.
[2739.26 → 2745.56] Everyone, we're back with Lots.
[2745.70 → 2746.96] We're diving deep.
[2747.40 → 2748.24] You know, I said Lots.
[2748.32 → 2749.28] You know why I said Lots?
[2749.76 → 2752.00] Because I was thinking about Toy Story.
[2752.08 → 2756.40] Anybody out there listening to this show, thinking about Toy Story when I say Lacey.
[2756.40 → 2761.74] Because one of the characters in the most recent, I can't believe I'm going on this tangent.
[2761.88 → 2763.44] But I'm going to just run with it.
[2763.98 → 2769.60] Because Lots was the antagonist of Toy Story 3.
[2770.38 → 2772.50] And so when I said Lacey, it kind of reminded me of Lots.
[2772.66 → 2772.90] Nonetheless.
[2774.98 → 2777.80] We're back, nonetheless, with Lots.
[2777.80 → 2781.90] And we're diving deep, even deeper into this ultimate hacking keyboard.
[2782.76 → 2787.56] And maybe the best part to start with this segment is the open source behind it.
[2787.90 → 2794.94] We've got everything from CAD drawings to JavaScript user agents, firmware, bootloaders.
[2795.06 → 2799.70] Where do we begin with talking about the open source out there that powers this hardware device?
[2799.70 → 2807.78] Okay, so everything is open source except for the CAD, which we will release in a delayed fashion.
[2809.66 → 2816.54] Five years later, that is the only way that we gain some leverage.
[2816.54 → 2819.26] All the other components.
[2820.26 → 2827.62] That is the electronics, the firmware, and the host size software are already open source and uploaded to GitHub.
[2827.62 → 2835.84] So when I'm on your profile, which if you want to follow along, listeners, you can go to GitHub.com slash ultimate hacking keyboard.
[2836.38 → 2838.10] And you'll see some repos there.
[2838.22 → 2847.34] The first one that might come to notice for me is agent, then electronics, then firmware, and then bootloader left, and then ultimately bootloader right.
[2848.20 → 2852.60] And the languages GitHub chose to label these, tell me if they're wrong or not.
[2852.60 → 2856.34] So agent is JavaScript, electronics is KiCad, which is why I said CAD.
[2856.48 → 2858.68] I thought that meant actually CAD drawings.
[2859.30 → 2861.06] And then the firmware is obviously written C.
[2861.92 → 2864.52] And then bootloader left is processing.
[2865.18 → 2867.58] And then bootloader right is C.
[2868.02 → 2870.66] Are those accurate labels that GitHub mess up?
[2871.26 → 2874.12] Actually, bootloader left is C, just like bootloader right.
[2874.46 → 2876.18] But other than that, it's correct.
[2876.18 → 2884.30] We just saw a processing lab, you know, we just covered processing recently in an issue of Change Law Weekly, and I didn't think it was C-like.
[2885.54 → 2886.36] It's different.
[2886.54 → 2888.70] It's more something else.
[2888.86 → 2895.38] Well, the Arduino platform uses a processing API that is implemented on top of C.
[2895.68 → 2895.94] Okay.
[2895.94 → 2899.48] So in a way, it's C, but especially API.
[2899.84 → 2900.16] I see.
[2900.26 → 2900.42] Okay.
[2900.78 → 2903.30] So let's start with agent, then, if we can.
[2903.42 → 2908.14] So agent is the configuration application used for the UK.
[2908.44 → 2909.46] What is this?
[2909.50 → 2910.76] This is your native language.
[2910.84 → 2911.72] You love JavaScript.
[2911.96 → 2912.64] So it's your preferred.
[2913.72 → 2914.26] What is this?
[2914.36 → 2915.28] What does it do for the keyboard?
[2915.28 → 2926.98] Well, there is a difference between what does it do and what will it do, because agent is in a pretty early stage at this point.
[2927.16 → 2928.20] It's right now.
[2928.20 → 2939.54] It's a command line application, which enables you to configure and enumerate the UK and do some operations.
[2939.54 → 2949.58] But ultimately, this will be a GUI configuration applications executed on top of Node WebKit.
[2950.10 → 2955.92] That is, I think, the project has been renamed to NWJS.
[2956.08 → 2956.96] I mean, Node WebKit.
[2957.38 → 2957.50] Right.
[2957.66 → 2959.34] So this is a runtime.
[2959.94 → 2968.64] This is basically Chromium and Node.js fused together, so you can develop native applications.
[2969.54 → 2973.08] On top of web technologies and Node APIs.
[2974.20 → 2983.40] So Node WebKit, aka NWJS, that agent runs on Windows.
[2983.94 → 2986.70] It runs on OS X and also runs on Linux platforms.
[2986.82 → 2989.76] Can you tell us more about that project and how you're using it?
[2990.76 → 2991.40] Sure.
[2991.68 → 2994.64] So right now, agent is a command line application.
[2995.02 → 2998.56] I can use it to enumerate the keyboard.
[2998.56 → 3001.66] So normally, it's enumerated in keyboard mode.
[3002.18 → 3013.66] But it can also be enumerated as the left and the right bootloader if I want to upgrade the firmware of the keyboard via USB.
[3013.66 → 3022.36] And I can also manipulate and query the EEPROM memory of the keyboard.
[3023.14 → 3026.20] So right now, it's rather low-level and command line.
[3026.20 → 3038.94] But by building on this low-level functionality, it will end up being an Angular application, AngularJS-based GUI application,
[3038.94 → 3051.94] in which you will be able to individually configure the keys and the layers and key maps of the keyboard and all kinds of functionality.
[3052.32 → 3057.94] The speed of the mouse movement and its acceleration and the various add-on modules.
[3057.94 → 3062.80] So this will be a full-blown configuration application.
[3063.56 → 3063.70] Gotcha.
[3064.06 → 3065.38] And you mentioned mouse.
[3065.48 → 3068.86] And I got to mention, I got to imagine that anybody listening is thinking like,
[3069.20 → 3077.02] now I have a keyboard with four different layers of different functionality that I can totally program, including the mouse.
[3077.72 → 3080.20] Can we talk about the accuracy of the mouse whatsoever?
[3080.34 → 3081.58] How does the mouse function work?
[3081.58 → 3082.58] Is it enough to do?
[3083.48 → 3084.92] I mean, is it painful to use?
[3085.06 → 3086.52] Obviously, you're not going to say no.
[3086.86 → 3089.42] But, you know, how accurate is it?
[3089.46 → 3092.28] Will people really enjoy using the mouse feature of this keyboard?
[3093.76 → 3096.96] Yeah, so for what it is, it's surprisingly useful.
[3097.30 → 3099.24] I implemented inertia.
[3100.00 → 3107.48] So when you start to move your pointer, it doesn't start with full speed, but slowly increments.
[3107.62 → 3109.62] So it's pretty useful.
[3109.62 → 3116.52] But of course, such a keyboard-based solution can't replace a dedicated mouse.
[3117.42 → 3123.06] And this is the reason why we came up with add-on modules.
[3123.76 → 3132.78] So if you split the keyboard, you will be able to mount additional physical hardware modules to the main keyboard,
[3132.78 → 3144.72] such as a key cluster on the left hand or a trackpad and the track point.
[3145.06 → 3145.38] Right.
[3145.56 → 3145.72] Yep.
[3145.98 → 3151.10] So you can choose of these modules and mount whichever you like.
[3151.10 → 3155.84] And this is the extension of the original concept of Never Limit the Home Rule.
[3156.76 → 3167.22] And there is a large area that our thumbs cover, and you can easily reach dedicated point or devices this way.
[3167.96 → 3170.50] So these modules are obviously pretty interesting.
[3170.66 → 3173.80] Anybody listening right now is thinking like, okay, so I can layer on these modules.
[3174.06 → 3175.14] Are they optional?
[3175.56 → 3176.74] Are there future ones plans?
[3176.74 → 3180.46] Are there some that you've already kind of pre-configured that are available?
[3181.18 → 3185.66] And then obviously, since this is the ultimate hacking keyboard, you can obviously make your own.
[3186.12 → 3187.34] Or at least I'm assuming.
[3187.60 → 3187.74] Yep.
[3187.74 → 3188.90] You know, are they optional?
[3189.22 → 3190.22] Are there future ones planned?
[3190.48 → 3191.64] What are available right now?
[3192.74 → 3194.02] Yeah, they are completely optional.
[3194.18 → 3196.80] You can use the UK without any mocks.
[3196.80 → 3205.94] And if some of the mocks you think you would be using them, then you can just purchase them separately.
[3206.28 → 3207.94] Use them as you like.
[3208.28 → 3208.92] Replace them.
[3209.30 → 3209.56] Okay.
[3210.08 → 3215.26] So some, you know, you said the word purchase there, which may have gotten some people like, whoa, hang on.
[3215.34 → 3216.42] I bought this keyboard.
[3216.86 → 3217.70] Now there's more to buy.
[3217.84 → 3220.04] I feel like there's like an in-app purchase, so to speak.
[3220.04 → 3227.60] Can you talk about the ecosystem from a revenue generation point to the hacking point?
[3227.68 → 3231.18] Because obviously hackers love to make their own things and use freely.
[3231.82 → 3240.84] Not meaning don't pay the person who made it, because we obviously want to support you making this thing in the first place to make your business sustainable to keep doing this thing.
[3240.96 → 3245.28] But, you know, what are the plans for modules?
[3245.78 → 3249.36] Is there going to be a module ecosystem people can go to and purchase things?
[3249.36 → 3253.10] Describe that as you might like to.
[3253.94 → 3254.32] Sure.
[3254.74 → 3263.12] So we will open up the protocol via which the modules communicate with the keyboard itself.
[3264.06 → 3270.20] And third-party developers will be able to develop their own modules.
[3270.20 → 3279.70] And we will also sell a developer kit and publish the CAD data of the modules.
[3280.28 → 3291.62] So anybody will be able to 3D print their own modules and create whatever crazy input device they want to make.
[3291.62 → 3294.62] We could even use joysticks or...
[3294.62 → 3302.86] Well, there are a lot of possibilities there using any kind of pointer devices.
[3302.86 → 3308.82] So what I thought of as modules, and you thought of modules seem to be similar but different.
[3309.02 → 3310.40] So you just talked about a joystick.
[3310.56 → 3318.90] It sounds like we're breaking out of just the UK into actually allowing developers to have open source that you're providing to build their own modules.
[3319.64 → 3323.46] And then you're using that same open source to build your own modules, which you'll be able to sell.
[3323.46 → 3325.46] Is that right?
[3326.44 → 3328.42] How did you mean this exactly?
[3328.68 → 3336.12] What I mean by that is that you've got some open source author that allows somebody to build their own modules so they can 3D print their own thing if they wanted to.
[3336.22 → 3343.48] So if they wanted to hack away and build something like a numeric key or just a keypad that sits there only.
[3343.78 → 3345.32] They can do that if they wanted to.
[3346.10 → 3347.04] Is that what I heard?
[3347.04 → 3351.44] Yep, they could do that but because of the mechanical constraints.
[3351.76 → 3361.10] So the whole thing is designed that the keyboard halves are interconnected by these precision machined steel guides.
[3361.44 → 3365.16] And these same steel guides are used for modules.
[3365.68 → 3366.32] Gotcha, okay.
[3366.76 → 3374.82] So when you separate the two halves, these same guides are used to mount the modules themselves.
[3374.82 → 3384.86] So this way the add-on modules are mechanically constrained to be located there between the two keyboard halves essentially.
[3385.64 → 3391.92] And there are POGO pins for the electricity and data.
[3392.12 → 3397.10] So there's some hardware that they might need to buy from you that they can build upon basically.
[3397.80 → 3398.28] Yep.
[3398.56 → 3399.90] Okay, that totally makes sense.
[3399.90 → 3409.62] So once you break this keyboard apart, again, once we went back to the earlier analogy, 6TGB down to the space bar is the left-hand side when you break it apart.
[3409.72 → 3414.18] And 7YHN, if I remember correctly myself, that's the right-hand side.
[3414.26 → 3424.76] And in between those two, once you break it apart, hackers out there that are working with UK could essentially buy some hardware for themselves to put in between these two pieces
[3424.76 → 3433.54] or attach to the two pieces once they're broken apart and use open source that you've already provided to build upon it, fork it, make their own things,
[3434.08 → 3439.54] and potentially even 3D print their own actual stuff and connect back to it.
[3440.40 → 3440.84] Yep.
[3440.84 → 3446.36] That really does complete the whole entire cycle of being the ultimate hacking.
[3446.64 → 3450.18] I mean, so when you said ultimate hacking, you really, really meant it, didn't you?
[3451.26 → 3464.16] Yeah, we really want to push this as much as possible to cram as much functionality to the hardware as possible.
[3464.16 → 3464.24] Cool.
[3465.54 → 3467.54] So we camped out a bit on the agent.
[3467.78 → 3473.30] Let's talk a bit about firmware because I remember we got emailed from you, let's say, about a month ago.
[3473.82 → 3483.36] And we've had some things going on in between now and then that didn't allow this call to take place until roughly three days before your funding end.
[3483.82 → 3489.82] But nonetheless, you mentioned that once funding was reached, you would open source several things.
[3489.82 → 3495.78] And one of those things was the firmware, electronics, the agent we've just been talking about here.
[3496.26 → 3498.28] Can you talk a bit about the electronics piece?
[3498.70 → 3504.18] There's an electronics project on GitHub on your profile there, and there's also a firmware.
[3504.34 → 3505.74] Can you talk about those two pieces there?
[3506.90 → 3507.42] Sure.
[3507.82 → 3511.70] So the electronics repo contains the KiCad files.
[3511.84 → 3514.74] KiCad is an electronics design program.
[3514.74 → 3525.94] So if you download and install KiCad, then you can open these files, and you can see the printed circuit board, and you can manipulate it.
[3526.74 → 3530.88] You can even send to a fab and get it made.
[3530.88 → 3544.40] So it really enables you to extend the UK, add LEDs, backlighting, for example, or all kinds of crazy stuff.
[3544.88 → 3551.54] So when you talk about KiCad, you're talking about the same, if my Google foo is correct,
[3551.54 → 3563.00] if you go to KiCAD-PCB.org, which is KiCad EDA, a cross-platform and open-source electronic design automation suite,
[3563.04 → 3564.48] is that the same thing you're leveraging?
[3564.60 → 3567.20] You're building upon somebody else's shoulders here?
[3568.50 → 3568.94] Yep.
[3569.06 → 3571.48] It's the project that we are talking about.
[3571.68 → 3571.88] Gotcha.
[3572.02 → 3572.90] It's the KiCad PCB.
[3573.38 → 3575.98] I know the hardware hackers are there like, Adam, get with it.
[3576.20 → 3577.48] You know, this is out there already.
[3577.96 → 3578.58] But you know what?
[3578.58 → 3580.74] Open source moves fast, so we just try to keep up.
[3581.54 → 3586.68] So, okay, so this is some more open-source already out there, available developers,
[3587.12 → 3589.82] and you're just building on the shoulders of more giants.
[3591.20 → 3591.72] Yep.
[3591.88 → 3599.12] Originally, we used Eagle, which is another popular choice in the electronic design,
[3599.24 → 3605.52] open-source electronic design community, but that isn't an open-source software,
[3605.52 → 3611.82] and you are limited to design very small boards with the free version.
[3612.74 → 3618.16] So eventually I migrated to KiCad because it is totally free on like Eagle.
[3618.16 → 3624.46] And this way we can enable more people to hack the keyboard.
[3624.46 → 3624.86] Right.
[3625.02 → 3628.40] So the electronics repo is a KiCad project,
[3628.88 → 3636.16] building upon the KiCad ADA cross-platform open-source software we just talked about there.
[3636.16 → 3647.42] So it's your open-source is leveraging specs, platforms, software already out there from someone else that's desiring the same thing you are,
[3647.48 → 3649.26] which is, hey, I have some hardware.
[3649.42 → 3658.34] I want to be able to manipulate and give back to, as a developer, whether super hacker or not, back to open-source.
[3659.34 → 3659.78] Yep.
[3659.98 → 3660.62] That's the idea.
[3660.86 → 3661.26] Fantastic.
[3661.26 → 3662.80] All right.
[3663.08 → 3664.56] Let's move to the next one then.
[3664.60 → 3665.60] So the next one is the firmware.
[3665.76 → 3667.06] What's going on in the firmware?
[3667.28 → 3668.26] Is there a...
[3669.04 → 3673.80] What can a developer do inside the firmware that is notable?
[3675.02 → 3675.58] Okay.
[3675.74 → 3685.06] So the way it works is the left keyboard half sends key press and key release events to the right keyboard halves.
[3685.06 → 3693.90] Then the right keyboard half maintains a matrix of keys and the state of the keys.
[3694.86 → 3701.72] And based on this state, it decides which layer is the active one.
[3702.56 → 3710.30] And it sends out the relevant scan codes via USB to the host computer.
[3710.30 → 3722.44] And it's more versatile than most keyboards because it exposes three different USB interfaces.
[3722.68 → 3724.78] So there is the keyboard interface, of course.
[3725.12 → 3725.22] Right.
[3725.32 → 3729.54] And there is the mouse interface to implement the mouse functionality.
[3729.54 → 3735.56] And there is a third generic HID interface for communication purposes.
[3736.50 → 3744.18] So when you use agent to configure the UK, this third interface is used as transport.
[3744.18 → 3745.18] So...
[3745.18 → 3746.18] So...
[3746.18 → 3747.18] So...
[3747.18 → 3747.86] And there is a...
[3747.86 → 3755.16] There is a library that is used for the firmware of the right keyboard half that is called Luff,
[3755.76 → 3760.10] which stands for lightweight USB library for Airs.
[3760.90 → 3764.56] The microcontrollers are AVR processors.
[3764.56 → 3779.84] And this is pretty much the most popular library to interface with USB capable AVR microcontrollers because USB is a very complex protocol.
[3779.84 → 3791.12] If you think about it, there are pen drives and Bluetooth modems and printers and all kinds of devices that use USB, a single protocol.
[3791.12 → 3794.94] So this is a heavily layered, super complex protocol.
[3795.72 → 3801.98] And I personally couldn't write from the ground up a USB stack, USB library.
[3802.66 → 3806.00] And luckily, this is available and open source.
[3806.40 → 3808.46] And we built upon this library.
[3809.66 → 3810.04] Very interesting.
[3810.78 → 3812.64] So you got the left side and the right side.
[3812.68 → 3814.40] Can you talk a bit more about...
[3814.40 → 3820.10] I can imagine those listening to that piece, they were thinking like, okay, the left side communicates to the right.
[3820.10 → 3824.50] The right, as we mentioned earlier in the show, has alternate modifier keys.
[3824.64 → 3828.42] The space key typically is alternated on the left and the right.
[3828.48 → 3830.26] So the left-hand side is...
[3830.26 → 3833.54] Let me go back to my screenshot to make sure I'm speaking correctly.
[3833.78 → 3840.48] So the left side, the key that is typically your space bar is the mod key.
[3841.12 → 3844.96] And then when you break it apart, the right side, which is typically your space bar, is...
[3844.96 → 3845.86] You guessed it.
[3846.04 → 3846.58] The space bar.
[3847.18 → 3849.24] And so those two alternate whenever you break them apart.
[3849.24 → 3861.04] Can you talk a bit about this conversation that happens between software and between the hardware that hackers would enjoy when they really make this thing their own between the left and the right?
[3862.74 → 3865.88] So it all starts with the keyboard matrix.
[3866.46 → 3871.02] So the keys are arranged into matrix of rows and columns.
[3871.02 → 3876.46] And this matrix is scanned about a thousand times per second.
[3877.50 → 3881.64] And so the software can maintain a state of these keys.
[3881.64 → 3890.24] So the state of the keys are stored in this matrix in the RAM of the microcontroller.
[3891.44 → 3897.64] And like I said, the left keyboard half sends over the keyboard...
[3897.64 → 3901.32] The key press and key release of the right keyboard half.
[3901.32 → 3905.74] And then we end up with a matrix of keys.
[3906.50 → 3915.10] And then in the next phase, the firmware checks for the layer switcher keys like mod or mouse and FN.
[3915.10 → 3923.30] And based on those keys, it sees which layer is the active one.
[3924.38 → 3942.54] And then based on that layer, it constructs a USB report containing the scan codes that are related to those keys on the actual layer on the actual key map.
[3942.54 → 3944.28] So did that make sense?
[3944.70 → 3945.88] It totally...
[3945.88 → 3948.44] I mean, it makes sense as much as it makes sense.
[3948.58 → 3948.82] Okay.
[3948.98 → 3954.24] Without seeing it touching that visually as we have this conversation, it's a little foreign, but I'm following.
[3954.74 → 3963.36] And I guess what I'm trying to gather at this point is thinking like, you know, going back to the name, the ultimate hacking keyboard.
[3963.36 → 3968.76] I know some people that just are...
[3968.76 → 3973.60] I don't want to call them true hackers because it sort of mislabels the word hacker, period.
[3973.96 → 3977.86] But they're just people who love, like you had mentioned earlier, to tinker.
[3978.36 → 3982.40] To go beyond the status quo of like making something their own.
[3982.40 → 3989.30] And I feel like what you've done here with creating the hardware and the software is what...
[3989.30 → 3996.40] Maybe not where it's at right today, and maybe you can help back me up on this, but I'm going to hypothesize that the future of this thing is that...
[3997.56 → 4003.04] If you're someone who loves to tinker with their keyboard, loves to make what they do their own,
[4003.12 → 4006.82] you love the fact that you can break apart a keyboard and do all sorts of stuff,
[4006.82 → 4014.04] and maybe even borrow some of your polyglot attributes, they can dive deep into this thing, make it their own.
[4014.42 → 4018.88] And above all else, what we haven't even talked about is taken it anywhere.
[4019.56 → 4025.54] You know, like that's what I love most about what I think this conversation is about is like this hardware piece
[4025.54 → 4035.14] that came out of like several years of love from you and a passion for when you touch a hardware object
[4035.14 → 4042.56] that has software components, not being able to change those, but making what has come from it open source
[4042.56 → 4047.02] so that those who use it can, and even add to it, and enrich the ecosystem.
[4047.32 → 4053.18] So if I'm understanding correctly, like this thing sounds to me like a hacker's dream.
[4053.18 → 4061.86] And going back to the original blog post on Trello, how I built the developer's dream keyboard
[4061.86 → 4064.50] seems to me like it's really going to be playing true.
[4064.50 → 4071.22] Yeah, originally I gave a more modest title to that article.
[4071.56 → 4071.74] Yeah.
[4071.98 → 4075.92] And the Top Tile guys made it a little fancier.
[4076.66 → 4078.66] But thanks for saying that.
[4079.20 → 4085.12] Well, you know, going back to our friends at Top Tile, those guys are committed to excellence.
[4085.12 → 4086.12] For sure.
[4086.12 → 4091.58] And outside the sponsors that you've, the sponsor notes you mentioned that I've mentioned during this show,
[4092.04 → 4093.62] we love those guys.
[4093.76 → 4099.62] We love working with Top Tile because they are so committed to enriching developers' lives.
[4100.08 → 4105.00] And, you know, I think that post with you and then, you know, how they helped you with it
[4105.00 → 4108.38] and then where you're at today is completely evident.
[4108.58 → 4114.04] So if you've been on the fence about what Top Tile is, go back and listen to our sponsor mentions.
[4114.22 → 4114.88] We love them.
[4115.00 → 4115.82] We think you'll love them too.
[4115.88 → 4116.62] We totally trust them.
[4116.62 → 4122.94] But moving on to some future topics here, we've got to go to a break real quick.
[4123.22 → 4129.66] We're going to come back, and we're going to talk a little bit about not so much the UK,
[4130.02 → 4135.52] but who you are, I guess, again, as a software developer, maybe some of your heroes,
[4135.78 → 4140.08] something that's super secret that no one knows about you can share.
[4140.74 → 4142.22] But we're going to take a break.
[4142.34 → 4143.98] We'll come back, and we'll talk about that.
[4145.48 → 4147.66] Our friends in Linde are huge fans of the show,
[4147.68 → 4149.64] and they're excited to support what we're doing here at the Changelog.
[4149.64 → 4154.90] And they want to invite every single listener of the Changelog to try out one of the fastest,
[4155.22 → 4158.16] most efficient SSD cloud servers on the market.
[4158.74 → 4162.70] You can get a Linde cloud server up and running in seconds with your choice of Linux distro,
[4163.02 → 4164.88] resources, and also node location.
[4165.20 → 4168.26] And they've got eight data centres spread across the entire world,
[4168.26 → 4173.58] North America, Europe, Asia Pacific, and plans started at just $10 a month.
[4174.02 → 4177.40] They've got hourly billing with a monthly cap on all plans and add-on services.
[4177.86 → 4183.50] Get full root access for more control, run VMs, run containers, or even your own private Git server.
[4183.94 → 4189.58] Enjoy native SSD storage, 40 gigabit network, and Intel E5 processors on your servers.
[4190.18 → 4192.56] Use the code ChangeLog10 with unlimited uses.
[4192.56 → 4193.78] Tell your friends.
[4193.90 → 4196.56] It doesn't expire until December 31st, 2016.
[4197.38 → 4198.34] That's next year.
[4198.76 → 4201.04] Head to linode.com slash changelog to get started.
[4201.36 → 4202.56] And now back to the show.
[4204.56 → 4206.82] All right, we're back with Lacey again.
[4207.76 → 4211.26] Just so excited about what you've built here so far.
[4211.26 → 4214.68] And the open source component of it is obviously pivotal.
[4215.00 → 4217.18] So if you're out there, and you're listening to this, and you're thinking,
[4217.36 → 4225.40] this literally is, or I think it might be, the ultimate hacker keyboard,
[4225.78 → 4231.52] the open source component to me is unheard of.
[4231.88 → 4234.04] It's not there so far.
[4234.24 → 4235.20] We talked about the agent.
[4235.28 → 4237.46] We talked about the electronics, the firmware,
[4237.46 → 4241.98] which also led to bootloader left and bootloader right if I'm clear on that.
[4242.60 → 4248.12] What else do you have planned on the open source horizon around this hardware device
[4248.12 → 4251.42] that is going to get hackers excited today,
[4252.04 → 4254.24] that they're going to make them either want to go support the project
[4254.24 → 4258.72] or do whatever it takes to get 200 bucks out of their pocket
[4258.72 → 4260.82] and give it to you for this thing?
[4260.82 → 4269.74] Yeah, so I think the UK provides a unique set of features.
[4270.32 → 4274.70] I mean, there are other split keyboards on the market.
[4274.92 → 4275.98] Right, it's not a new thing.
[4276.06 → 4276.92] It's been done before.
[4277.52 → 4277.94] Yeah, sure.
[4278.12 → 4278.58] But you're doing it differently.
[4279.36 → 4283.14] Yeah, for example, the add-on modules are one of a kind.
[4283.30 → 4286.04] I mean, nobody has ever done that before.
[4286.04 → 4293.90] Or the other unique feature is the stainless steel inserts on the back of the keyboard.
[4294.12 → 4300.52] So you can mount it, the two keyboard halves separately to the arms of your armchair.
[4301.14 → 4303.96] So this is another unique thing.
[4304.62 → 4307.86] So you can sit essentially back into like a lazy boy, so to speak.
[4307.96 → 4309.58] Here in America, we have a lazy boy.
[4309.78 → 4312.38] And you can put one on the right and one on the left
[4312.38 → 4317.16] and kick it all the way back totally in comfort, in leather, in hack.
[4317.92 → 4318.16] Yep.
[4319.34 → 4320.68] See, that's the best, man.
[4321.46 → 4325.66] Yeah, and the way I see it, this is a platform.
[4325.66 → 4330.38] I mean, it has a hardware-software architecture.
[4331.26 → 4336.78] And based on this architecture, we plan to build other keyboards in the future.
[4337.00 → 4341.72] Like this is a 60% keyboard, which means that it only contains the alphanumeric block.
[4342.38 → 4345.44] We plan to build an 80% version.
[4345.86 → 4352.58] We should contain the alphanumeric block plus the F keys plus the navigation block.
[4353.40 → 4353.66] Okay.
[4353.88 → 4356.20] And then maybe other versions.
[4356.38 → 4361.82] But the way I see it, this is a nervous system, if you will.
[4361.82 → 4369.70] And you can fit this nervous system into various shapes and forms.
[4370.64 → 4381.04] And it can be a basis of other split keyboards that have the same great features
[4381.04 → 4386.02] and extensibility with add-ons and all this fancy stuff.
[4386.02 → 4398.52] So even hackers can design keyboards of other shapes with this same core of hardware and software
[4398.52 → 4400.08] and firmware components.
[4400.08 → 4405.98] You know, on that note, too, I think we, you know, it just wouldn't do it justice if we didn't touch on it
[4405.98 → 4408.98] because it's clear as day when you go watch the video.
[4409.34 → 4414.34] And I don't want to repeat everything that's out there already, although it should at least be touched on.
[4414.34 → 4419.78] And what I think is kind of interesting is that, like, no matter what the program you work with,
[4419.82 → 4425.02] whether it's a game, whether it's an IDE, whether it's, you know, you name it,
[4425.50 → 4429.22] the four layers that we talked about already and even the mouse,
[4430.22 → 4435.74] all the application-specific key maps you can do, it's totally customizable.
[4435.74 → 4444.06] So if you're playing, you know, Fallout 4, for example, and you want to configure it specifically to how you like to play that game,
[4444.36 → 4445.62] you can do it for that.
[4445.90 → 4451.18] And if it's Ruby on Rails or if it's, in your case, JavaScript programming
[4451.18 → 4455.48] and you've got some specific keys that really help you be a better developer,
[4456.10 → 4457.38] then you can remap to that.
[4457.46 → 4460.06] I think that's really an interesting piece there is that just this,
[4460.06 → 4466.18] the ability to just make it your own, regardless of application device,
[4466.36 → 4468.36] you know, that you can just do that.
[4468.54 → 4470.80] And it's easy.
[4471.74 → 4472.22] Yeah.
[4472.44 → 4473.58] Hopefully, is it easy?
[4474.50 → 4475.56] It will be easy.
[4475.56 → 4479.96] Right now you have to modify a matrix, a C matrix.
[4480.26 → 4480.44] Right.
[4480.44 → 4487.46] But later on, if the agent, the configurator application will be in a more advanced state,
[4487.92 → 4489.12] that will happen before shipping,
[4489.12 → 4494.32] then you will be able simply to click in a GUI application
[4494.32 → 4498.82] and reconfigure the keyboard, the key map.
[4499.58 → 4504.08] And for example, I'm a heavy user of convenience shortcuts.
[4504.72 → 4509.86] So add tab, for example, is used by every one of us many times a day.
[4510.56 → 4516.08] And add tab on the factory key map is mapped to the key of the mod layer.
[4516.08 → 4523.62] So instead of reaching out for add tab, I simply press mod D without leaving the home row.
[4523.92 → 4530.14] And this may not seem like a big deal, but when you use add tab hundreds,
[4530.50 → 4533.88] if not thousands of times per day, it's a big deal.
[4533.88 → 4537.64] Yeah, probably half a thousand for me.
[4537.86 → 4539.36] 500 times a day, I'm going to guess.
[4539.98 → 4541.94] Yeah, I think it's a good estimate.
[4542.46 → 4542.58] Yep.
[4542.58 → 4549.04] So Jared couldn't make this show, but it wouldn't be a show.
[4549.56 → 4554.10] It wouldn't be a change long episode if we didn't even have a little bit of Jared in here.
[4554.14 → 4556.10] And there's been a couple sprinkles of it in here.
[4556.10 → 4563.50] But he said before the modules are fascinating.
[4563.80 → 4565.00] They're totally optional.
[4565.62 → 4568.60] You mentioned some plan for the future of these modules.
[4569.84 → 4574.14] How will you support those out there who are maybe making modules
[4574.14 → 4576.20] and don't have the ability to 3D print?
[4576.88 → 4582.04] What kind of support can you give back to the community that's building upon this
[4582.04 → 4584.20] but don't have the ability to print?
[4584.20 → 4590.20] Well, we will offer developer kits for sale.
[4590.62 → 4597.46] And that way, do you mean the physical accessibility of creating an add-on?
[4597.96 → 4599.78] Yeah, well, I think there's the software side of it,
[4599.80 → 4602.50] which I think people can probably get to the point on their own.
[4603.00 → 4605.02] But if they actually want to build something out of it
[4605.02 → 4607.30] and they don't have the ability, or let's say they build it
[4607.30 → 4608.78] and it's kind of like, eh, it's okay.
[4609.92 → 4612.68] And maybe it's something they want to pony up back to you and say,
[4612.68 → 4615.44] well, can you manufacture this and give it to everyone?
[4615.86 → 4617.30] You know, it's that cool.
[4618.84 → 4621.02] Yeah, we should be able to do that.
[4621.72 → 4626.56] Maybe we should do a pause about it later on.
[4626.78 → 4632.42] Because if there is only one person in the world who wants that module,
[4632.42 → 4636.08] that it's just simply not feasible to be manufactured.
[4636.76 → 4640.14] But if there is a significant community interest,
[4641.14 → 4643.78] then we should be able to do that.
[4643.88 → 4644.58] We should do that.
[4645.02 → 4647.90] In order to develop a module,
[4648.14 → 4651.24] you will have to have some hardware skills
[4651.24 → 4655.48] because, well, software is easier in this respect.
[4656.30 → 4661.24] You just have to download the IDE and stuff and start coding.
[4661.40 → 4664.08] But in order to develop a physical module,
[4664.08 → 4668.00] you have to have some gear like soldering Byron
[4668.00 → 4670.92] and stuff like that.
[4671.24 → 4675.14] And some experience with electronics,
[4675.14 → 4677.16] I think it's pretty much necessary.
[4678.26 → 4682.52] We want to make this process as simple as possible for people.
[4683.48 → 4687.78] But Harvard is just harder.
[4690.28 → 4690.80] Yeah.
[4690.96 → 4691.72] That's all to there.
[4691.72 → 4695.78] Well, you actually have to make something real.
[4696.34 → 4696.48] You know?
[4697.16 → 4697.44] Yep.
[4697.78 → 4703.18] Plastic, metal, whatever material you work with,
[4704.00 → 4707.44] we get so used to this Command Z,
[4709.18 → 4713.02] RF, RM,
[4713.62 → 4717.70] to just remove something from command line or something like that.
[4718.62 → 4721.36] We just get so used to that in the real world
[4721.36 → 4723.34] and things are real.
[4724.16 → 4724.32] You know?
[4724.38 → 4726.52] Yeah, but more and more developers
[4726.52 → 4729.84] seem to go into the hardware scene.
[4730.54 → 4733.58] And they purchase Arduino's
[4733.58 → 4736.04] and start incurring with hardware.
[4737.14 → 4738.60] And once you get into it,
[4738.70 → 4739.84] you learn more and more
[4739.84 → 4743.68] and this becomes natural over time.
[4744.34 → 4745.60] So it's not rocket science,
[4745.74 → 4748.88] but it needs some practice for sure.
[4749.34 → 4749.44] Right.
[4749.44 → 4752.50] And if you want to create a new voice tool,
[4752.50 → 4757.50] maybe you also have to order components
[4757.50 → 4763.18] from drives, stores, like joystick or what have you.
[4763.52 → 4763.66] Right.
[4764.38 → 4765.46] I think it's interesting too,
[4765.66 → 4768.10] going back to your note before about being a platform.
[4768.10 → 4771.18] And maybe I'm reading between the lines,
[4771.46 → 4772.20] you tell me,
[4772.48 → 4776.68] but being a platform to me sounds like you're not going anywhere.
[4776.96 → 4777.22] Right?
[4777.66 → 4780.66] And there's something that there's a promise there, so to speak.
[4780.66 → 4782.70] So when you come on this show
[4782.70 → 4787.24] and you go out there, and you create a crowdfunding campaign
[4787.24 → 4789.62] and you actually make something real
[4789.62 → 4790.84] and you ship it to people
[4790.84 → 4792.86] and you open source software
[4792.86 → 4794.02] and you talk about it
[4794.02 → 4795.28] and you live it, and you dream it,
[4795.88 → 4798.10] it sounds to me like you're making a promise.
[4798.40 → 4800.40] And especially when you said there's a platform here.
[4800.48 → 4801.88] Like if there's someone,
[4802.10 → 4803.96] if there's someone listening to this show
[4803.96 → 4805.10] and they're thinking,
[4805.30 → 4806.50] this may,
[4807.18 → 4808.26] this may not be for me.
[4808.26 → 4809.38] It sounds interesting.
[4809.72 → 4811.02] The software sounds interesting.
[4811.28 → 4813.62] The open source aspect of it sounds interesting.
[4814.10 → 4815.82] The hardware clearly is interesting.
[4817.54 → 4820.10] We didn't even touch at all on,
[4820.18 → 4821.66] I mean, I guess to a degree,
[4821.80 → 4822.76] we touched on,
[4822.90 → 4823.78] you know,
[4823.96 → 4826.76] the makeup of it,
[4826.82 → 4828.60] how strong and sturdy it is.
[4828.72 → 4830.90] But when you make something like you have,
[4830.92 → 4831.68] and I haven't touched it,
[4831.70 → 4833.52] but I've talked to other people who have
[4833.52 → 4834.76] that I trust,
[4835.14 → 4835.40] right?
[4835.40 → 4838.10] Like egghead.io.
[4838.38 → 4839.30] I trust that guy.
[4839.54 → 4839.74] You know,
[4839.98 → 4840.78] he touched it.
[4840.86 → 4841.24] He put it,
[4841.34 → 4842.24] he pulled it apart.
[4842.38 → 4843.06] He put it back together.
[4843.18 → 4843.88] But what I,
[4843.94 → 4844.78] the point I'm trying to make here
[4844.78 → 4845.32] is that if,
[4845.48 → 4847.56] if you're doing that,
[4847.76 → 4848.08] then,
[4848.22 → 4849.66] and you're saying this is a platform,
[4849.66 → 4850.50] to me,
[4850.52 → 4852.60] it sounds like to the developer world,
[4852.60 → 4854.02] you're making a promise
[4854.02 → 4855.06] that you're going to be there
[4855.06 → 4855.94] for the future,
[4855.94 → 4857.62] whether it's in the open source,
[4857.78 → 4858.58] whether it's in the hardware,
[4858.58 → 4861.16] and that if you can dream it
[4861.16 → 4862.58] and you can build it,
[4862.58 → 4863.76] it sounds a little cliché,
[4863.76 → 4865.74] but if you can do those things
[4865.74 → 4867.34] with this ultimate hacking keyboard,
[4867.34 → 4868.72] then you're going to be there
[4868.72 → 4869.76] in one way or another
[4869.76 → 4870.76] to support it,
[4871.08 → 4872.32] whether it's through some way
[4872.32 → 4873.28] to make money from it
[4873.28 → 4874.12] as other developers,
[4874.12 → 4875.78] or one way to support
[4875.78 → 4876.62] their open source
[4876.62 → 4877.70] and help them become better
[4877.70 → 4878.64] software developers.
[4878.96 → 4880.20] Is that a fair statement?
[4881.18 → 4881.52] Absolutely.
[4881.90 → 4883.30] You are spot on
[4883.30 → 4884.70] by saying that
[4884.70 → 4885.52] it's a platform.
[4885.70 → 4885.92] I mean,
[4886.30 → 4887.46] most manufacturers
[4887.46 → 4888.60] create a
[4888.60 → 4890.22] single product,
[4890.22 → 4891.84] that we
[4891.84 → 4892.62] rather
[4892.62 → 4893.56] think
[4893.56 → 4895.24] about
[4895.24 → 4895.88] integrating
[4895.88 → 4898.24] the
[4898.24 → 4899.08] hardware,
[4899.34 → 4899.78] the firmware,
[4899.98 → 4900.42] the software,
[4900.78 → 4901.22] and cloud
[4901.22 → 4901.54] and
[4901.54 → 4903.80] provide the
[4903.80 → 4906.26] how should I
[4906.26 → 4907.16] say it?
[4907.72 → 4908.20] More
[4908.20 → 4911.46] let's stop
[4911.46 → 4912.26] for a minute.
[4912.26 → 4912.66] Well,
[4912.80 → 4914.10] some sort of support.
[4914.28 → 4914.94] Some sort of support
[4914.94 → 4915.40] if there's something
[4915.40 → 4916.18] built from it,
[4916.18 → 4917.64] then you're going to be
[4917.64 → 4918.52] able to
[4918.52 → 4919.84] provide a way
[4919.84 → 4920.26] to
[4920.26 → 4921.68] almost
[4921.68 → 4924.18] package manager it
[4924.18 → 4925.10] to it away.
[4925.24 → 4926.06] If you build it,
[4926.58 → 4927.38] people can find it.
[4928.68 → 4928.92] Yep.
[4929.22 → 4929.84] And the
[4929.84 → 4931.80] hardware and software
[4931.80 → 4933.08] is much better
[4933.08 → 4933.68] integrated
[4933.68 → 4934.06] than
[4934.06 → 4935.62] on
[4935.62 → 4936.62] other
[4936.62 → 4937.98] keyboards,
[4938.22 → 4938.50] which is
[4938.50 → 4941.40] maybe a brave statement
[4941.40 → 4942.04] to make.
[4942.42 → 4942.76] But
[4942.76 → 4943.94] when
[4943.94 → 4945.02] you
[4945.02 → 4946.06] open up
[4946.06 → 4946.50] the box,
[4946.78 → 4947.56] you will
[4947.56 → 4948.20] encounter
[4948.20 → 4949.32] something
[4949.32 → 4950.18] that you
[4950.18 → 4950.56] have never
[4950.56 → 4951.00] seen
[4951.00 → 4952.50] in other
[4952.50 → 4952.88] products.
[4953.10 → 4953.34] And I
[4953.34 → 4955.10] don't want
[4955.10 → 4955.78] to
[4955.78 → 4957.52] talk about
[4957.52 → 4957.74] this,
[4957.86 → 4958.64] but I
[4958.64 → 4958.92] want to
[4958.92 → 4959.38] surprise
[4959.38 → 4960.14] people.
[4960.68 → 4960.86] So I
[4960.86 → 4962.36] rather
[4962.36 → 4962.78] want
[4962.78 → 4963.90] to
[4963.90 → 4964.36] talk about
[4964.36 → 4964.52] this.
[4964.54 → 4964.88] We have
[4964.88 → 4965.24] to leave
[4965.24 → 4965.86] some
[4965.86 → 4967.04] cards
[4967.04 → 4967.54] up our
[4967.54 → 4967.94] sleeves,
[4968.00 → 4968.26] so to
[4968.26 → 4968.62] speak.
[4969.44 → 4969.68] Yep.
[4969.90 → 4970.58] We can't
[4970.58 → 4970.86] reveal
[4970.86 → 4971.66] every single
[4971.66 → 4971.92] thing,
[4972.02 → 4972.22] but we
[4972.22 → 4972.58] can do
[4972.58 → 4972.90] what we
[4972.90 → 4973.14] can
[4973.14 → 4973.34] to get
[4973.34 → 4973.48] people
[4973.48 → 4973.76] excited
[4973.76 → 4973.98] about
[4973.98 → 4974.14] it.
[4974.44 → 4974.64] I
[4974.64 → 4974.92] have
[4974.92 → 4975.08] one
[4975.08 → 4975.24] more
[4975.24 → 4975.56] question
[4975.56 → 4975.70] on
[4975.70 → 4975.82] your
[4975.82 → 4976.06] open
[4976.06 → 4976.32] source
[4976.32 → 4976.64] piece.
[4976.78 → 4977.76] And as
[4977.76 → 4977.90] we
[4977.90 → 4978.20] talk
[4978.20 → 4978.40] through
[4978.40 → 4978.60] the
[4978.60 → 4979.00] agent,
[4979.18 → 4979.28] the
[4979.28 → 4979.62] firmware,
[4979.88 → 4979.96] and
[4979.96 → 4980.18] several
[4980.18 → 4980.36] other
[4980.36 → 4980.78] pieces,
[4981.74 → 4982.14] if
[4982.14 → 4982.46] someone's
[4982.46 → 4982.82] listening to
[4982.82 → 4983.10] this and
[4983.10 → 4983.20] they're
[4983.20 → 4983.50] going to
[4983.50 → 4983.84] those
[4983.84 → 4984.32] repos
[4984.32 → 4984.56] now,
[4984.64 → 4984.76] they
[4984.76 → 4985.08] seem
[4985.08 → 4985.48] a little,
[4986.22 → 4986.48] let's
[4986.48 → 4986.64] say,
[4986.76 → 4987.80] a better
[4987.80 → 4988.08] way to
[4988.08 → 4988.30] say it
[4988.30 → 4988.54] might be
[4988.54 → 4989.04] sparse.
[4989.34 → 4989.58] There's
[4989.58 → 4990.00] not a lot
[4990.00 → 4991.58] of getting
[4991.58 → 4992.04] started.
[4992.34 → 4993.02] So clearly
[4993.02 → 4993.36] some
[4993.36 → 4994.00] documentation
[4994.00 → 4994.80] is lacking
[4994.80 → 4995.16] here.
[4995.36 → 4995.92] And one
[4995.92 → 4996.56] final question
[4996.56 → 4997.16] I have
[4997.16 → 4997.60] before we
[4997.60 → 4998.06] go into
[4998.06 → 4998.98] some of
[4998.98 → 4999.08] our
[4999.08 → 4999.34] closing
[4999.34 → 4999.86] questions
[4999.86 → 5001.50] is for
[5001.50 → 5001.84] those who
[5001.84 → 5002.06] are trying
[5002.06 → 5002.46] to hack
[5002.46 → 5003.02] it or
[5003.02 → 5004.76] reprogram it
[5004.76 → 5004.98] or do
[5004.98 → 5005.50] other things
[5005.50 → 5007.08] where right
[5007.08 → 5007.38] now it
[5007.38 → 5007.82] seems like
[5007.82 → 5008.56] the resources
[5008.56 → 5009.00] to do
[5009.00 → 5009.42] that are
[5009.42 → 5009.66] a little
[5009.66 → 5010.18] lacking.
[5010.84 → 5011.22] How soon
[5011.22 → 5013.08] will those
[5013.08 → 5013.72] come online?
[5013.80 → 5014.02] Will those
[5014.02 → 5014.46] be in the
[5014.46 → 5015.02] individual
[5015.02 → 5015.80] repos?
[5016.00 → 5016.28] Will they
[5016.28 → 5018.16] be at
[5018.16 → 5018.40] some of
[5018.40 → 5019.76] the place?
[5019.88 → 5020.04] Will there
[5020.04 → 5020.38] be some
[5020.38 → 5021.16] screencasts
[5021.16 → 5021.50] about it?
[5021.54 → 5021.76] What can
[5021.76 → 5022.32] people expect
[5022.32 → 5022.70] to say
[5022.70 → 5022.92] like,
[5023.00 → 5023.26] hey,
[5024.50 → 5024.78] Lacey,
[5024.86 → 5025.10] you got to
[5025.10 → 5025.70] hold my
[5025.70 → 5026.10] hand a little
[5026.10 → 5026.32] bit.
[5026.48 → 5026.80] Get me
[5026.80 → 5027.14] started.
[5027.14 → 5027.66] How can
[5027.66 → 5028.02] I get
[5028.02 → 5028.86] to the
[5028.86 → 5029.08] hello
[5029.08 → 5029.92] world of
[5029.92 → 5031.04] the UK?
[5032.54 → 5033.02] Sure.
[5033.26 → 5034.10] So I
[5034.10 → 5034.50] plan to
[5034.50 → 5035.18] gradually
[5035.18 → 5035.76] add
[5035.76 → 5036.38] documentation
[5036.38 → 5036.94] to the
[5036.94 → 5037.40] repos.
[5037.66 → 5038.50] I just
[5038.50 → 5039.60] published
[5039.60 → 5039.92] them
[5039.92 → 5041.60] yesterday.
[5042.06 → 5042.70] So I
[5042.70 → 5043.30] haven't had
[5043.30 → 5043.68] time to
[5043.68 → 5044.04] do that.
[5044.16 → 5044.46] This is
[5044.46 → 5044.84] fresh and
[5044.84 → 5045.26] open source.
[5045.34 → 5045.56] This is
[5045.56 → 5046.06] fresh and
[5046.06 → 5046.42] new right
[5046.42 → 5046.62] here.
[5046.72 → 5047.12] This is
[5047.12 → 5047.50] as fresh
[5047.50 → 5047.74] as it
[5047.74 → 5048.08] gets.
[5048.52 → 5048.72] Yeah,
[5048.82 → 5049.74] but I
[5049.74 → 5050.14] agree that
[5050.14 → 5050.48] it's
[5050.48 → 5050.80] super
[5050.80 → 5051.40] important
[5051.40 → 5052.28] to hold
[5052.28 → 5052.82] the hand
[5052.82 → 5053.28] of other
[5053.28 → 5053.72] people.
[5054.86 → 5055.60] And this
[5055.60 → 5055.88] will be
[5055.88 → 5056.36] done for
[5056.36 → 5056.64] sure.
[5057.08 → 5057.62] I really
[5057.62 → 5058.30] want this
[5058.30 → 5059.24] to be
[5059.24 → 5060.30] easily
[5060.30 → 5061.24] digestible,
[5061.92 → 5062.30] easy to
[5062.30 → 5062.74] hack on.
[5063.44 → 5063.90] And maybe
[5063.90 → 5064.46] some grace
[5064.46 → 5065.06] back to you
[5065.06 → 5065.36] from the
[5065.36 → 5065.88] community is
[5065.88 → 5066.14] that,
[5066.14 → 5066.84] you know,
[5067.10 → 5068.88] maybe 30
[5068.88 → 5069.44] seconds,
[5069.94 → 5070.98] share what
[5070.98 → 5071.22] you've been
[5071.22 → 5071.56] going through.
[5071.56 → 5071.78] like,
[5071.82 → 5072.62] you're just
[5072.62 → 5073.30] about to
[5073.30 → 5074.04] close out
[5074.04 → 5075.96] a 104%
[5075.96 → 5077.12] funded
[5077.12 → 5078.62] project on
[5078.62 → 5079.42] crowd supply.
[5080.50 → 5080.64] You know,
[5080.70 → 5081.32] so you've
[5081.32 → 5081.72] got the
[5081.72 → 5082.14] necessary
[5082.14 → 5082.86] funding to
[5082.86 → 5083.68] do what
[5083.68 → 5083.92] you're
[5083.92 → 5084.50] promising to
[5084.50 → 5084.88] do.
[5085.76 → 5086.30] So you
[5086.30 → 5086.56] got a lot
[5086.56 → 5086.92] of pressure
[5086.92 → 5087.26] on you as
[5087.26 → 5087.60] a one
[5087.60 → 5087.88] man,
[5088.06 → 5088.58] maybe a
[5088.58 → 5089.24] two people
[5089.24 → 5089.58] show.
[5089.72 → 5089.82] I don't
[5089.82 → 5090.06] know who
[5090.06 → 5090.36] else you
[5090.36 → 5091.06] have involved
[5091.06 → 5091.58] with you.
[5091.84 → 5091.96] Yeah.
[5092.14 → 5092.36] And we
[5092.36 → 5092.66] didn't talk
[5092.66 → 5093.02] about that
[5093.02 → 5093.28] really,
[5093.28 → 5093.72] but you
[5093.72 → 5093.96] got a lot
[5093.96 → 5094.34] of pressure
[5094.34 → 5094.74] on you to
[5094.74 → 5095.22] deliver
[5095.22 → 5096.04] right now.
[5096.04 → 5096.38] And so
[5096.38 → 5096.64] you've
[5096.64 → 5096.94] got
[5096.94 → 5098.14] priorities
[5098.14 → 5099.52] and maybe
[5099.52 → 5100.14] documentation
[5100.14 → 5100.84] and getting
[5100.84 → 5101.34] started in
[5101.34 → 5101.84] Hello Worlds
[5101.84 → 5102.86] are lower
[5102.86 → 5103.22] down,
[5103.30 → 5103.62] but not
[5103.62 → 5103.98] at the
[5103.98 → 5104.30] bottom.
[5105.16 → 5106.16] So should
[5106.16 → 5106.48] I talk
[5106.48 → 5106.86] about the
[5106.86 → 5107.42] priorities?
[5107.88 → 5108.06] Yeah,
[5108.10 → 5108.40] sure.
[5108.58 → 5108.90] What are
[5108.90 → 5109.24] the closing
[5109.24 → 5109.88] priorities on
[5109.88 → 5110.38] this?
[5110.54 → 5110.58] Like,
[5110.64 → 5111.34] so you're
[5111.34 → 5112.62] on Sunday,
[5113.00 → 5113.52] it's clear
[5113.52 → 5113.80] it's going
[5113.80 → 5114.20] to be funded.
[5114.44 → 5114.82] So on
[5114.82 → 5115.18] Sunday,
[5115.18 → 5115.94] it may be
[5115.94 → 5116.40] just be
[5116.40 → 5117.02] even more
[5117.02 → 5117.62] overfunded.
[5117.80 → 5117.84] So,
[5117.90 → 5118.22] but right
[5118.22 → 5118.66] now,
[5119.14 → 5119.68] even before
[5119.68 → 5120.08] the end
[5120.08 → 5120.48] of the
[5120.48 → 5121.08] funding,
[5121.30 → 5122.06] it is
[5122.06 → 5122.66] fully funded.
[5123.20 → 5123.60] So what's
[5123.60 → 5123.90] next?
[5124.98 → 5125.18] Sure.
[5125.52 → 5125.80] So,
[5126.04 → 5127.66] now we
[5127.66 → 5128.46] should start
[5128.46 → 5129.44] to create
[5129.44 → 5130.08] the moulds
[5130.08 → 5130.98] of the
[5130.98 → 5131.98] plastic parts
[5131.98 → 5132.78] as soon
[5132.78 → 5133.38] as possible.
[5134.00 → 5135.36] So we
[5135.36 → 5136.20] should finalize
[5136.20 → 5136.76] the design
[5136.76 → 5138.30] very quickly
[5138.30 → 5138.76] because the
[5138.76 → 5139.22] mould making
[5139.22 → 5139.82] process will
[5139.82 → 5141.64] take about
[5141.64 → 5142.40] three or
[5142.40 → 5143.10] four months.
[5143.54 → 5144.50] So we
[5144.50 → 5144.78] have to
[5144.78 → 5145.14] kickstart
[5145.14 → 5145.62] it as soon
[5145.62 → 5146.16] as possible.
[5146.70 → 5147.28] So right
[5147.28 → 5147.50] now,
[5147.56 → 5148.46] this is the
[5148.46 → 5149.46] fifth generation
[5149.46 → 5150.06] prototype.
[5150.70 → 5151.56] We will
[5151.56 → 5152.76] iterate a
[5152.76 → 5153.28] little bit
[5153.28 → 5154.64] to make it
[5154.64 → 5155.18] easier to
[5155.18 → 5155.60] manufacture.
[5156.04 → 5156.76] and then
[5156.76 → 5158.80] contact
[5158.80 → 5159.14] the
[5159.14 → 5160.44] company
[5160.44 → 5162.02] who will
[5162.02 → 5162.38] create the
[5162.38 → 5162.64] moulds.
[5162.98 → 5163.24] Okay.
[5163.90 → 5165.16] And then
[5165.16 → 5166.52] gradually
[5166.52 → 5168.80] create
[5168.80 → 5169.38] mould for
[5169.38 → 5170.36] the add-on
[5170.36 → 5170.60] modules
[5170.60 → 5171.42] and in
[5171.42 → 5171.82] parallel
[5171.82 → 5173.46] develop the
[5173.46 → 5174.82] firmware
[5174.82 → 5176.10] and especially
[5176.10 → 5176.80] the agent.
[5178.08 → 5178.58] By the way,
[5178.58 → 5179.24] my partner
[5179.24 → 5180.78] Andreas is a
[5180.78 → 5181.10] mechanical
[5181.10 → 5182.76] engineer and
[5182.76 → 5183.46] he's very
[5183.46 → 5184.34] hands-on with
[5184.34 → 5184.70] these,
[5185.06 → 5185.82] the mechanical
[5185.82 → 5188.08] topics of
[5188.08 → 5188.56] the project.
[5188.68 → 5188.90] Right,
[5188.96 → 5189.10] right,
[5189.16 → 5189.38] right.
[5189.38 → 5190.08] Which is
[5190.08 → 5191.22] very different
[5191.22 → 5192.22] from outsourcing
[5192.22 → 5192.86] everything to
[5192.86 → 5194.86] China and
[5194.86 → 5196.24] expect them
[5196.24 → 5198.82] to make
[5198.82 → 5199.20] everything
[5199.20 → 5199.74] perfectly.
[5199.74 → 5200.28] because we
[5200.28 → 5200.86] could totally
[5200.86 → 5201.62] outsource
[5201.62 → 5203.48] anything,
[5204.14 → 5204.64] but then
[5204.64 → 5206.28] Andreas would
[5206.28 → 5206.88] have to fly
[5206.88 → 5208.66] out a
[5208.66 → 5209.26] dozen of
[5209.26 → 5209.94] times to
[5209.94 → 5210.62] China or
[5210.62 → 5210.98] Taiwan.
[5211.40 → 5211.78] Or live
[5211.78 → 5212.06] there.
[5212.46 → 5213.24] Or live
[5213.24 → 5213.42] there.
[5213.60 → 5213.74] Yeah,
[5213.92 → 5214.14] yeah.
[5214.14 → 5214.94] So there
[5214.94 → 5215.80] are huge
[5215.80 → 5216.06] hidden
[5216.06 → 5216.44] costs.
[5217.66 → 5218.50] So I
[5218.50 → 5219.10] think it's
[5219.10 → 5219.56] just great
[5219.56 → 5220.16] that he's
[5220.16 → 5221.24] able to
[5221.24 → 5223.54] to hop
[5223.54 → 5223.92] into the
[5223.92 → 5224.70] car and
[5224.70 → 5225.20] drive for
[5225.20 → 5226.06] an hour and
[5226.06 → 5226.48] arrive to
[5226.48 → 5226.98] the company
[5226.98 → 5228.10] and directly
[5228.10 → 5230.04] see where
[5230.04 → 5230.96] they are.
[5231.26 → 5231.40] Well,
[5231.42 → 5231.68] that's a lot
[5231.68 → 5232.42] easier than a
[5232.42 → 5232.98] plane flight,
[5233.10 → 5233.76] than a half
[5233.76 → 5234.28] day trip or
[5234.28 → 5234.64] something like
[5234.64 → 5234.84] that.
[5235.20 → 5235.88] So that's
[5235.88 → 5236.48] interesting too.
[5236.58 → 5237.70] Like I have
[5237.70 → 5238.12] to apologize
[5238.12 → 5238.86] for not
[5238.86 → 5240.52] asking you who
[5240.52 → 5241.26] else is involved
[5241.26 → 5241.90] in this because
[5241.90 → 5242.76] I guess this
[5242.76 → 5243.46] whole conversation
[5243.46 → 5243.94] people have been
[5243.94 → 5244.56] assuming it's
[5244.56 → 5245.40] just you.
[5246.08 → 5246.54] And it's
[5246.54 → 5247.82] not just you,
[5248.00 → 5248.82] it's counterparts
[5248.82 → 5249.80] that complement
[5249.80 → 5250.68] you're existing
[5250.68 → 5251.38] software development
[5251.38 → 5253.12] skills to make
[5253.12 → 5254.06] proper hardware
[5254.06 → 5255.16] and to do all
[5255.16 → 5255.58] the mechanical
[5255.58 → 5256.40] pieces and stuff
[5256.40 → 5256.84] like that.
[5257.86 → 5258.06] Yeah,
[5258.10 → 5258.64] if somebody
[5258.64 → 5259.48] takes a close
[5259.48 → 5260.04] look at the
[5260.04 → 5260.50] UK,
[5260.80 → 5261.38] it will be
[5261.38 → 5262.90] apparent that
[5262.90 → 5263.76] mechanical
[5263.76 → 5264.72] engineer is
[5264.72 → 5265.66] heavily involved
[5265.66 → 5267.12] because just
[5267.12 → 5268.84] the interconnection
[5268.84 → 5269.36] mechanism,
[5270.16 → 5272.66] these precision
[5272.66 → 5273.26] machined
[5273.26 → 5273.88] stainless
[5273.88 → 5274.52] steel parts
[5274.52 → 5276.06] and all
[5276.06 → 5276.34] of these
[5276.34 → 5276.78] mechanical
[5276.78 → 5277.34] solutions,
[5277.56 → 5278.60] it's very
[5278.60 → 5279.64] robust and
[5279.64 → 5280.20] professionally
[5280.20 → 5281.70] designed and
[5281.70 → 5282.56] Andres is a
[5282.56 → 5284.98] great mechanical
[5284.98 → 5285.88] engineer and
[5285.88 → 5287.28] perfectionist,
[5287.58 → 5288.66] so I fully
[5288.66 → 5289.26] trust him
[5289.26 → 5291.16] absolutely to
[5291.16 → 5292.42] make this
[5292.42 → 5294.24] great product.
[5294.24 → 5294.36] perfect.
[5294.86 → 5295.42] Well,
[5295.50 → 5297.14] let's stop
[5297.14 → 5297.72] tailing off the
[5297.72 → 5298.74] call to some
[5298.74 → 5299.24] of our closing
[5299.24 → 5299.74] questions,
[5300.06 → 5300.76] which were just
[5300.76 → 5301.78] as much
[5301.78 → 5302.80] interesting as
[5302.80 → 5303.68] our previous
[5303.68 → 5304.28] conversations
[5304.28 → 5305.98] around the
[5305.98 → 5306.70] UK,
[5306.96 → 5307.72] the open source
[5307.72 → 5308.20] around it,
[5308.20 → 5308.92] the platform,
[5309.08 → 5309.68] the promise,
[5309.86 → 5310.38] the hardware,
[5311.24 → 5312.08] all the ability
[5312.08 → 5313.06] to hack it to
[5313.06 → 5314.10] the hacker's
[5314.10 → 5314.86] heart's content.
[5314.86 → 5315.04] And,
[5315.24 → 5317.46] but again,
[5317.46 → 5318.16] going back to
[5318.16 → 5319.00] who you are,
[5319.40 → 5320.94] maybe the first
[5320.94 → 5321.38] question we can
[5321.38 → 5322.22] start with is
[5322.22 → 5323.06] what's something
[5323.06 → 5323.96] that's super
[5323.96 → 5325.14] secret that's
[5325.14 → 5326.60] not known by
[5326.60 → 5327.52] anybody else,
[5327.56 → 5327.98] it could be a
[5327.98 → 5328.78] personal attribute,
[5328.78 → 5330.06] it could be an
[5330.06 → 5330.80] upcoming announcement,
[5331.00 → 5331.82] but what's something
[5331.82 → 5332.78] super secret that no
[5332.78 → 5333.78] one knows about you
[5333.78 → 5334.48] or what you're doing
[5334.48 → 5335.76] that you can share
[5335.76 → 5336.34] here today on the
[5336.34 → 5336.92] show as we close
[5336.92 → 5337.20] out?
[5337.20 → 5340.62] So I'm pretty
[5340.62 → 5341.18] much a
[5341.18 → 5343.38] perfectionist and
[5343.38 → 5345.42] I take
[5345.42 → 5346.66] code quality
[5346.66 → 5347.56] very seriously
[5347.56 → 5348.84] and
[5348.84 → 5350.74] I guess
[5350.74 → 5351.56] it's challenging
[5351.56 → 5352.38] for me to
[5352.38 → 5355.14] I can work
[5355.14 → 5355.70] in a team,
[5356.36 → 5356.62] but
[5356.62 → 5358.80] I always
[5358.80 → 5359.56] strive to
[5359.56 → 5360.74] write
[5360.74 → 5361.50] super clean
[5361.50 → 5361.92] code
[5361.92 → 5363.44] that is as
[5363.44 → 5363.88] simple as
[5363.88 → 5364.32] possible
[5364.32 → 5365.20] and even
[5365.20 → 5365.80] name the
[5365.80 → 5366.42] individual
[5366.42 → 5366.86] variable
[5366.86 → 5367.60] variables
[5367.60 → 5368.48] and both
[5368.48 → 5368.86] on the
[5368.86 → 5370.02] high level
[5370.02 → 5370.98] and on the
[5370.98 → 5371.66] low level
[5371.66 → 5373.60] create something
[5373.60 → 5374.42] that is very
[5374.42 → 5374.98] easier to
[5374.98 → 5375.88] understand and
[5375.88 → 5377.02] yeah, it's a
[5377.02 → 5377.76] personal challenge
[5377.76 → 5378.62] of mine,
[5378.84 → 5380.48] but I think
[5380.48 → 5381.44] it serves
[5381.44 → 5382.92] the projects
[5382.92 → 5383.60] that I work
[5383.60 → 5384.50] on the
[5384.50 → 5384.94] long term.
[5386.20 → 5386.74] So, yeah.
[5387.30 → 5388.26] So you're a
[5388.26 → 5389.02] perfectionist.
[5389.54 → 5389.82] Yeah.
[5390.16 → 5390.42] And you're
[5390.42 → 5391.24] asking for
[5391.24 → 5392.06] grace
[5392.06 → 5395.44] on being a
[5395.44 → 5396.18] perfectionist.
[5396.18 → 5398.60] to a degree.
[5399.12 → 5399.46] That makes
[5399.46 → 5399.68] sense.
[5399.78 → 5400.04] I mean,
[5400.86 → 5402.20] we all
[5402.20 → 5402.62] want to,
[5403.16 → 5403.34] you know,
[5403.40 → 5403.76] one of the
[5403.76 → 5404.40] the biggest fears
[5404.40 → 5406.08] about doing
[5406.08 → 5406.54] something like
[5406.54 → 5406.94] you're doing,
[5407.12 → 5407.78] which is days
[5407.78 → 5408.14] away,
[5408.14 → 5409.84] and people
[5409.84 → 5410.30] are listening to
[5410.30 → 5410.68] this, and they're
[5410.68 → 5410.88] thinking,
[5411.10 → 5412.16] this thing is
[5412.16 → 5412.52] awesome.
[5412.96 → 5413.60] I want it.
[5413.66 → 5414.68] Or it's the
[5414.68 → 5415.44] the worst idea ever.
[5415.48 → 5416.06] I hate it.
[5416.30 → 5416.46] You know,
[5416.48 → 5417.20] who knows what
[5417.20 → 5417.62] they're thinking.
[5418.08 → 5418.86] I'm guessing
[5418.86 → 5419.52] the former.
[5419.52 → 5421.32] We have seen
[5421.32 → 5421.78] all these
[5421.78 → 5423.00] opinions over
[5423.00 → 5423.54] the years.
[5423.94 → 5424.28] Right.
[5424.40 → 5425.04] So you've seen
[5425.04 → 5425.70] all the opinions
[5425.70 → 5427.02] and what I'm
[5427.02 → 5427.78] thinking is that
[5427.78 → 5430.00] as makers,
[5430.46 → 5430.70] right,
[5430.74 → 5431.62] as someone
[5431.62 → 5432.34] audacious
[5432.34 → 5432.94] enough to
[5432.94 → 5433.68] actually make
[5433.68 → 5434.74] something real,
[5435.74 → 5436.82] not saying
[5436.82 → 5437.60] make an open
[5437.60 → 5438.32] source isn't
[5438.32 → 5438.60] real,
[5438.68 → 5439.08] but what I
[5439.08 → 5439.58] mean by that
[5439.58 → 5439.94] is like,
[5440.94 → 5441.46] is like,
[5441.58 → 5442.60] we just went
[5442.60 → 5443.02] back to it,
[5443.02 → 5443.50] the promise
[5443.50 → 5443.82] that you're
[5443.82 → 5444.06] making.
[5444.06 → 5444.32] Like,
[5444.40 → 5444.76] to make
[5444.76 → 5445.40] this promise
[5445.40 → 5446.04] to deliver
[5446.04 → 5446.42] what you're
[5446.42 → 5448.10] doing takes
[5448.10 → 5449.54] a lot of
[5449.54 → 5450.00] courage,
[5450.52 → 5450.82] right?
[5451.50 → 5452.42] In my opinion,
[5452.48 → 5453.02] and you may
[5453.02 → 5453.88] completely agree
[5453.88 → 5454.30] and the listeners
[5454.30 → 5454.96] may as well,
[5455.40 → 5457.06] but it requires
[5457.06 → 5458.10] so much courage
[5458.10 → 5458.70] that you might
[5458.70 → 5459.36] get to the
[5459.36 → 5460.04] point of like
[5460.04 → 5460.82] the go button,
[5460.94 → 5461.10] right?
[5461.16 → 5461.88] The button that
[5461.88 → 5462.20] says,
[5462.70 → 5463.20] okay,
[5463.66 → 5464.48] make it real.
[5465.10 → 5466.06] And the problem
[5466.06 → 5466.62] with you might
[5466.62 → 5467.12] be like,
[5467.70 → 5467.98] man,
[5468.00 → 5468.88] I'm so scared
[5468.88 → 5470.14] that this thing
[5470.14 → 5470.72] might actually be
[5470.72 → 5471.44] successful and I
[5471.44 → 5472.34] have to do
[5472.34 → 5473.86] the thing.
[5474.06 → 5474.56] I have to
[5474.56 → 5476.24] deliver, so I
[5476.24 → 5477.36] can appreciate
[5477.36 → 5479.80] the juxtaposition
[5479.80 → 5481.68] of perfectionism
[5481.68 → 5483.54] and actually
[5483.54 → 5484.42] releasing something
[5484.42 → 5485.26] because the fear
[5485.26 → 5486.20] gap between
[5486.20 → 5487.38] those two pieces
[5487.38 → 5489.00] can weigh heavy
[5489.00 → 5489.62] on the person
[5489.62 → 5490.92] doing it and
[5490.92 → 5491.68] ultimately may
[5491.68 → 5492.40] just cripple you
[5492.40 → 5492.94] and you never
[5492.94 → 5493.36] do it.
[5493.50 → 5494.02] And I'm glad
[5494.02 → 5494.58] that you got
[5494.58 → 5495.54] through it and
[5495.54 → 5495.96] did it.
[5497.22 → 5497.32] Yeah,
[5497.36 → 5498.10] but for me,
[5498.16 → 5498.76] it's a no-brainer
[5498.76 → 5500.82] because quite
[5500.82 → 5501.24] honestly,
[5501.38 → 5502.12] this is in my
[5502.12 → 5502.42] mind,
[5502.48 → 5502.96] this is the
[5502.96 → 5503.70] the coolest project
[5503.70 → 5504.76] that I can
[5504.76 → 5505.44] work on in
[5505.44 → 5506.08] this phase
[5506.08 → 5506.68] of my life.
[5506.88 → 5508.34] So really,
[5508.44 → 5508.90] there is no
[5508.90 → 5510.36] option for me.
[5510.88 → 5512.98] I just want
[5512.98 → 5513.60] to do it so
[5513.60 → 5514.94] badly and I
[5514.94 → 5515.84] think it can
[5515.84 → 5516.42] be a great
[5516.42 → 5517.38] offering for
[5517.38 → 5517.64] many.
[5518.68 → 5519.54] So maybe a
[5519.54 → 5520.52] good segue
[5520.52 → 5521.70] would be to
[5521.70 → 5523.24] talk about
[5523.24 → 5523.64] who might
[5523.64 → 5524.06] have
[5524.06 → 5525.42] influenced you.
[5525.86 → 5526.44] And so here
[5526.44 → 5526.78] on the show,
[5526.82 → 5527.98] we call that
[5527.98 → 5528.50] question,
[5528.96 → 5529.32] who's your
[5529.32 → 5530.10] programming hero?
[5530.10 → 5531.66] could be
[5531.66 → 5532.32] professor,
[5532.64 → 5533.04] could be
[5533.04 → 5533.52] mom and
[5533.52 → 5533.94] dad,
[5534.06 → 5534.62] could be
[5534.62 → 5535.72] high school
[5535.72 → 5536.34] teacher,
[5536.50 → 5536.76] could be
[5536.76 → 5537.10] whatever,
[5537.24 → 5537.76] but who is
[5537.76 → 5538.36] the hero
[5538.36 → 5538.86] in your
[5538.86 → 5539.20] life?
[5539.48 → 5540.06] Who's the
[5540.06 → 5540.72] influencer
[5540.72 → 5541.34] in your
[5541.34 → 5541.72] life,
[5542.48 → 5543.00] programmer or
[5543.00 → 5543.34] not,
[5543.34 → 5544.20] that said
[5544.20 → 5545.00] to you,
[5546.40 → 5546.74] Lace,
[5546.84 → 5547.42] you got the
[5547.42 → 5547.98] talent to do
[5547.98 → 5548.18] it,
[5548.40 → 5548.90] do it,
[5549.14 → 5549.62] or here's
[5549.62 → 5549.84] how I
[5549.84 → 5550.24] encourage you
[5550.24 → 5550.54] to do it.
[5550.54 → 5550.84] Who's your
[5550.84 → 5551.10] hero?
[5551.10 → 5552.90] Well,
[5553.32 → 5554.32] nobody has
[5554.32 → 5555.14] explicitly told
[5555.14 → 5555.88] me to do
[5555.88 → 5556.84] the UK,
[5556.96 → 5558.08] but I look
[5558.08 → 5559.64] up to a
[5559.64 → 5560.08] couple of
[5560.08 → 5560.72] people for
[5560.72 → 5561.06] sure.
[5561.44 → 5562.12] For example,
[5562.50 → 5563.02] the first
[5563.02 → 5564.94] person that
[5564.94 → 5565.76] comes to my
[5565.76 → 5566.08] mind is
[5566.08 → 5566.86] John Carmack,
[5567.18 → 5568.40] probably because
[5568.40 → 5569.96] I played too
[5569.96 → 5570.42] much Doom
[5570.42 → 5571.12] back in the
[5571.12 → 5571.64] days and
[5571.64 → 5572.98] enjoyed it
[5572.98 → 5573.42] a little bit
[5573.42 → 5573.92] too much.
[5574.30 → 5575.74] I think
[5575.74 → 5576.72] it's crazy
[5576.72 → 5577.66] that he
[5577.66 → 5579.24] could develop
[5579.24 → 5579.94] that engine
[5579.94 → 5580.56] back in the
[5580.56 → 5580.90] days.
[5581.10 → 5583.54] to smoothly
[5583.54 → 5584.58] run on
[5584.58 → 5585.92] those
[5585.92 → 5586.80] pieces.
[5588.24 → 5588.42] And
[5588.42 → 5591.24] there wasn't
[5591.24 → 5592.04] OpenGL or
[5592.04 → 5592.60] any high-level
[5592.60 → 5593.54] APIs and
[5593.54 → 5594.56] he had to
[5594.56 → 5595.08] implement it
[5595.08 → 5595.58] from the
[5595.58 → 5596.10] ground up.
[5596.84 → 5597.46] So I think
[5597.46 → 5597.88] it's a
[5597.88 → 5599.28] major
[5599.28 → 5600.42] accomplishment.
[5601.08 → 5601.98] And there
[5601.98 → 5602.60] is Jeff
[5602.60 → 5603.60] Atwood
[5603.60 → 5604.90] who created
[5604.90 → 5605.68] the
[5605.68 → 5607.82] Stack
[5607.82 → 5608.32] Exchange
[5608.32 → 5609.28] that were
[5609.28 → 5609.84] co-created.
[5609.84 → 5611.10] Jeff's been
[5611.10 → 5611.44] on the show
[5611.44 → 5611.80] before,
[5611.90 → 5612.12] Coding
[5612.12 → 5612.40] Horror.
[5612.60 → 5612.80] He's been
[5612.80 → 5613.10] on the show
[5613.10 → 5613.46] before,
[5613.56 → 5614.38] great guests.
[5615.38 → 5617.62] So easy
[5617.62 → 5618.26] to talk to
[5618.26 → 5618.90] as well.
[5620.10 → 5620.88] Super smart
[5620.88 → 5621.18] guy,
[5621.56 → 5622.10] very capable.
[5622.10 → 5625.16] smart
[5625.16 → 5625.90] entrepreneur as
[5625.90 → 5626.16] well.
[5626.38 → 5626.72] I mean,
[5626.96 → 5628.08] the way
[5628.08 → 5628.56] they built
[5628.56 → 5628.92] Stack
[5628.92 → 5629.34] Exchange
[5629.34 → 5631.04] and now
[5631.04 → 5631.56] Trello is
[5631.56 → 5632.16] a part of
[5632.16 → 5633.34] the ramifications,
[5633.82 → 5634.34] to use that
[5634.34 → 5634.82] word again,
[5635.54 → 5636.26] the ripple
[5636.26 → 5636.96] effect of
[5636.96 → 5638.10] doing what
[5638.10 → 5638.48] they did
[5638.48 → 5639.22] with Stack
[5639.22 → 5639.62] Exchange
[5639.62 → 5639.92] and all
[5639.92 → 5641.04] that was
[5641.04 → 5641.68] what we
[5641.68 → 5641.92] know as
[5641.92 → 5642.10] Trello
[5642.10 → 5642.40] today,
[5642.48 → 5642.74] which we
[5642.74 → 5643.42] use here
[5643.42 → 5643.78] internally
[5643.78 → 5644.24] at the
[5644.24 → 5644.68] Changelog.
[5644.68 → 5646.36] Honestly,
[5646.58 → 5647.14] what would
[5647.14 → 5647.46] we do
[5647.46 → 5647.90] without
[5647.90 → 5648.46] Stack
[5648.46 → 5648.96] Overflow?
[5649.44 → 5650.42] We forgot
[5650.42 → 5650.92] the program.
[5652.10 → 5652.40] We'd be
[5652.40 → 5652.96] lost.
[5653.44 → 5653.74] We'd be
[5653.74 → 5654.30] just
[5654.30 → 5655.38] coders in
[5655.38 → 5655.78] the dark,
[5655.86 → 5656.30] so to speak.
[5656.42 → 5656.74] Coders in
[5656.74 → 5657.06] the dark.
[5658.42 → 5659.30] Another guy
[5659.30 → 5659.76] is Dean
[5659.76 → 5660.34] Camera,
[5660.78 → 5661.82] author of
[5661.82 → 5662.48] the Luna
[5662.48 → 5662.94] library,
[5663.20 → 5664.66] this USB
[5664.66 → 5665.48] AVR
[5665.48 → 5665.90] library.
[5666.42 → 5667.00] I think
[5667.00 → 5667.46] it's a
[5667.46 → 5668.26] beautiful
[5668.26 → 5669.50] piece of
[5669.50 → 5670.28] software.
[5670.58 → 5670.76] I mean,
[5671.36 → 5672.50] so well
[5672.50 → 5673.32] and cleanly
[5673.32 → 5673.66] written.
[5674.84 → 5675.26] He may
[5675.26 → 5675.58] not be
[5675.58 → 5676.18] that famous,
[5676.30 → 5676.68] but I
[5676.68 → 5677.22] look up
[5677.22 → 5677.60] to him.
[5678.02 → 5678.48] And he's
[5678.48 → 5678.98] pretty young,
[5679.04 → 5679.54] by the way.
[5680.16 → 5680.78] I'm not
[5680.78 → 5681.16] sure about
[5681.16 → 5681.50] his age,
[5681.54 → 5682.18] but he's
[5682.18 → 5682.74] young and
[5682.74 → 5683.76] very talented.
[5684.90 → 5685.12] Yep,
[5685.70 → 5686.12] that's it.
[5687.04 → 5687.24] Good.
[5687.34 → 5687.44] Well,
[5687.46 → 5687.68] those are
[5687.68 → 5688.12] good heroes
[5688.12 → 5688.64] for sure.
[5688.94 → 5689.24] You know,
[5689.58 → 5690.20] one of the
[5690.20 → 5690.60] reasons why
[5690.60 → 5691.04] we do that
[5691.04 → 5691.38] segment,
[5691.52 → 5691.78] just for
[5691.78 → 5692.08] listeners'
[5692.24 → 5692.38] sake,
[5692.50 → 5692.98] that have
[5692.98 → 5693.46] been listening
[5693.46 → 5693.64] to the
[5693.64 → 5694.08] show several
[5694.08 → 5694.38] times,
[5694.46 → 5694.70] I'm like,
[5695.42 → 5695.62] you know,
[5695.66 → 5695.90] I always
[5695.90 → 5696.62] love the
[5696.62 → 5697.62] heroes part
[5697.62 → 5697.88] of it,
[5697.98 → 5698.60] but why?
[5698.82 → 5699.20] And I
[5699.20 → 5699.76] think that
[5699.76 → 5700.84] maybe this
[5700.84 → 5701.30] show is the
[5701.30 → 5702.00] the best place
[5702.00 → 5702.48] to earmark
[5702.48 → 5702.76] that,
[5702.82 → 5703.04] is to
[5703.04 → 5703.52] say that
[5703.52 → 5704.10] there's
[5704.10 → 5704.54] somebody,
[5705.34 → 5706.08] as you've
[5706.08 → 5706.38] said,
[5706.52 → 5707.02] that has
[5707.02 → 5707.56] influenced
[5707.56 → 5707.96] you,
[5708.22 → 5708.66] whether it's
[5708.66 → 5709.24] directly or
[5709.24 → 5709.66] indirectly,
[5710.54 → 5711.20] to have the
[5711.20 → 5711.68] courage to
[5711.68 → 5712.02] do what you
[5712.02 → 5712.30] do.
[5713.00 → 5713.36] And I think
[5713.36 → 5713.60] that's the
[5713.60 → 5714.20] the best reason
[5714.20 → 5714.44] why.
[5714.56 → 5714.70] Like,
[5714.76 → 5715.24] who is your
[5715.24 → 5715.54] hero?
[5716.46 → 5716.90] Pretty
[5716.90 → 5717.34] diverse.
[5717.52 → 5717.72] John
[5717.72 → 5718.24] Carmack,
[5718.44 → 5719.28] and I
[5719.28 → 5719.72] wouldn't say
[5719.72 → 5720.52] that Jeff
[5720.52 → 5721.16] Atwood is
[5721.16 → 5721.74] any less
[5721.74 → 5722.16] of a John
[5722.16 → 5722.50] Carmack,
[5722.56 → 5723.02] but he did
[5723.02 → 5723.80] not create
[5723.80 → 5724.74] what he
[5724.74 → 5725.00] created,
[5725.06 → 5725.30] which was
[5725.30 → 5725.60] like the
[5725.60 → 5726.14] Doom stuff,
[5726.26 → 5726.86] but he did
[5726.86 → 5727.22] do something
[5727.22 → 5727.80] pretty cool
[5727.80 → 5728.50] with Stack
[5728.50 → 5728.84] Exchange.
[5728.84 → 5729.18] I mean,
[5729.62 → 5729.98] so he's
[5729.98 → 5730.64] not anybody,
[5730.96 → 5731.60] but they're
[5731.60 → 5732.86] very different.
[5733.30 → 5733.40] You know,
[5733.44 → 5733.88] they're,
[5733.94 → 5735.64] to a degree,
[5735.76 → 5736.42] polar opposites,
[5736.60 → 5736.92] gaming,
[5737.16 → 5737.46] and then,
[5737.46 → 5738.02] you know,
[5738.94 → 5739.82] enriching
[5739.82 → 5740.12] developers'
[5740.28 → 5740.54] lives.
[5740.86 → 5741.92] So it's
[5741.92 → 5742.40] always interesting
[5742.40 → 5743.74] to see who's
[5743.74 → 5744.56] influenced you.
[5744.56 → 5746.50] And I
[5746.50 → 5747.06] guess the
[5747.06 → 5747.82] last closing
[5747.82 → 5748.28] questions,
[5748.42 → 5748.96] given that
[5748.96 → 5749.80] we've talked
[5749.80 → 5750.92] about the
[5750.92 → 5751.54] UK,
[5752.18 → 5752.80] the open
[5752.80 → 5753.24] source that
[5753.24 → 5754.08] powers it,
[5754.58 → 5755.26] and the
[5755.26 → 5755.88] promise and
[5755.88 → 5756.36] the platform
[5756.36 → 5756.78] that you're
[5756.78 → 5757.02] going to
[5757.02 → 5758.00] give to
[5758.00 → 5759.32] software
[5759.32 → 5760.08] developers and
[5760.08 → 5761.00] hackers around
[5761.00 → 5761.46] the world
[5761.46 → 5762.62] through this
[5762.62 → 5763.86] hardware-software
[5763.86 → 5764.50] combination,
[5765.16 → 5765.48] the only
[5765.48 → 5765.96] question I
[5765.96 → 5766.50] can think of
[5766.50 → 5767.78] to close the
[5767.78 → 5768.12] show would
[5768.12 → 5768.42] be,
[5768.90 → 5770.02] what's on
[5770.02 → 5770.44] your radar?
[5770.64 → 5770.74] Like,
[5770.84 → 5771.58] what's on
[5771.58 → 5772.06] your open
[5772.06 → 5772.52] source radar?
[5772.66 → 5773.08] What's on
[5773.08 → 5774.28] your software
[5774.28 → 5775.26] radar that's
[5775.26 → 5776.24] got you
[5776.24 → 5776.60] excited,
[5776.70 → 5777.08] that if you
[5777.08 → 5777.34] had a
[5777.34 → 5777.90] weekend that
[5777.90 → 5778.22] you weren't
[5778.22 → 5779.66] doing UK
[5779.66 → 5780.30] stuff,
[5782.14 → 5782.40] you know,
[5782.48 → 5783.44] what pieces of software,
[5783.72 → 5784.36] what projects
[5784.36 → 5784.76] would you be
[5784.76 → 5785.28] playing with,
[5785.40 → 5786.26] and why is it
[5786.26 → 5786.76] interesting to
[5786.76 → 5786.92] you?
[5788.02 → 5788.22] Yeah,
[5788.28 → 5789.02] so I'm
[5789.02 → 5789.58] interested in
[5789.58 → 5790.14] the whole
[5790.14 → 5790.84] JavaScript
[5790.84 → 5791.60] ecosystem,
[5792.68 → 5793.94] and within
[5793.94 → 5794.24] that,
[5794.46 → 5795.56] Angular
[5795.56 → 5796.88] interests me,
[5797.06 → 5798.32] and I'm
[5798.32 → 5798.96] looking forward
[5798.96 → 5800.04] to Angular
[5800.04 → 5800.40] 2.
[5801.28 → 5801.72] I would
[5801.72 → 5802.62] love to
[5802.62 → 5802.90] build
[5802.90 → 5803.94] agent on
[5803.94 → 5804.26] top of
[5804.26 → 5804.82] Angular 2,
[5804.94 → 5806.08] but right
[5806.08 → 5806.40] now,
[5806.74 → 5807.36] its API
[5807.36 → 5807.94] is in
[5807.94 → 5808.24] flux,
[5809.34 → 5810.76] and other
[5810.76 → 5811.22] than that,
[5811.32 → 5812.24] I'm interested
[5812.24 → 5812.60] about
[5812.60 → 5813.86] microcontrollers,
[5814.60 → 5816.56] and yeah,
[5817.64 → 5818.10] all the
[5818.10 → 5818.70] kind of
[5818.70 → 5819.10] this stuff.
[5819.68 → 5820.46] Good deal,
[5820.62 → 5821.10] good deal.
[5821.40 → 5822.54] Well, I
[5822.54 → 5823.22] will say,
[5823.72 → 5824.36] only because I
[5824.36 → 5824.82] have to,
[5825.28 → 5827.40] that I did
[5827.40 → 5827.98] notice that you
[5827.98 → 5828.36] did say
[5828.36 → 5828.68] Angular
[5828.68 → 5829.38] earlier,
[5829.38 → 5829.96] and I
[5829.96 → 5830.70] didn't go
[5830.70 → 5831.20] deeper on
[5831.20 → 5831.50] that for
[5831.50 → 5831.86] a reason,
[5831.98 → 5832.90] because that's
[5832.90 → 5833.18] not what the
[5833.18 → 5833.60] show's about
[5833.60 → 5833.98] today.
[5834.78 → 5835.18] However,
[5835.44 → 5836.80] there are
[5836.80 → 5837.44] some conversations
[5837.44 → 5837.82] I want to have
[5837.82 → 5838.20] with you around
[5838.20 → 5838.76] Angular that
[5838.76 → 5839.02] we're not
[5839.02 → 5839.34] going to have
[5839.34 → 5839.68] today.
[5840.20 → 5840.44] So,
[5840.68 → 5841.22] listeners out
[5841.22 → 5841.76] there thinking
[5841.76 → 5842.38] about that,
[5842.52 → 5843.00] feel that I
[5843.00 → 5843.32] feel your
[5843.32 → 5843.66] pain,
[5844.06 → 5844.46] wanted to
[5844.46 → 5844.72] have the
[5844.72 → 5845.12] conversation
[5845.12 → 5845.48] about it,
[5845.52 → 5845.86] but it just
[5845.86 → 5846.46] didn't make
[5846.46 → 5847.04] sense to have
[5847.04 → 5847.60] that conversation
[5847.60 → 5847.96] today.
[5848.60 → 5848.70] So,
[5848.78 → 5849.60] maybe some of
[5849.60 → 5850.08] the time in a
[5850.08 → 5850.68] blog post you
[5850.68 → 5851.36] can talk about
[5851.36 → 5851.88] why Angular
[5851.88 → 5852.38] for you,
[5852.86 → 5854.24] versus all the
[5854.24 → 5854.86] other options,
[5854.86 → 5855.34] obviously.
[5856.30 → 5857.14] IoT platform
[5857.14 → 5858.04] are also super
[5858.04 → 5858.42] interesting.
[5858.66 → 5859.28] I would like
[5859.28 → 5860.66] to build a
[5860.66 → 5862.64] smart home
[5862.64 → 5863.62] if I had
[5863.62 → 5864.14] time.
[5864.40 → 5864.62] Yeah,
[5865.02 → 5865.30] yeah,
[5866.30 → 5866.74] absolutely.
[5866.96 → 5867.16] Well,
[5868.08 → 5868.36] Lassie,
[5868.44 → 5869.14] it has been
[5869.14 → 5870.00] an absolute
[5870.00 → 5870.82] pleasure to
[5870.82 → 5871.32] dive deep
[5871.32 → 5871.78] with you on
[5871.78 → 5872.60] this ultimate
[5872.60 → 5873.72] hacking keyboard.
[5874.50 → 5875.50] I think that
[5875.50 → 5876.00] the promise,
[5876.16 → 5876.60] the platform,
[5876.72 → 5877.40] the open source,
[5877.50 → 5877.78] and everything
[5877.78 → 5878.16] we've talked
[5878.16 → 5878.74] about today
[5878.74 → 5880.04] is something
[5880.04 → 5880.54] that our
[5880.54 → 5881.44] audience and
[5881.44 → 5882.42] hackers around
[5882.42 → 5882.78] the world
[5882.78 → 5883.36] will resonate
[5883.36 → 5883.68] with.
[5883.90 → 5884.08] So,
[5884.08 → 5885.08] if you
[5885.08 → 5885.54] love this
[5885.54 → 5885.90] show,
[5886.08 → 5886.44] go on
[5886.44 → 5886.72] Twitter,
[5886.94 → 5887.32] mention it
[5887.32 → 5887.68] today,
[5887.92 → 5888.18] share it
[5888.18 → 5888.42] with a
[5888.42 → 5888.74] friend,
[5889.32 → 5889.76] do whatever
[5889.76 → 5890.34] it takes
[5890.34 → 5891.76] to share
[5891.76 → 5892.30] what Lassie's
[5892.30 → 5893.02] doing and
[5893.02 → 5893.80] his team
[5893.80 → 5894.64] with this
[5894.64 → 5895.00] keyboard.
[5895.12 → 5895.48] And if you
[5895.48 → 5896.16] totally appreciate
[5896.16 → 5896.56] it,
[5897.18 → 5898.02] and you use
[5898.02 → 5898.16] it,
[5898.18 → 5898.64] and you buy
[5898.64 → 5898.78] it,
[5898.80 → 5899.14] and you get
[5899.14 → 5899.42] it next
[5899.42 → 5900.10] July when
[5900.10 → 5900.56] he ships
[5900.56 → 5900.88] it,
[5901.30 → 5901.74] well,
[5901.84 → 5902.12] maybe not
[5902.12 → 5903.08] July in
[5903.08 → 5903.42] particular,
[5903.54 → 5903.96] but somewhere
[5903.96 → 5904.30] in those
[5904.30 → 5905.04] few months
[5905.04 → 5905.44] thereafter,
[5906.22 → 5906.76] and you
[5906.76 → 5907.18] love it,
[5907.28 → 5908.12] it may be
[5908.12 → 5908.56] months and
[5908.56 → 5908.98] months away
[5908.98 → 5909.32] from now
[5909.32 → 5909.60] because it's
[5909.60 → 5911.22] just near the
[5911.22 → 5911.48] turn of
[5911.48 → 5911.92] 2016,
[5912.26 → 5912.92] so we're a
[5912.92 → 5913.20] few months
[5913.20 → 5913.56] away from
[5913.56 → 5913.76] that.
[5914.08 → 5914.58] But if you
[5914.58 → 5915.02] get to that
[5915.02 → 5915.38] point and
[5915.38 → 5915.70] you're listening
[5915.70 → 5915.96] to this
[5915.96 → 5916.24] show and
[5916.24 → 5916.36] you're
[5916.36 → 5916.52] thinking,
[5916.64 → 5916.86] man,
[5917.22 → 5917.68] I love
[5917.68 → 5918.28] this thing,
[5918.72 → 5919.20] tell the
[5919.20 → 5919.96] world and
[5919.96 → 5920.46] point back
[5920.46 → 5920.68] to the
[5920.68 → 5920.90] change
[5920.90 → 5921.32] log and
[5921.32 → 5922.30] share what
[5922.30 → 5922.62] the story
[5922.62 → 5923.02] is about.
[5924.14 → 5924.90] So Lassie,
[5924.98 → 5925.28] thanks so
[5925.28 → 5925.64] much for
[5925.64 → 5926.00] coming on
[5926.00 → 5926.30] the show.
[5926.40 → 5926.56] Is there
[5926.56 → 5927.24] any closing
[5927.24 → 5927.94] thoughts you
[5927.94 → 5928.36] have that
[5928.36 → 5928.56] you want to
[5928.56 → 5928.82] share with
[5928.82 → 5929.16] the audience
[5929.16 → 5929.68] today before
[5929.68 → 5930.64] we close
[5930.64 → 5930.86] out the
[5930.86 → 5931.08] show?
[5932.50 → 5932.78] Well,
[5933.14 → 5933.58] there is
[5933.58 → 5934.62] nothing else
[5934.62 → 5935.12] on my mind,
[5935.34 → 5935.86] to be honest.
[5936.06 → 5936.90] I thank you
[5936.90 → 5937.42] very much for
[5937.42 → 5937.62] them.
[5937.98 → 5939.06] I appreciate
[5939.06 → 5940.12] it very
[5940.12 → 5940.40] much.
[5940.64 → 5940.94] Absolutely.
[5941.14 → 5941.22] Thanks for
[5941.22 → 5941.66] having me.
[5942.12 → 5942.38] Totally.
[5942.38 → 5943.00] It was great
[5943.00 → 5943.46] having you.
[5944.58 → 5945.28] Well, I do
[5945.28 → 5945.60] have a few
[5945.60 → 5946.12] people to
[5946.12 → 5946.44] thanks.
[5946.58 → 5946.84] I got
[5946.84 → 5948.18] obviously
[5948.18 → 5948.78] you, the
[5948.78 → 5949.18] listeners.
[5949.68 → 5950.32] We couldn't
[5950.32 → 5950.74] do this show
[5950.74 → 5951.22] without you.
[5951.56 → 5952.26] Your ears are
[5952.26 → 5952.84] very important.
[5954.40 → 5955.46] And we thank
[5955.46 → 5955.88] you so much
[5955.88 → 5956.38] for listening to
[5956.38 → 5957.04] the show and
[5957.04 → 5957.50] to our
[5957.50 → 5958.10] members who
[5958.10 → 5958.86] support us.
[5959.20 → 5959.98] If you go
[5959.98 → 5961.66] to changelog.com
[5961.66 → 5962.22] slash
[5962.22 → 5963.50] memberships,
[5963.68 → 5964.20] let me make
[5964.20 → 5964.58] sure that you
[5964.58 → 5964.92] are correct,
[5964.98 → 5965.18] because I
[5965.18 → 5965.56] always forget
[5965.56 → 5965.82] if it's
[5965.82 → 5966.34] plural or
[5966.34 → 5966.54] not.
[5967.92 → 5968.50] It is
[5968.50 → 5969.02] membership,
[5969.60 → 5970.44] not plural.
[5971.34 → 5972.06] I'll add a
[5972.06 → 5972.64] direct to
[5972.64 → 5973.30] memberships
[5973.30 → 5973.52] to
[5973.52 → 5974.00] membership.
[5974.24 → 5974.60] But nonetheless,
[5975.18 → 5976.02] if you go to
[5976.02 → 5976.98] changelog.com
[5976.98 → 5977.70] slash membership
[5977.70 → 5979.04] for 20 bucks
[5979.04 → 5979.74] a year, you can
[5979.74 → 5980.48] support what we're
[5980.48 → 5981.00] doing here.
[5981.10 → 5981.42] We give you
[5981.42 → 5982.20] access to our
[5982.20 → 5982.90] members only
[5982.90 → 5983.64] Slack room,
[5984.20 → 5984.72] exclusive
[5984.72 → 5985.52] discounts from
[5985.52 → 5986.48] our favourite
[5986.48 → 5987.30] products and
[5987.30 → 5987.90] most trusted
[5987.90 → 5988.54] partners,
[5989.42 → 5990.18] unrestrictive
[5990.18 → 5991.30] access to our
[5991.30 → 5992.16] archives, which
[5992.16 → 5992.84] can be Googled,
[5993.14 → 5993.56] but nonetheless,
[5993.76 → 5994.30] you can't find
[5994.30 → 5994.96] them easily just
[5994.96 → 5996.00] by clicking
[5996.00 → 5996.34] around the
[5996.34 → 5996.62] site.
[5997.06 → 5997.68] And then also,
[5997.82 → 5998.50] if you want a
[5998.50 → 5999.60] changelog tea to
[5999.60 → 6000.62] outfit yourself with,
[6001.16 → 6001.82] we give you that
[6001.82 → 6002.82] basically at cost,
[6002.90 → 6003.72] half off,
[6003.94 → 6004.72] because we love
[6004.72 → 6006.16] our listeners and
[6006.16 → 6007.10] our members.
[6007.82 → 6009.20] We also love our
[6009.20 → 6009.78] sponsors.
[6010.16 → 6010.92] Those sponsors are
[6010.92 → 6011.52] Code Ship,
[6012.20 → 6012.86] Top Tile, which we
[6012.86 → 6014.14] mentioned, so Top Tile,
[6014.20 → 6014.90] big shout out to you
[6014.90 → 6015.98] today on this show.
[6016.52 → 6017.64] Harvest, love
[6017.64 → 6018.56] tracking time with
[6018.56 → 6019.68] Harvest, and
[6019.68 → 6020.16] Linde.
[6020.64 → 6021.62] Linde is awesome.
[6022.08 → 6023.26] VPSs that are just
[6023.26 → 6024.16] tried and true in
[6024.16 → 6024.54] Linux.
[6025.34 → 6026.54] Easiest way to get up
[6026.54 → 6028.02] on the internet with
[6028.02 → 6028.48] Linde.
[6029.44 → 6030.14] Thanks so much to
[6030.14 → 6030.58] those guys for
[6030.58 → 6031.14] supporting the show,
[6031.28 → 6031.98] and thanks so much
[6031.98 → 6033.20] to you, Lacey, and
[6033.20 → 6033.90] everyone else for
[6033.90 → 6035.50] joining us on this
[6035.50 → 6036.10] show today.
[6036.26 → 6037.16] And with that,
[6037.90 → 6038.64] let's say goodbye.
[6039.04 → 6039.64] Thanks for that.
[6039.86 → 6040.08] Bye, Bill.
[6040.08 → 6040.10] Bye, Bill.
[6040.10 → 6040.20] Bye, Bill.
[6040.20 → 6040.52] Bye, Bill.
[6040.52 → 6041.82] Bye, Bill.
[6041.82 → 6042.00] Bye, Bill.
[6042.00 → 6071.98] Outro Music
