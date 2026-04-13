[0.00 → 4.74] This week's episode is sponsored by Tweet Bot, a full-featured iPhone Twitter client with a lot of personality.
[5.44 → 11.98] Whether it's a meticulously crafted interface, sounds, and animation, or features like multiple timelines and smart gestures,
[12.34 → 13.72] there's a lot to love about Tweet Bot.
[14.10 → 19.08] You can find Tweet Bot in the App Store or head to tapbots.com slash tweet bot to learn more.
[30.00 → 34.00] Don't push me away!
[60.00 → 67.04] Fun episode this week, talk to the guys at CDNJS, more Aussie Java Scripters from down under.
[67.40 → 71.96] Yeah, apparently they don't do much with sports, so they dig deep into JavaScript.
[72.38 → 75.48] That's kind of a national pastime, so we're gathering down there.
[76.26 → 78.78] The CDNJS project is pretty interesting.
[78.78 → 89.22] It's a way to put, I think, the second-tier JavaScript frameworks up on a CDN for the world to share.
[89.22 → 89.62] Absolutely.
[90.32 → 94.44] They also announced some good brand-new sponsorships, so stay tuned for that in the show.
[94.74 → 95.18] Absolutely.
[95.40 → 99.76] Speaking of sponsors, we're glad to be part of Fusion Podcast Network now.
[100.10 → 100.58] That's right.
[101.02 → 106.30] It's our second episode up on that, and excited to be part of that excellent network.
[106.78 → 108.14] Where can folks catch up with us?
[108.46 → 112.44] Well, on the blog, thechangelog.com, and on Twitter, Changelog Show.
[112.64 → 115.50] What about it in person, to come up and say hi and get a Changelog sticker?
[115.74 → 116.48] Oh, yeah, that's right.
[116.58 → 117.02] Big D.
[117.02 → 117.18] Big D.
[117.54 → 119.36] Big D conference, design conference.
[119.48 → 124.02] It's one of the better design conferences that I've attended right here in Dallas.
[124.12 → 124.84] You'll be up for that.
[125.14 → 126.22] I'll be up for that as well, yeah.
[126.38 → 128.98] It's in July, and then we've got Lone Star Ruby Comp in August.
[129.06 → 129.74] Looking forward to that.
[130.20 → 130.56] Always.
[131.28 → 131.64] Always.
[131.74 → 132.56] It's a fun episode this week.
[132.60 → 133.14] Should we get to it?
[133.34 → 134.02] Let's do it.
[134.02 → 134.46] Let's do it.
[134.46 → 149.08] We're chatting today with the folks behind CDNJS, Ryan Kirkman and Thomas Davis.
[149.08 → 153.62] So, Thomas, why don't you go first and introduce yourself a little bit about your day job, and
[153.62 → 155.56] then we'll let Ryan introduce himself.
[156.50 → 157.00] No problem.
[157.00 → 157.52] Thanks for that.
[158.18 → 162.96] So, I'm a 21-year-old from Australia and a heavy JavaScript developer at the moment.
[163.80 → 170.96] I did a computer science degree at a university, and I've been freelancing web development for
[170.96 → 172.66] the last three to four years.
[173.06 → 178.50] But I started when I was 14, so it'll be my eighth year of web developing so far.
[178.50 → 181.40] How long do you usually speak for, sorry?
[182.10 → 183.06] That's fine, Ryan.
[184.38 → 188.12] I'm still in shock about the eight years of experience at 21.
[188.86 → 189.64] Yeah, no, that's great.
[191.22 → 194.26] Yeah, so I'm a little bit like Thomas in that regard.
[194.26 → 198.72] I did a software engineering degree at UP, University of Queensland in Australia.
[199.80 → 204.62] So, I guess I've been making websites not as long as Thomas here, but for quite a few
[204.62 → 205.18] years now.
[205.18 → 211.66] So, previously, I've been doing JavaScript development, much like Thomas.
[211.76 → 214.06] We've been working together for the last six months.
[215.32 → 220.88] And yeah, so we started CDN.js one fine day when we decided the web needed to be a faster
[220.88 → 222.42] and easier place for web developers.
[223.42 → 225.40] So, we'll get into CDN.js in just a moment.
[225.62 → 232.22] So, our buddy, Michael Smith from Down Under is a JavaScript child prodigy himself.
[232.44 → 233.92] Is he even 20 yet, Adam?
[234.08 → 234.86] I don't think he is.
[234.86 → 236.84] No, I don't think he's even able to drink.
[237.20 → 241.30] So, I want to know just what it is about the Australian culture that just breeds JavaScript
[241.30 → 241.82] developers.
[242.04 → 246.40] And you guys just not have basketball or rugby or something else to occupy your time these
[246.40 → 246.68] days?
[247.80 → 252.56] Well, I guess we don't have as big sports advertising budgets.
[252.56 → 255.10] So, we have to turn to the internet for our entertainment down under.
[255.10 → 262.16] So, CDN.js for the folks that don't know, give a little background around this project and
[262.16 → 263.22] what it aims to solve.
[264.34 → 264.64] All right.
[264.68 → 265.00] So, yeah.
[265.06 → 269.22] Basically, we started CDN.js one day when we were just pumping out websites.
[269.22 → 273.38] And we were finding that we had to copy these scripts over and over to all of these different
[273.38 → 273.84] websites.
[273.84 → 277.46] And we were using the Google API CDN.
[277.68 → 279.48] And that was a fantastic resource.
[279.48 → 281.94] If you want jQuery, it's fast.
[282.18 → 283.44] It's the latest version.
[283.44 → 288.26] And it's probably on a server pretty close to your location.
[288.54 → 289.62] So, it's perfect.
[290.16 → 294.66] And we thought, you know, we're using things like backbone.js, underscore.js.
[294.86 → 296.68] Wouldn't it be cool if these were on a CDN?
[297.44 → 301.56] Now, the Google CDN, you really have no avenue for adding a script to that.
[301.56 → 305.32] So, we thought, you know, why isn't there a place where you can add your, you know, your
[305.32 → 306.92] favourite script or a popular script?
[307.34 → 313.02] We also went on the Google forums to suggest scripts such as backbone and underscore and other
[313.02 → 314.10] pub knob.js.
[314.62 → 320.34] But the actual Google forums, even though they have, what, 500 updates to upload a script,
[320.52 → 322.52] they weren't very receptive in that manner.
[323.36 → 324.14] Which was fair enough.
[324.20 → 324.90] They are each company.
[325.14 → 328.00] But it seemed like something that was required.
[328.68 → 332.94] So, we basically wanted to build a service that was community-driven and that responded
[332.94 → 335.24] much more quickly than anything else that's out there.
[336.20 → 338.44] So, CDN.js is the result of that.
[338.44 → 343.24] Well, since you talk about quickness, what is the response time for, say, me forking and
[343.24 → 347.76] adding my favourite script and or library and it being live and available?
[348.76 → 353.44] I mean, assuming we deem it appropriate for CDN.js, as in it's got significant community
[353.44 → 355.84] backing, and it's popular and well-respected.
[356.44 → 359.34] I mean, turnaround time is, you know, 24 to 48 hours.
[360.32 → 366.78] Do you, in terms of being well-respected and popular, is that your say, or who gives the
[366.78 → 367.56] final cut on that?
[368.66 → 372.74] Well, we do have quite a bit of a say at the moment because the community isn't really
[372.74 → 377.42] large enough to show, like, the real numbers behind how popular a script is.
[377.94 → 383.72] But eventually, we would prefer the we have a user voice account where people suggest
[383.72 → 384.84] scripts they were not uploaded.
[385.44 → 389.78] And we would prefer in the future, you know, not uploading a script unless it has over 1,000
[389.78 → 392.34] or 2,000 votes to be included on the CDN.
[393.18 → 399.12] The more scripts we upload that are possibly obscure or not even quality means there's a
[399.12 → 402.86] lot more maintenance as far as keeping CDN.js a worthy tool.
[403.92 → 409.44] So basically, you have a prerequisite for, okay, if your project has this much reach or this
[409.44 → 413.80] kind of community behind it, then it's probably a good fit for CDN.js.
[413.80 → 417.60] Yeah, that's exactly what we're aiming for.
[417.72 → 422.68] So right now, it's kind of like we're aiming for a meritocracy, but at the moment, we basically
[422.68 → 427.76] have two benevolent dictators for life, but we prefer to move more towards a meritocracy
[427.76 → 429.54] type approach as we gain more traction.
[430.70 → 433.90] And from what I understand, you guys are a non-profit, so this is a non-profit initiative.
[434.24 → 435.04] It's something you guys started.
[435.18 → 440.04] Is this something that's, I mean, Thomas, you said you're 21, and Ryan, I didn't catch your
[440.04 → 441.46] age, but you're probably just as old, right?
[441.46 → 443.38] So I mean, this is kind of new to you guys.
[443.44 → 444.80] What got you into this non-profit scene?
[444.86 → 449.56] Is it just about CDN.js, or is it, where do you plan on taking this particular initiative?
[450.74 → 454.82] I mean, CDN.js, from our perspective, was just about sort of helping the web developer
[454.82 → 459.36] community and sort of making the web faster by serving these scripts on a CDN.
[459.78 → 464.98] The non-profit thing was just, I don't know, I don't really think that a resource like this
[464.98 → 465.92] should be for profit.
[465.92 → 472.18] And it seems like it has much more benefit for everybody, especially the community, if
[472.18 → 476.66] it is a sort of community-driven thing, and they have the ability to sort of review anything
[476.66 → 477.46] that we put out there.
[477.72 → 483.10] At the very least, it was an attempt at innovating the web, or getting a collection of scripts
[483.10 → 483.92] into a CDN.
[485.52 → 490.32] It didn't really, we weren't overly concerned as to where we took it.
[490.32 → 491.96] Like, we didn't expect to go global.
[493.32 → 498.50] But I think everyone that's in this audience should know what a CDN is, in case we have
[498.50 → 501.48] some folks that stumbled across the podcast and don't know.
[501.66 → 502.64] What is a CDN?
[503.66 → 505.42] A content delivery network.
[505.68 → 512.54] So basically, if you have a JavaScript library, let's say jQuery, everyone should have an idea
[512.54 → 519.70] of what jQuery is, and you have your servers, let's say, are in America, but you have some
[519.70 → 524.52] poor souls like us living in Australia, your website's probably going to load a bit slower.
[524.68 → 530.72] So what a content delivery network does is they might have some servers in Sydney, which
[530.72 → 533.78] is much closer for us kangaroo-riding people.
[534.64 → 539.42] And so our scripts are going to load much faster if we have servers in our country than us having
[539.42 → 543.60] to go all the way across the ocean to grab the scripts from American servers, things
[543.60 → 544.00] like that.
[544.28 → 547.66] It also adds in fail-sleeves to file loading.
[547.78 → 552.18] Like, if your server can't find a file, if it fails at one location, it will choose another
[552.18 → 553.30] location to serve it from.
[554.26 → 555.14] And, yeah.
[556.38 → 560.82] So typically, in the past, these things have been for private assets that are kind of on
[560.82 → 563.88] an application-specific basis, right?
[563.88 → 569.88] So I guess what makes CDN.js unique is that you guys are offloading shared resources.
[570.80 → 570.92] Yeah.
[571.08 → 576.20] So I guess things like, if I understand you correctly, things like sort of CloudFront have
[576.20 → 581.92] opened up that previously sort of private CDN-type thing.
[584.92 → 588.02] And, of course, our sponsoring company, CloudFront.
[588.02 → 588.46] Yeah.
[589.40 → 589.68] Yeah.
[589.70 → 594.76] So traditionally, Akamai, I guess probably the pioneers of the space, provided their
[594.76 → 601.34] servers and bandwidth for fees to put assets closer to users for applications.
[601.34 → 604.32] But it was pretty much everybody had to rent that space and rent that bandwidth.
[605.18 → 607.80] And it was just a matter of serving up your own assets.
[607.94 → 612.82] But I guess what makes this unique is that you're serving up assets that, since they're
[612.82 → 616.08] common frameworks, multiple applications can take advantage of those.
[616.90 → 617.34] Yeah, definitely.
[617.34 → 622.22] So Cloudflare, our new partnership, they aim at improving the web.
[622.40 → 625.84] And they synchronize a lot of common resources across websites.
[626.50 → 631.74] And so it only made sense to synchronize these common shared JavaScript libraries and make
[631.74 → 637.10] them load much faster for all users, which takes a lot of strain off developers also.
[638.08 → 640.28] Now, you put JS right there in the name.
[640.38 → 645.80] But are you going to look at any other types of assets other than JavaScript, maybe CSS or other
[645.80 → 646.10] frameworks?
[646.10 → 649.28] I mean, that's a possibility in the future.
[649.40 → 653.10] But right now, we'd sort of like to focus on the JavaScript side of things.
[653.76 → 655.80] I guess the service is still quite young.
[655.92 → 658.60] It's only sort of, you know, half a year old at this point in time.
[658.66 → 660.00] So it's still in its infancy.
[660.32 → 664.82] So we're just sort of trying to find a fit for it in the open source world type of thing.
[664.98 → 667.86] There aren't particularly too many shared CSS resources either.
[667.86 → 669.76] I could probably only count two myself.
[670.44 → 673.58] Well, you start talking about some of those shared other ones besides JavaScript.
[673.78 → 678.22] You've got Cached Commons, which does things like Swift files as well.
[678.50 → 683.96] And I think it's mostly JavaScript, but they seem to have a couple additional libraries beyond
[683.96 → 686.04] like fonts and markup and text editors.
[686.04 → 688.14] And it's not just JavaScript.
[688.44 → 691.10] So how is this different from, say, Cached Commons?
[692.18 → 699.48] I mean, essentially, Cached Commons and CDN and JS aren't so much different in their sort
[699.48 → 702.06] of their vision or their goal.
[702.06 → 708.32] It's just that Cached Commons was originally, and I think it still is, hosted on GitHub, which
[708.32 → 712.82] means it's probably not leveraging a content distribution network.
[713.06 → 718.04] And if it is, maybe not as effectively as we're able to, because we actually sort of control
[718.04 → 720.14] the content delivery network that we're using.
[721.78 → 728.30] And I think one of the things that we aim to try to solve, too, is we're trying to sort
[728.30 → 734.18] of move quite quickly in terms of keeping our libraries updated and sort of accepting new
[734.18 → 734.80] pull requests.
[735.12 → 738.94] So I think that was a problem that people have found in the past with other solutions.
[739.42 → 742.98] I think we've also, we also try to involve the community much more.
[743.34 → 746.90] It's, we like to make it as community-involved as possible.
[747.68 → 751.26] And we have, we actually have quite a lot of people who do support CDN.js.
[751.26 → 753.80] And I guess we'll have a shout-out to everyone.
[753.80 → 758.08] And thanks so far for helping out with Volker Quest.
[759.68 → 764.40] Yeah, on the note of Cached Commons, too, I've had a chat with, in the back channel,
[765.28 → 768.74] about a week back, with Lance, the guy behind Cached Commons.
[768.86 → 771.20] And he is actually discontinuing that project.
[771.34 → 776.62] He said he's been, he's been focusing on his company, getting off, getting off the ground
[776.62 → 777.84] for the past eight or so months.
[777.84 → 780.46] So he hasn't had much time to dedicate to Cached Commons.
[780.46 → 786.36] And you can probably guys validate this, but he said he's talked to you guys about CDN.js
[786.36 → 787.26] and where it's going.
[787.38 → 792.38] And he's hoping to possibly lend his contributions when he has time opened up.
[792.48 → 794.52] But pretty much he thinks you guys have a solid plan.
[795.08 → 799.64] And he says whatever's 100% free, clean, up-to-date, and user-driven is awesome.
[799.64 → 800.48] So he's all for it.
[800.48 → 806.20] Yeah, no, it's been fantastic talking to sort of icons in the community like Lance.
[806.54 → 812.16] And we're sort of really looking forward to working together with this sort of big names
[812.16 → 815.82] in the community just to push this forward, as you say.
[816.14 → 820.30] And everyone seems to be pretty excited about sort of where this is going.
[820.30 → 822.66] So, yeah, we're pretty excited as well.
[822.66 → 830.14] Do you have any standardization on minification or packaging formats for these JavaScript's?
[830.86 → 834.78] So currently we're using Coleman.js package formats.
[835.52 → 837.78] It's an initiative that someone started.
[837.90 → 839.08] I couldn't credit it, sorry.
[839.72 → 845.84] But Node.js packages, NPM, uses the same format, I guess.
[845.84 → 855.48] And so we require all our forks to contain a package.Jason, which just lists the basic information
[855.48 → 864.14] about the file, such as author, the author's, the file name, a few tags about what the library is,
[864.14 → 866.20] a short description of what the library does.
[867.42 → 871.76] And so each one of our libraries has one of these packages.Jason associated with it.
[871.76 → 877.96] And we pull that information in to use it on the client side for the website.
[878.30 → 884.68] And tools such as CDN.js command uses these packages.Jason to generate useful information,
[885.12 → 888.56] which helps developers choose which libraries they want to implement.
[889.26 → 891.54] And you mentioned minification in there.
[891.72 → 897.56] So our policy on minification is that we prefer the library maintainers to take responsibility for that.
[897.56 → 904.26] The reason for that is if we use a minified that for some reason breaks a developer's library,
[904.90 → 906.78] we don't want to be held accountable for that.
[907.12 → 910.92] So by and large, we much prefer that libraries are sort of minified,
[911.30 → 914.76] and preferably in the repository that they specify in their metadata.
[915.58 → 922.62] In some rare cases, we will minify libraries that don't have any minified version available.
[922.62 → 926.34] You mentioned Google's CDN earlier.
[927.04 → 932.12] On the Google site, you've got a couple different options to reference these applications,
[932.62 → 936.50] or the frameworks you can link to them directly in the head,
[936.58 → 938.72] or you can go through their script loader.
[939.28 → 943.02] How can you reference these packages from CDN.js?
[944.22 → 945.64] So at the moment, you have to do it manually.
[946.82 → 947.96] The URLs are included.
[948.56 → 950.40] You have to copy them into your code manually, sorry.
[950.40 → 957.08] Anyway, we're working on tools such as JavaScript loader to implement them.
[958.32 → 960.24] But at the moment, it's not quite necessary,
[960.64 → 963.50] and you can already implement your own loader
[963.50 → 969.22] and just use the CDN URLs to load the scripts, I guess.
[969.22 → 977.00] We will actually be working on a tool that lets you download the local files also.
[977.98 → 981.02] So if the CDN ever goes down for some bizarre reason,
[981.74 → 983.92] like Google CDN has gone down before, for example,
[984.70 → 988.34] we're making a tool that lets you back up the local files,
[988.54 → 993.74] and if the CDN link fails, it'll fall back to the local script.
[993.74 → 999.66] And our HTML5 boilerplate by Paul Irish actually implements this for the jQuery.
[1000.70 → 1006.64] If the jQuery CDN fails, it implements the local jQuery file in the HTML5 boilerplate.
[1008.04 → 1010.04] How are you guys handling versioning?
[1010.04 → 1019.26] Yeah, so this is another thing that we prefer library maintainers to take responsibility for.
[1020.14 → 1022.36] Most scripts will generally have a version number.
[1022.48 → 1026.38] For example, with jQuery, we're up to 1.6 point something right now.
[1027.42 → 1031.78] Almost every other script that we have on CDN.js right now
[1031.78 → 1033.64] has that sort of version number.
[1034.40 → 1037.42] And, I mean, that's available as part of the URL.
[1037.76 → 1043.38] So, I mean, it's sort of, I guess, it's fairly obvious which version of the script you're using.
[1044.00 → 1045.08] What about older versions?
[1045.44 → 1048.06] How long are you going to keep older versions around?
[1048.56 → 1053.26] So Cloudflare, our sponsors, they will be hosting the files indefinitely.
[1053.56 → 1057.44] So any files that are uploaded at any stage will remain there forever.
[1058.60 → 1061.12] So you can think of it as a write-only file store.
[1061.12 → 1063.94] Anything we put in there is going to be in there forever, essentially.
[1064.86 → 1068.50] What about package management or dependencies among these?
[1068.64 → 1073.82] I noticed that Micro.js tends to be getting a lot of play in the JavaScript community lately.
[1074.10 → 1077.94] And, you know, with Ender, you can basically roll your own little micro framework.
[1078.16 → 1081.26] Any plans to mix and match and cache those versions?
[1082.22 → 1086.96] So, personally, CDN.js will probably already be enough for us to maintain.
[1086.96 → 1092.82] Building a dependency package manager is possibly too much work for us to handle and update.
[1093.42 → 1095.84] So, again, we would prefer that would be a community initiative.
[1096.34 → 1101.06] So things such as CDN.js command built by RSA-Cruz.
[1101.06 → 1105.28] He may implement dependency management.
[1106.02 → 1111.10] But we'll probably prefer the community generate tools that handle such things.
[1112.44 → 1117.94] So you've got to be doing something with JavaScript to get into this particular project.
[1118.04 → 1119.90] So what are you guys actually doing with these frameworks?
[1119.90 → 1123.12] We've been working on a product of ours.
[1123.28 → 1125.00] It's a web application.
[1125.98 → 1127.94] But we'd prefer not to announce it on here.
[1128.32 → 1135.12] But basically, it's made exceptionally heavy use of quite a few of the libraries that we host on CDN.js.
[1135.56 → 1141.38] And it was our initial inspiration for sort of creating the service.
[1141.38 → 1146.16] So it's a single-page web application built using Backbone.js by Jeremy Askings.
[1146.46 → 1149.14] And we use Node.js for the server.
[1149.56 → 1151.54] And we use Couch DB for the database.
[1152.24 → 1156.96] And Couch DB relies on JavaScript for the views and queries.
[1157.84 → 1161.30] So it's pretty much our entire code base is JavaScript at the moment.
[1161.44 → 1162.70] 100% on GitHub, actually.
[1163.54 → 1165.50] So, yeah, it's JavaScript all the way down.
[1166.24 → 1168.24] I don't want to announce it on here.
[1168.32 → 1168.96] What are you waiting for?
[1169.08 → 1170.20] Wake up Sydney or...?
[1170.20 → 1173.52] Well, it's only in beta.
[1174.00 → 1175.82] And we're possibly ashamed of it at the moment.
[1176.08 → 1178.38] But it's called Proposal, sorry.
[1178.98 → 1181.78] It's pretty much a fresh book for proposal generation.
[1182.34 → 1184.62] So instead of generating invoices, we generate proposals.
[1185.44 → 1190.08] And we like to aggregate the accepting and decline rates of your proposals.
[1191.08 → 1192.40] Doesn't seem that embarrassing to me.
[1192.42 → 1193.14] It looks pretty all right.
[1194.46 → 1198.22] From two developers, I mean, it looks just as good as CDN.js.
[1198.22 → 1203.38] Well, I mean, yeah, we have a fantastic designer here.
[1203.74 → 1205.36] I'm not changing the designer at all.
[1207.68 → 1214.24] We might have to pull them to the side and have a drink with them and teach them about SaaS and Compass and frameworks and stuff.
[1214.90 → 1216.34] Speaking of drinking, that's your cue.
[1216.34 → 1220.26] What are you guys doing on the server?
[1221.26 → 1221.46] Node?
[1221.46 → 1224.34] Yeah, so the server is Node.js.
[1225.20 → 1234.98] And basically, we're trying to make it a RESTful service and effectively build our service such that we're using our own API to sort of work with the client side.
[1234.98 → 1240.94] I mean, the client side and the server side are completely sort of reintegrated, so to speak.
[1240.94 → 1241.06] Yeah.
[1241.16 → 1245.46] So at the moment, Ryan actually is working heavily on Node.js, and I prefer to stick to the client side.
[1245.88 → 1254.44] And we prefer to make our projects independent so that my client side can interact with anything Ryan throws at me through his API.
[1254.44 → 1259.74] Is that API documented anywhere, or is that something that's public that we can kind of trudge through?
[1260.62 → 1262.90] No, that's absolutely not at this point in time.
[1263.06 → 1267.78] It's still very much in beta and very much for internal use only at this point in time.
[1267.86 → 1272.82] But that's definitely something we plan to look into releasing in the future.
[1273.20 → 1279.02] So I haven't driven into CDN.js command that Jim available to ping in there.
[1279.02 → 1283.92] How is he kind of pulling back different things, or is he just hacking the URL and pulling back different data?
[1284.74 → 1289.78] Yeah, so he's actually pulling back the packages.Jason, which is included with each library.
[1290.16 → 1290.42] Okay.
[1290.52 → 1291.96] So he's using that information.
[1292.10 → 1293.36] There's a concatenated version.
[1293.78 → 1300.70] There's a concatenated file which contains every single package.Jason in one file called packages.Jason.
[1301.12 → 1303.90] And you can actually access that through CDN.js.com.
[1304.28 → 1306.40] It's one of the resources that get loaded in.
[1306.40 → 1310.18] So I hear that you guys have a pretty good uptime.
[1310.48 → 1316.76] I guess this kind of leverages into what you're doing, Ryan, with Node and what you're doing on the front end as well.
[1316.76 → 1321.76] But I go to your ping in stats, and it's basically 100% uptime for quite a while now.
[1321.96 → 1325.60] What is it that you think that attributes to this percentage of uptime?
[1326.84 → 1331.28] Yeah, so up until now, we've been using CloudFront as our CDN.
[1331.28 → 1335.70] And so essentially, CloudFront's just been rock solid.
[1337.74 → 1339.74] Yeah, really, that's essentially it.
[1340.74 → 1341.82] That's not how it works for you?
[1342.70 → 1348.94] Yeah, I mean, so with this service, we wanted to sort of stand on the shoulders of giants, so to speak.
[1348.94 → 1356.64] So to use sort of the best of breed sort of software and services out there to ensure that it's the best possible thing.
[1356.96 → 1361.00] Ryan and I actually live together, and we argue for hours and hours on every decision we make.
[1361.00 → 1365.88] And I'm surprised I haven't killed him yet, but it actually works out for best practices, I guess.
[1366.78 → 1373.96] So if, I guess, building a system like this, where are the common places, you know, a CDN in general, where are some of the common places it would break?
[1373.96 → 1379.16] And what are some of the things that you're using that mitigates and prevents that breakage?
[1380.34 → 1388.10] Yeah, so if we had decided to roll our own sort of servers or something, that would have been a massive task to undertake.
[1388.10 → 1392.48] We would have had to maintain sort of the servers, do all that sysadmin stuff.
[1392.98 → 1395.04] So that was really impractical.
[1395.42 → 1402.90] We needed some way to focus on sort of focus on the product rather than focus on all the administration behind the product.
[1402.90 → 1416.64] And sort of things such as Amazon Web Services have given us the ability to focus on sort of the product itself rather than the management and the housekeeping behind it.
[1417.18 → 1425.02] So that's really only been an option in the past sort of a couple of years, which is really exciting, actually, that you can do something like this.
[1425.02 → 1432.66] But I was curious if you wanted to chime in with some questions about the recent outage and how they're handling that.
[1433.40 → 1438.04] Yeah, so you're probably talking about the Amazon EC2.
[1438.30 → 1438.52] Yeah.
[1438.98 → 1441.96] Yeah, so that was a massive outage.
[1442.14 → 1446.28] But luckily for us, it didn't roll over into any of their other services.
[1446.28 → 1455.34] So Cloudflare and – sorry, not Cloudflare, CloudFront and S3, they were completely fine, rock solid all the way through.
[1455.66 → 1458.46] But again, I'm working on it right now.
[1459.28 → 1462.20] We will be implementing the local fallbacks.
[1463.18 → 1466.32] It's good to always prepare for any situation.
[1466.32 → 1472.82] And we will be including the HTML5 boilerplate code for every library instead of just gate jQuery.
[1473.56 → 1484.56] And we will make it accessible to any users or developers who access cdnjs.com to download their files instantly and get the code that provides a local fallback.
[1485.16 → 1490.00] And that will always at least be a failsafe for any CDNs outages.
[1490.00 → 1502.12] So I guess in full answer to your question, yes, if the infrastructure or the service that we're using to serve our files does go down, then all of our links will go down.
[1502.30 → 1509.34] But the fact of the matter is services like CloudFront and Cloudflare can do a much better job than we ever could.
[1509.56 → 1511.84] So we'd prefer to leave it in experts' hands.
[1511.84 → 1518.00] I think at the moment Cloudflare is actually saving 2 billion or 3 billion page views a month.
[1518.48 → 1521.92] Something like 65,000 requests a second or something.
[1522.16 → 1522.56] I'm not sure.
[1523.42 → 1528.12] So they're definitely capable of handling this CDN as it is.
[1529.56 → 1531.36] So let's talk about traffic for a bit here.
[1531.92 → 1534.74] In terms of you launched in January.
[1535.00 → 1535.84] It's now June.
[1535.92 → 1538.46] So we're looking at just even six months.
[1538.46 → 1545.52] I can see your stats and I can tell the listeners what's going on here because you're actually linking to it.
[1545.58 → 1557.30] But give us a gist of what's happened in terms of the traffic and just general hits, I guess, files hits, page hits, and just overall traffic of CDN.js.
[1558.10 → 1558.58] Yeah.
[1558.68 → 1564.44] So, I mean, when we launched in January, for the month of January, we only got about 107,000 hits.
[1564.78 → 1567.22] But since then, it's kind of taken off.
[1567.22 → 1569.74] We've had double-digit month-on-month growth.
[1570.46 → 1573.76] Sort of February, we were serving 500,000 scripts.
[1574.00 → 1574.96] March, almost a million.
[1576.34 → 1581.78] And by the time we got to the end of May, we're serving, you know, around 2 million scripts a month.
[1581.88 → 1583.98] This month, we're set to go way past that.
[1584.12 → 1589.28] So we understood the exponential behaviour of a CDN that provides JavaScript libraries.
[1589.28 → 1593.06] So we've never actually publicized or advertised CDN.js.
[1593.42 → 1598.14] As with, like, the first six months, we considered to be, like, an iteration period, a bug-finding period.
[1598.70 → 1602.22] And we've actually knotted out bugs in the past, which has been great.
[1602.36 → 1605.30] And it's better that we didn't advertise it to begin with.
[1605.30 → 1612.68] Otherwise, we would have had, you know, 5,000, 10,000 websites going down just for a simple error that we would have encountered in the first week or two.
[1613.26 → 1613.36] Yeah.
[1613.44 → 1621.38] So we've come a long way since January, 3,000 hits a day to today about 90,000 or 91,000 hits a day.
[1621.50 → 1623.22] So it's a pretty exciting growth.
[1624.04 → 1624.94] I mean, that's pretty good.
[1624.98 → 1626.28] I mean, this is obviously good growth.
[1626.28 → 1632.24] I mean, you're looking at over a million hits this month here alone, which is quite nice.
[1632.84 → 1639.54] The whole point of a shared CDN like this is the more people use it, the better it is for everyone.
[1639.54 → 1646.38] Because the chances of me hitting a site that's got a cached resource are better if you've already hidden that site, right?
[1647.00 → 1647.40] Definitely.
[1647.56 → 1653.28] So if you look at the S3 stats that we have, it actually gives you a number of three or four not-modified.
[1653.28 → 1659.24] And what that means is how many times has a file been requested but is already cached on the server.
[1660.48 → 1668.22] And I think at the moment it's about 20, 25% of requests are actually already cached on the clients.
[1668.98 → 1672.24] So the more that spreads over the internet, yeah, the better.
[1674.94 → 1682.10] So you guys have any overlap with the Google files or is it in everybody's best interest not to duplicate files they're already hosting?
[1682.10 → 1689.14] Yeah, so up until recently we hadn't, and that was one of our mission statements, but we've actually sort of changed our opinion on that.
[1689.70 → 1695.44] We do offer the scripts that Google hosts and Microsoft hosts right now.
[1695.88 → 1703.86] I guess, I don't know, we're sort of turning into a more one-stop solution than an augmentation that we were in the past.
[1703.86 → 1711.14] Because now we have sort of far more resources available in terms of bandwidth and hosting capacity.
[1713.14 → 1721.68] I was going to say, I mean, this was a non-profit started at first, but up until Cloudflare kind of picked it up and said, we'll host you for indefinitely, like as you mentioned before.
[1722.36 → 1723.76] I mean, that must have cost money.
[1723.94 → 1727.48] Was that something you guys were doing for the community?
[1727.54 → 1730.70] Were you paying for that at first and just hoping that sponsors would eventually pick it up?
[1730.70 → 1733.04] Yeah, actually we were.
[1733.20 → 1736.34] So up until now we have been personally funding this project.
[1737.14 → 1744.58] We went out of our way to actually approach lots of different CDNs such as Amazon themselves to seek funding.
[1745.24 → 1756.12] And if that was going to fail, we were going to get community funding, like possibly SAAS kind of plans for anyone who wants to use the CDN just to keep it alive.
[1756.12 → 1759.24] But besides that, yeah, we were going to fund it ourselves.
[1760.34 → 1766.24] Yeah, so luckily we had a few companies that were receptive to sort of sponsoring us.
[1766.92 → 1770.88] And I mean, we had other options available, as Thomas said, community sponsorship.
[1771.14 → 1773.54] So it was never a particularly dire situation.
[1773.94 → 1778.70] It's just that long term, we probably didn't have the capacity to personally fund it forever.
[1778.70 → 1780.46] But it's actually convenient.
[1780.64 → 1785.82] Cloudflare is probably the most synonymous mission statement with CDN.js.
[1786.42 → 1790.66] They want to accelerate the web, and it's exactly what we want to do.
[1790.80 → 1793.82] And they're rapidly moving ahead, and we'd also like to rapidly move ahead.
[1794.50 → 1796.58] So we're synergizing at the moment.
[1796.66 → 1797.06] It's great.
[1797.06 → 1804.02] So Thomas, you'd mentioned you're on the front end with Backbone, and Ryan, you're on the back end with Node.js.
[1804.44 → 1807.44] But I guess you guys can choose who will go first.
[1807.50 → 1817.92] But I'm just kind of curious, on the open source front, besides those two, what projects are out there that you're really either wanting to play with or have dabbled with a little bit?
[1818.00 → 1820.54] What's on your open source radar in terms of what you want to play with?
[1820.66 → 1821.70] Ryan, I guess you can go first.
[1821.70 → 1828.60] At the moment, I'm really just interested in playing around with everything to do with Node.js.
[1829.48 → 1837.58] Up until recently, JavaScript hadn't piked my interest that much, but now I'm absolutely loving it.
[1839.14 → 1843.70] I really love the asynchronous aspect of Node.js.
[1843.70 → 1859.88] So that's something I'm really interested in investigating and just sort of getting to know and wrapping my head around sort of programming sort of in an asynchronous fashion rather than a typically procedural fashion as you would in PHP or something like that.
[1860.32 → 1864.86] Anything in the Node world in general besides just Node as the platform?
[1864.98 → 1865.84] What else has got your interest?
[1866.70 → 1871.02] Well, to be honest, Couch DB, that's something I'm really interested in.
[1871.02 → 1879.32] I really like working with information systems and Couch DB is something that I consider to be really cutting edge.
[1879.54 → 1883.76] And the fact that we're using it is sort of another reason it's got me interested.
[1884.70 → 1892.00] But, yeah, I mean, sort of working with that, with a web application such as ours, it gives you quite a lot of flexibility.
[1892.00 → 1895.12] And just to clarify, we're talking about Pryptozle here.
[1895.78 → 1901.34] CDN.js is actually a static website in case there was any confusion there.
[1902.48 → 1909.44] So, yeah, from my perspective, Node.js and specifically its interaction with Couch DB is what I'm interested in at this point in time.
[1910.02 → 1910.70] Thomas, how about you?
[1911.72 → 1913.86] No, I like to stay away from databases these days.
[1913.86 → 1922.50] If I'm going to talk about databases, key value stores such as Regis and Catch DB, well, not Catch DB, but any other key value stores I like to mess with.
[1923.00 → 1924.88] But I definitely love client-side at the moment.
[1925.92 → 1931.20] I'm trying to improve my usability skills, but I'm getting there slowly.
[1931.20 → 1937.84] But probably my favourite technology at the moment, and I'll give a shout-out to it, I guess, is Brunch.
[1938.28 → 1941.04] You can find Brunch with Coffee in Google.
[1941.84 → 1955.68] And what Brunch is, I don't want to define it too much because I don't own it, but it collaborates all the latest technologies such as CoffeeScript, Backbone.js, Eco, Stylus, jQuery, and Stitch.
[1955.68 → 1965.16] And it takes care of the entire JavaScript, CSS, HTML rendering, and using the best technologies that we have available.
[1965.88 → 1968.96] Well, I see one fun thing in here we've covered on the change log, which is Stylus.
[1969.04 → 1970.76] And you mentioned getting into usability more.
[1970.86 → 1977.44] So that must mean that you're wanting to do something with preprocessing style sheets and some other fun stuff.
[1977.56 → 1980.24] And jQuery and Kept are both thrown in there along with Underscore.
[1980.96 → 1981.62] Yeah, definitely.
[1981.62 → 1985.68] We were going to use CSS precompiles with our latest startup.
[1986.34 → 2001.66] At the time, though, I was going to say Ryan wasn't efficient at CSS, so I wanted to just use CSS for both of us to get on a clear pathway of understanding the CSS of the application.
[2001.66 → 2016.76] And I guess that's one of my main concerns with things such as CoffeeScript and precompiles, because I don't like the idea of if I wanted to introduce a new developer to the project, they'd have to understand the technologies that even compile the CSS.
[2017.52 → 2020.82] I wouldn't say it's completely fair to say that they don't understand the CSS.
[2021.20 → 2025.42] It's just that they maybe don't understand Stylus or Eco, for example.
[2025.42 → 2030.82] I can hear you on that, because I've worked with people that don't know Sass.
[2030.94 → 2038.32] And I hate to keep mentioning it, because I think we and I have a small stack of drinks on our side to take because of our continuous rants on it.
[2038.42 → 2041.08] But I've had to work with training people to come into that, too.
[2041.10 → 2043.18] And it's the same kind of chicken and egg.
[2043.18 → 2051.24] You want to get them into this different world of doing it better, but they have to kind of learn the syntax or different changes to it.
[2051.64 → 2056.88] In the end, they're going to spit out JavaScript or CSS in Sass or Stylus' case.
[2057.08 → 2061.66] But you want them to use this new cutting-edge technology, but it's kind of difficult.
[2062.38 → 2067.62] So all I really press for at the moment, I'm not sold on CoffeeScript, or I'm not sold on the CSS compilers.
[2067.62 → 2070.70] But I definitely like JavaScript frameworks.
[2071.42 → 2078.52] So there's Backbone or Spine.js, or you can use the big Cappuccino and Sprout core.
[2079.00 → 2083.88] I do like the idea of JavaScript frameworks, because I love single web page application development.
[2084.86 → 2088.22] But besides that, I only support JavaScript frameworks.
[2090.26 → 2092.22] So final set of questions here.
[2093.06 → 2094.24] I'll put you guys on the spot.
[2094.24 → 2097.42] And so I'm assuming both of you guys were born in the 90s, right?
[2098.52 → 2099.08] Actually, no.
[2099.28 → 2101.24] We're children of the 80s, 1989.
[2101.94 → 2102.70] There you go.
[2103.26 → 2103.64] Yes.
[2104.36 → 2107.30] Still youngsters by today's standards.
[2107.72 → 2111.80] So you're closer to college than we are.
[2112.04 → 2112.62] That's for sure.
[2113.40 → 2115.04] Yeah, fresh out of college, in fact.
[2115.42 → 2116.00] There you go.
[2116.10 → 2124.48] So what are the college kids these days learning about computing in regard to the personalities involved in this space?
[2124.48 → 2126.20] Who are your programming heroes?
[2127.62 → 2128.18] Cool.
[2128.74 → 2129.58] Programming heroes.
[2133.08 → 2135.58] To be honest, I'm not quite sure.
[2136.00 → 2137.16] Well, you don't have sports heroes.
[2137.30 → 2138.46] We've already established that fact.
[2139.46 → 2140.22] Wait a minute.
[2140.22 → 2145.84] So I couldn't really even tell you what kids in university like to learn these days.
[2146.00 → 2152.24] I think over here it's a lot of C and C++, Python and C Sharp, I guess.
[2152.24 → 2158.96] And a lot of people are into Apple and any kind of mobile development.
[2159.96 → 2164.62] But my heroes on the internet, there's definitely quite a few.
[2164.62 → 2169.96] I like all the main celebrities like Paul Irish and Jeremy and Damien Katz.
[2169.96 → 2176.36] But the other people who I look up to, like the Brunch developers, I like what they are doing.
[2176.36 → 2178.36] Yeah.
[2180.00 → 2186.34] And I guess I'm going to say my favourite guy on the web right now is one of the original authors of Couch to Beat, Damien Katz.
[2186.82 → 2189.12] The reason for that he's a really smart guy.
[2189.72 → 2192.60] And he looks like he weight lifts every now and again.
[2193.06 → 2194.54] I'm kind of a little bit interested in that.
[2194.54 → 2198.06] That's why I like the merging of health and programming.
[2198.42 → 2198.50] Yeah.
[2198.70 → 2200.70] We both go to gym five days a week.
[2201.02 → 2204.14] So we're like anyone else who has to gym and programs.
[2205.02 → 2207.10] Well, I think that's about all we want to talk to you about.
[2207.18 → 2208.60] I know we're pretty excited to have you on the show.
[2208.74 → 2213.82] We certainly enjoyed the fact that you guys are so young and so adamant about doing something fun for our community.
[2213.94 → 2220.28] And the fact that also that not only is it cool for our community, but it's a nonprofit.
[2220.86 → 2222.98] You've got some good support from things.
[2222.98 → 2227.32] And if that support didn't come around, you were still willing to shell some of your bucks out.
[2227.54 → 2238.84] So if I'll say to the audience that if you meet them up at a conference or a meetup or something like that, buy them a beer or coffee or whatever, maybe a supplement drink or something.
[2240.24 → 2241.82] I was going to say there are too many carbohydrates.
[2244.80 → 2245.88] There you go.
[2246.04 → 2246.52] There you go.
[2246.58 → 2247.40] But thanks for coming on the show.
[2247.44 → 2248.92] It's been a pleasure to talk to you guys.
[2252.98 → 2253.98] Thank you.
[2253.98 → 2254.98] Thank you.
