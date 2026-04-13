[0.00 → 4.72] Well, I haven't looked into it too much, but there is Automaton that comes standard with Macs.
[4.80 → 4.94] Yeah.
[5.02 → 8.90] And you probably have to write AppleScript, which is immediately something I don't want to look at.
[9.00 → 13.42] But you can do a lot of automation just natively on the Mac without any extra software.
[13.42 → 16.40] Yeah. So have you written AppleScript's? Because I have.
[17.86 → 19.24] I'd rather do the manual way.
[19.88 → 23.82] That being said, there is a JavaScript interface now into scripting the Mac,
[23.98 → 26.64] but I've also tried to use that and to very little success.
[26.84 → 26.98] It's still terrible.
[26.98 → 30.52] And like the docs, yeah, the documentation is just like, I can't, it's inscrutable.
[30.68 → 31.46] How do I even use it?
[31.46 → 33.80] Like I understand JavaScript, but I can't use this API.
[36.34 → 38.90] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[39.26 → 41.32] We love Linde. They keep it fast and simple.
[41.32 → 43.82] Check them out at linode.com slash changelog.
[44.12 → 46.10] Our bandwidth is provided by Vastly.
[46.46 → 50.00] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[50.28 → 52.00] Get a demo at LaunchDarkly.com.
[52.60 → 53.98] What's up, JS Party people?
[53.98 → 58.84] Well, have you ever wondered if you could be offering a faster, less buggy experience for your customers?
[59.40 → 64.44] Well, with Ray gun Error and Performance Monitoring, you have all the information you need at your fingertips
[64.44 → 70.08] to quickly find and fix errors and performance issues across your tech stack down to the line of code.
[70.40 → 73.26] Ray gun makes it easy to monitor the impact of your performance improvements,
[73.46 → 75.90] quickly identify issues across web and mobile apps,
[75.90 → 78.86] and see how your code performs in the hands of your customers.
[79.36 → 82.94] This saves you time, this saves you money, and this saves your sanity.
[83.28 → 87.92] Head to Raygun.com to join thousands of customer-centric software teams who use Ray gun every single day.
[88.22 → 92.08] Again, Raygun.com to give them a try with a free 14-day trial.
[92.08 → 116.12] This is JS Party, your weekly celebration of JavaScript and the web.
[116.12 → 119.74] We take requests, just like your favourite wedding DJ.
[120.14 → 125.74] You can head to jsparty.fm slash request and let us know what you'd like to hear about on the pod.
[125.96 → 127.52] We also have an awesome back catalogue.
[127.98 → 131.96] Find our recommended and popular episodes at jsparty.fm.
[132.14 → 133.20] Okay, let's get into it.
[133.24 → 134.70] Hey, it's party time, you all.
[134.70 → 142.44] It's JS Party time.
[142.66 → 144.38] It's JS Party time.
[144.78 → 146.26] Get jacked for JS Party time.
[146.32 → 147.14] Oh, hi.
[147.42 → 148.30] I didn't see you there.
[149.02 → 152.10] I was just attending the pep rally for JS Party.
[152.92 → 154.24] And now I'm jacked.
[154.46 → 155.86] I'm Jared, your internet friend.
[156.24 → 159.40] And I'm joined by my friend, Nick Needed.
[159.54 → 160.24] What's up, Nick?
[160.40 → 160.98] Ahoy, ahoy.
[161.08 → 161.66] Hi, jacked.
[162.42 → 163.32] Are you a dad?
[164.12 → 164.60] Yes.
[165.60 → 166.60] Hijacked, I'm dad.
[167.62 → 170.46] You didn't quite finish the line, but I appreciate the effort anyway.
[170.92 → 171.34] Team effort.
[171.64 → 175.24] And it's just you and me here today, but I brought you something.
[175.38 → 176.16] I hope you appreciate it.
[176.16 → 177.20] A little gift from me to you.
[184.60 → 187.40] Can't play any more of it, otherwise we'll get demonetized again.
[187.48 → 189.10] But that was a good 12 seconds.
[189.56 → 192.48] I was trying to think of what the kids said at the end of it.
[192.48 → 194.80] I have not heard that song in a long time.
[195.10 → 197.16] All I remember is Will Smith saying, daddy loves you.
[197.38 → 197.46] Yeah.
[197.46 → 198.32] Daddy loves you.
[198.70 → 199.90] I don't remember the kids line.
[200.04 → 201.44] I think it was actually his son, wasn't it?
[201.44 → 201.74] I think so.
[202.62 → 202.94] Yeah.
[203.90 → 205.28] Making him famous at a very young age.
[205.34 → 209.34] Of course, the Dr. Evil version with Mini-Me is even better.
[209.34 → 212.52] In which he says, mini-me, you complete me.
[213.26 → 216.50] That's a set of movies that I haven't seen in a long time that I've been thinking about.
[216.84 → 217.56] But I'm just...
[217.56 → 218.24] The Austin Powers?
[218.30 → 218.50] Yeah.
[218.78 → 219.94] I just worry that they won't hold up.
[219.94 → 223.32] I have a feeling they do, because I still quote them on a regular basis.
[223.66 → 226.64] So maybe parts won't hold up, but there's got to be good stuff in there.
[227.00 → 229.02] I mean, I eat a baby, you know?
[229.38 → 230.16] Gold member.
[230.32 → 231.56] I love gold.
[231.96 → 235.02] I mean, there are lots of stupid things that are funny still, to me at least.
[235.12 → 236.98] But I'm perpetually 12 years old, I think.
[237.66 → 238.86] Well, I have a question for you, Nick.
[238.88 → 240.18] Do you like April Fool's Day?
[240.64 → 241.90] No, I don't.
[241.90 → 244.26] I don't either.
[245.26 → 246.32] But here we are.
[246.80 → 247.78] It's April Fool's Day.
[248.58 → 250.42] Probably the worst day on the internet, isn't it?
[250.48 → 250.80] Mm-hmm.
[251.76 → 252.16] For sure.
[252.24 → 254.42] So bad that none of our friends showed up for Jazz Party.
[254.56 → 258.12] They're just like, we're just going to peace out and not be on the show today,
[258.18 → 259.50] because we want to avoid internet.
[261.26 → 262.44] But here we are.
[262.56 → 265.18] It's April Fool's, and so none of the headlines can be believed.
[265.18 → 268.18] So based on that, I came up with this cool...
[269.02 → 270.22] You decide if it's cool.
[270.22 → 273.32] I came up with this game called Head Lies.
[274.04 → 275.80] Now, if not Head Lies, that would be gross.
[275.92 → 278.18] It's Head Lies, like fake news, you know?
[279.30 → 282.92] And I thought I would pitch it to you today, live on the air.
[283.54 → 283.76] Okay.
[283.96 → 286.44] But first, let's talk about some of the big news that came out.
[286.48 → 288.68] This is real news that launched this week.
[288.72 → 290.02] Kind of big deal, it seems like.
[290.18 → 291.42] I just wanted to get your take on it,
[291.90 → 297.60] which is the Dino Land folks now have their own company.
[297.60 → 302.26] So Ryan Dahl and Bert Elder wrote at the beginning of this week,
[302.46 → 304.34] announcing the Dino company.
[305.20 → 306.84] And they're taking it official.
[307.34 → 308.38] They've raised money.
[309.04 → 314.70] $4.9 million of seed capital from folks from Four River Ventures,
[315.80 → 317.58] Guillermo Rout from Routh Capital.
[318.02 → 320.70] We know him from Tercel and Next and those things.
[321.42 → 323.28] Lee Jacobs from Long Journey Ventures,
[323.28 → 326.24] the Mozilla Corporation, Shasta Ventures,
[326.54 → 329.68] and a longtime collaborator, Ben Nordics,
[330.28 → 334.28] all invested up to almost $5 million into this deal.
[334.44 → 337.12] And now Dino's like this official business now.
[337.40 → 337.52] Yeah.
[337.72 → 339.58] So can you maybe explain it to me?
[339.74 → 341.84] Like what they're actually doing?
[341.90 → 342.52] Like you're five?
[345.22 → 346.38] Limited liability.
[346.60 → 346.74] No.
[346.74 → 349.16] What are they doing?
[349.46 → 353.38] So I don't know exactly what they're going to do.
[353.50 → 356.50] I will tell you that they're not going to do an open core business model,
[356.68 → 359.62] which would be where they provide certain features of Dino
[359.62 → 361.42] and some sort of like an open source core,
[361.70 → 364.82] and then build on top of that around it,
[365.14 → 368.04] more advanced or pro or premium features of Dino,
[368.26 → 370.92] and make that what you pay for.
[371.50 → 372.46] They're not doing that.
[372.46 → 378.98] In fact, the software is MIT licensed and will retain the MIT license.
[379.52 → 381.06] In fact, Ryan says in their post,
[381.18 → 384.08] for Dino to grow and be maximally useful,
[384.22 → 386.02] it must remain permissively free.
[386.28 → 388.82] We don't believe the open core business model is right
[388.82 → 391.50] for a programming platform like Dino.
[392.68 → 395.10] We do not want to find ourselves in the unfortunate position
[395.10 → 398.46] where we have to decide if certain features are for paid customers only.
[398.84 → 400.72] That's really the rub with these open cores.
[400.72 → 402.48] It's like deciding what goes where,
[402.66 → 404.58] and there's a conflict of interest at different times,
[404.60 → 407.38] and it can be difficult to navigate that successfully.
[408.20 → 409.78] When they say, if you watch our conference talks,
[409.82 → 412.28] you'll find we've been hinting at commercial applications
[412.28 → 414.34] of this infrastructure for years.
[415.18 → 417.48] We are bullish about the technology stack we've built
[417.48 → 421.44] and intend to pursue those commercial applications ourselves.
[422.10 → 425.02] Our business will build on the open source project,
[425.02 → 427.82] not attempt to monetize it directly.
[427.82 → 431.50] So that's what they're saying now, you know, TBD,
[432.08 → 433.68] what exactly all that means.
[434.34 → 436.82] There is on the new Dino.com,
[436.92 → 438.92] so they probably shelled out some of that 5 million
[438.92 → 442.02] on getting Dino.com because it's always been Dino. Land,
[442.36 → 444.78] and now they have Dino.com because it's official.
[445.56 → 447.34] They have a new deployment section,
[447.54 → 450.86] which seems to hint at their first potentially commercial offering.
[451.06 → 451.26] Yeah.
[451.66 → 453.52] I just don't know exactly what that is.
[453.58 → 454.84] Did you check out that deploy thing?
[454.84 → 457.68] Yeah, that does seem to be the first product
[457.68 → 460.00] from the Dino company, I guess you could put it.
[460.38 → 462.22] That's what I was trying to understand.
[462.48 → 464.92] In terms of, I guess, what I already know,
[465.04 → 467.62] they call it a globally distributed JavaScript VM.
[468.28 → 471.30] So it's a V8 runtime where you can run your JavaScript,
[471.56 → 473.80] your TypeScript, your WebAssembly code
[473.80 → 476.80] at the edge worldwide is what they say.
[477.30 → 478.60] What I'm trying to understand,
[478.70 → 481.56] is this their own custom way to run Dino
[481.56 → 484.44] as like a Lambda function type thing?
[484.60 → 485.82] Is that comparable?
[486.52 → 488.96] It seems like that's what it is.
[489.18 → 493.14] Yeah, probably competing with Cloudflare workers
[493.14 → 495.24] and Netlify functions,
[495.52 → 497.62] whatever their Netlify functions thing is called.
[498.96 → 500.22] But can't all these other providers
[500.22 → 502.04] just run Dino as well and do the same thing?
[502.08 → 504.14] It seems like maybe they'll have some secret sauce
[504.14 → 505.90] that makes it fast or cheap
[505.90 → 507.74] or whatever way they can compete
[507.74 → 512.12] and make it better than what these other cloddish things
[512.12 → 512.70] are providing.
[513.22 → 514.80] That's why I say it's kind of to be determined
[514.80 → 516.94] on whether there's a real value proposition there
[516.94 → 519.48] because anybody can spin up the Dino runtime
[519.48 → 522.58] and run it in some sort of VM or container environment
[522.58 → 524.44] and provide you access to that, right?
[525.06 → 526.10] I think, yeah.
[526.72 → 530.06] And kind of what they're touting in the blog post
[530.06 → 532.66] and on the Dino deploy landing page,
[532.66 → 535.82] the runtime or the environment that you would deploy to
[535.82 → 538.82] is very similar to the Dino CLI.
[539.02 → 541.44] So it makes it really seamless for development
[541.44 → 544.14] because you run it basically the same way
[544.14 → 546.66] and pass it in for the cloud version.
[547.28 → 550.34] And then also, I think in the blog post
[550.34 → 551.84] they were touting the ability,
[552.04 → 553.52] like one of the key features of Dino
[553.52 → 556.74] is its kind of different take on the security model,
[557.18 → 558.22] a JavaScript runtime,
[558.22 → 562.84] where specifically when you run Dino just by itself,
[563.32 → 564.58] you don't have access to the network,
[564.68 → 565.98] you don't have access to the file system,
[566.04 → 567.20] you don't have access to any of this.
[567.94 → 570.02] And what I got from this is that
[570.02 → 571.88] if you don't allow those flags
[571.88 → 573.66] in what you're actually deploying,
[574.20 → 576.24] then that portion of the Dino runtime
[576.24 → 577.10] just doesn't ship.
[577.34 → 579.02] There's absolutely no way
[579.02 → 581.50] to do any kind of file system stuff if it's not.
[581.72 → 582.40] That's cool.
[582.50 → 582.66] Yeah.
[582.92 → 583.66] It's kind of annoying.
[583.76 → 584.50] Have you done any Dino?
[584.50 → 587.00] So I've done some just toying with it lately,
[587.14 → 588.28] just building a couple of things
[588.28 → 588.92] that are kind of like,
[589.00 → 590.08] I would normally write these
[590.08 → 592.58] just in Ruby or in Node or whatever.
[593.02 → 593.26] And I'm like,
[593.30 → 594.30] well, I'll just try Dino out
[594.30 → 596.78] just for utilities and scripts.
[597.56 → 598.50] And I actually found that
[598.50 → 599.48] this kind of headline flags
[599.48 → 600.20] are kind of annoying.
[600.76 → 601.32] And I get it.
[601.36 → 602.58] I think it's probably worth the trade-off
[602.58 → 603.54] at the end of the day.
[603.64 → 605.58] But allowing file system access,
[605.92 → 607.60] dash allow env is one,
[607.68 → 609.28] just to get an environment variable.
[610.50 → 611.88] And so it is definitely a trade-off.
[611.88 → 614.38] And I find it to be kind of annoying
[614.38 → 615.30] for writing scripts,
[615.38 → 617.40] but maybe that's just not the main use case
[617.40 → 618.68] for Dino's scripting.
[618.96 → 618.98] Yeah.
[619.38 → 620.66] So, I mean, that really puts it,
[620.78 → 621.66] it kind of flips it, right?
[621.72 → 623.00] Because if you write a script
[623.00 → 624.54] and give it to me to run,
[625.24 → 627.68] you have to tell me exactly how to run it too.
[628.60 → 630.38] And you as the scriptwriter,
[630.48 → 632.34] do you have to then do the checks?
[632.58 → 635.00] Like, do I have access to the environment variable?
[635.24 → 635.44] Nope.
[635.58 → 636.64] Throw up this error message.
[637.14 → 637.54] Yeah.
[637.62 → 639.24] Or does the thing just blow up, right?
[639.24 → 641.68] Because, I mean, if you try to run it without,
[641.94 → 643.16] it will just error out.
[643.48 → 644.60] Like, the runtime just errors out.
[644.66 → 645.72] It says, I can't run the script
[645.72 → 647.58] because I need access to this, and I don't have it.
[647.66 → 650.70] So it tells you, run it again with dash allow env.
[651.28 → 652.08] So that's nice.
[652.26 → 653.20] But, yeah, I don't know.
[653.56 → 654.14] I'm not sure.
[654.24 → 657.38] I think, ultimately, that trade-off
[657.38 → 660.44] was one that they were very serious about making.
[660.66 → 662.88] And so kind of putting a stake in the ground
[662.88 → 664.16] and saying, well, it's worth it.
[664.16 → 666.24] Because, and it sounds like if that's the case,
[666.28 → 667.24] if you can ship these, like,
[667.80 → 669.92] miniaturized container runtimes
[669.92 → 673.38] that don't even have the dangerous stuff in them
[673.38 → 674.34] in those cases, right?
[674.68 → 676.98] Like, it can't actually access the file system
[676.98 → 678.04] because it doesn't even have those bits
[678.04 → 679.00] anywhere in the binary
[679.00 → 680.52] and it's just not going to work.
[680.80 → 683.64] I think that's pretty cool for security.
[684.08 → 684.20] Yeah.
[684.68 → 685.96] Dino is, like,
[686.02 → 688.72] I haven't really taken too much time to play with it,
[688.76 → 691.70] although it's definitely on my list of things to look into.
[691.70 → 694.62] And going back to that runtime,
[694.82 → 697.42] that's really, like, the appeal of it to me,
[697.56 → 699.46] I think, the most right now
[699.46 → 702.18] is the idea that you can write your scripts.
[702.42 → 704.64] Like, if I'm thinking of things that I would want to do,
[704.70 → 705.98] it'd be, like, command line applications
[705.98 → 708.32] where I'm writing stuff in Bash right now
[708.32 → 709.34] and I write it in Bash
[709.34 → 711.62] because I know that Bash is probably on your system
[711.62 → 715.10] and there's not really, like, a need to, you know,
[715.16 → 716.32] to NPM install anything
[716.32 → 717.76] or set up anything like that.
[717.76 → 720.30] And that's, like, a knock against Node
[720.30 → 723.38] and why I don't write command line stuff like that
[723.38 → 725.84] because I consider, like, global modules
[725.84 → 727.06] to be, like, ephemeral
[727.06 → 730.32] and you'd have to, like, provide, like, a NPM install
[730.32 → 731.26] and then get all of that
[731.26 → 732.70] and then you'd be able to run the script.
[733.12 → 733.66] But with Dino,
[733.90 → 737.36] it sounds like you can create, like, an executable
[737.36 → 738.74] that has the entire runtime
[738.74 → 739.98] and everything you need in it
[739.98 → 741.34] and then just ship that.
[741.44 → 742.28] Yeah, single binary.
[742.56 → 742.76] Yeah.
[743.10 → 744.54] That's one of the big things.
[744.54 → 747.04] Which is spectacular for distribution, right?
[747.04 → 747.24] Yep.
[747.56 → 748.18] Yeah, exactly.
[748.40 → 749.36] That's one of the big things
[749.36 → 752.70] that I've seen Go being hoisted up as,
[752.80 → 754.24] like, being a really great way
[754.24 → 758.58] to build these completely self-contained binaries
[758.58 → 759.86] that contain everything you need.
[760.00 → 761.28] It's a perfect language
[761.28 → 765.24] for creating those command line scripts
[765.24 → 765.90] if you need it
[765.90 → 767.22] without having to worry about
[767.22 → 768.82] what's actually available on the system.
[769.40 → 771.00] And now, like, I really like this
[771.00 → 772.60] because now I can do it with JavaScript
[772.60 → 774.24] and it's a lot easier.
[774.24 → 775.12] Yeah, exactly.
[775.44 → 777.18] We actually just shipped an episode of Go Time
[777.18 → 778.00] all about releasing
[778.00 → 779.66] and there's a project called Go Releaser
[779.66 → 782.20] and a lot of the conversation on that episode is
[782.20 → 785.32] with Go, I just create a username and personal binary
[785.32 → 787.36] and then I just, like, send that where it needs to go.
[787.46 → 789.22] What kind of release process do I need?
[789.36 → 790.72] You know, so some of the argumentation was, like,
[790.76 → 794.30] is this even necessary to have these, like, release tools?
[794.84 → 797.32] Because it really is as simple as, you know,
[797.38 → 798.44] generating that binary
[798.44 → 801.62] and then you can FTP it, you can SSH it,
[801.70 → 803.26] you can drop it in your Slack channel,
[803.26 → 804.90] you could probably email it if it's small enough
[804.90 → 806.94] and pass it around
[806.94 → 808.46] and as long as it's been compiled
[808.46 → 810.18] for, you know, everybody's architectures,
[810.22 → 811.92] which it has, for the most part,
[811.96 → 814.56] it's just going to work on everybody's machines,
[814.64 → 816.20] which has been one of the reasons
[816.20 → 818.32] that Go has really succeeded.
[818.42 → 819.56] I think that's a huge advantage
[819.56 → 820.96] that Dino has over Node.
[821.62 → 823.06] And I'm sure there's Node efforts
[823.06 → 827.32] to provide tooling around making that be a thing,
[827.44 → 829.56] but having it built right into the project
[829.56 → 830.58] and being a first-party thing
[830.58 → 832.66] is, I think, going to be something that sets it apart.
[832.66 → 833.06] Totally.
[833.36 → 834.48] In terms of the business side,
[834.52 → 835.40] I'll just say, like, you know,
[835.42 → 837.50] to Ryan Dahl and the team, like, you know,
[837.84 → 839.18] congrats, go ahead and get that money,
[839.30 → 840.70] get that sustainability there.
[840.78 → 841.72] We know last time around,
[841.80 → 843.74] I don't remember the entire history of Node.js,
[843.90 → 846.38] but I know, like, Ryan created this awesome thing
[846.38 → 848.94] and many people got involved
[848.94 → 850.32] and there are lots of early adopters
[850.32 → 852.22] and lots of other people working on it as well.
[852.72 → 853.98] And he left the project,
[854.28 → 855.40] it went on from there.
[855.72 → 857.16] And it seems like this time, you know,
[857.16 → 858.06] he worked at Joint
[858.06 → 860.24] and there was, you know, IP issues.
[860.24 → 862.12] There's lots of stuff that went in and out of that.
[862.70 → 863.70] NPM came along
[863.70 → 865.20] and made a big business
[865.20 → 866.82] around the package management side.
[867.34 → 868.36] And this time it's like,
[868.52 → 869.36] I feel like, you know,
[869.42 → 871.56] Ryan is trying to correct
[871.56 → 873.54] a lot of his mistakes with Node
[873.54 → 875.14] is the way he kind of set out with Dino.
[875.74 → 877.08] You know, he came out with that talk,
[877.16 → 877.74] 10 mistakes,
[878.12 → 879.28] 10 things I regret about Node.
[879.78 → 881.54] And then Dino was kind of his new idea
[881.54 → 882.84] of fixing those things.
[882.94 → 883.90] And it seems like maybe Dino,
[884.06 → 884.60] the company,
[885.22 → 886.64] is him trying to fix another,
[886.64 → 888.12] maybe mistake that he made
[888.12 → 889.64] last time around with Node.
[889.90 → 891.28] And so I hope it works out for him.
[891.48 → 892.62] Yeah, yeah, I hope so too.
[892.88 → 894.12] It's always good to see
[894.12 → 895.74] attempts at sustainability
[895.74 → 896.90] around open source.
[897.02 → 898.36] And I really hope it works out.
[898.36 → 899.36] Thank you.
[916.64 → 920.04] This episode is brought to you
[920.04 → 921.14] by our friends at Source graph.
[921.66 → 923.00] Source graph is code search
[923.00 → 924.58] for every developer and team.
[924.92 → 925.62] And in this segment,
[925.66 → 926.56] I'm talking with Bing Liu,
[926.74 → 928.50] co-founder and CTO of Source graph.
[928.86 → 929.74] And he's sharing exactly
[929.74 → 930.66] how code search works
[930.66 → 931.32] and how it will work
[931.32 → 932.04] for you and your team.
[932.46 → 933.62] So Bing, I want you to share
[933.62 → 935.16] exactly what code search is
[935.16 → 936.66] and how teams can use it.
[936.94 → 938.32] So Adam, I think the best way
[938.32 → 939.16] to describe Source graph
[939.16 → 941.08] is that it's this single search
[941.08 → 942.38] and exploration tool
[942.38 → 943.22] that encompasses
[943.22 → 945.54] the entire universe of code
[945.54 → 946.76] that you might care about.
[946.96 → 948.68] And that includes all the code
[948.68 → 949.80] inside your organization,
[950.06 → 951.06] code written by other teams,
[951.14 → 952.14] as well as code
[952.14 → 952.84] that might be external
[952.84 → 953.66] to your organization.
[953.94 → 954.42] For example,
[954.56 → 955.30] open source dependencies
[955.30 → 956.08] that you're pulling in.
[956.08 → 957.48] So it's a single portal,
[957.60 → 958.66] a single search box
[958.66 → 960.08] that lets you type in
[960.08 → 961.12] a string literal
[961.12 → 962.72] or a regex pattern
[962.72 → 964.04] and instantly search
[964.04 → 965.38] across all that code
[965.38 → 967.78] and jump to the specific points
[967.78 → 968.38] in that code
[968.38 → 969.40] that you're interested
[969.40 → 970.30] in learning about.
[970.64 → 971.14] And then it becomes
[971.14 → 972.32] this interface that allows you
[972.32 → 973.88] to easily navigate
[973.88 → 976.00] and build up a mental model
[976.00 → 978.42] of how that part of code works.
[978.56 → 980.20] So whether it's trying
[980.20 → 980.84] to find a needle
[980.84 → 981.62] in a haystack
[981.62 → 982.44] that you're concerned about
[982.44 → 984.48] or trying to find examples
[984.48 → 985.42] of how to use
[985.42 → 987.52] a particular unfamiliar library
[987.52 → 988.52] or package,
[988.66 → 990.36] or maybe you just want to
[990.36 → 991.58] jump to a bunch of places
[991.58 → 993.02] in code that you can then link to
[993.02 → 994.02] and discuss with teammates.
[994.40 → 995.26] And this is all in the service
[995.26 → 997.24] of eventually getting back
[997.24 → 997.92] into your editor
[997.92 → 999.08] so that you have
[999.08 → 999.94] all the context,
[1000.10 → 1000.70] all the information
[1000.70 → 1001.56] that you need to know
[1001.56 → 1002.74] about the area of code
[1002.74 → 1003.40] that you're modifying
[1003.40 → 1004.32] and get back
[1004.32 → 1005.14] into that flow state
[1005.14 → 1006.14] where you're just coding
[1006.14 → 1006.88] at the speed of light
[1006.88 → 1007.46] and you feel like
[1007.46 → 1008.76] you're making rapid progress
[1008.76 → 1010.00] towards that bug fix
[1010.00 → 1010.78] or that feature
[1010.78 → 1011.58] that you're currently building.
[1012.10 → 1012.34] All right,
[1012.36 → 1012.92] if code search
[1012.92 → 1013.62] powered by Source graph
[1013.62 → 1014.32] sounds like something
[1014.32 → 1015.60] you and your team can use,
[1015.84 → 1017.52] head to info.sourcegraph.com
[1017.52 → 1018.42] slash changelog
[1018.42 → 1019.24] and click the button
[1019.24 → 1020.60] that says try Source graph now.
[1020.84 → 1021.72] You can install locally,
[1022.08 → 1022.92] deploy it to a server
[1022.92 → 1023.92] or to a cluster.
[1024.32 → 1025.10] They have a quick start guide
[1025.10 → 1026.08] that takes less than five minutes
[1026.08 → 1026.90] to install Source graph
[1026.90 → 1027.56] using Docker
[1027.56 → 1028.78] so it's too easy
[1028.78 → 1029.40] to give a try.
[1029.66 → 1029.98] Again,
[1030.12 → 1031.96] head to info.sourcegraph.com
[1031.96 → 1033.04] slash changelog.
[1052.04 → 1052.48] Okay,
[1052.66 → 1053.30] let's find out
[1053.30 → 1054.52] who is an April fool
[1054.52 → 1057.10] and who's going to April drool.
[1057.22 → 1057.68] I don't know.
[1057.86 → 1058.72] That didn't really work out.
[1058.72 → 1060.20] We're going to play
[1060.20 → 1061.92] a game called Headlines.
[1062.40 → 1063.48] I've gathered a bunch
[1063.48 → 1064.68] of real headlines
[1064.68 → 1066.86] along with the first paragraph
[1066.86 → 1067.72] from the story.
[1068.06 → 1069.34] I've also gathered
[1069.34 → 1069.92] and written
[1069.92 → 1071.96] some fake headlines
[1071.96 → 1074.04] along with the first paragraph
[1074.04 → 1075.10] to those stories.
[1075.74 → 1076.92] Here's how it's going to work.
[1077.24 → 1078.48] The headline will be presented
[1078.48 → 1080.22] at which point,
[1080.68 → 1081.02] Nick,
[1081.42 → 1082.58] you can guess
[1082.58 → 1083.56] true or false
[1083.56 → 1085.34] with two points on the line.
[1085.74 → 1086.32] So if you're wrong,
[1086.38 → 1087.02] I get the points.
[1087.12 → 1087.48] If you're right,
[1087.52 → 1088.12] you get the points.
[1088.94 → 1089.88] Or you can opt
[1089.88 → 1091.20] to hear the first paragraph
[1091.20 → 1092.68] before guessing
[1092.68 → 1093.86] with only one point
[1093.86 → 1094.40] on the line.
[1094.48 → 1095.40] So you can hear more,
[1095.86 → 1096.80] but you win more
[1096.80 → 1097.56] for getting it correct.
[1097.68 → 1098.34] Now at the end of the day,
[1098.40 → 1099.36] you got a 50-50 shot
[1099.36 → 1100.02] on all these, right?
[1100.86 → 1102.50] So you can always just guess
[1102.50 → 1103.92] and you're going to have to guess.
[1104.50 → 1105.04] And we'll see
[1105.04 → 1105.90] who comes up the victor.
[1106.06 → 1106.60] Sound like fun?
[1106.84 → 1107.52] It sounds like
[1107.52 → 1108.26] every other game
[1108.26 → 1109.12] that we try and play
[1109.12 → 1110.80] and my best shot
[1110.80 → 1111.56] is to not play.
[1113.52 → 1114.22] That's true.
[1114.22 → 1115.88] I do hope I win,
[1115.98 → 1116.48] as always.
[1116.88 → 1117.18] Mostly,
[1117.28 → 1118.10] I just hope that this is
[1118.10 → 1119.78] entertaining for everybody involved.
[1120.14 → 1120.64] Are you ready?
[1120.78 → 1121.16] I'm ready.
[1121.32 → 1121.86] Let's do it.
[1122.20 → 1122.52] All right.
[1122.58 → 1123.56] Here's the first headline.
[1124.24 → 1125.44] Apple adds two
[1125.44 → 1126.80] brand-new Siri voices
[1126.80 → 1127.96] and will no longer
[1127.96 → 1129.28] default to a female
[1129.28 → 1130.74] or male voice
[1130.74 → 1131.36] in iOS.
[1131.92 → 1132.32] Now,
[1132.42 → 1133.22] you can guess
[1133.22 → 1133.86] true or false
[1133.86 → 1134.60] with two points
[1134.60 → 1135.06] on the line
[1135.06 → 1136.16] or you can hear
[1136.16 → 1137.38] the first paragraph
[1137.38 → 1138.68] of the article.
[1138.68 → 1139.96] That is true.
[1141.98 → 1142.46] Congratulations.
[1142.88 → 1143.32] You got it.
[1143.42 → 1143.92] I've already listened
[1143.92 → 1145.12] to Accidental Tech Podcast
[1145.12 → 1145.88] today, so.
[1146.42 → 1146.86] Ah!
[1148.46 → 1149.10] All right.
[1149.18 → 1150.12] So you're winning
[1150.12 → 1150.72] two to zero.
[1151.66 → 1152.32] Not fair.
[1152.42 → 1153.34] You heard that headline.
[1153.88 → 1154.20] All right.
[1154.28 → 1154.72] Next one.
[1154.76 → 1155.10] Are you ready?
[1155.20 → 1155.54] I'm ready.
[1156.14 → 1157.24] Engine raises
[1157.24 → 1158.44] nearly $19 million
[1158.44 → 1159.48] to build
[1159.48 → 1160.62] Polka-dot-based
[1160.62 → 1162.32] blockchain for NFTs.
[1163.12 → 1164.34] That sounds like
[1164.34 → 1165.30] a real headline
[1165.30 → 1166.38] for sure.
[1167.08 → 1167.18] But
[1167.18 → 1169.04] Inge makes me think
[1169.04 → 1170.36] of the Jurassic Park
[1170.36 → 1170.70] company,
[1170.92 → 1171.54] so I'm going to say
[1171.54 → 1172.02] it's false.
[1172.52 → 1172.98] You're going to say
[1172.98 → 1173.48] it's false.
[1174.52 → 1175.00] Oh!
[1175.84 → 1176.20] Sorry,
[1176.32 → 1176.88] you are incorrect.
[1177.12 → 1178.12] It was true
[1178.12 → 1178.94] or it is true.
[1179.08 → 1179.60] No way.
[1180.04 → 1180.44] Yes.
[1180.76 → 1181.72] Blockchain development
[1181.72 → 1182.40] firm Inge
[1182.40 → 1183.70] has raised $18.9 million
[1183.70 → 1185.56] to build a Polka-dot-based
[1185.56 → 1186.52] blockchain network
[1186.52 → 1187.76] especially for
[1187.76 → 1188.66] non-fungible tokens.
[1188.82 → 1189.28] The network,
[1189.42 → 1190.18] dubbed Xfinity,
[1190.60 → 1191.34] will have its own
[1191.34 → 1192.28] token called
[1192.28 → 1193.18] Xfinity Token.
[1194.10 → 1194.78] The funding has been
[1194.78 → 1196.42] secured by selling
[1196.42 → 1197.54] EFT tokens.
[1198.10 → 1198.50] There you go.
[1198.70 → 1199.72] Those fools were too
[1199.72 → 1200.90] busy worrying about
[1200.90 → 1201.38] if they could.
[1201.46 → 1201.92] They didn't stop
[1201.92 → 1202.36] to think whether
[1202.36 → 1202.94] they should.
[1205.94 → 1206.38] Oh,
[1206.48 → 1207.20] very nice.
[1207.70 → 1208.38] Jurassic Park
[1208.38 → 1209.02] pull in there.
[1210.06 → 1210.36] All right,
[1210.42 → 1210.98] so with that,
[1211.10 → 1211.86] the score is tied.
[1211.96 → 1212.72] I'm back at it.
[1212.78 → 1213.92] It's 0-0.
[1214.14 → 1214.90] You've lost 2.
[1214.96 → 1215.42] Now remember,
[1215.62 → 1216.40] if you're not sure,
[1216.48 → 1216.96] you can listen
[1216.96 → 1217.94] to the first paragraph
[1217.94 → 1218.96] and give yourself
[1218.96 → 1219.72] a little more information
[1219.72 → 1220.60] or you can just keep
[1220.60 → 1221.64] gambling it all.
[1221.76 → 1222.34] Be ready for your next one.
[1222.34 → 1222.66] I'm ready.
[1222.66 → 1224.14] Google's Alphabet
[1224.14 → 1225.54] invests $50 million
[1225.54 → 1227.04] in soup startup.
[1227.56 → 1228.00] Okay.
[1231.36 → 1231.94] Go ahead,
[1232.00 → 1232.50] think out loud.
[1232.58 → 1232.92] Tell me your
[1232.92 → 1233.70] thought process here.
[1233.94 → 1234.16] Well,
[1234.24 → 1235.28] Alphabet's a real company.
[1236.76 → 1237.24] Yes?
[1237.38 → 1238.32] A soup startup.
[1239.46 → 1240.62] I think I do want
[1240.62 → 1241.54] to hear the paragraph.
[1241.54 → 1242.08] Do you want to hear more?
[1242.12 → 1242.24] Yeah.
[1242.78 → 1243.14] Okay.
[1243.60 → 1244.64] Here's the first paragraph
[1244.64 → 1245.08] of the article.
[1245.18 → 1246.22] If you need more indicators
[1246.22 → 1247.70] of easy access to capital
[1247.70 → 1248.72] in today's speculation
[1248.72 → 1249.42] craze market,
[1249.90 → 1250.56] look no further
[1250.56 → 1251.54] than a Silicon Valley
[1251.54 → 1252.46] startup called
[1252.46 → 1253.32] Souped Up,
[1253.90 → 1254.84] which announced today
[1254.84 → 1255.32] they've raised
[1255.32 → 1255.78] $100 million
[1255.78 → 1257.20] in a series B round
[1257.20 → 1257.82] that is led by
[1257.82 → 1258.34] none other than
[1258.34 → 1259.36] Google's parent company,
[1259.48 → 1259.74] Alphabet.
[1260.46 → 1261.22] Souped Up applies
[1261.22 → 1261.98] advanced machine
[1261.98 → 1262.66] learning techniques
[1262.66 → 1263.54] to bring low-cost
[1263.54 → 1264.14] canned goods
[1264.14 → 1265.52] to developing nations
[1265.52 → 1266.68] and indigenous peoples.
[1267.00 → 1267.94] That's a mouthful.
[1268.38 → 1268.64] Okay.
[1269.30 → 1270.80] It seems more plausible,
[1271.38 → 1274.06] but Igor in the chat
[1274.06 → 1275.04] says Alphabet Soup.
[1275.44 → 1276.16] I'm going to say
[1276.16 → 1276.84] it's not real.
[1277.24 → 1277.60] You're going to say
[1277.60 → 1278.66] it's not correct.
[1278.76 → 1279.44] So it's a false,
[1279.54 → 1280.16] it's a headline.
[1280.32 → 1280.46] Yeah.
[1281.56 → 1282.04] Whew.
[1282.32 → 1283.14] You are correct.
[1283.32 → 1284.26] I made that one up.
[1284.58 → 1285.26] But I had you going,
[1285.36 → 1285.62] didn't I?
[1285.86 → 1286.16] Nice.
[1287.08 → 1287.58] For sure.
[1287.64 → 1288.18] I was going to ask
[1288.18 → 1289.22] if you used GPT-3
[1289.22 → 1290.24] to make that.
[1290.62 → 1292.02] To generate these.
[1292.72 → 1293.70] Well, that would require
[1293.70 → 1294.50] way more forethought
[1294.50 → 1295.44] than I put into this.
[1295.84 → 1296.62] And skill,
[1296.90 → 1297.98] which I hold very little of.
[1298.42 → 1298.74] All right.
[1298.76 → 1299.28] You're now winning
[1299.28 → 1299.82] one to nothing.
[1299.92 → 1300.64] You got one point
[1300.64 → 1301.70] for getting that one correct.
[1301.88 → 1302.34] And yes,
[1302.48 → 1304.08] the Alphabet Soup
[1304.08 → 1306.02] really was the funny bit,
[1306.28 → 1306.78] I thought.
[1306.98 → 1307.26] Okay.
[1308.02 → 1308.64] Next headline.
[1309.12 → 1309.92] Carbon labels
[1309.92 → 1310.84] are coming to your
[1310.84 → 1311.56] shampoo bottle.
[1312.24 → 1313.16] Carbon labels
[1313.16 → 1313.96] are coming to your
[1313.96 → 1314.66] shampoo bottle.
[1315.30 → 1316.08] That's correct.
[1316.34 → 1317.38] I want to hear the paragraph
[1317.38 → 1318.24] on this one too.
[1318.74 → 1319.02] Okay.
[1319.78 → 1321.08] Shoppers have been able
[1321.08 → 1322.36] to use nutrition labels
[1322.36 → 1323.88] to choose low-salt meals
[1323.88 → 1325.50] or reduced-sugar cereal.
[1325.88 → 1326.76] Now some companies
[1326.76 → 1327.50] want to use labels
[1327.50 → 1328.26] to help them pick
[1328.26 → 1329.46] everything from shampoo
[1329.46 → 1330.04] to milk
[1330.04 → 1331.36] based on products'
[1331.52 → 1332.18] carbon emissions.
[1332.18 → 1334.22] I hope this is true.
[1334.64 → 1335.70] I'm going to go with that.
[1335.84 → 1336.82] There's no opium here.
[1336.90 → 1337.66] Is it true or false?
[1337.74 → 1338.18] It's true.
[1339.30 → 1340.02] All right.
[1340.10 → 1340.84] You got it.
[1340.92 → 1341.58] All right.
[1341.68 → 1342.18] You're now winning
[1342.18 → 1342.72] two to zero.
[1343.36 → 1344.26] These next few
[1344.26 → 1345.72] are all Florida Man headlines.
[1346.18 → 1346.82] Are you familiar
[1346.82 → 1347.46] with Florida Man?
[1347.50 → 1347.80] Yes.
[1348.64 → 1349.08] Okay.
[1350.48 → 1351.38] You're about to be
[1351.38 → 1352.04] even more familiar
[1352.04 → 1352.72] with Florida Man.
[1352.92 → 1353.72] Why don't you explain
[1353.72 → 1354.36] Florida Man
[1354.36 → 1355.70] just in case any of our listeners
[1355.70 → 1357.16] aren't familiar?
[1357.40 → 1357.74] Okay.
[1358.22 → 1359.04] Well, why don't you go ahead
[1359.04 → 1359.88] and explain Florida Man?
[1359.88 → 1361.48] What do you think of it?
[1362.28 → 1363.16] Anytime you see
[1363.16 → 1364.32] some ridiculous article,
[1364.58 → 1365.26] it usually starts
[1365.26 → 1366.48] with Florida Man.
[1366.62 → 1367.32] Like Florida Man
[1367.32 → 1368.46] gets head stuck
[1368.46 → 1368.94] in alligator
[1368.94 → 1369.98] or something like that.
[1370.46 → 1370.66] Yeah.
[1370.96 → 1371.84] So there's this
[1371.84 → 1373.60] canonical Florida Man
[1373.60 → 1374.92] that is always
[1374.92 → 1375.72] getting into hi jinks.
[1376.02 → 1376.42] That's right.
[1376.66 → 1377.62] These are three of those.
[1378.02 → 1379.34] The first one is
[1379.34 → 1380.16] Florida Man
[1380.16 → 1380.78] gets beat up
[1380.78 → 1381.60] by Santa Claus.
[1383.10 → 1383.58] True.
[1384.68 → 1385.16] True?
[1385.34 → 1385.56] Yep.
[1386.34 → 1387.04] I'm sorry.
[1387.10 → 1387.64] That's incorrect.
[1388.14 → 1388.74] Turns out it was
[1388.74 → 1389.26] the Easter Bunny.
[1389.88 → 1393.72] Oh, and with that,
[1394.02 → 1395.56] it's now zero, zero again.
[1395.64 → 1396.32] You're back at zero.
[1397.06 → 1398.26] The full story
[1398.26 → 1399.04] is a Florida Man
[1399.04 → 1399.92] received a beat down
[1399.92 → 1400.70] from the Easter Bunny
[1400.70 → 1402.00] and the whole thing
[1402.00 → 1402.74] was caught on video.
[1402.96 → 1403.48] It all started
[1403.48 → 1403.94] when the man
[1403.94 → 1404.74] bumped into a woman
[1404.74 → 1405.82] and words were exchanged.
[1406.54 → 1407.36] The Easter Bunny
[1407.36 → 1408.24] hopped into action
[1408.24 → 1409.38] and proceeded to demonstrate
[1409.38 → 1410.08] what happens
[1410.08 → 1410.80] when you're...
[1410.80 → 1411.28] Oh, sorry.
[1411.74 → 1412.64] I rewrote it.
[1413.66 → 1414.52] I was trying to read
[1414.52 → 1414.90] the original.
[1415.04 → 1415.66] I'm reading mine.
[1416.18 → 1416.76] I changed it to
[1416.76 → 1417.88] Santa leaped into action
[1417.88 → 1418.92] and proceeded to demonstrate
[1418.92 → 1419.40] what happens
[1419.40 → 1419.96] when you're naughty
[1419.96 → 1420.68] or not nice.
[1421.16 → 1422.38] The fight was eventually
[1422.38 → 1424.10] broken up by Orlando police
[1424.10 → 1424.86] and a bystander.
[1424.96 → 1425.34] So, yeah,
[1425.42 → 1426.32] everything there is true
[1426.32 → 1426.90] except for it was
[1426.90 → 1427.34] the Easter Bunny
[1427.34 → 1428.20] and not Santa Claus
[1428.20 → 1430.14] and I changed the puns.
[1430.20 → 1431.02] I think it said
[1431.02 → 1431.68] the Easter Bunny
[1431.68 → 1432.84] showed what happens
[1432.84 → 1433.84] when he pulls out
[1433.84 → 1434.84] his fists of fury
[1434.84 → 1435.56] or something stupid
[1435.56 → 1435.96] like that.
[1436.06 → 1436.42] I don't know.
[1436.62 → 1436.88] Anyway,
[1436.94 → 1437.68] that one is false.
[1437.68 → 1438.74] I should get a half a point
[1438.74 → 1439.90] because I refuse to believe
[1439.90 → 1440.92] that if you went back
[1440.92 → 1441.42] far enough,
[1441.52 → 1442.60] there's not some article
[1442.60 → 1443.50] about a Florida man
[1443.50 → 1444.20] fighting Santa.
[1444.20 → 1445.80] Well,
[1446.94 → 1447.92] if you can find the link
[1447.92 → 1448.62] behind the show,
[1448.74 → 1449.86] I'll edit it back in.
[1450.36 → 1450.68] All right,
[1450.72 → 1451.32] next one.
[1451.72 → 1452.36] Florida man
[1452.36 → 1454.06] with state tattooed
[1454.06 → 1454.72] on head
[1454.72 → 1455.58] calls 911
[1455.58 → 1456.78] for a ride home.
[1457.32 → 1457.78] Florida man
[1457.78 → 1459.16] with state tattooed,
[1459.16 → 1460.22] like the word state
[1460.22 → 1461.70] or the state of Florida?
[1462.34 → 1462.88] I can't provide
[1462.88 → 1463.46] any more context
[1463.46 → 1464.38] unless you want the paragraph.
[1464.60 → 1465.14] Do you want the paragraph?
[1465.30 → 1465.48] Yeah,
[1465.58 → 1466.26] I'll do the paragraph.
[1466.68 → 1467.02] All right.
[1467.38 → 1468.22] A Florida man
[1468.22 → 1469.40] with his favourite state
[1469.40 → 1470.68] tattooed on his forehead
[1470.68 → 1471.64] was arrested
[1471.64 → 1472.58] after calling 911
[1472.58 → 1473.62] multiple times
[1473.62 → 1474.70] requesting a ride home.
[1475.10 → 1476.26] A deputy who found
[1476.26 → 1476.88] the Florida man
[1476.88 → 1478.18] offered to call him a cab
[1478.18 → 1478.96] but he said he didn't
[1478.96 → 1479.90] have money for one.
[1480.14 → 1481.40] He then began to walk
[1481.40 → 1482.64] in the direction of his home
[1482.64 → 1483.82] then called 911
[1483.82 → 1484.66] a second time
[1484.66 → 1486.34] again requesting a ride.
[1486.56 → 1487.38] The same officer
[1487.38 → 1488.14] caught up with him
[1488.14 → 1489.00] and arrested him
[1489.00 → 1490.78] while he was on the line.
[1491.02 → 1491.98] That sounds real.
[1493.32 → 1494.34] That one's real.
[1494.78 → 1495.52] One point.
[1495.88 → 1496.60] We've all been there,
[1496.66 → 1497.16] Florida man.
[1497.66 → 1498.80] We've all been there.
[1498.80 → 1500.40] Have you ever had
[1500.40 → 1501.10] the state of Nebraska
[1501.10 → 1502.08] tattooed on your forehead?
[1502.86 → 1503.14] All right,
[1503.18 → 1503.72] last one.
[1503.82 → 1504.58] Florida man
[1504.58 → 1505.74] breaks into home
[1505.74 → 1507.48] sucks on sleeping man's toes.
[1511.98 → 1513.00] Oh gosh.
[1513.64 → 1514.56] What do you think?
[1516.66 → 1518.22] I think that it's false
[1518.22 → 1519.38] but I want to hear
[1519.38 → 1519.86] the paragraph
[1519.86 → 1520.78] just so I can
[1520.78 → 1522.02] hear that
[1522.02 → 1523.62] and just assume
[1523.62 → 1524.34] that you wrote that
[1524.34 → 1525.30] and I just want to hear
[1525.30 → 1526.32] what you would write
[1526.32 → 1526.84] about there.
[1527.28 → 1528.36] The incident occurred
[1528.36 → 1529.18] on Christmas Eve.
[1529.34 → 1530.16] According to the resident
[1530.16 → 1531.20] he awoke to find
[1531.20 → 1531.88] the Florida man
[1531.88 → 1532.82] at his feet
[1532.82 → 1533.74] who then proclaimed
[1533.74 → 1534.32] that he broke
[1534.32 → 1534.92] into the home
[1534.92 → 1536.82] quote to suck toes.
[1537.96 → 1538.94] He then attempted
[1538.94 → 1539.78] to fondle the man
[1539.78 → 1540.90] according to the police report.
[1541.00 → 1541.68] After the two got
[1541.68 → 1542.34] into a fight
[1542.34 → 1543.30] the Florida man
[1543.30 → 1544.02] smashed a window
[1544.02 → 1545.12] and the victim's windshield
[1545.12 → 1546.36] before making an escape.
[1546.46 → 1547.60] No arrests have been made.
[1548.40 → 1549.40] I think it's false.
[1549.84 → 1550.54] I think it's a lie.
[1551.18 → 1552.28] And you are false.
[1552.48 → 1553.68] That is 100% true
[1553.68 → 1554.16] my friend.
[1554.16 → 1557.24] And with that
[1557.24 → 1558.06] you're back at zero.
[1558.72 → 1559.66] This is going very well.
[1559.74 → 1560.26] You get one right
[1560.26 → 1560.84] you get one wrong.
[1560.98 → 1561.34] Get one right
[1561.34 → 1561.78] get one wrong.
[1562.04 → 1562.84] I wish that wasn't
[1562.84 → 1563.48] true as well.
[1565.62 → 1567.06] That is terrible.
[1567.28 → 1567.44] Okay.
[1567.86 → 1568.78] The next headline.
[1569.48 → 1570.68] Rapper Lava Flag
[1570.68 → 1571.50] in hot water
[1571.50 → 1572.76] after exposing himself
[1572.76 → 1573.58] during cameo.
[1575.04 → 1576.32] I have seriously
[1576.32 → 1577.04] looked at getting
[1577.04 → 1577.50] a cameo
[1577.50 → 1578.36] from Lava Flag
[1578.36 → 1580.04] so I hope
[1580.04 → 1580.74] that's not true
[1580.74 → 1581.88] but I'm going to say
[1581.88 → 1582.92] that it is true.
[1582.92 → 1584.34] You're saying it's true.
[1585.10 → 1586.44] I made that one up.
[1587.04 → 1588.42] It was somebody else right?
[1588.74 → 1589.48] No I just completely
[1589.48 → 1589.92] made it up
[1589.92 → 1590.98] in a full cloth.
[1591.82 → 1592.48] You want to hear
[1592.48 → 1593.52] the paragraph I wrote for it?
[1593.52 → 1593.86] I do.
[1594.14 → 1594.44] Okay.
[1594.62 → 1595.58] I'll let you know
[1595.58 → 1596.72] that you have negative one now
[1596.72 → 1597.56] so I'm officially winning.
[1597.86 → 1599.40] William Jonathan Drayton Jr
[1599.40 → 1600.12] widely known
[1600.12 → 1600.96] by his stage name
[1600.96 → 1601.56] Lava Flag
[1601.56 → 1602.90] may face charges
[1602.90 → 1603.54] for a video
[1603.54 → 1604.84] he produced on Cameo
[1604.84 → 1606.04] a service where people
[1606.04 → 1606.68] hire celebrities
[1606.68 → 1607.62] to create brief videos
[1607.62 → 1608.10] and share them
[1608.10 → 1608.62] with their friends.
[1609.08 → 1609.78] The video in question
[1609.78 → 1610.58] was for a woman's
[1610.58 → 1611.18] 40th birthday
[1611.18 → 1612.28] and according to Drayton
[1612.28 → 1613.68] the customer requested
[1613.68 → 1615.42] quote something special
[1615.42 → 1616.58] for his biggest fan.
[1617.02 → 1618.04] Pretty believable I guess.
[1619.06 → 1619.28] Yeah.
[1621.68 → 1622.64] I thought that one
[1622.64 → 1623.74] might get over on you
[1623.74 → 1624.10] although
[1624.10 → 1625.66] I think that would make
[1625.66 → 1626.58] some sort of bigger news
[1626.58 → 1627.08] like you probably
[1627.08 → 1627.86] would have heard about it
[1627.86 → 1628.22] you know?
[1628.30 → 1628.38] Yeah.
[1628.46 → 1628.76] I don't know
[1628.76 → 1629.20] maybe not
[1629.20 → 1629.90] there's lots of
[1629.90 → 1630.62] ridiculous things
[1630.62 → 1630.96] on the news.
[1631.48 → 1631.88] Okay.
[1632.06 → 1633.00] You now have negative one
[1633.00 → 1633.64] you're digging out
[1633.64 → 1634.54] of the red
[1634.54 → 1635.02] are you ready?
[1635.16 → 1635.46] I'm ready.
[1635.72 → 1636.90] There's one, two, three
[1636.90 → 1637.86] there's four more.
[1638.48 → 1639.08] Next headline
[1639.08 → 1640.10] Internet's
[1640.10 → 1641.30] Hide the Pain Herald
[1641.30 → 1642.54] accidentally used
[1642.54 → 1643.24] by Swedish
[1643.24 → 1644.98] COVID-19 vaccine website.
[1645.50 → 1645.82] Do you know
[1645.82 → 1646.44] Hide the Pain Herald?
[1646.56 → 1646.88] I do.
[1647.18 → 1647.64] You know that guy?
[1647.66 → 1647.84] Yeah.
[1647.84 → 1648.02] Okay.
[1648.26 → 1649.08] It's the old guy
[1649.08 → 1649.94] holding a mug right?
[1650.18 → 1651.26] Yeah and he's smiling
[1651.26 → 1652.82] but you can tell
[1652.82 → 1653.44] on his face
[1653.44 → 1654.10] that he's actually
[1654.10 → 1655.58] like seriously
[1655.58 → 1656.38] in pain
[1656.38 → 1657.78] or hates his life
[1657.78 → 1658.30] or whatever
[1658.30 → 1659.06] so people use it
[1659.06 → 1659.46] all the time
[1659.46 → 1660.02] when you're like
[1660.02 → 1661.42] acting like you're okay.
[1661.76 → 1662.58] I actually watched
[1662.58 → 1664.12] a Where Are They Now
[1664.12 → 1665.04] with that guy
[1665.04 → 1665.88] on YouTube.
[1666.00 → 1666.36] Oh really?
[1666.54 → 1666.74] Yeah.
[1667.36 → 1668.14] Where is he now?
[1668.48 → 1669.78] He's enjoying it.
[1669.88 → 1670.50] He gets noticed
[1670.50 → 1671.04] on the street
[1671.04 → 1672.40] and people want
[1672.40 → 1672.86] to take pictures
[1672.86 → 1673.36] with him.
[1673.88 → 1674.54] Yeah because wasn't
[1674.54 → 1675.02] he just like
[1675.02 → 1676.04] it was like stock photo
[1676.04 → 1676.52] wasn't it?
[1676.58 → 1676.70] Yeah.
[1677.02 → 1677.22] Yeah.
[1677.22 → 1677.74] He's been doing it
[1677.74 → 1678.18] for years
[1678.18 → 1679.42] and never had
[1679.42 → 1680.18] anything come of it
[1680.18 → 1680.54] and then
[1680.54 → 1681.82] someone just noticed
[1681.82 → 1683.18] like this guy's eyes
[1683.18 → 1684.14] tell a different story
[1684.14 → 1684.82] than his lips
[1684.82 → 1685.16] you know
[1685.16 → 1685.90] his smile.
[1686.40 → 1687.02] That's cool
[1687.02 → 1687.62] he's living up
[1687.62 → 1688.72] he's an internet celebrity now.
[1689.54 → 1689.94] Internet's
[1689.94 → 1691.08] Hide the Pain Herald
[1691.08 → 1692.06] accidentally used
[1692.06 → 1692.70] by Swedish
[1692.70 → 1694.38] COVID-19 vaccine website.
[1694.72 → 1695.44] You're at negative one
[1695.44 → 1696.08] so you can guess
[1696.08 → 1697.10] you can get the paragraph.
[1697.62 → 1698.88] If it's stock photography
[1698.88 → 1699.72] how can it be
[1699.72 → 1700.82] accidentally used?
[1701.18 → 1701.54] Hmm.
[1702.10 → 1702.52] You have like
[1702.52 → 1703.56] a private eye over there.
[1704.18 → 1705.24] I'm going to say it's false.
[1705.48 → 1706.54] You're going to say it's false
[1706.54 → 1708.52] and you fail once again
[1708.52 → 1709.18] that one's true.
[1709.78 → 1710.38] So accidentally
[1710.38 → 1711.48] might be a
[1711.48 → 1713.04] editorial word
[1713.04 → 1713.86] used by the
[1713.86 → 1715.22] whoever is reporting this
[1715.22 → 1716.14] maybe it was on purpose
[1716.14 → 1716.64] you know
[1716.64 → 1718.22] but I think
[1718.22 → 1718.78] if you're using
[1718.78 → 1719.38] stock photo
[1719.38 → 1719.92] I think the point
[1719.92 → 1720.40] of like a
[1720.40 → 1720.90] you know
[1720.90 → 1721.42] these websites
[1721.42 → 1721.68] is like
[1721.68 → 1722.34] it's a real person
[1722.34 → 1722.84] who's happy
[1722.84 → 1723.30] because they got
[1723.30 → 1723.86] their vaccine
[1723.86 → 1724.30] or something
[1724.30 → 1724.90] but it's like
[1724.90 → 1725.62] you know what I'm saying?
[1725.70 → 1726.38] But then he's hiding the pain.
[1726.38 → 1727.22] So it probably was accidental
[1727.22 → 1728.16] like yeah
[1728.16 → 1728.66] exactly.
[1729.20 → 1730.18] Okay I get it.
[1730.94 → 1731.26] Yeah.
[1731.58 → 1732.54] He's hiding the pain.
[1734.60 → 1735.80] And according to
[1735.80 → 1736.82] the health authority
[1736.82 → 1737.74] in Sweden
[1737.74 → 1739.02] officials said
[1739.02 → 1739.78] on Tuesday evening
[1739.78 → 1740.56] that the image
[1740.56 → 1741.52] has now been removed
[1741.52 → 1742.26] so it definitely
[1742.26 → 1742.82] was an accident
[1742.82 → 1743.68] because they got called out
[1743.68 → 1744.10] and they're like
[1744.10 → 1745.00] okay we're taking that one down.
[1745.36 → 1745.64] You would think
[1745.64 → 1746.32] that that would get
[1746.32 → 1747.18] the younger folks
[1747.18 → 1747.82] in to
[1747.82 → 1749.38] to actually get the vaccine.
[1749.80 → 1750.04] Yeah.
[1750.50 → 1751.50] Like if Harold can do it
[1751.50 → 1751.90] you know
[1751.90 → 1752.72] I should be okay.
[1753.34 → 1753.98] Okay the next one
[1753.98 → 1755.06] Pringles to launch
[1755.06 → 1756.62] new lip balm product line.
[1756.86 → 1757.24] Oh man.
[1759.34 → 1760.16] I want to hear those.
[1760.18 → 1761.14] You're at negative three.
[1761.30 → 1761.60] You want to hear it?
[1761.60 → 1761.70] Yeah.
[1762.20 → 1763.08] Kellogg company
[1763.08 → 1764.18] announced a new set
[1764.18 → 1764.66] of products
[1764.66 → 1765.46] from its iconic
[1765.46 → 1766.32] Pringles brand.
[1766.80 → 1767.42] The company said
[1767.42 → 1767.86] it would release
[1767.86 → 1768.88] a delicious lip balm
[1768.88 → 1769.42] with flavours
[1769.42 → 1770.64] such as salt and vinegar
[1770.64 → 1772.12] and sour cream
[1772.12 → 1772.66] and onion.
[1774.06 → 1775.12] That can't be real.
[1776.94 → 1777.84] But you're not sure
[1777.84 → 1778.22] are you?
[1778.30 → 1778.92] I'm not.
[1779.06 → 1779.52] It's just like
[1779.52 → 1780.10] doing the internet
[1780.10 → 1780.84] on April Fool's Day.
[1780.90 → 1781.38] You never know.
[1781.50 → 1782.34] Is this real or not?
[1782.86 → 1784.46] I'm going to say
[1784.46 → 1786.18] you know what?
[1786.76 → 1787.58] I'm going to say it's real.
[1787.84 → 1788.18] You're going to say
[1788.18 → 1788.58] it's real?
[1788.86 → 1789.12] Yeah.
[1790.02 → 1791.06] I made it up.
[1791.50 → 1791.86] No.
[1793.44 → 1794.60] That was after one
[1794.60 → 1795.80] so you got negative four there
[1795.80 → 1797.40] or total negative four.
[1798.24 → 1799.24] I'm feeling pretty happy
[1799.24 → 1799.78] at this point.
[1799.94 → 1800.52] I feel like I got
[1800.52 → 1801.94] I got you just
[1801.94 → 1803.12] never knowing what's true.
[1803.54 → 1803.86] All right.
[1803.92 → 1804.26] Two more.
[1805.26 → 1806.70] 330 million Americans
[1806.70 → 1807.78] sue Cardi B
[1807.78 → 1809.34] for psychological damage.
[1809.82 → 1810.24] It's true.
[1810.24 → 1812.26] Nope.
[1813.26 → 1813.90] This one
[1813.90 → 1815.96] this one came off
[1815.96 → 1816.40] the onion
[1816.40 → 1816.96] or one of those
[1816.96 → 1817.66] satire sites.
[1817.74 → 1818.56] I did not write that one.
[1819.22 → 1820.00] But it's believable.
[1820.40 → 1820.80] Okay.
[1821.50 → 1823.04] You're now at negative six.
[1823.14 → 1824.22] You're failing miserably.
[1824.78 → 1825.98] And you would have been
[1825.98 → 1827.08] better off not having played
[1827.08 → 1827.88] as you said at the top.
[1829.28 → 1830.30] Last one.
[1830.92 → 1832.04] U.S. man returns
[1832.04 → 1833.30] from Swift shopping trip
[1833.30 → 1835.00] to find 15,000 bees
[1835.00 → 1835.72] in his car.
[1835.72 → 1838.96] I feel like I saw this one
[1838.96 → 1840.10] so I'm going to say it's true.
[1841.04 → 1841.80] All right.
[1841.88 → 1842.56] Yeah, that's right.
[1842.74 → 1843.68] You got the last one right
[1843.68 → 1845.52] which puts you at negative four.
[1845.82 → 1846.96] So still a big loser.
[1847.74 → 1848.74] But it feels nice
[1848.74 → 1849.70] to get the last one correct.
[1849.84 → 1850.66] Yeah, apparently this guy
[1850.66 → 1851.24] went shopping
[1851.24 → 1852.52] in New Mexico.
[1853.32 → 1854.02] Came back.
[1854.24 → 1855.86] There was 15,000 honeybees
[1855.86 → 1857.60] who had gotten in
[1857.60 → 1858.58] through an open window
[1858.58 → 1859.66] while he spent 10 minutes
[1859.66 → 1860.48] buying groceries.
[1860.48 → 1862.20] Astonishingly,
[1862.24 → 1863.50] the man did not notice
[1863.50 → 1864.52] the sudden presence
[1864.52 → 1865.60] of a giant swarm
[1865.60 → 1866.50] of buzzing insects
[1866.50 → 1868.00] on his vehicle's backseat
[1868.00 → 1869.30] until he was driving away.
[1870.34 → 1870.66] Yeah.
[1871.14 → 1872.58] So he must have been distracted
[1872.58 → 1873.88] because how do you miss it, right?
[1873.92 → 1874.18] Yeah.
[1874.38 → 1874.94] And I just wonder
[1874.94 → 1875.64] what they were doing.
[1876.18 → 1876.80] Why would they
[1876.80 → 1877.86] want to be in his car?
[1878.40 → 1878.88] I don't know.
[1878.96 → 1879.52] Maybe there was something
[1879.52 → 1880.18] sweet in there.
[1880.34 → 1881.40] You know, bees swarm
[1881.40 → 1882.92] and sometimes they'll leave
[1882.92 → 1884.06] their hive
[1884.06 → 1885.32] and swarm somewhere else
[1885.32 → 1886.96] around specific
[1886.96 → 1888.40] sources of food
[1888.40 → 1888.80] or something.
[1889.40 → 1889.88] I don't know.
[1889.88 → 1891.16] bees me.
[1892.64 → 1893.44] Oh, gosh.
[1894.12 → 1894.40] All right.
[1894.42 → 1894.94] With that,
[1895.04 → 1896.22] we finish Head Lies.
[1896.50 → 1897.06] I would say
[1897.06 → 1897.92] it was a big victory
[1897.92 → 1898.76] for me at least.
[1899.16 → 1900.16] If you enjoyed
[1900.16 → 1900.90] this segment,
[1901.04 → 1902.04] please let us know
[1902.04 → 1903.08] and we will do it again.
[1903.16 → 1903.44] Otherwise,
[1903.60 → 1904.34] we'll banish it
[1904.34 → 1905.68] to the farthest recesses
[1905.68 → 1906.42] of the internet,
[1906.60 → 1907.62] never to be seen again
[1907.62 → 1910.18] until April Fool's Day, 2022.
[1916.76 → 1918.30] This episode is brought to you
[1918.30 → 1919.34] by our friends at O'Reilly.
[1919.34 → 1920.48] Many of you know O'Reilly
[1920.48 → 1921.62] for their animal tech books
[1921.62 → 1922.34] and their conferences,
[1922.68 → 1923.80] but you may not know
[1923.80 → 1924.68] they have an online
[1924.68 → 1925.86] learning platform as well.
[1926.22 → 1927.84] The platform has all their books,
[1928.06 → 1928.86] all their videos,
[1929.12 → 1930.66] and all their conference talks.
[1931.02 → 1932.24] Plus, you can learn by doing
[1932.24 → 1934.04] with live online training courses
[1934.04 → 1935.20] and virtual conferences,
[1935.70 → 1937.12] certification practice exams,
[1937.46 → 1939.06] and interactive sandboxes
[1939.06 → 1939.86] and scenarios
[1939.86 → 1940.72] to practice coding
[1940.72 → 1941.78] alongside what you're learning.
[1941.78 → 1943.00] They cover a ton
[1943.00 → 1943.96] of technology topics,
[1944.08 → 1944.82] machine learning,
[1945.16 → 1945.52] AI,
[1946.02 → 1946.80] programming languages,
[1947.34 → 1947.62] DevOps,
[1948.14 → 1948.94] data science,
[1949.22 → 1949.62] cloud,
[1949.96 → 1950.44] containers,
[1951.04 → 1951.48] security,
[1951.82 → 1953.32] and even soft skills
[1953.32 → 1954.30] like business management
[1954.30 → 1955.72] and presentation skills.
[1955.86 → 1956.38] You name it,
[1956.52 → 1957.64] it is all in there.
[1957.94 → 1959.08] If you need to keep your team
[1959.08 → 1960.34] or yourself up to speed
[1960.34 → 1961.20] on their tech skills,
[1961.30 → 1961.70] then check out
[1961.70 → 1963.12] O'Reilly's online learning platform.
[1963.64 → 1964.04] Learn more
[1964.04 → 1965.30] and keep your team skills sharp
[1965.30 → 1966.26] at O'Reilly.com
[1966.26 → 1967.22] slash changelog.
[1967.34 → 1967.80] Again,
[1967.94 → 1968.74] O'Reilly.com
[1968.74 → 1969.60] slash changelog.
[1980.06 → 1982.62] All right,
[1982.66 → 1983.36] we're going to finish up
[1983.36 → 1984.72] today's show
[1984.72 → 1986.56] with some shout-outs.
[1987.10 → 1988.20] And I'm going to go first,
[1988.32 → 1989.28] I'm going to give a shout-out
[1989.28 → 1990.00] to a tool
[1990.00 → 1990.82] and some people
[1990.82 → 1992.36] that we're using right now
[1992.36 → 1993.68] that I've been appreciating
[1993.68 → 1995.04] quite a bit lately.
[1995.04 → 1996.18] Hacked,
[1996.76 → 1997.36] which you'll find
[1997.36 → 1998.90] at hackmd.io.
[1999.58 → 2002.56] It is an online collaborative
[2002.56 → 2005.66] markdown based writing tool.
[2006.12 → 2008.90] So think about Google Docs
[2008.90 → 2011.06] and how crappy the UI
[2011.06 → 2012.04] and everything
[2012.04 → 2013.20] and writing in there
[2013.20 → 2014.50] and copying and pasting out of it.
[2014.56 → 2015.30] Think about all that
[2015.30 → 2015.92] and just,
[2016.10 → 2017.04] don't you ever have Google Docs
[2017.04 → 2017.22] where you're like,
[2017.26 → 2018.36] I just want to write in Markdown,
[2018.72 → 2019.00] you know?
[2019.70 → 2020.94] And there's Dropbox Paper,
[2021.14 → 2021.90] which is better
[2021.90 → 2022.52] because you can kind of
[2022.52 → 2023.38] write in Markdown
[2023.38 → 2024.68] whether it formats things weird
[2024.68 → 2026.04] and then you can't copy it out
[2026.04 → 2026.90] exactly the same
[2026.90 → 2028.50] and they have a lot of
[2028.50 → 2030.06] unfurling they do
[2030.06 → 2030.84] and I'm just like,
[2030.94 → 2031.96] please stop unfurling.
[2032.06 → 2032.80] I just want the link
[2032.80 → 2033.88] to just sit there anyway.
[2034.50 → 2035.72] Not a huge fan.
[2035.76 → 2036.36] Although I would take
[2036.36 → 2037.40] Paper over Docs
[2037.40 → 2039.68] and now I would take Hacked
[2039.68 → 2040.72] because it's basically
[2040.72 → 2042.80] exactly what I would want.
[2042.90 → 2044.80] It is a Markdown editor
[2044.80 → 2046.34] and it even has that cool
[2046.34 → 2046.90] split view
[2046.90 → 2047.84] where the left-hand side
[2047.84 → 2048.46] is what you write
[2048.46 → 2049.74] and the right-hand side
[2049.74 → 2050.50] is the rendered version.
[2050.50 → 2051.36] You can toggle that
[2051.36 → 2051.84] off and on.
[2051.92 → 2052.22] So you can go like
[2052.22 → 2053.14] full writing mode,
[2053.28 → 2054.14] full viewing mode,
[2054.26 → 2055.90] or split screen mode.
[2056.06 → 2057.26] But it has all the nifty
[2057.26 → 2059.18] collaboration tools,
[2059.42 → 2059.72] you know,
[2060.02 → 2060.76] that you'd expect
[2060.76 → 2062.16] from like a Google Docs
[2062.16 → 2063.18] or a Dropbox Paper
[2063.18 → 2065.04] just by sharing the URL,
[2065.22 → 2066.00] which is my favourite thing.
[2066.06 → 2066.20] Like,
[2066.26 → 2067.00] give me a URL,
[2067.36 → 2067.54] right?
[2067.60 → 2069.26] Make it an obfuscated one
[2069.26 → 2070.38] so it can't be easily found
[2070.38 → 2071.82] and just pass it around.
[2071.88 → 2071.96] Now,
[2071.96 → 2072.60] they do have settings
[2072.60 → 2073.40] you can set up like
[2073.40 → 2074.22] who can read,
[2074.26 → 2074.74] who can write.
[2074.86 → 2075.86] It gets more complicated,
[2075.86 → 2077.42] but like the base use case
[2077.42 → 2079.18] is super simple
[2079.18 → 2080.56] and that's what I love about it.
[2080.68 → 2081.82] I love web tools
[2081.82 → 2082.46] that allow me
[2082.46 → 2083.94] just to share quickly
[2083.94 → 2085.64] and get people involved.
[2085.72 → 2086.26] We've been using it
[2086.26 → 2089.52] for JS Party documentation
[2089.52 → 2090.60] or not documentation,
[2090.74 → 2091.50] like scratch sheets
[2091.50 → 2092.24] where we're sharing
[2092.24 → 2093.70] to do the show for a while.
[2093.78 → 2094.24] I've been doing it
[2094.24 → 2095.64] for a lot of my blog writing.
[2096.30 → 2096.82] I've been doing it
[2096.82 → 2097.68] for pretty much everything
[2097.68 → 2098.32] for the last,
[2098.56 → 2098.94] I don't know,
[2099.02 → 2099.74] six months or so.
[2100.40 → 2101.14] And today,
[2101.26 → 2102.26] because of April Fool's
[2102.26 → 2102.88] it turns out,
[2103.08 → 2103.94] I've realized
[2103.94 → 2105.26] they also have Vim mode
[2105.26 → 2106.08] and the reason
[2106.08 → 2106.82] why I found that out,
[2106.86 → 2107.70] I thought maybe this was
[2107.70 → 2108.94] actually an April Fool's joke
[2108.94 → 2109.54] and I was like,
[2109.78 → 2111.06] please don't let this be fake.
[2111.12 → 2112.44] I want this to always be here.
[2113.02 → 2115.12] But it has existed for a while.
[2115.18 → 2116.12] I just didn't notice it.
[2116.68 → 2117.04] Today,
[2117.20 → 2118.08] for April Fool's
[2118.08 → 2119.26] in the menu bar,
[2119.36 → 2120.04] they did put this
[2120.04 → 2121.04] like April Fool's joke
[2121.04 → 2121.88] which is like the
[2121.88 → 2123.42] Nyan Cat,
[2123.54 → 2124.62] they called it a red panda,
[2124.80 → 2125.26] which I'm not sure
[2125.26 → 2125.92] if that's like a
[2125.92 → 2127.28] different meme,
[2128.02 → 2130.06] but it's like a progress bar
[2130.06 → 2131.28] with like the red panda
[2131.28 → 2131.94] walking across
[2131.94 → 2133.36] and that drew my eyes down
[2133.36 → 2134.62] and I saw on the right-hand side
[2134.62 → 2135.52] they have different settings
[2135.52 → 2136.40] such as
[2136.40 → 2136.96] do you want to use
[2136.96 → 2137.70] tabs or spaces?
[2137.88 → 2138.08] Of course,
[2138.16 → 2139.14] everybody picks spaces
[2139.14 → 2140.40] and you want to have
[2140.40 → 2141.12] two or four
[2141.12 → 2142.28] and everybody picks two
[2142.28 → 2143.98] but you can also set
[2143.98 → 2144.46] your editor
[2144.46 → 2145.64] and they have Sublime
[2145.64 → 2147.76] and they have Emacs
[2147.76 → 2148.50] and they have Vim.
[2148.88 → 2149.84] So you get your Vim
[2149.84 → 2150.68] key bindings
[2150.68 → 2151.50] in your browser,
[2152.12 → 2152.76] collaborative,
[2154.02 → 2155.00] share view URL
[2155.00 → 2157.18] with lots of cool
[2157.18 → 2157.74] keyboard shortcuts
[2157.74 → 2159.06] and all the bells
[2159.06 → 2159.40] and whistles.
[2159.86 → 2161.06] I just really like this tool.
[2161.40 → 2161.92] So shout out
[2161.92 → 2162.90] to the folks at Hacked.
[2162.90 → 2164.20] I did put some tweets out today
[2164.20 → 2164.90] and they responded
[2164.90 → 2166.20] regarding this Vim thing
[2166.20 → 2167.44] ensuring me
[2167.44 → 2168.80] that it's not an April Fool's joke.
[2168.86 → 2169.74] It's actually a real feature
[2169.74 → 2171.98] and I decided to invite him
[2171.98 → 2172.46] on the show.
[2172.68 → 2174.76] So I think it's all open source.
[2174.96 → 2175.92] I saw they have like
[2175.92 → 2177.10] 56 open source repos
[2177.10 → 2178.28] on their GitHub.
[2178.42 → 2179.08] I think they're over there
[2179.08 → 2179.70] in Taiwan.
[2180.02 → 2181.20] So they've agreed to come on.
[2181.26 → 2181.76] I'm not sure
[2181.76 → 2182.84] how it'll work out
[2182.84 → 2184.52] timing and whatnot
[2184.52 → 2186.98] and if they're native English speakers
[2186.98 → 2187.72] or anything like that
[2187.72 → 2188.90] but cool technology,
[2189.68 → 2190.20] open source,
[2190.30 → 2192.36] all built with webby tools.
[2192.90 → 2194.02] And I'm a big fan.
[2194.18 → 2195.58] So shout out to Hacked.
[2196.08 → 2196.92] Yeah, that's awesome.
[2197.22 → 2197.90] I saw your tweet
[2197.90 → 2199.34] about the Vim mode.
[2199.88 → 2200.64] It made me wonder
[2200.64 → 2201.58] what is special
[2201.58 → 2202.68] about Sublime mode
[2202.68 → 2204.54] versus anything else,
[2204.74 → 2205.40] any other editor.
[2205.82 → 2206.98] Yeah, I don't really know.
[2207.36 → 2208.08] So I brought a lot
[2208.08 → 2209.46] of my Sublime shortcuts
[2209.46 → 2211.16] into VS Code.
[2211.58 → 2212.26] So I'm not sure
[2212.26 → 2213.74] what VS Code's defaults are
[2213.74 → 2214.62] because I just kind of thought
[2214.62 → 2215.32] they were the same
[2215.32 → 2217.04] in terms of keyboard shortcuts.
[2217.04 → 2218.76] I wonder how different
[2218.76 → 2220.80] those like stock Sublime text
[2220.80 → 2222.10] versus stock VS Code
[2222.10 → 2223.04] if those are similar.
[2223.32 → 2223.94] Of course,
[2224.12 → 2225.98] a lot of the editors used
[2225.98 → 2227.34] or borrowed from Emacs,
[2227.56 → 2227.82] you know,
[2227.86 → 2228.78] which is a lot of the control
[2228.78 → 2229.46] based shortcuts
[2229.46 → 2230.46] and not modes.
[2231.10 → 2232.54] So maybe there's Emacs
[2232.54 → 2233.08] and there's a Sublime.
[2233.22 → 2233.94] I don't know the difference
[2233.94 → 2234.44] between the two.
[2234.54 → 2236.10] I think it defaults to Sublime
[2236.10 → 2237.46] because that's what I was in
[2237.46 → 2238.78] before I realized
[2238.78 → 2239.58] you could toggle it.
[2240.00 → 2241.22] But I'm not really sure.
[2241.72 → 2243.44] They have a question mark operator.
[2243.54 → 2243.98] Let me see.
[2244.80 → 2245.16] A lot of times
[2245.16 → 2246.08] you can do question mark
[2246.08 → 2247.90] and just they'll open up
[2247.90 → 2249.26] a keyboard shortcut,
[2249.58 → 2249.88] you know,
[2250.10 → 2250.52] overlay,
[2250.70 → 2251.10] which tells you
[2251.10 → 2252.32] what all things do.
[2252.74 → 2254.06] But it doesn't seem
[2254.06 → 2254.54] to be working
[2254.54 → 2255.42] at least in Vim mode.
[2255.76 → 2256.24] In Vim mode,
[2256.30 → 2256.84] it opens up
[2256.84 → 2258.22] to do a regex search.
[2258.52 → 2259.02] That's right.
[2259.30 → 2260.06] Is that what Vim does?
[2260.90 → 2261.58] Slash does,
[2261.66 → 2263.04] which it also does in here.
[2263.28 → 2263.56] Yeah.
[2263.68 → 2264.74] So forward slash I do.
[2264.84 → 2265.84] I never hit question mark
[2265.84 → 2267.08] to do a regex in Vim,
[2267.18 → 2268.16] but I wouldn't be surprised
[2268.16 → 2269.54] if it did that as well.
[2269.88 → 2270.04] Now,
[2270.10 → 2271.12] I've only used it in Vim mode
[2271.12 → 2272.50] for probably like two hours
[2272.50 → 2274.90] and all of my normal navigation
[2274.90 → 2275.38] is working.
[2275.52 → 2277.02] So like DD to delete a line,
[2277.58 → 2279.42] colon one goes to the top,
[2279.54 → 2280.44] shift G goes to the bottom,
[2280.48 → 2281.54] like all the things I'm used to.
[2281.64 → 2283.32] But I wonder how uncanny valley
[2283.32 → 2285.22] it gets the more you use it.
[2285.46 → 2286.22] How are they achieving
[2286.22 → 2287.04] this Vim support?
[2287.22 → 2287.78] And is it getting one
[2287.78 → 2288.16] of those things
[2288.16 → 2288.76] where it supports
[2288.76 → 2290.84] like 80% of Vim key bindings,
[2290.96 → 2291.64] but then,
[2291.82 → 2292.10] you know,
[2292.10 → 2293.28] your favourite tip and trick
[2293.28 → 2294.38] doesn't work?
[2294.44 → 2294.88] I don't know.
[2295.32 → 2296.12] I haven't used it long enough
[2296.12 → 2296.52] to know that,
[2296.52 → 2298.06] but it is good enough
[2298.06 → 2299.12] for me to enjoy it so far.
[2299.32 → 2299.42] Yeah.
[2299.42 → 2299.46] Yeah.
[2300.10 → 2301.68] And real-time follow-up,
[2301.82 → 2302.74] I did not know this,
[2302.88 → 2303.96] but question mark
[2303.96 → 2305.26] does actually do
[2305.26 → 2306.02] reject search,
[2306.22 → 2306.78] but backwards.
[2307.28 → 2307.92] Backwards meaning
[2307.92 → 2308.64] starting at the bottom
[2308.64 → 2309.10] of the document
[2309.10 → 2309.66] and working up?
[2309.80 → 2310.96] Starting from your cursor
[2310.96 → 2311.68] and looking up
[2311.68 → 2312.54] rather than down.
[2313.00 → 2313.36] Oh,
[2313.72 → 2314.34] that's nifty.
[2314.40 → 2315.12] I did not know that
[2315.12 → 2316.12] because I've never used it.
[2316.38 → 2317.42] I use slash all the time.
[2317.56 → 2317.86] Right.
[2318.08 → 2318.62] But it's the
[2318.74 → 2319.62] and it's shift slash,
[2319.74 → 2320.38] so it's like,
[2320.62 → 2321.26] it makes sense,
[2321.32 → 2321.44] right?
[2321.44 → 2322.18] It's the same key.
[2322.30 → 2322.50] Yeah.
[2322.72 → 2323.66] Just one with a shift key.
[2323.66 → 2324.38] So one goes one way,
[2324.44 → 2325.02] one goes the other.
[2325.94 → 2327.30] T-I-L right here,
[2327.40 → 2328.52] live on JS Party.
[2328.52 → 2332.24] I got a story
[2332.24 → 2334.26] that I'm going to tell.
[2334.54 → 2335.52] You're going to love it,
[2335.60 → 2335.80] baby,
[2335.92 → 2337.02] take it swell.
[2337.32 → 2339.18] I only learned it today.
[2339.74 → 2341.14] T-I-L.
[2344.58 → 2345.32] T-I-L.
[2345.38 → 2345.80] There we go.
[2346.02 → 2346.92] I stalled for you.
[2347.56 → 2348.74] We're still doing shoutouts.
[2349.04 → 2350.18] Do you have a shoutout, Nick?
[2350.32 → 2350.84] Shout us out.
[2351.10 → 2352.10] I was going to shout out
[2352.10 → 2353.16] also a thing,
[2353.82 → 2354.70] and that is
[2354.70 → 2356.10] an app called
[2356.10 → 2357.06] Keyboard Maestro.
[2357.70 → 2358.22] Have you heard of it?
[2358.22 → 2359.82] I have heard of it.
[2360.10 → 2361.74] I do not know what it does,
[2362.20 → 2363.10], so please tell me.
[2363.56 → 2365.30] So it does a lot,
[2365.58 → 2367.10] but it lets you
[2367.10 → 2367.98] set up
[2367.98 → 2369.22] automations,
[2369.34 → 2369.68] basically,
[2369.90 → 2371.06] on your Mac.
[2371.22 → 2372.42] It's a Mac program,
[2373.14 → 2374.20] and it lets you,
[2374.38 → 2374.44] like,
[2374.60 → 2375.06] up so that,
[2375.10 → 2375.22] you know,
[2375.26 → 2376.50] when I hit these specific
[2376.50 → 2377.76] keyboard shortcuts,
[2378.18 → 2378.78] and I can have it,
[2378.82 → 2379.00] like,
[2379.12 → 2380.28] specific to an application,
[2380.40 → 2380.92] so I can say,
[2381.08 → 2382.82] when Slack is
[2382.82 → 2383.42] in the foreground,
[2383.80 → 2384.56] and I press
[2384.56 → 2385.40] question mark,
[2385.46 → 2385.82] question mark,
[2385.82 → 2386.66] or something like that,
[2386.66 → 2388.44] then run this script,
[2388.68 → 2389.62] or I can have it,
[2390.32 → 2390.52] like,
[2390.56 → 2391.52] I can record a macro,
[2391.66 → 2392.36] and have it actually,
[2392.40 → 2392.58] like,
[2392.62 → 2393.28] move my mouse around,
[2393.34 → 2395.06] and quickly do something,
[2395.26 → 2396.16] or I can have it select
[2396.16 → 2396.82] from a menu,
[2397.10 → 2399.36] and you can mix and match
[2399.36 → 2400.32] these all together
[2400.32 → 2401.22] to build
[2401.22 → 2402.76] cool automations
[2402.76 → 2403.48] that do a lot of
[2403.48 → 2404.06] different things,
[2404.06 → 2406.00] and so I started
[2406.00 → 2406.70] playing with this,
[2406.78 → 2408.30] and I also have
[2408.30 → 2409.14] a Stream Deck,
[2409.58 → 2410.34] and Stream Deck
[2410.34 → 2410.66] is,
[2410.76 → 2411.50] it's like a little
[2411.50 → 2413.02] device that has,
[2413.12 → 2414.64] mine has 16 buttons,
[2414.74 → 2415.52] and all the buttons
[2415.52 → 2415.92] have,
[2416.50 → 2416.78] are,
[2416.88 → 2416.94] like,
[2416.98 → 2418.16] little LCD screens,
[2418.28 → 2418.98] so you can set
[2418.98 → 2420.34] what each button is,
[2420.52 → 2422.74] and I can trigger
[2422.74 → 2423.38] Keyboard Maestro
[2423.38 → 2425.42] macros from that,
[2425.68 → 2426.84] and so I can push a button
[2426.84 → 2427.80] and have it
[2427.80 → 2428.98] do things like,
[2429.32 → 2429.82] like,
[2429.90 → 2430.56] turn my lights on
[2430.56 → 2430.90] and off,
[2430.90 → 2433.50] and I can also have it
[2433.50 → 2434.88] do things like,
[2435.14 → 2436.26] automatically open up
[2436.26 → 2437.04] Audio Hijack,
[2437.20 → 2438.46] and get ready for
[2438.46 → 2439.70] a Zoom meeting,
[2440.06 → 2441.56] and get ready to record,
[2441.64 → 2442.26] or have it automatically
[2442.26 → 2442.94] start recording,
[2443.58 → 2444.76] and kind of combine
[2444.76 → 2445.32] them all together,
[2445.44 → 2446.48] so then I just push a button,
[2446.98 → 2448.16] and it can do things
[2448.16 → 2448.34] like,
[2448.48 → 2449.12] lay out windows,
[2449.22 → 2449.60] so I have it,
[2449.60 → 2449.74] like,
[2449.84 → 2450.58] moving windows
[2450.58 → 2451.84] where I want on my screen,
[2452.02 → 2452.80] so everything is
[2452.80 → 2454.04] not overlapping,
[2454.28 → 2454.98] and it's all
[2454.98 → 2456.86] readily visible for me,
[2457.14 → 2458.28] and then it can start
[2458.28 → 2458.64] recording,
[2458.84 → 2459.84] and turn my lights on,
[2459.84 → 2461.38] and do all this
[2461.38 → 2462.02] really cool stuff.
[2462.54 → 2464.08] It's a pretty cool way
[2464.08 → 2466.84] to do some simple
[2466.84 → 2468.12] and complex automation
[2468.12 → 2468.70] on your Mac.
[2469.02 → 2469.72] That is cool.
[2469.86 → 2470.98] So it's actually
[2470.98 → 2471.82] driving, like,
[2472.34 → 2472.98] the mouse around
[2472.98 → 2473.82] and everything as well,
[2473.88 → 2474.02] right?
[2474.04 → 2474.30] It can.
[2474.30 → 2475.02] It's not just,
[2475.42 → 2476.12] yeah, it can.
[2476.24 → 2476.74] So you can, like,
[2476.76 → 2477.00] say,
[2477.12 → 2477.86] go to this area
[2477.86 → 2478.30] of the screen
[2478.30 → 2479.24] and click here,
[2479.28 → 2480.36] kind of thing?
[2480.56 → 2480.74] Yep.
[2481.00 → 2481.52] It's got a little
[2481.52 → 2482.14] recorder, too,
[2482.14 → 2482.66] so you can just
[2482.66 → 2483.34] record and then
[2483.34 → 2483.96] do it once,
[2484.08 → 2484.96] and it'll figure out
[2484.96 → 2485.64] what to do from there.
[2486.14 → 2486.66] So it'll, like,
[2487.14 → 2487.64] from there,
[2487.72 → 2488.22] it'll be like,
[2488.34 → 2488.92] oh, you know,
[2488.98 → 2489.64] I click in,
[2489.84 → 2490.84] instead of Tweet Bot,
[2491.00 → 2492.56] and then click,
[2492.70 → 2492.98] you know,
[2493.04 → 2494.18] 60 pixels from the right
[2494.18 → 2495.46] and 120 pixels
[2495.46 → 2496.50] from the top,
[2496.84 → 2497.64] click right there.
[2497.76 → 2498.22] So it's, like,
[2498.36 → 2499.32] relative to where
[2499.32 → 2500.12] the window is,
[2500.28 → 2501.42] or relative to the
[2501.42 → 2502.24] window edges,
[2502.50 → 2503.88] and then go from there.
[2504.38 → 2505.34] That sounds a little fickle.
[2505.68 → 2505.88] Yeah,
[2506.22 → 2506.70] it can be,
[2506.78 → 2507.10] I'm sure.
[2507.30 → 2507.44] Yeah.
[2508.48 → 2508.86] Like,
[2508.90 → 2509.92] if you change the size
[2509.92 → 2510.62] of your Tweet Bot window,
[2510.74 → 2511.06] it's broken.
[2511.12 → 2511.30] Yeah.
[2511.72 → 2511.96] Well,
[2512.12 → 2512.96] now you know about
[2512.96 → 2513.70] my unit tests,
[2513.76 → 2514.02] so.
[2514.02 → 2518.06] So is this a free app?
[2518.10 → 2518.96] Is it a paid app?
[2519.00 → 2519.90] Is it Mac only?
[2520.08 → 2520.52] What's the...
[2520.52 → 2521.68] It is Mac only.
[2522.00 → 2524.40] It is not free either.
[2524.94 → 2526.10] I forgot how much it is.
[2526.18 → 2527.02] $36 American.
[2528.02 → 2528.76] It's pretty cool.
[2529.18 → 2529.98] Just being able to set
[2529.98 → 2530.66] these things up
[2530.66 → 2531.64] and have automatically
[2531.64 → 2533.34] set my workspace up
[2533.34 → 2534.06] the way I want it
[2534.06 → 2536.02] for different scenarios,
[2536.12 → 2537.12] whether that's writing code
[2537.12 → 2538.90] or looking at documentation
[2538.90 → 2539.86] or taking a meeting
[2539.86 → 2541.36] or doing a podcast.
[2541.36 → 2543.14] I can have it quickly switch.
[2543.76 → 2544.72] And that's kind of the
[2544.72 → 2546.10] main thing
[2546.10 → 2546.76] that I've been coming
[2546.76 → 2547.56] into it with
[2547.56 → 2549.02] is how do I set up
[2549.02 → 2549.40] my workspace
[2549.40 → 2550.44] without me having to
[2550.44 → 2552.56] manually move windows around
[2552.56 → 2554.06] and set things up
[2554.06 → 2555.94] exactly how I always want them.
[2556.60 → 2557.82] It's just now
[2557.82 → 2559.36] a button click away for me.
[2559.90 → 2559.92] Yeah,
[2559.96 → 2560.46] that's nice.
[2560.56 → 2561.60] So I have this laptop
[2561.60 → 2563.32] and I don't dock it,
[2563.38 → 2564.32] but I plug it into things,
[2564.40 → 2564.48] right?
[2564.52 → 2564.76] I come,
[2564.86 → 2565.80] I have a separate monitor
[2565.80 → 2568.58] and I have my interface,
[2568.78 → 2569.12] et cetera,
[2569.52 → 2570.08] to plug into.
[2570.34 → 2571.28] And then I want
[2571.28 → 2572.02] to leave my desk
[2572.02 → 2572.72] and take my laptop
[2572.72 → 2573.38] downstairs
[2573.38 → 2574.60] and I do that
[2574.60 → 2575.64] and everything kind of
[2575.64 → 2577.04] like mungs into one screen.
[2577.36 → 2578.20] So I kind of have
[2578.20 → 2579.72] two modes of computing
[2579.72 → 2580.26] on this thing.
[2580.36 → 2581.50] I have liked my plugged in
[2581.50 → 2582.58] almost like docked mode
[2582.58 → 2583.42] and undocked mode.
[2583.92 → 2584.54] And it would be nice
[2584.54 → 2585.50] to have just like,
[2586.12 → 2586.94] I wish it was just a tech
[2586.94 → 2587.12] like,
[2587.22 → 2587.28] hey,
[2587.30 → 2587.98] I just plugged into
[2587.98 → 2588.98] your second monitor.
[2589.26 → 2590.24] I'm going to do all of the
[2590.38 → 2591.14] put everything back
[2591.14 → 2591.84] where you had it,
[2591.88 → 2592.12] you know,
[2592.16 → 2593.10] before you detached
[2593.10 → 2593.72] or something like that.
[2593.94 → 2594.02] Yeah.
[2594.12 → 2594.98] So I could get that done
[2594.98 → 2595.82] maybe with Keyboard Maestro
[2595.82 → 2596.74] and just have it
[2596.74 → 2598.12] do certain things.
[2598.12 → 2598.96] Does it trigger,
[2599.42 → 2600.10] like it triggers
[2600.10 → 2600.84] on a keyboard shortcut
[2600.84 → 2601.42] or a trigger?
[2601.52 → 2602.00] Can I have it trigger
[2602.00 → 2602.60] on an event?
[2602.72 → 2602.86] Yeah.
[2603.16 → 2604.00] So you could have it trigger
[2604.00 → 2604.86] on like mounting
[2604.86 → 2605.90] a particular volume,
[2606.36 → 2608.48] connecting to a specific Wi-Fi.
[2609.00 → 2610.36] There's display layout changed,
[2610.40 → 2611.38] which would probably be like
[2611.38 → 2612.64] going from an external monitor
[2612.64 → 2613.68] to your laptop.
[2613.92 → 2614.28] Exactly.
[2614.52 → 2615.20] And have it trigger
[2615.20 → 2615.88] based on that.
[2616.20 → 2616.52] So yeah,
[2616.56 → 2617.68] there's lots of different.
[2617.76 → 2618.44] That's cool.
[2618.58 → 2619.10] And then there's just
[2619.10 → 2619.78] simple things like
[2619.78 → 2620.46] you can just have it
[2620.46 → 2621.58] start up its own web server
[2621.58 → 2623.18] and then you can send it triggers.
[2623.68 → 2625.96] Like if you publicly expose that,
[2626.04 → 2627.24] you can just send triggers to it.
[2627.58 → 2628.74] Or from like your local network,
[2628.74 → 2629.36] you could have it,
[2630.10 → 2630.32] you know,
[2630.38 → 2631.92] I'm going to just post
[2631.92 → 2632.54] to this address
[2632.54 → 2634.10] and now my Mac's
[2634.10 → 2634.80] going to go do something.
[2635.34 → 2636.08] Or you can just have it
[2636.08 → 2637.04] like be a Iron trigger.
[2637.22 → 2638.08] That sounds dangerous.
[2638.80 → 2639.20] Yeah.
[2640.32 → 2641.38] How do you do this deal
[2641.38 → 2642.36] where you change the lights
[2642.36 → 2643.24] in your room there
[2643.24 → 2644.14] that you just demonstrated?
[2644.46 → 2644.70] Yeah.
[2644.70 → 2646.36] So that's actually connected
[2646.36 → 2648.98] with the Stream Deck software.
[2649.34 → 2651.32] It has a control centre
[2651.32 → 2652.58] that is controlling them.
[2652.90 → 2653.72] Which is a piece of software
[2653.72 → 2654.78] that runs on your machine.
[2654.78 → 2655.96] So Keyboard Maestro
[2655.96 → 2657.30] is just controlling that software.
[2657.56 → 2657.66] Right.
[2657.80 → 2658.00] Okay.
[2658.44 → 2660.26] So what would be a cool thing
[2660.26 → 2661.40] that you would run a web server
[2661.40 → 2662.40] and post to it
[2662.40 → 2663.14] from different parts
[2663.14 → 2664.24] of your house?
[2664.54 → 2664.80] Ooh.
[2665.48 → 2666.70] That is a good question.
[2667.16 → 2668.78] Can those hue lights,
[2669.12 → 2671.00] can they do webhook kind of things?
[2671.20 → 2671.98] Like can you configure
[2671.98 → 2673.08] those things to make,
[2673.48 → 2674.16] because this is like
[2674.16 → 2675.84] inbound request, right?
[2675.84 → 2675.90] Yeah.
[2675.90 → 2676.82] Like it's posting
[2676.82 → 2678.22] to your Keyboard Maestro
[2678.22 → 2678.80] web server.
[2679.16 → 2680.32] So something would have to be
[2680.32 → 2681.12] like pushing data
[2681.12 → 2682.06] or pushing an event.
[2682.18 → 2683.38] Like the lights turned on.
[2683.38 → 2684.68] Maybe you could have it
[2684.68 → 2687.34] hook up to your switch as well.
[2687.48 → 2687.94] Like if you had
[2687.94 → 2688.86] a regular light switch
[2688.86 → 2690.52] and it turned on,
[2690.72 → 2691.46] if you could configure
[2691.46 → 2692.04] the hue lights
[2692.04 → 2692.76] to actually do that,
[2692.82 → 2693.68] they could make a post
[2693.68 → 2694.72] over to your web server
[2694.72 → 2695.66] and do something
[2695.66 → 2696.26] on your laptop.
[2696.66 → 2696.82] You know,
[2696.82 → 2697.90] control your laptop somehow.
[2698.00 → 2698.20] Yeah.
[2698.42 → 2699.36] Via some other switch
[2699.36 → 2699.88] in your house.
[2699.94 → 2700.66] Yeah, for sure.
[2700.78 → 2701.26] Pretty neat.
[2701.58 → 2701.80] Yeah.
[2701.98 → 2703.00] All I want is for
[2703.00 → 2704.70] my windows to go back
[2704.70 → 2705.24] where they were
[2705.24 → 2706.20] when I unplug, man.
[2706.32 → 2707.14] That's all I want in my life.
[2709.06 → 2710.26] I like this dance I do.
[2710.34 → 2711.46] Plug in like this one here,
[2711.60 → 2712.14] that goes there,
[2712.24 → 2712.82] that goes there.
[2712.82 → 2713.56] Oh, I'm back.
[2713.82 → 2714.12] I was like,
[2714.16 → 2714.80] this seems like
[2714.80 → 2716.32] something a computer
[2716.32 → 2716.78] should do.
[2717.78 → 2718.70] They can do it.
[2718.76 → 2719.68] That's the amazing thing.
[2720.00 → 2720.68] They can,
[2720.96 → 2721.88] but they won't
[2721.88 → 2723.36] without a lot of tomfooleries.
[2723.64 → 2724.58] That's what it always seems like.
[2724.70 → 2725.02] So,
[2725.72 → 2726.28] it is.
[2726.44 → 2726.68] You're like,
[2726.74 → 2728.04] oh, this thing's not going to last.
[2728.22 → 2728.34] You know,
[2728.34 → 2729.68] I've set up enough hacks
[2729.68 → 2730.20] in my life
[2730.20 → 2730.64] where I'm like,
[2730.74 → 2731.94] this hack isn't going to last.
[2732.76 → 2733.24] And nowadays,
[2733.24 → 2734.66] I just do the manual thing.
[2734.74 → 2734.98] I'm like,
[2735.08 → 2735.24] yeah,
[2735.52 → 2737.02] I can either set up the hack,
[2737.24 → 2737.94] maintain the hack,
[2737.94 → 2739.82] or I can just do the manual thing.
[2740.72 → 2741.48] And nowadays,
[2741.62 → 2742.04] I'm just like,
[2742.10 → 2742.92] I'm just going to drag the window
[2742.92 → 2743.52] every time
[2743.52 → 2744.72] until something that actually
[2744.72 → 2746.08] is like supported
[2746.08 → 2747.36] by the operating system.
[2747.62 → 2747.76] Yeah.
[2747.82 → 2748.04] You know,
[2748.30 → 2750.04] if Steve Jobs
[2750.04 → 2750.78] doesn't come back
[2750.78 → 2751.24] from the dead
[2751.24 → 2752.56] and do the feature for me,
[2752.68 → 2753.68] I'm not going to have it.
[2753.82 → 2754.96] That's what has to happen.
[2754.96 → 2756.22] I haven't looked into it too much,
[2756.30 → 2757.84] but there is Automaton
[2757.84 → 2759.80] that comes standard with Macs.
[2760.18 → 2761.14] And you'd probably have to write
[2761.14 → 2761.72] AppleScript,
[2761.88 → 2762.58] which is immediately
[2762.58 → 2764.42] something I don't want to look at.
[2765.00 → 2766.98] But you can do a lot of automation
[2766.98 → 2769.18] just natively on the Mac
[2769.18 → 2770.28] without any extra software.
[2770.28 → 2770.62] Yeah.
[2770.84 → 2771.14] So,
[2771.36 → 2772.62] have you written AppleScript's?
[2772.64 → 2773.26] Because I have.
[2774.70 → 2776.08] I'd rather do the manual way.
[2776.70 → 2777.28] That being said,
[2777.54 → 2779.10] there is a JavaScript interface
[2779.10 → 2780.68] now into scripting the Mac,
[2780.80 → 2782.08] but I've also tried to use that
[2782.08 → 2783.94] to very little success.
[2783.96 → 2784.28] It's still terrible.
[2784.28 → 2784.52] Like,
[2784.72 → 2785.16] the docs,
[2785.52 → 2785.68] yeah,
[2785.70 → 2786.94] the documentation is just like,
[2786.98 → 2787.30] I can't,
[2787.34 → 2787.84] it's inscrutable.
[2787.98 → 2788.76] How do I even use it?
[2788.76 → 2788.90] Like,
[2788.92 → 2789.72] I understand JavaScript,
[2790.00 → 2791.10] but I can't use this API.
[2791.46 → 2791.58] You know?
[2791.96 → 2792.88] The only piece of AppleScript
[2792.88 → 2793.72] that I've written,
[2793.82 → 2794.62] and I wrote it actually
[2794.62 → 2796.08] in AppleScript and JavaScript,
[2796.68 → 2799.24] and that was to ask music
[2799.24 → 2799.96] or Spotify
[2799.96 → 2801.50] what song is playing
[2801.50 → 2802.18] so that I can put that
[2802.18 → 2802.98] in my T-Bunk stock.
[2803.12 → 2804.38] And then the T-Bunk stock
[2804.38 → 2805.62] just refreshes every five seconds
[2805.62 → 2806.14] and asks,
[2806.40 → 2807.20] what's playing right now?
[2807.22 → 2808.16] And it updates right there.
[2808.88 → 2809.98] And that broke
[2809.98 → 2811.82] in macOS Big Sur.
[2812.10 → 2812.96] And it broke
[2812.96 → 2814.00] in a really weird way
[2814.00 → 2815.44] where it just like
[2815.44 → 2816.18] throws an error
[2816.18 → 2816.78] that the object
[2816.78 → 2817.70] that I'm trying to grab
[2817.70 → 2818.80] from music
[2818.80 → 2819.70] doesn't exist,
[2820.18 → 2821.62] except it does
[2821.62 → 2822.92] if I'm playing
[2822.92 → 2824.58] like a music file
[2824.58 → 2825.84] that is in my library.
[2825.84 → 2826.70] But if it's just like
[2826.70 → 2827.60] I'm listening to,
[2827.60 → 2828.34] you know,
[2828.52 → 2829.60] Apple Music Radio,
[2829.94 → 2830.94] whatever that's called,
[2831.00 → 2832.22] or like an Apple Music playlist
[2832.22 → 2833.76] that is not in my library,
[2834.34 → 2834.98] then it's like,
[2835.08 → 2835.26] whoa,
[2835.42 → 2836.56] I don't know what this is.
[2836.56 → 2837.78] And it just blows up.
[2837.78 → 2838.30] Wow.
[2838.62 → 2838.98] Yeah.
[2839.40 → 2840.10] That's life.
[2840.50 → 2841.60] The best Apple Script
[2841.60 → 2842.10] I've written,
[2842.68 → 2843.28] probably ever,
[2843.38 → 2844.08] but definitely lately,
[2844.36 → 2845.70] is one that we use
[2845.70 → 2846.38] for our clips,
[2846.50 → 2847.32] the way we make our clips,
[2847.72 → 2848.68] which does we actually use
[2848.68 → 2849.66] Keynote for our clips.
[2850.30 → 2853.08] And we write the text
[2853.08 → 2854.60] in a text document.
[2854.80 → 2856.80] So we pull the text
[2856.80 → 2857.86] out of our transcripts,
[2858.40 → 2859.00] and they're just
[2859.00 → 2860.18] markdown transcripts.
[2860.18 → 2861.06] So they're basically text
[2861.06 → 2861.58] with a little bit
[2861.58 → 2861.98] of formatting.
[2862.56 → 2863.60] And we just copy all those
[2863.60 → 2864.62] into a text document
[2864.62 → 2867.02] and just space it out
[2867.02 → 2867.94] so it'll be like Jared
[2867.94 → 2868.68] and then a thing
[2868.68 → 2869.26] and then Nick
[2869.26 → 2869.88] and then a thing.
[2870.22 → 2871.16] And just format it
[2871.16 → 2871.68] according to what
[2871.68 → 2872.30] I came up with.
[2872.80 → 2874.36] And then you copy that
[2874.36 → 2875.66] into your clipboard.
[2876.32 → 2877.80] And then you open up Keynote
[2877.80 → 2880.02] and you execute
[2880.02 → 2881.00] this Apple Script.
[2881.28 → 2882.48] And it actually scripts Keynote
[2882.48 → 2884.64] to go and parse the text
[2884.64 → 2886.88] and then like add a slide
[2886.88 → 2887.50] for each one
[2887.50 → 2888.66] and paste it into there.
[2889.08 → 2889.80] And then it'll even go
[2889.80 → 2891.14] and switch like the active face
[2891.14 → 2891.78] and stuff like that.
[2891.78 → 2892.22] Wow.
[2892.46 → 2893.18] Super cool.
[2893.26 → 2894.76] It took me way too long.
[2895.12 → 2895.64] Way too long
[2895.64 → 2896.24] to get this to work.
[2896.34 → 2897.44] But once it worked,
[2897.54 → 2898.66] it felt like magic
[2898.66 → 2899.76] because I hit paste.
[2900.10 → 2900.66] It's like a special.
[2900.86 → 2901.52] And then I attached
[2901.52 → 2902.18] that Apple Script
[2902.18 → 2902.98] to a keyboard shortcut
[2902.98 → 2903.80] inside a Keynote.
[2904.16 → 2905.46] So I just like execute it
[2905.46 → 2905.80] and it's like
[2905.80 → 2907.70] and all these slides
[2907.70 → 2908.80] come into life.
[2908.92 → 2909.68] Do you like to watch it
[2909.68 → 2910.36] as it's going?
[2910.48 → 2911.08] So cool.
[2911.36 → 2912.64] Is it recording?
[2912.80 → 2913.36] Like does it start
[2913.36 → 2914.08] the screen show
[2914.08 → 2915.34] and then record that somehow
[2915.34 → 2916.52] or is that something manual?
[2916.94 → 2917.30] No.
[2917.50 → 2918.00] So that,
[2918.22 → 2919.64] it just pastes them in basically.
[2919.86 → 2920.66] And then you're like
[2920.66 → 2921.56] you'll want to do some
[2921.56 → 2923.38] fixes and stuff from there usually
[2923.38 → 2924.38] because like the way
[2924.38 → 2925.68] the words show up on the slide
[2925.68 → 2926.96] will be like weirdly formatted.
[2927.08 → 2928.46] So like maybe like add a line
[2928.46 → 2929.20] or remove a line
[2929.20 → 2930.00] or shrink the text
[2930.00 → 2930.72] to make the text bigger.
[2930.94 → 2931.86] So you do all that.
[2931.92 → 2933.48] It's kind of like a QA phase.
[2933.84 → 2935.66] And then inside Keynote,
[2935.78 → 2938.62] they have an actual recording option
[2938.62 → 2940.00] which people use,
[2940.00 → 2940.46] I believe,
[2940.66 → 2942.12] to either pre-record their talks
[2942.12 → 2943.18] or to practice their talks
[2943.18 → 2944.00] and watch them back.
[2944.00 → 2945.96] So you can go into Side Keynote
[2945.96 → 2947.84] and say like record my talk
[2947.84 → 2950.36] and it will display your talk,
[2950.62 → 2950.90] you know,
[2950.96 → 2951.74] on the screen
[2951.74 → 2955.96] as well as your regular heads up display.
[2956.08 → 2956.60] What do they call that?
[2956.64 → 2957.24] Like the speaker,
[2957.36 → 2958.24] the presentation view.
[2958.82 → 2959.76] So you can see the timing
[2959.76 → 2960.92] and you can see the next slide,
[2961.04 → 2961.30] et cetera.
[2961.50 → 2962.54] And it will record
[2962.54 → 2964.00] what's on the screen
[2964.00 → 2965.14] and your voice
[2965.14 → 2967.18] and anything that's going through
[2967.18 → 2967.90] the system.
[2968.50 → 2970.88] So you can also add a back,
[2970.98 → 2972.44] a soundtrack in Keynote as well.
[2972.44 → 2974.30] So like maybe you want to have like mood music
[2974.30 → 2975.24] while you're doing your talk.
[2975.46 → 2975.88] I don't know.
[2975.98 → 2977.28] These weird features of Keynote,
[2977.48 → 2978.56] we're abusing them.
[2978.90 → 2981.42] So we drag the sounds into there
[2981.42 → 2983.46] and we just say like play
[2983.46 → 2984.88] and we record it
[2984.88 → 2987.08] and then we just hit the next button
[2987.08 → 2988.38] over and over again
[2988.38 → 2989.56] as it makes sense
[2989.56 → 2990.40] with the person talking.
[2990.92 → 2993.30] So you basically perform the slide once
[2993.30 → 2994.84] in real time
[2994.84 → 2995.98] and then it records that
[2995.98 → 2996.72] and then you got your clip.
[2997.64 → 2997.90] Yeah.
[2998.24 → 2999.42] It still takes some work
[2999.42 → 3000.48] but it's way less work
[3000.48 → 3001.86] than what the other way is
[3001.86 → 3003.22] which is basically
[3003.22 → 3005.24] you like get
[3005.24 → 3006.26] most of these tools,
[3006.46 → 3007.34] you get all your clips
[3007.34 → 3008.00] into a thing
[3008.00 → 3009.50] and then you have to like
[3009.50 → 3011.84] change the start and end times
[3011.84 → 3013.76] of every clip
[3013.76 → 3015.50] and it's usually on like this side
[3015.50 → 3016.44] or every slide
[3016.44 → 3017.96] and it's like this sideways
[3017.96 → 3019.42] horizontal scroll thing.
[3019.82 → 3020.58] Super annoying
[3020.58 → 3022.54] and then uses up a bunch of RAM
[3022.54 → 3023.18] because it's like
[3023.18 → 3024.34] some Adobe thing
[3024.34 → 3025.72] or some web thing
[3025.72 → 3027.08] that just clogs
[3027.08 → 3027.94] the rest of your machine down
[3027.94 → 3029.78] and it takes like an hour
[3029.78 → 3030.72] to do one good clip
[3030.72 → 3031.78] and this way we can crank them out.
[3032.42 → 3033.92] But that automaton
[3033.92 → 3035.32] was worth writing
[3035.32 → 3036.48] because I wrote it once
[3036.48 → 3037.32] and we've used it
[3037.32 → 3037.88] hundreds of times.
[3037.88 → 3038.06] Yeah.
[3038.24 → 3038.56] You know?
[3038.96 → 3040.14] That's amazing.
[3040.44 → 3041.60] Sometimes computers are cool.
[3043.28 → 3044.42] As long as we don't change
[3044.42 → 3045.26] the size of the window
[3045.26 → 3046.22] or whatever.
[3046.72 → 3046.96] You know,
[3046.98 → 3047.72] until it breaks
[3047.72 → 3048.94] and then I'll be cursing it again.
[3049.06 → 3049.26] Yeah.
[3050.20 → 3051.08] So did you have to write
[3051.08 → 3052.34] a lot of Apple script for that
[3052.34 → 3054.52] or was it more of like
[3054.52 → 3056.02] recording macros type thing?
[3056.02 → 3058.44] I have the Apple script here
[3058.44 → 3059.74] at the end of the day.
[3059.84 → 3060.38] It's probably like
[3060.38 → 3062.08] 100, 150 lines.
[3062.34 → 3062.58] Okay.
[3062.96 → 3064.04] But getting to those lines,
[3064.28 → 3064.42] right?
[3064.48 → 3064.60] Yeah.
[3064.60 → 3065.48] Like I wrote probably
[3065.48 → 3066.24] a thousand lines
[3066.24 → 3067.14] to get to the 150.
[3067.40 → 3067.54] Yeah.
[3067.64 → 3068.04] Because there's like
[3068.04 → 3069.26] certain ways you access
[3069.26 → 3070.86] the keynote object
[3070.86 → 3071.64] and you can like
[3071.64 → 3073.00] instruct it to do things
[3073.00 → 3073.98] and then pass it the data
[3073.98 → 3074.58] but that's not the way.
[3074.58 → 3075.28] And every time
[3075.28 → 3076.04] that you change it
[3076.04 → 3076.58] you have to like
[3076.58 → 3077.34] run through,
[3077.96 → 3078.26] you know,
[3078.30 → 3079.38] there's no automated test suite
[3079.38 → 3080.20] where I can just hit
[3080.20 → 3081.72] compile and run.
[3082.08 → 3082.22] You know?
[3082.40 → 3082.86] You have to like,
[3083.38 → 3084.38] so it took a long time
[3084.38 → 3085.20] but I think it's not
[3085.20 → 3086.14] very much Apple script
[3086.14 → 3087.98] and there are built in things
[3087.98 → 3089.86] for like parsing a text file.
[3090.08 → 3090.70] Not parsing it
[3090.70 → 3092.04] but ingesting a text file
[3092.04 → 3093.44] and then looping over the lines
[3093.44 → 3095.06] and then just very basic
[3095.06 → 3096.32] regular expression stuff
[3096.32 → 3097.48] to like say
[3097.48 → 3099.24] is this a start of a phrase
[3099.24 → 3100.52] or is this a person's name?
[3101.32 → 3102.12] That kind of stuff.
[3102.92 → 3103.02] So.
[3103.58 → 3103.72] Yeah.
[3103.82 → 3104.20] Nice.
[3105.06 → 3106.32] I tried to write it in JavaScript
[3106.32 → 3107.58] and I just couldn't figure it out.
[3107.68 → 3108.76] It wasn't the JavaScript's fault.
[3108.90 → 3110.62] It was their scripting API.
[3110.98 → 3111.94] Like AppleScript, JavaScript?
[3112.22 → 3112.50] Yeah.
[3112.78 → 3113.58] Like this is written
[3113.58 → 3114.92] in actual AppleScript
[3114.92 → 3116.38] when I was trying to use
[3116.38 → 3117.62] the JavaScript interface.
[3118.14 → 3119.28] The documentation just didn't,
[3119.36 → 3119.58] it was,
[3120.60 → 3121.72] I just couldn't figure it out.
[3121.76 → 3122.02] So I was like,
[3122.08 → 3122.24] well,
[3122.78 → 3123.88] the AppleScript documentation
[3123.88 → 3124.82] is actually better.
[3125.24 → 3126.40] So that's going to be the difference
[3126.40 → 3127.10] even though the language
[3127.10 → 3128.06] is just terrible.
[3128.48 → 3129.60] Tell this to do that.
[3129.70 → 3129.86] Like,
[3129.92 → 3130.48] it's like weird.
[3131.34 → 3131.72] Anyway,
[3131.86 → 3132.64] Keyboard Maestro,
[3132.90 → 3133.66] shout out to that
[3133.66 → 3135.22] and shout out to Hacked.
[3135.92 → 3138.52] That's our show for this week.
[3138.56 → 3140.64] We have a couple of cool episodes
[3140.64 → 3141.72] coming down the pipeline.
[3142.06 → 3142.64] Next week,
[3142.66 → 3143.44] we're going to have
[3143.44 → 3145.44] the author of HTMX
[3145.44 → 3146.92] come on the show.
[3147.02 → 3147.70] This is a
[3147.70 → 3150.40] HTML over the wire solution.
[3150.40 → 3152.32] So similar to like Alpine
[3152.32 → 3153.84] or Live wire,
[3154.06 → 3154.50] excuse me,
[3154.82 → 3155.78] Phoenix Live View
[3155.78 → 3157.32] and Basecamp's new
[3157.32 → 3158.44] Hotwire stuff.
[3158.44 → 3160.16] So HTMX author
[3160.16 → 3160.82] is going to be on.
[3161.16 → 3161.78] We're also going to be back
[3161.78 → 3162.74] for that one as well.
[3162.92 → 3163.94] We also have Jen Creighton
[3163.94 → 3164.62] coming up soon.
[3165.20 → 3165.88] She is the host
[3165.88 → 3167.32] of the Single Threaded podcast.
[3168.02 → 3169.74] So stay tuned for that one
[3169.74 → 3171.10] and other cool things
[3171.10 → 3171.78] that I can't think of
[3171.78 → 3172.74] off the top of my head.
[3173.26 → 3174.22] But we appreciate you
[3174.22 → 3174.82] hanging out with us.
[3174.90 → 3176.18] If you liked Headlines,
[3176.32 → 3176.96] let us know
[3176.96 → 3178.10] because that's the only way
[3178.10 → 3178.64] we'll do it again
[3178.64 → 3179.76] is if people say,
[3179.88 → 3180.00] yeah,
[3180.10 → 3180.54] do it again.
[3180.60 → 3180.98] Otherwise,
[3181.52 → 3182.32] it was a one hit wonder.
[3183.12 → 3183.72] And yeah,
[3184.12 → 3185.38] that's Jay's Party for this week.
[3185.46 → 3186.18] We'll talk to you next time.
[3186.88 → 3187.34] See ya.
[3187.34 → 3191.78] Thank you for listening
[3191.78 → 3192.48] to Jay's Party.
[3192.66 → 3193.52] We appreciate you
[3193.52 → 3194.58] spending your time with us.
[3194.88 → 3196.06] If you dig what we're putting out,
[3196.20 → 3197.30] please do tell a friend
[3197.30 → 3197.96] about the show.
[3198.38 → 3199.34] Personal recommendations
[3199.34 → 3200.70] are the number one way
[3200.70 → 3202.08] people find new podcasts
[3202.08 → 3202.70] they love.
[3203.08 → 3204.38] This episode was hosted
[3204.38 → 3205.72] and produced by me,
[3205.86 → 3206.38] Jared Santo.
[3206.66 → 3207.74] So I'm the guy to blame.
[3207.98 → 3208.40] But seriously,
[3208.50 → 3209.34] you should probably blame Nick.
[3209.78 → 3210.54] It's all Nick's fault.
[3210.90 → 3212.10] The music was produced
[3212.10 → 3213.66] by our beat-freaking-residence,
[3214.00 → 3214.80] Break master Cylinder.
[3215.32 → 3216.46] Jay's Party is brought to you
[3216.46 → 3217.54] by awesome sponsors.
[3217.88 → 3218.80] Check out Vastly,
[3219.16 → 3219.50] Linde,
[3219.62 → 3220.52] and Launch Darkly.
[3220.98 → 3222.48] Next up on Jay's Party,
[3222.82 → 3223.94] for Ross and me,
[3224.16 → 3225.02] invite Carson
[3225.02 → 3226.12] from Big Sky Software
[3226.12 → 3226.78] to the show.
[3226.90 → 3228.12] We're talking HTMX
[3228.12 → 3229.06] and Hyperscript.
[3229.48 → 3230.46] Stay tuned for that.
[3230.58 → 3231.34] It'll be ready for you
[3231.34 → 3231.98] next week.
[3231.98 → 3236.40] reading the ECMAScript
[3236.40 → 3237.64] standard literally
[3237.64 → 3238.92] changed my life.
[3239.46 → 3240.66] Like most people.
[3240.66 → 3242.40] Game on!
