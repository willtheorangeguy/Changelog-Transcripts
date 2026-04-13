[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.40 --> 17.94]  This episode is brought to you by TopTow,
[18.04 --> 20.48]  freelance development jobs for world-class engineers.
[20.88 --> 25.12]  This message is specifically for our listeners who prefer the freelance lifestyle.
[25.46 --> 28.24]  TopTow gives you the ability to work on freelance development jobs
[28.24 --> 32.38]  and projects with top clients who understand the value of elite engineering talent.
[32.76 --> 35.18]  Work with leading organizations at the rate you decide,
[35.52 --> 37.26]  be in control of your own schedule,
[37.62 --> 42.42]  and get plugged into support from a community of experts in the TopTow global network.
[42.72 --> 44.68]  TopTow handles all billing and invoicing,
[44.84 --> 46.64]  letting you fully focus on your engagements
[46.64 --> 50.36]  without negotiating terms with clients or bidding against other developers.
[50.92 --> 53.46]  TopTow is also 100% remote,
[53.46 --> 55.52]  which means you get to design your own lifestyle
[55.52 --> 57.60]  and choose projects that fit your career ambitions.
[57.60 --> 60.22]  If you're ready for an exciting remote work lifestyle,
[60.40 --> 63.70]  take the next step by joining TopTow at TopTowjobs.com.
[63.90 --> 65.92]  Again, TopTowjobs.com.
[76.92 --> 78.44]  Welcome to JS Party,
[78.62 --> 81.58]  a weekly celebration of JavaScript and the web.
[81.58 --> 83.14]  It is conference season,
[83.34 --> 86.60]  and we love packing up our mics and joining in on the fun.
[86.60 --> 91.42]  K-Ball flew from all things open directly to JamstackConf in San Francisco
[91.42 --> 93.98]  to chat with Phil Hawksworth and others.
[94.44 --> 95.26]  Let's get to it.
[95.30 --> 96.66]  Here's K-Ball taking it to 11.
[101.28 --> 101.76]  Okay.
[102.34 --> 104.00]  Hello, JS Party people.
[104.12 --> 105.34]  It's me again, K-Ball,
[105.48 --> 108.30]  and I am here at JamstackConf SF.
[108.30 --> 110.12]  I am here with Phil Hawksworth,
[110.12 --> 112.68]  who is a developer experience engineer at Netlify
[112.68 --> 117.36]  and the MC, the host, the man in charge here at JamstackConf.
[117.36 --> 119.12]  Wow, the man in charge is pushing it.
[119.12 --> 121.18]  Other things, that was bang on,
[121.18 --> 123.28]  but man in charge, I wouldn't even dare to claim that.
[123.28 --> 124.68]  But yeah, I get to introduce the people,
[124.68 --> 125.90]  which is a lovely thing.
[125.90 --> 127.12]  You keep things flowing and moving.
[127.12 --> 127.62]  Yes.
[127.62 --> 128.62]  Yeah, exactly.
[128.62 --> 129.44]  Yeah, it's been fun.
[129.44 --> 131.44]  Yeah, it seems like a great conference so far.
[131.44 --> 132.90]  Yeah, I've been delighted.
[132.90 --> 135.34]  I mean, we were expecting it to be a lot of fun.
[135.34 --> 136.86]  You know, we've had, this is the,
[136.86 --> 140.96]  I guess it's the fourth version of this now in just one short year.
[140.96 --> 141.30]  Yeah.
[141.30 --> 142.56]  So it's been happening very quickly.
[142.56 --> 147.44]  But yeah, I was expecting it to be fun because now I got the chance to help curate the content,
[147.44 --> 149.98]  know that we could invite really amazing speakers,
[149.98 --> 155.86]  and then also got this huge privilege of being part of the committee that reviewed all of the papers.
[155.86 --> 159.48]  So we opened it up this year for some of the talks to come through a CFP.
[159.48 --> 160.08]  Yeah.
[160.08 --> 162.54]  And the quality of the submissions has been fantastic.
[162.54 --> 166.00]  So I think we felt pretty confident earlier on that it was going to be a good event.
[166.00 --> 167.66]  But it's been a lot of fun.
[167.66 --> 168.24]  It's been great.
[168.24 --> 168.54]  Yeah.
[168.54 --> 172.16]  Well, the ecosystem around Jamstack is just exploding.
[172.16 --> 172.54]  Right.
[172.54 --> 173.04]  Yeah.
[173.04 --> 174.04]  It's huge.
[174.04 --> 174.68]  It is.
[174.68 --> 176.30]  And it's growing all the time.
[176.30 --> 178.26]  And that's, I think, one of the things that, first of all,
[178.26 --> 183.68]  makes working in Jamstack exciting because there are lots of tools and companies which keep on emerging.
[183.68 --> 187.40]  And they're not things that you then see and say, oh, I wish I was using that.
[187.40 --> 188.64]  I have to ditch what I was doing.
[188.64 --> 190.00]  Often they can be complementary.
[190.00 --> 193.54]  So you start to kind of add more quivers to your bow, if you,
[193.54 --> 195.66]  quivers to your arrow, whatever that expression is.
[196.18 --> 198.66]  So you get more of these tools that you can then leverage.
[199.04 --> 203.16]  But the other aspect of this is that it means that the people who are at this event,
[203.40 --> 205.82]  like the vendors, the sponsors, the people participating,
[206.54 --> 208.66]  we're all kind of digging in the same direction,
[208.86 --> 211.36]  even though some of them are kind of competition for each other.
[211.52 --> 211.72]  Right.
[211.72 --> 215.66]  But everyone is trying to kind of raise the water level.
[215.94 --> 218.12]  So, you know, it's the rising tide, lift all boats kind of thing.
[218.60 --> 221.34]  And so this ecosystem, as you say, is thriving right now.
[221.46 --> 225.52]  So it makes the whole environment a lot of fun to be in.
[225.76 --> 225.94]  Yeah.
[226.04 --> 228.22]  I've been tuning in a lot to this recently,
[228.36 --> 232.46]  but I know some of our listeners may or may not have had the chance to play around with Jamstack.
[232.86 --> 237.74]  And since you literally wrote the book on Jamstack recently published last year, late last year?
[237.82 --> 238.36]  Earlier this year.
[238.36 --> 239.14]  Earlier this year.
[239.14 --> 245.98]  Maybe you can do a great kind of one or two minute explanation of what Jamstack is and why it matters.
[246.10 --> 246.42]  Sure.
[246.54 --> 246.72]  Yeah.
[246.80 --> 250.76]  Well, I'll do my best without reciting an entire book's worth of stuff.
[251.30 --> 255.28]  But I mean, some people might think of, well, is Jamstack the new word for static sites?
[255.74 --> 256.84]  And yeah, kind of.
[256.90 --> 259.32]  But yes and no, because it's much broader than that now.
[259.32 --> 263.10]  I mean, we've been building things with static assets for a really long time.
[263.22 --> 268.18]  You know, before things were dynamic, we were putting files on web servers and serving those directly.
[268.28 --> 269.14]  And that was nice and simple.
[269.62 --> 272.06]  Things got more complicated as we got more dynamic.
[272.26 --> 273.28]  And that's been great.
[273.66 --> 275.74]  But this is kind of a return to simplification.
[275.74 --> 280.76]  And that's possible because the environment, the ecosystem, as you put it, has grown up.
[280.84 --> 283.32]  The tooling around this has gotten so much richer.
[283.94 --> 287.84]  So Jamstack stands, I mean, Jam stands for JavaScript APIs and markup.
[288.04 --> 297.14]  And it really is trying to find a good way to build kind of modern web applications and sites using pre-rendered markup and served without web servers.
[297.14 --> 300.88]  And that sounds really counterintuitive, the served without web service things.
[301.66 --> 310.30]  Because really, one of the huge attributes of Jamstack sites is that since they're pre-generated, pre-rendered, you can serve them in their entirety from a CDN.
[310.84 --> 312.88]  So, I mean, realistically, they're very portable.
[313.04 --> 314.24]  You could serve them from anything.
[314.42 --> 317.46]  You know, you pre-render a bunch of assets and you put them wherever is convenient.
[317.92 --> 319.22]  That's a really portable, nice thing.
[319.62 --> 323.62]  But their superpower is that they can be entirely served from a CDN.
[323.62 --> 329.16]  And so whereas previously you might have thought, well, I'll pre-generate some of the things, but I'll have some dynamic aspects as well.
[329.56 --> 331.68]  Some of my things I can put on a CDN.
[332.12 --> 335.56]  You've got to manage that slight headache of what goes to the CDN when?
[335.72 --> 337.16]  How do I update all of these things?
[337.22 --> 339.12]  And you're in kind of mixed territory.
[339.38 --> 339.58]  Yeah.
[339.58 --> 345.80]  With a Jamstack site, every deploy is a deployable, immutable, atomic deployment.
[346.02 --> 348.56]  It's this set of assets that you can put directly to the CDN.
[348.56 --> 354.94]  And the lovely thing about that is that now there's all this tooling that's popping up to make that deployment process as simple as possible.
[355.04 --> 357.14]  So it unlocks all kinds of crazy possibilities.
[357.56 --> 357.72]  Yeah.
[357.88 --> 361.02]  It's part of a couple really interesting trends going on.
[361.14 --> 366.84]  We've got these ideas around how much can we pre-compute so we don't have to ship as much stuff over the wire.
[367.50 --> 370.38]  And then these ideas about how far out can we put things?
[370.38 --> 379.90]  How close to the edge can things be so that if I'm in Latin America or in Africa on a slow network connection, I can still get it lightning fast.
[380.14 --> 380.30]  Exactly.
[380.78 --> 383.18]  And, yeah, I mean, you struck upon it perfectly there.
[383.26 --> 388.88]  I mean, we talk about decoupling a lot, you know, where there's like headless CMS and you hear the word decoupled quite a lot.
[389.68 --> 398.40]  Ultimately, for me, it's this ability to put some distance between the complexity, you know, the cogs turning to generate the view of a site and the user who's consuming it.
[398.40 --> 403.70]  And I like the complexity to happen kind of in my house, you know, not in the user's house.
[403.82 --> 408.02]  Where you have control and it's on your timeline and they're not waiting for that to happen.
[408.16 --> 408.74]  Yeah, exactly.
[408.82 --> 419.34]  So if you can do all of that work ahead of time and then when the user comes along, all of that work's done, it gives you the chance to have this great performance and resilience as well.
[419.86 --> 425.34]  And as you mentioned, you know, getting things close to the edge and the right edge, you know, the correct place where the user is.
[425.54 --> 425.70]  Yeah.
[425.98 --> 427.52]  That's what CDNs are great at.
[427.52 --> 434.68]  So if we can get content out there with low friction, like nice and easy, then, you know, that just is wonderful for performance.
[435.12 --> 435.26]  Yeah.
[435.46 --> 437.92]  It also has some fun security benefits and other things.
[438.04 --> 439.52]  I invited people on.
[439.66 --> 444.56]  I this may have been a mistake, but I invited people on the show a while back to try to hack my website.
[444.88 --> 445.32]  Okay.
[445.88 --> 446.32]  Which.
[447.38 --> 448.44]  It's a static site.
[448.58 --> 448.82]  Okay.
[449.02 --> 449.14]  Yeah.
[449.14 --> 451.82]  It's a, it's a jam stack essentially.
[452.08 --> 452.18]  Right.
[452.30 --> 455.80]  Though it is deployed on a traditional virtual server.
[455.80 --> 457.80]  Which my new site is now on Netlify.
[458.10 --> 458.32]  Oh, it is?
[458.32 --> 460.10]  I'll invite them to hack that all day long.
[460.74 --> 462.06]  That doesn't even scare me.
[462.28 --> 462.48]  Yeah.
[462.82 --> 463.62]  Well, that's, I mean, that's the thing.
[463.84 --> 472.26]  I sometimes when I talk about Jamstack, I have this diagram where I kind of compare the traditional or a dynamic stack and all of the lines and boxes that are in there, the bits of infrastructure.
[472.26 --> 475.36]  And then a Jamstack site, which is served directly from the CDN.
[475.92 --> 482.98]  And it kind of, I mean, it's a bit of an oversimplification, but it does show, you know, how much, how much complexity there is in one versus the other.
[483.34 --> 488.88]  And, you know, I sometimes kind of make this slightly smart ass comment that there's no server more secure than the one that doesn't exist.
[489.20 --> 489.40]  Yes.
[489.46 --> 494.58]  If you take infrastructure out of the equation, there's less like surface area to attack.
[494.70 --> 499.66]  There's less things to, or fewer things to kind of have to scale, fewer things to deploy to.
[499.66 --> 507.14]  All of these moving parts, if you can get them out of the equation, it just makes everything go much faster and, as you say, much more secure.
[507.26 --> 510.54]  So I love the fact that you're encouraging people to try and hack your site on Netlify.
[511.04 --> 514.96]  I should introduce you to our infrastructure team around the corner and see if they raise an eyebrow.
[515.56 --> 518.10]  But no, I think you make exactly the right point.
[518.22 --> 529.06]  You know, if it's static, if it's pre-generated and it's removed from the complexity of where, you know, your handle is cranked to generate that thing in the first place, then the attack vectors are just removed.
[529.06 --> 530.66]  Yeah, there's no way to get to it.
[530.78 --> 531.08]  Exactly.
[531.82 --> 533.72]  What are some of the other benefits that you highlight?
[533.78 --> 535.78]  So we talked about performance, getting it out there.
[535.84 --> 537.02]  We talked about security.
[537.22 --> 537.40]  Yes.
[539.42 --> 541.08]  Where complexity is living.
[541.30 --> 541.48]  Yes.
[541.54 --> 543.40]  What else do you highlight when you're talking to folks?
[543.48 --> 548.16]  Well, one of the things that I think is a real benefit, and this is one of the things that actually led me to it in the first place.
[548.24 --> 550.68]  I used to work a large digital agency.
[551.44 --> 557.22]  And so the projects were often quite complicated, working with, you know, big brands who have lots of infrastructure and what have you.
[557.84 --> 565.26]  This approach, aside from having those other benefits you mentioned, actually really increases or reduces, rather, the time to market.
[565.58 --> 574.16]  The time to actually develop these things can be far reduced because, again, you're simplifying, you know, every bit of that lead time, every bit of that process.
[574.16 --> 581.36]  So you take out some of the maybe the more exotic skills and the exotic complexity and technologies in that stack.
[581.56 --> 585.54]  I no longer have to manage Kubernetes and my hosting and my this and my that.
[585.66 --> 585.94]  Exactly.
[585.94 --> 587.12]  I just push a site.
[587.30 --> 590.06]  Kubernetes is a wonderful thing, but I never want to have to deal with it.
[590.18 --> 594.94]  You know, in the background of the infrastructure and things like Netlify, that all exists, but I never need to touch it.
[595.02 --> 595.62]  Thank you very much.
[595.62 --> 600.56]  So it means that we can find developers who are really talented at front end things.
[600.74 --> 612.04]  You know, we can find talented front end engineers with JavaScript, HTML, CSS skills, brilliant SVG animators, all of those kind of people who can now become so much more empowered and have much more impact.
[612.46 --> 621.22]  You know, we don't have to worry about them shoehorning their technologies and their kind of code into the output of some other kind of big monolith, which sometimes can be a bit of a frustration.
[621.22 --> 630.52]  So it kind of takes the shackles off a little bit and it means that engineers can be so much more impactful and so much more rapid about it.
[630.90 --> 640.22]  And when you start to pull at that particular thread, it means that we can start building things that we can put in front of clients in a realistic way much sooner.
[640.80 --> 644.80]  You know, we can start to share the work as it's being developed in a real context.
[645.28 --> 649.82]  And it just increases the kind of confidence in what we're building and reduces lead time.
[649.82 --> 652.68]  So it's really kind of an exciting thing as a developer.
[652.86 --> 659.12]  And I know that a lot of people here at the conference are developers who are enthusiastic because they enjoy the experience of building in this way.
[669.72 --> 672.96]  This episode is brought to you by Linode, our cloud server of choice.
[673.14 --> 675.10]  It is so easy to get started with Linode.
[675.46 --> 677.32]  Servers start at just five bucks a month.
[677.32 --> 680.56]  We host Changelog on Linode cloud servers and we love it.
[680.68 --> 682.38]  We get great 24-7 support.
[682.70 --> 685.32]  Zeus-like powers with native SSDs.
[685.48 --> 690.70]  A super fast 40 gigabit per second network and incredibly fast CPUs for processing.
[691.16 --> 693.26]  And we trust Linode because they keep it fast.
[693.42 --> 694.36]  They keep it simple.
[694.74 --> 697.12]  Check them out at linode.com slash Changelog.
[697.12 --> 710.90]  So let's talk about a little bit about the A in the Jamstack.
[710.90 --> 715.52]  Because what we've talked about a lot here is the J, the JavaScript, and M, the markup.
[715.68 --> 718.42]  And we can do some things in a pre-computed way.
[718.42 --> 723.88]  I could move my CMS from being in WordPress to being in Git or something like that.
[724.38 --> 732.32]  But sometimes you still do need some sort of interaction, interactivity, authentication, things like that.
[732.46 --> 734.06]  So how does that play in?
[734.44 --> 735.76]  Well, I mean, that's such an excellent question.
[735.98 --> 738.46]  And actually, you remind me of a very important point.
[738.46 --> 744.28]  And that is that even though there's the J, the A, and the M in Jamstack, you don't need to use all three.
[744.54 --> 748.22]  In the same way as you might be building on the LAMP stack, but actually you didn't use a database.
[748.50 --> 753.90]  You might not have been using MySQL, but you're still kind of on the LAMP stack if you're using those other technologies.
[754.40 --> 756.58]  That's very much the case with Jamstack as well.
[756.66 --> 763.22]  Because I consider a site that maybe doesn't hit any APIs or maybe doesn't have any JavaScript at all.
[763.62 --> 764.60]  But it's pre-rendered.
[764.66 --> 765.60]  It's served from a CDN.
[765.74 --> 768.34]  That fits perfectly for me into the Jamstack kind of world.
[768.94 --> 774.82]  However, when you're talking about APIs and the things that you might want to kind of leverage there, the world's your oyster a little bit.
[775.02 --> 775.14]  Right?
[775.20 --> 785.90]  Because you can be calling APIs, maybe getting content from content services or pricing engines or goodness knows what else, like image optimization services like Cloudinary.
[785.90 --> 790.02]  You can be pulling content in through those APIs at build time if you want.
[790.12 --> 793.06]  So you kind of compile things and you're consuming APIs then.
[793.58 --> 794.84]  And then pre-rendering everything.
[794.84 --> 800.14]  And then maybe serving things that have no JavaScript and no API kind of usage in the front end.
[800.14 --> 803.34]  Or you can kind of push the lever a little bit further.
[803.50 --> 804.38]  And maybe you're doing that.
[804.46 --> 811.68]  But maybe you're wanting to add some interactions with some third-party services from the front end that make sense to happen at interaction time.
[811.68 --> 820.28]  And that's when JavaScript and APIs start to come into play where you can use things like progressive enhancement to start to say, okay, now we've got this level of interactivity.
[820.48 --> 824.18]  And we can be calling on this huge suite of content APIs or other services.
[824.46 --> 826.50]  And they're just popping up all the time now.
[826.64 --> 828.68]  You know, it's becoming so much more popular.
[828.68 --> 832.54]  And I really think it's kind of inheriting a superpower.
[833.04 --> 839.90]  Because in the same way that you didn't want to be managing Kubernetes, I don't want to be managing authentication services.
[840.12 --> 840.82]  I'll screw that up.
[841.06 --> 843.88]  You know, I don't want to be managing database services for the same reason.
[844.44 --> 848.88]  So being able to have vendors and services that provide that through APIs.
[849.14 --> 851.10]  And they've got teams who specialize in just that.
[851.44 --> 854.46]  And they've got SLAs that say, this is going to be the uptime for this.
[854.52 --> 855.80]  This is how secure it's going to be.
[855.80 --> 858.22]  They've got, you know, expertise there.
[859.04 --> 867.54]  You get to onboard that through using their APIs without having to become an expert in the kind of the deeper kind of gnarly business under the covers of that.
[867.68 --> 870.20]  And just get to be proficient in using their APIs.
[870.68 --> 873.18]  And that's just like inheriting these superpowers.
[873.34 --> 874.68]  And that excites me a great deal.
[875.02 --> 875.16]  Yeah.
[875.44 --> 875.60]  Yeah.
[875.64 --> 877.44]  So there are two pieces of that that I'd love to dig in.
[877.44 --> 884.78]  So one that I think is really insightful and really important is the APIs don't have to be at client side.
[885.10 --> 885.16]  Right?
[885.16 --> 886.52]  Like, I love the idea.
[886.72 --> 888.98]  And I think Gatsby's probably gone the furthest in the direction.
[888.98 --> 896.06]  But having essentially a data pipeline that happens at build time where we may be storing these things in a database somewhere.
[896.30 --> 900.70]  But we can pre-compute and pre-fetch and sort of use that to generate our outcome.
[900.86 --> 900.92]  Yeah.
[901.44 --> 907.10]  And so as you say, like, the user doesn't have to see that complexity or that time lag or anything along those lines.
[907.22 --> 907.32]  Yeah.
[907.32 --> 909.82]  So there's a ton there.
[909.88 --> 915.36]  And I'd be curious your thoughts on the direction that's going and where the boundaries of that are.
[915.36 --> 924.14]  And it's such a tricky one because there are so many wonderful tools available to us now that do incredibly powerful things client side.
[924.70 --> 929.10]  You know, and there's so many JavaScript frameworks and libraries that do really powerful and exciting things.
[929.10 --> 931.12]  And it's tempting to use them for everything.
[931.46 --> 931.54]  Yep.
[931.54 --> 934.04]  And I'm a big fan of all of those.
[934.26 --> 940.98]  But I think one of the most important skills is in knowing how to choose when to use what.
[941.34 --> 941.42]  Yeah.
[941.42 --> 944.52]  So I'm a bit of an old web hippie.
[945.34 --> 949.04]  You know, I'm traditional about I like meaningful URLs.
[949.36 --> 953.00]  I like getting things off the render path as much as possible.
[953.58 --> 953.68]  Yeah.
[954.04 --> 957.74]  Just do as much as you can up front is kind of where I start from.
[958.06 --> 962.06]  And I think that's a really kind of sensible place to begin.
[962.36 --> 968.22]  You know, how much can we do ahead of time so we don't have to do it later is a great way to approach it.
[968.22 --> 972.16]  But then you still have the ability to enhance things later on.
[973.10 --> 979.20]  And I think on projects that I've worked in years ago when I'd be working on maybe a traditional stack,
[980.06 --> 983.08]  you just assumed that everything was going to be dynamic by default.
[983.28 --> 985.92]  You know, we're going to be, cogs would be turning at request time always.
[986.50 --> 988.62]  But then as you start to think, well, how can we scale it?
[988.70 --> 991.38]  How can we make it more resilient and all those things?
[991.80 --> 995.46]  You start to look for opportunities of things that, oh, maybe I can take that and make that static
[995.46 --> 998.14]  and, you know, start to cache certain things and what have you.
[998.48 --> 999.28]  And you start to do that.
[999.96 --> 1005.80]  But that does leave you in the position where you have to figure out what's dynamic and what's static all the time.
[1006.12 --> 1006.24]  Yeah.
[1006.28 --> 1008.06]  You know, and you have to figure out how you balance those two.
[1008.44 --> 1013.38]  So what I prefer to do is invert that and say, okay, this project will be static.
[1013.64 --> 1017.84]  It will be, and by static, I mean pre-generated and then served from a CDN.
[1018.02 --> 1019.38]  And that's going to be my default.
[1019.38 --> 1022.04]  And then you start to think about every feature.
[1022.72 --> 1025.02]  Can this work in that way or can it not?
[1025.02 --> 1033.18]  And it's amazing when you start thinking of it that way, how many kind of creative ways you can find to, oh, actually, I can pre-generate this.
[1033.32 --> 1038.00]  Because the friction in pre-generating is so low now that I can do that many, many times.
[1038.08 --> 1039.16]  I can do it quite frequently.
[1039.16 --> 1044.62]  And so that takes you much further to something that feels kind of, I'm doing the air quotes, dynamic.
[1046.22 --> 1050.06]  But eventually you sometimes hit something that, oh, actually, now it does need to be dynamic.
[1050.32 --> 1054.30]  And until you reach that boundary, there's no point to make something dynamic.
[1054.46 --> 1058.00]  It's much better, I think, to make it pre-generated and as much as possible.
[1058.00 --> 1059.60]  Yeah, so where's the boundary?
[1059.88 --> 1064.70]  I mean, the one obvious one I can think of is essentially logged in experiences.
[1065.02 --> 1069.00]  Place where you only have access to content if you have authenticated in some way.
[1069.12 --> 1074.52]  Though I do find myself wondering, are there ways to pre-generate some of even that?
[1074.74 --> 1077.02]  Yeah, and I absolutely think there are.
[1077.44 --> 1083.98]  But that moment of authenticating, that's the perfect kind of place to start to think about using JavaScript and APIs.
[1083.98 --> 1087.80]  And again, there are these services now that we don't have to roll our own.
[1087.92 --> 1102.08]  There are identity providers, identity services, authentication providers that you can use with things like JavaScript web tokens and different authentication kind of methods that can then unlock either access to routes to things that have been pre-generated.
[1102.18 --> 1103.02]  That's a common path.
[1103.48 --> 1110.56]  Because sometimes you and I might visit a URL and after authenticating, get things that are personalized just to us.
[1110.56 --> 1117.40]  And maybe those have been generated at request time or embellished at request time through some kind of progressive enhancement.
[1118.20 --> 1131.30]  But you might equally find that you and I might visit the same URL which is private and maybe has targeted content for us after we've logged in rather than very individual content.
[1131.30 --> 1131.74]  Right.
[1131.94 --> 1140.24]  So in that case, you can start segmenting the content, pre-generating that, and then all you're doing, and I should be careful saying all you're doing and using words like just.
[1140.92 --> 1148.70]  But what's happening there is you're doing the authentication that then allows people access to the URLs which will be pre-generated for them.
[1148.84 --> 1152.04]  So that is content that is not personalized but is gated, essentially.
[1152.04 --> 1152.76]  Exactly, yeah.
[1152.88 --> 1153.64]  And targeted.
[1153.98 --> 1164.24]  So there's this spectrum, isn't there, of personalization, whether it's localized, translated, internationalized, segmented, right the way down to personal.
[1164.76 --> 1164.92]  Yeah.
[1165.10 --> 1170.70]  And so it's another one of these scenarios where it's a use case thing.
[1170.70 --> 1176.54]  And it's very easy to default to, oh, well, it's targeted content, so it has to be dynamic.
[1177.16 --> 1185.54]  But if you look at your project closely, often you'll find that, well, the level of personalization is actually maybe six different variants or something of that nature.
[1185.70 --> 1185.94]  Right.
[1186.14 --> 1187.26]  Well, I can pre-generate that.
[1187.52 --> 1195.34]  And then I can have the authentication and the routing be something which is dynamic and happening at request time through JavaScript and APIs.
[1195.90 --> 1198.16]  And that's a path that we see very, very often.
[1198.16 --> 1204.14]  Yeah, so, okay, to dive into that specifically, mostly because I want it right now.
[1204.34 --> 1207.10]  Like, that's something I am looking at right now with my new site.
[1207.20 --> 1208.46]  How do I handle this case?
[1208.92 --> 1216.70]  So if I'm using, for example, Netlify, and I'm asking you Netlify, not just because that's what you represent, but because that's what I'm using and it's freaking amazing.
[1216.78 --> 1217.06]  You're right.
[1218.02 --> 1220.60]  How would I do that sort of gated route?
[1221.34 --> 1221.56]  Right.
[1221.72 --> 1224.44]  So that's, I mean, there's a number of options for you there.
[1224.44 --> 1229.92]  I don't want to turn this into a Netlify advert, but what the heck, I'm closer to that than other things.
[1230.42 --> 1233.52]  So Netlify do provide an identity service.
[1233.66 --> 1233.82]  Yeah.
[1233.82 --> 1238.10]  So that you can turn that on and you can start to introduce gates through to your content.
[1238.54 --> 1244.98]  And that can leverage a bunch of different identity providers as well, or you can use one that's rolled right into Netlify.
[1245.48 --> 1255.64]  But that ultimately gives you, for want of a better word, a JavaScript widget that will set an authentication cookie for you at the point you go through that login flow.
[1255.64 --> 1260.08]  And at that point, you can use that to enable access to different parts of the site.
[1260.74 --> 1268.00]  So I know we don't want to just be all in Netlify, but essentially I think of Netlify as I'm pushing up a bunch of files.
[1268.28 --> 1268.38]  Yeah.
[1268.58 --> 1272.08]  Can I specify somehow which of those files require what authentication?
[1272.44 --> 1272.84]  Absolutely.
[1273.04 --> 1273.18]  Yeah.
[1273.22 --> 1273.94]  And you can do that.
[1274.14 --> 1279.46]  So in Netlify land, this is done through, it's such an easily overlooked thing, actually.
[1279.46 --> 1284.04]  But the redirects API in Netlify is really powerful.
[1284.82 --> 1292.00]  So the redirects API, just very briefly, is available to you as a developer through a simple configuration file.
[1292.20 --> 1300.32]  So you can either put it in an underscore redirects file, write as part of your code, which means then, of course, that it's version controlled along with everything else as it evolved.
[1300.92 --> 1304.38]  Version controlled from end to end is just like another superpower.
[1304.78 --> 1304.80]  Yeah.
[1305.08 --> 1305.42]  Exactly.
[1305.54 --> 1305.88]  Holy grail.
[1305.88 --> 1308.10]  How did we survive without it?
[1308.10 --> 1308.30]  Yeah.
[1308.36 --> 1315.30]  And now, yeah, all of my routes that used to be independently managed on my Nginx config or whatever are just living in my code base.
[1315.30 --> 1315.62]  Exactly.
[1315.62 --> 1316.16]  Thank you.
[1316.48 --> 1316.92]  Yeah, exactly.
[1317.08 --> 1318.12]  So they live in there.
[1318.20 --> 1320.46]  Or indeed, you can put them in a Netlify TML file.
[1320.62 --> 1323.60]  Again, same thing, but just organized slightly differently.
[1324.32 --> 1329.00]  In their kind of most basic form, those allow you to specify redirects.
[1329.08 --> 1332.14]  You can say, okay, paths that match this, go to there, please.
[1332.14 --> 1336.80]  And you can also specify things like the HTTP response code.
[1336.80 --> 1340.82]  So I can 301 or 302 things through from one place to another.
[1341.32 --> 1349.46]  I can also specify things like custom 404 handlers at different routes, which is kind of a mind-blowing thing after you've used it for a while.
[1349.46 --> 1353.02]  Because it means that, yes, you have a default 404.
[1353.40 --> 1361.26]  But at particular parts of your site, maybe you've had a flash sale or there are certain things that are open or available at certain times.
[1361.48 --> 1361.70]  Right.
[1361.70 --> 1365.34]  If those go away, you can 404 things there and handle that differently.
[1365.62 --> 1365.78]  Right.
[1365.88 --> 1367.30]  So you can display different messages.
[1367.52 --> 1369.86]  Or you can even redirect those to other things.
[1370.00 --> 1372.16]  And it gets kind of gnarly and fun.
[1372.68 --> 1379.86]  But the other thing that happens in this redirects API is that we can conditionally set authentication rules there.
[1379.86 --> 1388.82]  So you can say, for this path, someone arriving at this URL, they have to have been authenticated with this kind of a role before they come through.
[1389.26 --> 1392.90]  And then it's the job of the authentication widget to allow and specify that role.
[1393.14 --> 1396.84]  So it all lives in there and it's kind of programmatically controllable.
[1397.14 --> 1401.34]  But ultimately you're creating content and then giving people access conditionally to it.
[1401.48 --> 1401.78]  Got it.
[1401.82 --> 1407.56]  So in the redirects, you would say, essentially, if they have this type of role, let them through, otherwise redirect?
[1407.56 --> 1408.00]  Exactly.
[1408.00 --> 1408.58]  Or, okay.
[1408.62 --> 1408.94]  Exactly.
[1409.22 --> 1409.64]  Brilliant.
[1409.64 --> 1410.22]  Exactly so.
[1411.08 --> 1416.30]  And that redirects API also does things like localization and internationalization.
[1416.60 --> 1420.46]  So we can, we just kind of, we don't want to put everything in there.
[1420.46 --> 1423.58]  So you've got like user agent sniffing or anything like that.
[1423.68 --> 1432.94]  But we can absolutely conditionally do things differently depending on people's language settings or their locale, which is great for things like localized sites.
[1433.38 --> 1433.60]  Yeah.
[1433.60 --> 1439.46]  So you pre-generate with your static site generator, all of your content in all of the languages that you want.
[1439.84 --> 1447.00]  And then you can route people based on where they are or their language settings to those routes as they request it.
[1447.12 --> 1458.32]  And all of that redirection is happening at the edge, at the CDN kind of nodes, which is why internally at Netlify, we actually refer to our CDN as the ADN, the application delivery network.
[1458.32 --> 1458.60]  Right.
[1458.72 --> 1462.84]  Just because it has that kind of extra slight bit of logic that you can start to build applications on.
[1463.08 --> 1464.46]  So it's been interesting.
[1464.68 --> 1466.54]  Well, and that's a, that's a topic that I want to dig in more.
[1466.90 --> 1468.94]  Everything you say, I'm like, oh, I want to dig more of that.
[1468.94 --> 1469.16]  Yeah.
[1469.16 --> 1489.68]  This episode is brought to you by Codacy.
[1489.68 --> 1497.92]  Codacy helps developers and teams automate and standardize their code quality by instantly identifying issues through static code analysis.
[1497.92 --> 1508.04]  With Codacy, you get notified on security and complexity issues, gaps in coverage and code duplication for every commit and pull request directly from your current Git workflow.
[1508.48 --> 1510.82]  Identify OWASP top 10 vulnerabilities.
[1511.32 --> 1518.38]  Ensure code quality is standardized across all teams and projects by applying code patterns and customizing parameters.
[1518.90 --> 1521.94]  Get visibility into your technical debt and so much more.
[1521.94 --> 1533.10]  With 30 supported languages and counting, you have options to use the cloud service or go self-hosted to bring Codacy behind your firewall with support for GitHub Enterprise, Bitbucket Server, and GitLab.
[1533.46 --> 1539.70]  Learn more, get started for free, and grab a sweet pair of Codacy socks at changelaw.com slash Codacy.
[1539.94 --> 1541.94]  Again, changelaw.com slash Codacy.
[1541.94 --> 1571.92]  One of the big questions in my mind is essentially how much can we push it?
[1571.92 --> 1572.64]  What can we push out to the edge?
[1572.80 --> 1574.02]  What can be there?
[1574.08 --> 1576.20]  Because it's not just content, right?
[1576.20 --> 1577.64]  You can have authentication out there.
[1577.74 --> 1579.42]  You can have some amount of routing out there.
[1580.12 --> 1583.04]  Where I start to run into challenges is what about data?
[1583.40 --> 1589.10]  What about, like, you know, I was chatting with, oh, I'm blanking on his name now, Brian.
[1590.54 --> 1590.98]  Brian.
[1591.08 --> 1591.48]  Brian LaRue?
[1591.68 --> 1592.00]  Yes.
[1592.04 --> 1592.22]  Yes.
[1592.60 --> 1599.60]  LaRue, earlier or yesterday, and we were talking about one of the big challenges is, okay, how do you update data?
[1599.60 --> 1599.64]  Yeah.
[1600.12 --> 1602.08]  In a JAMstack application.
[1602.70 --> 1606.02]  And what pieces of that can live where?
[1606.14 --> 1609.86]  So I kind of want to get your sense on, you know, where's the line?
[1610.00 --> 1611.64]  What can't we push out to the edge?
[1612.34 --> 1612.36]  Yeah.
[1612.36 --> 1612.62]  Yeah.
[1612.70 --> 1613.58]  Oh, that's such a good question.
[1613.82 --> 1617.58]  And, like, dynamic data is a very interesting one, right?
[1617.64 --> 1621.94]  Because, so I'm thinking about, like, Netlify for the context of this.
[1622.06 --> 1624.68]  We don't have our own kind of database service or data store.
[1624.76 --> 1626.46]  That's not the business we want to get into.
[1626.46 --> 1629.46]  We want to be the glue layer that allows you to stitch those things together.
[1629.66 --> 1635.92]  So when it comes to where you stash data and how close to the edge it gets, it kind of depends on the service you end up using.
[1636.14 --> 1638.66]  Some of them are more readily distributable than others.
[1639.30 --> 1643.84]  But very often, you know, there is an origin that you're hitting there.
[1643.94 --> 1644.04]  Yeah.
[1644.04 --> 1646.92]  And so eventually you're going to start to bump into that.
[1647.84 --> 1652.34]  And it really, I hate using the phrase it depends, but it kind of depends.
[1652.84 --> 1652.94]  Yeah.
[1653.06 --> 1653.22]  Yeah.
[1653.24 --> 1658.48]  I mean, some services are in good shape to distribute that and, like, distribute the data around the edge.
[1658.90 --> 1666.34]  And so those requests are themselves being routed through and served by something which is close to where the user is requesting them.
[1666.70 --> 1669.34]  But not all of them have the same kind of profile.
[1669.34 --> 1673.14]  So you're kind of leaning on the provider a little bit there.
[1673.94 --> 1674.30]  Yeah.
[1674.60 --> 1678.24]  Is there anything else that doesn't make sense to push out to the edge?
[1681.06 --> 1682.64]  Well, kind of, I don't know.
[1682.72 --> 1683.24]  I don't know.
[1683.34 --> 1685.32]  I'm focusing so much on trying to do that.
[1685.56 --> 1685.72]  Yeah.
[1686.68 --> 1692.16]  Well, I guess, or flipping that around, as you have pushed more and more things and you come from this perspective of default push it out.
[1692.24 --> 1692.42]  Yeah.
[1692.42 --> 1695.82]  And then ask yourself, is there something that I can't?
[1696.38 --> 1701.20]  Where else have you run into, even if it's not impossible, friction in moving to this paradigm?
[1701.32 --> 1703.60]  I think it's content that updates very, very frequently.
[1704.08 --> 1704.18]  Right.
[1704.30 --> 1713.10]  So when people are keen to do things like push notifications and, like, opening WebSockets and those kind of things, that gets to be a bit more challenging.
[1713.60 --> 1721.40]  You know, when you need to centrally manage state somewhere, that gets to be kind of tricky because, you know, you need some central kind of resource for that.
[1721.40 --> 1723.88]  So that starts to get a little bit more challenging.
[1724.90 --> 1728.34]  I need to level up a little bit on where Lambdas are going.
[1728.66 --> 1732.20]  You know, so, I mean, people ask, Jamstack, is that serverless?
[1732.34 --> 1733.42]  Serverless, is that Jamstack?
[1733.50 --> 1735.74]  And I kind of think of the two as just really good friends.
[1736.38 --> 1737.90]  You know, they're really complementary.
[1738.30 --> 1739.94]  That's one way you can build your A.
[1740.42 --> 1741.04]  Yeah, exactly.
[1741.34 --> 1741.70]  Absolutely.
[1742.00 --> 1742.52]  Yeah, totally.
[1743.20 --> 1744.98]  And there's some fun things you can do with that.
[1744.98 --> 1755.32]  But, yeah, it feels like things like Lambdas are starting to get more powerful for how they can do something approximating sockets and those kind of things.
[1755.52 --> 1756.62]  I need to level up on that.
[1756.70 --> 1758.74]  There are smarter people who can talk about that stuff than I.
[1758.74 --> 1767.78]  But, yeah, anywhere to do with, like, state management gets to sometimes be a little bit tricky when it's something that needs to be unified across a system.
[1768.26 --> 1776.00]  Real-time kind of messaging layers and those kind of things, that gets to be a little bit more, a little bit less of an obvious fit, I think.
[1776.26 --> 1776.40]  Yeah.
[1776.72 --> 1777.64]  Yeah, that makes sense.
[1777.64 --> 1782.36]  Well, and there's kind of an interesting thing when you talk about data updating a lot.
[1782.64 --> 1782.90]  Yes.
[1783.28 --> 1786.44]  Which is incremental builds.
[1786.88 --> 1787.24]  Yeah.
[1787.40 --> 1788.26]  And things around that.
[1788.32 --> 1795.90]  And I feel like that's something that some of the big Jamstack stacks, so to speak, are working towards and saying, okay, how can we do incremental builds?
[1795.90 --> 1796.08]  Yeah.
[1796.64 --> 1806.68]  But that enables a lot more in that because if your data is updating very rapidly but each update only requires you to rebuild a small portion of the site, you're probably fine.
[1806.78 --> 1806.94]  Yeah.
[1806.94 --> 1811.92]  Whereas if each update requires a complete rebuild, it's a little harder.
[1812.06 --> 1812.48]  It's true.
[1812.66 --> 1817.78]  And it's, yeah, lots of people are working on this kind of problem or this challenge, I should say.
[1817.94 --> 1818.10]  Yeah.
[1818.42 --> 1824.72]  But it's absolutely right to call this out as it's kind of a limitation of a pre-generated model, right?
[1824.72 --> 1834.98]  But if you're working on a news organization that has three, four, five million pages, your build's going to get long and latency matters.
[1835.38 --> 1835.48]  Yeah.
[1835.48 --> 1836.94]  Time to publishing matters.
[1837.44 --> 1838.78]  So it's not such a good fit.
[1838.78 --> 1846.28]  So this idea of incremental builds is kind of, I don't want to use the word holy grail, but it certainly is like a very important.
[1846.28 --> 1847.64]  It will unlock a whole nother level.
[1847.86 --> 1848.22]  Exactly.
[1848.44 --> 1849.28]  Of who can use this.
[1849.32 --> 1849.66]  Exactly.
[1849.84 --> 1850.96]  It's a really big deal.
[1850.96 --> 1853.78]  And there are ways that you can creatively get around some of these things.
[1853.78 --> 1860.46]  Again, once you start to stitch together some of the tools that we've got to play with in creative ways, you can work around some of this.
[1860.64 --> 1866.96]  But ultimately, having true incremental builds unlocks all kinds of new things.
[1866.96 --> 1873.28]  Different static site generators strive differently for this and get closer to it than others.
[1873.28 --> 1886.20]  But ultimately, if you're talking about running a build which is going to understand the dependency graph of every URL on there and know if there are related articles or tags that are different.
[1886.20 --> 1890.36]  Or if you make one file change in a template file, it impacts everything.
[1890.70 --> 1894.20]  Understanding that and being able to target the right things to regenerate.
[1895.20 --> 1895.36]  Yep.
[1896.00 --> 1896.90]  That's a big problem.
[1896.90 --> 1898.00]  It's a non-trivial challenge.
[1898.26 --> 1898.32]  Yeah.
[1898.32 --> 1907.28]  And then you get into the realms as well of, well, now if I've solved that, I'm still getting to the point that I need to understand how I cache things between builds.
[1907.70 --> 1908.90]  So this kind of intra-build cache.
[1908.90 --> 1909.76]  Where does that live?
[1909.82 --> 1910.12]  Yeah.
[1910.38 --> 1916.42]  And if you're integrating multiple data sources as well, you've got to manage the dependencies between those.
[1916.60 --> 1916.70]  Right.
[1916.80 --> 1916.98]  Yeah.
[1917.26 --> 1921.28]  So I've been having quite a lot of fun playing with things kind of in this territory a little bit.
[1921.54 --> 1921.64]  Yeah.
[1921.64 --> 1923.90]  Mostly in the kind of what do I cache between builds.
[1924.12 --> 1924.34]  Yeah.
[1924.34 --> 1928.90]  Um, situation because it's kind of a lesser known kind of secret.
[1929.20 --> 1930.14]  Uh, don't tell anyone.
[1930.30 --> 1935.98]  This is between you and I, uh, that, you know, in Netlify, there is a means to cache things between builds.
[1936.26 --> 1940.74]  Now, this is not a thing that we've documented, but we use it and you could use it too.
[1940.96 --> 1941.80]  So for instance.
[1941.82 --> 1942.74]  Okay, where do I find it?
[1942.74 --> 1942.92]  Yeah.
[1943.52 --> 1950.48]  So, uh, so the, the key is that, um, you know, between builds, we, you know, when we, let me explain.
[1950.48 --> 1957.38]  So the first time you run a build of a project on Netlify, we'll install all of your dependencies, um, and then we'll run your build.
[1957.84 --> 1959.52]  Um, we stash those dependencies.
[1959.86 --> 1960.06]  Yeah.
[1960.10 --> 1960.62]  I noticed that.
[1960.72 --> 1960.92]  Yeah.
[1960.94 --> 1962.48]  So that speeds up the subsequent builds.
[1962.64 --> 1964.82]  Ah, so that means you have a caching layer somewhere.
[1965.00 --> 1965.34]  Somewhere.
[1965.66 --> 1965.84]  Yeah.
[1965.84 --> 1969.52]  And the, we very deliberately haven't documented that and exposed that.
[1969.66 --> 1971.92]  We haven't locked it down, but we haven't exposed that.
[1971.92 --> 1980.52]  And the reason we haven't exposed that to everyone is that as soon as you start managing your build, your cache between builds yourself, it's a very easy.
[1980.52 --> 1982.00]  It's really easy to F yourself up.
[1982.02 --> 1982.40]  Exactly.
[1982.90 --> 1986.46]  Uh, and so, you know, it's a very much a kind of a buyer beware kind of scenario.
[1986.70 --> 1986.92]  Right.
[1987.04 --> 1989.28]  However, you absolutely can use that.
[1989.28 --> 1995.66]  And, you know, I built a few kind of proof of concepts, just exploring that a little bit so that I could kind of shard my site.
[1995.66 --> 2001.32]  So I built a site which was a Hugo build, which is already very fast in terms of its generation speed.
[2001.72 --> 2003.36]  Um, but I kind of segmented it.
[2003.40 --> 2007.44]  So I was like, well, I've got a new section and I've got a, I don't know, a blog section.
[2007.66 --> 2012.86]  And so depending on which part of the sites I updated, I ran a slightly different build.
[2013.08 --> 2013.26]  Right.
[2013.32 --> 2017.58]  Um, and then I cached things into this layer between, between the builds.
[2018.44 --> 2020.38]  It's, it's a little bit clunky.
[2020.62 --> 2021.06]  Right.
[2021.06 --> 2022.36]  It's absolutely possible.
[2022.36 --> 2032.60]  And I think once we start seeing ways to ease that use of, of the cash in and out of, uh, in between builds, then this becomes a little bit more approachable.
[2032.78 --> 2040.58]  And the reason I kind of mentioned this now, um, is that just yesterday we announced build plugins for Netlify, um, at, uh, at the conference.
[2040.84 --> 2046.66]  And those allow kind of programmatic access to different parts of the build life cycle.
[2046.74 --> 2052.14]  So whereas before all you could say as well, here's what, here's what I'd like you to execute during the build.
[2052.36 --> 2054.74]  There's lots of things that go on outside of that.
[2054.82 --> 2060.78]  So there's like getting the cash, uh, in initializing the, the build all the way through to the post processing.
[2061.28 --> 2065.40]  Now, what we're going to say is you can write plugins, which are just bits of JavaScript.
[2065.68 --> 2074.04]  They're just node, um, that you can either dispute as NPM modules, or you can keep privately, but ultimately you can hook into different parts of the life cycle.
[2074.04 --> 2078.28]  So one of those, the aspects of that is exposing the cash.
[2078.80 --> 2089.20]  So having a plugin, which could, for example, make requests to where your data sources are and stash those in the cash so that then when your build gets to run, that's already there.
[2089.74 --> 2096.40]  That's really nice because it's, it's convenient, but also it means that we can start to say, we'll cash that for however many seconds you like.
[2096.40 --> 2099.22]  So content that, you know, doesn't update very often.
[2099.48 --> 2101.74]  You don't need to request that every time you run your build.
[2101.94 --> 2105.62]  So we can start to squeeze down the length of the build and kind of optimize for that.
[2105.72 --> 2109.40]  And you can start to do all kinds of things with like getting things in and out of the build cash.
[2109.50 --> 2111.54]  And it's, it's a fun playground.
[2111.54 --> 2113.54]  I'm really, I'm kind of excited about building stuff.
[2113.72 --> 2114.34]  That is really interesting.
[2114.62 --> 2121.04]  Uh, can you, can you, uh, introspect it essentially?
[2121.04 --> 2125.86]  So, so I'm thinking about this problem now of, okay, how would I even go about this?
[2126.22 --> 2127.80]  You know, I'm using a third party framework.
[2128.00 --> 2132.22]  I'm, I just built this new site using Svelte and Sapper and I'm playing around with that, which is super fun.
[2132.30 --> 2135.64]  But I can't pretend to understand all the dependency paths.
[2136.12 --> 2146.64]  Uh, would I be able to, for example, say, okay, let's keep data on which files change and which output files change and sort of map that over time.
[2146.64 --> 2150.92]  So then I can start to drive, derive this dependency graph, right?
[2150.92 --> 2159.84]  Rather than having a, you know, essentially, um, rather than thinking of it top down of I'm going to figure out how to do it.
[2159.90 --> 2165.18]  I'm going to observe it empirically and say, okay, I have observed that these files influence these things.
[2165.26 --> 2165.46]  Yes.
[2165.72 --> 2169.02]  So until I change something about my site structure, I can make these assumptions.
[2169.28 --> 2170.74]  You, I mean, you absolutely could do that.
[2170.80 --> 2173.24]  We're, we're not going to give you the code to do that, but you.
[2173.66 --> 2174.44]  But the hooks are there.
[2174.52 --> 2175.06]  The hooks are there.
[2175.06 --> 2175.10]  Yeah.
[2175.10 --> 2185.28]  So, I mean, so the, the important thing is that if you can write like a JavaScript function to, to consider what, what's changed when, uh, you know, think about what the dependencies are.
[2185.28 --> 2203.50]  If you can inspect that through a JavaScript function that you've written, you can absolutely introduce that into your build logic so that before you actually execute the build, you can, you can have that level of introspection beforehand that says, okay, well, now I need to run this build command or maybe this build command, which is different depending on what's changed.
[2203.50 --> 2205.58]  So, yeah, that's an interesting use case.
[2205.64 --> 2210.08]  You see, every time I talk to someone about build plugins, another idea kind of springs forth.
[2210.58 --> 2216.64]  And, uh, yeah, if, if, if you can build it, you know, it can be run as part of the, the build lifecycle now.
[2216.74 --> 2217.78]  So it's, uh, yeah.
[2217.78 --> 2221.88]  So in that build lifecycle, then can I look at what's in the cache and output it?
[2222.28 --> 2222.56]  Yes.
[2222.76 --> 2222.96]  Okay.
[2223.02 --> 2223.50]  Yeah, you can.
[2223.72 --> 2227.52]  So, cause I wouldn't know yet how to write the final version, right?
[2227.56 --> 2230.30]  But what I'd want to do is first write a observation.
[2230.70 --> 2230.86]  Okay.
[2230.86 --> 2233.02]  Look, these things have changed since my last build.
[2233.02 --> 2234.14]  And here's what's in the cache.
[2234.24 --> 2235.40]  Here's what's after the cache.
[2235.66 --> 2238.56]  So, so this is, I mean, this is still in private beta.
[2238.74 --> 2240.46]  You know, the private beta was just announced yesterday.
[2240.88 --> 2246.84]  Um, but one of the utilities we're absolutely going to have is, um, an easier cache API.
[2247.06 --> 2249.38]  And when I talk about cache, I'm talking about the intra build.
[2249.50 --> 2249.90]  Yeah.
[2249.94 --> 2250.82]  Kind of notify cache.
[2251.18 --> 2255.76]  Um, and so in that way you will be able to inspect what's in there and then take action accordingly.
[2256.26 --> 2258.08]  So, um, so yes, yes.
[2258.08 --> 2261.78]  I expect the plugin to be done and finished by, I don't know what this time tomorrow.
[2261.78 --> 2262.32]  Are you going to build?
[2264.32 --> 2265.64]  Maybe by the time this airs.
[2265.70 --> 2265.88]  Yeah.
[2265.94 --> 2266.14]  Okay.
[2266.26 --> 2266.64]  Fair enough.
[2266.90 --> 2267.84]  But yeah, it's fun.
[2267.94 --> 2269.50]  It's fun stuff to start playing around with.
[2269.58 --> 2274.18]  And, uh, I've, I've seen so many different kind of, uh, bits of imagination used on this,
[2274.24 --> 2278.46]  whether it's like, okay, once I've done my build, I can inspect what's come out of that as well.
[2278.46 --> 2283.54]  So I can maybe do lighthouse test against it and start reporting about that over time.
[2283.70 --> 2284.14]  Yeah.
[2284.14 --> 2285.10]  That excites me.
[2285.20 --> 2290.34]  The idea of not just, um, getting a score for my site, but tracking it over time.
[2290.52 --> 2292.04]  And linking it back to particular commits.
[2292.42 --> 2292.78]  Exactly.
[2293.20 --> 2293.36]  Yeah.
[2293.36 --> 2293.42]  Yeah.
[2293.42 --> 2293.46]  Yeah.
[2293.46 --> 2293.56]  Yeah.
[2293.56 --> 2293.68]  Yeah.
[2293.68 --> 2293.78]  Yeah.
[2293.78 --> 2294.16]  Okay.
[2294.16 --> 2296.92]  Well, you know, our, our performance took a hit here.
[2297.20 --> 2298.18]  What was the cause of that?
[2298.30 --> 2298.48]  Yeah.
[2298.48 --> 2300.90]  And then being able to track that back to a Git commit.
[2301.30 --> 2305.12]  Again, it comes back to this Git all the way to the, you know, from end to end.
[2305.56 --> 2306.94]  So many good opportunities.
[2307.22 --> 2309.96]  So, um, yes, I'm, I'm excited about it.
[2310.02 --> 2310.76]  That's really cool.
[2311.00 --> 2314.24]  Um, I want to be very respectful of your time and you need to get back pretty soon.
[2314.24 --> 2314.98]  I probably do.
[2314.98 --> 2315.16]  Yeah.
[2315.22 --> 2319.58]  Before they need to get another speaker on stage and, uh, and it'll be a free for all.
[2319.76 --> 2319.82]  Okay.
[2319.90 --> 2322.24]  So one final question that I'm going to put out there.
[2322.52 --> 2327.98]  Um, so a lot of what we've talked about in terms of the benefits of the Jamstack are
[2327.98 --> 2331.42]  benefits for developers, benefits for end users.
[2331.42 --> 2331.86]  Uh huh.
[2332.30 --> 2335.62]  One of the areas that I have questions that I know there've been folks at this conference
[2335.62 --> 2340.44]  talking about this is, you know, what about other parts of the business?
[2340.44 --> 2344.22]  So for example, if you're interacting with a marketing department, you're interacting with
[2344.22 --> 2348.64]  a content department, folks who are doing this, folks who are not using Git and having
[2348.64 --> 2349.70]  stuff on there.
[2349.90 --> 2352.12]  Like how developed is that ecosystem?
[2352.34 --> 2356.66]  What still needs to be created there to make this as seamless for them as it is for
[2356.66 --> 2356.84]  us?
[2356.84 --> 2357.72]  Oh, that's a great question.
[2357.72 --> 2360.20]  And it's, it's getting richer and richer all the time.
[2360.20 --> 2364.24]  So when I first started working in this kind of space, I was very enthusiastic about static
[2364.24 --> 2369.96]  site generators and I love writing Markdown and putting some YAML front matter and committing
[2369.96 --> 2372.56]  it to Git and then like doing a little happy dance.
[2372.80 --> 2373.22]  Yeah, it's great.
[2373.58 --> 2377.90]  But a content author never wants to touch Git and frankly, a content author should never
[2377.90 --> 2379.42]  even need to know that Git exists.
[2379.42 --> 2387.90]  So one of the things that kind of came along a bit later were tools like Git based content
[2387.90 --> 2388.66]  management systems.
[2388.66 --> 2393.70]  And one of the talks actually here at the conference was by Sean Ockhart, who's the lead for Netlify
[2393.70 --> 2394.04]  CMS.
[2394.04 --> 2399.36]  And Netlify CMS is by no means the only kind of Git based CMS that exists.
[2399.36 --> 2405.88]  But what tools like that do are aiming to kind of close this gap between writing Markdown
[2405.88 --> 2410.26]  and submitting it to Git and then having your continuous integration do all of its magic.
[2411.00 --> 2415.10]  It's closing that gap between that and the content authoring experience.
[2415.54 --> 2421.66]  So Netlify CMS, for an example, gives you an authoring experience that looks like what
[2421.66 --> 2426.98]  you'd expect, can give you an instant render of what your page will look like because it
[2426.98 --> 2430.64]  can apply the same templates for that page in real time as you're typing.
[2431.50 --> 2435.66]  But behind the scenes, all it's doing is it's poking content into your Git repository.
[2436.20 --> 2439.76]  So as a content author, you're writing content in a structured way.
[2439.92 --> 2441.34]  You're seeing the result immediately.
[2441.96 --> 2448.20]  But when you hit, give me a preview of that, you don't know that it's behind the scenes making
[2448.20 --> 2453.42]  a pull request, pushing that to a repo, making sure that your code, your content is managed
[2453.42 --> 2456.30]  and version controlled with your code, all of those things.
[2456.50 --> 2458.24]  You're just working seamlessly on top of that.
[2458.76 --> 2463.62]  And more and more tools are arriving to kind of make it feel like, oh, it's the context that
[2463.62 --> 2467.18]  I want to work in as an author or a marketing person, what have you.
[2467.54 --> 2468.64]  So that's kind of one example.
[2469.08 --> 2476.72]  But I think another real strength of Jamstack sites is how immediate you can get a real life,
[2476.72 --> 2479.66]  real context preview into the hands of stakeholders.
[2479.98 --> 2480.20]  Yes.
[2480.36 --> 2480.52]  Right.
[2481.44 --> 2482.46]  Branch previews.
[2482.52 --> 2484.38]  We were talking, I was talking about that with Katie earlier.
[2484.50 --> 2485.64]  Like, it's brilliant.
[2485.94 --> 2485.96]  Yeah.
[2485.96 --> 2491.12]  And it's one of those things is when you start using it, you think, how did I do this before?
[2491.36 --> 2492.48]  How did, you know, you just get spoiled.
[2492.48 --> 2496.80]  I have one site doing this and one site that is using old school staging environments or whatever.
[2496.80 --> 2499.74]  And oh my gosh, I just want to get out of that as soon as I can.
[2499.74 --> 2500.18]  Absolutely.
[2500.42 --> 2501.20]  All in the new world.
[2501.42 --> 2501.52]  Yeah.
[2501.52 --> 2506.64]  And it's incredible because there are so many like big, expensive, you know, reassuringly
[2506.64 --> 2511.70]  expensive trusted blue chip products that try and do all of this for you.
[2512.50 --> 2517.22]  And if you want to, you know, if you've got maybe a big expensive CMS and a big, big site
[2517.22 --> 2520.80]  that you're going to roll out, you'll want a production environment and a staging environment
[2520.80 --> 2521.78]  and a QA environment.
[2522.04 --> 2523.42]  And they have to be in lockstep.
[2523.74 --> 2525.78]  You know, they have, they have to be managing things.
[2525.96 --> 2529.66]  Oh, this went out to staging, but then it was disapproved by this person.
[2529.74 --> 2529.86]  Right.
[2529.86 --> 2531.16]  These other things need to go out.
[2531.22 --> 2531.46]  Yeah.
[2531.56 --> 2537.10]  And it's, and since each one of those is infrastructure and it's its own infrastructure, strictly speaking,
[2537.10 --> 2540.58]  that needs to be a perfect facsimile of each other, you know, part of infrastructure.
[2540.76 --> 2544.98]  So that if you do see something in your staging environment, you're a hundred percent confident
[2544.98 --> 2546.62]  that that's how it will behave in production.
[2547.34 --> 2549.58]  Managing those things is difficult.
[2549.78 --> 2551.44]  I think lots of us have been stung by that before.
[2551.64 --> 2555.68]  I worked on projects where it's been many, the lead time to get content deployed.
[2555.86 --> 2558.48]  Content, mind you, not code, has been many, many weeks.
[2558.48 --> 2565.60]  And that's from a dynamic kind of large enterprise kind of piece of software.
[2566.20 --> 2570.70]  The situation we're now in with Jamstack and, you know, lots, many vendors, but I'm particularly
[2570.70 --> 2574.82]  thinking about Netlify here is that, you know, we work on this branch model on Git, right?
[2574.86 --> 2579.26]  So if you want another environment, you create another branch and then those builds go to
[2579.26 --> 2579.78]  that URL.
[2579.78 --> 2582.44]  Realistically, that's all on the same infrastructure.
[2582.86 --> 2587.48]  It's all being served as production, which means that if you see it there, that's how it
[2587.48 --> 2588.04]  will behave.
[2588.16 --> 2588.34]  Yep.
[2588.34 --> 2593.34]  And we're not reinventing methods of forking and branching and creating versions.
[2593.34 --> 2595.96]  We're using something that exists already, which is designed for that.
[2595.96 --> 2596.72]  And that's Git.
[2596.72 --> 2601.82]  So the point that we're happy with what's been deployed onto the production or a feature
[2601.82 --> 2607.14]  branch rather, or a staging branch, happy with that, it gets merged in and your deployment
[2607.14 --> 2607.52]  is done.
[2607.52 --> 2613.26]  So that means that you can create these views of what your feature is, what your latest content
[2613.26 --> 2620.00]  change is, and share that with the URL, a unique URL or a URL for that branch with whoever
[2620.00 --> 2623.78]  needs to see it and be absolutely confident that what they see is what they'll get.
[2624.74 --> 2626.36]  And for me, that's really empowering.
[2626.50 --> 2631.78]  That has reduced the overhead on so many projects that I've worked on in the past and has been,
[2631.96 --> 2636.20]  that's actually been the real aha moment because, yes, developers, we love to have a nicer
[2636.20 --> 2637.88]  developer experience and that's great.
[2638.32 --> 2643.20]  But realistically, the things that really matters is, well, ultimately the users, but
[2643.20 --> 2646.18]  before we get to them, the stakeholders, are they going to be happy?
[2646.64 --> 2649.66]  Are they going to be confident in what they're seeing and give you the thumbs up so you can
[2649.66 --> 2650.40]  get something live?
[2651.12 --> 2657.54]  And increasing the visibility of what you're working on and reducing the lead time and getting
[2657.54 --> 2662.40]  changes that you're working on into the eyes of the people that need to approve it, that's
[2662.40 --> 2662.98]  a game changer.
[2662.98 --> 2666.74]  And so for me, that's one of the superpowers of the JAMstack, I think.
[2667.86 --> 2668.22]  Wonderful.
[2668.38 --> 2669.24]  Thank you so much, Phil.
[2669.34 --> 2669.98]  This has been fun.
[2670.12 --> 2670.74]  Thanks for having me.
[2670.80 --> 2672.22]  It's great to chat.
[2672.40 --> 2673.26]  Yeah, absolutely.
[2675.26 --> 2675.76]  All right.
[2675.80 --> 2677.64]  Thank you for tuning in to JS Party this week.
[2677.78 --> 2680.72]  Tune in live on Thursdays at 1 p.m.
[2680.76 --> 2683.80]  U.S. Eastern at changelog.com slash live.
[2684.20 --> 2686.80]  Join the community and Slack with us in real time during the shows.
[2687.12 --> 2688.60]  Head to changelog.com slash community.
[2688.60 --> 2689.90]  And do us a favor.
[2690.04 --> 2692.72]  Share this show with a friend or it doesn't have a podcast.
[2692.94 --> 2694.50]  Go into Overcast and favorite it.
[2694.98 --> 2697.24]  And thank you to Fastly, our bandwidth partner.
[2697.60 --> 2699.10]  Head to fastly.com to learn more.
[2699.50 --> 2702.10]  And we move fast to fix things around here at changelog because of Rollbar.
[2702.46 --> 2704.04]  Check them out at rollbar.com.
[2704.28 --> 2706.36]  We're hosted on Leno cloud servers.
[2706.72 --> 2708.32]  Head to leno.com slash changelog.
[2708.40 --> 2709.78]  Check them out and support this show.
[2710.24 --> 2712.20]  Our music is produced by Breakmaster Cylinder.
[2712.60 --> 2715.64]  And you can find more shows just like this at changelog.com.
[2715.84 --> 2716.78]  Thanks for tuning in.
[2716.78 --> 2717.82]  We'll see you next week.
