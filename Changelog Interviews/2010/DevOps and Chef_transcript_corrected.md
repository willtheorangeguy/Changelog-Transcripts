[0.00 → 18.90] Welcome to the Change Log episode 0.3.8.
[19.06 → 20.04] I'm Adam Stachowiak.
[20.26 → 21.00] And I'm Wynne Mechelen.
[21.26 → 22.32] This is the Change Log.
[22.40 → 24.30] We cover what's fresh and new in the world of open source.
[24.74 → 27.70] If you found us on iTunes, we're also on the web at thechangelog.com.
[28.08 → 28.92] We're also up on GitHub.
[28.92 → 33.14] Hey, at thegithub.com forward slash explore, you'll find some trending repos, some feature
[33.14 → 35.50] repos from our blog, as well as the audio podcasts.
[35.82 → 39.32] If you're on Twitter, follow changelog show, not the changelog.
[39.60 → 40.62] And I'm Adam Stack.
[41.04 → 43.40] And I'm Penguin, P-E-N-G-W-Y-N-N.
[43.94 → 49.10] Fun show this week, talk some DevOps and Chef with Corey Donahoe from GitHub and Seth Chisholm
[49.10 → 50.18] from Opcode.
[50.82 → 52.24] A lot of fun stuff happened in that space.
[52.30 → 54.54] You guys talked about Chef, and what else did you guys talk about?
[54.54 → 60.16] Just the whole topic of DevOps in general and how it's kind of an amalgamation of development
[60.16 → 64.32] and sysadmin, much the same way that we're amalgamation of design and development.
[64.76 → 64.94] Yeah.
[65.14 → 69.04] And Chef is a pretty wild tool for building some servers and doing some automated stuff,
[69.10 → 71.08] so I guess that's got to make their job a little bit easier.
[71.36 → 72.46] And our job easier, too.
[72.74 → 75.04] You know, we don't like to play too much in that area.
[75.20 → 76.48] We usually hire folks for that.
[76.56 → 80.18] But it makes it a lot more approachable for front-end folks like you and me.
[80.66 → 81.08] Very cool.
[81.08 → 83.34] We also have to do a little bill pan.
[83.44 → 85.60] We work with Jason Heifer over at GeniusPool.com.
[85.70 → 89.22] He runs an awesome job board.
[89.42 → 91.38] So we've got a few jobs to listen off.
[91.54 → 92.86] So, WIM, why don't you take the first one?
[93.48 → 93.80] Sure.
[93.94 → 97.46] You know, I think every developer wants to be a gamer developer.
[97.68 → 99.70] When they first start out, well, here's your chance.
[99.78 → 104.98] Of course, games, hiring a Ruby engineer can work locally or via telecommuting.
[105.10 → 105.96] So that's also a dream.
[106.52 → 110.06] Flexible hours, free time for personal projects, and awesome coworkers.
[110.06 → 113.86] Plus, you'll enjoy quadruple bacon pizza, at least occasionally.
[114.48 → 114.68] Nice.
[115.46 → 117.80] And the next one is DealBase.com.
[117.84 → 119.94] They're looking for a Ruby on Rails developer.
[120.02 → 121.26] Hey, WIM, I've got a couple questions for you, bud.
[121.32 → 122.20] Do you like Git?
[122.50 → 123.10] You know it.
[123.50 → 125.98] Do you write Ruby like you write English?
[126.18 → 127.70] Probably better than I write English.
[128.10 → 128.36] Sweet.
[128.72 → 133.28] Do you like Rails 3, and are you itching to use CoffeeScript?
[133.68 → 134.58] Yes and yes.
[135.06 → 135.34] Sweet.
[135.94 → 138.34] Are you interested in writing mobile applications?
[138.34 → 139.12] You know it.
[139.60 → 143.04] Well, that's good, because if you answer yes like you just did to all those questions,
[143.30 → 145.44] then Deal Base wants to talk to you.
[145.60 → 150.52] Deal Base is a well-funded, deals-based site looking for someone who knows Ruby, Rails,
[150.68 → 152.60] JavaScript, and test-driven development.
[153.02 → 153.68] Don't tempt me.
[153.74 → 154.46] I may give them a call.
[155.20 → 155.76] Do it.
[156.48 → 159.72] And finally, Media Temple is hiring a senior Pearl developer, and we don't know if this
[159.72 → 160.90] is age or title.
[161.74 → 162.80] Everybody knows Media Temple.
[162.88 → 164.40] They're a leader in the web hosting space.
[164.40 → 167.34] They want you to work in their Culver City, California office.
[167.88 → 171.52] Your primary mission will be to interact with customers and business owners as you add to
[171.52 → 173.70] and maintain their customer portal and user interface.
[173.90 → 177.10] If you're looking for a challenge and appreciate being recognized for your efforts, explore
[177.10 → 180.26] this opportunity with a recognized leader in the web hosting space.
[180.26 → 184.68] And if you want to check out any of these jobs whatsoever, go to thechangelock.com forward
[184.68 → 189.96] slash jobs and or geniuspool.com to find all these listings and more.
[190.32 → 195.56] If you want to have your job read on this podcast, just let us know through geniuspool.com.
[196.22 → 197.06] Fun episode this week.
[197.10 → 197.68] Should we get to it?
[197.92 → 198.46] Let's do it.
[198.46 → 213.20] We're chatting today with Corey Donahoe and Seth Chisholm ore from GitHub and from Opcode,
[213.32 → 214.34] respectively.
[214.64 → 216.90] Corey, why don't you introduce yourself and let the folks know who you are?
[217.42 → 219.10] Hey, my name is Corey Donahoe.
[219.32 → 220.84] As Wynn said, I work at GitHub.
[221.12 → 224.10] That's kind of a new job for me.
[224.10 → 229.86] But I've basically been an open source hacker and part-time or sort of sysadmin for the
[229.86 → 231.08] last eight to ten years.
[232.12 → 237.18] I have a number of projects available on GitHub at GitHub.com slash Atmos.
[237.54 → 239.00] That's A-T-M-O-S.
[239.88 → 245.70] And, you know, I basically am trying to wade my way through a very large code base that's
[245.70 → 249.30] been in use by most of my friends for the last two to three years.
[249.30 → 254.06] So it's been an interesting month to just kind of come up to speed on a larger legacy
[254.06 → 254.70] application.
[256.20 → 256.86] Fun times at GitHub.
[257.08 → 257.76] Seth, how about you?
[258.12 → 263.92] My name is Seth Chisholm ore, and I'm a technical evangelist for Opcode, Inc., the company behind
[263.92 → 264.52] Chef.
[265.20 → 269.90] And I've been a developer for, you know, the last ten years and sort of found my way into
[269.90 → 273.18] operations system administration over the last few years.
[273.80 → 277.92] And right now, you know, I'm just helping, you know, evangelize Chef, do training.
[277.92 → 279.76] I also help write cookbooks for customers.
[279.92 → 284.30] So I'm sort of, you know, a user just like everybody else, a Chef, and do that type of
[284.30 → 284.64] development.
[284.88 → 286.70] So, yeah, that's a little about me.
[287.40 → 291.06] So we're chatting today about DevOps in general and then Chef more specifically.
[291.22 → 293.94] Corey, why don't you make a stab at defining DevOps?
[294.76 → 295.74] It's a buzzword.
[296.64 → 296.82] No.
[297.30 → 303.22] It's kind of things that have been emerging from really talented system administrations
[303.22 → 306.20] that have kind of embraced, you know, reproducibility and automation.
[306.20 → 311.28] And I feel that, you know, there's been a number of people that have been doing it, but those
[311.28 → 313.16] people have kind of started to cross paths.
[313.50 → 318.80] And there's kind of a little movement brewing where, you know, people are really excited
[318.80 → 325.86] about kind of taking almost agile methodologies and applying them to, you know, deployment practices
[325.86 → 327.28] and systems operations.
[328.48 → 331.20] So, Seth, where does Chef fit into the DevOps landscape?
[331.20 → 334.00] Well, I mean, Chef's an important piece of that.
[334.08 → 336.96] I mean, we fit into sort of the configuration management and automation piece of that.
[337.20 → 342.58] But obviously, you can be doing DevOps and be doing it right and not be using any tooling,
[342.76 → 343.00] right?
[343.32 → 348.56] I think that once you adopt some DevOps practices, within your organization, you start to look
[348.56 → 351.34] to things like automation, configuration management.
[351.54 → 353.22] That question comes naturally.
[353.22 → 359.18] But, you know, we at Opcode and me in particular, you know, I'm a big believer that you can be
[359.18 → 361.16] lo-fi and still be a DevOps shop, right?
[361.48 → 365.42] So, but, you know, obviously we'd like everybody to use Chef.
[365.60 → 366.22] I think it's awesome.
[366.74 → 366.76] So.
[367.72 → 372.54] So as DevOps, is this an evolution of the sysadmin rule or something totally different?
[372.54 → 375.32] I mean, I'll step in.
[375.38 → 379.94] I sort of think that the biggest thing to remember about DevOps is it's a cultural and
[379.94 → 380.78] professional movement.
[381.62 → 386.96] So, I mean, if you think about that, that sort of drives everything through the rest of the
[386.96 → 388.14] DevOps discussion, right?
[388.42 → 393.24] So it's really just about that culture that a company is willing to adopt where their development
[393.24 → 396.76] team and their operations team has seen that chasm that exists between the two and that
[396.76 → 402.20] sort of like broken wall that develops toxicity that develops between the two groups.
[402.54 → 408.60] So, you know, I think that, you know, just following that, you start to see that, you
[408.60 → 411.96] know, that it's an evolution that's happened for both the developers and the operations roles.
[412.82 → 418.10] Yeah, I definitely think that that's kind of the awesome part of DevOps or the theme that
[418.10 → 423.14] really wins out is the cultural shift where everybody just gets along rather than, you
[423.14 → 428.00] know, everybody looking at operations as the BOTH that is keeping them from shipping their
[428.00 → 428.30] code.
[428.42 → 432.04] It's just a matter of getting everybody on the same page and understanding that, you
[432.04 → 436.16] know, the product lifecycle goes all the way through to deployment, not just tagging
[436.16 → 440.68] your release and that they're going to need to work together, you know, in an ongoing
[440.68 → 446.32] fashion in order to basically, you know, be a successful company and basically have a
[446.32 → 452.90] little bit of, you know, extra, you know, I don't know, extra expertise or extra interaction
[452.90 → 456.74] that's going to make them, you know, a more successful shop than the next one.
[456.74 → 463.30] You know, with the term web 2.0 and then now recently HTML5, we found the term means different
[463.30 → 465.46] things to different folks, and it evolves as you go.
[465.58 → 467.80] Are you finding the same thing with this DevOps term?
[468.84 → 469.00] Yes.
[469.10 → 470.36] Yeah, definitely.
[471.20 → 472.86] And that's why the confusion, right?
[472.86 → 476.76] And there's a lot of people trying to co-opt this for their own gains, which is another
[476.76 → 478.66] thing that's sort of bad about it, and it confuses people.
[479.56 → 483.74] But again, like trying to keep things simple and just understand that it's purely a cultural
[483.74 → 484.20] movement.
[484.38 → 488.28] It's about culture and process helps sort of like, I don't know, wade through some of
[488.28 → 489.48] the BS that comes out, right?
[489.54 → 493.50] People trying to say that they sell DevOps, or they have DevOps compliant tool sets or this,
[493.60 → 493.86] you know.
[495.50 → 500.38] It sort of allows you to use that as a litmus when you're seeing what somebody's selling.
[500.38 → 506.34] So I think the other thing that's fascinating is it's like in development world, Agile,
[506.42 → 510.74] the Agile development movement sort of got the business in line with the development team,
[510.84 → 510.96] right?
[511.00 → 513.96] Those two teams were working closely together, and I feel like this DevOps movement is sort
[513.96 → 517.84] of that final thing to bring the DevOps in line with operations, right?
[517.90 → 523.10] And now we finally got this like full life cycle where business is fully in line with the
[523.10 → 524.26] product all the way through.
[524.34 → 525.22] And I think that's really cool.
[525.86 → 529.92] So it was sort of like that last link that we needed to make it all happen.
[530.38 → 534.08] Yeah, because that was like one of my first jobs when I got out of college was like supporting
[534.08 → 536.56] a bunch of J2E app servers.
[536.82 → 539.22] And they had like complex QA and things like that.
[539.26 → 543.56] But there was definitely like a lot of finger pointing and basically, you know, the throwing
[543.56 → 548.24] the code over the wall and hoping that it works track, you know.
[548.26 → 553.98] But it was nice to see this start to emerge the last few years and people, you know, work
[553.98 → 558.02] more effectively together rather than, you know, complex, just really annoying meetings
[558.02 → 561.72] where everybody's talking about, you know, circumventing the process in order to meet deadlines and
[561.72 → 562.30] things like that.
[562.36 → 567.38] It's more, you know, from an upfront perspective, everybody being on the same page and working
[567.38 → 568.02] more effectively.
[569.42 → 574.10] You know, Adam and I are both front end developers and there's been this healthy tension between
[574.10 → 578.94] developers and designers and trying to get designers to be a little bit more technical
[578.94 → 582.80] and trying to get developers to be a little bit more design focused.
[582.80 → 588.26] Do you see the same tension between sysadmin types and developers and where that kind of
[588.26 → 588.76] crosses?
[589.72 → 590.20] Definitely.
[590.68 → 596.70] I think those three roles definitely they're traditionally everybody has kind of said I'm
[596.70 → 600.88] one of those three things and the really talented people generally bridge the gap.
[601.24 → 604.94] And I think that enough people have seen that people can do more than just one thing
[604.94 → 608.62] effectively, that it's almost inspirational, and you want to be good at those other things
[608.62 → 608.86] too.
[608.86 → 614.42] So, you know, if the operations team is perfect and the developers are perfect, you
[614.42 → 618.80] know, you should be able to mask a lot of the production type things to the designers
[618.80 → 622.20] so they don't even have to worry about, you know, oh, are all the services running on my
[622.20 → 625.96] local machine in order to spin up and like design some views or something like that.
[626.50 → 632.50] But it's more of a modern thing now and a lot more people are doing it rather than just,
[632.74 → 635.74] you know, a few small shops that you happen to read blogs about.
[635.74 → 636.18] Yeah.
[636.90 → 640.32] And I think the other thing we have happening is this line blurred between what is
[640.32 → 641.80] the application and what is the infrastructure.
[642.20 → 642.60] Right.
[642.64 → 646.08] And so the fact that the infrastructure is the application, the application is the
[646.08 → 647.86] infrastructure has really started to change a lot of that.
[648.34 → 651.66] I think we all realized we're there to enable the business.
[651.78 → 652.84] That's our ultimate end job.
[652.88 → 653.06] Right.
[653.12 → 653.98] Everybody on the team.
[654.38 → 656.40] And I think that's a great thing.
[656.42 → 658.56] And it's brought people into better alignment across the board.
[658.56 → 663.98] So, Seth, what's the elevator pitch for Chef, infrastructure automation for the masses?
[665.02 → 665.84] So, Chef.
[666.10 → 669.42] Well, high level, like Chef is a couple of things.
[669.72 → 671.76] It's sort of like all these things at once.
[671.84 → 673.66] So it's a library for configuration management.
[674.90 → 677.78] And it's also a configuration management system.
[678.62 → 682.42] And then an important thing, it actually does systems integration, helps you do that.
[682.48 → 684.24] And then it's also an API for your infrastructure.
[684.24 → 687.22] And so I'll go back and sort of, you know, explain each of those.
[687.34 → 691.88] So, I mean, Chef, the actual core product is a Ruby gem, and it's a library that you can
[691.88 → 693.40] use in other products.
[693.44 → 697.44] So you can see things like Corey Cinderella that actually leverage Chef, right, to do some
[697.44 → 700.70] lightweight configuration management within another application.
[701.40 → 706.46] And obviously, we've got the whole system, which we have, which is a Chef server, the Chef
[706.46 → 710.58] client that helps you actually configure your infrastructure and get things in line.
[710.58 → 716.06] But an important piece of all this is Chef takes, I think, things a step farther past
[716.06 → 717.18] things like Puppet and CF Engine.
[717.40 → 719.20] And we're a big believer in systems integration.
[720.04 → 724.38] And the fact that you can do, like, live search within your configuration management and actually
[724.38 → 727.96] do things like a load balancer can call out and get a list of all the app servers he needs
[727.96 → 728.70] to balance, right?
[729.12 → 734.30] Or an application server can actually call out and get a reference to the master database
[734.30 → 736.56] server or the slave database servers, things like that.
[736.98 → 739.06] You know, that's taken things to another step.
[739.06 → 742.32] And you've actually got a data-driven infrastructure, which is really cool.
[743.18 → 746.06] And obviously, it's a RESTful API at its core.
[746.38 → 748.52] And it can be an API for your entire infrastructure.
[748.84 → 752.88] The Chef server, the centralized Chef server that's indexing all this information about your
[752.88 → 757.50] infrastructure can be searched from a command line using Knife or actually in real time in
[757.50 → 759.14] other applications could leverage that data.
[759.60 → 762.40] So, I mean, that's sort of the high-level pitch about it.
[762.48 → 767.12] And I mean, you know, we can get into maybe some of the principles and stuff later.
[767.12 → 769.38] But I don't know, Corey's...
[769.38 → 770.38] I know Corey's working with Chef.
[770.38 → 772.98] Do you get, like, the configuration management search style stuff?
[773.24 → 774.70] Is that available on the platform?
[774.84 → 776.52] And if you host Chef server yourself?
[777.00 → 777.88] Or is that just available?
[778.08 → 778.18] Oh, yeah, definitely.
[778.18 → 778.46] Okay, cool.
[778.62 → 780.66] Yeah, I've pretty much only messed with Chef Solo.
[781.64 → 781.96] Yes.
[782.18 → 782.52] And that's...
[782.52 → 783.78] I mean, Chef Solo is awesome.
[783.86 → 785.58] And I think it's a great place to start.
[785.58 → 790.16] But if you want to really get into some of the cool stuff, you lose some of the benefits
[790.16 → 791.16] of that systems' integration.
[792.06 → 795.32] And you do need to leverage that centralized index data.
[797.08 → 801.36] And the platform really, you know, there's a lot of people get confused on the platform
[801.36 → 803.50] versus the open source Chef server.
[803.98 → 805.32] They're fully API compatible.
[805.68 → 808.50] And we plan on keeping them in that way, you know, for the future.
[808.70 → 809.68] Now, we've...
[809.68 → 812.88] Our big play on the Opcode platform is it's highly available.
[813.48 → 814.36] It's multi-tenant.
[814.36 → 814.96] It's scalable.
[815.18 → 820.06] I mean, the guys that sort of started Opcode, you know, you've got Adam Jacob, who'd worked
[820.06 → 820.90] for Puppet with years.
[822.84 → 825.92] Jesse Robbins, who used to be in charge of all of Amazon's infrastructure.
[827.04 → 830.46] And Chris Brown, who's sort of the core architect of Amazon EC2.
[830.54 → 833.04] So these guys definitely know how to build, like, scalable systems.
[834.20 → 838.72] So, you know, for us, we sort of say, look, just give that to us.
[838.80 → 839.98] We know how to scale the Chef server.
[840.10 → 841.34] We know how to make it highly available.
[841.52 → 843.24] You know, it's something you definitely don't want going down.
[843.24 → 849.62] And then we also add some extra things on top of that, like role-based authorities for
[849.62 → 850.36] doing some of that stuff.
[850.42 → 855.40] So you can actually put all kinds of different authorities on each different component of
[855.40 → 857.00] the Chef platform, whether it be nodes.
[857.14 → 858.42] You know who can see this node?
[858.46 → 859.30] Who can touch this node?
[859.38 → 861.30] Or data bags and all those different things.
[861.30 → 865.12] And that's another thing that if you leverage a Chef server is you can use data bags, which
[865.12 → 867.92] allow you to sort of have this centralized store to drop data.
[868.66 → 871.64] It could be user data for all the users that you need to put on each of your nodes.
[871.74 → 874.88] It could be application data for apps that you need to deploy out on your app servers,
[874.96 → 875.50] things like that.
[875.62 → 878.52] So, you know, that's definitely a huge win.
[878.60 → 882.30] And I think if you really want to do it sort of the Chef way and truly go data-driven,
[882.30 → 885.52] at some point you'll realize your sort of want to leverage a Chef server.
[887.58 → 891.78] And you also have a growing community around it with sharing cookbooks, right?
[892.22 → 892.92] Yeah, yeah.
[893.02 → 896.28] And that's actually something, you know, I've been a Chef user for about a year and a half
[896.28 → 897.26] before I started with Ops Code.
[897.36 → 900.60] I actually was in the Chef Alpha, my former company.
[900.60 → 903.56] And so I've been there since the start and seen it sort of evolve.
[904.24 → 908.56] And I think the cookbooks, you know, until I started Ops Code, I never really clicked with me.
[908.62 → 910.12] That's one thing we're going to try to get the message out.
[910.12 → 913.68] But cookbooks.opscode.com is sort of like rubygems.org.
[914.14 → 917.16] You know, a lot of people just thought, like, okay, we've got, you know,
[917.22 → 920.18] there's a GitHub repo for the Ops Code cookbooks,
[920.22 → 923.34] and I should just submodule that into my Chef repo and go ahead and start using those.
[923.72 → 927.74] But really the better way is to leverage cookbooks.opscode.com
[927.90 → 931.48] and use that as your main source, just like when you install a gem, right?
[931.52 → 933.58] You do a pseudo gem install, and it just comes on your system.
[934.10 → 936.46] So, you know, using Knife, which is our command line tool,
[936.54 → 938.52] you can do the same thing and sort of bring the cookbook down,
[938.52 → 941.36] and then you can start sort of leveraging and building on top of it.
[941.50 → 946.38] But that central community of sharing is one of the big things where Chef shines
[946.38 → 949.08] compared to some of the other configuration management tools.
[949.36 → 950.58] And I think it's one of the coolest parts,
[950.60 → 953.30] and we're definitely going to be evolving that in the next year,
[953.30 → 957.32] sort of making that site better and sort of, you know,
[957.36 → 959.58] making it more community-driven, closer to something like GitHub
[959.58 → 961.54] where you've got feedback from people,
[961.64 → 964.32] and you might have some stats that tell you how many people have installed the cookbook,
[964.38 → 965.98] how many are using it, you know, stuff like that,
[966.02 → 966.96] which I think would be really cool.
[966.96 → 970.76] Is the idea more with that type of platform to have, like,
[970.86 → 974.30] the one MySQL cookbook to rule them all or different flavours
[974.30 → 977.22] or just kind of embrace the community to collaborate
[977.22 → 982.04] and kind of agree upon what's the best, you know, general MySQL for deployment?
[982.40 → 985.08] I think we're definitely always going to have multiple versions
[985.08 → 989.12] because one of the big guiding principles of Chef is that, you know,
[989.20 → 990.60] there's more than one way to do it.
[991.38 → 994.58] We obviously, you know, everyone models our infrastructure slightly different.
[994.58 → 996.54] We're going to hopefully, with the Ops Code cookbooks,
[996.92 → 1000.54] sort of put forth some of the best practices and best configurations to get you started,
[1000.76 → 1002.84] but we know that people are going to have to change that.
[1003.76 → 1006.94] So there's probably always going to be some multiple cookbooks up there,
[1007.00 → 1009.44] and we're working right now on figuring out how we're going to namespace those.
[1010.38 → 1013.18] You know, the discussion we've had internally going back and forth is, like, you know,
[1013.20 → 1015.84] in Ruby, everyone comes up with clever names for gems,
[1015.84 → 1021.00] and we sort of want to make sure that the cookbook names give some indication of the function
[1021.00 → 1021.96] that cookbook's going to fill.
[1022.64 → 1025.06] So, you know, we're still trying to figure some of that out,
[1025.12 → 1028.10] but I think you're always going to have the fact that multiple people can, you know,
[1028.14 → 1029.66] place multiple MySQL cookbooks.
[1029.72 → 1032.54] Maybe they're all for doing different things up there, and that's cool.
[1032.68 → 1034.78] Like, we're all about that and all about embracing that.
[1035.36 → 1038.00] And just like in the rest of the Ruby world, you know,
[1038.22 → 1042.04] there might be multiple ones up there, and one's going to win out maybe just because of popularity
[1042.04 → 1043.50] or doing it slightly better.
[1043.50 → 1044.70] So I think that's a good thing.
[1045.72 → 1048.54] Speaking of creative names, Seth mentioned it.
[1048.60 → 1050.40] Corey, tell us about Cinderella, nay, Cider.
[1052.10 → 1053.72] It used to be called Cider.
[1053.90 → 1059.96] Cinderella is basically a chef solo run on your MacBook Pro.
[1060.10 → 1062.82] So the idea is to leverage RVM and Homebrew
[1062.82 → 1068.08] and get people going on OS X for open source collaboration trivially.
[1068.30 → 1073.18] So you get a system that's bootstrapped with MySQL and Postgres and Regis,
[1073.18 → 1077.44] Meccas, Congo, like Python, Node.js, and Erlang.
[1077.98 → 1082.34] And so that just seems to be kind of the fashionable libraries that people have.
[1082.66 → 1088.44] And the idea is that it's a centralized gem that you run when you boot your system for the first time,
[1088.50 → 1092.00] like when you do a fresh install, but you can continue to run over time.
[1092.00 → 1096.56] And it's the chef item potency where Cinderella just runs.
[1096.70 → 1098.98] If anything needs to be upgraded, it upgrades it.
[1099.42 → 1104.20] And if everything's fine, and you have the latest version of things, it just exits really quickly.
[1105.02 → 1109.48] And so the idea was kind of like we were talking about earlier with bridging the gap with designers.
[1110.06 → 1113.26] This came out of trying to get one of our designers going on a system.
[1113.26 → 1121.20] And it's cool when developers are in charge of their own machines because they're usually pretty anal about where things go and how they're set up.
[1121.54 → 1127.46] But when you're just trying to get a designer able to run your application that has some complex components,
[1127.96 → 1129.14] they just want it to work.
[1129.56 → 1133.88] So the idea was just to give it to our designer and say, hey, you have a running system.
[1134.14 → 1137.66] Like you're good, and you're basically set up with all the same tooling that we are.
[1137.66 → 1143.62] And you don't have to care about knowing how to add things to your startup environment with launch CTL
[1143.62 → 1148.92] or what version of Ruby you should be on because you might want P248 or P305.
[1149.12 → 1154.00] There's all these little things that basically people know what the best practices are,
[1154.10 → 1155.80] what you should probably be developing on.
[1156.16 → 1160.34] And if you just give that to them, they're generally happy to move on and just get some work done
[1160.34 → 1163.68] rather than spending a day or two messing around getting their system going.
[1164.40 → 1166.08] We had Max from Homebrew on the show recently.
[1166.08 → 1168.66] What's your take on Homebrew?
[1169.56 → 1170.36] I love it.
[1170.46 → 1171.96] I think it's a perfect model.
[1172.14 → 1175.74] I mean, Homebrew is actually, I think it's probably the most forked project on GitHub now.
[1176.36 → 1180.02] And so they're actually, there are stress tests for a lot of new features.
[1180.24 → 1182.18] It's like, will Homebrew kill the site, yes or no?
[1182.86 → 1184.48] But I really like the model.
[1184.60 → 1189.08] I was really impressed when I tried to get like NPM merged into Homebrew.
[1189.52 → 1193.78] And not only did they notice that I had forked it, amongst all these forks that they'd done,
[1193.78 → 1199.80] they noticed that I'd forked it, and two guys from the Homebrew project were like commenting in line and saying,
[1200.12 → 1202.22] oh, there's a slightly better way to do this, check here.
[1202.42 → 1204.44] You know, and it was the right kind of community.
[1204.60 → 1206.36] Like those guys really stay on top of it.
[1206.84 → 1210.34] And, you know, things might be broken one day, but they're generally fixed the next.
[1210.34 → 1215.94] So it was nice to just, you know, basically take the ops code Chef Solo.
[1216.62 → 1219.14] And what they have normally is like a package manager.
[1219.40 → 1222.76] And so what I was able to do was mimic the default package manager with Homebrew.
[1223.02 → 1226.82] And then you just declare, you know, Homebrew NPM and you get NPM.
[1227.44 → 1234.20] So it was kind of cool just to take advantage of that and to have those guys working hard to make sure that those packages work.
[1234.34 → 1236.58] Whereas you kind of just glue it all together with Chef.
[1236.58 → 1242.80] Yeah, I don't know if you know, too, up in the Core Chef project, there is a Homebrew provider now.
[1243.34 → 1244.92] So like the package resource.
[1245.10 → 1245.64] So it's sort of cool.
[1245.78 → 1249.78] Like that's actually there's a Mac ports one and a Homebrew one that are shipping with Chef at this point.
[1250.14 → 1252.12] So I need to actually check that out.
[1252.20 → 1255.12] I want to try 0.910, but I haven't yet.
[1255.22 → 1260.64] I was hoping to try it because of some of the newer dependencies that are out that I'd like to take advantage of.
[1260.64 → 1265.62] Like being able to run, you know, Ruinous as the default or something like that.
[1265.62 → 1268.84] But we weren't able to previously because of the Jason gem.
[1269.36 → 1272.14] But, yeah, it was Kurt Mile, I think, actually added that.
[1272.26 → 1273.42] He hit me up when he did it.
[1273.54 → 1276.30] And I've just been kind of busy and it works.
[1276.38 → 1278.24] So I haven't adopted the new stuff yet.
[1278.66 → 1279.16] That's cool.
[1280.10 → 1286.38] You know, with tools in this space like Chef and Puppet and Sprinkle, I'd like to propose that the Swedish Chef be the mascot for DevOps.
[1286.38 → 1293.10] What other tools are out there, and what's the complete landscape look like other than Chef?
[1294.10 → 1299.62] Oh, I mean, you've got obviously the old school CF engine, which a lot of shops are still using.
[1300.18 → 1304.44] And they've modified it heavily to work, sort of add the features they need.
[1304.56 → 1305.12] I think.
[1305.12 → 1308.20] And then Puppet, you've got a lot of places that depend on Puppet.
[1308.32 → 1309.60] I mean, Twitter, Google.
[1310.16 → 1314.54] And a lot of the things that were lacking in Puppet, these guys just sort of put a custom layer on top of it.
[1314.72 → 1316.76] The centralization we talked about a little bit.
[1317.42 → 1319.50] That's sort of a big differentiator between Chef and Puppet.
[1319.58 → 1322.04] But a lot of people have sort of found ways to make that work, right?
[1322.04 → 1324.68] Yeah, we're using Puppet at GitHub.
[1325.14 → 1328.62] And we were using Puppet for a lot of the internal servers at Engine Yard.
[1328.92 → 1333.38] Most of the App Cloud, the newer Amazon offering, is all Chef-based.
[1333.84 → 1336.44] But a lot of the older stuff is still managed by Puppet.
[1336.58 → 1340.22] So it's, you know, I think it really depends on what people are more comfortable with.
[1340.38 → 1345.36] And, you know, as long as they can get the job done, and it's automated, it's generally a good step forward.
[1345.90 → 1347.78] Yeah, something's better than nothing at this point.
[1348.30 → 1348.78] Exactly.
[1348.78 → 1351.84] If you're doing it, meet Cloud style still, you've got a problem there.
[1352.04 → 1352.60] So...
[1352.60 → 1356.54] Nothing else immediately comes to mind as far as config management.
[1356.80 → 1366.44] I mean, I think one of the other things that's kind of been left out is so many people just kind of take the whole DevOps idea for being just like, you know, configuration management.
[1366.44 → 1371.10] Where it's a bunch of other stuff where it's like, you know, metrics and things like that built around your system.
[1371.96 → 1375.02] We use a tool at GitHub called Silverlike.
[1375.74 → 1377.18] It's like Silverlike.
[1377.56 → 1379.04] Or I think it's Librato.com.
[1379.10 → 1380.84] I'll just send you the link in a minute.
[1380.84 → 1386.62] But it's an amazing tool that basically allows you to take process groups on your systems.
[1387.24 → 1390.64] And basically, it's almost like if the nice command worked very well.
[1390.64 → 1400.62] But we have like containers that, you know, the Git server will run in and then like our unicorn front ends and then Regis and, you know, all of our disk activity and things like that.
[1401.12 → 1412.36] What you can do is build policies and get really cool metrics about the state of your system and how, you know, introducing changes into your system impacted performance.
[1412.36 → 1413.76] And so it was really cool.
[1413.76 → 1417.66] One of the first things I got rolled out at GitHub, I basically killed performance.
[1418.26 → 1422.44] And so we have this neat way of approaching the problem where, you know, we can't go down.
[1422.56 → 1424.44] Like the whole world goes crazy when we're down.
[1424.90 → 1430.40] So we basically rolled it out to a subset of the front ends and then just started looking at Silverlike.
[1430.56 → 1432.32] And it was like, well, this isn't up to snuff.
[1432.32 → 1436.66] So we're going to roll it back, and we're going to do some performance analysis on the changes that were made.
[1436.90 → 1438.94] And we're going to roll it out again and look at these things.
[1439.22 → 1443.96] And metrics, I think, are like a huge part of that because without that, you know, the site would have gone down.
[1443.96 → 1450.14] And even without the Labrador tool in place, basically, the changes that I rolled out would have killed that front end.
[1450.30 → 1457.18] So it kind of managed everything in the system and kept it from just like killing the server more or less.
[1458.26 → 1459.58] So that is like.
[1459.58 → 1466.56] How much of DevOps is being, I guess, driven by this move to the cloud recently?
[1467.46 → 1469.32] I definitely think that that's an enabler.
[1469.66 → 1471.52] It makes it easier to do a lot of this stuff.
[1472.34 → 1477.96] And I think the fact that we've gone to this spot where we've got all these smaller nodes that are there to serve the application.
[1478.12 → 1480.14] You know, we're spreading things out and have all these things to manage.
[1480.26 → 1481.22] It's made it harder, right?
[1481.60 → 1488.60] It's that I think we're splitting things up into smaller servers in a lot of ways versus in the past, let's say, 10 years ago when we had these huge servers
[1488.60 → 1490.60] and we threw a bunch of apps on them and scaled them vertically.
[1491.14 → 1494.16] Now we're actually creating stacks that serve the application.
[1495.78 → 1497.78] And there's complexity that's added there, right?
[1497.78 → 1500.90] Even though the servers might not be that big, you still have more of them to manage.
[1501.34 → 1503.88] And we can't just keep hiring sysadmins to do it.
[1504.12 → 1504.84] So we have to get smarter.
[1504.84 → 1505.02] Yeah.
[1506.34 → 1512.04] It was kind of interesting to go from EY, which is basically all VMs, where we would almost tell people,
[1512.12 → 1512.96] oh, you need a search server?
[1513.08 → 1516.86] Well, get one with this amount of memory over here, and that's just going to be a search server.
[1517.04 → 1521.94] And then to go to GitHub and see how they're using big, beefy physical servers from Rackspace
[1521.94 → 1528.74] and just kind of using a tool like Libra do to manage that all in user space rather than having to do VMs or something like that.
[1528.74 → 1532.00] I think VMs make a lot of sense to a lot of people.
[1532.22 → 1535.50] Like the stuff you can do on Amazon and Rackspace right now is amazing.
[1536.22 → 1541.74] But I still think a lot of performance apps are going to have really racked boxes for at least a couple more years
[1541.74 → 1546.58] until somebody really comes in and gives people the not quite virtualized,
[1546.70 → 1552.48] but the performance they need that they get out of something like a traditionally racked box versus something like a VM.
[1552.90 → 1554.32] VMs are good enough for a lot of people,
[1554.32 → 1560.60] and kind of the world's exploding with applications and utilities that help people.
[1561.12 → 1563.26] And a lot of those don't have crazy performance needs.
[1563.34 → 1566.98] And I think you're going to see more of those in the future than people with crazy performance needs.
[1567.62 → 1572.86] But I think that both of those are going to be valid models for at least another two to three years.
[1573.42 → 1577.40] And the other thing that's really cool is we've seen some customers doing some very innovative things
[1577.40 → 1580.76] with their infrastructures that without VMs would be really hard to do.
[1580.76 → 1587.76] We've actually got a customer who every, so they sprint, they sync their sprints for their code releases with infrastructure rebuilds.
[1588.72 → 1593.54] And every two weeks they actually rebuild their infrastructure from scratch and lay the code on there.
[1593.70 → 1595.50] They go ahead and QA it, and then they release it.
[1595.76 → 1599.26] And so at the end of that, they kill the old infrastructure and start over.
[1599.34 → 1599.80] It's awesome.
[1600.12 → 1601.84] And you're seeing just things like that.
[1601.84 → 1602.20] The 10th floor test.
[1602.20 → 1603.98] Yeah, it's awesome.
[1604.20 → 1608.66] And I mean, buying into this whole infrastructure is code thing that basically says that, right, you know,
[1608.72 → 1614.26] we could rebuild our infrastructure just using a source code repository, you know, bare metal and app backup.
[1614.44 → 1615.30] That's all we need.
[1615.72 → 1616.88] I mean, that's a really cool thing.
[1617.42 → 1625.32] And that kind of innovation is, it really would be not as cost-effective or possible without something like virtualization, I think, to help you.
[1625.32 → 1635.68] Do projects like this offer some sort of de facto standardization where if I've got multiple infrastructure providers that I want to shop between,
[1635.82 → 1639.50] that I can move back and forth between those relatively more easily?
[1640.04 → 1641.78] I think that's on the horizon.
[1642.16 → 1648.18] I think the marketplace you sort of are talking about, you hear a lot of innovators or people, you know, future thinkers talking about that,
[1648.26 → 1653.54] this idea that you could actually multiple times a day switch your infrastructure around based on who's giving you the best cost.
[1653.54 → 1656.14] And I know there's some people out there starting to solve that problem.
[1656.18 → 1660.60] And I think it's just inevitable that that's going to happen, right?
[1660.80 → 1662.40] You're going to have this real-time marketplace.
[1662.72 → 1668.00] And, yeah, you're going to need something like Chef that says, okay, you know, either sync my infrastructure or rebuild it over here.
[1668.76 → 1672.08] And obviously, something like Chef makes that pretty easy to do.
[1672.22 → 1675.20] You know, you still have to worry about how do I get my application data moved around, stuff like that.
[1675.26 → 1676.46] You know, those are this kind of issues.
[1676.46 → 1686.68] But in theory, you know, you would need something like a configuration management tool that sort of rebuilds or has a copy of your infrastructure in some kind of repository to do that.
[1686.98 → 1692.30] So, yeah, there's a guy named Simon Wardley who gave like an OSCAN keynote.
[1692.90 → 1695.30] And he has a perfect blog that I've been enjoying.
[1695.30 → 1708.36] And he actually kind of commented on this whereas more of these cloud providers emerge, I hope I get this right, but as more of these cloud providers emerge, the people who are going to be able to work on each of them are basically going to have to adopt the lowest common denominator.
[1708.82 → 1714.86] And as a result, people probably won't like it as much initially because they won't be able to take advantage of what each of those are.
[1714.96 → 1717.08] And he basically referred to the cloud providers as islands.
[1717.08 → 1727.16] And so if you're on the Rackspace island or on the VMware island or on the Amazon island, and right now they're not all interchangeable, but, you know, like Seth was saying, that'll eventually happen.
[1727.62 → 1728.70] I just don't know how soon.
[1728.82 → 1730.76] What's your take on OpenStack and that effort?
[1732.12 → 1733.88] I think it's awesome, personally.
[1734.36 → 1738.50] I think it's good to finally have hopefully one API to rule them all.
[1739.28 → 1742.64] And, you know, it is going to be a little of that lowest common denominator, but I don't think that's a bad thing.
[1743.22 → 1745.92] So, I don't know, starting to see the people get behind it.
[1745.92 → 1748.32] It might start to be it's OpenStack versus Amazon.
[1748.68 → 1753.16] You know, it seems like all the smaller players are starting to sort of rally under OpenStack.
[1753.44 → 1756.86] Is this the DevOps version of Facebook versus Open Social?
[1758.50 → 1762.58] Well, I hope not because I want Open Social to succeed or OpenStack to succeed.
[1763.96 → 1769.84] Yeah, I feel like it's just market positioning.
[1770.12 → 1773.68] You know, basically, if those companies don't do it, someone else will eventually.
[1773.68 → 1776.20] So, they're trying to get people together and do it.
[1776.30 → 1784.44] But it feels like a bunch of traditional companies banding together to kind of embrace open source, but also stay viable as the market changes.
[1784.58 → 1789.30] And I think it's a viable option for a lot of enterprises who maybe can't use a public cloud.
[1789.40 → 1795.16] I think it's cool that they can, in their data centres, install a private cloud that its API is fully compatible with a lot of the tools.
[1795.38 → 1796.30] I think that's really cool.
[1796.30 → 1803.54] And it allows an enterprise to maybe mix data between stuff that maybe they have to keep internal and stuff that they can put out in the public cloud.
[1803.90 → 1807.96] So, I think that's a really neat thing because, you know, I think all of us get caught up in this.
[1808.20 → 1814.36] Remember, you know, we work for startups and all these innovative companies, but there are still a lot of enterprises out there that, you know, they can't move quite as fast.
[1814.42 → 1816.64] And I think something like OpenStack is going to be a good thing for them.
[1816.64 → 1824.78] So, you guys have seen the Twitter account ShitMyDadSays that Shatter now stars in on CBS.
[1825.68 → 1827.24] Have you guys seen ShitMyDevOpsSays?
[1827.78 → 1828.06] Yeah.
[1828.46 → 1828.62] Yep.
[1829.14 → 1831.22] That's not either one of you ghostwriting this, is it?
[1831.50 → 1831.92] No.
[1832.60 → 1838.66] The one that cracks me up is every time someone mentions a SaaS app as an example of cloud computing, I throw it in my mouth a little bit.
[1839.68 → 1840.04] Yeah.
[1840.40 → 1844.26] There's also DevOps Borat, which is kind of hilarious at times, too.
[1844.44 → 1845.32] DevOps Borat.
[1845.84 → 1846.24] Yeah.
[1847.12 → 1848.56] It's really dated jokes.
[1848.68 → 1853.50] Like, it's like your friend if he was still making Borat jokes at work about cloud technology.
[1853.76 → 1855.64] But it's pretty funny occasionally.
[1857.04 → 1861.72] Do either one of you have a good way to explain to your folks in Thanksgiving what you do for a living?
[1863.26 → 1863.62] No.
[1864.64 → 1865.38] It's difficult.
[1865.38 → 1869.50] I mean, especially if I try to explain the software you're making and then try to explain what an evangelist does.
[1869.70 → 1870.80] You know, that's tough.
[1872.84 → 1873.52] But, yeah.
[1874.20 → 1876.42] It's definitely trying to explain automation.
[1877.04 → 1877.40] Virtualization.
[1877.82 → 1883.44] I actually was trying to explain it to my – we just moved into a new neighbourhood and I met my 75-year-old neighbour yesterday.
[1883.88 → 1886.56] And that was very difficult to explain what I do to him.
[1886.62 → 1889.02] And he sort of just glazed over and smiled.
[1889.70 → 1889.82] So.
[1889.82 → 1890.22] Yeah.
[1890.86 → 1891.92] I know that conversation.
[1891.92 → 1896.70] I meet my neighbours and I tell them I work with – for Hewlett Packard, and it's, oh, I need you to fix my printer.
[1897.50 → 1897.70] Yeah.
[1897.98 → 1898.34] Exactly.
[1898.34 → 1901.58] No, I don't.
[1902.16 → 1911.76] GitHub is kind of easier to explain to people because it's just like, hey, it's where a bunch of people get together and share code to make – you know if you just tell them websites, they can understand that.
[1911.76 → 1915.88] But, you know, when I was at Engineer, it was a little more difficult.
[1915.88 → 1927.68] But, you know, if you try to explain that you help people make online businesses that, you know, process credit cards and do transactions, and sometimes they need a bunch of servers and some days they don't need as many.
[1928.46 → 1929.68] They kind of got virtualization.
[1930.64 → 1933.92] But in general, you know, my parents just think I'm a computer nerd.
[1936.46 → 1941.44] So this is the part of the show where we kind of turn it around and see what has you guys excited about open source.
[1941.60 → 1942.76] So, Seth, you're up first.
[1942.80 → 1943.78] What's on your open source radar?
[1944.74 → 1950.70] Well, in particular, since I'm a user chef, there are two things that I've actually started committing code to and I love.
[1951.04 → 1954.60] The Fog project is awesome, and I'm sure we've all heard about that.
[1954.60 → 1957.10] But it's sort of the Ruby abstraction layer for all the cloud providers.
[1958.68 → 1969.80] And, you know, it's sort of an interest to me because our tool knife, which is our command line utility, and it's sort of how, you know, a chef cook like all of us that are using chef actually interact on a daily basis with chef.
[1969.88 → 1974.74] It's this awesome, like, command line utility that 37 signals donated to the community and sort of taken on a life of its own.
[1975.50 → 1980.96] And under the covers, like, you can actually call knife bootstrap or knife EC2 server create.
[1981.58 → 1986.00] And, you know, it'll pick up your credentials and using Fog under the covers will actually start an instance.
[1986.00 → 1992.10] It's get the information back about how to log in that server and then start bootstrapping it with chef, which I think is really cool.
[1992.30 → 1994.96] So, I've really started messing with that quite a bit more.
[1995.02 → 1998.56] And I think, you know, Corey actually being an engineer, those guys are the guys that started the project, I think.
[1998.60 → 2000.24] And it's a very cool project.
[2000.24 → 2010.90] Other than that, I've got a lot of interest lately with RVM and homebrew and some of those things just, you know, for the reasons that Corey mentioned, just being able to configure and test under multiple versions of Ruby and that kind of stuff.
[2010.96 → 2012.86] So, those things have really made it a lot easier on me.
[2013.14 → 2023.74] Speaking of RVM, I've gotten into Infinity Test and some others lately that allow you to test multiple RVMs as you're developing gems, you know, to test multiple versions of Ruby as you go.
[2023.86 → 2024.94] And those are really cool.
[2025.90 → 2026.76] That's very cool.
[2028.12 → 2028.56] Corey?
[2028.56 → 2028.60] Corey?
[2030.02 → 2030.46] No.
[2030.64 → 2032.14] Basically, Fog's pretty amazing.
[2032.32 → 2036.90] Was has been doing a really solid job of just kind of working with the community and getting people.
[2037.06 → 2043.60] If you're into, you know, working with clouds and things like that, that's, you know, it's a really pretty powerful tool.
[2044.26 → 2058.06] It's not open source, but the Vibrato tool I mentioned earlier is just amazing for keeping systems under control and getting metrics around what the different components in your system are working with.
[2058.06 → 2062.68] There's also, we use Collected for certain parts of our reporting.
[2062.68 → 2065.88] So, we've been using a tool called Visage.
[2066.62 → 2072.30] I think that the guy, he might work at, he works at Bulletproof Networks.
[2072.34 → 2072.48] Okay.
[2072.48 → 2077.46] I thought he worked on Chef or something like that, but he apparently does not.
[2077.56 → 2082.60] But it's a different and slightly newer and nicer interface to Collected.
[2082.74 → 2088.58] The old Collected standard graphs are like GD, and they feel like they're from 2000.
[2088.58 → 2096.26] The newer stuff at least feels like, you know, it was written by people with a little bit of taste for designing things.
[2096.50 → 2098.70] So, I'm pretty impressed with that.
[2099.60 → 2105.98] Other than that, there's been very little that I can think of right now that comes to mind.
[2106.22 → 2110.52] The Opcode platform is pretty much what I would tell people to check out.
[2110.76 → 2111.82] So, I'm not really sure.
[2112.66 → 2118.20] The platform, that's the other thing I just want to mention to everybody is like you can sign up right now for free, and you get five servers for free.
[2118.32 → 2119.88] So, you can manage up to five servers right now.
[2119.96 → 2121.48] And honestly, we're in beta.
[2121.66 → 2124.42] So, if you have more than five servers, we're probably not going to charge you.
[2124.84 → 2128.80] So, definitely if you're getting started, I would say get out there and just sign up.
[2128.86 → 2131.38] And there's some really cool getting started guides that can help get you rolling.
[2131.38 → 2136.44] But, you know, I'm usually in the Chef IRC rooms too if you're getting started.
[2136.58 → 2141.24] It's just my Twitter handle which is S-C-H-I-S-A-M-O-S-C-H-I-S-M-O.
[2142.06 → 2145.56] And, you know, like I said, I'm sure Corey can tell you the same thing.
[2145.58 → 2148.80] It doesn't take a lot to get rolling and start doing something productive.
[2149.90 → 2155.00] Yeah, that's kind of the best bet is when the next time or when you need someone else to do it, it's pretty trivial.
[2155.28 → 2156.66] It's always kind of nice.
[2156.66 → 2161.06] Well, our users have been hankering for some non-web content on the changelog.
[2161.12 → 2161.98] And this is right up their alley.
[2162.14 → 2164.14] So, certainly appreciate you guys joining us today.
[2165.02 → 2165.16] Yeah.
[2165.70 → 2166.48] Thanks for having us.
[2166.48 → 2166.54] Thanks for having us.
[2166.54 → 2184.88] See it in my eyes
[2184.88 → 2188.52] So how could I forget when
[2188.52 → 2194.28] I found myself for the first time
[2194.28 → 2198.00] Safe in your arms
[2198.00 → 2200.12] As a dark passion
[2200.12 → 2202.08] Thank you for having us here.
[2202.08 → 2202.66] Thank you.
[2202.74 → 2204.58] Thank you.
[2204.58 → 2206.84] Thank you.
[2206.90 → 2207.40] Awesome.
[2207.44 → 2209.16] Bye-bye.
