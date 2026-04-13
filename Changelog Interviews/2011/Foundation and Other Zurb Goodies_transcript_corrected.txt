[0.00 → 18.04] Welcome to the Changelog episode 0.7.0.
[18.28 → 19.26] I'm Adam Stachowiak.
[19.52 → 20.30] And I am Wynne Netherlands.
[20.44 → 21.32] This is the Changelog.
[21.38 → 22.88] We cover what's fresh and new and open source.
[23.34 → 26.04] If you found us on iTunes, we're also on the web at thechangelog.com.
[26.14 → 27.16] We're also up on GitHub.
[27.16 → 33.50] At GitHub.com slash explore, you'll find some trending reposts, some feature reposts from our blog, as well as the audio podcasts.
[33.82 → 36.84] If you're on Twitter, follow Changelog Show and me, Adam Stack.
[37.10 → 39.36] And I'm Penguin, P-E-N-G-W-Y-N-N.
[39.64 → 40.56] Fun episode this week.
[40.66 → 46.14] I caught up with the guys over at Curb and talked about Foundation and all the projects in the Curb playground.
[46.90 → 48.62] We've got a lot of fun stuff they work on, really.
[48.84 → 52.72] I mean, everything from Joyride to Flickr Bomb, some fun names, too.
[53.00 → 54.52] A lot of personality in these projects.
[54.60 → 56.20] I love what they do with the project pages.
[56.20 → 64.90] We talked about some of the backstories for Foundation and Joyride and Orbit reveal the whole arsenal.
[65.66 → 67.16] I'm bummed I didn't go on this call.
[67.26 → 71.78] Actually, I was working with Chris to kind of rev Foundation into the SaaS world, too.
[71.80 → 72.56] I was giving him some advice.
[72.72 → 78.72] But I'm glad you guys caught up with them, or at least that you caught up with them and had a good conversation with them.
[79.20 → 81.18] Pretty good technical discussion on this one.
[81.18 → 86.04] But look for another episode on Founders Talk to get the business side of Curb.
[86.36 → 87.06] Yeah, absolutely.
[87.18 → 88.00] I'm talking to Brian.
[88.48 → 90.08] I had him scheduled a week or so ago.
[90.14 → 92.22] I had to reschedule it, but he'll be on the show soon.
[92.28 → 98.70] So if you're a fan of Founders Talk, definitely catch Brian there soon and learn about the backstory and, I guess, how Curb got started.
[98.76 → 99.12] We'll see.
[99.78 → 100.62] Keep an eye out for that.
[100.78 → 101.22] Fun episode.
[101.32 → 101.86] Should we get to it?
[101.86 → 102.86] Let's do it.
[111.68 → 114.00] We're chatting today with the team over at Curb.
[114.32 → 118.34] So Jonathan, Matt, why don't you guys introduce yourselves a little bit about your role at Curb.
[119.36 → 119.66] Cool.
[119.84 → 121.32] So my name is Jonathan Smiley.
[121.50 → 122.72] I'm a design lead at Curb.
[122.80 → 124.12] I've been with Curb for a few years now.
[125.00 → 128.36] I work on a lot of our client projects as a design lead.
[128.36 → 133.72] I'm also involved a lot in our product efforts as well as in some of our open source efforts like Foundation.
[134.18 → 134.30] Cool.
[134.52 → 135.16] And I'm Matt Kelly.
[135.34 → 136.76] I'm the engineering lead here at Curb.
[136.96 → 142.58] I've been here for about almost three years now, and I work mostly on the product stuff here at Curb, so I'm Notable and Verify.
[142.90 → 148.06] I do stuff on the back end Ruby on Rails, and then on the front end, jQuery, Backbone, all that good JavaScript stuff.
[149.04 → 152.14] Why don't one of you introduce Curb and a little bit about what Curb does?
[152.84 → 153.10] Okay.
[153.66 → 154.06] Sure.
[154.06 → 158.78] So Curb is an interaction design agency in Campbell, California, in Silicon Valley.
[159.06 → 165.70] We work with a lot of startups as well as with a lot of larger kinds of Silicon Valley companies like Facebook, eBay, Yahoo, Netflix.
[166.96 → 171.12] A while back we did the website for BritneySpears.com, so we hang our hat on that for a little bit.
[171.24 → 180.78] But we do interaction design and design strategy, so we work on front-to-end basic – sorry, front – what am I trying to say here?
[180.78 → 183.42] This is one of those brain fart things that can be edited out later.
[183.42 → 184.82] All the ends in front of the back.
[184.82 → 186.22] Or we'll just leave it in for comic relief.
[186.32 → 188.44] Yeah, we'll just leave it in for – yeah, to make fun of us.
[189.88 → 200.24] But we do basically begin to end for a lot of our startup clients from business strategy stuff all the way through to tactical pieces like wire framing into front-end code,
[201.46 → 203.72] basically solving design problems for our clients.
[203.72 → 207.54] So it's a little unusual to have so much open source for a design agency.
[208.18 → 210.42] Talk a little bit about how that plays into your strategy.
[211.68 → 223.32] So we kind of got into it because for a lot of our clients, it's helpful for us to – it's helpful for us to know as much as we can about what the capabilities are on the front-end and on the back-end, for that matter,
[223.32 → 231.34] so that we can design things that aren't just, I don't know, design eye candy kind of stuff, things that can actually be implemented and built.
[232.12 → 238.54] So in the course of knowing as much as we can about that, as well as in the course of designing and building our own products, of which we have a number,
[238.54 → 246.18] we did a lot of work on really researching JavaScript and getting much more into that, doing a lot more work on the back-end,
[246.30 → 252.32] really kind of pushing the envelope on front-end pieces like CSS3 or stuff that we can do with HTML5.
[253.08 → 257.04] And in order to learn how to do some of that, we put together the playground, the Zero playground,
[257.70 → 261.52] which is where we could do all these experiments and kind of like just screw around with things.
[261.52 → 269.92] Like we wanted to figure out what's a better way to do image uploads or what's a better way to do specific kind of JavaScript stuff.
[270.78 → 274.16] I know Matt could probably talk more authoritatively about a lot of those pieces.
[274.78 → 277.16] And we figured why keep all that to ourselves.
[277.44 → 280.14] Our mission is kind of to bring design to everybody.
[280.90 → 285.06] So if we're going to be bringing the work that we're doing to everybody, we may as well expose it as much as we can.
[285.62 → 287.40] We're going to jump into the playground in just a minute.
[287.40 → 290.92] A lot of goodies in the playground, but I wanted to start with foundation.
[291.52 → 293.28] Talk a bit about foundation and what it does.
[294.40 → 300.38] So foundation was actually born out of what we used to call the Zero style guide, the Zero CSS style guide,
[300.88 → 309.90] which was a set of resets and common styles and sort of layout affordances that helped us get running much more quickly
[309.90 → 311.68] when we were doing front-end code for our clients.
[312.20 → 319.10] And we realized as we were going through that not only was it pretty poorly documented and not really –
[319.10 → 320.98] it was a little difficult to get going with.
[321.52 → 325.06] It was also – it didn't have all the best practices we could have in it,
[325.12 → 327.68] and it wasn't as good of a starting point as it could be.
[328.00 → 332.06] So we started to build it out into something much more full-featured with a lot more documentation,
[332.50 → 336.36] and that's what eventually became the first version of foundation,
[336.50 → 340.84] which actually nobody outside Zero ever really saw, which was for fixed-width websites.
[341.00 → 342.26] It was for desktop only.
[342.62 → 346.10] It had a lot of best practices, and it had a lot of good code in it,
[346.10 → 351.22] but it wasn't everything that it needed to be for it to really be useful going forward.
[351.86 → 360.02] So about six months ago, nine months ago, we started adapting it into a really, really responsive framework,
[360.18 → 365.88] something that we could really rapidly prototype with and actually build sites that worked for desktops,
[366.02 → 368.64] tablets, phones, any kind of device really.
[368.64 → 374.32] Since mobile devices are definitely the future, mobile devices are already huge.
[375.04 → 379.80] Within the next couple of years, they'll account for more internet traffic than desktops in the U.S.
[380.86 → 384.22] Since that's what's kind of coming down the pipe, we wanted to make sure we were ready for that.
[384.56 → 388.74] And since we were building out this huge framework, and we were building out all the pieces that we needed for this
[388.74 → 392.48] and we were documenting everything, it made pretty good sense to open it up to everybody.
[392.48 → 395.14] And that's kind of the genesis of Foundation.
[395.98 → 400.44] Talk a bit about, maybe draw some distinctions between it and, say, Twitter Bootstrap.
[401.00 → 408.60] So Twitter Bootstrap, we actually know the guys who work on Bootstrap.
[408.98 → 409.82] They're good guys.
[410.28 → 412.24] There's a lot of good code, actually, in Bootstrap.
[412.36 → 414.48] They have a lot of really nice styles, especially for forms.
[415.12 → 417.24] They really went above and beyond for doing stuff like forms.
[417.24 → 423.72] Probably the biggest distinction between Foundation and Bootstrap is that Bootstrap today, certainly,
[423.98 → 429.40] and for the indeterminate future, is still designed exclusively for desktops.
[429.62 → 431.00] It's purely fixed width.
[432.26 → 435.36] It doesn't really have any affordances to do any kind of responsive design.
[436.34 → 437.38] They are working on that.
[437.46 → 439.68] There's no real timeline on when that's going to actually happen.
[440.78 → 444.32] And from the work-in-progress stuff, it looks like their approach is going to differ a bit from ours.
[444.32 → 449.84] But at the moment, that's probably the biggest delineation between Foundation and Bootstrap.
[449.96 → 455.28] Foundation was also designed to be a little bit more agnostic in terms of style and in terms of what you're going to do with it.
[455.50 → 460.88] Bootstrap is really phenomenal if what you want to do is build a desktop site that looks a lot like Twitter.
[461.18 → 463.18] It's more of a style guide than Foundation is.
[463.42 → 471.80] Foundation is built to be extensible and modified and be more of a baseline than a final solution, I guess, for what you want to build.
[471.80 → 476.50] Would it be closer than to, say, HTML5 boilerplate?
[477.04 → 480.14] It actually incorporates a number of aspects of HTML5 boilerplate.
[480.26 → 484.32] We actually included a number of pieces from that, and you can find those in the code.
[484.40 → 485.66] Those are actually credited in the code.
[486.68 → 494.28] Boilerplate is kind of the other end of the spectrum, which is that it's absolutely just a baseline in order to build all of your stuff on top of.
[494.28 → 505.92] Foundation includes the grid is probably the biggest piece that it includes that boilerplate omits, which is a construct for really quickly doing layouts, nestable, flexible layouts.
[506.60 → 512.24] It also includes – Foundation also includes a lot of just common elements like tabs and pagination, things that boilerplate omits,
[512.24 → 519.38] because their intention isn't really to build a framework that you can use to completely prototype a site and completely move that into production code.
[519.48 → 525.50] It's really just a great way to start coding that has a lot of sorts of best practices about really low-level stuff.
[525.88 → 532.24] You provide a Rails gem out of the box, and I see that it's been ported to WordPress and .NET, ASP.NET MVC.
[532.32 → 534.16] Any other server-side frameworks in the works?
[534.64 → 535.38] Not by us.
[535.48 → 537.06] We know a lot of people are working on other things.
[537.06 → 541.74] We're a Rails shop here, so we did the Rails' asset gem, and we're going to continue to maintain that.
[542.14 → 548.58] But in terms of the WordPress gem and the .NET MVC gem, those are all done by people who are outside Curb who are contributing to this kind of stuff.
[548.72 → 552.96] So we've heard from a lot of people they're doing stuff in pretty much every framework.
[553.26 → 557.14] Someone's got something that they're working on, but if anybody out there wants to do one for their favourite framework,
[557.32 → 560.50] we're more than willing to answer any questions and give you any kind of support.
[560.56 → 561.36] I hope that you need to do that.
[561.82 → 564.96] But here, our wheelhouse is more Ruby on Rails.
[564.96 → 565.78] It's Josh from J.P.G.
[565.78 → 571.86] So we're going to stick with maintaining the Rails' asset gem, but then help anybody else in the community who wants to do gems for their own favourite framework.
[572.40 → 579.06] We've been trying to get through these episodes without mentioning Compass or SAS because we get so much flack on the Twitter when we do that.
[579.16 → 582.98] But I couldn't help but ask, you know, why just static CSS only?
[583.08 → 585.28] Why not a pre-processed flavour of it?
[585.28 → 588.56] I mean, we want to make Foundation accessible to everyone.
[588.84 → 597.44] So we kind of wanted to code at least the baseline that's on GitHub that we're going to maintain needs to be at the, you know, the base language that or the base markup language that everyone understands.
[597.66 → 597.84] Right.
[598.06 → 603.74] So we want to steer clear of Tamil and SAS and Compass, at least for the version that we're going to put out there.
[603.74 → 611.54] Again, we're totally encouraging people if they love SAS, if they love Tamil, then totally, you know, do your own port of that and keep it up to date.
[611.66 → 612.18] And that's awesome.
[612.56 → 619.94] But for us, we want to make sure that everyone can use Foundation, and we don't want to get into some kind of like holy war about, you know, SAS is the best or, you know, Tamil rocks.
[620.02 → 620.46] Forget HTML.
[620.80 → 624.52] We're just going to go with the one thing that everybody knows so that it's accessible to everyone.
[624.96 → 626.88] We don't want that to be a barrier that you have to learn Tamil.
[626.88 → 630.66] We're not super opinionated about like, yes, everything has to be in Tamil.
[630.72 → 631.64] Everything has to be in SAS.
[632.62 → 634.16] That's kind of the way we feel about it.
[634.88 → 636.36] Do you use those tools on your projects?
[637.64 → 638.28] Some of us do.
[638.72 → 641.32] We have kind of a, well, we have kind of a varied shop.
[641.42 → 642.46] I mean, we have various designers.
[642.66 → 644.68] I know Chris is one of our designers.
[644.82 → 647.12] He likes to use SAS, which actually I think he's even working.
[647.12 → 650.68] I think he's working kind of on the side on like a SAS gem for Foundation.
[651.60 → 654.86] So he's a SAS proponent, but I think he's the only one in the office.
[654.86 → 659.00] We've played around with less before trying to use that.
[659.20 → 661.76] We kind of, I don't know, we poke our noses into all these different things.
[661.88 → 665.62] But at the end of the day, I always come back to just using vanilla CSS.
[665.86 → 668.96] I feel like I have more control, but that's just a curmudgeon that way.
[669.22 → 670.74] It's an accessibility problem, right?
[670.78 → 674.26] If you use a language that not everybody knows, then you're just saying,
[674.26 → 675.58] well, I don't really want you to work on this project.
[675.64 → 676.50] It puts a barrier up.
[676.84 → 680.24] If someone new joins a team, if you want to get somebody outside the organization to contribute to it,
[680.26 → 683.74] if they don't know Tamil if they don't know SAS, then it's a barrier for them to get in there,
[683.74 → 686.06] and they can't quite as quickly get in there and have it co.
[686.12 → 688.76] So we're all about making this stuff accessible for everyone
[688.76 → 691.04] and having everyone on the team be able to contribute to every project.
[691.82 → 694.88] So again, for some of the smaller pet stuff, if somebody here wants to use Tamil,
[694.94 → 695.58] more power to them.
[695.70 → 698.02] But as a company, we haven't said, like, this is the way.
[698.18 → 700.98] We haven't standardized on we're all going to use Tamil, we're all going to use SAS.
[701.04 → 702.02] We just think of the vanilla stuff.
[702.02 → 706.42] So I guess as a design agency, do you find yourself having to hand off assets
[706.42 → 708.96] to external teams quite a bit in project lifecycle?
[709.50 → 710.30] Oh, yeah, absolutely.
[710.92 → 715.48] For almost all of our client projects, at the end of most of our projects,
[715.54 → 719.78] what we end up handing over is front-end either style guide or templates,
[719.88 → 724.16] coded style guides or coded templates that they need to be able to implement.
[724.30 → 727.56] That's actually another reason that we don't delve too much into less or SAS.
[727.56 → 733.20] We don't have a lot of clients who are comfortable with any kind of additional frameworks like that.
[733.42 → 735.28] So it's difficult for them to integrate into their workflows.
[735.44 → 739.02] It's easier if we can give them, you know, CSS that we understand, that we wrote,
[739.12 → 743.98] that's all organized correctly and organized logically for us and for them.
[744.72 → 747.90] So almost 1,600 watchers on GitHub.
[748.06 → 748.70] How long has it been out?
[749.52 → 750.04] About a month.
[751.20 → 751.88] That's impressive.
[752.02 → 752.94] I think about four weeks now.
[753.02 → 755.56] Yeah, it really, really took off there.
[755.56 → 758.06] So we're pretty stoked about that.
[759.06 → 762.76] So I wanted to jump into some of the projects in the Playground.
[762.88 → 765.68] So over in Foundation, a lot of the layouts that you've got,
[765.76 → 771.46] it looks like you're using the Placeholder web service that will return assets on the fly,
[771.54 → 772.26] the images on the fly.
[772.32 → 775.58] But I noticed you have another project in the Playground called Flickr Bomb,
[775.80 → 779.30] which does almost the same thing except with Flickr images.
[779.40 → 779.94] Talk about that.
[780.60 → 781.84] Yeah, same thing but different.
[781.84 → 785.82] It's the same problem that Placeholder solves, but when we're doing,
[786.02 → 787.46] mostly this came from our client work.
[787.56 → 791.28] When we're doing client work, we kind of have to go out and grab some images from stock.
[792.22 → 793.28] What's that website called?
[793.88 → 794.40] The stock photo?
[794.56 → 794.96] iStock.
[795.08 → 795.40] Yeah, whatever.
[795.60 → 799.80] You go to iStock and get the watermark image thrown in there.
[800.00 → 804.42] But the Place hold images are great, but if we're trying to convey like a mood or a feeling for the page
[804.42 → 807.46] without having the actual final images, you still have to go out there and find them and hunt them down.
[807.46 → 811.94] So we thought, you know, how cool would it be, because what we usually do is we just go to Flickr,
[812.36 → 814.58] search for something by a keyword, and then pull in an image.
[814.62 → 818.68] How cool would it be to just be able to do that similarly that Placeholder works?
[819.08 → 825.92] So instead of specifying a regular SRC attribute on your image tag, you specify one.
[825.98 → 829.52] But instead of it being like an HTTP URL, you specify it like Flickr colon slash,
[829.60 → 830.60] and you put in the Flickr keywords.
[831.08 → 833.64] And you just drop the Flickr bomb script somewhere on your page.
[833.64 → 836.78] And then all those Placeholder images where you specified the width and the height,
[837.00 → 839.10] they get this little control button on them.
[839.42 → 840.38] So you go to your image.
[840.48 → 843.90] It pulls in the first image from Flickr that has that keyword in it.
[844.26 → 845.36] And so you can just see that.
[845.44 → 847.60] So, for example, I'm prototyping a Britney Spears site,
[847.78 → 850.72] and I got a bunch of Britney Spears Placeholder images on there.
[850.98 → 854.58] When I load it up with Flickr bomb, they'll just pull the first Britney Spears image for each one of those.
[854.86 → 858.84] And if I don't like that image, I can click on the little tool icon on that image and pull in a different one.
[858.84 → 863.16] And it uses local storage to persist whatever image that I chose down to my local machine.
[863.16 → 867.18] So it's a really quick way to do some fast prototyping but have actual images in there
[867.18 → 869.58] rather than just this kind of gray Placeholder images.
[870.72 → 873.84] This has got to be the first time we've ever mentioned Britney Spears twice in an episode.
[874.18 → 874.38] Yeah.
[874.78 → 877.14] Is that what's usually on loop in the office?
[877.60 → 879.88] Not as much as it used to be.
[879.96 → 881.34] It pops up every once in a while.
[881.44 → 883.68] We're more likely to be listening to Kesha than Britney Spears.
[883.72 → 884.54] Yeah, that's a true story.
[885.80 → 888.38] Britney Spears was really hot back when we were working on the client, right?
[889.14 → 890.56] You really have to do your research.
[890.94 → 891.34] Exactly.
[891.34 → 894.10] We still got a picture of her up in the office.
[894.54 → 895.12] We do.
[896.12 → 897.72] Kesha has not been a client of ours yet, though.
[898.52 → 899.34] We're holding out hope.
[899.34 → 901.16] If she's listening, we'd love to do her website.
[902.62 → 905.02] If you're listening, probably not to this podcast.
[906.76 → 908.00] Talk to me about Joyride.
[909.68 → 911.54] Joyride was kind of fun.
[911.62 → 915.10] Joyride popped up because since we do product development here,
[915.10 → 919.08] since we have a number of products that we've released and that we continue to work on,
[919.42 → 922.26] Notable and Verify are the ones that are out right now.
[923.30 → 928.38] We ran into an issue where basically we make changes to the application based on customer feedback,
[928.72 → 931.34] based on internal review and things of that nature,
[931.68 → 936.32] but we didn't have a great way to actually communicate to our users what was happening.
[936.32 → 941.24] We were never doing a spectacular job of actually showing what was changing,
[941.66 → 945.02] of showing where they should be going or how they should be interacting with these new pieces.
[945.80 → 950.74] So it occurred to us that the simplest way to deal with this would be to have a plugin that we could use
[950.74 → 955.80] and that other people could use to very quickly just attach a little tour,
[955.80 → 959.86] or a little joyride on the page, to take you from step to step.
[959.94 → 961.66] And we wanted to make it really easy to use.
[961.74 → 964.80] So you can basically drop in the plugin, and you just attach these steps.
[965.12 → 968.14] You create them as sort of ordered list at the bottom of the page,
[968.14 → 971.36] and you attach them to just elements that have individual IDs.
[972.08 → 975.02] So you just can get, you know, a lot of your elements on, especially in an application,
[975.18 → 977.26] a lot of your elements on the page already have IDs,
[977.44 → 978.84] so you don't really have to do anything for that.
[979.24 → 980.96] Or adding IDs is very simple.
[980.96 → 987.48] So it's really easy to just create a very quick, very easy-to-use tour that will take you down the page
[987.48 → 989.42] and will actually show you all the new stuff.
[990.28 → 993.66] We used it in Notable fairly recently for one of our releases,
[993.76 → 995.06] and we got a lot of good feedback from that.
[995.12 → 998.12] A lot of people were really pleased to see that when things changed,
[998.18 → 1001.94] we were actually telling them what changed and how they changed and how they work now.
[1002.74 → 1004.12] It helped a lot with engagement.
[1005.30 → 1008.74] And also it was just, you know, as with a lot of our Playground pages,
[1008.74 → 1011.58] it was a lot of fun to actually put together the Playground piece itself.
[1012.42 → 1015.46] You can check out the Joyride page on the Playground
[1015.46 → 1019.72] and, you know, see us playing around with imagery and, you know, big flashing headlights.
[1019.98 → 1022.20] And if you punch in the Donati code, you can have some fun with that too.
[1023.26 → 1024.32] I'll have to try that.
[1024.42 → 1028.52] You guys put so much design into your project pages.
[1028.76 → 1030.08] I mean, how much time does that take?
[1030.70 → 1031.64] As much as the code?
[1032.02 → 1033.50] It takes some time.
[1033.54 → 1035.26] It doesn't usually take as much time as the code
[1035.26 → 1038.00] because we've gotten pretty good at doing it fairly quickly.
[1038.00 → 1039.80] But it's also just fun.
[1039.96 → 1042.20] I mean, all the stuff on the Playground is literally that.
[1042.26 → 1043.34] It's really a Playground for us.
[1044.68 → 1048.40] Other than the listings of our actual products on the Playground,
[1048.52 → 1051.78] everything we've done on the Playground is just open code.
[1051.90 → 1054.60] It's just stuff that people can use and stuff that we thought was cool.
[1055.56 → 1060.00] It was really born out of a few years ago when we were first getting into CSS3
[1060.52 → 1064.76] and what you could do with that with transitions and transformations and some of those other pieces.
[1064.76 → 1071.88] And the first thing we put together for the Playground was actually a gallery of Polaroid-looking images.
[1072.14 → 1075.52] And we wanted to see what all we could do with CSS3 to make images look like Polaroids
[1075.52 → 1077.42] without doing a lot of extra work.
[1077.98 → 1082.68] And we were putting it together, and we realized it doesn't really sell it as being as cool as it is
[1082.68 → 1083.94] unless it looks really nice.
[1083.94 → 1089.58] So we took the time to give it a nice background and play around with text shadows
[1089.58 → 1091.80] and make inset text and do all this fun stuff.
[1092.38 → 1099.84] And that was kind of the genesis of really, at times almost over-the-top Playground pages.
[1100.88 → 1103.64] Because it's fun for us to mess around with the code,
[1103.72 → 1106.38] but it's also fun for us to mess around with the display of all this stuff.
[1106.38 → 1109.62] I think it's almost become like a one-upmanship type thing too, right?
[1110.56 → 1113.34] The Playground stuff, it's not like somebody tells you, like, you need to do this plugin,
[1113.46 → 1114.10] like John was saying.
[1114.16 → 1115.90] It's always something that you want to do that's really cool.
[1116.38 → 1120.04] So different people do different pages and, you know, it's kind of their baby as they're growing.
[1120.16 → 1123.12] And it's kind of, you know, some of the competition where like, well, all right,
[1123.24 → 1126.54] we did the really crazy radioactive flashing buttons with the awesome background.
[1126.54 → 1128.68] And now for the next one, it has to be even bigger and more exciting.
[1128.68 → 1132.20] So they kind of continue to get more elaborate and more ridiculous.
[1133.08 → 1139.74] Speaking of, so Curb buttons I think is the gateway that most folks have into landing on a Curb page.
[1139.84 → 1141.86] So talk a bit about Curb buttons and what they are.
[1142.16 → 1142.92] We love buttons.
[1144.44 → 1150.18] I couldn't even, I'm not even sure we could tell you exactly what the impetus behind all of that was.
[1150.28 → 1154.98] But when we were first getting going, I think what really kicked it off was
[1154.98 → 1160.04] there's a page on the playground which is just super awesome buttons with CSS3.
[1161.00 → 1165.94] And we put that together because we realized one day that with some of this new CSS3 stuff,
[1166.00 → 1171.02] we didn't have to mess around with sliding doors like you used to have to with these, like, crappy sprites
[1171.02 → 1174.98] where you had all these problems, and it was just a huge pain in the ass for different browsers.
[1174.98 → 1179.92] We realized you can actually make really nice-looking buttons with really intelligent stuff
[1179.92 → 1183.42] with very simple markup and fairly simple CSS.
[1183.42 → 1185.88] So we're really excited about that.
[1185.94 → 1189.38] So we put together this page for super awesome buttons, and we put together a blog post
[1189.38 → 1194.12] and it just took off like almost nothing else that we've seen.
[1194.68 → 1196.88] Just tremendous numbers of views.
[1197.06 → 1198.88] It's been used all over the place.
[1199.48 → 1205.04] For a while we had some fun looking at all the sites that had hot linked our overlay images,
[1205.42 → 1206.40] which was pretty entertaining.
[1206.60 → 1207.04] Oh, man.
[1207.58 → 1208.06] Yeah, there's...
[1208.06 → 1209.88] Very popular among adult sites.
[1210.00 → 1210.16] Yeah.
[1210.16 → 1214.10] There are some interesting URLs in there.
[1215.12 → 1221.06] So that kind of started like a little love affair with us for buttons, and we still have a tremendous amount of fun
[1221.06 → 1227.70] just making really refined buttons that require almost as little markup and as little CSS as humanly possible.
[1228.42 → 1229.66] And some of this stuff is just silly.
[1229.78 → 1233.38] I mean, you can check out like the radioactive buttons, which are great to play around with
[1233.38 → 1238.66] until you realize that if you keep that page up, eventually your fan will kick on and your processor will spike to 100%
[1238.66 → 1239.96] and it just kind of goes crazy.
[1240.70 → 1243.54] But it was fun to look at and fun to play around with.
[1243.94 → 1250.58] And then Google was starting in on doing buttons using just CSS for production stuff.
[1250.66 → 1253.60] So we figured, hey, let's show how you roll your own Google buttons.
[1253.60 → 1258.42] And now that's become somewhat commonplace, but at the time it was pretty cutting edge.
[1259.26 → 1262.88] So that was, I guess that was kind of what kicked off our love affair with buttons.
[1263.06 → 1264.12] We still just love buttons.
[1264.22 → 1267.36] Anytime anybody asks us about buttons, we're like, ooh, let us tell you about buttons.
[1267.76 → 1272.38] Speaking of buttons and Google, what do you think of the new UI direction over at Google?
[1272.38 → 1275.86] I provisionally like it.
[1276.62 → 1278.08] I like some aspects of it.
[1278.14 → 1283.96] In a few of their applications, it falls apart a little bit because they've almost gone a little too far in that direction.
[1284.26 → 1286.32] They've lost a little bit of structure in a few places.
[1287.06 → 1289.76] Well, the buttons in Gmail got a lot of play when they first came out, as you said,
[1289.82 → 1293.78] but now it seems like they've just gone to flat, square, DIVS everywhere.
[1294.04 → 1299.98] Yeah, it's very minimal and parts of it I really like.
[1299.98 → 1305.32] I mean, in terms of the first place I saw it, I think, was actually when Google Plus first came out,
[1305.84 → 1307.88] which it works pretty well for that.
[1308.00 → 1311.30] It's pretty simple, and it's still got a pretty good structure to it.
[1312.12 → 1314.74] In a few places, it doesn't adapt quite as well.
[1314.86 → 1318.94] It's mostly nice to see that they're working on design at all, actually,
[1319.06 → 1323.62] that they're bringing design into their products or into their process at all,
[1323.68 → 1328.48] since traditionally Google's been in, no offence to engineers who are in the room with me or listening,
[1328.48 → 1331.34] but it's traditionally been an engineer-driven society over there,
[1331.42 → 1336.64] which is basically functioned well over for more usability.
[1337.94 → 1339.50] So it's nice to see some aspects of that.
[1339.60 → 1341.32] I don't know, that's my take on it.
[1342.24 → 1343.72] Matt's just bobbing his head next to me.
[1344.68 → 1345.72] Yeah, designers.
[1349.64 → 1351.92] Another popular project of yours is Orbit.
[1351.92 → 1356.10] Yes, Orbit, our jQuery image slider.
[1358.18 → 1362.02] That was kind of just created as we wanted to do our own image slider.
[1362.24 → 1365.10] It was one of those things where we're like, there's a thousand image sliders out there,
[1365.26 → 1366.20] but we're just going to make our own.
[1366.26 → 1366.92] We have some specific needs.
[1367.48 → 1371.46] I think it was more as a development exercise and specifically saying, no, no,
[1371.62 → 1372.98] this slide is going to be a little different.
[1373.16 → 1376.12] So we were very opinionated about a couple of things we wanted to do with the slider.
[1376.12 → 1380.72] We wanted to make sure that, first, we didn't want you to have to set the width and height of it.
[1380.86 → 1385.40] So Orbit does look at the images that it has, and it sets its own width and height based on that,
[1385.50 → 1386.76] or if you do want to do it automatically.
[1387.74 → 1393.14] The way we slide images through the slider, you can position controls without them being hidden.
[1393.18 → 1394.94] So we're not doing like an overflow hidden on the container.
[1395.28 → 1397.74] So we did a lot of small things differently.
[1398.18 → 1402.64] It came out with a fairly simplistic, at least a used slider that a lot of people like.
[1402.64 → 1408.66] On the jQuery side, it's actually by far our most complicated jQuery plugin or jQuery tool that we've done.
[1409.28 → 1412.72] It dominates everything else in terms of like lines of code and complexity,
[1413.06 → 1415.62] but it does offer a lot more simplicity for the user side.
[1415.88 → 1419.06] But on the backend invitation side, it's pretty crazy going on that,
[1419.08 → 1420.06] so we have going on in there.
[1420.28 → 1425.28] It also easily dominates in terms of emails and support requests received.
[1425.66 → 1425.80] Yeah.
[1426.12 → 1430.98] By far we get the most people asking like, why doesn't it work in this crazy situation?
[1430.98 → 1434.06] Just because it is so complex, and it is so accessible,
[1434.32 → 1437.04] people are using it in all kinds of different crazy ways we could never imagine.
[1437.64 → 1441.56] We did have a lot of fun, though, adapting Orbit to work with Foundation
[1441.56 → 1444.64] because originally Orbit was not a responsive image slider,
[1445.02 → 1446.36] and now it is within Foundation.
[1446.88 → 1450.50] We're still working on porting the original one that will work both in responsive
[1450.50 → 1454.06] and non-responsive layouts, but we have like a branch of it in Foundation
[1454.06 → 1458.30] that's fully responsive and implements the responsive portion of it
[1458.30 → 1460.62] differently than the other image sliders out there.
[1460.98 → 1466.38] So it doesn't use quite as much JavaScript on the resizing and detective size.
[1466.46 → 1469.32] It's almost all CSS tricks to try to maintain the ethic ratio.
[1469.68 → 1472.20] It's also responsive with content as well.
[1472.32 → 1475.12] So you can put in a DIV and resize that.
[1475.44 → 1479.34] You just literally grab your window, resize it, and we will resize that DIV,
[1479.50 → 1482.68] keep the same aspect ratio without using JavaScript to take the window resize.
[1483.80 → 1484.40] It's pretty fun.
[1484.40 → 1488.60] It's a great, cool technical challenge to make things work inside the responsive world.
[1488.60 → 1491.84] I know across all your open source projects, it's hard to pick a favourite,
[1491.96 → 1493.98] but if I had to, I think Reveal would be mine.
[1494.90 → 1495.80] Yeah? Okay.
[1496.92 → 1501.14] It seems like it's just a UI pattern that you have in almost every project now
[1501.14 → 1504.80] and it just makes it so darn simple to add a dialog box.
[1505.00 → 1508.44] You would think we would have something like this baked into the spec by now, you know?
[1508.80 → 1510.24] Yeah, you might think so.
[1510.42 → 1511.88] Reveal was fun.
[1512.04 → 1516.06] I mean, Reveal had a similar genesis, I suppose, to Orbit, which was basically,
[1516.54 → 1520.80] there are other solutions out there for it, but we didn't have any particularly strong feelings
[1520.80 → 1523.84] about one or another, so we figured we'd just roll our own and have control over it
[1523.84 → 1525.30] and it would do the things we wanted it to do.
[1526.44 → 1527.78] We wanted something really simple.
[1527.92 → 1530.22] We were also having a lot of fun with data attributes.
[1530.22 → 1535.44] I don't know if you've gone through our jQuery stuff, but that's kind of been our preferred way of hooking stuff in.
[1535.82 → 1541.36] So rather than having to call a JavaScript function at the end of your script tag or at the bottom,
[1541.74 → 1545.40] we like to just use data attributes and have the scripts just look at the DOM and say,
[1545.46 → 1545.96] what should I do?
[1546.08 → 1547.82] So that way you don't have to actually write any JavaScript code.
[1548.08 → 1551.20] You just include our script, you add some data attributes, and everything works.
[1551.32 → 1553.72] So Reveal was, we were trying to play with data attributes.
[1553.88 → 1559.30] We're like, let's just do a really easy dialog box that just is driven totally out of data attributes
[1559.30 → 1562.54] and really simple, a couple animations, and just get it done.
[1562.84 → 1564.94] And the difference between Orbit is very complex.
[1565.06 → 1567.36] Reveal is actually pretty straightforward on the jQuery side.
[1567.50 → 1570.64] We just tried to make it a very minimalist API and really easy to hook in.
[1570.68 → 1571.76] You just drop in the code and go.
[1572.78 → 1578.10] Outside your open source, you still have a number of free apps that I guess some of these are hosted services
[1578.10 → 1580.20] and not open source projects.
[1580.60 → 1581.84] What about Axe?
[1582.56 → 1583.36] Axe was fun.
[1584.14 → 1589.06] Axe is, so Axe is a it's a tablet-only web app.
[1589.30 → 1592.60] Which was, which made it fairly interesting from the get-go.
[1592.70 → 1598.24] But it's basically a way to capture a website and then sort of axe out, basically scribble out
[1598.24 → 1601.20] or cross out the things that you don't want or the things that you want to change
[1601.20 → 1603.62] and then, you know, quickly add notes about what you would change
[1603.62 → 1605.38] and then take that and share it with somebody else.
[1606.70 → 1610.00] I know we had a lot of fun doing the design of it actually was pretty cool,
[1610.06 → 1613.46] especially the visual design, which if you look at all of our different feeder apps,
[1613.56 → 1616.30] well, we call them feeder apps, the free apps that we provide.
[1616.30 → 1623.22] But if you look at all of our different free apps, Axe is definitely the most aggressive and bloody of all of them,
[1623.28 → 1624.06] which was pretty fun.
[1626.04 → 1628.18] They're pretty valid. Axe, Chop, Strike.
[1628.94 → 1635.44] Yeah, I know. I guess we could have gone a little more violent with some of those other ones,
[1635.52 → 1637.34] but Axe is a really, really aggressive one.
[1637.58 → 1643.28] But I know with Axe, a lot of the fun with Axe came in terms of just the technical challenges of it,
[1643.28 → 1646.18] which were pretty interesting. There was a lot of weird stuff going on there.
[1646.62 → 1650.92] Yeah, we wanted to do something. We wanted to do a native app for tablet devices,
[1651.10 → 1654.48] so really kind of getting into the touch events and seeing.
[1654.58 → 1659.68] You've seen a lot of others, I'm sorry, not native, but like browser apps for mobile devices.
[1660.32 → 1664.12] Seen a lot of limitations. It seems like browser apps kind of felt sluggish in general,
[1664.12 → 1668.96] so we wanted to go in and see what the limitations were in terms of how good of an experience could we build.
[1669.08 → 1670.62] We didn't want it to look like a native app.
[1670.72 → 1674.64] We just wanted it to perform well and feel like a nice web app.
[1674.90 → 1679.34] So it was a pretty decent amount of work to get all the little moments right on Axe,
[1679.38 → 1682.24] but I think you guys were pretty happy with what we got running on that, at least on the iPad.
[1683.40 → 1684.40] We didn't spend that much.
[1684.74 → 1685.68] I mean, we spent some time.
[1685.82 → 1690.46] It works on tablet Android devices, but, I mean, the performance is not that great,
[1690.46 → 1694.06] and it doesn't feel nearly as fluid, and there are some weird edges.
[1694.16 → 1696.22] But it certainly works on Android tablet devices.
[1696.68 → 1701.30] But on the iPad, it is where it seems to run really well and performs very well for a browser app,
[1701.36 → 1703.12] so we were pretty stoked about that.
[1703.70 → 1708.16] You guys have mentioned mobile quite a few times, so what sort of applications is you creating?
[1708.88 → 1711.38] Pretty much everything we're working on right now has some sort of mobile component.
[1712.64 → 1718.16] We're definitely on a mobile warpath right now, which was a lot of the impetus behind Foundation,
[1718.16 → 1728.10] but we're working on a couple of paid applications, so paid services that we're going to be releasing in the coming months,
[1728.66 → 1734.92] both of which have fairly strong mobile components in terms of bringing mobile development into your workflow
[1734.92 → 1741.06] and doing more with mobile, because we definitely believe that doing things for mobile is really a requirement at this point
[1741.06 → 1743.80] in terms of development for the web or for applications.
[1743.80 → 1754.06] For all of our recent free applications, so Reel, Spur, and Axe, all three of those have mobile components to them.
[1754.24 → 1755.56] They're all responsive, basically.
[1755.70 → 1759.10] Each of those works on phones, tablets, desktops.
[1759.32 → 1762.72] In Axe's case, it restricts the actual functionality to tablets.
[1762.88 → 1763.26] We did that.
[1763.34 → 1767.30] That was just a decision that we made in terms of what would be the best experience,
[1767.44 → 1769.84] but Spur and Reel are both completely responsive.
[1769.84 → 1776.50] And for both of those, in fact, for all three of those, we didn't write three different code bases for different categories of device.
[1776.64 → 1782.32] Just like with Foundation, we wrote one code base, and we did the adaptation and did the changes that we needed
[1782.32 → 1785.88] to make that a good experience on the different categories of device, I suppose.
[1786.72 → 1793.68] But even for client projects and stuff now, we're bringing in a fairly strong mobile component to really everything that we're working on.
[1793.68 → 1799.78] So you mentioned responsive layout and, I guess, Axe has the touch events and touch APIs.
[1800.10 → 1803.08] What other sort of device capabilities are you taking advantage of?
[1803.72 → 1810.42] So right now, at least on the web side, we're still somewhat limited in terms of what we can take advantage of.
[1811.22 → 1815.88] You can take advantage of location now through web applications on mobile devices.
[1816.04 → 1818.66] We haven't had occasion to do that just yet.
[1818.66 → 1824.92] It just hasn't really made sense in terms of decisions that we're making for the current applications that we're working on.
[1825.46 → 1826.32] We certainly could.
[1826.42 → 1828.66] It might pop up in the future probably for a client application.
[1829.88 → 1832.20] So there's definitely some stuff that we could do there.
[1832.94 → 1837.14] In terms of other capabilities of mobile devices, things like orientation,
[1837.90 → 1842.58] most of our stuff right now is designed to be agnostic in terms of the orientation you use it in,
[1842.64 → 1844.94] whether it's landscape or portrait on tablets or phones.
[1844.94 → 1848.20] Everything, we try to make sure everything just works.
[1849.36 → 1857.22] We have gotten into a little bit of using media queries and CSS to do specific things for one orientation over the other.
[1858.94 → 1860.82] But, yeah, I don't know.
[1860.90 → 1869.30] I think that's, thus far, it's mostly been the adaptation of screen size that's really made an impact for us for touch,
[1869.54 → 1873.16] or for, like, touch-based devices for smartphones or tablets or things like that.
[1873.16 → 1879.44] Axe is probably the best example of taking advantage of actual touch events and different gestures and such.
[1879.88 → 1882.58] And using Canvas to draw the annotations on there.
[1883.46 → 1886.62] So this is the part of the show where we kind of turn it around and ask you,
[1886.74 → 1889.10] what's got you excited in the open source world?
[1889.18 → 1891.14] What's on your radar that you just can't wait to play with?
[1893.00 → 1893.84] That's a good question.
[1894.22 → 1895.08] That is a good question.
[1896.54 → 1898.50] Exciting in the open source world right now?
[1898.50 → 1898.58] Yeah.
[1899.48 → 1900.78] It's always fun to...
[1901.96 → 1902.78] I know I have a...
[1903.72 → 1906.90] I think I have a tab open right now, which I'm pretty sure it's open source,
[1907.02 → 1910.26] which is Inuit, which is a new CSS framework.
[1910.36 → 1913.58] I've got a tab open to play around with that and kind of tear that apart.
[1913.66 → 1918.84] I'm always curious to see what other CSS frameworks are doing,
[1918.84 → 1921.66] what their best practices are, and what they're implementing as far as layout
[1921.66 → 1925.16] or as far as device-specific code.
[1925.62 → 1929.42] I had a lot of fun messing around with Golden Grid System,
[1929.98 → 1931.74] which has been out for a little bit.
[1931.80 → 1932.84] I know that's on GitHub.
[1933.56 → 1936.22] But Golden Grid was really cool because it's...
[1936.22 → 1938.56] I actually like their approach to the grid.
[1939.62 → 1942.18] Conceptually, I like their approach to doing layout with a grid
[1942.18 → 1944.28] a little better than what we even do in Foundation.
[1944.42 → 1946.06] They make some really smart decisions about that.
[1946.06 → 1951.04] What they trade is a total lack of support for any version of Internet Explorer
[1951.04 → 1954.92] before 9, which we're not really willing to give up in Foundation just yet.
[1955.30 → 1958.32] So we can't do exactly what they've done, but I do like what they did.
[1959.18 → 1963.12] And yeah, I'm interested in tearing into Inuit and seeing what they put together.
[1963.24 → 1965.72] But it's always fun to see all the different frameworks that people are working on
[1965.72 → 1971.48] because doing things more quickly with CSS is definitely a growing trend right now,
[1971.52 → 1972.54] and there's some good stuff right there.
[1972.68 → 1973.84] But that's me.
[1974.54 → 1975.18] I don't know about Matt.
[1976.06 → 1979.64] I'm pretty excited to see what's coming out on the JavaScript front-end world.
[1979.80 → 1981.58] I mean, I'm a big fan of Backbone,
[1981.66 → 1984.74] but there are a lot of other front-end libraries that are kind of on the rise still.
[1984.82 → 1988.08] So I'm just kind of sitting around and waiting until some more exciting stuff comes out.
[1988.40 → 1990.30] Really interested to see where Sprout Core goes,
[1990.66 → 1992.00] where Backbone continues to go,
[1992.28 → 1994.86] or a bunch of the other frameworks like that.
[1995.04 → 1996.72] So it seems like it's still really early,
[1997.08 → 1998.88] but there's some very exciting things that are on the horizon.
[1999.08 → 2000.80] So I'm just really excited in the next year
[2000.80 → 2003.16] to see what other kind of Backbone-type libraries we have
[2003.16 → 2004.54] to make our lives a lot easier
[2004.54 → 2007.04] for doing the more client-side heavy applications.
[2007.78 → 2010.06] So you're up to eight projects on your GitHub account.
[2010.32 → 2012.12] Is Git used company-wide?
[2012.90 → 2013.66] Yes, absolutely.
[2014.00 → 2016.46] Yeah, that was kind of something after I,
[2016.62 → 2018.02] a little while after I started.
[2018.02 → 2021.12] We were there using SVN for everything,
[2021.26 → 2025.34] and that was one area where I felt like we just really needed to company-wide,
[2025.44 → 2027.96] make the decision, do the cutoff, bite the bullet, teach everybody Git,
[2028.22 → 2029.74] and just standardize on Git straight up.
[2029.84 → 2032.82] And we've done that, and we've been very happy overall.
[2034.08 → 2036.48] For the designers, I mean, some of the command line stuff is pretty rough,
[2036.48 → 2039.36] but the Glee client made life much easier for everybody.
[2040.30 → 2041.90] I wanted to thank you guys for joining us today.
[2042.82 → 2045.54] I want to do a quick plug for, you know, Adam couldn't join us,
[2045.66 → 2049.06] but he's going to be interviewing your boss, Dimitri,
[2049.22 → 2052.10] I guess on Founders Talk, coming up on the 5x5.
[2052.18 → 2053.32] No, Brian.
[2053.68 → 2054.66] He's going to interview Brian.
[2055.06 → 2055.78] Brian, okay.
[2057.44 → 2060.94] Be sure and catch that if you want to see the business side of Curb
[2060.94 → 2064.68] on the 5x5 network with Adam in the very near future.
[2065.48 → 2066.02] Thanks, guys.
[2066.68 → 2067.80] Hey, thanks for having us.
[2067.82 → 2068.28] It was a lot of fun.
[2068.28 → 2069.28] Thank you.
